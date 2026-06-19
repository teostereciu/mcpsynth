from typing import Any, List, Optional

from generated_tools.core import client


def get_blog_posts(
    ids: Optional[List[int]] = None,
    space_ids: Optional[List[int]] = None,
    sort: Optional[str] = None,
    content_status: Optional[List[str]] = None,
    title: Optional[str] = None,
    body_format: Optional[str] = None,
    cursor: Optional[str] = None,
    max_results: Optional[int] = None,
) -> Any:
    return client.request(
        "GET",
        "/api/v2/blogposts",
        params={
            "id": ids,
            "space-id": space_ids,
            "sort": sort,
            "content_status": content_status,
            "title": title,
            "body-format": body_format,
            "cursor": cursor,
            "max_results": max_results,
        },
    )


def create_blog_post(
    title: str,
    body_value: str,
    space_id: str,
    content_status: str = "current",
    representation: str = "storage",
    created_at: Optional[str] = None,
    private: Optional[bool] = None,
) -> Any:
    return client.request(
        "POST",
        "/api/v2/blogposts",
        params={"private": private},
        json={
            "spaceId": space_id,
            "content_status": content_status,
            "title": title,
            "body": {"representation": representation, "value": body_value},
            "createdAt": created_at,
        },
    )


def get_blog_post(blog_post_id: int, **params: Any) -> Any:
    return client.request("GET", f"/api/v2/blogposts/{blog_post_id}", params=params)


def update_blog_post(
    blog_post_id: int,
    title: str,
    body_value: str,
    version_number: int,
    content_status: str = "current",
    representation: str = "storage",
    space_id: Optional[str] = None,
    version_message: Optional[str] = None,
    created_at: Optional[str] = None,
) -> Any:
    return client.request(
        "PUT",
        f"/api/v2/blogposts/{blog_post_id}",
        json={
            "id": str(blog_post_id),
            "content_status": content_status,
            "title": title,
            "spaceId": space_id,
            "body": {"representation": representation, "value": body_value},
            "version": {"number": version_number, "message": version_message},
            "createdAt": created_at,
        },
    )


def delete_blog_post(blog_post_id: int, purge: Optional[bool] = None, draft: Optional[bool] = None) -> Any:
    return client.request("DELETE", f"/api/v2/blogposts/{blog_post_id}", params={"purge": purge, "draft": draft})


def get_blog_posts_for_label(
    label_id: int,
    space_ids: Optional[List[int]] = None,
    body_format: Optional[str] = None,
    sort: Optional[str] = None,
    cursor: Optional[str] = None,
    max_results: Optional[int] = None,
) -> Any:
    return client.request(
        "GET",
        f"/api/v2/labels/{label_id}/blogposts",
        params={
            "space-id": space_ids,
            "body-format": body_format,
            "sort": sort,
            "cursor": cursor,
            "max_results": max_results,
        },
    )


def get_blog_posts_in_space(
    space_id: int,
    sort: Optional[str] = None,
    content_status: Optional[List[str]] = None,
    title: Optional[str] = None,
    body_format: Optional[str] = None,
    cursor: Optional[str] = None,
    max_results: Optional[int] = None,
) -> Any:
    return client.request(
        "GET",
        f"/api/v2/spaces/{space_id}/blogposts",
        params={
            "sort": sort,
            "content_status": content_status,
            "title": title,
            "body-format": body_format,
            "cursor": cursor,
            "max_results": max_results,
        },
    )
