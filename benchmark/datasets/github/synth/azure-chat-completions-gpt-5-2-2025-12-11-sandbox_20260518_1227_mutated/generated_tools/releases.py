from typing import Any, Dict, Optional

from .github_client import GitHubClient


def list_releases(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    per_page: int = 30,
    page: int = 1,
) -> Any:
    params: Dict[str, Any] = {"per_page": per_page, "page": page}
    return client.request("GET", f"/repos/{owner}/{repo}/releases", params=params)


def create_release(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    tag_name: str,
    target_commitish: Optional[str] = None,
    name: Optional[str] = None,
    body: Optional[str] = None,
    draft: bool = False,
    prerelease: bool = False,
    discussion_category_name: Optional[str] = None,
    generate_release_notes: bool = False,
    make_latest: Optional[str] = None,
) -> Any:
    payload: Dict[str, Any] = {
        "tag_name": tag_name,
        "draft": draft,
        "prerelease": prerelease,
        "generate_release_notes": generate_release_notes,
    }
    if target_commitish is not None:
        payload["target_commitish"] = target_commitish
    if name is not None:
        payload["name"] = name
    if body is not None:
        payload["body"] = body
    if discussion_category_name is not None:
        payload["discussion_category_name"] = discussion_category_name
    if make_latest is not None:
        payload["make_latest"] = make_latest

    return client.request("POST", f"/repos/{owner}/{repo}/releases", json=payload)


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
    payload: Dict[str, Any] = {"tag_name": tag_name}
    if target_commitish is not None:
        payload["target_commitish"] = target_commitish
    if previous_tag_name is not None:
        payload["previous_tag_name"] = previous_tag_name
    if configuration_file_path is not None:
        payload["configuration_file_path"] = configuration_file_path

    return client.request("POST", f"/repos/{owner}/{repo}/releases/generate-notes", json=payload)


def get_latest_release(client: GitHubClient, *, owner: str, repo: str) -> Any:
    return client.request("GET", f"/repos/{owner}/{repo}/releases/latest")
