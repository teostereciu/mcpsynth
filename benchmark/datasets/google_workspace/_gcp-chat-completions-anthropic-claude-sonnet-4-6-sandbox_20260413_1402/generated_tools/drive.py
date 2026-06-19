"""Google Drive API tools for the Google Workspace MCP Server."""

from typing import Any, Optional

import requests

from generated_tools import mcp
from generated_tools.auth import (
    DRIVE_BASE,
    api_delete,
    api_get,
    api_patch,
    api_post,
    handle_http_error,
    _auth_headers,
)


# ---------------------------------------------------------------------------
# Files
# ---------------------------------------------------------------------------


@mcp.tool()
def drive_create_file(
    name: str,
    mime_type: Optional[str] = None,
    parent_ids: Optional[list] = None,
    description: Optional[str] = None,
    starred: bool = False,
) -> dict:
    """Create a new file or folder in Google Drive (metadata only, no content upload).

    To create a folder, use mime_type='application/vnd.google-apps.folder'.
    To create a Google Doc, use mime_type='application/vnd.google-apps.document'.
    To create a Google Sheet, use mime_type='application/vnd.google-apps.spreadsheet'.

    Args:
        name: The name of the file or folder.
        mime_type: MIME type of the file (e.g. 'application/vnd.google-apps.folder').
        parent_ids: List of parent folder IDs.
        description: A short description of the file.
        starred: Whether the user has starred the file.
    """
    try:
        payload: dict[str, Any] = {"name": name}
        if mime_type:
            payload["mimeType"] = mime_type
        if parent_ids:
            payload["parents"] = parent_ids
        if description:
            payload["description"] = description
        if starred:
            payload["starred"] = starred
        return api_post(f"{DRIVE_BASE}/files", payload=payload)
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def drive_get_file(
    file_id: str,
    fields: Optional[str] = None,
    supports_all_drives: bool = False,
) -> dict:
    """Get a file's metadata from Google Drive.

    Args:
        file_id: The ID of the file.
        fields: Comma-separated list of fields to include in the response
                (e.g. 'id,name,mimeType,size,createdTime,modifiedTime,parents').
        supports_all_drives: Whether to support shared drives.
    """
    try:
        params: dict[str, Any] = {"supportsAllDrives": supports_all_drives}
        if fields:
            params["fields"] = fields
        return api_get(f"{DRIVE_BASE}/files/{file_id}", params=params)
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def drive_list_files(
    page_size: int = 10,
    q: Optional[str] = None,
    order_by: Optional[str] = None,
    fields: Optional[str] = None,
    spaces: str = "drive",
    page_token: Optional[str] = None,
    drive_id: Optional[str] = None,
    include_items_from_all_drives: bool = False,
) -> dict:
    """List files in Google Drive.

    Args:
        page_size: Maximum number of files to return per page (default 10).
        q: Query string for filtering files (e.g. "mimeType='application/vnd.google-apps.folder'").
        order_by: Sort order (e.g. 'name', 'modifiedTime desc', 'createdTime').
        fields: Fields to include in the response (e.g. 'files(id,name,mimeType)').
        spaces: Spaces to query: 'drive' or 'appDataFolder'.
        page_token: Page token for pagination.
        drive_id: ID of a shared drive to search.
        include_items_from_all_drives: Include items from shared drives.
    """
    try:
        params: dict[str, Any] = {
            "pageSize": page_size,
            "spaces": spaces,
            "includeItemsFromAllDrives": include_items_from_all_drives,
        }
        if q:
            params["q"] = q
        if order_by:
            params["orderBy"] = order_by
        if fields:
            params["fields"] = fields
        if page_token:
            params["pageToken"] = page_token
        if drive_id:
            params["driveId"] = drive_id
        return api_get(f"{DRIVE_BASE}/files", params=params)
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def drive_update_file(
    file_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    add_parents: Optional[str] = None,
    remove_parents: Optional[str] = None,
    starred: Optional[bool] = None,
    trashed: Optional[bool] = None,
) -> dict:
    """Update a file's metadata in Google Drive (patch semantics).

    Args:
        file_id: The ID of the file to update.
        name: New name for the file.
        description: New description for the file.
        add_parents: Comma-separated list of parent IDs to add.
        remove_parents: Comma-separated list of parent IDs to remove.
        starred: Whether the user has starred the file.
        trashed: Whether the file is in the trash.
    """
    try:
        payload: dict[str, Any] = {}
        if name is not None:
            payload["name"] = name
        if description is not None:
            payload["description"] = description
        if starred is not None:
            payload["starred"] = starred
        if trashed is not None:
            payload["trashed"] = trashed

        params: dict[str, Any] = {}
        if add_parents:
            params["addParents"] = add_parents
        if remove_parents:
            params["removeParents"] = remove_parents

        return api_patch(f"{DRIVE_BASE}/files/{file_id}", payload=payload, params=params)
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def drive_delete_file(file_id: str) -> dict:
    """Permanently delete a file from Google Drive.

    Args:
        file_id: The ID of the file to delete.
    """
    try:
        return api_delete(f"{DRIVE_BASE}/files/{file_id}")
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def drive_copy_file(
    file_id: str,
    name: Optional[str] = None,
    parent_ids: Optional[list] = None,
) -> dict:
    """Create a copy of a file in Google Drive.

    Args:
        file_id: The ID of the file to copy.
        name: Name for the copy (defaults to 'Copy of <original name>').
        parent_ids: List of parent folder IDs for the copy.
    """
    try:
        payload: dict[str, Any] = {}
        if name:
            payload["name"] = name
        if parent_ids:
            payload["parents"] = parent_ids
        return api_post(f"{DRIVE_BASE}/files/{file_id}/copy", payload=payload)
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def drive_export_file(file_id: str, mime_type: str) -> dict:
    """Export a Google Workspace document to a specified MIME type.

    Common export MIME types:
    - Google Docs → 'application/pdf', 'text/plain', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    - Google Sheets → 'application/pdf', 'text/csv', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    - Google Slides → 'application/pdf', 'application/vnd.openxmlformats-officedocument.presentationml.presentation'

    Args:
        file_id: The ID of the Google Workspace file to export.
        mime_type: The MIME type to export to.
    """
    try:
        resp = requests.get(
            f"{DRIVE_BASE}/files/{file_id}/export",
            headers=_auth_headers(),
            params={"mimeType": mime_type},
        )
        resp.raise_for_status()
        return {
            "content_type": resp.headers.get("Content-Type", mime_type),
            "size_bytes": len(resp.content),
            "content_base64": __import__("base64").b64encode(resp.content).decode(),
        }
    except requests.HTTPError as e:
        return handle_http_error(e)


