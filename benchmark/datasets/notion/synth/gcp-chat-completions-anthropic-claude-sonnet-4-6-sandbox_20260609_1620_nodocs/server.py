"""
MCP Server for the Notion API.

Covers:
  - Pages      : retrieve, create, update, archive
  - Databases  : retrieve, create, query, update
  - Blocks     : retrieve, append children, update, delete
  - Comments   : list, create
  - Users      : list, retrieve, me
  - Search     : search pages & databases
  - Block children: list children

Authentication: NOTION_API_KEY env var (Bearer token)
Notion-Version: 2022-06-28
"""

import os
import json
from typing import Any, Optional

import requests
from mcp.server.fastmcp import FastMCP

# ---------------------------------------------------------------------------
# Initialisation
# ---------------------------------------------------------------------------

mcp = FastMCP("notion")

NOTION_VERSION = "2022-06-28"
BASE_URL = "https://api.notion.com/v1"


def _headers() -> dict:
    api_key = os.environ.get("NOTION_API_KEY", "")
    return {
        "Authorization": f"Bearer {api_key}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def _get(path: str, params: Optional[dict] = None) -> Any:
    try:
        resp = requests.get(f"{BASE_URL}{path}", headers=_headers(), params=params, timeout=30)
        return resp.json()
    except Exception as exc:
        return {"error": str(exc)}


def _post(path: str, body: Optional[dict] = None) -> Any:
    try:
        resp = requests.post(f"{BASE_URL}{path}", headers=_headers(), json=body or {}, timeout=30)
        return resp.json()
    except Exception as exc:
        return {"error": str(exc)}


def _patch(path: str, body: Optional[dict] = None) -> Any:
    try:
        resp = requests.patch(f"{BASE_URL}{path}", headers=_headers(), json=body or {}, timeout=30)
        return resp.json()
    except Exception as exc:
        return {"error": str(exc)}


def _delete(path: str) -> Any:
    try:
        resp = requests.delete(f"{BASE_URL}{path}", headers=_headers(), timeout=30)
        return resp.json()
    except Exception as exc:
        return {"error": str(exc)}


# ===========================================================================
# PAGES
# ===========================================================================

@mcp.tool()
def retrieve_page(page_id: str) -> dict:
    """Retrieve a Notion page by its ID.

    Args:
        page_id: The UUID of the Notion page (with or without hyphens).
    """
    return _get(f"/pages/{page_id}")


@mcp.tool()
def retrieve_page_property(page_id: str, property_id: str) -> dict:
    """Retrieve a specific property item from a page.

    Args:
        page_id: The UUID of the page.
        property_id: The ID of the property to retrieve.
    """
    return _get(f"/pages/{page_id}/properties/{property_id}")


@mcp.tool()
def create_page(
    parent_type: str,
    parent_id: str,
    properties: str,
    children: Optional[str] = None,
    icon_emoji: Optional[str] = None,
    cover_url: Optional[str] = None,
) -> dict:
    """Create a new Notion page.

    Args:
        parent_type: Either "database_id" or "page_id" — the type of parent.
        parent_id: UUID of the parent database or page.
        properties: JSON string of page properties (must match the parent database schema
                    when parent is a database). For a plain page parent use
                    {"title": [{"text": {"content": "My title"}}]}.
        children: Optional JSON string of block objects to add as page content.
        icon_emoji: Optional single emoji character to use as the page icon.
        cover_url: Optional external image URL for the page cover.
    """
    body: dict = {
        "parent": {parent_type: parent_id},
        "properties": json.loads(properties),
    }
    if children:
        body["children"] = json.loads(children)
    if icon_emoji:
        body["icon"] = {"type": "emoji", "emoji": icon_emoji}
    if cover_url:
        body["cover"] = {"type": "external", "external": {"url": cover_url}}
    return _post("/pages", body)


@mcp.tool()
def update_page_properties(page_id: str, properties: str) -> dict:
    """Update properties on an existing Notion page.

    Args:
        page_id: UUID of the page to update.
        properties: JSON string of property values to update.
    """
    body = {"properties": json.loads(properties)}
    return _patch(f"/pages/{page_id}", body)


@mcp.tool()
def archive_page(page_id: str) -> dict:
    """Archive (soft-delete) a Notion page.

    Args:
        page_id: UUID of the page to archive.
    """
    return _patch(f"/pages/{page_id}", {"archived": True})


@mcp.tool()
def unarchive_page(page_id: str) -> dict:
    """Restore (un-archive) a previously archived Notion page.

    Args:
        page_id: UUID of the page to restore.
    """
    return _patch(f"/pages/{page_id}", {"archived": False})


@mcp.tool()
def set_page_icon(page_id: str, icon_type: str, value: str) -> dict:
    """Set or update the icon of a Notion page.

    Args:
        page_id: UUID of the page.
        icon_type: "emoji" for an emoji icon, or "external" for an image URL.
        value: The emoji character or the external image URL.
    """
    if icon_type == "emoji":
        icon = {"type": "emoji", "emoji": value}
    else:
        icon = {"type": "external", "external": {"url": value}}
    return _patch(f"/pages/{page_id}", {"icon": icon})


@mcp.tool()
def set_page_cover(page_id: str, cover_url: str) -> dict:
    """Set or update the cover image of a Notion page.

    Args:
        page_id: UUID of the page.
        cover_url: External image URL to use as the cover.
    """
    cover = {"type": "external", "external": {"url": cover_url}}
    return _patch(f"/pages/{page_id}", {"cover": cover})


# ===========================================================================
# DATABASES
# ===========================================================================

@mcp.tool()
def retrieve_database(database_id: str) -> dict:
    """Retrieve a Notion database schema by its ID.

    Args:
        database_id: UUID of the database.
    """
    return _get(f"/databases/{database_id}")


@mcp.tool()
def create_database(
    parent_page_id: str,
    title: str,
    properties: str,
    is_inline: bool = False,
    icon_emoji: Optional[str] = None,
    cover_url: Optional[str] = None,
) -> dict:
    """Create a new Notion database as a child of a page.

    Args:
        parent_page_id: UUID of the parent page.
        title: Plain-text title for the database.
        properties: JSON string defining the database schema (property definitions).
                    Must include at least a "title" property of type "title".
                    Example: {"Name": {"title": {}}, "Status": {"select": {"options": []}}}
        is_inline: If True the database is rendered inline in the parent page.
        icon_emoji: Optional emoji icon for the database.
        cover_url: Optional external cover image URL.
    """
    body: dict = {
        "parent": {"type": "page_id", "page_id": parent_page_id},
        "title": [{"type": "text", "text": {"content": title}}],
        "properties": json.loads(properties),
        "is_inline": is_inline,
    }
    if icon_emoji:
        body["icon"] = {"type": "emoji", "emoji": icon_emoji}
    if cover_url:
        body["cover"] = {"type": "external", "external": {"url": cover_url}}
    return _post("/databases", body)


@mcp.tool()
def update_database(
    database_id: str,
    title: Optional[str] = None,
    description: Optional[str] = None,
    properties: Optional[str] = None,
) -> dict:
    """Update a Notion database's title, description, or schema.

    Args:
        database_id: UUID of the database to update.
        title: New plain-text title (optional).
        description: New plain-text description (optional).
        properties: JSON string of property schema changes (optional).
    """
    body: dict = {}
    if title is not None:
        body["title"] = [{"type": "text", "text": {"content": title}}]
    if description is not None:
        body["description"] = [{"type": "text", "text": {"content": description}}]
    if properties is not None:
        body["properties"] = json.loads(properties)
    return _patch(f"/databases/{database_id}", body)


@mcp.tool()
def query_database(
    database_id: str,
    filter: Optional[str] = None,
    sorts: Optional[str] = None,
    start_cursor: Optional[str] = None,
    page_size: int = 100,
) -> dict:
    """Query a Notion database with optional filters and sorts.

    Args:
        database_id: UUID of the database to query.
        filter: Optional JSON string of a Notion filter object.
                Example: {"property": "Status", "select": {"equals": "Done"}}
        sorts: Optional JSON string of a list of sort objects.
               Example: [{"property": "Created", "direction": "descending"}]
        start_cursor: Pagination cursor from a previous response's next_cursor field.
        page_size: Number of results per page (1–100, default 100).
    """
    body: dict = {"page_size": min(max(page_size, 1), 100)}
    if filter:
        body["filter"] = json.loads(filter)
    if sorts:
        body["sorts"] = json.loads(sorts)
    if start_cursor:
        body["start_cursor"] = start_cursor
    return _post(f"/databases/{database_id}/query", body)


@mcp.tool()
def query_database_with_compound_filter(
    database_id: str,
    filter: str,
    sorts: Optional[str] = None,
    start_cursor: Optional[str] = None,
    page_size: int = 100,
) -> dict:
    """Query a database using a compound (and/or) filter.

    Args:
        database_id: UUID of the database.
        filter: JSON string of a compound filter, e.g.
                {"and": [{"property": "Done", "checkbox": {"equals": true}},
                          {"property": "Tags", "multi_select": {"contains": "Design"}}]}
        sorts: Optional JSON string list of sort objects.
        start_cursor: Pagination cursor.
        page_size: Results per page (1–100).
    """
    body: dict = {"filter": json.loads(filter), "page_size": min(max(page_size, 1), 100)}
    if sorts:
        body["sorts"] = json.loads(sorts)
    if start_cursor:
        body["start_cursor"] = start_cursor
    return _post(f"/databases/{database_id}/query", body)


# ===========================================================================
# BLOCKS
# ===========================================================================

@mcp.tool()
def retrieve_block(block_id: str) -> dict:
    """Retrieve a single Notion block by its ID.

    Args:
        block_id: UUID of the block.
    """
    return _get(f"/blocks/{block_id}")


@mcp.tool()
def retrieve_block_children(
    block_id: str,
    start_cursor: Optional[str] = None,
    page_size: int = 100,
) -> dict:
    """List the children blocks of a block (or page).

    Args:
        block_id: UUID of the parent block or page.
        start_cursor: Pagination cursor from a previous response.
        page_size: Number of results per page (1–100).
    """
    params: dict = {"page_size": min(max(page_size, 1), 100)}
    if start_cursor:
        params["start_cursor"] = start_cursor
    return _get(f"/blocks/{block_id}/children", params)


@mcp.tool()
def append_block_children(block_id: str, children: str) -> dict:
    """Append new child blocks to an existing block or page.

    Args:
        block_id: UUID of the parent block or page.
        children: JSON string of a list of block objects to append.
                  Example: [{"object": "block", "type": "paragraph",
                              "paragraph": {"rich_text": [{"type": "text",
                              "text": {"content": "Hello world"}}]}}]
    """
    body = {"children": json.loads(children)}
    return _patch(f"/blocks/{block_id}/children", body)


@mcp.tool()
def update_block(block_id: str, block_data: str) -> dict:
    """Update the content of an existing block.

    Args:
        block_id: UUID of the block to update.
        block_data: JSON string of the block type object with updated content.
                    Example: {"paragraph": {"rich_text": [{"type": "text",
                    "text": {"content": "Updated text"}}]}}
    """
    return _patch(f"/blocks/{block_id}", json.loads(block_data))


@mcp.tool()
def delete_block(block_id: str) -> dict:
    """Delete (archive) a block by its ID.

    Args:
        block_id: UUID of the block to delete.
    """
    return _delete(f"/blocks/{block_id}")


@mcp.tool()
def append_paragraph(block_id: str, text: str) -> dict:
    """Convenience tool: append a plain paragraph block to a page or block.

    Args:
        block_id: UUID of the parent page or block.
        text: Plain text content of the paragraph.
    """
    children = [
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": text}}]
            },
        }
    ]
    return _patch(f"/blocks/{block_id}/children", {"children": children})


