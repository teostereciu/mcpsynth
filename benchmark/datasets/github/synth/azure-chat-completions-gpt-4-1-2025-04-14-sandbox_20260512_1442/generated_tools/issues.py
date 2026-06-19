import os
import requests
from typing import List, Optional, Dict, Any

def _github_headers():
    token = os.environ.get("GITHUB_TOKEN")
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2026-03-10",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers

def list_issues_assigned_to_authenticated_user(
    filter: str = "assigned",
    state: str = "open",
    labels: Optional[str] = None,
    sort: str = "created",
    direction: str = "desc",
    since: Optional[str] = None,
    collab: Optional[bool] = None,
    orgs: Optional[bool] = None,
    owned: Optional[bool] = None,
    pulls: Optional[bool] = None,
    per_page: int = 30,
    page: int = 1,
) -> Any:
    """List issues assigned to the authenticated user across all visible repositories."""
    url = f"{os.environ.get('GITHUB_API_BASE_URL', 'https://api.github.com')}/issues"
    params = {
        "filter": filter,
        "state": state,
        "sort": sort,
        "direction": direction,
        "per_page": per_page,
        "page": page,
    }
    if labels is not None:
        params["labels"] = labels
    if since is not None:
        params["since"] = since
    if collab is not None:
        params["collab"] = str(collab).lower()
    if orgs is not None:
        params["orgs"] = str(orgs).lower()
    if owned is not None:
        params["owned"] = str(owned).lower()
    if pulls is not None:
        params["pulls"] = str(pulls).lower()
    resp = requests.get(url, headers=_github_headers(), params=params)
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text, "status_code": resp.status_code}

def list_labels_for_issue(owner: str, repo: str, issue_number: int, per_page: int = 30, page: int = 1) -> Any:
    """List all labels for an issue."""
    url = f"{os.environ.get('GITHUB_API_BASE_URL', 'https://api.github.com')}/repos/{owner}/{repo}/issues/{issue_number}/labels"
    params = {"per_page": per_page, "page": page}
    resp = requests.get(url, headers=_github_headers(), params=params)
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text, "status_code": resp.status_code}

def add_labels_to_issue(owner: str, repo: str, issue_number: int, labels: List[str]) -> Any:
    """Add labels to an issue."""
    url = f"{os.environ.get('GITHUB_API_BASE_URL', 'https://api.github.com')}/repos/{owner}/{repo}/issues/{issue_number}/labels"
    data = {"labels": labels}
    resp = requests.post(url, headers=_github_headers(), json=data)
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text, "status_code": resp.status_code}

def set_labels_for_issue(owner: str, repo: str, issue_number: int, labels: List[str]) -> Any:
    """Set labels for an issue (replaces all labels)."""
    url = f"{os.environ.get('GITHUB_API_BASE_URL', 'https://api.github.com')}/repos/{owner}/{repo}/issues/{issue_number}/labels"
    data = {"labels": labels}
    resp = requests.put(url, headers=_github_headers(), json=data)
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text, "status_code": resp.status_code}

def remove_all_labels_from_issue(owner: str, repo: str, issue_number: int) -> Any:
    """Remove all labels from an issue."""
    url = f"{os.environ.get('GITHUB_API_BASE_URL', 'https://api.github.com')}/repos/{owner}/{repo}/issues/{issue_number}/labels"
    resp = requests.delete(url, headers=_github_headers())
    if resp.status_code == 204:
        return {"result": "All labels removed."}
    else:
        return {"error": resp.text, "status_code": resp.status_code}

def remove_label_from_issue(owner: str, repo: str, issue_number: int, name: str) -> Any:
    """Remove a label from an issue."""
    url = f"{os.environ.get('GITHUB_API_BASE_URL', 'https://api.github.com')}/repos/{owner}/{repo}/issues/{issue_number}/labels/{name}"
    resp = requests.delete(url, headers=_github_headers())
    if resp.status_code == 200:
        return resp.json()
    else:
        return {"error": resp.text, "status_code": resp.status_code}

def list_assignees(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    """List available assignees for issues in a repository."""
    url = f"{os.environ.get('GITHUB_API_BASE_URL', 'https://api.github.com')}/repos/{owner}/{repo}/assignees"
    params = {"per_page": per_page, "page": page}
    resp = requests.get(url, headers=_github_headers(), params=params)
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text, "status_code": resp.status_code}

def check_user_can_be_assigned(owner: str, repo: str, assignee: str) -> Any:
    """Check if a user can be assigned to issues in a repository."""
    url = f"{os.environ.get('GITHUB_API_BASE_URL', 'https://api.github.com')}/repos/{owner}/{repo}/assignees/{assignee}"
    resp = requests.get(url, headers=_github_headers())
    if resp.status_code == 204:
        return {"result": True}
    elif resp.status_code == 404:
        return {"result": False}
    else:
        return {"error": resp.text, "status_code": resp.status_code}

def add_assignees_to_issue(owner: str, repo: str, issue_number: int, assignees: List[str]) -> Any:
    """Add assignees to an issue."""
    url = f"{os.environ.get('GITHUB_API_BASE_URL', 'https://api.github.com')}/repos/{owner}/{repo}/issues/{issue_number}/assignees"
    data = {"assignees": assignees}
    resp = requests.post(url, headers=_github_headers(), json=data)
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text, "status_code": resp.status_code}

