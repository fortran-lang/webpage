:::{div} sd-text-center sd-fs-2 sd-font-weight-bold sd-text-primary
Featured Open Source Projects
:::

:::{div} sd-text-center sd-fs-3
A rich ecosystem of high-performance code
:::

## {{title}}

{% for item in items|sort(attribute='name') %}
{% import '_templates/badges.jinja' as badges %}
{{ badges.render_badges(item, True) }}
{% endfor %}


See [package index guidelines](../community/packages) for how to get your project listed.
