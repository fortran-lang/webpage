import yaml
from pathlib import Path
from collections import Counter
import json
import requests


def get_contributors(repo: str) -> list[str]:
    """Query GitHub REST API to determine the contributors to a repository.

    :arg repo: repository name
    :return: list of GitHub usernames for contributors to the repository
    """
    info = requests.get(f"https://api.github.com/repos/{repo}/contributors").json()
    if "message" in info:
        raise Exception(info["message"])
    return [contributor["login"] for contributor in info]


def update_json_files() -> None:
    """
    Update the JSON files that define the webpage configuration.
    """
    root = Path(__file__).parent

    # --- Update references

    with open(root / "data" / "learning.yml", "r") as f:
        conf = yaml.safe_load(f)
    conf["reference_books"] = conf["reference-books"]
    conf["reference_courses"] = conf["reference-courses"]
    conf["reference_links"] = conf["reference-links"]
    conf["reference_course_providers"] = conf["reference-course-providers"]
    conf["reference_ebooks"] = conf["reference-ebooks"]
    with open(root / "_data" / "fortran_learn.json", "w") as f:
        json.dump(conf, f)

    # --- Update package index tags

    with open(root / "data" / "package_index.yml", "r") as f:
        fortran_index = yaml.safe_load(f)
    fortran_index_tags = []
    categories = [
        "libraries",
        "data-types",
        "strings",
        "programming",
        "graphics",
        "interfaces",
        "examples",
        "scientific",
        "io",
        "numerical",
    ]
    fortran_tags = {"fortran_tags": "tags"}

    for i in fortran_index:
        try:
            fortran_index_tags += i["tags"].split()
        except Exception:
            pass

        for j in categories:
            if j in i["categories"].split():
                if fortran_tags.get(j, None):
                    fortran_tags[j].append(i)
                else:
                    fortran_tags[j] = [i]

    fortran_index_tags_data = Counter(fortran_index_tags)
    fortran_tags["tags"] = [
        item[0]
        for item in sorted(
            fortran_index_tags_data.items(), key=lambda x: x[1], reverse=True
        )
        if item[0] != "None" and item[1] > 0
    ][:50]
    fortran_tags["data_types"] = fortran_tags.pop("data-types")
    with open(root / "_data" / "fortran_package.json", "w") as f:
        json.dump(fortran_tags, f)

    # --- Gather contributor information for all fortran-lang repositories

    repos = [
        "fortran-lang/fortran-lang.org",
        "fortran-lang/webpage",
        "fortran-lang/fpm",
        "fortran-lang/stdlib",
        "j3-fortran/fortran_proposals",
    ]
    contributors = set()
    for repo in repos:
        contributors.update(get_contributors(repo))
    contributors = list(contributors)
    contributors.sort()
    contributor_repo = {"repo": "fortran-lang", "contributor": contributors}
    with open(root / "_data" / "contributor.json", "w") as f:
        json.dump(contributor_repo, f)


if __name__ == "__main__":
    update_json_files()
