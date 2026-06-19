from typing import Any, Dict, Optional

from .http_client import ConfluenceClient, ok_or_error


def list_spaces(
    *,
    keys: Optional[list[str]] = None,
    ids: Optional[list[int]] = None,
    space_type: Optional[str] = None,
    content_status: Optional[str] = None,
    labels: Optional[list[str]] = None,
    description_format: Optional[str] = None,
    include_icon: Optional[bool] = None,
    cursor: Optional[str] = None,
    max_results: int = 25,
) -> Dict[str, Any]:
    """GET /api/v2/spaces"""
    c = ConfluenceClient()
    params: Dict[str, Any] = {"limit": max_results}
    if keys:
        params["keys"] = keys
    if ids:
        params["ids"] = ids
    if space_type:
        params["type"] = space_type
    if content_status:
        params["status"] = content_status
    if labels:
        params["labels"] = labels
    if description_format:
        params["description-format"] = description_format
    if include_icon is not None:
        params["include-icon"] = str(include_icon).lower()
    if cursor:
        params["cursor"] = cursor

    status, body, headers = c.request("GET", "/api/v2/spaces", params=params)
    return ok_or_error(status, body, headers)


def get_space(space_id: int, *, include_icon: Optional[bool] = None, include_permissions: Optional[bool] = None) -> Dict[str, Any]:
    """GET /api/v2/spaces/{id}"""
    c = ConfluenceClient()
    params: Dict[str, Any] = {}
    if include_icon is not None:
        params["include-icon"] = str(include_icon).lower()
    if include_permissions is not None:
        params["include-permissions"] = str(include_permissions).lower()
    status, body, headers = c.request("GET", f"/api/v2/spaces/{space_id}", params=params)
    return ok_or_error(status, body, headers)


def create_space(
    *,
    name: str,
    key: Optional[str] = None,
    description_value: Optional[str] = None,
    description_representation: str = "plain",
    create_private_space: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /api/v2/spaces"""
    c = ConfluenceClient()
    payload: Dict[str, Any] = {"name": name}
    if key:
        payload["key"] = key
    if description_value is not None:
        payload["description"] = {"value": description_value, "representation": description_representation}
    if create_private_space is not None:
        payload["createPrivateSpace"] = create_private_space

    status, body, headers = c.request("POST", "/api/v2/spaces", json_body=payload)
    return ok_or_error(status, body, headers)
