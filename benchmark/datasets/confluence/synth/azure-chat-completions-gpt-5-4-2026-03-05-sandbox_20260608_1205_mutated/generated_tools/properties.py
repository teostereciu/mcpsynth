from typing import Any

from generated_tools.core import client


def _list(path: str, **params: Any) -> Any:
    return client.request("GET", path, params=params)


def _create(path: str, key: str, value: Any) -> Any:
    return client.request("POST", path, json={"key": key, "value": value})


def _get(path: str) -> Any:
    return client.request("GET", path)


def _update(path: str, key: str, value: Any, version_number: int, version_message: str | None = None) -> Any:
    return client.request("PUT", path, json={"key": key, "value": value, "version": {"number": version_number, "message": version_message}})


def _delete(path: str) -> Any:
    return client.request("DELETE", path)


def get_page_properties(page_id: int, **params: Any) -> Any:
    return _list(f"/api/v2/pages/{page_id}/properties", **params)


def create_page_property(page_id: int, key: str, value: Any) -> Any:
    return _create(f"/api/v2/pages/{page_id}/properties", key, value)


def get_page_property(page_id: int, property_id: int) -> Any:
    return _get(f"/api/v2/pages/{page_id}/properties/{property_id}")


def update_page_property(page_id: int, property_id: int, key: str, value: Any, version_number: int, version_message: str | None = None) -> Any:
    return _update(f"/api/v2/pages/{page_id}/properties/{property_id}", key, value, version_number, version_message)


def delete_page_property(page_id: int, property_id: int) -> Any:
    return _delete(f"/api/v2/pages/{page_id}/properties/{property_id}")


def get_blog_post_properties(blog_post_id: int, **params: Any) -> Any:
    return _list(f"/api/v2/blogposts/{blog_post_id}/properties", **params)


def create_blog_post_property(blog_post_id: int, key: str, value: Any) -> Any:
    return _create(f"/api/v2/blogposts/{blog_post_id}/properties", key, value)


def get_blog_post_property(blog_post_id: int, property_id: int) -> Any:
    return _get(f"/api/v2/blogposts/{blog_post_id}/properties/{property_id}")


def update_blog_post_property(blog_post_id: int, property_id: int, key: str, value: Any, version_number: int, version_message: str | None = None) -> Any:
    return _update(f"/api/v2/blogposts/{blog_post_id}/properties/{property_id}", key, value, version_number, version_message)


def delete_blog_post_property(blog_post_id: int, property_id: int) -> Any:
    return _delete(f"/api/v2/blogposts/{blog_post_id}/properties/{property_id}")


def get_attachment_properties(attachment_id: str, **params: Any) -> Any:
    return _list(f"/api/v2/attachments/{attachment_id}/properties", **params)


def create_attachment_property(attachment_id: str, key: str, value: Any) -> Any:
    return _create(f"/api/v2/attachments/{attachment_id}/properties", key, value)


def get_attachment_property(attachment_id: str, property_id: int) -> Any:
    return _get(f"/api/v2/attachments/{attachment_id}/properties/{property_id}")


def update_attachment_property(attachment_id: str, property_id: int, key: str, value: Any, version_number: int, version_message: str | None = None) -> Any:
    return _update(f"/api/v2/attachments/{attachment_id}/properties/{property_id}", key, value, version_number, version_message)


def delete_attachment_property(attachment_id: str, property_id: int) -> Any:
    return _delete(f"/api/v2/attachments/{attachment_id}/properties/{property_id}")


def get_comment_properties(comment_id: int, **params: Any) -> Any:
    return _list(f"/api/v2/comments/{comment_id}/properties", **params)


def create_comment_property(comment_id: int, key: str, value: Any) -> Any:
    return _create(f"/api/v2/comments/{comment_id}/properties", key, value)


def get_comment_property(comment_id: int, property_id: int) -> Any:
    return _get(f"/api/v2/comments/{comment_id}/properties/{property_id}")


def update_comment_property(comment_id: int, property_id: int, key: str, value: Any, version_number: int, version_message: str | None = None) -> Any:
    return _update(f"/api/v2/comments/{comment_id}/properties/{property_id}", key, value, version_number, version_message)


def delete_comment_property(comment_id: int, property_id: int) -> Any:
    return _delete(f"/api/v2/comments/{comment_id}/properties/{property_id}")
