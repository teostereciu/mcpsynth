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

def list_pull_requests(owner: str, repo: str, state: str = "open", head: str = "", base: str = "", sort: str = "created", direction: str = "desc", per_page: int = 30, page: int = 1) -> dict:
    """
    Lists pull requests for a repository.
    https://docs.github.com/en/rest/pulls/pulls#list-pull-requests
    """
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/pulls"
    params = {
        "state": state,
        "head": head,
        "base": base,
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


def get_pull_request(owner: str, repo: str, pull_number: int) -> dict:
    """
    Retrieves a specific pull request.
    https://docs.github.com/en/rest/pulls/pulls#get-a-pull-request
    """
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/pulls/{pull_number}"
    response = session.get(url)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code, "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def create_pull_request(owner: str, repo: str, title: str, head: str, base: str, body: str = "", draft: bool = False) -> dict:
    """
    Creates a new pull request.
    https://docs.github.com/en/rest/pulls/pulls#create-a-pull-request
    """
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/pulls"
    payload = {
        "title": title,
        "head": head,
        "base": base,
        "body": body,
        "draft": draft
    }
    # Filter out None values from payload
    payload = {k: v for k, v in payload.items() if v is not None and v != ""}
    response = session.post(url, data=json.dumps(payload))
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code, "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
