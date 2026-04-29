:::::{jinja} fortran_index
{% set items = strings|sort(attribute='name') %}
{% set title = "Libraries for manipulating characters and strings" %}
{% include "_templates/project_pages.html" %}
:::::
