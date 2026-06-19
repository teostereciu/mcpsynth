from typing import Any, Dict

from .slack_client import get_client


def pins_add(channel: str, timestamp: str) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"channel": channel, "timestamp": timestamp}
    return get_client().request("POST", "/pins.add", json=payload)


def pins_remove(channel: str, timestamp: str) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"channel": channel, "timestamp": timestamp}
    return get_client().request("POST", "/pins.remove", json=payload)
