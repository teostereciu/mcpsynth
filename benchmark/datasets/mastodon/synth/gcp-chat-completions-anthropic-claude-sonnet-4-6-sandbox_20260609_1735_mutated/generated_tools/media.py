"""Mastodon media API tools."""
import os
import requests
from typing import Optional
from mcp.server.fastmcp import FastMCP

BASE_URL = os.environ.get("MASTODON_BASE_URL", "").rstrip("/")
ACCESS_TOKEN = os.environ.get("MASTODON_ACCESS_TOKEN", "")


def _headers():
    return {"Authorization": f"Bearer {ACCESS_TOKEN}"}


def _api(path: str) -> str:
    return f"{BASE_URL}{path}"


def register(mcp: FastMCP):

    @mcp.tool()
    def upload_media(
        file_path: str,
        description: Optional[str] = None,
        focus: Optional[str] = None,
    ) -> dict:
        """Upload a media file as an attachment for use in a status.

        Args:
            file_path: Local filesystem path to the file to upload.
            description: Plain-text description for accessibility (alt text).
            focus: Focal point as 'x,y' floats in range -1.0 to 1.0 (e.g. '0.5,-0.3').
        """
        try:
            with open(file_path, "rb") as f:
                files = {"file": f}
                data = {}
                if description:
                    data["description"] = description
                if focus:
                    data["focus"] = focus
                resp = requests.post(
                    _api("/api/v2/media"),
                    headers=_headers(),
                    files=files,
                    data=data,
                )
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_media_attachment(media_id: str) -> dict:
        """Get a media attachment by ID (check processing status).

        Args:
            media_id: The ID of the media attachment.
        """
        try:
            resp = requests.get(_api(f"/api/v1/media/{media_id}"), headers=_headers())
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def update_media_attachment(
        media_id: str,
        description: Optional[str] = None,
        focus: Optional[str] = None,
    ) -> dict:
        """Update a media attachment's description or focal point before posting.

        Args:
            media_id: The ID of the media attachment.
            description: New plain-text description for accessibility.
            focus: New focal point as 'x,y' floats in range -1.0 to 1.0.
        """
        try:
            data = {}
            if description is not None:
                data["description"] = description
            if focus is not None:
                data["focus"] = focus
            resp = requests.put(_api(f"/api/v1/media/{media_id}"), headers=_headers(), data=data)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def delete_media_attachment(media_id: str) -> dict:
        """Delete a media attachment that has not yet been attached to a status.

        Args:
            media_id: The ID of the media attachment to delete.
        """
        try:
            resp = requests.delete(_api(f"/api/v1/media/{media_id}"), headers=_headers())
            if resp.status_code == 200:
                try:
                    return resp.json()
                except Exception:
                    return {"status": "deleted"}
            return {"status": resp.status_code, "text": resp.text}
        except Exception as e:
            return {"error": str(e)}
