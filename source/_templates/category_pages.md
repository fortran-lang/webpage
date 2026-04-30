## {{title}}

### {{description}}

{% for item in items|sort(attribute='name') %}
{% import '_templates/badges.jinja' as badges %}
{{ badges.render_badges(item, True) }}
{% endfor %}


See [package index guidelines](../community/packages) for how to get your project listed.
