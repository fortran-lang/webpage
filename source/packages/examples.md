:::::{jinja} fortran_index
{% set items = examples|sort(attribute='name') %}
{% set title = "Demonstration code and templates for Fortran" %}
{% include "_templates/project_pages.html" %}
:::::
