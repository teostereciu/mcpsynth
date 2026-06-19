from typing import Any, Optional

from .http_client import request_json


def list_releases(
    *,
    owner: str,
    repo: str,
    per_page: int = 30,
    page: int = 1,
    accept: str = "application/vnd.github+json",
) -> Any:
    """GET /repos/{owner}/{repo}/releases - List releases."""
    _, data, _ = request_json(
        "GET",
        f"/repos/{owner}/{repo}/releases",
        params={"per_page": per_page, "page": page},
        accept=accept,
    )
    return data


def create_release(
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
    accept: str = "application/vnd.github+json",
) -> Any:
    """POST /repos/{owner}/{repo}/releases - Create a release."""
    _, data, _ = request_json(
        "POST",
        f"/repos/{owner}/{repo}/releases",
        json_body={
            "tag_name": tag_name,
            "target_commitish": target_commitish,
            "name": name,
            "body": body,
            "draft": draft,
            "prerelease": prerelease,
            "discussion_category_name": discussion_category_name,
            "generate_release_notes": generate_release_notes,
            "make_latest": make_latest,
        },
        accept=accept,
    )
    return data


def generate_release_notes(
    *,
    owner: str,
    repo: str,
    tag_name: str,
    target_commitish: Optional[str] = None,
    previous_tag_name: Optional[str] = None,
    configuration_file_path: Optional[str] = None,
    accept: str = "application/vnd.github+json",
) -> Any:
    """POST /repos/{owner}/{repo}/releases/generate-notes - Generate release notes content for a release."""
    _, data, _ = request_json(
        "POST",
        f"/repos/{owner}/{repo}/releases/generate-notes",
        json_body={
            "tag_name": tag_name,
            "target_commitish": target_commitish,
            "previous_tag_name": previous_tag_name,
            "configuration_file_path": configuration_file_path,
        },
        accept=accept,
    )
    return data


def get_latest_release(
    *,
    owner: str,
    repo: str,
    accept: str = "application/vnd.github+json",
) -> Any:
    """GET /repos/{owner}/{repo}/releases/latest - Get the latest release."""
    _, data, _ = request_json("GET", f"/repos/{owner}/{repo}/releases/latest", accept=accept)
    return data
