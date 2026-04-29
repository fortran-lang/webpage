:::::{jinja} fortran_index
{% set items = programming|sort(attribute='name') %}
{% set title = "Fortran libraries for error handling, logging, documentation and testing" %}
{% include "_templates/project_pages.html" %}
:::::
