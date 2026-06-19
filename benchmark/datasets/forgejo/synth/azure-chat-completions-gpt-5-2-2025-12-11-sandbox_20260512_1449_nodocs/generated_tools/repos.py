from typing import Any, Dict, Optional

from .client import request_json


def list_my_repos(page: Optional[int] = None, limit: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    return request_json("GET", "/user/repos", params=params if params else None)


def get_repo(owner: str, repo: str) -> Any:
    return request_json("GET", f"/repos/{owner}/{repo}")


def create_repo(name: str, description: Optional[str] = None, private: Optional[bool] = None, auto_init: Optional[bool] = None, default_branch: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {"name": name}
    if description is not None:
        payload["description"] = description
    if private is not None:
        payload["private"] = private
    if auto_init is not None:
        payload["auto_init"] = auto_init
    if default_branch is not None:
        payload["default_branch"] = default_branch
    return request_json("POST", "/user/repos", json=payload)


def delete_repo(owner: str, repo: str) -> Any:
    return request_json("DELETE", f"/repos/{owner}/{repo}")


def fork_repo(owner: str, repo: str, organization: Optional[str] = None, name: Optional[str] = None) -> Any:
    payload: Dict[str, Any] = {}
    if organization is not None:
        payload["organization"] = organization
    if name is not None:
        payload["name"] = name
    return request_json("POST", f"/repos/{owner}/{repo}/forks", json=payload if payload else {})
