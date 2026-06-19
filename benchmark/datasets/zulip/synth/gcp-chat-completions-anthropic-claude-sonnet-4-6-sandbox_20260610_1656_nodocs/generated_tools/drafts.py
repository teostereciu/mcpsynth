"""
Zulip MCP Tools — Drafts domain
Covers: list, create, edit, delete drafts
"""
import os, requests
from mcp.server.fastmcp import FastMCP


def _client():
    email   = os.environ["ZULIP_EMAIL"]
    api_key = os.environ["ZULIP_API_KEY"]
    site    = os.environ["ZULIP_SITE"].rstrip("/")
    base    = f"{site}/api/v1"
    return base, (email, api_key)


def register_draft_tools(mcp: FastMCP):

    @mcp.tool()
    def get_drafts() -> dict:
        """List all message drafts saved by the current user."""
        base, auth = _client()
        try:
            r = requests.get(f"{base}/drafts", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def create_drafts(drafts: str) -> dict:
        """Create one or more message drafts.

        Args:
            drafts: JSON list of draft objects. Each object must have:
                - 'type': 'stream' or 'direct'
                - 'to': list of stream IDs (stream) or user IDs (direct)
                - 'topic': topic name (stream only)
                - 'content': draft message content
                - 'timestamp': (optional) Unix timestamp
            Example: '[{"type":"stream","to":[1],"topic":"hello","content":"Draft text"}]'
        """
        base, auth = _client()
        try:
            r = requests.post(
                f"{base}/drafts", data={"drafts": drafts}, auth=auth
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def update_draft(
        draft_id: int,
        type: str,
        to: str,
        topic: str,
        content: str,
        timestamp: int = 0,
    ) -> dict:
        """Update an existing draft.

        Args:
            draft_id: The numeric ID of the draft to update.
            type: 'stream' or 'direct'.
            to: JSON list of stream IDs (stream) or user IDs (direct).
            topic: Topic name (stream messages only).
            content: New draft content.
            timestamp: Optional Unix timestamp for the draft.
        """
        base, auth = _client()
        draft: dict = {
            "type": type,
            "to": to,
            "topic": topic,
            "content": content,
        }
        if timestamp:
            draft["timestamp"] = timestamp
        import json
        try:
            r = requests.patch(
                f"{base}/drafts/{draft_id}",
                data={"draft": json.dumps(draft)},
                auth=auth,
            )
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def delete_draft(draft_id: int) -> dict:
        """Delete a draft.

        Args:
            draft_id: The numeric ID of the draft to delete.
        """
        base, auth = _client()
        try:
            r = requests.delete(f"{base}/drafts/{draft_id}", auth=auth)
            return r.json()
        except Exception as e:
            return {"error": str(e)}
