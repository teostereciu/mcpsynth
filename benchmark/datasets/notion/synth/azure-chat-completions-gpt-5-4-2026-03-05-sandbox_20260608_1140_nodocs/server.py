from typing import Any, Dict, List, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.blocks import (
    append_block_children,
    delete_block,
    retrieve_block,
    retrieve_block_children,
    update_block,
)
from generated_tools.comments import create_comment, list_comments
from generated_tools.databases import create_database, query_database, retrieve_database, update_database
from generated_tools.pages import (
    archive_page,
    create_page,
    restore_page,
    retrieve_page,
    retrieve_page_property_item,
    update_page,
)
from generated_tools.search import search
from generated_tools.users import list_users, retrieve_bot_user, retrieve_user


mcp = FastMCP("notion")


@mcp.tool()
def notion_create_page(
    parent: Dict[str, Any],
    properties: Dict[str, Any],
    children: Optional[List[Dict[str, Any]]] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
) -> Any:
    return create_page(parent, properties, children, icon, cover)


@mcp.tool()
def notion_retrieve_page(page_id: str) -> Any:
    return retrieve_page(page_id)


@mcp.tool()
def notion_update_page(
    page_id: str,
    properties: Optional[Dict[str, Any]] = None,
    archived: Optional[bool] = None,
    in_trash: Optional[bool] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    is_locked: Optional[bool] = None,
) -> Any:
    return update_page(page_id, properties, archived, in_trash, icon, cover, is_locked)


@mcp.tool()
def notion_archive_page(page_id: str) -> Any:
    return archive_page(page_id)


@mcp.tool()
def notion_restore_page(page_id: str) -> Any:
    return restore_page(page_id)


@mcp.tool()
def notion_retrieve_page_property_item(
    page_id: str,
    property_id: str,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Any:
    return retrieve_page_property_item(page_id, property_id, start_cursor, page_size)


@mcp.tool()
def notion_create_database(
    parent: Dict[str, Any],
    title: List[Dict[str, Any]],
    properties: Dict[str, Any],
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    description: Optional[List[Dict[str, Any]]] = None,
    is_inline: Optional[bool] = None,
) -> Any:
    return create_database(parent, title, properties, icon, cover, description, is_inline)


@mcp.tool()
def notion_retrieve_database(database_id: str) -> Any:
    return retrieve_database(database_id)


@mcp.tool()
def notion_update_database(
    database_id: str,
    title: Optional[List[Dict[str, Any]]] = None,
    description: Optional[List[Dict[str, Any]]] = None,
    properties: Optional[Dict[str, Any]] = None,
    icon: Optional[Dict[str, Any]] = None,
    cover: Optional[Dict[str, Any]] = None,
    is_inline: Optional[bool] = None,
    archived: Optional[bool] = None,
    in_trash: Optional[bool] = None,
) -> Any:
    return update_database(database_id, title, description, properties, icon, cover, is_inline, archived, in_trash)


@mcp.tool()
def notion_query_database(
    database_id: str,
    filter: Optional[Dict[str, Any]] = None,
    sorts: Optional[List[Dict[str, Any]]] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
    archived: Optional[bool] = None,
    in_trash: Optional[bool] = None,
) -> Any:
    return query_database(database_id, filter, sorts, start_cursor, page_size, archived, in_trash)


@mcp.tool()
def notion_retrieve_block(block_id: str) -> Any:
    return retrieve_block(block_id)


@mcp.tool()
def notion_retrieve_block_children(
    block_id: str,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Any:
    return retrieve_block_children(block_id, start_cursor, page_size)


@mcp.tool()
def notion_append_block_children(
    block_id: str,
    children: List[Dict[str, Any]],
    after: Optional[str] = None,
) -> Any:
    return append_block_children(block_id, children, after)


@mcp.tool()
def notion_update_block(
    block_id: str,
    block_type: str,
    block_data: Dict[str, Any],
    archived: Optional[bool] = None,
    in_trash: Optional[bool] = None,
) -> Any:
    return update_block(block_id, block_type, block_data, archived, in_trash)


@mcp.tool()
def notion_delete_block(block_id: str) -> Any:
    return delete_block(block_id)


@mcp.tool()
def notion_create_comment(
    rich_text: List[Dict[str, Any]],
    parent: Optional[Dict[str, Any]] = None,
    discussion_id: Optional[str] = None,
) -> Any:
    return create_comment(rich_text, parent, discussion_id)


@mcp.tool()
def notion_list_comments(
    block_id: str,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Any:
    return list_comments(block_id, start_cursor, page_size)


@mcp.tool()
def notion_list_users(
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Any:
    return list_users(start_cursor, page_size)


@mcp.tool()
def notion_retrieve_user(user_id: str) -> Any:
    return retrieve_user(user_id)


@mcp.tool()
def notion_retrieve_bot_user() -> Any:
    return retrieve_bot_user()


@mcp.tool()
def notion_search(
    query: Optional[str] = None,
    sort: Optional[Dict[str, Any]] = None,
    filter: Optional[Dict[str, Any]] = None,
    start_cursor: Optional[str] = None,
    page_size: Optional[int] = None,
) -> Any:
    return search(query, sort, filter, start_cursor, page_size)


if __name__ == "__main__":
    mcp.run()
