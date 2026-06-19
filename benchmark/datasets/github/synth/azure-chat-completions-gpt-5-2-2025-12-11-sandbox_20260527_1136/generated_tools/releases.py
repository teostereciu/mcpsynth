from typing import Any, Dict, Optional

from .http_client import request_json, parse_owner_repo


# docs/api_releases-releases.md

def list_releases(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}
    return request_json(
        "GET",
        f"/repos/{o}/{r}/releases",
        accept=accept,
        params={"per_page": per_page, "page": page},
    )


# docs/api_releases-releases.md

def get_latest_release(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}
    return request_json("GET", f"/repos/{o}/{r}/releases/latest", accept=accept)


# docs/api_releases-releases.md

def create_release(
    *,
    tag_name: str,
    target_commitish: Optional[str] = None,
    name: Optional[str] = None,
    body: Optional[str] = None,
    draft: Optional[bool] = None,
    prerelease: Optional[bool] = None,
    discussion_category_name: Optional[str] = None,
    generate_release_notes: Optional[bool] = None,
    make_latest: Optional[str] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}

    payload: Dict[str, Any] = {"tag_name": tag_name}
    for k, v in {
        "target_commitish": target_commitish,
        "name": name,
        "body": body,
        "draft": draft,
        "prerelease": prerelease,
        "discussion_category_name": discussion_category_name,
        "generate_release_notes": generate_release_notes,
        "make_latest": make_latest,
    }.items():
        if v is not None:
            payload[k] = v

    return request_json("POST", f"/repos/{o}/{r}/releases", accept=accept, json=payload)


# docs/api_releases-releases.md

def generate_release_notes(
    *,
    tag_name: str,
    target_commitish: Optional[str] = None,
    previous_tag_name: Optional[str] = None,
    configuration_file_path: Optional[str] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}

    payload: Dict[str, Any] = {"tag_name": tag_name}
    for k, v in {
        "target_commitish": target_commitish,
        "previous_tag_name": previous_tag_name,
        "configuration_file_path": configuration_file_path,
    }.items():
        if v is not None:
            payload[k] = v

    return request_json(
        "POST",
        f"/repos/{o}/{r}/releases/generate-notes",
        accept=accept,
        json=payload,
    )
