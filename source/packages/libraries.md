:::::{jinja} fortran_index
{% set items = libraries|sort(attribute='name') %}
{% set title = "Fortran libraries for general programming tasks" %}
{% include "_templates/project_pages.html" %}
:::::
