import os
import requests
from typing import Any, Dict, List, Optional

def zulip_auth() -> Dict[str, str]:
    return {
        "email": os.environ["ZULIP_EMAIL"],
        "api_key": os.environ["ZULIP_API_KEY"],
        "site": os.environ["ZULIP_SITE"].rstrip("/"),
    }

def create_drafts(drafts: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Create one or more drafts on the server.
    drafts: list of dicts with keys: type, to, topic, content, timestamp (optional)
    """
    auth = zulip_auth()
    url = f"{auth['site']}/api/v1/drafts"
    import json
    data = {"drafts": json.dumps(drafts)}
    resp = requests.post(url, auth=(auth["email"], auth["api_key"]), data=data)
    try:
        return resp.json()
    except Exception:
        return {"error": f"Invalid response: {resp.text}"}

def get_drafts() -> Dict[str, Any]:
    """
    Fetch all drafts for the current user.
    """
    auth = zulip_auth()
    url = f"{auth['site']}/api/v1/drafts"
    resp = requests.get(url, auth=(auth["email"], auth["api_key"]))
    try:
        return resp.json()
    except Exception:
        return {"error": f"Invalid response: {resp.text}"}

def edit_draft(draft_id: int, draft: Dict[str, Any]) -> Dict[str, Any]:
    """
    Edit a draft by ID. draft: dict with keys: type, to, topic, content, timestamp (optional)
    """
    auth = zulip_auth()
    url = f"{auth['site']}/api/v1/drafts/{draft_id}"
    import json
    data = {"draft": json.dumps(draft)}
    resp = requests.patch(url, auth=(auth["email"], auth["api_key"]), data=data)
    try:
        return resp.json()
    except Exception:
        return {"error": f"Invalid response: {resp.text}"}

def delete_draft(draft_id: int) -> Dict[str, Any]:
    """
    Delete a draft by ID.
    """
    auth = zulip_auth()
    url = f"{auth['site']}/api/v1/drafts/{draft_id}"
    resp = requests.delete(url, auth=(auth["email"], auth["api_key"]))
    try:
        return resp.json()
    except Exception:
        return {"error": f"Invalid response: {resp.text}"}
