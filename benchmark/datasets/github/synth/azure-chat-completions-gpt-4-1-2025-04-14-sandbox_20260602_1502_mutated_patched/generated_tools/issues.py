import os
import requests
from typing import Any, Dict

GITHUB_API_BASE_URL = os.getenv("GITHUB_API_BASE_URL", "https://api.github.com")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {GITHUB_TOKEN}" if GITHUB_TOKEN else None,
    "X-GitHub-Api-Version": "2026-03-10"
}
HEADERS = {k: v for k, v in HEADERS.items() if v is not None}


def list_issues_assigned_to_authenticated_user(
    filter: str = "assigned",
    state: str = "open",
    labels: str = None,
    sort: str = "created",
    direction: str = "desc",
    since: str = None,
    collab: bool = None,
    orgs: bool = None,
    owned: bool = None,
    pulls: bool = None,
    per_page: int = 30,
    page: int = 1
) -> Any:
    """
    List issues assigned to the authenticated user across all visible repositories.
    Source: docs/api_issues-issues.md
    Endpoint: GET /issues
    """
    url = f"{GITHUB_API_BASE_URL}/issues"
    params = {
        "filter": filter,
        "state": state,
        "labels": labels,
        "sort": sort,
        "direction": direction,
        "since": since,
        "collab": collab,
        "orgs": orgs,
        "owned": owned,
        "pulls": pulls,
        "per_page": per_page,
        "page": page
    }
    params = {k: v for k, v in params.items() if v is not None}
    try:
        resp = requests.get(url, headers=HEADERS, params=params)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {"error": f"{resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}


def list_issue_comments_for_repository(
    owner: str,
    repo: str,
    sort: str = "created",
    direction: str = "asc",
    since: str = None,
    per_page: int = 30,
    page: int = 1
) -> Any:
    """
    List comments on issues and pull requests for a repository.
    Source: docs/api_issues-comments.md
    Endpoint: GET /repos/{owner}/{repo}/issues/comments
    """
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/issues/comments"
    params = {
        "sort": sort,
        "direction": direction,
        "since": since,
        "per_page": per_page,
        "page": page
    }
    params = {k: v for k, v in params.items() if v is not None}
    try:
        resp = requests.get(url, headers=HEADERS, params=params)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {"error": f"{resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}


def get_issue_comment(
    owner: str,
    repo: str,
    comment_id: int
) -> Any:
    """
    Get a comment on an issue or pull request.
    Source: docs/api_issues-comments.md
    Endpoint: GET /repos/{owner}/{repo}/issues/comments/{comment_id}
    """
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/issues/comments/{comment_id}"
    try:
        resp = requests.get(url, headers=HEADERS)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {"error": f"{resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}


def update_issue_comment(
    owner: str,
    repo: str,
    comment_id: int,
    body: str
) -> Any:
    """
    Update a comment on an issue or pull request.
    Source: docs/api_issues-comments.md
    Endpoint: PATCH /repos/{owner}/{repo}/issues/comments/{comment_id}
    """
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/issues/comments/{comment_id}"
    data = {"body": body}
    try:
        resp = requests.patch(url, headers=HEADERS, json=data)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {"error": f"{resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}


def delete_issue_comment(
    owner: str,
    repo: str,
    comment_id: int
) -> Any:
    """
    Delete a comment on an issue or pull request.
    Source: docs/api_issues-comments.md
    Endpoint: DELETE /repos/{owner}/{repo}/issues/comments/{comment_id}
    """
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/issues/comments/{comment_id}"
    try:
        resp = requests.delete(url, headers=HEADERS)
        if resp.status_code == 204:
            return {"result": "deleted"}
        else:
            return {"error": f"{resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}


def pin_issue_comment(
    owner: str,
    repo: str,
    comment_id: int
) -> Any:
    """
    Pin a comment on an issue.
    Source: docs/api_issues-comments.md
    Endpoint: PUT /repos/{owner}/{repo}/issues/comments/{comment_id}/pin
    """
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/issues/comments/{comment_id}/pin"
    try:
        resp = requests.put(url, headers=HEADERS)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {"error": f"{resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}
