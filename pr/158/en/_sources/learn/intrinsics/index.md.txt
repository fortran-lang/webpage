# Fortran Intrinsics

This is a collection of extended descriptions of the Fortran intrinsics
based on the reference document
"[Current F2018 Working Document as of April 2018](http://isotc.iso.org/livelink/livelink?func=ll&objId=19442438&objAction=Open)".
Vendor-specific extensions are not included.

::::{dropdown} Intrinsics
:color: primary

```{toctree}
:maxdepth: 2
array
bit
character
compiler
cfi
math
model
numeric
parallel
state
system
transform
type
GNU Free Documentation License <https://www.gnu.org/licenses/old-licenses/fdl-1.2.en.html>

::::

## Overview

These documents expand on the intrinsic descriptions in the Fortran standard
by providing 

- expanded descriptions including the purpose and uses of the procedures,
  instead of just the technical specifications.
- tested working examples
- links to additional resources

This is a community-driven resource and everyone is encouraged to
contribute to the documents. For contribution guidelines see [minibook
guide](/community/minibooks) and the following Copyright guidelines.

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
_fortran-lang intrinsic descriptions_
```

to

```text
_fortran-lang intrinsic descriptions (License: MIT) @urbanjost_
```

Written in [Myst-Markdown](https://myst-parser.readthedocs.io/en/latest/)
