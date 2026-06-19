from typing import Any, Dict, Optional

from .github_client import GitHubClient


def list_releases(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    """GET /repos/{owner}/{repo}/releases"""
    params = {"per_page": per_page, "page": page}
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/releases", params=params)


def get_release(owner: str, repo: str, release_id: int) -> Any:
    """GET /repos/{owner}/{repo}/releases/{release_id}"""
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/releases/{release_id}")


def create_release(owner: str, repo: str, tag_name: str, name: str, body: str = "", target_commitish: str = "main", draft: bool = False, prerelease: bool = False, generate_release_notes: bool = False) -> Any:
    """POST /repos/{owner}/{repo}/releases"""
    payload: Dict[str, Any] = {
        "tag_name": tag_name,
        "name": name,
        "body": body,
        "target_commitish": target_commitish,
        "draft": draft,
        "prerelease": prerelease,
        "generate_release_notes": generate_release_notes,
    }
    return GitHubClient().request("POST", f"/repos/{owner}/{repo}/releases", json=payload)


def update_release(owner: str, repo: str, release_id: int, tag_name: Optional[str] = None, name: Optional[str] = None, body: Optional[str] = None, target_commitish: Optional[str] = None, draft: Optional[bool] = None, prerelease: Optional[bool] = None, make_latest: Optional[str] = None) -> Any:
    """PATCH /repos/{owner}/{repo}/releases/{release_id}"""
    payload: Dict[str, Any] = {}
    if tag_name is not None:
        payload["tag_name"] = tag_name
    if name is not None:
        payload["name"] = name
    if body is not None:
        payload["body"] = body
    if target_commitish is not None:
        payload["target_commitish"] = target_commitish
    if draft is not None:
        payload["draft"] = draft
    if prerelease is not None:
        payload["prerelease"] = prerelease
    if make_latest is not None:
        payload["make_latest"] = make_latest
    return GitHubClient().request("PATCH", f"/repos/{owner}/{repo}/releases/{release_id}", json=payload)


def delete_release(owner: str, repo: str, release_id: int) -> Any:
    """DELETE /repos/{owner}/{repo}/releases/{release_id}"""
    return GitHubClient().request("DELETE", f"/repos/{owner}/{repo}/releases/{release_id}")
