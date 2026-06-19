from typing import Any, Dict, List, Optional, Union

from .http_client import GitHubClient, parse_owner_repo


def list_repo_issue_comments(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    sort: str = "created",
    direction: Optional[str] = None,
    since: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """GET /repos/{owner}/{repo}/issues/comments"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    params: Dict[str, Any] = {"sort": sort, "per_page": per_page, "page": page}
    if direction is not None:
        params["direction"] = direction
    if since is not None:
        params["since"] = since
    return client.request("GET", f"/repos/{o}/{r}/issues/comments", params=params, accept=accept)


def list_issue_comments(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    issue_number: int,
    since: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """GET /repos/{owner}/{repo}/issues/{issue_number}/comments"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    params: Dict[str, Any] = {"per_page": per_page, "page": page}
    if since is not None:
        params["since"] = since
    return client.request("GET", f"/repos/{o}/{r}/issues/{issue_number}/comments", params=params, accept=accept)


def get_issue_comment(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    comment_id: int,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """GET /repos/{owner}/{repo}/issues/comments/{comment_id}"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{o}/{r}/issues/comments/{comment_id}", accept=accept)


def create_issue_comment(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    issue_number: int,
    body: str,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """POST /repos/{owner}/{repo}/issues/{issue_number}/comments"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    return client.request(
        "POST",
        f"/repos/{o}/{r}/issues/{issue_number}/comments",
        json={"body": body},
        accept=accept,
    )


def update_issue_comment(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    comment_id: int,
    body: str,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """PATCH /repos/{owner}/{repo}/issues/comments/{comment_id}"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    return client.request(
        "PATCH",
        f"/repos/{o}/{r}/issues/comments/{comment_id}",
        json={"body": body},
        accept=accept,
    )


def delete_issue_comment(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    comment_id: int,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """DELETE /repos/{owner}/{repo}/issues/comments/{comment_id}"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    return client.request("DELETE", f"/repos/{o}/{r}/issues/comments/{comment_id}", accept=accept)


def pin_issue_comment(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    comment_id: int,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """PUT /repos/{owner}/{repo}/issues/comments/{comment_id}/pin"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    return client.request("PUT", f"/repos/{o}/{r}/issues/comments/{comment_id}/pin", accept=accept)


def unpin_issue_comment(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    comment_id: int,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """DELETE /repos/{owner}/{repo}/issues/comments/{comment_id}/pin"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    return client.request("DELETE", f"/repos/{o}/{r}/issues/comments/{comment_id}/pin", accept=accept)
