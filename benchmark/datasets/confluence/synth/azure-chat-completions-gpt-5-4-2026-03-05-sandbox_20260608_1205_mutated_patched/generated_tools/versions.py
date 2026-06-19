from typing import Any

from generated_tools.core import client


def get_attachment_versions(attachment_id: str, **params: Any) -> Any:
    return client.request("GET", f"/api/v2/attachments/{attachment_id}/versions", params=params)


def get_attachment_version_details(attachment_id: str, version_number: int) -> Any:
    return client.request("GET", f"/api/v2/attachments/{attachment_id}/versions/{version_number}")


def get_blog_post_versions(blog_post_id: int, **params: Any) -> Any:
    return client.request("GET", f"/api/v2/blogposts/{blog_post_id}/versions", params=params)


def get_blog_post_version_details(blog_post_id: int, version_number: int) -> Any:
    return client.request("GET", f"/api/v2/blogposts/{blog_post_id}/versions/{version_number}")


def get_page_versions(page_id: int, **params: Any) -> Any:
    return client.request("GET", f"/api/v2/pages/{page_id}/versions", params=params)


def get_page_version_details(page_id: int, version_number: int) -> Any:
    return client.request("GET", f"/api/v2/pages/{page_id}/versions/{version_number}")


def get_custom_content_versions(custom_content_id: int, **params: Any) -> Any:
    return client.request("GET", f"/api/v2/custom-content/{custom_content_id}/versions", params=params)


def get_custom_content_version_details(custom_content_id: int, version_number: int) -> Any:
    return client.request("GET", f"/api/v2/custom-content/{custom_content_id}/versions/{version_number}")


def get_footer_comment_versions(comment_id: int, **params: Any) -> Any:
    return client.request("GET", f"/api/v2/footer-comments/{comment_id}/versions", params=params)


def get_footer_comment_version_details(comment_id: int, version_number: int) -> Any:
    return client.request("GET", f"/api/v2/footer-comments/{comment_id}/versions/{version_number}")


def get_inline_comment_versions(comment_id: int, **params: Any) -> Any:
    return client.request("GET", f"/api/v2/inline-comments/{comment_id}/versions", params=params)


def get_inline_comment_version_details(comment_id: int, version_number: int) -> Any:
    return client.request("GET", f"/api/v2/inline-comments/{comment_id}/versions/{version_number}")
