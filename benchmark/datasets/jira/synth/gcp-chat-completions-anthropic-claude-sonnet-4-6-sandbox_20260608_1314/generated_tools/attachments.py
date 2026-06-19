"""Issue attachment tools: get metadata, add, delete attachments."""
from mcp.server.fastmcp import FastMCP
from typing import Optional
import requests, os

def _client():
    base = os.environ["JIRA_BASE_URL"].rstrip("/")
    session = requests.Session()
    session.auth = (os.environ["JIRA_EMAIL"], os.environ["JIRA_API_TOKEN"])
    session.headers.update({"Accept": "application/json"})
    return session, f"{base}/rest/api/3"

def register(mcp: FastMCP):

    @mcp.tool()
    def get_attachment_metadata(attachment_id: str) -> dict:
        """Get metadata for a Jira issue attachment by ID (filename, size, mime type, author, etc.)."""
        session, base = _client()
        r = session.get(f"{base}/attachment/{attachment_id}")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def delete_attachment(attachment_id: str) -> dict:
        """Delete an attachment from a Jira issue by attachment ID."""
        session, base = _client()
        r = session.delete(f"{base}/attachment/{attachment_id}")
        if r.status_code == 204:
            return {"success": True}
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def get_attachment_settings() -> dict:
        """Get Jira attachment settings: whether attachments are enabled and the max upload size."""
        session, base = _client()
        r = session.get(f"{base}/attachment/meta")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}

    @mcp.tool()
    def add_attachment(issue_id_or_key: str, file_path: str) -> dict:
        """Add a file attachment to a Jira issue. file_path must be a local path to the file to upload."""
        session, base = _client()
        try:
            with open(file_path, "rb") as f:
                files = {"file": (os.path.basename(file_path), f)}
                headers = {"X-Atlassian-Token": "no-check"}
                r = session.post(
                    f"{base}/issue/{issue_id_or_key}/attachments",
                    files=files,
                    headers=headers
                )
            if r.ok:
                return r.json()
            return {"error": r.text, "status_code": r.status_code}
        except FileNotFoundError:
            return {"error": f"File not found: {file_path}"}

    @mcp.tool()
    def get_attachment_archive_metadata(attachment_id: str) -> dict:
        """Get metadata for the contents of an archive attachment (e.g. ZIP file)."""
        session, base = _client()
        r = session.get(f"{base}/attachment/{attachment_id}/expand/human")
        if r.ok:
            return r.json()
        return {"error": r.text, "status_code": r.status_code}
