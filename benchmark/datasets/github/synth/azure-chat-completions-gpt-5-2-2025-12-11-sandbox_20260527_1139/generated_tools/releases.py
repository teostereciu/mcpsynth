from typing import Any, Dict, Optional

from ._client import request_json, split_owner_repo


def list_releases(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: Optional[str] = None,
) -> Any:
    """GET /repos/{owner}/{repo}/releases

    List releases for a repository.
    """
    if owner is None or repo is None:
        parts = split_owner_repo(owner_repo)
        owner = owner or parts["owner"]
        repo = repo or parts["repo"]

    params: Dict[str, Any] = {"per_page": per_page, "page": page}
    return request_json("GET", f"/repos/{owner}/{repo}/releases", params=params, accept=accept)


def create_release(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    tag_name: str,
    target_commitish: Optional[str] = None,
    name: Optional[str] = None,
    body: Optional[str] = None,
    draft: bool = False,
    prerelease: bool = False,
    discussion_category_name: Optional[str] = None,
    generate_release_notes: bool = False,
    make_latest: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    """POST /repos/{owner}/{repo}/releases

    Create a release.
    """
    if owner is None or repo is None:
        parts = split_owner_repo(owner_repo)
        owner = owner or parts["owner"]
        repo = repo or parts["repo"]

    payload: Dict[str, Any] = {
        "tag_name": tag_name,
        "draft": draft,
        "prerelease": prerelease,
        "generate_release_notes": generate_release_notes,
    }
    for k, v in {
        "target_commitish": target_commitish,
        "name": name,
        "body": body,
        "discussion_category_name": discussion_category_name,
        "make_latest": make_latest,
    }.items():
        if v is not None:
            payload[k] = v

    return request_json("POST", f"/repos/{owner}/{repo}/releases", json=payload, accept=accept)


def generate_release_notes(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    tag_name: str,
    target_commitish: Optional[str] = None,
    previous_tag_name: Optional[str] = None,
    configuration_file_path: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    """POST /repos/{owner}/{repo}/releases/generate-notes

    Generate release notes content for a release.
    """
    if owner is None or repo is None:
        parts = split_owner_repo(owner_repo)
        owner = owner or parts["owner"]
        repo = repo or parts["repo"]

    payload: Dict[str, Any] = {"tag_name": tag_name}
    for k, v in {
        "target_commitish": target_commitish,
        "previous_tag_name": previous_tag_name,
        "configuration_file_path": configuration_file_path,
    }.items():
        if v is not None:
            payload[k] = v

    return request_json("POST", f"/repos/{owner}/{repo}/releases/generate-notes", json=payload, accept=accept)