@mcp.tool()
def append_heading(block_id: str, text: str, level: int = 1) -> dict:
    """Convenience tool: append a heading block (H1, H2, or H3) to a page or block.

    Args:
        block_id: UUID of the parent page or block.
        text: Heading text content.
        level: Heading level — 1, 2, or 3 (default 1).
    """
    level = max(1, min(level, 3))
    block_type = f"heading_{level}"
    children = [
        {
            "object": "block",
            "type": block_type,
            block_type: {
                "rich_text": [{"type": "text", "text": {"content": text}}]
            },
        }
    ]
    return _patch(f"/blocks/{block_id}/children", {"children": children})


@mcp.tool()
def append_bulleted_list(block_id: str, items: str) -> dict:
    """Convenience tool: append bulleted list items to a page or block.

    Args:
        block_id: UUID of the parent page or block.
        items: JSON string list of plain-text strings, one per bullet.
               Example: ["First item", "Second item"]
    """
    texts = json.loads(items)
    children = [
        {
            "object": "block",
            "type": "bulleted_list_item",
            "bulleted_list_item": {
                "rich_text": [{"type": "text", "text": {"content": t}}]
            },
        }
        for t in texts
    ]
    return _patch(f"/blocks/{block_id}/children", {"children": children})


@mcp.tool()
def append_numbered_list(block_id: str, items: str) -> dict:
    """Convenience tool: append numbered list items to a page or block.

    Args:
        block_id: UUID of the parent page or block.
        items: JSON string list of plain-text strings, one per numbered item.
               Example: ["Step one", "Step two"]
    """
    texts = json.loads(items)
    children = [
        {
            "object": "block",
            "type": "numbered_list_item",
            "numbered_list_item": {
                "rich_text": [{"type": "text", "text": {"content": t}}]
            },
        }
        for t in texts
    ]
    return _patch(f"/blocks/{block_id}/children", {"children": children})


