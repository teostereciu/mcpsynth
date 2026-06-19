from typing import Any, Dict, Optional

from ._client import gh_request, parse_owner_repo


def list_pull_reviews(
    *,
    pull_number: int,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    return gh_request(
        "GET",
        f"/repos/{o}/{r}/pulls/{pull_number}/reviews",
        params={"per_page": per_page, "page": page},
    )


def create_pull_review(
    *,
    pull_number: int,
    event: Optional[str] = None,
    body: Optional[str] = None,
    commit_id: Optional[str] = None,
    comments: Optional[list[dict]] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    payload: Dict[str, Any] = {}
    if event is not None:
        payload["event"] = event
    if body is not None:
        payload["body"] = body
    if commit_id is not None:
        payload["commit_id"] = commit_id
    if comments is not None:
        payload["comments"] = comments
    return gh_request("POST", f"/repos/{o}/{r}/pulls/{pull_number}/reviews", json=payload)


def get_pull_review(
    *,
    pull_number: int,
    review_id: int,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    return gh_request("GET", f"/repos/{o}/{r}/pulls/{pull_number}/reviews/{review_id}")


def submit_pull_review(
    *,
    pull_number: int,
    review_id: int,
    event: str,
    body: Optional[str] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    payload: Dict[str, Any] = {"event": event}
    if body is not None:
        payload["body"] = body
    return gh_request(
        "POST",
        f"/repos/{o}/{r}/pulls/{pull_number}/reviews/{review_id}/events",
        json=payload,
    )


def dismiss_pull_review(
    *,
    pull_number: int,
    review_id: int,
    message: str,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    return gh_request(
        "PUT",
        f"/repos/{o}/{r}/pulls/{pull_number}/reviews/{review_id}/dismissals",
        json={"message": message},
    )
