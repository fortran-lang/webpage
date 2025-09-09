from sphinx.directives.code import CodeBlock, dedent_lines, container_wrapper, logger
import urllib.parse
from sphinx.util._lines import parse_line_num_spec
from docutils import nodes
import subprocess
import hashlib
import os


comp_error = ["<ERROR>","Error","app/main.f90","<h1>Bad Request</h1>"]


class PlayCodeBlock(CodeBlock):

    def compile_and_execute_fortran(self,fortran_code):
        code_hash = hashlib.md5(fortran_code.encode('utf-8')).hexdigest()
        cache_filename = f"build/fortran_output_{code_hash}.txt"
        filename=f"build/code_{code_hash}.f90"

        # Check if the output is already cached
        if os.path.exists(cache_filename):
            with open(cache_filename, "r") as f:
                return f.read()

        with open(filename, "w") as f:
            f.write(fortran_code)

        compile_command = ["gfortran", filename, "-o", f"./build/{code_hash}.out"]
        compile_result = subprocess.run(compile_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        with open(cache_filename, "w") as f:
            
            if compile_result.returncode == 0:
                print("Compilation successful!")
                
                execute_command = [f"./build/{code_hash}.out"]
                execute_result = subprocess.run(execute_command, input="", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                if execute_result.returncode == 0:
                    print("Execution successful!")
                    print(execute_result.stdout)
                    f.write(str(execute_result.stdout))
                    return execute_result.stdout
                else:
                    print("Execution failed.")
                    print(execute_result.stderr)
                    f.write(str(execute_result.stderr))
                    return execute_result.stderr
            else:
                print("Compilation failed.")
                print(compile_result.stderr)
                f.write(str(compile_result.stderr))
                return compile_result.stderr

    def run(self):
        document = self.state.document
        code = '\n'.join(self.content)
        location = self.state_machine.get_source_and_line(self.lineno)
        linespec = self.options.get('emphasize-lines')
        if linespec:
            try:
                nlines = len(self.content)
                hl_lines = parse_line_num_spec(linespec, nlines)
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
        caption = f"<a href='https://play.fortran-lang.org/?code={urllib.parse.quote(code)}' target='_blank'>Fortran Playground</a>"
        try:
            literal = container_wrapper(self, literal, caption)
        except ValueError as exc:
            return [document.reporter.warning(exc, line=self.lineno)]
        if "end program" not in code:
            code = code+"\nend program"
        resp = self.compile_and_execute_fortran(code)
        if any(i in str(resp) for i in comp_error):
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

