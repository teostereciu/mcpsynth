import os
import requests
from typing import Any, Dict, List, Optional

def _github_headers() -> Dict[str, str]:
    token = os.environ.get("GITHUB_TOKEN")
    headers = {
        "Accept": "application/vnd.github+json",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers

def list_issues_assigned_to_authenticated_user(
    filter: Optional[str] = None,
    state: Optional[str] = None,
    labels: Optional[str] = None,
    sort: Optional[str] = None,
    direction: Optional[str] = None,
    since: Optional[str] = None,
    collab: Optional[bool] = None,
    orgs: Optional[bool] = None,
    owned: Optional[bool] = None,
    pulls: Optional[bool] = None,
    per_page: Optional[int] = 30,
    page: Optional[int] = 1,
) -> Any:
    """List issues assigned to the authenticated user across all visible repositories."""
    url = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com") + "/issues"
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
        "page": page,
    }
    params = {k: v for k, v in params.items() if v is not None}
    try:
        resp = requests.get(url, headers=_github_headers(), params=params)
        if resp.status_code == 200:
            return resp.json()
        return {"error": f"{resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}

def list_labels_for_issue(owner: str, repo: str, issue_number: int, per_page: int = 30, page: int = 1) -> Any:
    """List all labels for an issue."""
    url = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com") + f"/repos/{owner}/{repo}/issues/{issue_number}/labels"
    params = {"per_page": per_page, "page": page}
    try:
        resp = requests.get(url, headers=_github_headers(), params=params)
        if resp.status_code == 200:
            return resp.json()
        return {"error": f"{resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}

def add_labels_to_issue(owner: str, repo: str, issue_number: int, labels: List[str]) -> Any:
    """Add labels to an issue."""
    url = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com") + f"/repos/{owner}/{repo}/issues/{issue_number}/labels"
    data = {"labels": labels}
    try:
        resp = requests.post(url, headers=_github_headers(), json=data)
        if resp.status_code == 200:
            return resp.json()
        return {"error": f"{resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}

def set_labels_for_issue(owner: str, repo: str, issue_number: int, labels: List[str]) -> Any:
    """Set labels for an issue (replaces all labels)."""
    url = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com") + f"/repos/{owner}/{repo}/issues/{issue_number}/labels"
    data = {"labels": labels}
    try:
        resp = requests.put(url, headers=_github_headers(), json=data)
        if resp.status_code == 200:
            return resp.json()
        return {"error": f"{resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}

def remove_all_labels_from_issue(owner: str, repo: str, issue_number: int) -> Any:
    """Remove all labels from an issue."""
    url = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com") + f"/repos/{owner}/{repo}/issues/{issue_number}/labels"
    try:
        resp = requests.delete(url, headers=_github_headers())
        if resp.status_code == 204:
            return {"result": "All labels removed."}
        return {"error": f"{resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}

def remove_label_from_issue(owner: str, repo: str, issue_number: int, name: str) -> Any:
    """Remove a label from an issue."""
    url = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com") + f"/repos/{owner}/{repo}/issues/{issue_number}/labels/{name}"
    try:
        resp = requests.delete(url, headers=_github_headers())
        if resp.status_code == 200:
            return resp.json()
        return {"error": f"{resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}


def list_issue_comments_for_repository(owner: str, repo: str, sort: Optional[str] = None, direction: Optional[str] = None, since: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    """List comments on issues and pull requests for a repository."""
    url = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com") + f"/repos/{owner}/{repo}/issues/comments"
    params = {"sort": sort, "direction": direction, "since": since, "per_page": per_page, "page": page}
    params = {k: v for k, v in params.items() if v is not None}
    try:
        resp = requests.get(url, headers=_github_headers(), params=params)
        if resp.status_code == 200:
            return resp.json()
        return {"error": f"{resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}


def get_issue_comment(owner: str, repo: str, comment_id: int) -> Any:
    """Get an issue comment."""
    url = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com") + f"/repos/{owner}/{repo}/issues/comments/{comment_id}"
    try:
        resp = requests.get(url, headers=_github_headers())
        if resp.status_code == 200:
            return resp.json()
        return {"error": f"{resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}


def update_issue_comment(owner: str, repo: str, comment_id: int, body: str) -> Any:
    """Update an issue comment."""
    url = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com") + f"/repos/{owner}/{repo}/issues/comments/{comment_id}"
    data = {"body": body}
    try:
        resp = requests.patch(url, headers=_github_headers(), json=data)
        if resp.status_code == 200:
            return resp.json()
        return {"error": f"{resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}


def delete_issue_comment(owner: str, repo: str, comment_id: int) -> Any:
    """Delete an issue comment."""
    url = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com") + f"/repos/{owner}/{repo}/issues/comments/{comment_id}"
    try:
        resp = requests.delete(url, headers=_github_headers())
        if resp.status_code == 204:
            return {"result": "Comment deleted."}
        return {"error": f"{resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}


def list_assignees(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    """List available assignees for issues in a repository."""
    url = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com") + f"/repos/{owner}/{repo}/assignees"
    params = {"per_page": per_page, "page": page}
    try:
        resp = requests.get(url, headers=_github_headers(), params=params)
        if resp.status_code == 200:
            return resp.json()
        return {"error": f"{resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}


def check_if_user_can_be_assigned(owner: str, repo: str, assignee: str) -> Any:
    """Check if a user can be assigned to issues in a repository."""
    url = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com") + f"/repos/{owner}/{repo}/assignees/{assignee}"
    try:
        resp = requests.get(url, headers=_github_headers())
        if resp.status_code == 204:
            return {"result": "User can be assigned."}
        elif resp.status_code == 404:
            return {"error": "User cannot be assigned."}
        return {"error": f"{resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}


def add_assignees_to_issue(owner: str, repo: str, issue_number: int, assignees: list) -> Any:
    """Add assignees to an issue."""
    url = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com") + f"/repos/{owner}/{repo}/issues/{issue_number}/assignees"
    data = {"assignees": assignees}
    try:
        resp = requests.post(url, headers=_github_headers(), json=data)
        if resp.status_code == 201:
            return resp.json()
        return {"error": f"{resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}


def remove_assignees_from_issue(owner: str, repo: str, issue_number: int, assignees: list) -> Any:
    """Remove assignees from an issue."""
    url = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com") + f"/repos/{owner}/{repo}/issues/{issue_number}/assignees"
    data = {"assignees": assignees}
    try:
        resp = requests.delete(url, headers=_github_headers(), json=data)
        if resp.status_code == 200:
            return resp.json()
        return {"error": f"{resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}


def list_milestones(owner: str, repo: str, state: str = "open", sort: str = "due_on", direction: str = "asc", per_page: int = 30, page: int = 1) -> Any:
    """List milestones for a repository."""
    url = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com") + f"/repos/{owner}/{repo}/milestones"
    params = {"state": state, "sort": sort, "direction": direction, "per_page": per_page, "page": page}
    try:
        resp = requests.get(url, headers=_github_headers(), params=params)
        if resp.status_code == 200:
            return resp.json()
        return {"error": f"{resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}


def create_milestone(owner: str, repo: str, title: str, state: Optional[str] = None, description: Optional[str] = None, due_on: Optional[str] = None) -> Any:
    """Create a milestone."""
    url = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com") + f"/repos/{owner}/{repo}/milestones"
    data = {"title": title}
    if state:
        data["state"] = state
    if description:
        data["description"] = description
    if due_on:
        data["due_on"] = due_on
    try:
        resp = requests.post(url, headers=_github_headers(), json=data)
        if resp.status_code == 201:
            return resp.json()
        return {"error": f"{resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}


def get_milestone(owner: str, repo: str, milestone_number: int) -> Any:
    """Get a milestone by number."""
    url = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com") + f"/repos/{owner}/{repo}/milestones/{milestone_number}"
    try:
        resp = requests.get(url, headers=_github_headers())
        if resp.status_code == 200:
            return resp.json()
        return {"error": f"{resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}


def update_milestone(owner: str, repo: str, milestone_number: int, title: Optional[str] = None, state: Optional[str] = None, description: Optional[str] = None, due_on: Optional[str] = None) -> Any:
    """Update a milestone."""
    url = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com") + f"/repos/{owner}/{repo}/milestones/{milestone_number}"
    data = {}
    if title:
        data["title"] = title
    if state:
        data["state"] = state
    if description:
        data["description"] = description
    if due_on:
        data["due_on"] = due_on
    try:
        resp = requests.patch(url, headers=_github_headers(), json=data)
        if resp.status_code == 200:
            return resp.json()
        return {"error": f"{resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}


def delete_milestone(owner: str, repo: str, milestone_number: int) -> Any:
    """Delete a milestone by number."""
    url = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com") + f"/repos/{owner}/{repo}/milestones/{milestone_number}"
    try:
        resp = requests.delete(url, headers=_github_headers())
        if resp.status_code == 204:
            return {"result": "Milestone deleted."}
        return {"error": f"{resp.status_code}: {resp.text}"}
    except Exception as e:
        return {"error": str(e)}
