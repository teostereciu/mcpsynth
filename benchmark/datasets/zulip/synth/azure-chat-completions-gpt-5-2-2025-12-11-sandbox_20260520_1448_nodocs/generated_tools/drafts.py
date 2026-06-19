from __future__ import annotations

from typing import Any

from zulip_client import ZulipClient


def get_drafts(client: ZulipClient) -> dict:
    return client.request("GET", "/drafts")


def create_drafts(client: ZulipClient, *, drafts: list[dict[str, Any]]) -> dict:
    return client.request("POST", "/drafts", data={"drafts": drafts})


def delete_draft(client: ZulipClient, *, draft_id: int) -> dict:
    return client.request("DELETE", f"/drafts/{draft_id}")
