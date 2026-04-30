---
sd_hide_title: true
---

# Packages

:::{div} sd-text-center sd-fs-2 sd-font-weight-bold sd-text-primary
Fortran Packages
:::

:::{div} sd-text-center sd-fs-3
A rich ecosystem of high-performance code
:::

:::{div} sd-fs-3 sd-font-weight-bold sd-text-primary
Find a Package
:::

<form class="package-search-form" action="../search/index.html" method="get"> <input type="search" name="q" id="search-input" class="package-search-input" placeholder="Search for a package" aria-label="Search" autocomplete="off"></form>

:::::{grid} 2
:gutter: 3

::::{grid-item-card}
:shadow: none

:::{div} sd-fs-3
Package index
:::

:::{div} sd-fs-6
The fortran-lang package index is community-maintained and lists open source Fortran-related projects. This includes large-scale scientific applications, function libraries, Fortran interfaces, and developer tools.<br>
See [here](../community/packages/) for how to get your project listed. <br>
Use the box above to search the package index by keyword, package name, or author username.
:::

::::

::::{grid-item-card}
:shadow: none

:::{div} sd-fs-3
Featured topics
:::

:::{jinja} fortran_index
{% for j in tags %}
<a href='{{"../search/index.html?q="+j}}'>{{j}},</a>{% endfor %}
:::

::::

:::::

:::{div} sd-fs-3 sd-font-weight-bold sd-text-primary
Browse Packages by Category
:::

## [Data types and containers](../categories/data-types)

Libraries for advanced data types and container classes

## [Interface libraries](../categories/interfaces)

Libraries that interface with other systems, languages, or devices

## [Libraries](../categories/libraries)

Fortran libraries for general programming tasks

## [Input, output and parsing](../categories/io)

Libraries for reading, writing and parsing files and inputs

## [Graphics, plotting and user interfaces](../categories/graphics)

Libraries for plotting data, handling images and generating user interfaces

## [Examples and templates](../categories/examples)

Demonstration codes and templates for Fortran

## [Numerical projects](../categories/numerical)

Fortran libraries for linear algebra, optimization, root-finding etc.

## [Programming utilities](../categories/programming)

Error handling, logging, documentation and testing

## [Characters and strings](../categories/strings)

Libraries for manipulating characters and strings

## [Scientific Codes](../categories/scientific)

Applications and libraries for applied mathematical and scientific problems

See [package index guidelines](../community/packages) for how to get your project listed.

:::{toctree}
:hidden:
categories/data-types
categories/interfaces
categories/libraries
categories/io
categories/graphics
categories/examples
categories/numerical
categories/programming
categories/strings
categories/scientific
:::
