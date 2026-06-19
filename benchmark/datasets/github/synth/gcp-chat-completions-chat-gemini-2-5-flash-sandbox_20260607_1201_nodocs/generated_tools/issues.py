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

def list_repository_issues(owner: str, repo: str, milestone: str = "none", state: str = "open", assignee: str = "none", creator: str = "none", since: str = "", per_page: int = 30, page: int = 1) -> dict:
    """
    Lists issues for a repository.
    https://docs.github.com/en/rest/issues/issues#list-repository-issues
    """
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/issues"
    params = {
        "milestone": milestone,
        "state": state,
        "assignee": assignee,
        "creator": creator,
        "since": since,
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


def get_issue(owner: str, repo: str, issue_number: int) -> dict:
    """
    Retrieves a specific issue.
    https://docs.github.com/en/rest/issues/issues#get-an-issue
    """
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/issues/{issue_number}"
    response = session.get(url)
    try:
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": str(e), "status_code": e.response.status_code, "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def create_issue(owner: str, repo: str, title: str, body: str = "", assignee: str = "", milestone: int = None, labels: list = None) -> dict:
    """
    Creates a new issue.
    https://docs.github.com/en/rest/issues/issues#create-an-issue
    """
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/issues"
    payload = {
        "title": title,
        "body": body,
        "assignee": assignee,
        "milestone": milestone,
        "labels": labels
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
