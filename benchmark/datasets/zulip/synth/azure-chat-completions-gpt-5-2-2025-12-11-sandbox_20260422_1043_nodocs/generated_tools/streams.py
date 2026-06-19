import json as _json
from typing import Any, Dict, List, Optional, Union

from .client import ZulipClient


def get_streams(include_public: bool = True, include_subscribed: bool = True, include_all_active: bool = False, include_default: bool = False, include_owner_subscribed: bool = False) -> Dict[str, Any]:
    c = ZulipClient()
    params = {
        "include_public": "true" if include_public else "false",
        "include_subscribed": "true" if include_subscribed else "false",
        "include_all_active": "true" if include_all_active else "false",
        "include_default": "true" if include_default else "false",
        "include_owner_subscribed": "true" if include_owner_subscribed else "false",
    }
    return c.request("GET", "/streams", params=params)


def create_streams(streams: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Create one or more streams.

    streams: list of {"name": ..., "description": ..., "invite_only": bool, ...}
    """
    c = ZulipClient()
    data = {"subscriptions": _json.dumps(streams)}
    return c.request("POST", "/users/me/subscriptions", data=data)


def subscribe(streams: List[Dict[str, Any]], principals: Optional[List[Union[int, str]]] = None, authorization_errors_fatal: Optional[bool] = None) -> Dict[str, Any]:
    c = ZulipClient()
    data: Dict[str, Any] = {"subscriptions": _json.dumps(streams)}
    if principals is not None:
        data["principals"] = _json.dumps(principals)
    if authorization_errors_fatal is not None:
        data["authorization_errors_fatal"] = "true" if authorization_errors_fatal else "false"
    return c.request("POST", "/users/me/subscriptions", data=data)


def unsubscribe(stream_names: List[str], principals: Optional[List[Union[int, str]]] = None) -> Dict[str, Any]:
    c = ZulipClient()
    data: Dict[str, Any] = {"subscriptions": _json.dumps(stream_names)}
    if principals is not None:
        data["principals"] = _json.dumps(principals)
    return c.request("DELETE", "/users/me/subscriptions", data=data)


def get_subscriptions(include_subscribers: bool = False) -> Dict[str, Any]:
    c = ZulipClient()
    params = {"include_subscribers": "true" if include_subscribers else "false"}
    return c.request("GET", "/users/me/subscriptions", params=params)


def update_stream(stream_id: int, new_name: Optional[str] = None, description: Optional[str] = None, is_private: Optional[bool] = None, is_web_public: Optional[bool] = None, stream_post_policy: Optional[int] = None, message_retention_days: Optional[Union[int, str]] = None) -> Dict[str, Any]:
    c = ZulipClient()
    data: Dict[str, Any] = {}
    if new_name is not None:
        data["new_name"] = new_name
    if description is not None:
        data["description"] = description
    if is_private is not None:
        data["is_private"] = "true" if is_private else "false"
    if is_web_public is not None:
        data["is_web_public"] = "true" if is_web_public else "false"
    if stream_post_policy is not None:
        data["stream_post_policy"] = stream_post_policy
    if message_retention_days is not None:
        data["message_retention_days"] = message_retention_days
    return c.request("PATCH", f"/streams/{stream_id}", data=data)


def archive_stream(stream_id: int) -> Dict[str, Any]:
    c = ZulipClient()
    return c.request("DELETE", f"/streams/{stream_id}")


def get_stream_id(stream: str) -> Dict[str, Any]:
    c = ZulipClient()
    return c.request("GET", "/get_stream_id", params={"stream": stream})
