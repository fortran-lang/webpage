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

::::

## Overview

The standard documents and most vendor-supplied descriptions of the
intrinsics are often very brief and concise to the point where the
functionality of the intrinsics becomes obscure, particularly to someone
unfamiliar with the procedure.

By describing the procedures here

- in greater detail
- with a working example
- providing links to additional resources
  (including additional documents at fortran-lang.org and related
  discussions in Fortran Discourse)

these documents strive to clarify the intrinsics for Fortran programmers.

This is a community-driven resource and everyone is encouraged to contribute
to the documents. For contribution guidelines see {ref}`minibooks`
and the following Copyright guidelines.

## See Also

- The [Fortran stdlib](https://stdlib.fortran-lang.org/) project

- [fpm(1)](https://fortran-lang.org/packages/fpm) packages, many of
  which are general-purpose libraries/modules

- [M_intrinsics](https://github.com/urbanjost/M_intrinsics) a related project
  to leverage the descriptions here to generate man-pages and an OS-agnostic CLI
  (Command Line Interface) program. This includes a tar(1) and zip(1)
  file of man-pages and a self-contained Fortran program that lets you
  view the non-graphical plain ASCII portions of the documentation from
  a terminal interface.

## Text Content Copyrights

Many of the documents presented here are modified versions of
man-pages from the [Fortran Wiki](https://fortranwiki.org) and as such
are available under the terms of the GNU Free Documentation License
[**GFDL**](GNU_Free_Documentation_License.md) with no invariant sections,
front-cover texts, or back-cover texts.

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
