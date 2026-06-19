from typing import Any, Dict, Optional

from ._client import GitHubClient


def list_repo_issue_comments(
    *,
    owner: str,
    repo: str,
    sort: Optional[str] = None,
    direction: Optional[str] = None,
    since: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/issues/comments - List issue comments for a repository."""
    c = GitHubClient()
    return c.request(
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


def list_issue_comments(
    *, owner: str, repo: str, issue_number: int, per_page: int = 30, page: int = 1
) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/issues/{issue_number}/comments - List issue comments."""
    c = GitHubClient()
    return c.request(
        "GET",
        f"/repos/{owner}/{repo}/issues/{issue_number}/comments",
        params={"per_page": per_page, "page": page},
    )


def create_issue_comment(*, owner: str, repo: str, issue_number: int, body: str) -> Dict[str, Any]:
    """POST /repos/{owner}/{repo}/issues/{issue_number}/comments - Create an issue comment."""
    c = GitHubClient()
    return c.request(
        "POST", f"/repos/{owner}/{repo}/issues/{issue_number}/comments", json={"body": body}
    )


def get_issue_comment(*, owner: str, repo: str, comment_id: int) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/issues/comments/{comment_id} - Get an issue comment."""
    c = GitHubClient()
    return c.request("GET", f"/repos/{owner}/{repo}/issues/comments/{comment_id}")


def update_issue_comment(*, owner: str, repo: str, comment_id: int, body: str) -> Dict[str, Any]:
    """PATCH /repos/{owner}/{repo}/issues/comments/{comment_id} - Update an issue comment."""
    c = GitHubClient()
    return c.request(
        "PATCH", f"/repos/{owner}/{repo}/issues/comments/{comment_id}", json={"body": body}
    )


def delete_issue_comment(*, owner: str, repo: str, comment_id: int) -> Dict[str, Any]:
    """DELETE /repos/{owner}/{repo}/issues/comments/{comment_id} - Delete an issue comment."""
    c = GitHubClient()
    return c.request("DELETE", f"/repos/{owner}/{repo}/issues/comments/{comment_id}")
