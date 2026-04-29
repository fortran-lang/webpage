:::::{jinja} fortran_index
{% set items = io|sort(attribute='name') %}
{% set title = "Libraries for reading, writing and parsing files and inputs" %}
{% include "_templates/project_pages.html" %}
:::::
