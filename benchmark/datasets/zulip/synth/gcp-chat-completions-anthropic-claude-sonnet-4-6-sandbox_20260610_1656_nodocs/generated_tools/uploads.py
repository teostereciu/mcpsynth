"""
Zulip MCP Tools — File Uploads domain
Covers: upload file, get upload URL
"""
import os, requests
from mcp.server.fastmcp import FastMCP


def _client():
    email   = os.environ["ZULIP_EMAIL"]
    api_key = os.environ["ZULIP_API_KEY"]
    site    = os.environ["ZULIP_SITE"].rstrip("/")
    base    = f"{site}/api/v1"
    return base, (email, api_key)


def register_upload_tools(mcp: FastMCP):

    @mcp.tool()
    def upload_file(file_path: str) -> dict:
        """Upload a file to Zulip and get a URI to embed in messages.

        Args:
            file_path: Absolute or relative path to the file to upload.
        """
        base, auth = _client()
        try:
            with open(file_path, "rb") as fh:
                filename = os.path.basename(file_path)
                r = requests.post(
                    f"{base}/user_uploads",
                    files={"filename": (filename, fh)},
                    auth=auth,
                )
            return r.json()
        except FileNotFoundError:
            return {"error": f"File not found: {file_path}"}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_file_temporary_url(realm_id_str: str, filename: str) -> dict:
        """Get a temporary URL for a previously uploaded file.

        Args:
            realm_id_str: The realm-scoped path component returned when the file was uploaded
                          (the part after '/user_uploads/').
            filename: The filename of the uploaded file.
        """
        base, auth = _client()
        try:
            r = requests.get(
                f"{base}/user_uploads/{realm_id_str}/{filename}",
                auth=auth,
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}
