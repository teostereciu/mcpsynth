import os
import requests
import json

BASE_URL = os.environ.get("ZULIP_SITE", "") + "/api/v1"
AUTH = (os.environ.get("ZULIP_EMAIL"), os.environ.get("ZULIP_API_KEY"))


def subscribe_to_streams(subscriptions, principals=None, authorization_errors_fatal=True, announce=False, invite_only=False, is_web_public=False, is_default_stream=False, history_public_to_subscribers=False, message_retention_days=None, topics_policy=None):
    """Subscribe one or more users to one or more streams (channels). Creates streams if they don't exist."""
    url = f"{BASE_URL}/users/me/subscriptions"
    data = {
        "subscriptions": json.dumps(subscriptions),
        "authorization_errors_fatal": str(authorization_errors_fatal).lower(),
        "announce": str(announce).lower(),
        "invite_only": str(invite_only).lower(),
        "is_web_public": str(is_web_public).lower(),
        "is_default_stream": str(is_default_stream).lower(),
        "history_public_to_subscribers": str(history_public_to_subscribers).lower(),
    }
    if principals is not None:
        data["principals"] = json.dumps(principals)
    if message_retention_days is not None:
        data["message_retention_days"] = str(message_retention_days)
    if topics_policy is not None:
        data["topics_policy"] = topics_policy

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
    return ["subscribe_to_streams", "get_streams"]

def get_streams(include_public=True, include_web_public=False, include_subscribed=True, exclude_archived=True, include_all=False, include_default=False, include_owner_subscribed=False, include_can_access_content=False):
    """Get all streams (channels) the user has access to."""
    url = f"{BASE_URL}/streams"
    params = {
        "include_public": str(include_public).lower(),
        "include_web_public": str(include_web_public).lower(),
        "include_subscribed": str(include_subscribed).lower(),
        "exclude_archived": str(exclude_archived).lower(),
        "include_all": str(include_all).lower(),
        "include_default": str(include_default).lower(),
        "include_owner_subscribed": str(include_owner_subscribed).lower(),
        "include_can_access_content": str(include_can_access_content).lower(),
    }
    try:
        response = requests.get(url, auth=AUTH, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        try:
            return response.json()
        except Exception:
            return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}
