from typing import Any, Dict, List, Optional

from generated_tools.core import client


def get_pages(
    ids: Optional[List[int]] = None,
    space_ids: Optional[List[int]] = None,
    sort: Optional[str] = None,
    content_status: Optional[List[str]] = None,
    title: Optional[str] = None,
    body_format: Optional[str] = None,
    subtype: Optional[str] = None,
    cursor: Optional[str] = None,
    max_results: Optional[int] = None,
) -> Any:
    return client.request(
        "GET",
        "/api/v2/pages",
        params={
            "id": ids,
            "space-id": space_ids,
            "sort": sort,
            "content_status": content_status,
            "title": title,
            "body-format": body_format,
            "subtype": subtype,
            "cursor": cursor,
            "max_results": max_results,
        },
    )


def create_page(
    title: str,
    body_value: str,
    space_id: Optional[str] = None,
    parent_id: Optional[str] = None,
    content_status: str = "current",
    representation: str = "storage",
    subtype: Optional[str] = None,
    embedded: Optional[bool] = None,
    private: Optional[bool] = None,
    root_level: Optional[bool] = None,
) -> Any:
    return client.request(
        "POST",
        "/api/v2/pages",
        params={"embedded": embedded, "private": private, "root-level": root_level},
        json={
            "spaceId": space_id or __import__("os").environ.get("CONFLUENCE_SPACE_KEY"),
            "content_status": content_status,
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
    content_status: Optional[List[str]] = None,
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
            "content_status": content_status,
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
    content_status: str = "current",
    representation: str = "storage",
    version_message: Optional[str] = None,
    space_id: Optional[str] = None,
    parent_id: Optional[str] = None,
    owner_id: Optional[str] = None,
) -> Any:
    return client.request(
        "PUT",
        f"/api/v2/pages/{page_id}",
        json={
            "id": str(page_id),
            "content_status": content_status,
            "title": title,
            "spaceId": space_id,
            "parentId": parent_id,
            "ownerId": owner_id,
            "body": {"representation": representation, "value": body_value},
            "version": {"number": version_number, "message": version_message},
        },
    )


def delete_page(page_id: int, purge: Optional[bool] = None, draft: Optional[bool] = None) -> Any:
    return client.request("DELETE", f"/api/v2/pages/{page_id}", params={"purge": purge, "draft": draft})


def update_page_title(page_id: int, title: str, content_status: str = "current") -> Any:
    return client.request(
        "PUT",
        f"/api/v2/pages/{page_id}/title",
        json={"content_status": content_status, "title": title},
    )


def get_pages_for_label(
    label_id: int,
    space_ids: Optional[List[int]] = None,
    body_format: Optional[str] = None,
    sort: Optional[str] = None,
    cursor: Optional[str] = None,
    max_results: Optional[int] = None,
) -> Any:
    return client.request(
        "GET",
        f"/api/v2/labels/{label_id}/pages",
        params={
            "space-id": space_ids,
            "body-format": body_format,
            "sort": sort,
            "cursor": cursor,
            "max_results": max_results,
        },
    )


def get_pages_in_space(
    space_id: int,
    depth: Optional[int] = None,
    sort: Optional[str] = None,
    status: Optional[str] = None,
    title: Optional[str] = None,
    body_format: Optional[str] = None,
    cursor: Optional[str] = None,
    max_results: Optional[int] = None,
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
            "max_results": max_results,
        },
    )
