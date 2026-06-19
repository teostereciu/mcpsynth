from typing import Any, Dict, Optional

from generated_tools.confluence_client import client


def list_footer_comments(page_id: str, expand: Optional[str] = None) -> Dict[str, Any]:
    params = {}
    if expand:
        params["expand"] = expand
    return client.request("GET", f"/rest/api/content/{page_id}/child/comment", params=params or None)


def create_footer_comment(page_id: str, body_value: str) -> Dict[str, Any]:
    payload = {
        "type": "comment",
        "container": {"id": page_id, "type": "page"},
        "body": {"storage": {"value": body_value, "representation": "storage"}},
    }
    return client.request("POST", "/rest/api/content", json_body=payload)


def create_inline_comment(page_id: str, body_value: str, text_selection: Optional[str] = None) -> Dict[str, Any]:
    payload = {
        "type": "comment",
        "container": {"id": page_id, "type": "page"},
        "body": {"storage": {"value": body_value, "representation": "storage"}},
        "extensions": {"location": "inline"},
    }
    if text_selection:
        payload["extensions"]["inlineProperties"] = {"textSelection": text_selection}
    return client.request("POST", "/rest/api/content", json_body=payload)
