from sphinx.directives.code import *
import urllib.parse
from docutils import nodes


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
        return [literal]
        


def setup(app):
    app.add_directive('play-code-block', PlayCodeBlock)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
