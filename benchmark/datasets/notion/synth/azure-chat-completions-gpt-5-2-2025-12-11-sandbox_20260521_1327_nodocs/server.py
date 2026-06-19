from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.blocks import (
    append_block_children,
    delete_block,
    get_block,
    list_block_children,
    update_block,
)
from generated_tools.comments import create_comment, list_comments
from generated_tools.databases import create_database, get_database, query_database, update_database
from generated_tools.pages import archive_page, create_page, get_page, update_page
from generated_tools.search import search
from generated_tools.users import get_me, get_user, list_users


mcp = FastMCP("notion")


@mcp.tool()
def notion_get_page(page_id: str) -> Dict[str, Any]:
    return get_page(page_id)


@mcp.tool()
def notion_create_page(
    parent: Dict[str, Any],
    properties: Dict[str, Any],
    children: Optional[list] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    return create_page(parent, properties, children=children, icon=icon, cover=cover)


@mcp.tool()
def notion_update_page(
    page_id: str,
    properties: Optional[Dict[str, Any]] = None,
    archived: Optional[bool] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    return update_page(page_id, properties=properties, archived=archived, icon=icon, cover=cover)


@mcp.tool()
def notion_archive_page(page_id: str) -> Dict[str, Any]:
    return archive_page(page_id)


@mcp.tool()
def notion_get_database(database_id: str) -> Dict[str, Any]:
    return get_database(database_id)


@mcp.tool()
def notion_query_database(
    database_id: str,
    filter: Optional[Dict[str, Any]] = None,
    sorts: Optional[list] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Dict[str, Any]:
    return query_database(
        database_id,
        filter=filter,
        sorts=sorts,
        start_cursor=start_cursor,
        page_size=page_size,
    )


@mcp.tool()
def notion_create_database(
    parent: Dict[str, Any],
    title: list,
    properties: Dict[str, Any],
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    description: Optional[list] = None,
    is_inline: Optional[bool] = None,
) -> Dict[str, Any]:
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
    title: Optional[list] = None,
    properties: Optional[Dict[str, Any]] = None,
    description: Optional[list] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    is_inline: Optional[bool] = None,
) -> Dict[str, Any]:
    return update_database(
        database_id,
        title=title,
        properties=properties,
        description=description,
        icon=icon,
        cover=cover,
        is_inline=is_inline,
    )


@mcp.tool()
def notion_get_block(block_id: str) -> Dict[str, Any]:
    return get_block(block_id)


@mcp.tool()
def notion_update_block(block_id: str, block: Dict[str, Any]) -> Dict[str, Any]:
    return update_block(block_id, block)


@mcp.tool()
def notion_delete_block(block_id: str) -> Dict[str, Any]:
    return delete_block(block_id)


@mcp.tool()
def notion_list_block_children(
    block_id: str,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Dict[str, Any]:
    return list_block_children(block_id, start_cursor=start_cursor, page_size=page_size)


@mcp.tool()
def notion_append_block_children(block_id: str, children: list, after: Optional[str] = None) -> Dict[str, Any]:
    return append_block_children(block_id, children, after=after)


@mcp.tool()
def notion_list_comments(
    block_id: Optional[str] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Dict[str, Any]:
    return list_comments(block_id=block_id, start_cursor=start_cursor, page_size=page_size)


@mcp.tool()
def notion_create_comment(parent: Dict[str, Any], rich_text: list) -> Dict[str, Any]:
    return create_comment(parent, rich_text)


@mcp.tool()
def notion_list_users(start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Dict[str, Any]:
    return list_users(start_cursor=start_cursor, page_size=page_size)


@mcp.tool()
def notion_get_user(user_id: str) -> Dict[str, Any]:
    return get_user(user_id)


@mcp.tool()
def notion_get_me() -> Dict[str, Any]:
    return get_me()


@mcp.tool()
def notion_search(
    query: Optional[str] = None,
    sort: Optional[Dict[str, Any]] = None,
    filter: Optional[Dict[str, Any]] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Dict[str, Any]:
    return search(query=query, sort=sort, filter=filter, start_cursor=start_cursor, page_size=page_size)


if __name__ == "__main__":
    mcp.run_stdio()
