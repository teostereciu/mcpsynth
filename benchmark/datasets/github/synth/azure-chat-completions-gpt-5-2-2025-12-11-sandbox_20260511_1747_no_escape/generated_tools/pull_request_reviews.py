from typing import Any, Dict, List, Optional, Union

from .http_client import GitHubClient, parse_owner_repo


def list_pull_request_reviews(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    pull_number: int,
    per_page: int = 30,
    page: int = 1,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """GET /repos/{owner}/{repo}/pulls/{pull_number}/reviews"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    params = {"per_page": per_page, "page": page}
    return client.request("GET", f"/repos/{o}/{r}/pulls/{pull_number}/reviews", params=params, accept=accept)


def create_pull_request_review(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    pull_number: int,
    commit_id: Optional[str] = None,
    body: Optional[str] = None,
    event: Optional[str] = None,
    comments: Optional[List[Dict[str, Any]]] = None,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """POST /repos/{owner}/{repo}/pulls/{pull_number}/reviews"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {}
    if commit_id is not None:
        payload["commit_id"] = commit_id
    if body is not None:
        payload["body"] = body
    if event is not None:
        payload["event"] = event
    if comments is not None:
        payload["comments"] = comments
    return client.request("POST", f"/repos/{o}/{r}/pulls/{pull_number}/reviews", json=payload, accept=accept)


def get_pull_request_review(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    pull_number: int,
    review_id: int,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """GET /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{o}/{r}/pulls/{pull_number}/reviews/{review_id}", accept=accept)


def submit_pull_request_review(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    pull_number: int,
    review_id: int,
    event: str,
    body: Optional[str] = None,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """POST /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/events"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {"event": event}
    if body is not None:
        payload["body"] = body
    return client.request(
        "POST",
        f"/repos/{o}/{r}/pulls/{pull_number}/reviews/{review_id}/events",
        json=payload,
        accept=accept,
    )


def dismiss_pull_request_review(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    pull_number: int,
    review_id: int,
    message: str,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """PUT /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/dismissals"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    return client.request(
        "PUT",
        f"/repos/{o}/{r}/pulls/{pull_number}/reviews/{review_id}/dismissals",
        json={"message": message},
        accept=accept,
    )