def remove_assignees_from_issue(owner: str, repo: str, issue_number: int, assignees: List[str]) -> Any:
    """Remove assignees from an issue."""
    url = f"{os.environ.get('GITHUB_API_BASE_URL', 'https://api.github.com')}/repos/{owner}/{repo}/issues/{issue_number}/assignees"
    data = {"assignees": assignees}
    resp = requests.delete(url, headers=_github_headers(), json=data)
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text, "status_code": resp.status_code}

def list_issue_comments_for_repo(owner: str, repo: str, sort: str = "created", direction: str = "asc", since: str = None, per_page: int = 30, page: int = 1) -> Any:
    """List comments on issues and pull requests for a repository."""
    url = f"{os.environ.get('GITHUB_API_BASE_URL', 'https://api.github.com')}/repos/{owner}/{repo}/issues/comments"
    params = {"sort": sort, "direction": direction, "per_page": per_page, "page": page}
    if since:
        params["since"] = since
    resp = requests.get(url, headers=_github_headers(), params=params)
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text, "status_code": resp.status_code}

def get_issue_comment(owner: str, repo: str, comment_id: int) -> Any:
    """Get a single comment on an issue or pull request."""
    url = f"{os.environ.get('GITHUB_API_BASE_URL', 'https://api.github.com')}/repos/{owner}/{repo}/issues/comments/{comment_id}"
    resp = requests.get(url, headers=_github_headers())
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text, "status_code": resp.status_code}

def update_issue_comment(owner: str, repo: str, comment_id: int, body: str) -> Any:
    """Update a comment on an issue or pull request."""
    url = f"{os.environ.get('GITHUB_API_BASE_URL', 'https://api.github.com')}/repos/{owner}/{repo}/issues/comments/{comment_id}"
    data = {"body": body}
    resp = requests.patch(url, headers=_github_headers(), json=data)
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text, "status_code": resp.status_code}

def delete_issue_comment(owner: str, repo: str, comment_id: int) -> Any:
    """Delete a comment on an issue or pull request."""
    url = f"{os.environ.get('GITHUB_API_BASE_URL', 'https://api.github.com')}/repos/{owner}/{repo}/issues/comments/{comment_id}"
    resp = requests.delete(url, headers=_github_headers())
    if resp.status_code == 204:
        return {"result": "Comment deleted."}
    else:
        return {"error": resp.text, "status_code": resp.status_code}

def list_milestones(owner: str, repo: str, state: str = "open", sort: str = "due_on", direction: str = "asc", per_page: int = 30, page: int = 1) -> Any:
    """List milestones for a repository."""
    url = f"{os.environ.get('GITHUB_API_BASE_URL', 'https://api.github.com')}/repos/{owner}/{repo}/milestones"
    params = {"state": state, "sort": sort, "direction": direction, "per_page": per_page, "page": page}
    resp = requests.get(url, headers=_github_headers(), params=params)
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text, "status_code": resp.status_code}

def create_milestone(owner: str, repo: str, title: str, state: str = "open", description: str = None, due_on: str = None) -> Any:
    """Create a milestone for a repository."""
    url = f"{os.environ.get('GITHUB_API_BASE_URL', 'https://api.github.com')}/repos/{owner}/{repo}/milestones"
    data = {"title": title, "state": state}
    if description is not None:
        data["description"] = description
    if due_on is not None:
        data["due_on"] = due_on
    resp = requests.post(url, headers=_github_headers(), json=data)
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text, "status_code": resp.status_code}

def get_milestone(owner: str, repo: str, milestone_number: int) -> Any:
    """Get a milestone by number."""
    url = f"{os.environ.get('GITHUB_API_BASE_URL', 'https://api.github.com')}/repos/{owner}/{repo}/milestones/{milestone_number}"
    resp = requests.get(url, headers=_github_headers())
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text, "status_code": resp.status_code}

def update_milestone(owner: str, repo: str, milestone_number: int, title: str = None, state: str = None, description: str = None, due_on: str = None) -> Any:
    """Update a milestone by number."""
    url = f"{os.environ.get('GITHUB_API_BASE_URL', 'https://api.github.com')}/repos/{owner}/{repo}/milestones/{milestone_number}"
    data = {}
    if title is not None:
        data["title"] = title
    if state is not None:
        data["state"] = state
    if description is not None:
        data["description"] = description
    if due_on is not None:
        data["due_on"] = due_on
    resp = requests.patch(url, headers=_github_headers(), json=data)
    try:
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return {"error": resp.text, "status_code": resp.status_code}

def delete_milestone(owner: str, repo: str, milestone_number: int) -> Any:
    """Delete a milestone by number."""
    url = f"{os.environ.get('GITHUB_API_BASE_URL', 'https://api.github.com')}/repos/{owner}/{repo}/milestones/{milestone_number}"
    resp = requests.delete(url, headers=_github_headers())
    if resp.status_code == 204:
        return {"result": "Milestone deleted."}
    else:
        return {"error": resp.text, "status_code": resp.status_code}
