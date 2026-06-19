import os
import requests

BASE_URL = os.environ.get("ZULIP_SITE", "") + "/api/v1"
AUTH = (os.environ.get("ZULIP_EMAIL"), os.environ.get("ZULIP_API_KEY"))


def add_reaction(message_id: int, emoji_name: str, emoji_code: str = None, reaction_type: str = None):
    """Add an emoji reaction to a message."""
    url = f"{BASE_URL}/messages/{message_id}/reactions"
    data = {
        "emoji_name": emoji_name,
    }
    if emoji_code is not None:
        data["emoji_code"] = emoji_code
    if reaction_type is not None:
        data["reaction_type"] = reaction_type

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
    return ["add_reaction"]
