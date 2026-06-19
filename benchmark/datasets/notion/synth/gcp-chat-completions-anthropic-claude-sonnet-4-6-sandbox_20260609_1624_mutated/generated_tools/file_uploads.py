"""Notion File Uploads tools."""
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
        """Create a new file upload object in Notion.

        Use this to initiate a file upload. After creation, use send_file_upload to
        upload the actual file content, then complete_file_upload to finalize.

        Args:
            mode: How the file is being sent. One of: "single_part" (default, for files ≤20MB),
                  "multi_part" (for files >20MB), "external_url" (import from a public URL).
            filename: Name of the file including extension. Required for multi_part mode.
                      E.g. "document.pdf".
            content_type: MIME type of the file. E.g. "application/pdf", "image/png".
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
    def complete_file_upload(file_upload_id: str) -> dict:
        """Complete a multi-part file upload in Notion.

        Call this after all parts have been sent via send_file_upload.
        For single_part uploads, this is called automatically.

        Args:
            file_upload_id: The ID of the file upload to complete.
        """
        return notion_request("POST", f"/file_uploads/{file_upload_id}/complete")

    @mcp.tool()
    def retrieve_file_upload(file_upload_id: str) -> dict:
        """Retrieve the status and details of a Notion file upload.

        Args:
            file_upload_id: The ID of the file upload to retrieve.
        """
        return notion_request("GET", f"/file_uploads/{file_upload_id}")

    @mcp.tool()
    def list_file_uploads(
        status: Optional[str] = None,
        start_cursor: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> dict:
        """List file uploads in the Notion workspace.

        Args:
            status: Filter by status. One of: "pending", "uploaded", "expired", "failed".
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
