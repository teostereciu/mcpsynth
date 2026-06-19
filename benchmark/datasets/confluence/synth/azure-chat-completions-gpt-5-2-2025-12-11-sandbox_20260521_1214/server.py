from __future__ import annotations

from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.attachments import (
    delete_attachment,
    get_attachment,
    list_attachments,
    list_page_attachments,
)
from generated_tools.blog_posts import (
    create_blog_post,
    delete_blog_post,
    get_blog_post,
    list_blog_posts,
    update_blog_post,
)
from generated_tools.comments import (
    create_footer_comment,
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
from generated_tools.labels import (
    add_labels_to_content,
    remove_label_from_content,
    remove_label_from_content_by_query,
)
from generated_tools.pages import create_page, delete_page, get_page, list_pages, update_page
from generated_tools.search import cql_search
from generated_tools.spaces import create_space, get_space, list_spaces
from generated_tools.users import get_current_user, get_user_by_account_id
from generated_tools.versions import get_page_version_details, list_page_versions, restore_content_version

mcp = FastMCP("confluence-cloud")


@mcp.tool()
def pages_list(
    space_id: Optional[int] = None,
    title: Optional[str] = None,
    status: Optional[list[str]] = None,
    limit: int = 25,
    cursor: Optional[str] = None,
    body_format: Optional[str] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    return list_pages(
        space_id=space_id,
        title=title,
        status=status,
        limit=limit,
        cursor=cursor,
        body_format=body_format,
        sort=sort,
    )


@mcp.tool()
def pages_get(
    page_id: int,
    body_format: Optional[str] = None,
    get_draft: Optional[bool] = None,
    include_labels: Optional[bool] = None,
    include_properties: Optional[bool] = None,
    include_operations: Optional[bool] = None,
    include_likes: Optional[bool] = None,
    include_versions: Optional[bool] = None,
    version: Optional[int] = None,
) -> Dict[str, Any]:
    return get_page(
        page_id=page_id,
        body_format=body_format,
        get_draft=get_draft,
        include_labels=include_labels,
        include_properties=include_properties,
        include_operations=include_operations,
        include_likes=include_likes,
        include_versions=include_versions,
        version=version,
    )


@mcp.tool()
def pages_create(
    space_id: int,
    title: str,
    body_value: str,
    body_representation: str = "storage",
    parent_id: Optional[int] = None,
    status: str = "current",
    subtype: Optional[str] = None,
    embedded: Optional[bool] = None,
    private: Optional[bool] = None,
    root_level: Optional[bool] = None,
) -> Dict[str, Any]:
    return create_page(
        space_id=space_id,
        title=title,
        body_value=body_value,
        body_representation=body_representation,
        parent_id=parent_id,
        status=status,
        subtype=subtype,
        embedded=embedded,
        private=private,
        root_level=root_level,
    )


@mcp.tool()
def pages_update(
    page_id: int,
    title: str,
    body_value: str,
    version_number: int,
    status: str = "current",
    body_representation: str = "storage",
    version_message: Optional[str] = None,
) -> Dict[str, Any]:
    return update_page(
        page_id=page_id,
        title=title,
        body_value=body_value,
        version_number=version_number,
        status=status,
        body_representation=body_representation,
        version_message=version_message,
    )


@mcp.tool()
def pages_delete(page_id: int, purge: Optional[bool] = None, draft: Optional[bool] = None) -> Dict[str, Any]:
    return delete_page(page_id=page_id, purge=purge, draft=draft)


@mcp.tool()
def spaces_list(
    keys: Optional[list[str]] = None,
    ids: Optional[list[int]] = None,
    type: Optional[str] = None,
    status: Optional[str] = None,
    limit: int = 25,
    cursor: Optional[str] = None,
    sort: Optional[str] = None,
    include_icon: Optional[bool] = None,
    description_format: Optional[str] = None,
) -> Dict[str, Any]:
    return list_spaces(
        keys=keys,
        ids=ids,
        type=type,
        status=status,
        limit=limit,
        cursor=cursor,
        sort=sort,
        include_icon=include_icon,
        description_format=description_format,
    )


@mcp.tool()
def spaces_get(
    space_id: int,
    description_format: Optional[str] = None,
    include_icon: Optional[bool] = None,
    include_operations: Optional[bool] = None,
    include_properties: Optional[bool] = None,
    include_permissions: Optional[bool] = None,
    include_role_assignments: Optional[bool] = None,
    include_labels: Optional[bool] = None,
) -> Dict[str, Any]:
    return get_space(
        space_id=space_id,
        description_format=description_format,
        include_icon=include_icon,
        include_operations=include_operations,
        include_properties=include_properties,
        include_permissions=include_permissions,
        include_role_assignments=include_role_assignments,
        include_labels=include_labels,
    )


@mcp.tool()
def spaces_create(
    name: str,
    key: Optional[str] = None,
    alias: Optional[str] = None,
    description_value: Optional[str] = None,
    description_representation: Optional[str] = None,
    create_private_space: Optional[bool] = None,
    template_key: Optional[str] = None,
) -> Dict[str, Any]:
    return create_space(
        name=name,
        key=key,
        alias=alias,
        description_value=description_value,
        description_representation=description_representation,
        create_private_space=create_private_space,
        template_key=template_key,
    )


@mcp.tool()
def search_cql(
    cql: str,
    limit: int = 25,
    cursor: Optional[str] = None,
    start: Optional[int] = None,
    expand: Optional[list[str]] = None,
    excerpt: Optional[str] = None,
    include_archived_spaces: Optional[bool] = None,
    exclude_current_spaces: Optional[bool] = None,
) -> Dict[str, Any]:
    return cql_search(
        cql=cql,
        limit=limit,
        cursor=cursor,
        start=start,
        expand=expand,
        excerpt=excerpt,
        include_archived_spaces=include_archived_spaces,
        exclude_current_spaces=exclude_current_spaces,
    )


@mcp.tool()
def labels_add_to_content(content_id: str, labels: list[dict[str, str]]) -> Dict[str, Any]:
    return add_labels_to_content(content_id=content_id, labels=labels)


@mcp.tool()
def labels_remove_from_content(content_id: str, label: str) -> Dict[str, Any]:
    return remove_label_from_content(content_id=content_id, label=label)


@mcp.tool()
def labels_remove_from_content_by_query(content_id: str, name: str) -> Dict[str, Any]:
    return remove_label_from_content_by_query(content_id=content_id, name=name)


@mcp.tool()
def attachments_list(
    limit: int = 25,
    cursor: Optional[str] = None,
    filename: Optional[str] = None,
    media_type: Optional[str] = None,
    status: Optional[list[str]] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    return list_attachments(
        limit=limit,
        cursor=cursor,
        filename=filename,
        media_type=media_type,
        status=status,
        sort=sort,
    )


@mcp.tool()
def attachments_list_for_page(
    page_id: int,
    limit: int = 25,
    cursor: Optional[str] = None,
    filename: Optional[str] = None,
    media_type: Optional[str] = None,
    status: Optional[list[str]] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    return list_page_attachments(
        page_id=page_id,
        limit=limit,
        cursor=cursor,
        filename=filename,
        media_type=media_type,
        status=status,
        sort=sort,
    )


@mcp.tool()
def attachments_get(
    attachment_id: str,
    version: Optional[int] = None,
    include_labels: Optional[bool] = None,
    include_properties: Optional[bool] = None,
    include_operations: Optional[bool] = None,
    include_versions: Optional[bool] = None,
) -> Dict[str, Any]:
    return get_attachment(
        attachment_id=attachment_id,
        version=version,
        include_labels=include_labels,
        include_properties=include_properties,
        include_operations=include_operations,
        include_versions=include_versions,
    )


@mcp.tool()
def attachments_delete(attachment_id: int, purge: Optional[bool] = None) -> Dict[str, Any]:
    return delete_attachment(attachment_id=attachment_id, purge=purge)


@mcp.tool()
def comments_list_page_footer(
    page_id: int,
    limit: int = 25,
    cursor: Optional[str] = None,
    body_format: Optional[str] = None,
    status: Optional[list[str]] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    return list_page_footer_comments(
        page_id=page_id,
        limit=limit,
        cursor=cursor,
        body_format=body_format,
        status=status,
        sort=sort,
    )


@mcp.tool()
def comments_list_page_inline(
    page_id: int,
    limit: int = 25,
    cursor: Optional[str] = None,
    body_format: Optional[str] = None,
    status: Optional[list[str]] = None,
    resolution_status: Optional[list[str]] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    return list_page_inline_comments(
        page_id=page_id,
        limit=limit,
        cursor=cursor,
        body_format=body_format,
        status=status,
        resolution_status=resolution_status,
        sort=sort,
    )


@mcp.tool()
def comments_create_footer(
    body_value: str,
    body_representation: str = "storage",
    page_id: Optional[int] = None,
    blog_post_id: Optional[int] = None,
    parent_comment_id: Optional[str] = None,
    attachment_id: Optional[str] = None,
    custom_content_id: Optional[str] = None,
) -> Dict[str, Any]:
    return create_footer_comment(
        body_value=body_value,
        body_representation=body_representation,
        page_id=page_id,
        blog_post_id=blog_post_id,
        parent_comment_id=parent_comment_id,
        attachment_id=attachment_id,
        custom_content_id=custom_content_id,
    )


@mcp.tool()
def versions_list_page(
    page_id: int,
    limit: int = 25,
    cursor: Optional[str] = None,
    sort: Optional[str] = None,
    body_format: Optional[str] = None,
) -> Dict[str, Any]:
    return list_page_versions(page_id=page_id, limit=limit, cursor=cursor, sort=sort, body_format=body_format)


@mcp.tool()
def versions_get_page_details(page_id: int, version_number: int) -> Dict[str, Any]:
    return get_page_version_details(page_id=page_id, version_number=version_number)


@mcp.tool()
def versions_restore_content(
    content_id: str,
    version_number: int,
    message: Optional[str] = None,
    restore_title: bool = True,
    expand: Optional[list[str]] = None,
) -> Dict[str, Any]:
    return restore_content_version(
        content_id=content_id,
        version_number=version_number,
        message=message,
        restore_title=restore_title,
        expand=expand,
    )


@mcp.tool()
def properties_list_page(
    page_id: int,
    key: Optional[str] = None,
    limit: int = 25,
    cursor: Optional[str] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    return list_page_properties(page_id=page_id, key=key, limit=limit, cursor=cursor, sort=sort)


@mcp.tool()
def properties_create_page(page_id: int, key: str, value: Any) -> Dict[str, Any]:
    return create_page_property(page_id=page_id, key=key, value=value)


@mcp.tool()
def properties_get_page(page_id: int, property_id: int) -> Dict[str, Any]:
    return get_page_property(page_id=page_id, property_id=property_id)


@mcp.tool()
def properties_update_page(
    page_id: int,
    property_id: int,
    key: str,
    value: Any,
    version_number: int,
    version_message: Optional[str] = None,
) -> Dict[str, Any]:
    return update_page_property(
        page_id=page_id,
        property_id=property_id,
        key=key,
        value=value,
        version_number=version_number,
        version_message=version_message,
    )


@mcp.tool()
def properties_delete_page(page_id: int, property_id: int) -> Dict[str, Any]:
    return delete_page_property(page_id=page_id, property_id=property_id)


@mcp.tool()
def blogposts_list(
    space_id: Optional[int] = None,
    title: Optional[str] = None,
    status: Optional[list[str]] = None,
    limit: int = 25,
    cursor: Optional[str] = None,
    body_format: Optional[str] = None,
    sort: Optional[str] = None,
) -> Dict[str, Any]:
    return list_blog_posts(
        space_id=space_id,
        title=title,
        status=status,
        limit=limit,
        cursor=cursor,
        body_format=body_format,
        sort=sort,
    )


@mcp.tool()
def blogposts_get(
    blog_post_id: int,
    body_format: Optional[str] = None,
    get_draft: Optional[bool] = None,
    include_labels: Optional[bool] = None,
    include_properties: Optional[bool] = None,
    include_operations: Optional[bool] = None,
    include_likes: Optional[bool] = None,
    include_versions: Optional[bool] = None,
    version: Optional[int] = None,
) -> Dict[str, Any]:
    return get_blog_post(
        blog_post_id=blog_post_id,
        body_format=body_format,
        get_draft=get_draft,
        include_labels=include_labels,
        include_properties=include_properties,
        include_operations=include_operations,
        include_likes=include_likes,
        include_versions=include_versions,
        version=version,
    )


@mcp.tool()
def blogposts_create(
    space_id: int,
    title: str,
    body_value: str,
    body_representation: str = "storage",
    status: str = "current",
    created_at: Optional[str] = None,
    private: Optional[bool] = None,
) -> Dict[str, Any]:
    return create_blog_post(
        space_id=space_id,
        title=title,
        body_value=body_value,
        body_representation=body_representation,
        status=status,
        created_at=created_at,
        private=private,
    )


@mcp.tool()
def blogposts_update(
    blog_post_id: int,
    title: str,
    body_value: str,
    version_number: int,
    space_id: Optional[int] = None,
    status: str = "current",
    body_representation: str = "storage",
    version_message: Optional[str] = None,
    created_at: Optional[str] = None,
) -> Dict[str, Any]:
    return update_blog_post(
        blog_post_id=blog_post_id,
        title=title,
        body_value=body_value,
        version_number=version_number,
        space_id=space_id,
        status=status,
        body_representation=body_representation,
        version_message=version_message,
        created_at=created_at,
    )


@mcp.tool()
def blogposts_delete(blog_post_id: int, purge: Optional[bool] = None, draft: Optional[bool] = None) -> Dict[str, Any]:
    return delete_blog_post(blog_post_id=blog_post_id, purge=purge, draft=draft)


@mcp.tool()
def users_get_current(expand: Optional[list[str]] = None) -> Dict[str, Any]:
    return get_current_user(expand=expand)


@mcp.tool()
def users_get_by_account_id(account_id: str, expand: Optional[list[str]] = None) -> Dict[str, Any]:
    return get_user_by_account_id(account_id=account_id, expand=expand)


if __name__ == "__main__":
    mcp.run()