# ---------------------------------------------------------------------------
# Permissions
# ---------------------------------------------------------------------------


@mcp.tool()
def drive_list_permissions(
    file_id: str,
    page_size: Optional[int] = None,
    page_token: Optional[str] = None,
) -> dict:
    """List permissions for a file or shared drive.

    Args:
        file_id: The ID of the file or shared drive.
        page_size: Maximum number of permissions to return per page.
        page_token: Page token for pagination.
    """
    try:
        params: dict[str, Any] = {}
        if page_size:
            params["pageSize"] = page_size
        if page_token:
            params["pageToken"] = page_token
        return api_get(f"{DRIVE_BASE}/files/{file_id}/permissions", params=params)
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def drive_create_permission(
    file_id: str,
    role: str,
    type: str,
    email_address: Optional[str] = None,
    domain: Optional[str] = None,
    send_notification_email: bool = False,
    email_message: Optional[str] = None,
) -> dict:
    """Create a permission for a file or shared drive.

    Args:
        file_id: The ID of the file or shared drive.
        role: Access role: 'owner', 'organizer', 'fileOrganizer', 'writer', 'commenter', or 'reader'.
        type: Permission type: 'user', 'group', 'domain', or 'anyone'.
        email_address: Email address for 'user' or 'group' type permissions.
        domain: Domain name for 'domain' type permissions.
        send_notification_email: Whether to send a notification email.
        email_message: Custom message to include in the notification email.
    """
    try:
        payload: dict[str, Any] = {"role": role, "type": type}
        if email_address:
            payload["emailAddress"] = email_address
        if domain:
            payload["domain"] = domain

        params: dict[str, Any] = {
            "sendNotificationEmail": send_notification_email,
        }
        if email_message:
            params["emailMessage"] = email_message

        return api_post(
            f"{DRIVE_BASE}/files/{file_id}/permissions",
            payload=payload,
            params=params,
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def drive_delete_permission(file_id: str, permission_id: str) -> dict:
    """Delete a permission from a file or shared drive.

    Args:
        file_id: The ID of the file or shared drive.
        permission_id: The ID of the permission to delete.
    """
    try:
        return api_delete(f"{DRIVE_BASE}/files/{file_id}/permissions/{permission_id}")
    except requests.HTTPError as e:
        return handle_http_error(e)


# ---------------------------------------------------------------------------
# Shared Drives
# ---------------------------------------------------------------------------


@mcp.tool()
def drive_list_drives(
    page_size: int = 10,
    q: Optional[str] = None,
    page_token: Optional[str] = None,
) -> dict:
    """List the user's shared drives.

    Args:
        page_size: Maximum number of shared drives to return per page.
        q: Query string for searching shared drives.
        page_token: Page token for pagination.
    """
    try:
        params: dict[str, Any] = {"pageSize": page_size}
        if q:
            params["q"] = q
        if page_token:
            params["pageToken"] = page_token
        return api_get(f"{DRIVE_BASE}/drives", params=params)
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def drive_get_drive(drive_id: str) -> dict:
    """Get metadata for a shared drive.

    Args:
        drive_id: The ID of the shared drive.
    """
    try:
        return api_get(f"{DRIVE_BASE}/drives/{drive_id}")
    except requests.HTTPError as e:
        return handle_http_error(e)


# ---------------------------------------------------------------------------
# Comments and Replies
# ---------------------------------------------------------------------------


@mcp.tool()
def drive_list_comments(
    file_id: str,
    page_size: int = 20,
    include_deleted: bool = False,
    page_token: Optional[str] = None,
) -> dict:
    """List comments on a Google Drive file.

    Args:
        file_id: The ID of the file.
        page_size: Maximum number of comments to return per page.
        include_deleted: Whether to include deleted comments.
        page_token: Page token for pagination.
    """
    try:
        params: dict[str, Any] = {
            "pageSize": page_size,
            "includeDeleted": include_deleted,
            "fields": "comments(id,content,author,createdTime,resolved),nextPageToken",
        }
        if page_token:
            params["pageToken"] = page_token
        return api_get(f"{DRIVE_BASE}/files/{file_id}/comments", params=params)
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def drive_list_replies(
    file_id: str,
    comment_id: str,
    page_size: int = 20,
    include_deleted: bool = False,
) -> dict:
    """List replies to a comment on a Google Drive file.

    Args:
        file_id: The ID of the file.
        comment_id: The ID of the comment.
        page_size: Maximum number of replies to return per page.
        include_deleted: Whether to include deleted replies.
    """
    try:
        params: dict[str, Any] = {
            "pageSize": page_size,
            "includeDeleted": include_deleted,
            "fields": "replies(id,content,author,createdTime),nextPageToken",
        }
        return api_get(
            f"{DRIVE_BASE}/files/{file_id}/comments/{comment_id}/replies",
            params=params,
        )
    except requests.HTTPError as e:
        return handle_http_error(e)
