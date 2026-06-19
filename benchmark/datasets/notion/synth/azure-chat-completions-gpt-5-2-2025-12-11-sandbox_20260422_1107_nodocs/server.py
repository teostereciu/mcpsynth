import os
from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.pages import pages_retrieve, pages_create, pages_update, pages_archive
from generated_tools.databases import databases_retrieve, databases_query, databases_create, databases_update
from generated_tools.blocks import (
    blocks_retrieve,
    blocks_update,
    blocks_delete,
    blocks_children_list,
    blocks_children_append,
)
from generated_tools.comments import comments_list, comments_create
from generated_tools.users import users_list, users_retrieve, users_me
from generated_tools.search import search as notion_search


mcp = FastMCP("notion")


def _nv(notion_version: Optional[str]) -> str:
    return notion_version or os.getenv("NOTION_VERSION") or "2022-06-28"


@mcp.tool()
def notion_pages_retrieve(page_id: str, notion_version: Optional[str] = None) -> Dict[str, Any]:
    return pages_retrieve(page_id, notion_version=_nv(notion_version))


@mcp.tool()
def notion_pages_create(parent: Dict[str, Any], properties: Dict[str, Any], children: Optional[list] = None,
                       icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None,
                       notion_version: Optional[str] = None) -> Dict[str, Any]:
    return pages_create(parent, properties, children=children, icon=icon, cover=cover, notion_version=_nv(notion_version))


@mcp.tool()
def notion_pages_update(page_id: str, properties: Optional[Dict[str, Any]] = None, archived: Optional[bool] = None,
                       icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None,
                       notion_version: Optional[str] = None) -> Dict[str, Any]:
    return pages_update(page_id, properties=properties, archived=archived, icon=icon, cover=cover, notion_version=_nv(notion_version))


@mcp.tool()
def notion_pages_archive(page_id: str, notion_version: Optional[str] = None) -> Dict[str, Any]:
    return pages_archive(page_id, notion_version=_nv(notion_version))


@mcp.tool()
def notion_databases_retrieve(database_id: str, notion_version: Optional[str] = None) -> Dict[str, Any]:
    return databases_retrieve(database_id, notion_version=_nv(notion_version))


@mcp.tool()
def notion_databases_query(database_id: str, filter: Optional[Dict[str, Any]] = None, sorts: Optional[list] = None,
                          start_cursor: Optional[str] = None, page_size: Optional[int] = None,
                          notion_version: Optional[str] = None) -> Dict[str, Any]:
    return databases_query(database_id, filter=filter, sorts=sorts, start_cursor=start_cursor, page_size=page_size, notion_version=_nv(notion_version))


@mcp.tool()
def notion_databases_create(parent: Dict[str, Any], title: list, properties: Dict[str, Any],
                           icon: Optional[Dict[str, Any]] = None, cover: Optional[Dict[str, Any]] = None,
                           notion_version: Optional[str] = None) -> Dict[str, Any]:
    return databases_create(parent, title, properties, icon=icon, cover=cover, notion_version=_nv(notion_version))


@mcp.tool()
def notion_databases_update(database_id: str, title: Optional[list] = None, properties: Optional[Dict[str, Any]] = None,
                           description: Optional[list] = None, icon: Optional[Dict[str, Any]] = None,
                           cover: Optional[Dict[str, Any]] = None, archived: Optional[bool] = None,
                           notion_version: Optional[str] = None) -> Dict[str, Any]:
    return databases_update(
        database_id,
        title=title,
        properties=properties,
        description=description,
        icon=icon,
        cover=cover,
        archived=archived,
        notion_version=_nv(notion_version),
    )


@mcp.tool()
def notion_blocks_retrieve(block_id: str, notion_version: Optional[str] = None) -> Dict[str, Any]:
    return blocks_retrieve(block_id, notion_version=_nv(notion_version))


@mcp.tool()
def notion_blocks_update(block_id: str, block: Dict[str, Any], notion_version: Optional[str] = None) -> Dict[str, Any]:
    return blocks_update(block_id, block, notion_version=_nv(notion_version))


@mcp.tool()
def notion_blocks_delete(block_id: str, notion_version: Optional[str] = None) -> Dict[str, Any]:
    return blocks_delete(block_id, notion_version=_nv(notion_version))


@mcp.tool()
def notion_blocks_children_list(block_id: str, start_cursor: Optional[str] = None, page_size: Optional[int] = None,
                               notion_version: Optional[str] = None) -> Dict[str, Any]:
    return blocks_children_list(block_id, start_cursor=start_cursor, page_size=page_size, notion_version=_nv(notion_version))


@mcp.tool()
def notion_blocks_children_append(block_id: str, children: list, after: Optional[str] = None,
                                 notion_version: Optional[str] = None) -> Dict[str, Any]:
    return blocks_children_append(block_id, children, after=after, notion_version=_nv(notion_version))


@mcp.tool()
def notion_comments_list(block_id: Optional[str] = None, page_id: Optional[str] = None,
                         start_cursor: Optional[str] = None, page_size: Optional[int] = None,
                         notion_version: Optional[str] = None) -> Dict[str, Any]:
    return comments_list(block_id=block_id, page_id=page_id, start_cursor=start_cursor, page_size=page_size, notion_version=_nv(notion_version))


@mcp.tool()
def notion_comments_create(parent: Dict[str, Any], rich_text: list, notion_version: Optional[str] = None) -> Dict[str, Any]:
    return comments_create(parent, rich_text, notion_version=_nv(notion_version))


@mcp.tool()
def notion_users_list(start_cursor: Optional[str] = None, page_size: Optional[int] = None,
                     notion_version: Optional[str] = None) -> Dict[str, Any]:
    return users_list(start_cursor=start_cursor, page_size=page_size, notion_version=_nv(notion_version))


@mcp.tool()
def notion_users_retrieve(user_id: str, notion_version: Optional[str] = None) -> Dict[str, Any]:
    return users_retrieve(user_id, notion_version=_nv(notion_version))


@mcp.tool()
def notion_users_me(notion_version: Optional[str] = None) -> Dict[str, Any]:
    return users_me(notion_version=_nv(notion_version))


@mcp.tool()
def notion_search(query: Optional[str] = None, sort: Optional[Dict[str, Any]] = None, filter: Optional[Dict[str, Any]] = None,
                 start_cursor: Optional[str] = None, page_size: Optional[int] = None,
                 notion_version: Optional[str] = None) -> Dict[str, Any]:
    return notion_search(query, sort=sort, filter=filter, start_cursor=start_cursor, page_size=page_size, notion_version=_nv(notion_version))


if __name__ == "__main__":
    mcp.run()
