from typing import Any, Dict, Optional

from .http import request_json


def list_releases(owner: str, repo: str, *, per_page: int = 30, page: int = 1) -> Any:
    return request_json("GET", f"/repos/{owner}/{repo}/releases", params={"per_page": per_page, "page": page})


def get_release(owner: str, repo: str, release_id: int) -> Any:
    return request_json("GET", f"/repos/{owner}/{repo}/releases/{release_id}")


def get_latest_release(owner: str, repo: str) -> Any:
    return request_json("GET", f"/repos/{owner}/{repo}/releases/latest")


def create_release(owner: str, repo: str, tag_name: str, *, name: Optional[str] = None, body: str = "", target_commitish: str = "main", draft: bool = False, prerelease: bool = False, generate_release_notes: bool = False) -> Any:
    payload: Dict[str, Any] = {
        "tag_name": tag_name,
        "body": body,
        "target_commitish": target_commitish,
        "draft": draft,
        "prerelease": prerelease,
        "generate_release_notes": generate_release_notes,
    }
    if name is not None:
        payload["name"] = name
    return request_json("POST", f"/repos/{owner}/{repo}/releases", json=payload)


def update_release(owner: str, repo: str, release_id: int, *, tag_name: Optional[str] = None, name: Optional[str] = None, body: Optional[str] = None, draft: Optional[bool] = None, prerelease: Optional[bool] = None, target_commitish: Optional[str] = None) -> Any:
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
    if target_commitish is not None:
        payload["target_commitish"] = target_commitish
    return request_json("PATCH", f"/repos/{owner}/{repo}/releases/{release_id}", json=payload)


def delete_release(owner: str, repo: str, release_id: int) -> Any:
    return request_json("DELETE", f"/repos/{owner}/{repo}/releases/{release_id}")