@mcp.tool()
def append_todo(block_id: str, text: str, checked: bool = False) -> dict:
    """Convenience tool: append a to-do (checkbox) block to a page or block.

    Args:
        block_id: UUID of the parent page or block.
        text: Text content of the to-do item.
        checked: Whether the checkbox is checked (default False).
    """
    children = [
        {
            "object": "block",
            "type": "to_do",
            "to_do": {
                "rich_text": [{"type": "text", "text": {"content": text}}],
                "checked": checked,
            },
        }
    ]
    return _patch(f"/blocks/{block_id}/children", {"children": children})


@mcp.tool()
def append_code_block(block_id: str, code: str, language: str = "plain text") -> dict:
    """Convenience tool: append a code block to a page or block.

    Args:
        block_id: UUID of the parent page or block.
        code: The code content.
        language: Programming language for syntax highlighting (e.g. "python", "javascript").
                  Defaults to "plain text".
    """
    children = [
        {
            "object": "block",
            "type": "code",
            "code": {
                "rich_text": [{"type": "text", "text": {"content": code}}],
                "language": language,
            },
        }
    ]
    return _patch(f"/blocks/{block_id}/children", {"children": children})


@mcp.tool()
def append_divider(block_id: str) -> dict:
    """Convenience tool: append a horizontal divider block to a page or block.

    Args:
        block_id: UUID of the parent page or block.
    """
    children = [{"object": "block", "type": "divider", "divider": {}}]
    return _patch(f"/blocks/{block_id}/children", {"children": children})


