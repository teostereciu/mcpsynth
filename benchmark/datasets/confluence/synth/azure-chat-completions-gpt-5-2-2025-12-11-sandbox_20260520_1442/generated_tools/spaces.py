from typing import Any, Dict, Optional, List

from .http_client import ConfluenceClient


def list_spaces(
    *,
    ids: Optional[List[int]] = None,
    keys: Optional[List[str]] = None,
    type: Optional[str] = None,
    status: Optional[str] = None,
    labels: Optional[List[str]] = None,
    favorited_by: Optional[str] = None,
    not_favorited_by: Optional[str] = None,
    sort: Optional[str] = None,
    description_format: Optional[str] = None,
    include_icon: Optional[bool] = None,
    cursor: Optional[str] = None,
    limit: Optional[int] = 25,
) -> Dict[str, Any]:
    """GET /wiki/api/v2/spaces"""
    params: Dict[str, Any] = {}
    if ids:
        params["ids"] = ids
    if keys:
        params["keys"] = keys
    if type is not None:
        params["type"] = type
    if status is not None:
        params["status"] = status
    if labels:
        params["labels"] = labels
    if favorited_by is not None:
        params["favorited-by"] = favorited_by
    if not_favorited_by is not None:
        params["not-favorited-by"] = not_favorited_by
    if sort is not None:
        params["sort"] = sort
    if description_format is not None:
        params["description-format"] = description_format
    if include_icon is not None:
        params["include-icon"] = include_icon
    if cursor is not None:
        params["cursor"] = cursor
    if limit is not None:
        params["limit"] = limit

    return ConfluenceClient().request("GET", "/api/v2/spaces", params=params)  # type: ignore[return-value]


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
    params: Dict[str, Any] = {}
    if description_format is not None:
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

    return ConfluenceClient().request("GET", f"/api/v2/spaces/{space_id}", params=params)  # type: ignore[return-value]


def create_space(
    *,
    name: str,
    key: Optional[str] = None,
    alias: Optional[str] = None,
    description_value: Optional[str] = None,
    description_representation: Optional[str] = None,
    create_private_space: Optional[bool] = None,
    template_key: Optional[str] = None,
    copy_space_access_configuration: Optional[int] = None,
    role_assignments: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    """POST /wiki/api/v2/spaces"""
    payload: Dict[str, Any] = {"name": name}
    if key is not None:
        payload["key"] = key
    if alias is not None:
        payload["alias"] = alias
    if description_value is not None or description_representation is not None:
        payload["description"] = {
            "value": description_value or "",
            "representation": description_representation or "plain",
        }
    if role_assignments is not None:
        payload["roleAssignments"] = role_assignments
    if copy_space_access_configuration is not None:
        payload["copySpaceAccessConfiguration"] = copy_space_access_configuration
    if create_private_space is not None:
        payload["createPrivateSpace"] = create_private_space
    if template_key is not None:
        payload["templateKey"] = template_key

    return ConfluenceClient().request("POST", "/api/v2/spaces", json=payload)  # type: ignore[return-value]
