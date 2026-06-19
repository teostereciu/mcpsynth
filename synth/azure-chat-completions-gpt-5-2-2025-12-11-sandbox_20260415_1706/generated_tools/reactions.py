from typing import Any, Dict, Optional

from .slack_client import SlackWebAPIClient, _clean_dict


def reactions_add(
    channel: str,
    name: str,
    timestamp: str,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    payload = _clean_dict({"channel": channel, "name": name, "timestamp": timestamp})
    return client.post("reactions.add", payload)


def reactions_remove(
    name: str,
    channel: Optional[str] = None,
    timestamp: Optional[str] = None,
    file: Optional[str] = None,
    file_comment: Optional[str] = None,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    payload = _clean_dict(
        {
            "name": name,
            "channel": channel,
            "timestamp": timestamp,
            "file": file,
            "file_comment": file_comment,
        }
    )
    return client.post("reactions.remove", payload)
