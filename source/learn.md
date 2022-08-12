---
sd_hide_title: true
...

# Learn

:::{div} sd-text-center sd-fs-2 sd-font-weight-bold sd-text-primary
Learn Fortran
:::

:::{div} sd-text-center sd-fs-3
Learning resources for beginners and experts alike
:::

:::{div} sd-fs-3 sd-font-weight-bold sd-text-primary
Getting Started
:::

:::::::{grid} 1 1 2 2
:gutter: 1

::::::{grid-item}

:::::{grid} 1 1 1 1
:gutter: 1

::::{grid-item-card} {octicon}``info;1em;sd-text-info`` New to Fortran
:shadow: none

Try the quickstart Fortran tutorial, to get an overview of the language syntax and capabilities.

```{button-link} quickstart/
:color: primary
:expand:

{octicon}``book;1em;sd-text-info`` Quickstart tutorial
```
::::
:::::
::::::

::::::{grid-item}

:::::{grid} 1 1 1 1
:gutter: 1

::::{grid-item-card} {octicon}``bug;1em;sd-text-info`` Looking for help
:shadow: none

Ask a question in the Fortran-lang discourse - a forum for friendly discussion of all things Fortran.

:::{div} sd-btn sd-btn-primary sd-d-grid sd-text-light
```{button-link} https://fortran-lang.discourse.group/
:color: primary
:expand:

{octicon}``check-circle;1em;sd-text-info`` Fortran-lang Discourse
```
:::
::::
:::::
::::::
:::::::

:::{div} sd-fs-3 sd-font-weight-bold sd-text-primary

Mini-book Tutorials
:::

::::::{jinja} conf

{% for category in categories %}
:::{div} sd-fs-4 sd-font-weight-bold sd-text-primary

{{category.name}}
:::

:::::{grid} 2
{% for book in books %}
{% if book.category == category.name %}

::::{grid-item-card}
:columns: 6
:shadow: none

:::{div} sd-fs-5 sd-font-weight-bold sd-text-primary

{octicon}``book;1em;sd-text-info`` <a href='{{"../"+book.link[1:]+"/"}}'>{{book.title}}</a>
:::
{{book.description}}
::::
{% endif %}
{% endfor %}
:::::
{% endfor %}

:::{div} sd-fs-3 sd-font-weight-bold sd-text-primary

Other Resources
:::

:::{div} sd-fs-4 sd-font-weight-bold sd-text-primary

On the web
:::

:::{jinja} conf

{% for link in reference_links %}

* [{{link.name}}]({{link.url}}) {{link.description}}

{% endfor %}
:::



:::{div} sd-fs-4 sd-font-weight-bold sd-text-primary

Online Courses
:::


:::{jinja} conf

{% for course in reference_courses %}

* [{{course.name}}]({{course.url}}) {{course.description}}

{% endfor %}
:::

:::{div} sd-fs-4 sd-font-weight-bold sd-text-primary

In print
:::

:::{jinja} conf

{% for book in reference_books %}

* {{book.author}}
  {{book.year}}
  [{{book.title}}]({{book.url}})
  {{book.edition}}
  {{book.location}}. 
  {{book.publisher}}

{% endfor %}
:::


:::{toctree}
:hidden:

learn/quickstart/index
learn/best_practices/index
learn/os_setup/index
learn/building_programs/index
learn/intrinsics/index
:::
