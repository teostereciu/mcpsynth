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

def search_repositories(q: str, sort: str = "", order: str = "desc", per_page: int = 30, page: int = 1) -> dict:
    """
    Searches for repositories.
    https://docs.github.com/en/rest/search/search#search-repositories
    """
    url = f"{GITHUB_API_BASE_URL}/search/repositories"
    params = {
        "q": q,
        "sort": sort,
        "order": order,
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


def search_code(q: str, sort: str = "", order: str = "desc", per_page: int = 30, page: int = 1) -> dict:
    """
    Searches for code.
    https://docs.github.com/en/rest/search/search#search-code
    """
    url = f"{GITHUB_API_BASE_URL}/search/code"
    params = {
        "q": q,
        "sort": sort,
        "order": order,
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


def search_issues_and_pull_requests(q: str, sort: str = "", order: str = "desc", per_page: int = 30, page: int = 1) -> dict:
    """
    Searches for issues and pull requests.
    https://docs.github.com/en/rest/search/search#search-issues-and-pull-requests
    """
    url = f"{GITHUB_API_BASE_URL}/search/issues"
    params = {
        "q": q,
        "sort": sort,
        "order": order,
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
