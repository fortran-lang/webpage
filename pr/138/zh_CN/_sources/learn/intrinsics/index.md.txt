# Fortran Intrinsics

This is a collection of extended descriptions of the Fortran intrinsics
based on the reference document
"[Current F2018 Working Document as of April 2018](http://isotc.iso.org/livelink/livelink?func=ll&objId=19442438&objAction=Open)".
Vendor-specific extensions are not included.

::::{dropdown} Intrinsics
:color: primary

```{toctree}
:maxdepth: 2
array/index
bit/index
character/index
compiler/index
cfi/index
math/index
model/index
numeric/index
parallel/index
state/index
system/index
transform/index
type/index
GNU Free Documentation License <https://www.gnu.org/licenses/old-licenses/fdl-1.2.en.html>
```

::::

## Overview

The standard documents and most vendor-supplied descriptions of
the intrinsics are often very brief and concise to the point of the
functionality of the intrinsics being obscure, particularly to someone
unfamiliar with the procedure.

By describing the procedures here

- in greater detail
- with a working example
- providing links to additional resources
  (including additional documents at fortran-lang.org and related
  discussions in Fortran Discourse)

these documents strive to be a valuable asset for Fortran programmers.

This is a community-driven resource and everyone is encouraged to contribute
to the documents. For contribution guidelines see {ref}`minibooks`
and the following Copyright guidelines.

## See Also

- The [Fortran stdlib](https://stdlib.fortran-lang.org/) project
- [fpm(1)](https://fortran-lang.org/packages/fpm) packages, many of which are general-purpose libraries/modules

Experimental

- [review by procedure ](http://www.urbanjost.altervista.org/SUPPLEMENTS/slidy_byprocedure.html)

- [review by header ](http://www.urbanjost.altervista.org/SUPPLEMENTS/slidy_byheader.html)

- [fman(1)](http://www.urbanjost.altervista.org/SUPPLEMENTS/fman.f90) A self-contained Fortran program that
  lets you view the non-graphical plain ASCII portions of the
  documentation from a terminal interface. Compile the program and
  enter "./fman --help" for directions.

- [man pages](http://www.urbanjost.altervista.org/SUPPLEMENTS/fortran.tgz) A gzipped tar(1) file containing
  early versions of man-pages derived from the markdown documents.

  Typical installation on a Linux platform as an administrator ( but it varies) :

```bash
# as the administrator
cd /usr/share
tar xvfz /tmp/fortran.tgz
cd man
mandb -c
```

then anyone on that plaform can enter commands like

```bash
man sinh.3fortran     # specifically show Fortran sinh(3) documentation
man -k . -s 3fortran  # list all fortran pages
man -s 3fortran --regex '.*' |col -b # show all Fortran intrinsics
```

See man(1) (ie. enter "man man") for more information.

If you can only install the pages on your own ID, try

```bash
# as a user, placing the files in ~/man:
cd
tar xvfz /tmp/fortran.tgz
cd man
mandb -c
export MANPATH="$MANPATH:$HOME/man"
export MANWIDTH=80
```

Still debating whether having to keep the document limited to ANSI
characters is worth-while so these formats can be generated, and
still having issues converting the markdown to the proper formats.

## Text Content Copyrights

Many of the documents presented here are modified versions of man-pages from the
[Fortran Wiki](https://fortranwiki.org)
and as such are available under the terms of the GNU
Free Documentation License [**GFDL**](GNU_Free_Documentation_License.md)
with no invariant sections, front-cover texts, or back-cover texts.

If you contribute to this site by modifying the files marked as GFDL,
you thereby agree to license the contributed material to the public
under the GFDL (version 1.2 or any later version published by the Free
Software Foundation, with no invariant sections, front-cover texts,
or back-cover texts).

If you contribute new material you thereby agree to release it under
the MIT license, and should indicate this by placing MIT on the
specially-formatted last line. For example, change

```text
###### fortran-lang intrinsic descriptions
```

to

```text
###### fortran-lang intrinsic descriptions (License: MIT) @urbanjost
```

Written in [Myst-Markdown](https://myst-parser.readthedocs.io/en/latest/)
