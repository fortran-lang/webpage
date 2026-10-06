# Fortran 95 language features

:::{toctree}
:maxdepth: 2
:hidden:
Language elements <language_elements>
Expressions and assignments <expressions_and_assignments>
Control statements <control_statements>
Program units and procedures <program_units_and_procedures>
Array handling <array_handling>
Pointers <pointers>
Intrinsic procedures <intrinsic_procedures>
Data transfer <data_transfer>
Operations on external files <operations_on_external_files>
Bibliography <bibliography>
:::

This is an overview of **Fortran 95 language features** which is based
upon the standards document[^iso_1539_1997] which has been replaced by
a newer version.[^iso_1539_2023] Included are the additional features of
TR-15581:Enhanced Data Type Facilities, which have been universally
implemented. Old features that have been superseded by new ones are not
described few of those historic features are used in modern programs
although most have been retained in the language to maintain
[backward_compatibility](https://en.wikipedia.org/wiki/Backward_compatibility).
The additional features of subsequent standards, up to Fortran 2023, are
described in the Fortran 2023 standard document, ISO/IEC
1539-1:2023.[^iso_1539_2023] Some of its new features are still being
implemented in compilers.[^Fortran_plus] Details can also be found in a
range of textbooks, for instance[^OOPvF][^OOPC][^Chapman] and see the
list at Fortran Resources.[^Fortran_plus_18] Sources for the description
in the sections below can be found in the standards
documents,[^iso_1539_2023] textbooks[^OOPvF][^OOPC][^Chapman] as well as
the
[bibliography](bibliography).

The booklet is based on Wikipedia's article
[Fortran 95 language
features](https://en.wikipedia.org/wiki/Fortran_95_language_features),
last edit by February 25, 2025 16:08 UTC.

[^mfe]:
    Metcalf, Michael; Reid, John; Cohen, Malcolm; Bader, Reinhold (2023).
    _Modern Fortran Explained._ Numerical Mathematics and Scientific Computation.
    Oxford University Press.
    [ISBN 978-0-19-887657-1](https://en.wikipedia.org/wiki/Special:BookSources/978-0-19-887657-1).

[^iso_1539_1997]:
    [ISO/IEC 1539-1:1997](https://www.iso.org/standard/26933.html)

[^iso_1539_2023]:
    [ISO/IEC 1539-1:2023](https://www.iso.org/standard/82170.html)

[^Fortran_plus]:
    [Fortranplus | Fortran information](http://www.fortranplus.co.uk/fortran-information/)

[^OOPvF]:
    ["Features of Programming Languages"](https://doi.org/10.1017/cbo9780511530111.005),
    Object-Oriented Programming via Fortran 90/95, Cambridge University Press,
    pp. 56–118.

[^OOPC]:
    ["Object-Oriented Programming Concepts"](https://doi.org/10.1017/cbo9780511530111.004),
    Object-Oriented Programming via Fortran 90/95, Cambridge University Press,
    pp. 36–55

[^Chapman]:
    Chapman, Stephen J. (2004).
    [Fortran 90/95 for scientists and engineers](https://www.worldcat.org/title/ocm52465017)
    (2nd ed.). Boston: McGraw-Hill Higher Education. ISBN 978-0-07-282575-6.

[^Fortran_plus_18]:
    [Fortranplus | Fortran information](http://www.fortranplus.co.uk/fortran-information/),
    p. 18
