from typing import Any, Dict, Optional

from ._client import gh_request, parse_owner_repo


def get_content(
    *,
    path: str,
    ref: Optional[str] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    extra_headers = None
    if accept:
        extra_headers = {"Accept": accept}
    return gh_request(
        "GET",
        f"/repos/{o}/{r}/contents/{path.lstrip('/')}" if path else f"/repos/{o}/{r}/contents",
        params={"ref": ref},
        extra_headers=extra_headers,
    )


def create_or_update_file(
    *,
    path: str,
    message: str,
    content_base64: str,
    sha: Optional[str] = None,
    branch: Optional[str] = None,
    committer: Optional[dict] = None,
    author: Optional[dict] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    payload: Dict[str, Any] = {"message": message, "content": content_base64}
    for k, v in {"sha": sha, "branch": branch, "committer": committer, "author": author}.items():
        if v is not None:
            payload[k] = v
    return gh_request("PUT", f"/repos/{o}/{r}/contents/{path.lstrip('/')}" , json=payload)


def delete_file(
    *,
    path: str,
    message: str,
    sha: str,
    branch: Optional[str] = None,
    committer: Optional[dict] = None,
    author: Optional[dict] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    payload: Dict[str, Any] = {"message": message, "sha": sha}
    for k, v in {"branch": branch, "committer": committer, "author": author}.items():
        if v is not None:
            payload[k] = v
    return gh_request("DELETE", f"/repos/{o}/{r}/contents/{path.lstrip('/')}" , json=payload)
