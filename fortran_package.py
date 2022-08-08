import yaml
from pathlib import Path
from collections import Counter
import json
import requests


root = Path(__file__).parent

with open(root / "_data" / "package_index.yml", "r") as f:
    fortran_index = yaml.safe_load(f)
with open(root / "_data" / "learning.yml", "r") as f:
    conf = yaml.safe_load(f)

fortran_index_tags = []
fortran_index_tags_50 = []
fortran_index_categories = []
fortran_index_libraries = []
fortran_index_data_types = []
fortran_index_strings = []
fortran_index_programming = []
fortran_index_graphics = []
fortran_index_interfaces = []
fortran_index_examples = []
fortran_index_scientific = []
fortran_index_io = []
fortran_index_numerical = []

for i in fortran_index:
    try:
        for j in str(i["tags"]).split():
            fortran_index_tags.append(j)
    except KeyError:
        pass
    if "libraries" in i["categories"].split():
        fortran_index_libraries.append(i)
    if "data-types" in i["categories"].split():
        fortran_index_data_types.append(i)
    if "strings" in i["categories"].split():
        fortran_index_strings.append(i)
    if "programming" in i["categories"].split():
        fortran_index_programming.append(i)
    if "graphics" in i["categories"].split():
        fortran_index_graphics.append(i)
    if "interfaces" in i["categories"].split():
        fortran_index_interfaces.append(i)
    if "examples" in i["categories"].split():
        fortran_index_examples.append(i)
    if "scientific" in i["categories"].split():
        fortran_index_scientific.append(i)
    if "io" in i["categories"].split():
        fortran_index_io.append(i)
    if "numerical" in i["categories"].split():
        fortran_index_numerical.append(i)

fortran_tags = {"fortran_tags": "tags"}
fortran_index_tags = Counter(fortran_index_tags)
a = sorted(fortran_index_tags.items(), key=lambda x: x[1], reverse=True)
for i in a:
    if i[0] == "None":
        a.remove(i)

for k in range(50):
    fortran_index_tags_50.append(a[k][0])

for i in fortran_index:
    for j in i["categories"].split():
        fortran_index_categories.append(j)

fortran_index_categories = list(set(fortran_index_categories))

fortran_tags["numerical"] = fortran_index_numerical
fortran_tags["io"] = fortran_index_io
fortran_tags["scientific"] = fortran_index_scientific
fortran_tags["examples"] = fortran_index_examples
fortran_tags["interfaces"] = fortran_index_interfaces
fortran_tags["graphics"] = fortran_index_graphics
fortran_tags["programming"] = fortran_index_programming
fortran_tags["strings"] = fortran_index_strings
fortran_tags["data_types"] = fortran_index_data_types
fortran_tags["libraries"] = fortran_index_libraries
fortran_tags["tags"] = fortran_index_tags_50
conf["reference_books"] = conf["reference-books"]
conf["reference_courses"] = conf["reference-courses"]
conf["reference_links"] = conf["reference-links"]

with open(root / "_data" / "fortran_package.json", "w") as f:
    json.dump(fortran_tags, f)
with open(root / "_data" / "fortran_learn.json", "w") as f:
    json.dump(conf, f)

fortran_monthly = []
fortran_commits = []
fpm_monthly = []
fpm_commits = []
stdlib_monthly = []
stdlib_commits = []

contributor = []
contributor_repo = {
    "repo": "fortran-lang",
}


def contributors(repo):
    info = requests.get(
        f"https://api.github.com/repos/{repo}/contributors").text
    d = json.loads(info)
    if "message" in d:
        raise Exception(d["message"])
    for i in d:
        contributor.append(i["login"])


graphs = [
    "fortran-lang/fortran-lang.org",
    "fortran-lang/webpage",
    "fortran-lang/fpm",
    "fortran-lang/stdlib",
    "j3-fortran/fortran_proposals",
]
for i in graphs:
    contributors(i)

contributor = list(set(contributor))
contributor.sort()
contributor_repo["contributor"] = contributor

with open(root / "_data" / "contributor.json", "w") as f:
    json.dump(contributor_repo, f)
