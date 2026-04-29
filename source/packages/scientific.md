:::::{jinja} fortran_index
{% set items = scientific|sort(attribute='name') %}
{% set title = "Applications and libraries for applied mathematical and scientific problems" %}
{% include "_templates/project_pages.html" %}
:::::
