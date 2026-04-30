import json
import os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote_plus

import requests
import yaml

GITHUB_API_VERSION = "2022-11-28"
REQUEST_TIMEOUT = 20


def get_contributors(repo: str) -> list[str]:
    """Query GitHub REST API to determine contributors for a repository."""
    response = requests.get(
        f"https://api.github.com/repos/{repo}/contributors", timeout=REQUEST_TIMEOUT
    )
    response.raise_for_status()
    info = response.json()
    return [contributor["login"] for contributor in info]


def _request_json(
    url: str,
    *,
    headers: dict[str, str] | None = None,
    expected_statuses: tuple[int, ...] = (200,),
) -> dict | list | None:
    """Return parsed JSON data for successful requests, otherwise None."""
    try:
        response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
    except requests.RequestException as exc:
        print(f"Request failed for {url}: {exc}")
        return None

    if response.status_code not in expected_statuses:
        print(f"Request failed for {url}: HTTP {response.status_code}")
        return None

    try:
        return response.json()
    except ValueError:
        print(f"Request failed for {url}: invalid JSON")
        return None


def _github_headers(token: str | None) -> dict[str, str]:
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": GITHUB_API_VERSION,
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def _gitlab_headers(token: str | None) -> dict[str, str]:
    if not token:
        return {}
    return {"PRIVATE-TOKEN": token}


def fetch_github_repository_data(repo_slug: str, token: str | None) -> dict | None:
    headers = _github_headers(token)
    return _request_json(f"https://api.github.com/repos/{repo_slug}", headers=headers)


def fetch_github_latest_release(repo_slug: str, token: str | None) -> dict | None:
    headers = _github_headers(token)
    data = _request_json(
        f"https://api.github.com/repos/{repo_slug}/releases/latest",
        headers=headers,
        expected_statuses=(200, 404),
    )
    if isinstance(data, dict) and data.get("message") == "Not Found":
        return None
    if isinstance(data, dict):
        return data
    return None


def fetch_gitlab_project_data(repo_slug: str, token: str | None) -> dict | None:
    encoded = quote_plus(repo_slug)
    headers = _gitlab_headers(token)
    data = _request_json(f"https://gitlab.com/api/v4/projects/{encoded}", headers=headers)
    if isinstance(data, dict):
        return data
    return None


def fetch_gitlab_latest_commit(repo_slug: str, token: str | None) -> dict | None:
    encoded = quote_plus(repo_slug)
    headers = _gitlab_headers(token)
    data = _request_json(
        f"https://gitlab.com/api/v4/projects/{encoded}/repository/commits?per_page=1",
        headers=headers,
    )
    if isinstance(data, list) and data:
        first = data[0]
        if isinstance(first, dict):
            return first
    return None


def fetch_gitlab_latest_release(repo_slug: str, token: str | None) -> dict | None:
    encoded = quote_plus(repo_slug)
    headers = _gitlab_headers(token)
    data = _request_json(
        f"https://gitlab.com/api/v4/projects/{encoded}/releases/permalink/latest",
        headers=headers,
        expected_statuses=(200, 404),
    )
    if isinstance(data, dict) and data.get("message") == "404 Release Not Found":
        return None
    if isinstance(data, dict):
        return data
    return None


def normalize_github_metadata(
    package: dict,
    repository_data: dict | None,
    release_data: dict | None,
) -> dict:
    return {
        "provider": "github",
        "repo_slug": package["github"],
        "repository_url": f"https://github.com/{package['github']}",
        "last_commit_date": repository_data.get("pushed_at") if repository_data else None,
        "forks_count": repository_data.get("forks_count") if repository_data else None,
        "stars_count": repository_data.get("stargazers_count") if repository_data else None,
        "watchers_count": repository_data.get("watchers_count") if repository_data else None,
        "open_issues_count": repository_data.get("open_issues_count") if repository_data else None,
        "default_branch": repository_data.get("default_branch") if repository_data else None,
        "license": (
            repository_data.get("license", {}).get("spdx_id")
            if repository_data and repository_data.get("license")
            else None
        ),
        "latest_release": release_data.get("tag_name") if release_data else None,
        "latest_release_date": release_data.get("published_at") if release_data else None,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
    }


def normalize_gitlab_metadata(
    package: dict,
    project_data: dict | None,
    commit_data: dict | None,
    release_data: dict | None,
) -> dict:
    return {
        "provider": "gitlab",
        "repo_slug": package["gitlab"],
        "repository_url": f"https://gitlab.com/{package['gitlab']}",
        "last_commit_date": (
            commit_data.get("committed_date") if commit_data else project_data.get("last_activity_at") if project_data else None
        ),
        "forks_count": project_data.get("forks_count") if project_data else None,
        "stars_count": project_data.get("star_count") if project_data else None,
        "watchers_count": None,
        "open_issues_count": project_data.get("open_issues_count") if project_data else None,
        "default_branch": project_data.get("default_branch") if project_data else None,
        "license": (
            project_data.get("license", {}).get("key")
            if project_data and project_data.get("license")
            else None
        ),
        "latest_release": release_data.get("tag_name") if release_data else None,
        "latest_release_date": release_data.get("released_at") if release_data else None,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
    }


