:::{div} sd-text-center sd-fs-2 sd-font-weight-bold sd-text-primary
Featured Open Source Projects
:::

:::{div} sd-text-center sd-fs-3
A rich ecosystem of high-performance code
:::

## Demonstration codes and templates for Fortran


:::::{jinja} fortran_index

{% for j in examples|sort(attribute='name') %}
:::{div} sd-fs-5
{% if j.github is defined %}

## {fab}`github;1em` [{{j.name}}]({{"https://github.com/"+j.github}})
<img src="{{'https://img.shields.io/github/v/release/'+j.github+'?color=green'}}" alt="Release">
{% if j.license is defined %}
<img src='https://img.shields.io/badge/license-{{ j.license | replace("-", "--") | replace("_", "__") }}-blue' alt="license">
{% else %}
<img src="{{'https://img.shields.io/github/license/'+j.github}}" alt="license">
{% endif %}
<img src="{{'https://img.shields.io/github/stars/'+j.github}}" alt="stars">
<img src="{{'https://img.shields.io/github/forks/'+j.github}}" alt="forks">
<img src="{{'https://img.shields.io/github/last-commit/'+j.github+'?color=blue'}}" alt="last-commit">
<img src="{{'https://img.shields.io/github/issues/'+j.github+'?color=yellow'}}" alt="issues">
{% if j.description is defined %}
{{j.description}}
{% endif %}
{% if j.tags is defined and j.tags != None %}
Tags: {% for tag in j.tags.split() %} {bdg-light}`{{ tag }}` {% endfor %}

{% endif %}  

{% elif j.gitlab is defined%}

## {fab}`gitlab;1em` [{{j.name}}]({{"https://gitlab.com/"+j.gitlab}})

<img src="{{'https://img.shields.io/gitlab/v/release/'+j.gitlab+'?date_order_by=created_at&sort=date&color=green'}}" alt="Release">
{% if j.license is defined %}
<img src='https://img.shields.io/badge/license-{{ j.license | replace("-", "--") | replace("_", "__") }}-blue' alt="license">
{% else %}
<img src="{{'https://img.shields.io/gitlab/license/'+j.gitlab}}" alt="license">
{% endif %}
<img src="{{'https://img.shields.io/gitlab/forks/'+j.gitlab}}" alt="forks">
<img src="{{'https://img.shields.io/gitlab/issues/all/'+j.gitlab+'?color=yellow'}}" alt="issues">
{% if j.description is defined %}
{{j.description}}
{% endif %}
{% if j.tags is defined and j.tags != None %}
Tags: {% for tag in j.tags.split() %} {bdg-light}`{{ tag }}` {% endfor %}

{% endif %} 
{% else %}

## {fab}`git-alt;1em` [{{j.name}}]({{j.url}})

{% if j.license is defined %}
<img src='https://img.shields.io/badge/license-{{ j.license | replace("-", "--") | replace("_", "__") }}-blue' alt="license">
{% endif %}
{% if j.description is defined %}
{{j.description}}
{% endif %}
{% if j.tags is defined and j.tags != None %}
Tags: {% for tag in j.tags.split() %} {bdg-light}`{{ tag }}` {% endfor %}

{% endif %} 

{% endif %}
:::
{% endfor %}

:::::

See [package index guidelines](../community/packages) for how to get your project listed.
