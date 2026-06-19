"""Notion Pages tools."""
from typing import Optional, Any
from mcp.server.fastmcp import FastMCP
from .client import notion_request

def register(mcp: FastMCP):

    @mcp.tool()
    def retrieve_page(page_id: str, filter_properties: Optional[str] = None) -> dict:
        """Retrieve a Notion page by its ID.

        Args:
            page_id: The ID of the page to retrieve.
            filter_properties: Comma-separated list of property IDs to include in the response.
        """
        params = {}
        if filter_properties:
            params["filter_properties"] = filter_properties
        return notion_request("GET", f"/pages/{page_id}", params=params)

    @mcp.tool()
    def create_page(
        parent: dict,
        properties: Optional[dict] = None,
        children: Optional[list] = None,
        icon: Optional[dict] = None,
        cover: Optional[dict] = None,
        markdown_content: Optional[str] = None,
    ) -> dict:
        """Create a new Notion page.

        Args:
            parent: The parent of the page. E.g. {"database_id": "..."} or {"page_id": "..."} or {"data_source_id": "..."}.
            properties: Property values for the page (required when parent is a database).
            children: Array of block objects to set as the page content.
            icon: Icon for the page. E.g. {"type": "emoji", "emoji": "🚀"}.
            cover: Cover image for the page.
            markdown_content: Page content as Notion-flavored Markdown. Mutually exclusive with children.
        """
        body: dict[str, Any] = {"parent": parent}
        if properties is not None:
            body["properties"] = properties
        if children is not None:
            body["children"] = children
        if icon is not None:
            body["icon"] = icon
        if cover is not None:
            body["cover"] = cover
        if markdown_content is not None:
            body["markdown_content"] = markdown_content
        return notion_request("POST", "/pages", json=body)

    @mcp.tool()
    def update_page(
        page_id: str,
        properties: Optional[dict] = None,
        icon: Optional[dict] = None,
        cover: Optional[dict] = None,
        in_trash: Optional[bool] = None,
        is_locked: Optional[bool] = None,
        erase_content: Optional[bool] = None,
    ) -> dict:
        """Update a Notion page's properties, icon, cover, or trash status.

        Args:
            page_id: The ID of the page to update.
            properties: Property values to update.
            icon: New icon for the page. E.g. {"type": "emoji", "emoji": "🎯"}.
            cover: New cover image for the page.
            in_trash: Set to true to trash the page, false to restore it.
            is_locked: Whether to lock the page from editing in the Notion UI.
            erase_content: Whether to erase all existing content from the page.
        """
        body: dict[str, Any] = {}
        if properties is not None:
            body["properties"] = properties
        if icon is not None:
            body["icon"] = icon
        if cover is not None:
            body["cover"] = cover
        if in_trash is not None:
            body["in_trash"] = in_trash
        if is_locked is not None:
            body["is_locked"] = is_locked
        if erase_content is not None:
            body["erase_content"] = erase_content
        return notion_request("PATCH", f"/pages/{page_id}", json=body)

    @mcp.tool()
    def trash_page(page_id: str) -> dict:
        """Move a Notion page to the trash.

        Args:
            page_id: The ID of the page to trash.
        """
        return notion_request("PATCH", f"/pages/{page_id}", json={"in_trash": True})

    @mcp.tool()
    def restore_page(page_id: str) -> dict:
        """Restore a trashed Notion page.

        Args:
            page_id: The ID of the page to restore.
        """
        return notion_request("PATCH", f"/pages/{page_id}", json={"in_trash": False})

    @mcp.tool()
    def move_page(page_id: str, parent: dict) -> dict:
        """Move a Notion page to a new parent location.

        Args:
            page_id: The ID of the page to move.
            parent: The new parent. E.g. {"type": "page_id", "page_id": "..."} or
                    {"type": "data_source_id", "data_source_id": "..."}.
        """
        return notion_request("POST", f"/pages/{page_id}/move", json={"parent": parent})

    @mcp.tool()
    def retrieve_page_property(
        page_id: str,
        property_id: str,
        start_cursor: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> dict:
        """Retrieve a specific property item from a Notion page.

        Args:
            page_id: The ID of the page.
            property_id: The ID of the property to retrieve.
            start_cursor: Cursor for pagination.
            page_size: Number of results per page (max 100).
        """
        params = {}
        if start_cursor:
            params["start_cursor"] = start_cursor
        if page_size is not None:
            params["page_size"] = page_size
        return notion_request("GET", f"/pages/{page_id}/properties/{property_id}", params=params)

    @mcp.tool()
    def retrieve_page_as_markdown(
        page_id: str,
        include_meeting_note_transcripts: Optional[bool] = None,
    ) -> dict:
        """Retrieve a Notion page's content rendered as Markdown.

        Args:
            page_id: The ID of the page (or block) to retrieve as markdown.
            include_meeting_note_transcripts: Whether to include meeting note transcripts. Defaults to false.
        """
        params = {}
        if include_meeting_note_transcripts is not None:
            params["include_meeting_note_transcripts"] = str(include_meeting_note_transcripts).lower()
        return notion_request("GET", f"/pages/{page_id}/markdown", params=params)

    @mcp.tool()
    def update_page_markdown(
        page_id: str,
        update_type: str,
        content: dict,
    ) -> dict:
        """Update a Notion page's content using Markdown.

        Args:
            page_id: The ID of the page to update.
            update_type: The type of update operation. One of: "insert_content",
                         "replace_content_range", "update_content", "replace_content".
            content: The content update payload matching the update_type.
                     For "update_content": {"content_updates": [{"old_str": "...", "new_str": "..."}]}
                     For "replace_content": {"markdown": "..."}
                     For "insert_content": {"markdown": "...", "position": "..."}
        """
        body = {"type": update_type, update_type: content}
        return notion_request("PATCH", f"/pages/{page_id}/markdown", json=body)
