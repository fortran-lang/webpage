# Minimal makefile for Sphinx documentation
# You can set these variables from the command line, and also
# from the environment .

LANGUAGES     ?= en bn cs de es fr ja nl pl pt ru zh_CN
SPHINXINTL    ?= sphinx-intl
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
LOCALEDIR     ?= locale

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

dirhtml:
	@python3 build.py $(LANGUAGES)

gettext:
	@python3 intl.py $(filter-out en,$(LANGUAGES))
