"""Notion File Uploads API tools."""
from typing import Optional, Any
from mcp.server.fastmcp import FastMCP
from .client import notion_request

def register(mcp: FastMCP):

    @mcp.tool()
    def create_file_upload(
        mode: Optional[str] = None,
        filename: Optional[str] = None,
        content_type: Optional[str] = None,
        number_of_parts: Optional[int] = None,
        external_url: Optional[str] = None,
    ) -> dict:
        """Create a new Notion file upload object.

        Args:
            mode: How the file is being sent: 'single_part' (default), 'multi_part',
                  or 'external_url'.
            filename: Name of the file including extension. Required for multi_part mode.
            content_type: MIME type of the file (e.g. 'application/pdf', 'image/png').
            number_of_parts: For multi_part mode, the total number of parts to upload.
            external_url: For external_url mode, the HTTPS URL of the publicly accessible file.
        """
        body: dict[str, Any] = {}
        if mode is not None:
            body["mode"] = mode
        if filename is not None:
            body["filename"] = filename
        if content_type is not None:
            body["content_type"] = content_type
        if number_of_parts is not None:
            body["number_of_parts"] = number_of_parts
        if external_url is not None:
            body["external_url"] = external_url
        return notion_request("POST", "/file_uploads", json=body)

    @mcp.tool()
    def retrieve_file_upload(file_upload_id: str) -> dict:
        """Retrieve the status and metadata of a Notion file upload.

        Args:
            file_upload_id: The ID of the file upload to retrieve.
        """
        return notion_request("GET", f"/file_uploads/{file_upload_id}")

    @mcp.tool()
    def complete_file_upload(file_upload_id: str) -> dict:
        """Mark a Notion multi-part file upload as complete.

        Args:
            file_upload_id: The ID of the file upload to complete.
        """
        return notion_request("POST", f"/file_uploads/{file_upload_id}/complete")

    @mcp.tool()
    def list_file_uploads(
        status: Optional[str] = None,
        start_cursor: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> dict:
        """List Notion file uploads, optionally filtered by status.

        Args:
            status: Filter by status: 'pending', 'uploaded', 'expired', or 'failed'.
            start_cursor: Cursor for pagination.
            page_size: Number of results per page (max 100).
        """
        params: dict[str, Any] = {}
        if status:
            params["status"] = status
        if start_cursor:
            params["start_cursor"] = start_cursor
        if page_size is not None:
            params["page_size"] = page_size
        return notion_request("GET", "/file_uploads", params=params)
