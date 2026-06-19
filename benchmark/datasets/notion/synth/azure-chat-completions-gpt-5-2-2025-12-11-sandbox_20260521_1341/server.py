from mcp.server.fastmcp import FastMCP

from generated_tools.blocks import (
    blocks_children_append,
    blocks_children_list,
    blocks_delete,
    blocks_retrieve,
    blocks_update,
)
from generated_tools.comments import comments_create, comments_list, comments_retrieve
from generated_tools.databases import databases_create, databases_query, databases_retrieve, databases_update
from generated_tools.pages import pages_create, pages_retrieve, pages_update
from generated_tools.search import search_by_title
from generated_tools.users import users_list, users_me, users_retrieve


mcp = FastMCP("notion")


# Pages
@mcp.tool()
def notion_pages_create(
    parent: dict,
    properties: dict,
    children: list | None = None,
    content_markdown: str | None = None,
    icon: dict | None = None,
    cover: dict | None = None,
    template: dict | None = None,
):
    return pages_create(
        parent=parent,
        properties=properties,
        children=children,
        content_markdown=content_markdown,
        icon=icon,
        cover=cover,
        template=template,
    )


@mcp.tool()
def notion_pages_retrieve(page_id: str, filter_properties: list[str] | None = None):
    return pages_retrieve(page_id=page_id, filter_properties=filter_properties)


@mcp.tool()
def notion_pages_update(
    page_id: str,
    properties: dict | None = None,
    icon: dict | None = None,
    cover: dict | None = None,
    in_trash: bool | None = None,
    archived: bool | None = None,
    locked: bool | None = None,
    erase_content: bool | None = None,
    children: list | None = None,
    content_markdown: str | None = None,
    template: dict | None = None,
):
    return pages_update(
        page_id=page_id,
        properties=properties,
        icon=icon,
        cover=cover,
        in_trash=in_trash,
        archived=archived,
        locked=locked,
        erase_content=erase_content,
        children=children,
        content_markdown=content_markdown,
        template=template,
    )


# Databases
@mcp.tool()
def notion_databases_create(
    parent: dict,
    title: list,
    description: list | None = None,
    is_inline: bool | None = None,
    data_sources: list | None = None,
    icon: dict | None = None,
    cover: dict | None = None,
):
    return databases_create(
        parent=parent,
        title=title,
        description=description,
        is_inline=is_inline,
        data_sources=data_sources,
        icon=icon,
        cover=cover,
    )


@mcp.tool()
def notion_databases_retrieve(database_id: str):
    return databases_retrieve(database_id=database_id)


@mcp.tool()
def notion_databases_update(
    database_id: str,
    parent: dict | None = None,
    title: list | None = None,
    description: list | None = None,
    is_inline: bool | None = None,
    icon: dict | None = None,
    cover: dict | None = None,
    in_trash: bool | None = None,
    locked: bool | None = None,
    properties: dict | None = None,
):
    return databases_update(
        database_id=database_id,
        parent=parent,
        title=title,
        description=description,
        is_inline=is_inline,
        icon=icon,
        cover=cover,
        in_trash=in_trash,
        locked=locked,
        properties=properties,
    )


@mcp.tool()
def notion_databases_query(
    database_id: str,
    filter: dict | None = None,
    sorts: list | None = None,
    start_cursor: str | None = None,
    page_size: int | None = None,
    filter_properties: list[str] | None = None,
):
    return databases_query(
        database_id=database_id,
        filter=filter,
        sorts=sorts,
        start_cursor=start_cursor,
        page_size=page_size,
        filter_properties=filter_properties,
    )


# Blocks
@mcp.tool()
def notion_blocks_retrieve(block_id: str):
    return blocks_retrieve(block_id=block_id)


@mcp.tool()
def notion_blocks_children_list(
    block_id: str, start_cursor: str | None = None, page_size: int | None = None
):
    return blocks_children_list(
        block_id=block_id, start_cursor=start_cursor, page_size=page_size
    )


@mcp.tool()
def notion_blocks_children_append(
    block_id: str, children: list, position: dict | None = None
):
    return blocks_children_append(block_id=block_id, children=children, position=position)


@mcp.tool()
def notion_blocks_update(block_id: str, **block_fields):
    return blocks_update(block_id=block_id, **block_fields)


@mcp.tool()
def notion_blocks_delete(block_id: str):
    return blocks_delete(block_id=block_id)


# Comments
@mcp.tool()
def notion_comments_create(
    parent: dict,
    rich_text: list,
    attachments: list | None = None,
    display_name: dict | None = None,
):
    return comments_create(
        parent=parent,
        rich_text=rich_text,
        attachments=attachments,
        display_name=display_name,
    )


@mcp.tool()
def notion_comments_list(
    block_id: str, start_cursor: str | None = None, page_size: int | None = None
):
    return comments_list(block_id=block_id, start_cursor=start_cursor, page_size=page_size)


@mcp.tool()
def notion_comments_retrieve(comment_id: str):
    return comments_retrieve(comment_id=comment_id)


# Search
@mcp.tool()
def notion_search_by_title(
    query: str | None = None,
    filter: dict | None = None,
    sort: dict | None = None,
    start_cursor: str | None = None,
    page_size: int | None = None,
):
    return search_by_title(
        query=query,
        filter=filter,
        sort=sort,
        start_cursor=start_cursor,
        page_size=page_size,
    )


# Users
@mcp.tool()
def notion_users_list(start_cursor: str | None = None, page_size: int | None = None):
    return users_list(start_cursor=start_cursor, page_size=page_size)


@mcp.tool()
def notion_users_retrieve(user_id: str):
    return users_retrieve(user_id=user_id)


@mcp.tool()
def notion_users_me():
    return users_me()


if __name__ == "__main__":
    mcp.run()
