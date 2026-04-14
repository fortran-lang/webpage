# Putting Fortran’s object-related features to practical use

:::{toctree}
:maxdepth: 2
:hidden:
Object-based programming techniques <object_based_programming_techniques>
Object-oriented programming techniques <object_oriented_programming_techniques>
Performance and ease of use <performance_and_ease_of_use>
:::

This article by the late Reinhold Bader (1966-2024)
describes how advanced Fortran language features can be
applied toward object-based and object-oriented programming techniques.
These are, of course, to a significant extent a matter of taste,
personal style and possibly overarching program design considerations,
so should be taken with a pinch of salt.

Language features from Fortran 95 and later will be used; those from
Fortran 2003 and later will also be shortly described. They are
explained in more detail in e.g., Metcalf, Reid, Cohen and Bader.[^mfe]
See also [Fortran 95 language
features](https://en.wikipedia.org/wiki/Fortran_95_language_features) for
the language's fundamentals; the prerequisite for understanding this article
is that features explained there are well understood.

Boldface will be used where term definitions are introduced. They are
additionally annotated by "(not a Fortran term)" or similar if the term
is not used in the Fortran standard itself, but is in general use in the
technical literature.

Compilable and runnable example code is available from an external
[Github repository](https://github.com/reinh-bader/object_fortran).

[^mfe]:
    Metcalf, Michael; Reid, John; Cohen, Malcolm; Bader, Reinhold (2023).
    _Modern Fortran Explained._ Numerical Mathematics and Scientific Computation.
    Oxford University Press.
    [ISBN 978-0-19-887657-1](https://en.wikipedia.org/wiki/Special:BookSources/978-0-19-887657-1).
