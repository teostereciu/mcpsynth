from typing import Any, Dict, Optional

from .http_client import request_json, parse_owner_repo


# docs/api_repos-contents.md

def get_repo_content(
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
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}
    return request_json(
        "GET",
        f"/repos/{o}/{r}/contents/{path}",
        accept=accept,
        params={"ref": ref},
    )


# docs/api_repos-contents.md

def create_or_update_file(
    *,
    path: str,
    message: str,
    content_base64: str,
    sha: Optional[str] = None,
    branch: Optional[str] = None,
    committer: Optional[Dict[str, Any]] = None,
    author: Optional[Dict[str, Any]] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}

    payload: Dict[str, Any] = {"message": message, "content": content_base64}
    if sha is not None:
        payload["sha"] = sha
    if branch is not None:
        payload["branch"] = branch
    if committer is not None:
        payload["committer"] = committer
    if author is not None:
        payload["author"] = author

    return request_json(
        "PUT",
        f"/repos/{o}/{r}/contents/{path}",
        accept=accept,
        json=payload,
    )


# docs/api_repos-contents.md

def delete_file(
    *,
    path: str,
    message: str,
    sha: str,
    branch: Optional[str] = None,
    committer: Optional[Dict[str, Any]] = None,
    author: Optional[Dict[str, Any]] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}

    payload: Dict[str, Any] = {"message": message, "sha": sha}
    if branch is not None:
        payload["branch"] = branch
    if committer is not None:
        payload["committer"] = committer
    if author is not None:
        payload["author"] = author

    return request_json(
        "DELETE",
        f"/repos/{o}/{r}/contents/{path}",
        accept=accept,
        json=payload,
    )
