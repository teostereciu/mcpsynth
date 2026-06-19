from typing import Any, Dict, List, Optional, Union

from .http_client import GitHubClient, parse_owner_repo


def list_releases(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """GET /repos/{owner}/{repo}/releases"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    params = {"per_page": per_page, "page": page}
    return client.request("GET", f"/repos/{o}/{r}/releases", params=params, accept=accept)


def create_release(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    tag_name: str,
    target_commitish: Optional[str] = None,
    name: Optional[str] = None,
    body: Optional[str] = None,
    draft: Optional[bool] = None,
    prerelease: Optional[bool] = None,
    discussion_category_name: Optional[str] = None,
    generate_release_notes: Optional[bool] = None,
    make_latest: Optional[Union[bool, str]] = None,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """POST /repos/{owner}/{repo}/releases"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
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
    return client.request("POST", f"/repos/{o}/{r}/releases", json=payload, accept=accept)


def generate_release_notes(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    tag_name: str,
    target_commitish: Optional[str] = None,
    previous_tag_name: Optional[str] = None,
    configuration_file_path: Optional[str] = None,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """POST /repos/{owner}/{repo}/releases/generate-notes"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {"tag_name": tag_name}
    for k, v in {
        "target_commitish": target_commitish,
        "previous_tag_name": previous_tag_name,
        "configuration_file_path": configuration_file_path,
    }.items():
        if v is not None:
            payload[k] = v
    return client.request("POST", f"/repos/{o}/{r}/releases/generate-notes", json=payload, accept=accept)


def get_latest_release(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """GET /repos/{owner}/{repo}/releases/latest"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{o}/{r}/releases/latest", accept=accept)
