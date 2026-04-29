:::::{jinja} fortran_index
{% set items = graphics|sort(attribute='name') %}
{% set title = "Libraries for plotting data, handling images and generating user interfaces" %}
{% include "_templates/project_pages.html" %}
:::::
