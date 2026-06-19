import os
import requests
import json

GITHUB_API_BASE_URL = os.getenv("GITHUB_API_BASE_URL", "https://api.github.com")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

session = requests.Session()
session.headers.update({
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
})

def get_repository(owner: str, repo: str) -> dict:
    """
    Retrieves information about a specific repository.
    https://docs.github.com/en/rest/repos/repos#get-a-repository
    """
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}"
    response = session.get(url)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code, "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def create_repository_for_authenticated_user(name: str, description: str = "", homepage: str = "", private: bool = False, has_issues: bool = True, has_projects: bool = True, has_wiki: bool = True, auto_init: bool = False, gitignore_template: str = "", license_template: str = "", allow_squash_merge: bool = True, allow_merge_commit: bool = True, allow_rebase_merge: bool = True, delete_branch_on_merge: bool = False) -> dict:
    """
    Creates a new repository for the authenticated user.
    https://docs.github.com/en/rest/repos/repos#create-a-repository-for-the-authenticated-user
    """
    url = f"{GITHUB_API_BASE_URL}/user/repos"
    payload = {
        "name": name,
        "description": description,
        "homepage": homepage,
        "private": private,
        "has_issues": has_issues,
        "has_projects": has_projects,
        "has_wiki": has_wiki,
        "auto_init": auto_init,
        "gitignore_template": gitignore_template,
        "license_template": license_template,
        "allow_squash_merge": allow_squash_merge,
        "allow_merge_commit": allow_merge_commit,
        "allow_rebase_merge": allow_rebase_merge,
        "delete_branch_on_merge": delete_branch_on_merge
    }
    response = session.post(url, data=json.dumps(payload))
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code, "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def list_user_repositories(type: str = "owner", sort: str = "full_name", direction: str = "asc", per_page: int = 30, page: int = 1) -> dict:
    """
    Lists repositories for the authenticated user.
    https://docs.github.com/en/rest/repos/repos#list-repositories-for-the-authenticated-user
    """
    url = f"{GITHUB_API_BASE_URL}/user/repos"
    params = {
        "type": type,
        "sort": sort,
        "direction": direction,
        "per_page": per_page,
        "page": page
    }
    response = session.get(url, params=params)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code, "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
