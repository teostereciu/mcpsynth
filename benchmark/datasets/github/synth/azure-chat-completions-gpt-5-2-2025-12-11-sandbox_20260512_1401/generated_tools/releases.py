from typing import Any, Dict, Optional

from ._client import GitHubClient


def list_releases(*, owner: str, repo: str, per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/releases - List releases."""
    c = GitHubClient()
    return c.request(
        "GET", f"/repos/{owner}/{repo}/releases", params={"per_page": per_page, "page": page}
    )


def create_release(
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
    """POST /repos/{owner}/{repo}/releases - Create a release."""
    c = GitHubClient()
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
    return c.request("POST", f"/repos/{owner}/{repo}/releases", json=payload)


def generate_release_notes(
    *,
    owner: str,
    repo: str,
    tag_name: str,
    target_commitish: Optional[str] = None,
    previous_tag_name: Optional[str] = None,
    configuration_file_path: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /repos/{owner}/{repo}/releases/generate-notes - Generate release notes content."""
    c = GitHubClient()
    payload: Dict[str, Any] = {"tag_name": tag_name}
    for k, v in {
        "target_commitish": target_commitish,
        "previous_tag_name": previous_tag_name,
        "configuration_file_path": configuration_file_path,
    }.items():
        if v is not None:
            payload[k] = v
    return c.request("POST", f"/repos/{owner}/{repo}/releases/generate-notes", json=payload)


def get_latest_release(*, owner: str, repo: str) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/releases/latest - Get the latest release."""
    c = GitHubClient()
    return c.request("GET", f"/repos/{owner}/{repo}/releases/latest")
