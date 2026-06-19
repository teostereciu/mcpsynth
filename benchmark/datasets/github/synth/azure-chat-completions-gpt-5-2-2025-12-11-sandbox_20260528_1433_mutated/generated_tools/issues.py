from typing import Any, Dict, List, Optional

from ._client import GitHubClient


# Source docs:
# - docs/api_issues-issues.md
# - docs/api_issues-comments.md


def list_my_issues(
    *,
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
    per_page: Optional[int] = None,
    page: Optional[int] = None,
) -> Any:
    """GET /issues"""
    gh = GitHubClient()
    return gh.request(
        "GET",
        "/issues",
        params={
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
        },
    )


def list_repo_issue_comments(
    owner: str,
    repo: str,
    *,
    sort: Optional[str] = None,
    direction: Optional[str] = None,
    since: Optional[str] = None,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
) -> Any:
    """GET /repos/{owner}/{repo}/issues/comments"""
    gh = GitHubClient()
    return gh.request(
        "GET",
        f"/repos/{owner}/{repo}/issues/comments",
        params={
            "sort": sort,
            "direction": direction,
            "since": since,
            "per_page": per_page,
            "page": page,
        },
    )


def get_issue_comment(owner: str, repo: str, comment_id: int) -> Any:
    """GET /repos/{owner}/{repo}/issues/comments/{comment_id}"""
    gh = GitHubClient()
    return gh.request(
        "GET",
        f"/repos/{owner}/{repo}/issues/comments/{comment_id}",
    )


def update_issue_comment(owner: str, repo: str, comment_id: int, body: str) -> Any:
    """PATCH /repos/{owner}/{repo}/issues/comments/{comment_id}"""
    gh = GitHubClient()
    return gh.request(
        "PATCH",
        f"/repos/{owner}/{repo}/issues/comments/{comment_id}",
        json_body={"body": body},
    )


def delete_issue_comment(owner: str, repo: str, comment_id: int) -> Any:
    """DELETE /repos/{owner}/{repo}/issues/comments/{comment_id}"""
    gh = GitHubClient()
    return gh.request(
        "DELETE",
        f"/repos/{owner}/{repo}/issues/comments/{comment_id}",
    )


def pin_issue_comment(owner: str, repo: str, comment_id: int) -> Any:
    """PUT /repos/{owner}/{repo}/issues/comments/{comment_id}/pin"""
    gh = GitHubClient()
    return gh.request(
        "PUT",
        f"/repos/{owner}/{repo}/issues/comments/{comment_id}/pin",
    )
