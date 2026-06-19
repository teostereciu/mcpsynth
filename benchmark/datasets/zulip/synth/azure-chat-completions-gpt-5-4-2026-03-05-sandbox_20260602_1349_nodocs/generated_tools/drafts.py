from typing import Any, Dict, List, Optional

from generated_tools.common import client, json_dumps


def get_drafts() -> Dict[str, Any]:
    return client.request("GET", "/drafts")


def create_draft(type: str, to: List[str], content: str, topic: Optional[str] = None) -> Dict[str, Any]:
    draft: Dict[str, Any] = {"type": type, "to": json_dumps(to), "content": content}
    if topic is not None:
        draft["topic"] = topic
    return client.request("POST", "/drafts", params={"drafts": json_dumps([draft])})


def edit_draft(draft_id: int, type: str, to: List[str], content: str, topic: Optional[str] = None) -> Dict[str, Any]:
    draft: Dict[str, Any] = {"type": type, "to": json_dumps(to), "content": content}
    if topic is not None:
        draft["topic"] = topic
    return client.request("PATCH", f"/drafts/{draft_id}", params=draft)


def delete_draft(draft_id: int) -> Dict[str, Any]:
    return client.request("DELETE", f"/drafts/{draft_id}")
