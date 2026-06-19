
import os
import requests
from typing import Optional, Dict, Any, List

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_API_BASE_URL = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com")

def build_headers():
    headers = {
        "Accept": "application/vnd.github.v3+json",
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers

def create_issue(owner: str, repo: str, title: str, body: Optional[str] = None, labels: Optional[List[str]] = None, assignees: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Creates an issue in a repository.
    """
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/issues"
    data = {
        "title": title,
        "body": body,
        "labels": labels,
        "assignees": assignees
    }
    response = requests.post(url, headers=build_headers(), json=data)
    if response.status_code == 201:
        return response.json()
    else:
        return {"error": response.json()}

def update_issue(owner: str, repo: str, issue_number: int, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None, labels: Optional[List[str]] = None, assignees: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Updates an issue in a repository.
    """
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/issues/{issue_number}"
    data = {}
    if title:
        data["title"] = title
    if body:
        data["body"] = body
    if state:
        data["state"] = state
    if labels:
        data["labels"] = labels
    if assignees:
        data["assignees"] = assignees
    response = requests.patch(url, headers=build_headers(), json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.json()}

def get_issue(owner: str, repo: str, issue_number: int) -> Dict[str, Any]:
    """
    Gets an issue in a repository.
    """
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/issues/{issue_number}"
    response = requests.get(url, headers=build_headers())
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.json()}
