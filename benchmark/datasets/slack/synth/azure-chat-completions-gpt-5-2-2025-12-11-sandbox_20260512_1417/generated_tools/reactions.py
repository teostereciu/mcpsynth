from typing import Any, Dict, Optional

from .slack_client import get_client


def reactions_add(channel: str, name: str, timestamp: str) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"channel": channel, "name": name, "timestamp": timestamp}
    return get_client().request("POST", "/reactions.add", json=payload)


def reactions_remove(
    name: str,
    channel: Optional[str] = None,
    timestamp: Optional[str] = None,
    file: Optional[str] = None,
    file_comment: Optional[str] = None,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"name": name}
    if channel is not None:
        payload["channel"] = channel
    if timestamp is not None:
        payload["timestamp"] = timestamp
    if file is not None:
        payload["file"] = file
    if file_comment is not None:
        payload["file_comment"] = file_comment
    return get_client().request("POST", "/reactions.remove", json=payload)
