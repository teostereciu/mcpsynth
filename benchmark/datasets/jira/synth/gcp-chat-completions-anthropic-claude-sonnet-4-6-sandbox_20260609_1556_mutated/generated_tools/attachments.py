"""Issue attachment tools."""
from mcp.server.fastmcp import FastMCP
from typing import Optional
import requests, os

def _client():
    base = os.environ["JIRA_BASE_URL"].rstrip("/")
    s = requests.Session()
    s.auth = (os.environ["JIRA_EMAIL"], os.environ["JIRA_API_TOKEN"])
    s.headers.update({"Accept": "application/json"})
    return s, f"{base}/rest/api/3"

def register(mcp: FastMCP):

    @mcp.tool()
    def get_attachment_metadata(attachment_id: str) -> dict:
        """Get metadata for an attachment (filename, size, mime type, author)."""
        s, base = _client()
        try:
            r = s.get(f"{base}/attachment/{attachment_id}")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def delete_attachment(attachment_id: str) -> dict:
        """Delete an attachment from an issue."""
        s, base = _client()
        try:
            r = s.delete(f"{base}/attachment/{attachment_id}")
            if r.status_code == 204:
                return {"success": True}
            r.raise_for_status()
            return {"success": True}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_attachment_settings() -> dict:
        """Get Jira attachment settings (enabled status, max upload size)."""
        s, base = _client()
        try:
            r = s.get(f"{base}/attachment/meta")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def add_attachment(issue_id_or_key: str, file_path: str) -> dict:
        """Upload a file as an attachment to an issue. file_path is the local path to the file."""
        base_url = os.environ["JIRA_BASE_URL"].rstrip("/")
        email = os.environ["JIRA_EMAIL"]
        token = os.environ["JIRA_API_TOKEN"]
        url = f"{base_url}/rest/api/3/issue/{issue_id_or_key}/attachments"
        try:
            with open(file_path, "rb") as f:
                r = requests.post(
                    url,
                    auth=(email, token),
                    headers={"X-Atlassian-Token": "no-check", "Accept": "application/json"},
                    files={"file": f},
                )
            r.raise_for_status()
            return r.json()
        except FileNotFoundError:
            return {"error": f"File not found: {file_path}"}
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}

    @mcp.tool()
    def get_attachment_archive_metadata(attachment_id: str) -> dict:
        """Get metadata for the contents of an archive attachment (e.g. ZIP)."""
        s, base = _client()
        try:
            r = s.get(f"{base}/attachment/{attachment_id}/expand/human")
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "detail": e.response.text}
