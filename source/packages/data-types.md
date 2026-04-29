:::::{jinja} fortran_index
{% set items = data_types|sort(attribute='name') %}
{% set title = "Libraries for advanced data types and container classes" %}
{% include "_templates/project_pages.html" %}
:::::
