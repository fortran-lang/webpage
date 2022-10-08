from sphinx.directives.code import *
import urllib.parse
import requests
from requests.structures import CaseInsensitiveDict
from docutils import nodes

url = "https://play-api.fortran-lang.org/run"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"
data = """
{"code":"%s","programInput":"","libs":[]}
"""
class PlayCodeBlock(CodeBlock):

    def run(self):
        document = self.state.document
        text = '\n'.join(self.content)
        literal: Element = nodes.literal_block(text, text)
        caption = "<a href='https://play.fortran-lang.org/?code="+urllib.parse.quote(text)+"' target='_blank'>Fortran Playground</a>"
        if caption:
            try:
                literal = container_wrapper(self, literal, caption)
            except ValueError as exc:
                return [document.reporter.warning(exc, line=self.lineno)]
        
        resp = requests.post(url, headers=headers, data=data%clean(text))
        print(resp.content)
        if "<ERROR>" not in resp.content:
            return [literal]
        else:
            return [*super().run()]
        


def setup(app):
    app.add_directive('play-code-block', PlayCodeBlock)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

def clean(s):
    s = s.replace("\t", "\\t")
    s = s.replace("\n", "\\n")
    return s