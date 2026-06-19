from typing import Any, Optional

from confluence_client import client


def list_pages(
    ids: Optional[list[int]] = None,
    space_ids: Optional[list[int]] = None,
    status: Optional[list[str]] = None,
    title: Optional[str] = None,
    body_format: Optional[str] = None,
    subtype: Optional[str] = None,
    sort: Optional[str] = None,
    cursor: Optional[str] = None,
    limit: Optional[int] = None,
) -> Any:
    return client.request(
        "GET",
        "/api/v2/pages",
        params={
            "id": ids,
            "space-id": space_ids,
            "status": status,
            "title": title,
            "body-format": body_format,
            "subtype": subtype,
            "sort": sort,
            "cursor": cursor,
            "limit": limit,
        },
    )


def create_page(
    title: str,
    body_value: str,
    space_id: Optional[str] = None,
    parent_id: Optional[str] = None,
    status: str = "current",
    representation: str = "storage",
    subtype: Optional[str] = None,
) -> Any:
    return client.request(
        "POST",
        "/api/v2/pages",
        json_body={
            "spaceId": space_id,
            "status": status,
            "title": title,
            "parentId": parent_id,
            "body": {"representation": representation, "value": body_value},
            "subtype": subtype,
        },
    )


def get_page(
    page_id: int,
    body_format: Optional[str] = None,
    get_draft: Optional[bool] = None,
    status: Optional[list[str]] = None,
    version: Optional[int] = None,
    include_labels: Optional[bool] = None,
    include_properties: Optional[bool] = None,
    include_operations: Optional[bool] = None,
    include_likes: Optional[bool] = None,
    include_versions: Optional[bool] = None,
    include_version: Optional[bool] = None,
) -> Any:
    return client.request(
        "GET",
        f"/api/v2/pages/{page_id}",
        params={
            "body-format": body_format,
            "get-draft": get_draft,
            "status": status,
            "version": version,
            "include-labels": include_labels,
            "include-properties": include_properties,
            "include-operations": include_operations,
            "include-likes": include_likes,
            "include-versions": include_versions,
            "include-version": include_version,
        },
    )


def update_page(
    page_id: int,
    title: str,
    body_value: str,
    version_number: int,
    status: str = "current",
    representation: str = "storage",
    version_message: Optional[str] = None,
    space_id: Optional[str] = None,
    parent_id: Optional[str] = None,
    owner_id: Optional[str] = None,
) -> Any:
    return client.request(
        "PUT",
        f"/api/v2/pages/{page_id}",
        json_body={
            "id": str(page_id),
            "status": status,
            "title": title,
            "spaceId": space_id,
            "parentId": parent_id,
            "ownerId": owner_id,
            "body": {"representation": representation, "value": body_value},
            "version": {"number": version_number, "message": version_message},
        },
    )


def delete_page(page_id: int, purge: Optional[bool] = None, draft: Optional[bool] = None) -> Any:
    return client.request(
        "DELETE",
        f"/api/v2/pages/{page_id}",
        params={"purge": purge, "draft": draft},
    )


def update_page_title(page_id: int, title: str, status: str = "current") -> Any:
    return client.request(
        "PUT",
        f"/api/v2/pages/{page_id}/title",
        json_body={"status": status, "title": title},
    )


def get_pages_for_label(
    label_id: int,
    body_format: Optional[str] = None,
    cursor: Optional[str] = None,
    limit: Optional[int] = None,
) -> Any:
    return client.request(
        "GET",
        f"/api/v2/labels/{label_id}/pages",
        params={"body-format": body_format, "cursor": cursor, "limit": limit},
    )


def get_pages_in_space(
    space_id: int,
    depth: Optional[int] = None,
    sort: Optional[str] = None,
    status: Optional[list[str]] = None,
    title: Optional[str] = None,
    body_format: Optional[str] = None,
    cursor: Optional[str] = None,
    limit: Optional[int] = None,
) -> Any:
    return client.request(
        "GET",
        f"/api/v2/spaces/{space_id}/pages",
        params={
            "depth": depth,
            "sort": sort,
            "status": status,
            "title": title,
            "body-format": body_format,
            "cursor": cursor,
            "limit": limit,
        },
    )
