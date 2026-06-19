from typing import Any, List, Optional

from generated_tools.core import client


def get_spaces(
    ids: Optional[List[int]] = None,
    keys: Optional[List[str]] = None,
    type: Optional[str] = None,
    content_status: Optional[str] = None,
    labels: Optional[List[str]] = None,
    favorited_by: Optional[str] = None,
    not_favorited_by: Optional[str] = None,
    sort: Optional[str] = None,
    description_format: Optional[str] = None,
    include_icon: Optional[bool] = None,
    cursor: Optional[str] = None,
    max_results: Optional[int] = None,
) -> Any:
    return client.request(
        "GET",
        "/api/v2/spaces",
        params={
            "ids": ids,
            "keys": keys,
            "type": type,
            "content_status": content_status,
            "labels": labels,
            "favorited-by": favorited_by,
            "not-favorited-by": not_favorited_by,
            "sort": sort,
            "description-format": description_format,
            "include-icon": include_icon,
            "cursor": cursor,
            "max_results": max_results,
        },
    )


def create_space(
    name: str,
    key: Optional[str] = None,
    alias: Optional[str] = None,
    description_value: Optional[str] = None,
    description_representation: str = "plain",
    role_assignments: Optional[list] = None,
    copy_space_access_configuration: Optional[int] = None,
    create_private_space: Optional[bool] = None,
    template_key: Optional[str] = None,
) -> Any:
    description = None
    if description_value is not None:
        description = {"value": description_value, "representation": description_representation}
    return client.request(
        "POST",
        "/api/v2/spaces",
        json={
            "name": name,
            "key": key,
            "alias": alias,
            "description": description,
            "roleAssignments": role_assignments,
            "copySpaceAccessConfiguration": copy_space_access_configuration,
            "createPrivateSpace": create_private_space,
            "templateKey": template_key,
        },
    )


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
