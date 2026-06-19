import os
import requests

BASE_URL = os.environ.get("ZULIP_SITE", "") + "/api/v1"
AUTH = (os.environ.get("ZULIP_EMAIL"), os.environ.get("ZULIP_API_KEY"))


def create_scheduled_message(type: str, to, content: str, scheduled_delivery_timestamp: int, topic: str = None, read_by_sender: bool = None):
    """Create a new scheduled message."""
    url = f"{BASE_URL}/scheduled_messages"
    data = {
        "type": type,
        "to": to,
        "content": content,
        "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
    }
    if topic is not None:
        data["topic"] = topic
    if read_by_sender is not None:
        data["read_by_sender"] = str(read_by_sender).lower()

    try:
        response = requests.post(url, auth=AUTH, data=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        try:
            return response.json()
        except Exception:
            return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}


def list_tools():
    return ["create_scheduled_message"]
