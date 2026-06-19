from mcp.server.fastmcp import FastMCP

from generated_tools.attachments import delete_attachment, get_attachment, list_attachments, list_page_attachments
from generated_tools.blog_posts import (
    create_blog_post,
    delete_blog_post,
    get_blog_post,
    list_blog_posts,
    update_blog_post,
)
from generated_tools.comments import (
    create_footer_comment,
    create_inline_comment,
    list_page_footer_comments,
    list_page_inline_comments,
)
from generated_tools.content_properties import (
    create_page_property,
    delete_page_property,
    get_page_property,
    list_page_properties,
    update_page_property,
)
from generated_tools.labels import add_labels_to_content, remove_label_from_content, remove_label_from_content_by_query
from generated_tools.pages import (
    create_page,
    delete_page,
    get_page,
    list_pages,
    update_page,
    update_page_title,
)
from generated_tools.search import cql_search, cql_user_search
from generated_tools.spaces import create_space, get_space, list_spaces
from generated_tools.users import get_current_user, get_user_by_account_id
from generated_tools.versions import get_page_version_details, list_page_versions

mcp = FastMCP("confluence-cloud")


@mcp.tool()
def pages_list(
    space_id: int | None = None,
    title: str | None = None,
    content_status: list[str] | None = None,
    cursor: str | None = None,
    max_results: int = 25,
    body_format: str | None = None,
    sort: str | None = None,
    ids: list[int] | None = None,
):
    return list_pages(
        space_id=space_id,
        title=title,
        content_status=content_status,
        cursor=cursor,
        max_results=max_results,
        body_format=body_format,
        sort=sort,
        ids=ids,
    )


@mcp.tool()
def pages_get(page_id: int, body_format: str | None = None):
    return get_page(page_id=page_id, body_format=body_format)


@mcp.tool()
def pages_create(
    space_id: str,
    title: str,
    body_value: str,
    parent_id: str | None = None,
    body_representation: str = "storage",
    content_status: str = "current",
):
    return create_page(
        space_id=space_id,
        title=title,
        body_representation=body_representation,
        body_value=body_value,
        parent_id=parent_id,
        content_status=content_status,
    )


@mcp.tool()
def pages_update(
    page_id: int,
    title: str,
    body_value: str,
    version_number: int,
    version_message: str | None = None,
    body_representation: str = "storage",
    content_status: str = "current",
):
    return update_page(
        page_id=page_id,
        title=title,
        body_representation=body_representation,
        body_value=body_value,
        version_number=version_number,
        version_message=version_message,
        content_status=content_status,
    )


@mcp.tool()
def pages_delete(page_id: int, purge: bool | None = None, draft: bool | None = None):
    return delete_page(page_id=page_id, purge=purge, draft=draft)


@mcp.tool()
def pages_update_title(page_id: int, title: str, content_status: str = "current"):
    return update_page_title(page_id=page_id, title=title, content_status=content_status)


@mcp.tool()
def spaces_list(keys: list[str] | None = None, ids: list[int] | None = None, max_results: int = 25, cursor: str | None = None):
    return list_spaces(keys=keys, ids=ids, max_results=max_results, cursor=cursor)


@mcp.tool()
def spaces_get(space_id: int):
    return get_space(space_id=space_id)


@mcp.tool()
def spaces_create(name: str, key: str | None = None, description_value: str | None = None):
    return create_space(name=name, key=key, description_value=description_value)


@mcp.tool()
def search_cql(query: str, max_results: int = 25, cursor: str | None = None):
    return cql_search(query=query, max_results=max_results, cursor=cursor)


@mcp.tool()
def search_users_cql(query: str, max_results: int = 25, start: int | None = None):
    return cql_user_search(query=query, max_results=max_results, start=start)


@mcp.tool()
def labels_add(content_id: str, labels: list[dict]):
    return add_labels_to_content(content_id=content_id, labels=labels)


@mcp.tool()
def labels_remove(content_id: str, label: str):
    return remove_label_from_content(content_id=content_id, label=label)


@mcp.tool()
def labels_remove_by_query(content_id: str, name: str):
    return remove_label_from_content_by_query(content_id=content_id, name=name)


