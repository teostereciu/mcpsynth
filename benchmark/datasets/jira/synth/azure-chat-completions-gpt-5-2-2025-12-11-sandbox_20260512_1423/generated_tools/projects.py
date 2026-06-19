from typing import Any, Dict, List, Optional

from ._client import get_client


def project_search(start_at: int = 0, max_results: int = 50, order_by: Optional[str] = None,
                   ids: Optional[List[int]] = None, keys: Optional[List[str]] = None, query: Optional[str] = None,
                   type_key: Optional[str] = None, category_id: Optional[int] = None, action: Optional[str] = None,
                   expand: Optional[str] = None) -> Any:
    """GET /project/search"""
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if order_by is not None:
        params["orderBy"] = order_by
    if ids:
        params["id"] = ids
    if keys:
        params["keys"] = keys
    if query is not None:
        params["query"] = query
    if type_key is not None:
        params["typeKey"] = type_key
    if category_id is not None:
        params["categoryId"] = category_id
    if action is not None:
        params["action"] = action
    if expand is not None:
        params["expand"] = expand
    return get_client().request("GET", "/project/search", params=params)


def get_project(project_id_or_key: str, expand: Optional[str] = None, properties: Optional[List[str]] = None) -> Any:
    """GET /project/{projectIdOrKey}"""
    params: Dict[str, Any] = {}
    if expand is not None:
        params["expand"] = expand
    if properties:
        params["properties"] = ",".join(properties)
    return get_client().request("GET", f"/project/{project_id_or_key}", params=params or None)


def create_project(payload: Dict[str, Any]) -> Any:
    """POST /project"""
    return get_client().request("POST", "/project", json_body=payload)


def update_project(project_id_or_key: str, payload: Dict[str, Any]) -> Any:
    """PUT /project/{projectIdOrKey}"""
    return get_client().request("PUT", f"/project/{project_id_or_key}", json_body=payload)


def delete_project(project_id_or_key: str, enable_undo: Optional[bool] = None) -> Any:
    """DELETE /project/{projectIdOrKey}"""
    params: Dict[str, Any] = {}
    if enable_undo is not None:
        params["enableUndo"] = str(bool(enable_undo)).lower()
    return get_client().request("DELETE", f"/project/{project_id_or_key}", params=params or None)


def get_project_statuses(project_id_or_key: str) -> Any:
    """GET /project/{projectIdOrKey}/statuses"""
    return get_client().request("GET", f"/project/{project_id_or_key}/statuses")
