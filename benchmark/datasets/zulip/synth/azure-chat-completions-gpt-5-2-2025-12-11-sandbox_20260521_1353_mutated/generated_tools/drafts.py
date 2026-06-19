from typing import Any, Dict, List, Optional

from .http_client import ZulipClient, dumps_if_needed


def get_drafts() -> Dict[str, Any]:
    """GET /drafts

    Doc: docs/api_get-drafts.md
    """
    client = ZulipClient()
    return client.request("GET", "/drafts")


def create_drafts(*, drafts: List[Dict[str, Any]]) -> Dict[str, Any]:
    """POST /drafts

    Doc: docs/api_create-drafts.md
    """
    client = ZulipClient()
    return client.request("POST", "/drafts", data={"drafts": dumps_if_needed(drafts)})


def edit_draft(*, draft_id: int, draft: Dict[str, Any]) -> Dict[str, Any]:
    """PATCH /drafts/{draft_id}

    Doc: docs/api_edit-draft.md
    """
    client = ZulipClient()
    return client.request("PATCH", f"/drafts/{draft_id}", data={"draft": dumps_if_needed(draft)})


def delete_draft(*, draft_id: int) -> Dict[str, Any]:
    """DELETE /drafts/{draft_id}

    Doc: docs/api_delete-draft.md
    """
    client = ZulipClient()
    return client.request("DELETE", f"/drafts/{draft_id}")
