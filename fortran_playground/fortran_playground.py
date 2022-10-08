from sphinx.directives.code import *
import urllib.parse
import requests
from requests.structures import CaseInsensitiveDict
from docutils import nodes

url = "https://play-api.fortran-lang.org/run"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"
data = """{"code":"%s","programInput":"","libs":[]}"""
comp_error = [b"<ERROR>",b"Error",b"app/main.f90",b"<h1>Bad Request</h1>"]


class PlayCodeBlock(CodeBlock):

    def run(self):
        document = self.state.document
        code = '\n'.join(self.content)
        location = self.state_machine.get_source_and_line(self.lineno)
        linespec = self.options.get('emphasize-lines')
        if linespec:
            try:
                nlines = len(self.content)
                hl_lines = parselinenos(linespec, nlines)
                if any(i >= nlines for i in hl_lines):
                    logger.warning(__('line number spec is out of range(1-%d): %r') %
                                   (nlines, self.options['emphasize-lines']),
                                   location=location)

                hl_lines = [x + 1 for x in hl_lines if x < nlines]
            except ValueError as err:
                return [document.reporter.warning(err, line=self.lineno)]
        else:
            hl_lines = None

        if 'dedent' in self.options:
            location = self.state_machine.get_source_and_line(self.lineno)
            lines = code.splitlines(True)
            lines = dedent_lines(lines, self.options['dedent'], location=location)
            code = ''.join(lines)

        literal: Element = nodes.literal_block(code, code)
        if 'linenos' in self.options or 'lineno-start' in self.options:
            literal['linenos'] = True
        literal['classes'] += self.options.get('class', [])
        literal['force'] = 'force' in self.options
        if self.arguments:
            # highlight language specified
            literal['language'] = self.arguments[0]
        else:
            # no highlight language specified.  Then this directive refers the current
            # highlight setting via ``highlight`` directive or ``highlight_language``
            # configuration.
            literal['language'] = self.env.temp_data.get('highlight_language',
                                                         self.config.highlight_language)
        extra_args = literal['highlight_args'] = {}
        if hl_lines is not None:
            extra_args['hl_lines'] = hl_lines
        if 'lineno-start' in self.options:
            extra_args['linenostart'] = self.options['lineno-start']
        self.set_source_info(literal)
        caption = "<a href='https://play.fortran-lang.org/?code="+urllib.parse.quote(text)+"' target='_blank'>Fortran Playground</a>"
        if caption:
            try:
                literal = container_wrapper(self, literal, caption)
            except ValueError as exc:
                return [document.reporter.warning(exc, line=self.lineno)]
        resp = requests.post(url, headers=headers, data=data%clean(code))
        #print(resp.content)
        #print([i in resp.content  for i in comp_error])
        if any(i in resp.content  for i in comp_error):
            #print("original")
            return [*super().run()]
        else:
            #print("with link")
            return [literal]
        


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