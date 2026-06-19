from typing import Any, List, Optional

from generated_tools.core import client


def get_attachments(
    sort: Optional[str] = None,
    cursor: Optional[str] = None,
    content_status: Optional[List[str]] = None,
    media_type: Optional[str] = None,
    filename: Optional[str] = None,
    max_results: Optional[int] = None,
) -> Any:
    return client.request(
        "GET",
        "/api/v2/attachments",
        params={
            "sort": sort,
            "cursor": cursor,
            "content_status": content_status,
            "mediaType": media_type,
            "filename": filename,
            "max_results": max_results,
        },
    )


def get_attachment(attachment_id: str, **params: Any) -> Any:
    return client.request("GET", f"/api/v2/attachments/{attachment_id}", params=params)


def delete_attachment(attachment_id: int, purge: Optional[bool] = None) -> Any:
    return client.request("DELETE", f"/api/v2/attachments/{attachment_id}", params={"purge": purge})


def get_attachments_for_blog_post(blog_post_id: int, **params: Any) -> Any:
    return client.request("GET", f"/api/v2/blogposts/{blog_post_id}/attachments", params=params)


def get_attachments_for_custom_content(custom_content_id: int, **params: Any) -> Any:
    return client.request("GET", f"/api/v2/custom-content/{custom_content_id}/attachments", params=params)


def get_attachments_for_label(
    label_id: int,
    sort: Optional[str] = None,
    cursor: Optional[str] = None,
    max_results: Optional[int] = None,
) -> Any:
    return client.request(
        "GET",
        f"/api/v2/labels/{label_id}/attachments",
        params={"sort": sort, "cursor": cursor, "max_results": max_results},
    )


def get_attachments_for_page(page_id: int, **params: Any) -> Any:
    return client.request("GET", f"/api/v2/pages/{page_id}/attachments", params=params)


def get_attachment_thumbnail_download(
    attachment_id: str,
    version: Optional[int] = None,
    height: Optional[int] = None,
    width: Optional[int] = None,
) -> Any:
    return client.request(
        "GET",
        f"/api/v2/attachments/{attachment_id}/thumbnail/download",
        params={"version": version, "height": height, "width": width},
    )
