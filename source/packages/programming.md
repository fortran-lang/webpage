:::{div} sd-text-center sd-fs-2 sd-font-weight-bold sd-text-primary
Featured Open Source Projects
:::

:::{div} sd-text-center sd-fs-3
A rich ecosystem of high-performance code
:::

## Error handling, logging, documentation and testing

:::{jinja} fortran_index

{% for j in programming|sort(attribute='name') %}
{% if j.github is defined %}

<p>

## {fab}`github;1em` [{{j.name}}]({{"https://github.com/"+j.github}})

{% if j.description is defined %}

<p style="font-size:16px">{{j.description}} </p>
{% endif %}
{% if j.tags is defined %}
<p style="font-size:14px">Tags: {{j.tags}} </p>
{% endif %}

<img src="{{'https://img.shields.io/github/v/release/'+j.github+'?color=green'}}" alt="Release">
<img src="{{'https://img.shields.io/github/license/'+j.github}}" alt="license">
<img src="{{'https://img.shields.io/github/stars/'+j.github}}" alt="stars">
<img src="{{'https://img.shields.io/github/forks/'+j.github}}" alt="forks">
<img src="{{'https://img.shields.io/github/last-commit/'+j.github+'?color=blue'}}" alt="last-commit">
<img src="{{'https://img.shields.io/github/issues/'+j.github+'?color=yellow'}}" alt="issues">
</p>
{% elif j.gitlab is defined%}
<p>

## {fab}`gitlab;1em` [{{j.name}}]({{"https://gitlab.com/"+j.gitlab}})

{% if j.description is defined %}

<p style="font-size:16px">{{j.description}} </p>
{% endif %}
{% if j.tags is defined %}
<p style="font-size:14px">Tags: {{j.tags}} </p>
{% endif %}

<img src="{{'https://img.shields.io/gitlab/v/release/'+j.gitlab+'?date_order_by=created_at&sort=date&color=green'}}" alt="Release">
<img src="{{'https://img.shields.io/gitlab/license/'+j.gitlab}}" alt="license">
<img src="{{'https://img.shields.io/gitlab/forks/'+j.gitlab}}" alt="forks">
<img src="{{'https://img.shields.io/gitlab/issues/all/'+j.gitlab+'?color=yellow'}}" alt="issues">
</p>
{% else %}
<p>

## {fab}`git-alt;1em` [{{j.name}}]({{j.url}})

{% if j.description is defined %}

<p style="font-size:16px">{{j.description}} </p>
{% endif %}
{% if j.tags is defined %}
<p style="font-size:14px">Tags: {{j.tags}} </p>
{% endif %}
</p>

{% endif %}

{% endfor %}
:::

See [package index guidelines](../community/packages) for how to get your project listed.
