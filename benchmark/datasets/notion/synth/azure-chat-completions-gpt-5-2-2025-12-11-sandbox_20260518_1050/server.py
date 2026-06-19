from mcp.server.fastmcp import FastMCP

from generated_tools.pages import (
    create_page,
    move_page,
    restore_page,
    retrieve_page,
    retrieve_page_property_item,
    trash_page,
    update_page,
)
from generated_tools.databases import (
    create_database,
    list_databases,
    query_database,
    retrieve_database,
    update_database,
)
from generated_tools.blocks import (
    append_block_children,
    delete_block,
    retrieve_block,
    retrieve_block_children,
    update_block,
)
from generated_tools.comments import create_comment, list_comments, retrieve_comment
from generated_tools.search import search
from generated_tools.users import list_users, retrieve_me, retrieve_user


mcp = FastMCP("notion")


# Pages
@mcp.tool()
def notion_retrieve_page(page_id: str, property_ids: list[str] | None = None):
    return retrieve_page(page_id, property_ids=property_ids)


@mcp.tool()
def notion_create_page(
    parent: dict,
    properties: dict,
    children: list[dict] | None = None,
    icon: dict | None = None,
    cover: dict | None = None,
    content_markdown: str | None = None,
    show_child_attributes: bool | None = None,
):
    return create_page(
        parent,
        properties,
        children=children,
        icon=icon,
        cover=cover,
        content_markdown=content_markdown,
        show_child_attributes=show_child_attributes,
    )


@mcp.tool()
def notion_update_page(
    page_id: str,
    properties: dict | None = None,
    icon: dict | None = None,
    cover: dict | None = None,
    in_trash: bool | None = None,
    archived: bool | None = None,
    locked: bool | None = None,
    erase_content: bool | None = None,
    children: list[dict] | None = None,
    content_markdown: str | None = None,
    show_child_attributes: bool | None = None,
):
    return update_page(
        page_id,
        properties=properties,
        icon=icon,
        cover=cover,
        in_trash=in_trash,
        archived=archived,
        locked=locked,
        erase_content=erase_content,
        children=children,
        content_markdown=content_markdown,
        show_child_attributes=show_child_attributes,
    )


@mcp.tool()
def notion_trash_page(page_id: str):
    return trash_page(page_id)


@mcp.tool()
def notion_restore_page(page_id: str):
    return restore_page(page_id)


@mcp.tool()
def notion_move_page(page_id: str, parent: dict, show_child_attributes: bool | None = None):
    return move_page(page_id, parent, show_child_attributes=show_child_attributes)


@mcp.tool()
def notion_retrieve_page_property_item(
    page_id: str,
    property_id: str,
    start_cursor: str | None = None,
    page_size: int | None = None,
):
    return retrieve_page_property_item(page_id, property_id, start_cursor=start_cursor, page_size=page_size)


# Databases
@mcp.tool()
def notion_retrieve_database(database_id: str):
    return retrieve_database(database_id)


@mcp.tool()
def notion_list_databases(start_cursor: str | None = None, page_size: int | None = None):
    return list_databases(start_cursor=start_cursor, page_size=page_size)


@mcp.tool()
def notion_query_database(
    database_id: str,
    filter: dict | None = None,
    sorts: list | None = None,
    start_cursor: str | None = None,
    page_size: int | None = None,
    filter_properties: list | None = None,
):
    return query_database(
        database_id,
        filter=filter,
        sorts=sorts,
        start_cursor=start_cursor,
        page_size=page_size,
        filter_properties=filter_properties,
    )


@mcp.tool()
def notion_create_database(
    parent: dict,
    title: list,
    properties: dict,
    icon: dict | None = None,
    cover: dict | None = None,
    description: list | None = None,
    is_inline: bool | None = None,
):
    return create_database(
        parent,
        title,
        properties,
        icon=icon,
        cover=cover,
        description=description,
        is_inline=is_inline,
    )


@mcp.tool()
def notion_update_database(
    database_id: str,
    title: list | None = None,
    description: list | None = None,
    properties: dict | None = None,
    icon: dict | None = None,
    cover: dict | None = None,
    archived: bool | None = None,
):
    return update_database(
        database_id,
        title=title,
        description=description,
        properties=properties,
        icon=icon,
        cover=cover,
        archived=archived,
    )


# Blocks
@mcp.tool()
def notion_retrieve_block(block_id: str):
    return retrieve_block(block_id)


@mcp.tool()
def notion_retrieve_block_children(block_id: str, start_cursor: str | None = None, page_size: int | None = None):
    return retrieve_block_children(block_id, start_cursor=start_cursor, page_size=page_size)


@mcp.tool()
def notion_append_block_children(block_id: str, children: list, after: str | None = None):
    return append_block_children(block_id, children, after=after)


@mcp.tool()
def notion_update_block(block_id: str, block: dict):
    return update_block(block_id, block)


@mcp.tool()
def notion_delete_block(block_id: str):
    return delete_block(block_id)


# Comments
@mcp.tool()
def notion_create_comment(
    parent: dict,
    rich_text: list,
    attachments: list | None = None,
    display_name: str | None = None,
    show_child_attributes: bool | None = None,
):
    return create_comment(
        parent,
        rich_text,
        attachments=attachments,
        display_name=display_name,
        show_child_attributes=show_child_attributes,
    )


@mcp.tool()
def notion_retrieve_comment(comment_id: str):
    return retrieve_comment(comment_id)


@mcp.tool()
def notion_list_comments(
    block_id: str | None = None,
    page_id: str | None = None,
    start_cursor: str | None = None,
    page_size: int | None = None,
):
    return list_comments(block_id=block_id, page_id=page_id, start_cursor=start_cursor, page_size=page_size)


# Users
@mcp.tool()
def notion_list_users(
    start_cursor: str | None = None,
    page_size: int | None = None,
    show_child_attributes: bool | None = None,
):
    return list_users(start_cursor=start_cursor, page_size=page_size, show_child_attributes=show_child_attributes)


@mcp.tool()
def notion_retrieve_user(user_id: str):
    return retrieve_user(user_id)


@mcp.tool()
def notion_retrieve_me():
    return retrieve_me()


# Search
@mcp.tool()
def notion_search(
    query: str | None = None,
    filter: dict | None = None,
    sort: dict | None = None,
    start_cursor: str | None = None,
    page_size: int | None = None,
    show_child_attributes: bool | None = None,
):
    return search(
        query=query,
        filter=filter,
        sort=sort,
        start_cursor=start_cursor,
        page_size=page_size,
        show_child_attributes=show_child_attributes,
    )


if __name__ == "__main__":
    mcp.run()
