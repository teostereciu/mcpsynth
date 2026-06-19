from typing import Any, Dict, Optional

from .client import request_json


def list_pull_requests(owner: str, repo: str, state: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None) -> Any:
    params: Dict[str, Any] = {}
    if state is not None:
        params["state"] = state
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    return request_json("GET", f"/repos/{owner}/{repo}/pulls", params=params if params else None)


def get_pull_request(owner: str, repo: str, index: int) -> Any:
    return request_json("GET", f"/repos/{owner}/{repo}/pulls/{index}")


def create_pull_request(owner: str, repo: str, title: str, head: str, base: str, body: Optional[str] = None, draft: Optional[bool] = None) -> Any:
    payload: Dict[str, Any] = {"title": title, "head": head, "base": base}
    if body is not None:
        payload["body"] = body
    if draft is not None:
        payload["draft"] = draft
    return request_json("POST", f"/repos/{owner}/{repo}/pulls", json=payload)


def merge_pull_request(owner: str, repo: str, index: int, do: Optional[str] = None, merge_title_field: Optional[str] = None, merge_message_field: Optional[str] = None, delete_branch_after_merge: Optional[bool] = None) -> Any:
    payload: Dict[str, Any] = {}
    if do is not None:
        payload["Do"] = do
    if merge_title_field is not None:
        payload["MergeTitleField"] = merge_title_field
    if merge_message_field is not None:
        payload["MergeMessageField"] = merge_message_field
    if delete_branch_after_merge is not None:
        payload["delete_branch_after_merge"] = delete_branch_after_merge
    return request_json("POST", f"/repos/{owner}/{repo}/pulls/{index}/merge", json=payload if payload else {})
