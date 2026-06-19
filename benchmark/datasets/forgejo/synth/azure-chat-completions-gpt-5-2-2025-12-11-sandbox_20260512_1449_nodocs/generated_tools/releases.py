from typing import Any, Dict, Optional

from .client import request_json


def list_releases(owner: str, repo: str, page: Optional[int] = None, limit: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    return request_json("GET", f"/repos/{owner}/{repo}/releases", params=params if params else None)


def get_release(owner: str, repo: str, release_id: int) -> Any:
    return request_json("GET", f"/repos/{owner}/{repo}/releases/{release_id}")


def create_release(owner: str, repo: str, tag_name: str, name: Optional[str] = None, body: Optional[str] = None, draft: Optional[bool] = None, prerelease: Optional[bool] = None, target_commitish: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {"tag_name": tag_name}
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
    return request_json("POST", f"/repos/{owner}/{repo}/releases", json=payload)
