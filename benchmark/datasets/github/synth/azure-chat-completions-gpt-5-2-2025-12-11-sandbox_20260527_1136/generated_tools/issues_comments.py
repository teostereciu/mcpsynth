from typing import Any, Dict, Optional

from .http_client import GitHubClient


def list_issue_comments_for_repo(
    owner: str,
    repo: str,
    *,
    sort: Optional[str] = None,
    direction: Optional[str] = None,
    since: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/issues/comments"""
    return GitHubClient().request(
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


def get_issue_comment(owner: str, repo: str, comment_id: int) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/issues/comments/{comment_id}"""
    return GitHubClient().request(
        "GET", f"/repos/{owner}/{repo}/issues/comments/{comment_id}"
    )


def update_issue_comment(
    owner: str, repo: str, comment_id: int, *, body: str
) -> Dict[str, Any]:
    """PATCH /repos/{owner}/{repo}/issues/comments/{comment_id}"""
    return GitHubClient().request(
        "PATCH",
        f"/repos/{owner}/{repo}/issues/comments/{comment_id}",
        json={"body": body},
    )


def delete_issue_comment(owner: str, repo: str, comment_id: int) -> Dict[str, Any]:
    """DELETE /repos/{owner}/{repo}/issues/comments/{comment_id}"""
    return GitHubClient().request(
        "DELETE", f"/repos/{owner}/{repo}/issues/comments/{comment_id}"
    )


def pin_issue_comment(owner: str, repo: str, comment_id: int) -> Dict[str, Any]:
    """PUT /repos/{owner}/{repo}/issues/comments/{comment_id}/pin"""
    return GitHubClient().request(
        "PUT", f"/repos/{owner}/{repo}/issues/comments/{comment_id}/pin"
    )