@mcp.tool()
def attachments_list(max_results: int = 25, cursor: str | None = None, filename: str | None = None):
    return list_attachments(max_results=max_results, cursor=cursor, filename=filename)


@mcp.tool()
def attachments_get(attachment_id: str):
    return get_attachment(attachment_id=attachment_id)


@mcp.tool()
def attachments_list_for_page(page_id: int, max_results: int = 25, cursor: str | None = None):
    return list_page_attachments(page_id=page_id, max_results=max_results, cursor=cursor)


@mcp.tool()
def attachments_delete(attachment_id: int, purge: bool | None = None):
    return delete_attachment(attachment_id=attachment_id, purge=purge)


@mcp.tool()
def comments_list_page_footer(page_id: int, max_results: int = 25, cursor: str | None = None):
    return list_page_footer_comments(page_id=page_id, max_results=max_results, cursor=cursor)


@mcp.tool()
def comments_list_page_inline(page_id: int, max_results: int = 25, cursor: str | None = None):
    return list_page_inline_comments(page_id=page_id, max_results=max_results, cursor=cursor)


@mcp.tool()
def comments_create_footer(page_id: str, body_value: str, body_representation: str = "storage"):
    return create_footer_comment(body_representation=body_representation, body_value=body_value, page_id=page_id)


@mcp.tool()
def comments_create_inline(page_id: str, body_value: str, inline_marker_ref: str, body_representation: str = "storage"):
    return create_inline_comment(
        body_representation=body_representation,
        body_value=body_value,
        page_id=page_id,
        inline_marker_ref=inline_marker_ref,
    )


@mcp.tool()
def versions_list_page(page_id: int, max_results: int = 25, cursor: str | None = None):
    return list_page_versions(page_id=page_id, max_results=max_results, cursor=cursor)


@mcp.tool()
def versions_get_page_details(page_id: int, version_number: int):
    return get_page_version_details(page_id=page_id, version_number=version_number)


@mcp.tool()
def properties_list_page(page_id: int, max_results: int = 25, cursor: str | None = None, key: str | None = None):
    return list_page_properties(page_id=page_id, max_results=max_results, cursor=cursor, key=key)


@mcp.tool()
def properties_get_page(page_id: int, property_id: int):
    return get_page_property(page_id=page_id, property_id=property_id)


@mcp.tool()
def properties_create_page(page_id: int, key: str, value: dict):
    return create_page_property(page_id=page_id, key=key, value=value)


@mcp.tool()
def properties_update_page(page_id: int, property_id: int, key: str, value: dict, version_number: int, version_message: str | None = None):
    return update_page_property(
        page_id=page_id,
        property_id=property_id,
        key=key,
        value=value,
        version_number=version_number,
        version_message=version_message,
    )


@mcp.tool()
def properties_delete_page(page_id: int, property_id: int):
    return delete_page_property(page_id=page_id, property_id=property_id)


@mcp.tool()
def blogposts_list(space_id: int | None = None, max_results: int = 25, cursor: str | None = None, title: str | None = None):
    return list_blog_posts(space_id=space_id, max_results=max_results, cursor=cursor, title=title)


@mcp.tool()
def blogposts_get(blog_post_id: int):
    return get_blog_post(blog_post_id=blog_post_id)


@mcp.tool()
def blogposts_create(space_id: str, title: str, body_value: str, content_status: str = "current"):
    return create_blog_post(space_id=space_id, title=title, body_value=body_value, content_status=content_status)


@mcp.tool()
def blogposts_update(blog_post_id: int, space_id: str, title: str, body_value: str, version_number: int, version_message: str | None = None):
    return update_blog_post(
        blog_post_id=blog_post_id,
        space_id=space_id,
        title=title,
        body_value=body_value,
        version_number=version_number,
        version_message=version_message,
    )


@mcp.tool()
def blogposts_delete(blog_post_id: int, purge: bool | None = None, draft: bool | None = None):
    return delete_blog_post(blog_post_id=blog_post_id, purge=purge, draft=draft)


@mcp.tool()
def users_get_current():
    return get_current_user()


@mcp.tool()
def users_get_by_account_id(account_id: str):
    return get_user_by_account_id(account_id=account_id)


if __name__ == "__main__":
    mcp.run()
