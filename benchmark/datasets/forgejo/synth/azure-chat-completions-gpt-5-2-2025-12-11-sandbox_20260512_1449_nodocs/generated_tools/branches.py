from typing import Any, Dict, Optional

from .client import request_json


def list_branches(owner: str, repo: str, page: Optional[int] = None, limit: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    return request_json("GET", f"/repos/{owner}/{repo}/branches", params=params if params else None)


def get_branch(owner: str, repo: str, branch: str) -> Any:
    return request_json("GET", f"/repos/{owner}/{repo}/branches/{branch}")


def create_branch(owner: str, repo: str, new_branch_name: str, old_branch_name: str) -> Any:
    payload: Dict[str, Any] = {"new_branch_name": new_branch_name, "old_branch_name": old_branch_name}
    return request_json("POST", f"/repos/{owner}/{repo}/branches", json=payload)
