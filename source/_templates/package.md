## {{package.name}}

{% import '_templates/badges.jinja' as badges %}
{{ badges.render_badges(package, render_tags=False) }}

{% if package.tags %}
```{tags} {{ package.tags.split() | join(', ') }}
```
{% endif %}
