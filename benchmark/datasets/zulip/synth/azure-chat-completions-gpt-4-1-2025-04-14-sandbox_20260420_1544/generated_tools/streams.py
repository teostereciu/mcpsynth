import os
import requests
from typing import Any, Dict, List, Optional, Union

def zulip_auth() -> Dict[str, str]:
    return {
        "email": os.environ["ZULIP_EMAIL"],
        "api_key": os.environ["ZULIP_API_KEY"],
        "site": os.environ["ZULIP_SITE"].rstrip("/"),
    }

def get_streams(include_public: Optional[bool] = True, include_web_public: Optional[bool] = False, include_subscribed: Optional[bool] = True, exclude_archived: Optional[bool] = True, include_all: Optional[bool] = False, include_default: Optional[bool] = False, include_owner_subscribed: Optional[bool] = False, include_can_access_content: Optional[bool] = False, include_all_active: Optional[bool] = None) -> Dict[str, Any]:
    """
    Get all channels (streams) the user has access to.
    """
    auth = zulip_auth()
    url = f"{auth['site']}/api/v1/streams"
    params = {}
    if include_public is not None:
        params["include_public"] = include_public
    if include_web_public is not None:
        params["include_web_public"] = include_web_public
    if include_subscribed is not None:
        params["include_subscribed"] = include_subscribed
    if exclude_archived is not None:
        params["exclude_archived"] = exclude_archived
    if include_all is not None:
        params["include_all"] = include_all
    if include_default is not None:
        params["include_default"] = include_default
    if include_owner_subscribed is not None:
        params["include_owner_subscribed"] = include_owner_subscribed
    if include_can_access_content is not None:
        params["include_can_access_content"] = include_can_access_content
    if include_all_active is not None:
        params["include_all_active"] = include_all_active
    resp = requests.get(url, auth=(auth["email"], auth["api_key"]), params=params)
    try:
        return resp.json()
    except Exception:
        return {"error": f"Invalid response: {resp.text}"}

def update_stream(stream_id: int, description: Optional[str] = None, new_name: Optional[str] = None, is_private: Optional[bool] = None, is_web_public: Optional[bool] = None, history_public_to_subscribers: Optional[bool] = None, is_default_stream: Optional[bool] = None, message_retention_days: Optional[Union[str, int]] = None, is_archived: Optional[bool] = None, folder_id: Optional[int] = None, topics_policy: Optional[str] = None) -> Dict[str, Any]:
    """
    Update a channel (stream) by ID.
    """
    auth = zulip_auth()
    url = f"{auth['site']}/api/v1/streams/{stream_id}"
    data = {}
    if description is not None:
        data["description"] = description
    if new_name is not None:
        data["new_name"] = new_name
    if is_private is not None:
        data["is_private"] = is_private
    if is_web_public is not None:
        data["is_web_public"] = is_web_public
    if history_public_to_subscribers is not None:
        data["history_public_to_subscribers"] = history_public_to_subscribers
    if is_default_stream is not None:
        data["is_default_stream"] = is_default_stream
    if message_retention_days is not None:
        data["message_retention_days"] = message_retention_days
    if is_archived is not None:
        data["is_archived"] = is_archived
    if folder_id is not None:
        data["folder_id"] = folder_id
    if topics_policy is not None:
        data["topics_policy"] = topics_policy
    resp = requests.patch(url, auth=(auth["email"], auth["api_key"]), data=data)
    try:
        return resp.json()
    except Exception:
        return {"error": f"Invalid response: {resp.text}"}

def archive_stream(stream_id: int) -> Dict[str, Any]:
    """
    Archive a channel (stream) by ID.
    """
    auth = zulip_auth()
    url = f"{auth['site']}/api/v1/streams/{stream_id}"
    resp = requests.delete(url, auth=(auth["email"], auth["api_key"]))
    try:
        return resp.json()
    except Exception:
        return {"error": f"Invalid response: {resp.text}"}
