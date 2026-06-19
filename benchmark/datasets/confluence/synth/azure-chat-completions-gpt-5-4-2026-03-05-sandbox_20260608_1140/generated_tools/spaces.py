from typing import Any, Optional

from confluence_client import client


def list_spaces(
    ids: Optional[list[int]] = None,
    keys: Optional[list[str]] = None,
    type: Optional[str] = None,
    status: Optional[str] = None,
    labels: Optional[list[str]] = None,
    sort: Optional[str] = None,
    description_format: Optional[str] = None,
    include_icon: Optional[bool] = None,
    cursor: Optional[str] = None,
    limit: Optional[int] = None,
) -> Any:
    return client.request(
        "GET",
        "/api/v2/spaces",
        params={
            "ids": ids,
            "keys": keys,
            "type": type,
            "status": status,
            "labels": labels,
            "sort": sort,
            "description-format": description_format,
            "include-icon": include_icon,
            "cursor": cursor,
            "limit": limit,
        },
    )


def create_space(
    name: str,
    key: Optional[str] = None,
    alias: Optional[str] = None,
    description_value: Optional[str] = None,
    description_representation: str = "plain",
    create_private_space: Optional[bool] = None,
    template_key: Optional[str] = None,
) -> Any:
    body = {"name": name}
    if key is not None:
        body["key"] = key
    if alias is not None:
        body["alias"] = alias
    if description_value is not None:
        body["description"] = {
            "value": description_value,
            "representation": description_representation,
        }
    if create_private_space is not None:
        body["createPrivateSpace"] = create_private_space
    if template_key is not None:
        body["templateKey"] = template_key
    return client.request("POST", "/api/v2/spaces", json_body=body)


def get_space(
    space_id: int,
    description_format: Optional[str] = None,
    include_icon: Optional[bool] = None,
    include_operations: Optional[bool] = None,
    include_properties: Optional[bool] = None,
    include_permissions: Optional[bool] = None,
    include_role_assignments: Optional[bool] = None,
    include_labels: Optional[bool] = None,
) -> Any:
    return client.request(
        "GET",
        f"/api/v2/spaces/{space_id}",
        params={
            "description-format": description_format,
            "include-icon": include_icon,
            "include-operations": include_operations,
            "include-properties": include_properties,
            "include-permissions": include_permissions,
            "include-role-assignments": include_role_assignments,
            "include-labels": include_labels,
        },
    )