@mcp.tool()
def append_callout(
    block_id: str,
    text: str,
    icon_emoji: str = "💡",
) -> dict:
    """Convenience tool: append a callout block to a page or block.

    Args:
        block_id: UUID of the parent page or block.
        text: Text content of the callout.
        icon_emoji: Emoji icon for the callout (default 💡).
    """
    children = [
        {
            "object": "block",
            "type": "callout",
            "callout": {
                "rich_text": [{"type": "text", "text": {"content": text}}],
                "icon": {"type": "emoji", "emoji": icon_emoji},
            },
        }
    ]
    return _patch(f"/blocks/{block_id}/children", {"children": children})


@mcp.tool()
def append_toggle(block_id: str, text: str, children_blocks: Optional[str] = None) -> dict:
    """Convenience tool: append a toggle block to a page or block.

    Args:
        block_id: UUID of the parent page or block.
        text: Toggle summary text.
        children_blocks: Optional JSON string list of child block objects inside the toggle.
    """
    toggle_block: dict = {
        "object": "block",
        "type": "toggle",
        "toggle": {
            "rich_text": [{"type": "text", "text": {"content": text}}],
        },
    }
    if children_blocks:
        toggle_block["toggle"]["children"] = json.loads(children_blocks)
    return _patch(f"/blocks/{block_id}/children", {"children": [toggle_block]})


