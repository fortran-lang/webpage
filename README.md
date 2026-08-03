# Fortran-lang.org Website

## Contributing

- [contributing](https://fortran-lang.org/community/contributing/):
  getting started and general guidance on contributing to <https://fortran-lang.org>

- [minibooks](https://fortran-lang.org/community/minibooks/):
  how to write and structure a mini-book tutorial for the [Learn](https://fortran-lang.org/learn) section

- [packages](https://fortran-lang.org/community/packages/):
  adding an entry to the [Package index](https://fortran-lang.org/packages)

## Package search utility
Fortran-lang's' `package-search` application finds and reports information about
packages listed in `data/package_index.yml`.  To build and run the application with
the Fortran Package Manager (`fpm`) and a Fortran compiler installed, run a command
like the following in a terminal window:
```
fpm run --compiler flang --profile release -- --find "partial-differential"
```
which shoud return each package listing that contains the string "partial-differential".

To verify a working build of `package-search`, run the test suite with a command like
```
fpm test --compiler flang --profile release
```

<div align="center">
Platforms Tested
</div>

Vendor  |Compiler  |Version(s) Tested    |OS    |Recommended `--flag` argument
--------|----------|---------------------|------|---------------------------------------------------
GCC     |`gfortran`|13-17                |macOS | `-ffree-line-length-none` for version 13
LLVM    |`flang`   |23                   |macOS | `-O3 -mmlir -allow-assumed-rank` for version 19
NAG     |`nagfor`  |7.2 Build 7238       |Linux | `-fpp -O3 -coarray`
Intel   |`ifx`     |2026.1.0 20260617    |Linux | `-fpp -O3 -coarray`
LFortran|`lfortran`|0.64.0-157-g1e0305cfd|Linux | `--cpp --realloc-lhs-arrays --separate-compilation`

## Website Setup

### Build fortran-lang.org site (Sphinx Version)

This assumes that you already have a recent version of python.
For example on Ubuntu 20.04, do:

To install the dependencies of this project, use the command:

```
pip3 install --user -r requirements.txt
```

Local builds also require the GNU Fortran compiler `gfortran`.
For example on Ubuntu you can install it with:
```sh
sudo apt install gfortran
```
To install sphinx (if system is not able to recognize sphinx-build after installing requirements):

First check:
```sh
sphinx-build --version
```

if not recognized then run:
```sh
pip install -U sphinx
```

Build the site by invoking
```sh
python3 build.py
```

The website will be built in `build/html` and can be previewed by starting a webserver and opening the page with a browser (_e.g._ firefox, chromium or similar):
```sh
python3 -m http.server -d build/html
```

By default all languages will be built.
To limit the build to a single language subtree, _i.e._ English, use
```sh
python3 build.py en
```

After adding a new entry to package index, run the github action _fortran_packages_ before building the sphinx build.

### Activating the pre-commit hooks for Ruff:

This assumes that you already have a cloned the main branch of this repository.
Steps to activate the pre-commit hooks are:

1. Make sure that you have installed all the dependencies of the repository.

```sh
pip3 install --user -r requirements.txt
```

2. Activate the pre-commit hooks:

```sh
pre-commit install
```

Now, the precommit hooks have been successfully been installed into your clone.

#### Steps to debug/resolve issues which prevent the commit due to pre-commit hooks:

If linting causes the issues in commiting to the repo, and it seems mandatory to
`skip` the pre-commit hooks use:
```sh
git commit -m"my commit" --no-verify
```

### Translating via weblate

Translations can be contributed via [weblate](https://hosted.weblate.org/projects/fortran-lang/webpage/).

[![Translation status](https://hosted.weblate.org/widgets/fortran-lang/-/webpage/horizontal-auto.svg)](https://hosted.weblate.org/engage/fortran-lang/)

### Update or add translations

The documentation uses the
[sphinx-intl](https://sphinx-intl.readthedocs.io/en/master/quickstart.html)
utility to generate websites for multiple languages.
It generates `*.po` files,
which contain the original sentences and a placeholder for translations.

To update translations run

```sh
python3 intl.py
```

if you only want to update a single translation add `LANGUAGES=de` to the command.
This command will generate the message catalog (`*.pot`) and update the `*.po` files in the _locale_ directory of the respective translations.
Then edit the `*.po` files,
e.g. `locale/de/LC_MESSAGES/index.po`.
In the `*.po` files are paragraphs like

```po
#: ../../pages/index.md:16
msgid "Package manager and build system for Fortran"
msgstr ""
```

The first line describes the file and line where to find the original text.

The second line is the original text.
**Don't edit this line, edit the original document instead**.

The third line is meant for the translation.

To continue a long string in another line,
simply close the string in the current line with `"`
and open another one in the line underneath. E.g.

```po
msgstr "This is "
"one string"
```

_don't forget a space between 'is' and 'one'_

After adding or updating translations
build the documentation as described above.

## License

This project is free software: you can redistribute it and/or modify it under the terms of the [MIT license](LICENSE).

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an _as is_ basis, without warranties or conditions of any kind, either express or implied. See the License for the specific language governing permissions and limitations under the License.

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in this repository by you, shall be licensed as above, without any additional terms or conditions.
