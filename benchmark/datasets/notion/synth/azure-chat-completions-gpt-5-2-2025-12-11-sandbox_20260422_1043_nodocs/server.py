from mcp.server.fastmcp import FastMCP

from generated_tools.pages import pages_archive, pages_create, pages_retrieve, pages_update
from generated_tools.databases import (
    databases_create,
    databases_query,
    databases_retrieve,
    databases_update,
)
from generated_tools.blocks import (
    blocks_children_append,
    blocks_children_list,
    blocks_delete,
    blocks_retrieve,
    blocks_update,
)
from generated_tools.comments import comments_create, comments_list
from generated_tools.users import users_list, users_me, users_retrieve
from generated_tools.search import search


mcp = FastMCP("notion")


@mcp.tool
def notion_pages_retrieve(page_id: str, notion_version: str = "2022-06-28"):
    return pages_retrieve(page_id, notion_version=notion_version)


@mcp.tool
def notion_pages_create(
    parent: dict,
    properties: dict,
    children: list | None = None,
    icon: dict | None = None,
    cover: dict | None = None,
    notion_version: str = "2022-06-28",
):
    return pages_create(
        parent=parent,
        properties=properties,
        children=children,
        icon=icon,
        cover=cover,
        notion_version=notion_version,
    )


@mcp.tool
def notion_pages_update(
    page_id: str,
    properties: dict | None = None,
    archived: bool | None = None,
    icon: dict | None = None,
    cover: dict | None = None,
    notion_version: str = "2022-06-28",
):
    return pages_update(
        page_id,
        properties=properties,
        archived=archived,
        icon=icon,
        cover=cover,
        notion_version=notion_version,
    )


@mcp.tool
def notion_pages_archive(page_id: str, notion_version: str = "2022-06-28"):
    return pages_archive(page_id, notion_version=notion_version)


@mcp.tool
def notion_databases_retrieve(database_id: str, notion_version: str = "2022-06-28"):
    return databases_retrieve(database_id, notion_version=notion_version)


@mcp.tool
def notion_databases_query(
    database_id: str,
    filter: dict | None = None,
    sorts: list | None = None,
    start_cursor: str | None = None,
    page_size: int | None = None,
    notion_version: str = "2022-06-28",
):
    return databases_query(
        database_id,
        filter=filter,
        sorts=sorts,
        start_cursor=start_cursor,
        page_size=page_size,
        notion_version=notion_version,
    )


@mcp.tool
def notion_databases_create(
    parent: dict,
    title: list,
    properties: dict,
    icon: dict | None = None,
    cover: dict | None = None,
    description: list | None = None,
    is_inline: bool | None = None,
    notion_version: str = "2022-06-28",
):
    return databases_create(
        parent=parent,
        title=title,
        properties=properties,
        icon=icon,
        cover=cover,
        description=description,
        is_inline=is_inline,
        notion_version=notion_version,
    )


@mcp.tool
def notion_databases_update(
    database_id: str,
    title: list | None = None,
    properties: dict | None = None,
    description: list | None = None,
    icon: dict | None = None,
    cover: dict | None = None,
    archived: bool | None = None,
    notion_version: str = "2022-06-28",
):
    return databases_update(
        database_id,
        title=title,
        properties=properties,
        description=description,
        icon=icon,
        cover=cover,
        archived=archived,
        notion_version=notion_version,
    )


@mcp.tool
def notion_blocks_retrieve(block_id: str, notion_version: str = "2022-06-28"):
    return blocks_retrieve(block_id, notion_version=notion_version)


@mcp.tool
def notion_blocks_update(block_id: str, block: dict, notion_version: str = "2022-06-28"):
    return blocks_update(block_id, block, notion_version=notion_version)


@mcp.tool
def notion_blocks_delete(block_id: str, notion_version: str = "2022-06-28"):
    return blocks_delete(block_id, notion_version=notion_version)


@mcp.tool
def notion_blocks_children_list(
    block_id: str,
    start_cursor: str | None = None,
    page_size: int | None = None,
    notion_version: str = "2022-06-28",
):
    return blocks_children_list(
        block_id,
        start_cursor=start_cursor,
        page_size=page_size,
        notion_version=notion_version,
    )


@mcp.tool
def notion_blocks_children_append(
    block_id: str,
    children: list,
    after: str | None = None,
    notion_version: str = "2022-06-28",
):
    return blocks_children_append(block_id, children, after=after, notion_version=notion_version)


@mcp.tool
def notion_comments_create(
    parent: dict | None = None,
    discussion_id: str | None = None,
    rich_text: list | None = None,
    notion_version: str = "2022-06-28",
):
    return comments_create(
        parent=parent,
        discussion_id=discussion_id,
        rich_text=rich_text,
        notion_version=notion_version,
    )


@mcp.tool
def notion_comments_list(
    block_id: str | None = None,
    start_cursor: str | None = None,
    page_size: int | None = None,
    notion_version: str = "2022-06-28",
):
    return comments_list(
        block_id=block_id,
        start_cursor=start_cursor,
        page_size=page_size,
        notion_version=notion_version,
    )


@mcp.tool
def notion_users_list(notion_version: str = "2022-06-28"):
    return users_list(notion_version=notion_version)


@mcp.tool
def notion_users_retrieve(user_id: str, notion_version: str = "2022-06-28"):
    return users_retrieve(user_id, notion_version=notion_version)


@mcp.tool
def notion_users_me(notion_version: str = "2022-06-28"):
    return users_me(notion_version=notion_version)


@mcp.tool
def notion_search(
    query: str | None = None,
    sort: dict | None = None,
    filter: dict | None = None,
    start_cursor: str | None = None,
    page_size: int | None = None,
    notion_version: str = "2022-06-28",
):
    return search(
        query=query,
        sort=sort,
        filter=filter,
        start_cursor=start_cursor,
        page_size=page_size,
        notion_version=notion_version,
    )


if __name__ == "__main__":
    mcp.run()