@mcp.tool()
def append_image(block_id: str, image_url: str) -> dict:
    """Convenience tool: append an external image block to a page or block.

    Args:
        block_id: UUID of the parent page or block.
        image_url: Publicly accessible URL of the image.
    """
    children = [
        {
            "object": "block",
            "type": "image",
            "image": {"type": "external", "external": {"url": image_url}},
        }
    ]
    return _patch(f"/blocks/{block_id}/children", {"children": children})


@mcp.tool()
def append_bookmark(block_id: str, url: str, caption: Optional[str] = None) -> dict:
    """Convenience tool: append a bookmark block to a page or block.

    Args:
        block_id: UUID of the parent page or block.
        url: URL to bookmark.
        caption: Optional caption text for the bookmark.
    """
    bookmark: dict = {"url": url}
    if caption:
        bookmark["caption"] = [{"type": "text", "text": {"content": caption}}]
    children = [{"object": "block", "type": "bookmark", "bookmark": bookmark}]
    return _patch(f"/blocks/{block_id}/children", {"children": children})


@mcp.tool()
def append_quote(block_id: str, text: str) -> dict:
    """Convenience tool: append a quote block to a page or block.

    Args:
        block_id: UUID of the parent page or block.
        text: Quote text content.
    """
    children = [
        {
            "object": "block",
            "type": "quote",
            "quote": {
                "rich_text": [{"type": "text", "text": {"content": text}}]
            },
        }
    ]
    return _patch(f"/blocks/{block_id}/children", {"children": children})


@mcp.tool()
def append_table_of_contents(block_id: str) -> dict:
    """Convenience tool: append a Table of Contents block to a page or block.

    Args:
        block_id: UUID of the parent page or block.
    """
    children = [{"object": "block", "type": "table_of_contents", "table_of_contents": {}}]
    return _patch(f"/blocks/{block_id}/children", {"children": children})


# ===========================================================================
# COMMENTS
# ===========================================================================

@mcp.tool()
def list_comments(
    block_id: Optional[str] = None,
    page_id: Optional[str] = None,
    start_cursor: Optional[str] = None,
    page_size: int = 100,
) -> dict:
    """List comments on a page or block.

    Args:
        block_id: UUID of the block to list comments for (use this OR page_id).
        page_id: UUID of the page to list comments for (use this OR block_id).
        start_cursor: Pagination cursor from a previous response.
        page_size: Number of results per page (1–100).
    """
    params: dict = {"page_size": min(max(page_size, 1), 100)}
    if block_id:
        params["block_id"] = block_id
    elif page_id:
        params["block_id"] = page_id  # Notion API uses block_id for pages too
    if start_cursor:
        params["start_cursor"] = start_cursor
    return _get("/comments", params)


