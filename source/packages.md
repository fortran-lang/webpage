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

<form class="bd-search d-flex align-items-center" align="center" action="../search/index.html" method="get">  <input type="search" class="form-control" name="q" id="search-input" placeholder="Search for a package" aria-label="Search" autocomplete="off" style='margin: auto;text-align: center;width:40em;'> </form>

:::::{grid} 2

::::{grid-item-card}
:shadow: none

:::{div} sd-fs-3
Package index
:::

:::{div} sd-fs-6
The fortran-lang package index is community-maintained and lists open source Fortran-related projects.This includes large-scale scientific applications,function libraries, Fortran interfaces, and developer tools.<br>
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

## [Data types and containers](../packages/data-types)

Libraries for advanced data types and container classes

## [Interface libraries](../packages/interfaces)

Libraries that interface with other systems, languages, or devices

## [Libraries](../packages/libraries)

Fortran libraries for general programming tasks

## [Input, output and parsing](../packages/io)

Libraries for reading, writing and parsing files and inputs

## [Graphics, plotting and user interfaces](../packages/graphics)

Libraries for plotting data, handling images and generating user interfaces

## [Examples and templates](../packages/examples)

Demonstration codes and templates for Fortran

## [Numerical projects](../packages/numerical)

Fortran libraries for linear algebra, optimization, root-finding etc.

## [Programming utilities](../packages/programming)

Error handling, logging, documentation and testing

## [Characters and strings](../packages/strings)

Libraries for manipulating characters and strings

## [Scientific Codes](../packages/scientific)

Applications and libraries for applied mathematical and scientific problems

See [package index guidelines](../community/packages) for how to get your project listed.

:::{toctree}
:hidden:
packages/data-types
packages/interfaces
packages/libraries
packages/io
packages/graphics
packages/examples
packages/numerical
packages/programming
packages/strings
packages/scientific
:::
