---
title: "Fortran newsletter: February 2026"
category: newsletter
date: 2026-02-01
author: Jorge Galvez, 
...

# Fortran newsletter: February 2026

Welcome to the February edition of the monthly Fortran newsletter.
The newsletter comes out at the beginning of every month and details
Fortran news from the previous month.

## Community News 

### Talks/Youtube videos 

- [Damian Rouson IWOMP keynote: Fortran is all you need](https://www.youtube.com/watch?v=mwmYiKE1unE) 
- [Damian Rouson talk "Please no more loops" (waiting for an upload)](https://www.youtube.com/watch?v=DKV2Whf4MKg)

### Meetups/cons

- FortranCon2025 happened in November! See the slides from the presentations [here](https://www.youtube.com/watch?v=DKV2Whf4MKg)

### Community lead software 

Fortran users may wish to be aware that licences for Winteracter, the multi-platform Fortran graphics and GUI toolset, can now be requested, via https://www.winteracter.uk/licrequest.php. Winteracter is now wholly non-commercial, so licences are available free of charge. The package continues to be updated. V17.0 was released recently, adding five new compiler/platform combinations, including new versions for ARM64 and Flang.

### Community members 

- [Joe Wallwork](https://github.com/joewallwork), Institute of Computing for Climate Science, University of Cambridge has been awarded a [Computational Abilities Knowledge Exchange (CAKE) fellowship](https://www.cake.ac.uk/ke-fellowships/cohort1#joe-wallwork)! He will be working to further the efforts of Fortran index in 2026. Watch this space for useful improvements! Please see the full blog post for further information. 

#### News

- [Fortran and compiler wizard Ron Green moves to nvidia to join their compiler team](https://www.linkedin.com/posts/captainfortran_in-december-i-departed-intel-to-start-the-activity-7412901494569635842-jVDX?utm_source=share&utm_medium=member_desktop&rcm=ACoAADRETb0BpZR2yE4lAnduNfdPz_FaGi7gUXo)

#### Software releases/New projects 

- [Release of FMSL](https://github.com/sebastian-mutz/fsml), a scientific toolkit consisting of common statistical and machine learning procedures. See the [JOSS paper](https://joss.theoj.org/papers/10.21105/joss.09058) and try it out!
- [New release (v9.2.0) of json-fortran by Jacob Williams](https://github.com/jacobwilliams/json-fortran/releases/tag/9.2.0)
- [METISSE, a Fortran application for single star evolution ](https://joss.theoj.org/papers/10.21105/joss.08817), see the [repo](https://github.com/TeamMETISSE/METISSE)
- [FIATS, an application for functional inference and training](https://joss.theoj.org/papers/10.21105/joss.08785), see the [repo](https://github.com/BerkeleyLab/fiats)
- Release of [LightKrylov](https://github.com/nekStab/LightKrylov)! A modern Fortran package for linear algebra based on Krylov methods. See their accompanying [JOSS paper](https://joss.theoj.org/papers/10.21105/joss.09623)! 

## fortran-lang.org

The website has seen some quality of life upgrades, thanks to everyone that has contributed to make this possible! 

- [#618](https://github.com/fortran-lang/webpage/pull/618)
- [#612](https://github.com/fortran-lang/webpage/pull/612)
- [#611](https://github.com/fortran-lang/webpage/pull/611)
- [#608](https://github.com/fortran-lang/webpage/pull/608)
- [#606](https://github.com/fortran-lang/webpage/pull/606)
- [#603](https://github.com/fortran-lang/webpage/pull/603)

## Fortran Standard Library

New release of stdlib [v0.8.0](https://github.com/fortran-lang/stdlib/releases/tag/v0.8.0)! See the [Github generated changelog here!](https://github.com/fortran-lang/stdlib/compare/v0.7.0...v0.8.0)

Here's a short summary of changes in stdlib:

- Advanced linear algebra: New support for, among others, matrix inversion, QR factorization, Schur decomposition, sparse matrices, and enhanced BLAS/LAPACK intergration.
- New utilities: expanded system interfaces and improved file I/O helpers.
- Modularization of the library and improved CI workflows for better stability. 

Thanks to all (new) contributors who contributed to this release!


## Fortran Package Manager

Current latest release is [v0.12.0](https://github.com/fortran-lang/fpm/releases/tag/v0.12.0)

Version 0.13.0 is underway, keep posted! 

Additionally, the release of [set up fpm v9](https://github.com/marketplace/actions/setup-fpm)

Here's what's new in fpm:

- [#1232](https://github.com/fortran-lang/fpm/pull/1232)
- [#1231](https://github.com/fortran-lang/fpm/pull/1231)
- [#1227](https://github.com/fortran-lang/fpm/pull/1227)
- [#1225](https://github.com/fortran-lang/fpm/pull/1225)
- [#1224](https://github.com/fortran-lang/fpm/pull/1224)
- [#1221](https://github.com/fortran-lang/fpm/pull/1221)
- [#1220](https://github.com/fortran-lang/fpm/pull/1220)
- [Any many more...](https://github.com/fortran-lang/fpm/pulls?q=is%3Apr+is%3Aclosed)

The FPM is still in continuous development and we welcome any testers to find issues, and areas of improvement! Please let us know what you find. 


## Compiler updates:

### LFortran 
- Work continues towards beta quality (expected to work on most codes, but still have bugs)
- Can compile and run LAPACK
- Focus on compiling `fpm`
- 16 releases in 2025
- 130 total contributors
- 4,425 total merged PRs on GitHub since 2022.
### nvfortran 

Release of NVHPC [25.11](https://forums.developer.nvidia.com/t/just-released-hpc-sdk-v25-11/353413)

### Flang 

### gfortran

### amdflang 

### nagfor 

### Intel 

