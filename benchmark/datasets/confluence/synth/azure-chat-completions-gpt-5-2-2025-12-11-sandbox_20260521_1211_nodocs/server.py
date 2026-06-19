from mcp.server.fastmcp import FastMCP

from generated_tools.attachments import (
    v1_download_attachment,
    v1_list_attachments,
    v1_upload_attachment,
)
from generated_tools.blogposts import (
    v1_create_blog_post,
    v1_delete_blog_post,
    v1_get_blog_post,
    v1_update_blog_post,
)
from generated_tools.comments import v1_create_page_comment, v1_list_page_comments
from generated_tools.content_properties import v1_get_content_property, v1_set_content_property
from generated_tools.labels import v1_add_content_labels, v1_get_content_labels, v1_remove_content_label
from generated_tools.pages import (
    v1_get_page_ancestors,
    v1_move_page,
    v2_create_page,
    v2_delete_page,
    v2_get_page,
    v2_get_page_children,
    v2_update_page,
)
from generated_tools.search import v1_cql_search
from generated_tools.spaces import v1_create_space, v1_delete_space, v1_get_space_by_key, v2_get_space, v2_list_spaces
from generated_tools.users import v1_get_current_user, v1_get_user
from generated_tools.versions import v1_get_page_version, v1_list_page_versions, v1_restore_page_version

mcp = FastMCP("confluence-cloud")


@mcp.tool()
def get_page(page_id: str, body_format: str = "storage"):
    return v2_get_page(page_id, body_format=body_format)


@mcp.tool()
def create_page(space_id: str, title: str, parent_id: str | None = None, body: str = "", body_format: str = "storage"):
    return v2_create_page(space_id=space_id, title=title, parent_id=parent_id, body=body, body_format=body_format)


@mcp.tool()
def update_page(page_id: str, title: str | None = None, body: str | None = None, body_format: str = "storage", version_number: int | None = None):
    return v2_update_page(page_id, title=title, body=body, body_format=body_format, version_number=version_number)


@mcp.tool()
def delete_page(page_id: str, purge: bool = False):
    return v2_delete_page(page_id, purge=purge)


@mcp.tool()
def get_page_children(page_id: str, limit: int = 25, cursor: str | None = None):
    return v2_get_page_children(page_id, limit=limit, cursor=cursor)


@mcp.tool()
def get_page_ancestors(page_id: str):
    return v1_get_page_ancestors(page_id)


@mcp.tool()
def move_page(page_id: str, target_parent_id: str, position: str = "append"):
    return v1_move_page(page_id, target_parent_id=target_parent_id, position=position)


@mcp.tool()
def list_spaces(limit: int = 25, cursor: str | None = None):
    return v2_list_spaces(limit=limit, cursor=cursor)


@mcp.tool()
def get_space(space_id: str):
    return v2_get_space(space_id)


@mcp.tool()
def get_space_by_key(space_key: str):
    return v1_get_space_by_key(space_key)


@mcp.tool()
def create_space(key: str, name: str, description_plain: str = ""):
    return v1_create_space(key=key, name=name, description_plain=description_plain)


@mcp.tool()
def delete_space(space_key: str):
    return v1_delete_space(space_key)


@mcp.tool()
def cql_search(cql: str, limit: int = 25, start: int = 0, expand: str | None = None):
    return v1_cql_search(cql=cql, limit=limit, start=start, expand=expand)


@mcp.tool()
def get_content_labels(content_id: str, prefix: str = "global", limit: int = 200, start: int = 0):
    return v1_get_content_labels(content_id, prefix=prefix, limit=limit, start=start)


@mcp.tool()
def add_content_labels(content_id: str, labels: list[str], prefix: str = "global"):
    return v1_add_content_labels(content_id, labels=labels, prefix=prefix)


@mcp.tool()
def remove_content_label(content_id: str, name: str, prefix: str = "global"):
    return v1_remove_content_label(content_id, name=name, prefix=prefix)


@mcp.tool()
def list_attachments(content_id: str, limit: int = 25, start: int = 0, expand: str = ""):
    return v1_list_attachments(content_id, limit=limit, start=start, expand=expand)


@mcp.tool()
def upload_attachment(content_id: str, filename: str, file_bytes_b64: str, comment: str = "", minor_edit: bool = True):
    return v1_upload_attachment(content_id, filename=filename, file_bytes_b64=file_bytes_b64, comment=comment, minor_edit=minor_edit)


@mcp.tool()
def download_attachment(download_url: str):
    return v1_download_attachment(download_url)


@mcp.tool()
def list_page_comments(page_id: str, limit: int = 25, start: int = 0, expand: str = ""):
    return v1_list_page_comments(page_id, limit=limit, start=start, expand=expand)


@mcp.tool()
def create_page_comment(page_id: str, body: str, body_format: str = "storage", parent_comment_id: str | None = None):
    return v1_create_page_comment(page_id, body=body, body_format=body_format, parent_comment_id=parent_comment_id)


@mcp.tool()
def list_page_versions(page_id: str, limit: int = 25, start: int = 0):
    return v1_list_page_versions(page_id, limit=limit, start=start)


@mcp.tool()
def get_page_version(page_id: str, version_number: int):
    return v1_get_page_version(page_id, version_number)


@mcp.tool()
def restore_page_version(page_id: str, version_number: int):
    return v1_restore_page_version(page_id, version_number)


@mcp.tool()
def get_content_property(content_id: str, key: str):
    return v1_get_content_property(content_id, key)


@mcp.tool()
def set_content_property(content_id: str, key: str, value, version_number: int | None = None):
    return v1_set_content_property(content_id, key, value=value, version_number=version_number)


@mcp.tool()
def create_blog_post(space_key: str, title: str, body: str, body_format: str = "storage"):
    return v1_create_blog_post(space_key=space_key, title=title, body=body, body_format=body_format)


@mcp.tool()
def get_blog_post(content_id: str, expand: str = "body.storage,version"):
    return v1_get_blog_post(content_id, expand=expand)


@mcp.tool()
def update_blog_post(content_id: str, version_number: int, title: str | None = None, body: str | None = None, body_format: str = "storage"):
    return v1_update_blog_post(content_id, version_number=version_number, title=title, body=body, body_format=body_format)


@mcp.tool()
def delete_blog_post(content_id: str):
    return v1_delete_blog_post(content_id)


@mcp.tool()
def get_current_user():
    return v1_get_current_user()


@mcp.tool()
def get_user(account_id: str):
    return v1_get_user(account_id)


if __name__ == "__main__":
    mcp.run()
