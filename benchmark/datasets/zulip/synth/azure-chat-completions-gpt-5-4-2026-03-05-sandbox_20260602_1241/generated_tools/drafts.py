from typing import Any, Dict, List

from generated_tools.common import client


def get_drafts() -> Dict[str, Any]:
    return client.request("GET", "/drafts")


def create_drafts(drafts: List[Dict[str, Any]]) -> Dict[str, Any]:
    return client.request("POST", "/drafts", data={"drafts": drafts})


def edit_draft(draft_id: int, draft: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("PATCH", f"/drafts/{draft_id}", data={"draft": draft})


def delete_draft(draft_id: int) -> Dict[str, Any]:
    return client.request("DELETE", f"/drafts/{draft_id}")
