from typing import Any, Dict, Optional

from .http_client import request_json, parse_owner_repo


# docs/api_issues-comments.md

def list_repo_issue_comments(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    sort: Optional[str] = None,
    direction: Optional[str] = None,
    since: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}
    return request_json(
        "GET",
        f"/repos/{o}/{r}/issues/comments",
        accept=accept,
        params={
            "sort": sort,
            "direction": direction,
            "since": since,
            "per_page": per_page,
            "page": page,
        },
    )


# docs/api_issues-comments.md

def get_issue_comment(
    *,
    comment_id: int,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}
    return request_json("GET", f"/repos/{o}/{r}/issues/comments/{comment_id}", accept=accept)


# docs/api_issues-comments.md

def list_issue_comments(
    *,
    issue_number: int,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    since: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}
    return request_json(
        "GET",
        f"/repos/{o}/{r}/issues/{issue_number}/comments",
        accept=accept,
        params={"since": since, "per_page": per_page, "page": page},
    )


# docs/api_issues-comments.md

def create_issue_comment(
    *,
    issue_number: int,
    body: str,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}
    return request_json(
        "POST",
        f"/repos/{o}/{r}/issues/{issue_number}/comments",
        accept=accept,
        json={"body": body},
    )


# docs/api_issues-comments.md

def update_issue_comment(
    *,
    comment_id: int,
    body: str,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}
    return request_json(
        "PATCH",
        f"/repos/{o}/{r}/issues/comments/{comment_id}",
        accept=accept,
        json={"body": body},
    )


# docs/api_issues-comments.md

def delete_issue_comment(
    *,
    comment_id: int,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}
    return request_json("DELETE", f"/repos/{o}/{r}/issues/comments/{comment_id}", accept=accept)


# docs/api_issues-comments.md

def pin_issue_comment(
    *,
    comment_id: int,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}
    return request_json("PUT", f"/repos/{o}/{r}/issues/comments/{comment_id}/pin", accept=accept)


# docs/api_issues-comments.md

def unpin_issue_comment(
    *,
    comment_id: int,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}
    return request_json("DELETE", f"/repos/{o}/{r}/issues/comments/{comment_id}/pin", accept=accept)
