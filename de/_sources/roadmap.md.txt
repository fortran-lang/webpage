# Roadmap <!-- omit in toc -->

This is a snapshot of the Fortran-Lang roadmap, which is a living document.
It is intended to give a general idea of the direction of the Organization, encourage developers to contribute to our projects and seek funding opportunities.
It is not intended to be a commitment to deliver specific features or to prevent Fortran-Lang from doing other things.
The roadmap is a living document, and it will be updated as needed.

## [Fortran Standard Library](https://github.com/fortran-lang/stdlib)

### OS integration: File system

Currently, file system operations such as listing contents of directories, traversing directories, and similar,
are restricted to 3rd party libraries and compiler extensions that are platform-specific and not portable.
This project will entail designing and implementing a cross-platform solution for file system operations.

**Related issues:**

- [stdlib#201](https://github.com/fortran-lang/stdlib/issues/201): File system operations
- [stdlib#220](https://github.com/fortran-lang/stdlib/issues/220): API for file system operations, directory manipulation

**WIP implementation:**

- [stdlib_os](https://github.com/MarDiehl/stdlib_os)

**Expected outcomes:** Implemented an stdlib module that provides cross-platform file-system utilities

### OS integration: Subprocesses

Cross-platform solution to abstract POSIX and Windows API for creating subprocesses.

**Related issues:**

- [stdlib#22](https://github.com/fortran-lang/stdlib/issues/22): Interface to POSIX I/O API
- [stdlib#308](https://github.com/fortran-lang/stdlib/issues/308): Subprocesses and Multiprocessing

**Discourse thread:**

- [Ideas for command module](https://fortran-lang.discourse.group/t/ideas-for-command-module/439)

### Sparse matrices

Implementing a standardized API for procedures to handle (COO and CSR) sparse matrices.
Both non-OO low-level API and OO API should be implemented.

**Related issue**:

- [#38](https://github.com/fortran-lang/stdlib/issues/38)

**WIP implementation**:

- [#189](https://github.com/fortran-lang/stdlib/pull/189)

**Expected outcomes:** Implemented sparse matrix functionality in the `stdlib_linalg` module

## [Fortran Package Manager (fpm)](https://github.com/fortran-lang/fpm)

### Fortran Registry

Fpm currently supports decentralized package dependencies whereby dependencies are specified without a central registry.
A long-term goal for Fortran-Lang is to host a community-supported registry of fpm packages and for fpm to support interfacing with this and other registries to simplify dependency management.

This project idea aims to accomplish a major step towards a central package registry by implementing support in fpm for a locally hosted package registry.
In particular, this project will entail:

- Defining the manifest syntax to use dependencies from a registry
- Implementing support for looking up and loading a (local) registry
- Allowing fpm to manage a local registry by fetching it from a remote registry

**Related issues:**

- [fpm#321](https://github.com/fortran-lang/fpm/issues/321): Implement support for a local registry
- [fpm#35](https://github.com/fortran-lang/fpm/issues/35): Full package registry

**See also:**

- [fpm-registry](https://github.com/fortran-lang/fpm-registry): Prototype central registry
- [fpm-search](https://github.com/urbanjost/fpm-search): fpm app for searching the registry for fpm packages

**Expected outcomes:** Implemented a repository of fpm packages as a service

### Version Constraint Resolution

The current decentralized package system in fpm allows dependencies to be fetched via a git repository URL. As part of this, a git tag or commit can be given to require a specific version of a dependency. There is however no way of specifying version compatibility requirements (_e.g._ `>= 1.0.0, <2.0.0`) and no way to resolve such requirements across a dependency tree.

This project will involve:

- Defining a manifest syntax for version compatibility matching
- Implementing support in fpm for solving a set of version compatibility constraints

A possible approach would be to interface with an existing satisfiability solver such as:

- [libsolv](https://github.com/openSUSE/libsolv):
  interface via `iso_c_binding` as a separate fpm package

**See also:** existing options for version matching syntax:

- [conda](https://docs.conda.io/projects/conda-build/en/latest/resources/package-spec.html#package-match-specifications)
- [npm](https://docs.npmjs.com/about-semantic-versioning/)
- [cargo](https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html)

**Expected outcomes:** Implemented a working version constraint mechanism in fpm

### fpm-ize the Fortran ecosystem

Research the Fortran library and application ecosystem (on GitHub and beyond)
and collaborate with package maintainers on making their package fpm-compatible.

**Expected outcomes:** Bring popular Fortran, C and C++ packages to the fpm ecosystem.

### Extended Testing Support

The aim of this project is to create a manifest specification to provide defaults to executable targets in fpm projects.
Information can be passed as environment variables, command-line arguments or as a runner.
Desired features include:

- Programs should have a way to find resources of which the relative position within the project source directory is known.
- The current binary directory to access other targets within a project.
- Default runners like `mpirun`/`cafrun` or scripts from test frameworks should be usable to launch programs.
- A general syntax to define environment variables and command-line arguments should be defined.

Some features should be implemented directly in fpm, while more elaborated functionality could be implemented in a separate fpm package as an official Fortran-lang fpm package.

**Related issues:**

- [fpm#179](https://github.com/fortran-lang/fpm/issues/179): Testing with fpm test

**Related discussions:**

- [fpm#328](https://github.com/fortran-lang/fpm/discussions/328): Example which requires external data

**Expected outcomes:** fpm has broader and deeper testing functionality

### Source Code Distribution with Foreign Build Systems

The aim of this project is to enable fpm to create source code distributions of itself that can be bootstrapped without fpm.
Desired features include:

- Allow fpm to generate source code distributions with non-fpm build systems.
- Generated source code distribution should allow building fpm project without fpm, git or internet access.
- Potential third-party build systems are CMake and Meson.
- Allow easier distribution and packaging of fpm via various packaging ecosystems.

**Related issues:**

- [fpm#69](https://github.com/fortran-lang/fpm/issues/69): Have CMake and Make backends
- [fpm#70](https://github.com/fortran-lang/fpm/issues/70): Have a Conda backend

**Expected outcomes:** fpm can generate source code distributions of packages that can be build using CMake and/or Meson.

## [Modern Fortran for Visual Studio Code](https://github.com/fortran-lang/vscode-fortran-support)

### Integration with the Fortran Package Manager and CMake

The aim of this project is to integrate the Fortran Package Manager and CMake into the Modern Fortran Visual Studio Code extension. The integration should allow for building of a project with fpm or CMake through VS Code but also the
accurate configuration of the linter and the Language Server.

**Related issues:**

- [vscode-fortran-support#471](https://github.com/fortran-lang/vscode-fortran-support/issues/471): Add support for fpm
- [vscode-fortran-support#133](https://github.com/fortran-lang/vscode-fortran-support/issues/133): Linter setup via CMake
- [fpm#705](https://github.com/fortran-lang/fpm/issues/705): FPM pip installation

**Related discussions:**

- [fpm#768](https://github.com/fortran-lang/fpm/discussions/768): FPM integration discussion

**Expected outcomes:**

- fpm and CMake are integrated into the Modern Fortran Visual Studio Code extension.
- User is able to build, run and debug fpm project.
- The Modern Fortran extension is able to automatically configure the linter and the Language Server based on the fpm and CMake configurations.
- Easy installation of fpm via pip.

### Sphinx Documentation

The aim of the project is to write the documentation webpage for Modern Fortran
using Sphinx and MyST Markdown. The documentation should include:

- Installation instructions
- Available settings and how to set them
- Frequently Asked Questions and their answers

**Expected outcomes:** Modern Fortran for Visual Studio Code extension has a documentation webpage.

**Related issues:**

- [vscode-fortran-support#472](https://github.com/fortran-lang/vscode-fortran-support/issues/472): Add Walkthroughs

### Extension Localizations

The aim of the project is to localize the Modern Fortran for Visual Studio Code extension into other languages. There is already extensive documentation on how to localize Visual Studio Code extensions, and we already have tools in place to help with the process, see for example [fortran-lang.org](https://fortran-lang.org).

**Related issues:**

- [vscode-fortran-support#616](https://github.com/fortran-lang/vscode-fortran-support/issues/616): Add localization support

**Expected outcomes:** Modern Fortran for Visual Studio Code extension is localized into other languages.
