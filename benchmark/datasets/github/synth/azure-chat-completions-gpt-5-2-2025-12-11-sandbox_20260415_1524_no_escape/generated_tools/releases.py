from __future__ import annotations

from typing import Any, Dict, Optional

from .github_client import GitHubClient


def list_releases(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    per_page: int = 30,
    page: int = 1,
    paginate: bool = False,
) -> Any:
    params = {"per_page": per_page, "page": page}
    return client.request("GET", f"/repos/{owner}/{repo}/releases", params=params, paginate=paginate)


def get_latest_release(client: GitHubClient, *, owner: str, repo: str) -> Any:
    return client.request("GET", f"/repos/{owner}/{repo}/releases/latest")


def get_release(client: GitHubClient, *, owner: str, repo: str, release_id: int) -> Any:
    return client.request("GET", f"/repos/{owner}/{repo}/releases/{release_id}")


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
) -> Any:
    payload: Dict[str, Any] = {
        "tag_name": tag_name,
        "target_commitish": target_commitish,
        "name": name,
        "body": body,
        "draft": draft,
        "prerelease": prerelease,
        "discussion_category_name": discussion_category_name,
        "generate_release_notes": generate_release_notes,
        "make_latest": make_latest,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
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
) -> Any:
    payload: Dict[str, Any] = {
        "tag_name": tag_name,
        "target_commitish": target_commitish,
        "name": name,
        "body": body,
        "draft": draft,
        "prerelease": prerelease,
        "make_latest": make_latest,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    return client.request("PATCH", f"/repos/{owner}/{repo}/releases/{release_id}", json=payload)


def delete_release(client: GitHubClient, *, owner: str, repo: str, release_id: int) -> Any:
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
) -> Any:
    payload: Dict[str, Any] = {
        "tag_name": tag_name,
        "target_commitish": target_commitish,
        "previous_tag_name": previous_tag_name,
        "configuration_file_path": configuration_file_path,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    return client.request("POST", f"/repos/{owner}/{repo}/releases/generate-notes", json=payload)