@mcp.tool()
def create_comment(
    rich_text: str,
    page_id: Optional[str] = None,
    discussion_id: Optional[str] = None,
) -> dict:
    """Create a comment on a page or in an existing discussion thread.

    Args:
        rich_text: JSON string of a rich_text array.
                   Example: [{"type": "text", "text": {"content": "My comment"}}]
        page_id: UUID of the page to add a top-level comment to (use this OR discussion_id).
        discussion_id: ID of an existing discussion thread to reply to.
    """
    body: dict = {"rich_text": json.loads(rich_text)}
    if discussion_id:
        body["discussion_id"] = discussion_id
    elif page_id:
        body["parent"] = {"type": "page_id", "page_id": page_id}
    return _post("/comments", body)


# ===========================================================================
# USERS
# ===========================================================================

@mcp.tool()
def list_users(start_cursor: Optional[str] = None, page_size: int = 100) -> dict:
    """List all users in the Notion workspace.

    Args:
        start_cursor: Pagination cursor from a previous response.
        page_size: Number of results per page (1–100).
    """
    params: dict = {"page_size": min(max(page_size, 1), 100)}
    if start_cursor:
        params["start_cursor"] = start_cursor
    return _get("/users", params)


@mcp.tool()
def retrieve_user(user_id: str) -> dict:
    """Retrieve a Notion user by their ID.

    Args:
        user_id: UUID of the user.
    """
    return _get(f"/users/{user_id}")


@mcp.tool()
def retrieve_bot_user() -> dict:
    """Retrieve the bot user associated with the current integration token."""
    return _get("/users/me")


# ===========================================================================
# SEARCH
# ===========================================================================

@mcp.tool()
def search(
    query: Optional[str] = None,
    filter_object_type: Optional[str] = None,
    sort_direction: str = "descending",
    sort_timestamp: str = "last_edited_time",
    start_cursor: Optional[str] = None,
    page_size: int = 100,
) -> dict:
    """Search pages and databases accessible to the integration.

    Args:
        query: Text to search for in page/database titles. Omit to return all.
        filter_object_type: Limit results to "page" or "database" (optional).
        sort_direction: "ascending" or "descending" (default "descending").
        sort_timestamp: Timestamp to sort by — "last_edited_time" (default) or
                        "created_time".
        start_cursor: Pagination cursor from a previous response.
        page_size: Number of results per page (1–100).
    """
    body: dict = {
        "sort": {"direction": sort_direction, "timestamp": sort_timestamp},
        "page_size": min(max(page_size, 1), 100),
    }
    if query:
        body["query"] = query
    if filter_object_type:
        body["filter"] = {"value": filter_object_type, "property": "object"}
    if start_cursor:
        body["start_cursor"] = start_cursor
    return _post("/search", body)


@mcp.tool()
def search_pages(query: str, page_size: int = 20) -> dict:
    """Search for pages by title query string.

    Args:
        query: Text to search for in page titles.
        page_size: Number of results (1–100, default 20).
    """
    body = {
        "query": query,
        "filter": {"value": "page", "property": "object"},
        "sort": {"direction": "descending", "timestamp": "last_edited_time"},
        "page_size": min(max(page_size, 1), 100),
    }
    return _post("/search", body)


@mcp.tool()
def search_databases(query: str, page_size: int = 20) -> dict:
    """Search for databases by title query string.

    Args:
        query: Text to search for in database titles.
        page_size: Number of results (1–100, default 20).
    """
    body = {
        "query": query,
        "filter": {"value": "database", "property": "object"},
        "sort": {"direction": "descending", "timestamp": "last_edited_time"},
        "page_size": min(max(page_size, 1), 100),
    }
    return _post("/search", body)


# ===========================================================================
# ENTRY POINT
# ===========================================================================

if __name__ == "__main__":
    mcp.run()
