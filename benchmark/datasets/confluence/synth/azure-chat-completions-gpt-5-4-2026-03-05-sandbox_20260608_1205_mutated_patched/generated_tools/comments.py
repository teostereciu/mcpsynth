from typing import Any, Optional

from generated_tools.core import client


def get_attachment_comments(attachment_id: str, **params: Any) -> Any:
    return client.request("GET", f"/api/v2/attachments/{attachment_id}/footer-comments", params=params)


def get_custom_content_comments(custom_content_id: int, **params: Any) -> Any:
    return client.request("GET", f"/api/v2/custom-content/{custom_content_id}/footer-comments", params=params)


def get_page_footer_comments(page_id: int, **params: Any) -> Any:
    return client.request("GET", f"/api/v2/pages/{page_id}/footer-comments", params=params)


def get_page_inline_comments(page_id: int, **params: Any) -> Any:
    return client.request("GET", f"/api/v2/pages/{page_id}/inline-comments", params=params)


def get_blog_post_footer_comments(blog_post_id: int, **params: Any) -> Any:
    return client.request("GET", f"/api/v2/blogposts/{blog_post_id}/footer-comments", params=params)


def get_blog_post_inline_comments(blog_post_id: int, **params: Any) -> Any:
    return client.request("GET", f"/api/v2/blogposts/{blog_post_id}/inline-comments", params=params)


def get_footer_comments(body_format: Optional[str] = None, sort: Optional[str] = None, cursor: Optional[str] = None, max_results: Optional[int] = None) -> Any:
    return client.request("GET", "/api/v2/footer-comments", params={"body-format": body_format, "sort": sort, "cursor": cursor, "limit": max_results})


def create_footer_comment(
    body_value: str,
    page_id: Optional[str] = None,
    blog_post_id: Optional[str] = None,
    parent_comment_id: Optional[str] = None,
    attachment_id: Optional[str] = None,
    custom_content_id: Optional[str] = None,
    representation: str = "storage",
) -> Any:
    return client.request(
        "POST",
        "/api/v2/footer-comments",
        json={
            "pageId": page_id,
            "blogPostId": blog_post_id,
            "parentCommentId": parent_comment_id,
            "attachmentId": attachment_id,
            "customContentId": custom_content_id,
            "body": {"representation": representation, "value": body_value},
        },
    )


def get_footer_comment(comment_id: int, **params: Any) -> Any:
    return client.request("GET", f"/api/v2/footer-comments/{comment_id}", params=params)


def update_footer_comment(comment_id: int, version_number: int, body_value: str, representation: str = "storage") -> Any:
    return client.request(
        "PUT",
        f"/api/v2/footer-comments/{comment_id}",
        json={"version": {"number": version_number}, "body": {"representation": representation, "value": body_value}},
    )


def delete_footer_comment(comment_id: int) -> Any:
    return client.request("DELETE", f"/api/v2/footer-comments/{comment_id}")


def get_footer_comment_children(comment_id: int, **params: Any) -> Any:
    return client.request("GET", f"/api/v2/footer-comments/{comment_id}/children", params=params)


def get_inline_comments(body_format: Optional[str] = None, sort: Optional[str] = None, cursor: Optional[str] = None, max_results: Optional[int] = None) -> Any:
    return client.request("GET", "/api/v2/inline-comments", params={"body-format": body_format, "sort": sort, "cursor": cursor, "limit": max_results})


def create_inline_comment(
    body_value: str,
    page_id: Optional[str] = None,
    blog_post_id: Optional[str] = None,
    parent_comment_id: Optional[str] = None,
    representation: str = "storage",
) -> Any:
    return client.request(
        "POST",
        "/api/v2/inline-comments",
        json={
            "pageId": page_id,
            "blogPostId": blog_post_id,
            "parentCommentId": parent_comment_id,
            "body": {"representation": representation, "value": body_value},
        },
    )


def get_inline_comment(comment_id: int, **params: Any) -> Any:
    return client.request("GET", f"/api/v2/inline-comments/{comment_id}", params=params)


def update_inline_comment(comment_id: int, version_number: int, body_value: str, representation: str = "storage") -> Any:
    return client.request(
        "PUT",
        f"/api/v2/inline-comments/{comment_id}",
        json={"version": {"number": version_number}, "body": {"representation": representation, "value": body_value}},
    )


def delete_inline_comment(comment_id: int) -> Any:
    return client.request("DELETE", f"/api/v2/inline-comments/{comment_id}")


def get_inline_comment_children(comment_id: int, **params: Any) -> Any:
    return client.request("GET", f"/api/v2/inline-comments/{comment_id}/children", params=params)
