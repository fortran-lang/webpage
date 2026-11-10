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

:::{jinja} tags
{% for tag in tags %}{bdg-ref-secondary}`{{ tag }} <sphx_tag_{{ tag }}>`{% endfor %}
:::

::::

:::::

:::{div} sd-fs-3 sd-font-weight-bold sd-text-primary
Browse Packages by Category
:::

:::{jinja} categories
{% for slug, item in categories.items() %}
## [{{item.title}}](../categories/{{slug}})

{{item.description}}
{% endfor %}

See [package index guidelines](../community/packages) for how to get your project listed.

::::::{jinja} categories
:::{toctree}
:hidden:

{% for slug,item in categories.items() %}
categories/{{slug}}
{% endfor %}
:::
::::::

## Searchable Table Test

<table id="package_table_test">
 <thead>
   <tr>
     <th>Package</th>
     <th>Release</th>
     <th>Stars</th>
     <th>Forks</th>
     <th>Last Commit</th>
     <th>Issues</th>
     <th>Pull Requests</th>
   </tr>
 </thead>
 <tbody>
   <tr>
     <td><a href="https://github.com/PlasmaFAIR/Fortitude">Fortitude</a></td>
     <td>v0.10.0</td>
     <td>420</td>
     <td>12</td>
     <td>2026-09-28</td>
     <td>312</td>
     <td>6</td>
   </tr>
   <tr>
     <td><a href="https://github.com/Goddard-Fortran-Ecosystem/pFUnit">pFUnit</a></td>
     <td>v1.23.0</td>
     <td>69</td>
     <td>20</td>
     <td>2025-03-06</td>
     <td>13</td>
     <td>86</td>
   </tr>
 </tbody>
</table>
