from typing import Any, List, Optional

from generated_tools.core import client


def get_labels(
    label_ids: Optional[List[int]] = None,
    prefix: Optional[List[str]] = None,
    cursor: Optional[str] = None,
    sort: Optional[str] = None,
    max_results: Optional[int] = None,
) -> Any:
    return client.request(
        "GET",
        "/api/v2/labels",
        params={"label-id": label_ids, "prefix": prefix, "cursor": cursor, "sort": sort, "max_results": max_results},
    )


def get_labels_for_attachment(attachment_id: int, prefix: Optional[str] = None, sort: Optional[str] = None, cursor: Optional[str] = None, max_results: Optional[int] = None) -> Any:
    return client.request("GET", f"/api/v2/attachments/{attachment_id}/labels", params={"prefix": prefix, "sort": sort, "cursor": cursor, "max_results": max_results})


def get_labels_for_blog_post(blog_post_id: int, prefix: Optional[str] = None, sort: Optional[str] = None, cursor: Optional[str] = None, max_results: Optional[int] = None) -> Any:
    return client.request("GET", f"/api/v2/blogposts/{blog_post_id}/labels", params={"prefix": prefix, "sort": sort, "cursor": cursor, "max_results": max_results})


def get_labels_for_custom_content(custom_content_id: int, prefix: Optional[str] = None, sort: Optional[str] = None, cursor: Optional[str] = None, max_results: Optional[int] = None) -> Any:
    return client.request("GET", f"/api/v2/custom-content/{custom_content_id}/labels", params={"prefix": prefix, "sort": sort, "cursor": cursor, "max_results": max_results})


def get_labels_for_page(page_id: int, prefix: Optional[str] = None, sort: Optional[str] = None, cursor: Optional[str] = None, max_results: Optional[int] = None) -> Any:
    return client.request("GET", f"/api/v2/pages/{page_id}/labels", params={"prefix": prefix, "sort": sort, "cursor": cursor, "max_results": max_results})


def get_labels_for_space(space_id: int, prefix: Optional[str] = None, sort: Optional[str] = None, cursor: Optional[str] = None, max_results: Optional[int] = None) -> Any:
    return client.request("GET", f"/api/v2/spaces/{space_id}/labels", params={"prefix": prefix, "sort": sort, "cursor": cursor, "max_results": max_results})


def get_labels_for_space_content(space_id: int, prefix: Optional[str] = None, sort: Optional[str] = None, cursor: Optional[str] = None, max_results: Optional[int] = None) -> Any:
    return client.request("GET", f"/api/v2/spaces/{space_id}/content/labels", params={"prefix": prefix, "sort": sort, "cursor": cursor, "max_results": max_results})
