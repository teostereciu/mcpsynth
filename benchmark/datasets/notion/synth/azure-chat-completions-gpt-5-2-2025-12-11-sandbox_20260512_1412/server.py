from typing import Any, Dict, List, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.pages import (
    pages_archive,
    pages_create,
    pages_move,
    pages_retrieve,
    pages_retrieve_property_item,
    pages_restore,
    pages_update,
)
from generated_tools.databases import (
    databases_create,
    databases_list,
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
from generated_tools.comments import comments_create, comments_list, comments_retrieve
from generated_tools.users import users_list, users_me, users_retrieve
from generated_tools.search import search


mcp = FastMCP("notion")


@mcp.tool()
def notion_pages_create(parent: Dict[str, Any], properties: Dict[str, Any], children: Optional[List[Dict[str, Any]]] = None, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None) -> Any:
    return pages_create(parent, properties, children=children, icon=icon, cover=cover)


@mcp.tool()
def notion_pages_retrieve(page_id: str, filter_properties: Optional[List[str]] = None) -> Any:
    return pages_retrieve(page_id, filter_properties=filter_properties)


@mcp.tool()
def notion_pages_update(page_id: str, properties: Optional[Dict[str, Any]] = None, archived: Optional[bool] = None, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None) -> Any:
    return pages_update(page_id, properties=properties, archived=archived, icon=icon, cover=cover)


@mcp.tool()
def notion_pages_archive(page_id: str) -> Any:
    return pages_archive(page_id)


@mcp.tool()
def notion_pages_restore(page_id: str) -> Any:
    return pages_restore(page_id)


@mcp.tool()
def notion_pages_retrieve_property_item(page_id: str, property_id: str, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    return pages_retrieve_property_item(page_id, property_id, start_cursor=start_cursor, page_size=page_size)


@mcp.tool()
def notion_pages_move(page_id: str, parent: Dict[str, Any]) -> Any:
    return pages_move(page_id, parent)


@mcp.tool()
def notion_databases_create(parent: Dict[str, Any], title: List[Dict[str, Any]], properties: Dict[str, Any], icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None, description: Optional[List[Dict[str, Any]]] = None, is_inline: Optional[bool] = None) -> Any:
    return databases_create(parent, title, properties, icon=icon, cover=cover, description=description, is_inline=is_inline)


@mcp.tool()
def notion_databases_retrieve(database_id: str) -> Any:
    return databases_retrieve(database_id)


@mcp.tool()
def notion_databases_update(database_id: str, title: Optional[List[Dict[str, Any]]] = None, description: Optional[List[Dict[str, Any]]] = None, properties: Optional[Dict[str, Any]] = None, icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None, archived: Optional[bool] = None) -> Any:
    return databases_update(database_id, title=title, description=description, properties=properties, icon=icon, cover=cover, archived=archived)


@mcp.tool()
def notion_databases_list(start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    return databases_list(start_cursor=start_cursor, page_size=page_size)


@mcp.tool()
def notion_databases_query(database_id: str, filter: Optional[Dict[str, Any]] = None, sorts: Optional[List[Dict[str, Any]]] = None, start_cursor: Optional[str] = None, page_size: Optional[int] = None, filter_properties: Optional[List[str]] = None) -> Any:
    return databases_query(database_id, filter=filter, sorts=sorts, start_cursor=start_cursor, page_size=page_size, filter_properties=filter_properties)


@mcp.tool()
def notion_blocks_retrieve(block_id: str) -> Any:
    return blocks_retrieve(block_id)


@mcp.tool()
def notion_blocks_children_list(block_id: str, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    return blocks_children_list(block_id, start_cursor=start_cursor, page_size=page_size)


@mcp.tool()
def notion_blocks_children_append(block_id: str, children: List[Dict[str, Any]], after: Optional[str] = None) -> Any:
    return blocks_children_append(block_id, children, after=after)


@mcp.tool()
def notion_blocks_update(block_id: str, block: Dict[str, Any]) -> Any:
    return blocks_update(block_id, block)


@mcp.tool()
def notion_blocks_delete(block_id: str) -> Any:
    return blocks_delete(block_id)


@mcp.tool()
def notion_comments_create(parent: Dict[str, Any], rich_text: List[Dict[str, Any]], discussion_id: Optional[str] = None) -> Any:
    return comments_create(parent, rich_text, discussion_id=discussion_id)


@mcp.tool()
def notion_comments_retrieve(comment_id: str) -> Any:
    return comments_retrieve(comment_id)


@mcp.tool()
def notion_comments_list(block_id: Optional[str] = None, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    return comments_list(block_id=block_id, start_cursor=start_cursor, page_size=page_size)


@mcp.tool()
def notion_users_list(start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    return users_list(start_cursor=start_cursor, page_size=page_size)


@mcp.tool()
def notion_users_retrieve(user_id: str) -> Any:
    return users_retrieve(user_id)


@mcp.tool()
def notion_users_me() -> Any:
    return users_me()


@mcp.tool()
def notion_search(query: Optional[str] = None, filter: Optional[Dict[str, Any]] = None, sort: Optional[Dict[str, Any]] = None, start_cursor: Optional[str] = None, page_size: Optional[int] = None) -> Any:
    return search(query, filter=filter, sort=sort, start_cursor=start_cursor, page_size=page_size)


if __name__ == "__main__":
    mcp.run()
