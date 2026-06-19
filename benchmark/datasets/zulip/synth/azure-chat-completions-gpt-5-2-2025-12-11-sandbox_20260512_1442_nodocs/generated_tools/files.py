from __future__ import annotations

from zulip_client import ZulipClient


def register(mcp, client: ZulipClient):
    @mcp.tool()
    def zulip_upload_file(file_path: str, filename: str | None = None):
        """Upload a file from local path."""
        try:
            with open(file_path, "rb") as f:
                files = {"file": (filename or file_path.split("/")[-1], f)}
                return client.request("POST", "/user_uploads", files=files)
        except Exception as e:
            return {"error": str(e)}
