from __future__ import annotations

from zulip_client import ZulipClient


def register(mcp, client: ZulipClient):
    @mcp.tool()
    def zulip_get_drafts():
        """Fetch drafts."""
        return client.request("GET", "/drafts")

    @mcp.tool()
    def zulip_create_drafts(drafts: list[dict]):
        """Create drafts."""
        return client.request("POST", "/drafts", data={"drafts": drafts})

    @mcp.tool()
    def zulip_delete_draft(draft_id: int):
        """Delete a draft."""
        return client.request("DELETE", f"/drafts/{draft_id}")

    @mcp.tool()
    def zulip_edit_draft(draft_id: int, draft: dict):
        """Edit a draft."""
        return client.request("PATCH", f"/drafts/{draft_id}", data={"draft": draft})
