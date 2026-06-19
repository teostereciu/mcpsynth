from typing import Any, Dict, List

from .client import ZulipClient, _maybe_json_dumps


def get_drafts(client: ZulipClient) -> Dict[str, Any]:
    return client.request("GET", "/drafts")


def create_drafts(client: ZulipClient, drafts: List[Dict[str, Any]]) -> Dict[str, Any]:
    params: Dict[str, Any] = {"drafts": _maybe_json_dumps(drafts)}
    return client.request("POST", "/drafts", params)


def edit_draft(client: ZulipClient, draft_id: int, draft: Dict[str, Any]) -> Dict[str, Any]:
    params: Dict[str, Any] = {"draft": _maybe_json_dumps(draft)}
    return client.request("PATCH", f"/drafts/{draft_id}", params)


def delete_draft(client: ZulipClient, draft_id: int) -> Dict[str, Any]:
    return client.request("DELETE", f"/drafts/{draft_id}")
