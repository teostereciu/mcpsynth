from typing import Any, Dict, Optional

from .slack_client import SlackWebAPIClient, _clean_dict


def pins_add(
    channel: str,
    timestamp: str,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    payload = _clean_dict({"channel": channel, "timestamp": timestamp})
    return client.post("pins.add", payload)


def pins_list(
    channel: str,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    params = _clean_dict({"channel": channel})
    return client.get("pins.list", params)


def pins_remove(
    channel: str,
    timestamp: str,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    payload = _clean_dict({"channel": channel, "timestamp": timestamp})
    return client.post("pins.remove", payload)
