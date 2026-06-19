from typing import Any, Dict, Optional

from .github_client import GitHubClient


def list_releases(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{repo}/releases", params={"per_page": per_page, "page": page})


def get_release(owner: str, repo: str, release_id: int) -> Any:
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{repo}/releases/{release_id}")


def create_release(owner: str, repo: str, tag_name: str, name: Optional[str] = None, body: Optional[str] = None, target_commitish: Optional[str] = None, draft: bool = False, prerelease: bool = False) -> Any:
    client = GitHubClient()
    payload: Dict[str, Any] = {"tag_name": tag_name, "draft": draft, "prerelease": prerelease}
    if name is not None:
        payload["name"] = name
    if body is not None:
        payload["body"] = body
    if target_commitish is not None:
        payload["target_commitish"] = target_commitish
    return client.request("POST", f"/repos/{owner}/{repo}/releases", json=payload)


def update_release(owner: str, repo: str, release_id: int, tag_name: Optional[str] = None, name: Optional[str] = None, body: Optional[str] = None, draft: Optional[bool] = None, prerelease: Optional[bool] = None) -> Any:
    client = GitHubClient()
    payload: Dict[str, Any] = {}
    if tag_name is not None:
        payload["tag_name"] = tag_name
    if name is not None:
        payload["name"] = name
    if body is not None:
        payload["body"] = body
    if draft is not None:
        payload["draft"] = draft
    if prerelease is not None:
        payload["prerelease"] = prerelease
    return client.request("PATCH", f"/repos/{owner}/{repo}/releases/{release_id}", json=payload)


def delete_release(owner: str, repo: str, release_id: int) -> Any:
    client = GitHubClient()
    return client.request("DELETE", f"/repos/{owner}/{repo}/releases/{release_id}")
