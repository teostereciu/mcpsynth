from typing import Any, Dict, Optional

from .github_client import GitHubClient


def list_repo_issue_comments(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    sort: str = "created",
    direction: Optional[str] = None,
    since: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
) -> Any:
    params: Dict[str, Any] = {"sort": sort, "per_page": per_page, "page": page}
    if direction is not None:
        params["direction"] = direction
    if since is not None:
        params["since"] = since
    return client.request("GET", f"/repos/{owner}/{repo}/issues/comments", params=params)


def list_issue_comments(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    issue_number: int,
    since: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
) -> Any:
    params: Dict[str, Any] = {"per_page": per_page, "page": page}
    if since is not None:
        params["since"] = since
    return client.request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}/comments", params=params)


def get_issue_comment(client: GitHubClient, *, owner: str, repo: str, comment_id: int) -> Any:
    return client.request("GET", f"/repos/{owner}/{repo}/issues/comments/{comment_id}")


def create_issue_comment(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    issue_number: int,
    body: str,
) -> Any:
    return client.request(
        "POST",
        f"/repos/{owner}/{repo}/issues/{issue_number}/comments",
        json={"body": body},
    )


def update_issue_comment(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    comment_id: int,
    body: str,
) -> Any:
    return client.request(
        "PATCH",
        f"/repos/{owner}/{repo}/issues/comments/{comment_id}",
        json={"body": body},
    )


def delete_issue_comment(client: GitHubClient, *, owner: str, repo: str, comment_id: int) -> Any:
    return client.request("DELETE", f"/repos/{owner}/{repo}/issues/comments/{comment_id}")
