:::::{jinja} fortran_index
{% set items = interfaces|sort(attribute='name') %}
{% set title = "Libraries that interface with other systems, languages, or devices" %}
{% include "_templates/project_pages.html" %}
:::::