def update_json_files() -> None:
    """Update JSON files that define webpage configuration and package metadata."""
    root = Path(__file__).parent
    github_token: str | None = os.getenv("GITHUB_TOKEN")
    gitlab_token: str | None = os.getenv("GITLAB_TOKEN")

    packages = root / "data" / "packages"
    packages.mkdir(parents=True, exist_ok=True)

    # --- Update references
    with open(root / "data" / "learning.yml", "r", encoding="utf-8") as f:
        conf = yaml.safe_load(f)
    conf["reference_books"] = conf["reference-books"]
    conf["reference_courses"] = conf["reference-courses"]
    conf["reference_links"] = conf["reference-links"]
    conf["reference_course_providers"] = conf["reference-course-providers"]
    conf["reference_ebooks"] = conf["reference-ebooks"]
    with open(root / "_data" / "fortran_learn.json", "w", encoding="utf-8") as f:
        json.dump(conf, f)

    # --- Update package index tags
    with open(root / "data" / "package_index.yml", "r", encoding="utf-8") as f:
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
    fortran_tags: dict[str, list[dict]] = {}
    enriched_fortran_packages: dict[str, list[dict]] = {category: [] for category in categories}

    for package in fortran_index:
        if package.get("tags"):
            fortran_index_tags += package["tags"].split()

        repo_metadata: dict | None = None

        if "github" in package:
            repo_slug = package["github"]
            print(f"Fetching package data for GitHub repository {repo_slug}...")
            repository_data = fetch_github_repository_data(repo_slug, github_token)
            release_data = fetch_github_latest_release(repo_slug, github_token)
            repo_metadata = normalize_github_metadata(package, repository_data, release_data)

            cache_filename = f"github_{repo_slug.replace('/', '_')}.json"
            with open(packages / cache_filename, "w", encoding="utf-8") as f:
                json.dump(
                    {
                        "provider": "github",
                        "repo_slug": repo_slug,
                        "repository": repository_data,
                        "latest_release": release_data,
                    },
                    f,
                )

        elif "gitlab" in package:
            repo_slug = package["gitlab"]
            print(f"Fetching package data for GitLab repository {repo_slug}...")
            project_data = fetch_gitlab_project_data(repo_slug, gitlab_token)
            commit_data = fetch_gitlab_latest_commit(repo_slug, gitlab_token)
            release_data = fetch_gitlab_latest_release(repo_slug, gitlab_token)
            repo_metadata = normalize_gitlab_metadata(
                package, project_data, commit_data, release_data
            )

            cache_filename = f"gitlab_{repo_slug.replace('/', '_')}.json"
            with open(packages / cache_filename, "w", encoding="utf-8") as f:
                json.dump(
                    {
                        "provider": "gitlab",
                        "repo_slug": repo_slug,
                        "project": project_data,
                        "latest_commit": commit_data,
                        "latest_release": release_data,
                    },
                    f,
                )

        package_enriched = dict(package)
        if repo_metadata:
            package_enriched["repository"] = repo_metadata

        for category in categories:
            if category in package["categories"].split():
                fortran_tags.setdefault(category, []).append(package)
                enriched_fortran_packages[category].append(package_enriched)

    fortran_index_tags_data = Counter(fortran_index_tags)
    tags = {
        "tags": [
            item[0]
            for item in sorted(
                fortran_index_tags_data.items(), key=lambda x: x[1], reverse=True
            )
            if item[0] != "None" and item[1] > 0
        ][:50]
    }

    with open(root / "_data" / "fortran_tags.json", "w", encoding="utf-8") as f:
        json.dump(tags, f)
    with open(root / "_data" / "fortran_package.json", "w", encoding="utf-8") as f:
        json.dump(fortran_tags, f)

    enriched_fortran_packages["meta"] = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": "data/package_index.yml",
    }
    with open(root / "_data" / "fortran_packages.json", "w", encoding="utf-8") as f:
        json.dump(enriched_fortran_packages, f)

    # --- Gather contributor information for selected fortran-lang repositories
    repos = [
        "fortran-lang/fortran-lang.org",
        "fortran-lang/webpage",
        "fortran-lang/fpm",
        "fortran-lang/stdlib",
        "j3-fortran/fortran_proposals",
    ]
    contributors = set()
    for repo in repos:
        try:
            contributors.update(get_contributors(repo))
        except requests.RequestException as exc:
            print(f"Contributor query failed for {repo}: {exc}")

    contributor_repo = {"repo": "fortran-lang", "contributor": sorted(contributors)}
    with open(root / "_data" / "contributor.json", "w", encoding="utf-8") as f:
        json.dump(contributor_repo, f)


if __name__ == "__main__":
    update_json_files()
