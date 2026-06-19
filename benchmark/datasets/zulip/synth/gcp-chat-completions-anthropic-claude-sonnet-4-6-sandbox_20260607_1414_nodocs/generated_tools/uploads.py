"""
Zulip MCP Tools — File Uploads domain
Covers: upload files, get upload URL
"""

import os
from .client import zulip_post_file, zulip_get


def upload_file(file_path: str) -> dict:
    """Upload a file to Zulip and get a URI to embed in messages.

    Args:
        file_path: The absolute or relative path to the file to upload.
                   The file will be uploaded and a Zulip URI returned that
                   can be embedded in message content using Markdown syntax:
                   [filename](uri)
    """
    if not os.path.isfile(file_path):
        return {"result": "error", "msg": f"File not found: {file_path}"}
    filename = os.path.basename(file_path)
    try:
        with open(file_path, "rb") as f:
            files = {"filename": (filename, f)}
            return zulip_post_file("/user_uploads", files)
    except Exception as exc:
        return {"result": "error", "msg": str(exc)}


def get_uploaded_file_url(realm_id_str: str, filename: str) -> dict:
    """Retrieve metadata about an uploaded file.

    Args:
        realm_id_str: The realm-scoped path component for the file
                      (as returned in the URI from upload_file).
        filename: The filename of the uploaded file.
    """
    return zulip_get(f"/user_uploads/{realm_id_str}/{filename}")
