from typing import Any, Dict, List, Optional, Union

from .http_client import GitHubClient, parse_owner_repo


def list_my_issues(
    *,
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
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """GET /issues"""
    client = GitHubClient()
    params: Dict[str, Any] = {
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
        params["collab"] = collab
    if orgs is not None:
        params["orgs"] = orgs
    if owned is not None:
        params["owned"] = owned
    if pulls is not None:
        params["pulls"] = pulls
    return client.request("GET", "/issues", params=params, accept=accept)


def list_repo_issues(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    milestone: Optional[str] = None,
    state: str = "open",
    assignee: Optional[str] = None,
    creator: Optional[str] = None,
    mentioned: Optional[str] = None,
    labels: Optional[str] = None,
    sort: str = "created",
    direction: str = "desc",
    since: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
) -> Union[Dict[str, Any], List[Any], str]:
    """GET /repos/{owner}/{repo}/issues"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    params: Dict[str, Any] = {
        "state": state,
        "sort": sort,
        "direction": direction,
        "per_page": per_page,
        "page": page,
    }
    if milestone is not None:
        params["milestone"] = milestone
    if assignee is not None:
        params["assignee"] = assignee
    if creator is not None:
        params["creator"] = creator
    if mentioned is not None:
        params["mentioned"] = mentioned
    if labels is not None:
        params["labels"] = labels
    if since is not None:
        params["since"] = since
    return client.request("GET", f"/repos/{o}/{r}/issues", params=params)


def get_issue(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    issue_number: int,
) -> Union[Dict[str, Any], List[Any], str]:
    """GET /repos/{owner}/{repo}/issues/{issue_number}"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{o}/{r}/issues/{issue_number}")


def create_issue(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    title: str,
    body: Optional[str] = None,
    assignees: Optional[List[str]] = None,
    milestone: Optional[int] = None,
    labels: Optional[List[str]] = None,
) -> Union[Dict[str, Any], List[Any], str]:
    """POST /repos/{owner}/{repo}/issues"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {"title": title}
    if body is not None:
        payload["body"] = body
    if assignees is not None:
        payload["assignees"] = assignees
    if milestone is not None:
        payload["milestone"] = milestone
    if labels is not None:
        payload["labels"] = labels
    return client.request("POST", f"/repos/{o}/{r}/issues", json=payload)


def update_issue(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    issue_number: int,
    title: Optional[str] = None,
    body: Optional[str] = None,
    state: Optional[str] = None,
    state_reason: Optional[str] = None,
    assignees: Optional[List[str]] = None,
    milestone: Optional[Union[int, None]] = None,
    labels: Optional[List[str]] = None,
) -> Union[Dict[str, Any], List[Any], str]:
    """PATCH /repos/{owner}/{repo}/issues/{issue_number}"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {}
    if title is not None:
        payload["title"] = title
    if body is not None:
        payload["body"] = body
    if state is not None:
        payload["state"] = state
    if state_reason is not None:
        payload["state_reason"] = state_reason
    if assignees is not None:
        payload["assignees"] = assignees
    if milestone is not None:
        payload["milestone"] = milestone
    if labels is not None:
        payload["labels"] = labels
    return client.request("PATCH", f"/repos/{o}/{r}/issues/{issue_number}", json=payload)


def lock_issue(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    issue_number: int,
    lock_reason: Optional[str] = None,
) -> Union[Dict[str, Any], List[Any], str]:
    """PUT /repos/{owner}/{repo}/issues/{issue_number}/lock"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {}
    if lock_reason is not None:
        payload["lock_reason"] = lock_reason
    return client.request("PUT", f"/repos/{o}/{r}/issues/{issue_number}/lock", json=payload or None)


def unlock_issue(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    issue_number: int,
) -> Union[Dict[str, Any], List[Any], str]:
    """DELETE /repos/{owner}/{repo}/issues/{issue_number}/lock"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    return client.request("DELETE", f"/repos/{o}/{r}/issues/{issue_number}/lock")
