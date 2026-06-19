from typing import Any, Dict, Optional

from .github_client import GitHubClient


def list_releases(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/releases"""
    return client.request(
        "GET",
        f"/repos/{owner}/{repo}/releases",
        params={"per_page": per_page, "page": page},
    )


def get_release(client: GitHubClient, *, owner: str, repo: str, release_id: int) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/releases/{release_id}"""
    return client.request("GET", f"/repos/{owner}/{repo}/releases/{release_id}")


def get_latest_release(client: GitHubClient, *, owner: str, repo: str) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/releases/latest"""
    return client.request("GET", f"/repos/{owner}/{repo}/releases/latest")


def create_release(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    tag_name: str,
    target_commitish: Optional[str] = None,
    name: Optional[str] = None,
    body: Optional[str] = None,
    draft: Optional[bool] = None,
    prerelease: Optional[bool] = None,
    discussion_category_name: Optional[str] = None,
    generate_release_notes: Optional[bool] = None,
    make_latest: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /repos/{owner}/{repo}/releases"""
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
    return client.request("POST", f"/repos/{owner}/{repo}/releases", json=payload)


def update_release(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    release_id: int,
    tag_name: Optional[str] = None,
    target_commitish: Optional[str] = None,
    name: Optional[str] = None,
    body: Optional[str] = None,
    draft: Optional[bool] = None,
    prerelease: Optional[bool] = None,
    make_latest: Optional[str] = None,
) -> Dict[str, Any]:
    """PATCH /repos/{owner}/{repo}/releases/{release_id}"""
    payload: Dict[str, Any] = {}
    for k, v in {
        "tag_name": tag_name,
        "target_commitish": target_commitish,
        "name": name,
        "body": body,
        "draft": draft,
        "prerelease": prerelease,
        "make_latest": make_latest,
    }.items():
        if v is not None:
            payload[k] = v
    return client.request("PATCH", f"/repos/{owner}/{repo}/releases/{release_id}", json=payload)


def delete_release(client: GitHubClient, *, owner: str, repo: str, release_id: int) -> Dict[str, Any]:
    """DELETE /repos/{owner}/{repo}/releases/{release_id}"""
    return client.request("DELETE", f"/repos/{owner}/{repo}/releases/{release_id}")


def generate_release_notes(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    tag_name: str,
    target_commitish: Optional[str] = None,
    previous_tag_name: Optional[str] = None,
    configuration_file_path: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /repos/{owner}/{repo}/releases/generate-notes"""
    payload: Dict[str, Any] = {"tag_name": tag_name}
    for k, v in {
        "target_commitish": target_commitish,
        "previous_tag_name": previous_tag_name,
        "configuration_file_path": configuration_file_path,
    }.items():
        if v is not None:
            payload[k] = v
    return client.request("POST", f"/repos/{owner}/{repo}/releases/generate-notes", json=payload)
