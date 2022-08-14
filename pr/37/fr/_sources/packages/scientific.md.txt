:::{div} sd-text-center sd-fs-2 sd-font-weight-bold sd-text-primary
Featured Open Source Projects
:::

:::{div} sd-text-center sd-fs-3
A rich ecosystem of high-performance code
:::

## Applications and libraries for applied mathematical and scientific problems

:::{jinja} fortran_index

{% for j in scientific|sort(attribute='name') %}
{% if j.github is defined %}
## [{{j.name}}]({{"https://github.com/"+j.github}})  
{{j.description}} 

Tags: {{j.tags}} 

![Release]({{'https://img.shields.io/github/v/release/'+j.github+'?color=green'}})
![license]({{'https://img.shields.io/github/license/'+j.github}})
![stars]({{'https://img.shields.io/github/stars/'+j.github}})
![forks]({{'https://img.shields.io/github/forks/'+j.github}})
![last-commit]({{'https://img.shields.io/github/last-commit/'+j.github+'?color=blue'}})
![issues]({{'https://img.shields.io/github/issues/'+j.github+'?color=yellow'}})
{% elif j.gitlab is defined%}
## [{{j.name}}]({{"https://gitlab.com/"+j.gitlab}})
{{j.description}} 

Tags: {{j.tags}} 

![Release]({{'https://img.shields.io/gitlab/v/release/'+j.gitlab+'?date_order_by=created_at&sort=date&color=green'}})
![license]({{'https://img.shields.io/gitlab/license/'+j.gitlab}})
![forks]({{'https://img.shields.io/gitlab/forks/'+j.gitlab}})
![issues]({{'https://img.shields.io/gitlab/issues/all/'+j.gitlab+'?color=yellow'}})
{% else %}
## [{{j.name}}]({{j.url}})

{{j.description}} 

Tags: {{j.tags}} 
{% endif %}

{% endfor %}
:::

See [package index guidelines](../community/packages) for how to get your project listed.