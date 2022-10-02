"""
Script for conveniently updating the translation files.

Run this script with:

.. code::

    python3 intl.py


You can also pass the language code as an argument:

.. code::

    python3 intl.py de


Do not pass the default language code as an argument.
"""
# pylint: disable=invalid-name,import-error

import sys
import subprocess
from pathlib import Path
from typing import List
import yaml

root = Path(__file__).parent
"""Make sure to run this script from the root of the documenation repository."""

outdir = root / "build" / "gettext"
"""Directory where the ``gettext`` translation files are stored."""

srcdir = root / "source"
"""Path to the source directory."""

localedir = root / "locale"
"""Path to the locale directory."""

all_languages: List[str]
"""
List of currently supported languages, taken from ``_data/languages.yml``.

To support a new language add its `language code`_ to the list.

.. _language code: https://www.sphinx-doc.org/en/master/usage/configuration.html#intl-options
"""

with open(root / "data" / "languages.yml", "r", encoding="utf-8") as fd:
    all_languages = list(yaml.safe_load(fd).values())


def intl_gettext() -> None:
    """
    Update the ``gettext`` translation files.
    """

    subprocess.run(
        ["sphinx-build", "-b", "gettext", srcdir, outdir],
        cwd=root,
        check=True,
    )


def intl_update(language: str) -> None:
    """
    Update a translation file.

    Parameters
    ----------
    language : str
        Language to update.
    """

    subprocess.run(
        ["sphinx-intl", "update", "-l", language, "-d", localedir, "-p", outdir, "-w", "80"],
        cwd=root,
        check=True,
    )


def intl_all(languages: List[str]) -> None:
    """
    Update all translation files.

    Parameters
    ----------
    languages : List[str]
        List of languages to update.
    """

    intl_gettext()
    intl_update(",".join(languages))


if __name__ == "__main__":

    intl_all(sys.argv[1:] if len(sys.argv) > 1 else all_languages[1:])

    print()
    print("Please commit the changes to the translation files if necessary.")
    print()
    print(f'    git add "{localedir}"')
    print()
