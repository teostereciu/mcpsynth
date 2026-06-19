from typing import Any, Dict, Optional

from .github_client import GitHubClient, parse_owner_repo


def list_issues(owner_repo: str, state: str = "open", labels: Optional[str] = None, assignee: Optional[str] = None, creator: Optional[str] = None, mentioned: Optional[str] = None, since: Optional[str] = None, per_page: int = 100, max_pages: int = 5) -> Dict[str, Any]:
    """List issues in a repository (includes PRs unless filtered by GitHub)."""
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    params: Dict[str, Any] = {"state": state}
    if labels is not None:
        params["labels"] = labels
    if assignee is not None:
        params["assignee"] = assignee
    if creator is not None:
        params["creator"] = creator
    if mentioned is not None:
        params["mentioned"] = mentioned
    if since is not None:
        params["since"] = since
    return GitHubClient().paginate(f"/repos/{owner}/{repo}/issues", params=params, per_page=per_page, max_pages=max_pages)


def get_issue(owner_repo: str, issue_number: int) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}")


def create_issue(owner_repo: str, title: str, body: Optional[str] = None, assignees: Optional[list] = None, labels: Optional[list] = None, milestone: Optional[int] = None) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    payload: Dict[str, Any] = {"title": title}
    if body is not None:
        payload["body"] = body
    if assignees is not None:
        payload["assignees"] = assignees
    if labels is not None:
        payload["labels"] = labels
    if milestone is not None:
        payload["milestone"] = milestone
    return GitHubClient().request("POST", f"/repos/{owner}/{repo}/issues", json=payload)


def update_issue(owner_repo: str, issue_number: int, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None, assignees: Optional[list] = None, labels: Optional[list] = None, milestone: Optional[int] = None) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    payload: Dict[str, Any] = {}
    if title is not None:
        payload["title"] = title
    if body is not None:
        payload["body"] = body
    if state is not None:
        payload["state"] = state
    if assignees is not None:
        payload["assignees"] = assignees
    if labels is not None:
        payload["labels"] = labels
    if milestone is not None:
        payload["milestone"] = milestone
    return GitHubClient().request("PATCH", f"/repos/{owner}/{repo}/issues/{issue_number}", json=payload)


def lock_issue(owner_repo: str, issue_number: int, lock_reason: Optional[str] = None) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    payload = {"lock_reason": lock_reason} if lock_reason else None
    return GitHubClient().request("PUT", f"/repos/{owner}/{repo}/issues/{issue_number}/lock", json=payload)


def unlock_issue(owner_repo: str, issue_number: int) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().request("DELETE", f"/repos/{owner}/{repo}/issues/{issue_number}/lock")


def list_issue_comments(owner_repo: str, issue_number: int, per_page: int = 100, max_pages: int = 5) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().paginate(f"/repos/{owner}/{repo}/issues/{issue_number}/comments", per_page=per_page, max_pages=max_pages)


def create_issue_comment(owner_repo: str, issue_number: int, body: str) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/comments", json={"body": body})


def update_issue_comment(owner_repo: str, comment_id: int, body: str) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().request("PATCH", f"/repos/{owner}/{repo}/issues/comments/{comment_id}", json={"body": body})


def delete_issue_comment(owner_repo: str, comment_id: int) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().request("DELETE", f"/repos/{owner}/{repo}/issues/comments/{comment_id}")


def add_labels(owner_repo: str, issue_number: int, labels: list) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/labels", json=labels)


def set_labels(owner_repo: str, issue_number: int, labels: list) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().request("PUT", f"/repos/{owner}/{repo}/issues/{issue_number}/labels", json=labels)


def remove_label(owner_repo: str, issue_number: int, name: str) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().request("DELETE", f"/repos/{owner}/{repo}/issues/{issue_number}/labels/{name}")


def add_assignees(owner_repo: str, issue_number: int, assignees: list) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/assignees", json={"assignees": assignees})


def remove_assignees(owner_repo: str, issue_number: int, assignees: list) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().request("DELETE", f"/repos/{owner}/{repo}/issues/{issue_number}/assignees", json={"assignees": assignees})
