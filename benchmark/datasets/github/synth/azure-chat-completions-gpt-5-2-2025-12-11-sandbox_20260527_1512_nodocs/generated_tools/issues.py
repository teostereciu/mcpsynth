from typing import Any, Dict, Optional

from ._client import GitHubClient, split_repo


def list_issues(repo: str, state: str = "open", labels: Optional[str] = None, assignee: Optional[str] = None, creator: Optional[str] = None, mentioned: Optional[str] = None, since: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    """List issues in a repository (includes PRs unless filtered by GitHub)."""
    owner, name = split_repo(repo)
    client = GitHubClient()
    params: Dict[str, Any] = {"state": state, "per_page": per_page, "page": page}
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
    return client.request("GET", f"/repos/{owner}/{name}/issues", params=params)


def get_issue(repo: str, issue_number: int) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{name}/issues/{issue_number}")


def create_issue(repo: str, title: str, body: Optional[str] = None, assignees: Optional[list] = None, labels: Optional[list] = None, milestone: Optional[int] = None) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {"title": title}
    if body is not None:
        payload["body"] = body
    if assignees is not None:
        payload["assignees"] = assignees
    if labels is not None:
        payload["labels"] = labels
    if milestone is not None:
        payload["milestone"] = milestone
    return client.request("POST", f"/repos/{owner}/{name}/issues", json=payload, expected=(201,))


def update_issue(repo: str, issue_number: int, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None, assignees: Optional[list] = None, labels: Optional[list] = None, milestone: Optional[int] = None) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
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
    return client.request("PATCH", f"/repos/{owner}/{name}/issues/{issue_number}", json=payload)


def lock_issue(repo: str, issue_number: int, lock_reason: Optional[str] = None) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    payload = {"lock_reason": lock_reason} if lock_reason else None
    return client.request("PUT", f"/repos/{owner}/{name}/issues/{issue_number}/lock", json=payload, expected=(204,))


def unlock_issue(repo: str, issue_number: int) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("DELETE", f"/repos/{owner}/{name}/issues/{issue_number}/lock", expected=(204,))


def list_issue_comments(repo: str, issue_number: int, per_page: int = 30, page: int = 1) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{name}/issues/{issue_number}/comments", params={"per_page": per_page, "page": page})


def create_issue_comment(repo: str, issue_number: int, body: str) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("POST", f"/repos/{owner}/{name}/issues/{issue_number}/comments", json={"body": body}, expected=(201,))


def update_issue_comment(repo: str, comment_id: int, body: str) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("PATCH", f"/repos/{owner}/{name}/issues/comments/{comment_id}", json={"body": body})


def delete_issue_comment(repo: str, comment_id: int) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("DELETE", f"/repos/{owner}/{name}/issues/comments/{comment_id}", expected=(204,))


def add_issue_labels(repo: str, issue_number: int, labels: list) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("POST", f"/repos/{owner}/{name}/issues/{issue_number}/labels", json={"labels": labels}, expected=(200, 201))


def set_issue_labels(repo: str, issue_number: int, labels: list) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("PUT", f"/repos/{owner}/{name}/issues/{issue_number}/labels", json={"labels": labels})


def remove_issue_label(repo: str, issue_number: int, name_label: str) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("DELETE", f"/repos/{owner}/{name}/issues/{issue_number}/labels/{name_label}", expected=(200, 204))


def list_labels(repo: str, per_page: int = 30, page: int = 1) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{name}/labels", params={"per_page": per_page, "page": page})


def create_label(repo: str, name_label: str, color: str, description: Optional[str] = None) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {"name": name_label, "color": color}
    if description is not None:
        payload["description"] = description
    return client.request("POST", f"/repos/{owner}/{name}/labels", json=payload, expected=(201,))


def update_label(repo: str, current_name: str, new_name: Optional[str] = None, color: Optional[str] = None, description: Optional[str] = None) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {}
    if new_name is not None:
        payload["new_name"] = new_name
    if color is not None:
        payload["color"] = color
    if description is not None:
        payload["description"] = description
    return client.request("PATCH", f"/repos/{owner}/{name}/labels/{current_name}", json=payload)


def delete_label(repo: str, name_label: str) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("DELETE", f"/repos/{owner}/{name}/labels/{name_label}", expected=(204,))
