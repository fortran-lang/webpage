# Fortran-lang history

## Creation

The effort to build a new community around Fortran started at the beginning of 2020
and was initially led by Ondřej Čertík [[1]][blog-ondrej] and Milan Curcic [[2]][blog-milan].
Starting in several discussions around ambitious proposals for the Fortran Standards
Committee, the Fortran Standard Library (`stdlib`) [[3]][issue-stdlib], the Fortran
Package Manager (`fpm`) [[4]][issue-fpm] and the [`fortran-lang.org`][webpage-orig]
webpage with new logo [[5]][issue-logo] were created.
With the new webpage and projects attracting more contributors, the Fortran-lang discourse
was created to provide a place for general discussions around all the things Fortran,
announcing newly started projects, getting help, etc.
Since its creation the Fortran-lang community was joined by hundreds of contributors.

[blog-ondrej]: https://ondrejcertik.com/blog/2021/03/resurrecting-fortran/
[blog-milan]: https://medium.com/modern-fortran/first-year-of-fortran-lang-d8796bfa0067
[issue-fpm]: https://github.com/j3-fortran/fortran_proposals/issues/55
[issue-stdlib]: https://github.com/j3-fortran/fortran_proposals/issues/104
[issue-logo]: https://github.com/j3-fortran/fortran_proposals/issues/47
[webpage-orig]: https://web.archive.org/web/20200504000648/https://fortran-lang.org/

## Incubator J3 repo

## The Fortran Standard Library `stdlib`

Created in the late 2019 the Fortran Standard Library provides
a community driven and agreed upon de facto "standard" library for Fortran.
The library is a collection of modules that provide a wide range of
functionality, including: containers, sorting, searching, linear algebra,
unities, fast Fourier transforms, and more.

Find out more about `stdlib` on our [website](https://stdlib.fortran-lang.org/)
and on [GitHub](https://github.com/fortran-lang/stdlib).

## The Fortran Package Manager `fpm`

Fortran Package Manager (fpm) is a package manager and build system for Fortran.
Its key goal is to improve the user experience of Fortran programmers.
It does so by making it easier to build your Fortran program or library, run the
executables, tests, and examples, and distribute it as a dependency to other
Fortran projects.
Fpm's user interface is modeled after [Rust's Cargo](https://doc.rust-lang.org/cargo/),
so if you're familiar with that tool, you will feel at home with fpm.
Fpm's long term vision is to nurture and grow the ecosystem of modern Fortran
applications and libraries.

## Fortran Discourse

## Fortran Package Index

## Project migration to Fortran-lang

Over time crucial projects to the Fortran community were migrated to the
Fortran-lang organization to allow for community collaboration and to ensure
long-term sustainability of the projects.

### fftpack

### minipack

### test-drive

### vscode-fortran-support

<!-- Migration date: 22-04-2022 -->

Modern Fortran for Visual Studio Code is feature-rich Visual extension
for Fortran originally created by
Miguel Carvajal and maintained by Giannis Nikiteas.
The extension migrated in early 2022 to the Fortran-lang organization
to improve integration with other Fortran-lang projects such as `fpm`
and allow for easier community collaboration.

Find out more about Modern Fortran for Visual Studio Code on
[VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=fortran-lang.linter-gfortran)
and on [GitHub](httos://github.com/fortran-lang/vscode-fortran-support).

### fortls

<!-- Migration date: 28-11-2022 -->

`fortls` is a Fortran language server created by Giannis Nikiteas
in late 2019. The project started as a fork of the
archived project `fortran-language-server` but quickly diverged from it
both in terms of features and codebase. The project migrated to the
Fortran-lang organization in late 2022 to allow for easier community
collaboration.

Find out more about `fortls` on our [website](https://fortls.fortran-lang.org/)
and on [GitHub](https://github.com/fortran-lang/fortls).

## Fortran Publication

In April 2022, members of the Fortran-lang community published a paper in
Computing in Science & Engineering titled [_The State of Fortran_][pub-state-of-fortran]
providing an overview of the language and its ecosystem.
The paper focused on the ongoing efforts
of developing the Fortran standard library ([`stdlib`][webpage-stdlib])
and the Fortran package manager ([`fpm`][webpage-fpm]),
fostering a friendly and welcoming community online ([`Fortran-lang Discourse`][discourse]),
improving compiler support and language feature development.

[pub-state-of-fortran]: https://ieeexplore.ieee.org/document/9736688
[discourse]: https://fortran-lang.discourse.group/
[webpage-fpm]: https://fpm.fortran-lang.org/
[webpage-stdlib]: https://stdlib.fortran-lang.org/

## Conferences and Events
