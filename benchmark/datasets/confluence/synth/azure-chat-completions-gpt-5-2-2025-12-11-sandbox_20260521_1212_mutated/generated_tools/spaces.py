import os
from typing import Any, Dict, Optional

from .http_client import ConfluenceClient


def list_spaces(
    keys: Optional[list[str]] = None,
    ids: Optional[list[int]] = None,
    space_type: Optional[str] = None,
    content_status: Optional[str] = None,
    labels: Optional[list[str]] = None,
    favorited_by: Optional[str] = None,
    not_favorited_by: Optional[str] = None,
    sort: Optional[str] = None,
    description_format: Optional[str] = None,
    include_icon: Optional[bool] = None,
    cursor: Optional[str] = None,
    max_results: int = 25,
) -> Dict[str, Any]:
    """GET /api/v2/spaces"""
    client = ConfluenceClient()
    params: Dict[str, Any] = {"max_results": max_results}
    if ids is not None:
        params["ids"] = ids
    if keys is not None:
        params["keys"] = keys
    if space_type is not None:
        params["type"] = space_type
    if content_status is not None:
        params["content_status"] = content_status
    if labels is not None:
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
    return client.request("GET", "/api/v2/spaces", params=params)


def get_space(space_id: int, description_format: Optional[str] = None, include_icon: Optional[bool] = None) -> Dict[str, Any]:
    """GET /api/v2/spaces/{id}"""
    client = ConfluenceClient()
    params: Dict[str, Any] = {}
    if description_format is not None:
        params["description-format"] = description_format
    if include_icon is not None:
        params["include-icon"] = include_icon
    return client.request("GET", f"/api/v2/spaces/{space_id}", params=params)


def create_space(
    name: str,
    key: Optional[str] = None,
    alias: Optional[str] = None,
    description_value: Optional[str] = None,
    description_representation: Optional[str] = None,
    create_private_space: Optional[bool] = None,
    template_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /api/v2/spaces"""
    client = ConfluenceClient()
    payload: Dict[str, Any] = {"name": name}
    if key is None:
        key = os.getenv("CONFLUENCE_SPACE_KEY")
    if key:
        payload["key"] = key
    if alias is not None:
        payload["alias"] = alias
    if description_value is not None:
        payload["description"] = {
            "value": description_value,
            "representation": description_representation or "plain",
        }
    if create_private_space is not None:
        payload["createPrivateSpace"] = create_private_space
    if template_key is not None:
        payload["templateKey"] = template_key
    return client.request("POST", "/api/v2/spaces", json=payload)
