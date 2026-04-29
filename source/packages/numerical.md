:::::{jinja} fortran_index
{% set items = numerical|sort(attribute='name') %}
{% set title = "Fortran libraries for linear algebra, optimization, root-finding, etc." %}
{% include "_templates/project_pages.html" %}
:::::
