from __future__ import annotations

from typing import Any, Dict, Optional

from .http_client import ConfluenceClient


def list_spaces(
    *,
    keys: Optional[list[str]] = None,
    ids: Optional[list[int]] = None,
    type: Optional[str] = None,
    status: Optional[str] = None,
    limit: int = 25,
    cursor: Optional[str] = None,
    sort: Optional[str] = None,
    include_icon: Optional[bool] = None,
    description_format: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /wiki/api/v2/spaces"""
    client = ConfluenceClient.from_env()
    params: Dict[str, Any] = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    if keys:
        params["keys"] = keys
    if ids:
        params["ids"] = ids
    if type:
        params["type"] = type
    if status:
        params["status"] = status
    if sort:
        params["sort"] = sort
    if include_icon is not None:
        params["include-icon"] = include_icon
    if description_format:
        params["description-format"] = description_format
    return client.request("GET", "/api/v2/spaces", params=params)


def get_space(
    *,
    space_id: int,
    description_format: Optional[str] = None,
    include_icon: Optional[bool] = None,
    include_operations: Optional[bool] = None,
    include_properties: Optional[bool] = None,
    include_permissions: Optional[bool] = None,
    include_role_assignments: Optional[bool] = None,
    include_labels: Optional[bool] = None,
) -> Dict[str, Any]:
    """GET /wiki/api/v2/spaces/{id}"""
    client = ConfluenceClient.from_env()
    params: Dict[str, Any] = {}
    if description_format:
        params["description-format"] = description_format
    if include_icon is not None:
        params["include-icon"] = include_icon
    if include_operations is not None:
        params["include-operations"] = include_operations
    if include_properties is not None:
        params["include-properties"] = include_properties
    if include_permissions is not None:
        params["include-permissions"] = include_permissions
    if include_role_assignments is not None:
        params["include-role-assignments"] = include_role_assignments
    if include_labels is not None:
        params["include-labels"] = include_labels
    return client.request("GET", f"/api/v2/spaces/{space_id}", params=params or None)


def create_space(
    *,
    name: str,
    key: Optional[str] = None,
    alias: Optional[str] = None,
    description_value: Optional[str] = None,
    description_representation: Optional[str] = None,
    create_private_space: Optional[bool] = None,
    template_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /wiki/api/v2/spaces"""
    client = ConfluenceClient.from_env()
    body: Dict[str, Any] = {"name": name}
    if key is not None:
        body["key"] = key
    if alias is not None:
        body["alias"] = alias
    if description_value is not None:
        body["description"] = {
            "value": description_value,
            "representation": description_representation or "plain",
        }
    if create_private_space is not None:
        body["createPrivateSpace"] = create_private_space
    if template_key is not None:
        body["templateKey"] = template_key

    return client.request(
        "POST",
        "/api/v2/spaces",
        json_body=body,
        content_type="application/json",
    )
