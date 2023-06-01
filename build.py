"""
Script for conveniently building the documentation in all supported languages.

Run this script with:

.. code::

    python3 build.py


You can also pass the language as an argument:

.. code::

    python3 build.py en de


The first language will be handled as the default language.
"""
# pylint: disable=invalid-name,import-error

import sys
import subprocess
from pathlib import Path
from typing import List, Dict
import yaml

root: Path = Path(__file__).parent
"""Make sure to run this script from the root of the documenation repository."""

outdir: Path = root / "build" / "html"
"""Directory to build the documentation to."""

srcdir: Path = root / "source"
"""Directory containing the Sphinx configuration file."""

all_redirects: Dict[str, str]
"""All redirects from the original site without language component."""

with open(root / "data" / "redirects.yml", "r", encoding="utf-8") as fd:
    all_redirects = yaml.safe_load(fd)

all_languages: List[str]
"""List of currently supported languages, taken from ``doc/src/_static/languages.yml``."""

with open(root / "data" / "languages.yml", "r", encoding="utf-8") as fd:
    all_languages = list(yaml.safe_load(fd).values())

template = """
<!DOCTYPE HTML>
 
<meta charset="UTF-8">
<meta http-equiv="refresh" content="1; url={0}">
 
<script>
  window.location.href = "{0}"
</script>
 
<title>Page Redirection</title>
 
If you are not redirected automatically, follow the <a href='{0}'>link</a>.
"""


def build_docs(language: str, isroot: bool) -> None:
    """
    Build the documentation for a single language.

    Parameters
    ----------
    language : str
        The language to build the documentation for.
    """

    subprocess.run(
        [
            "sphinx-build",
            "-b",
            "dirhtml",
            str(srcdir),
            str(outdir) if isroot else str(outdir / language),
            f"-Dlanguage={language}",
        ],
        cwd=root,
        check=True,
    )


def build_redirects(redirects: Dict[str, str], language: str) -> None:
    """
    Build the redirects for a single language.

    Parameters
    ----------
    redirects : Dict[str, str]
        Page redirects to build.
    language : str
        The language to build the redirects for.
    """
    pass
    # for source, target in redirects.items():
    #     source_path = outdir / source
    #     redirect = template.format(target.format(language))
    #     if not source_path.parent.exists():
    #         source_path.parent.mkdir(parents=True)
    #     with open(source_path, "w", encoding="utf-8") as fp:
    #         fp.write(redirect)


def build_all(redirects: Dict[str, str], languages: List[str]) -> None:
    """
    Build the documentation for all languages.

    Parameters
    ----------
    redirects : Dict[str, str]
        Page redirects to build.
    languages : List[str]
        List of languages to build the documentation for.
    """

    for language in languages:
        build_docs(language, language == languages[0])

    build_redirects(redirects, languages[0])


if __name__ == "__main__":

    build_all(all_redirects, sys.argv[1:] if len(sys.argv) > 1 else all_languages)

    print()
    print("Preview the fortran-lang.org site using")
    print()
    print(f'    python3 -m http.server -d "{outdir}"')
    print()
