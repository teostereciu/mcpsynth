import json
from typing import Any, Dict, List, Optional, Union

from .client import ZulipClient


def get_streams(include_public: Optional[bool] = None, include_subscribed: Optional[bool] = None) -> Dict[str, Any]:
    """GET /streams"""
    params: Dict[str, Any] = {}
    if include_public is not None:
        params["include_public"] = json.dumps(include_public)
    if include_subscribed is not None:
        params["include_subscribed"] = json.dumps(include_subscribed)
    return ZulipClient().request("GET", "/streams", params=params)


def get_stream_id(stream: str) -> Dict[str, Any]:
    """GET /get_stream_id"""
    return ZulipClient().request("GET", "/get_stream_id", params={"stream": stream})


def get_stream_by_id(stream_id: int) -> Dict[str, Any]:
    """GET /streams/{stream_id}"""
    return ZulipClient().request("GET", f"/streams/{stream_id}")


def create_stream(
    name: str,
    description: Optional[str] = None,
    invite_only: Optional[bool] = None,
    is_web_public: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /streams"""
    data: Dict[str, Any] = {"name": name}
    if description is not None:
        data["description"] = description
    if invite_only is not None:
        data["invite_only"] = json.dumps(invite_only)
    if is_web_public is not None:
        data["is_web_public"] = json.dumps(is_web_public)
    return ZulipClient().request("POST", "/streams", data=data)


def update_stream(
    stream_id: int,
    new_name: Optional[str] = None,
    description: Optional[str] = None,
    is_private: Optional[bool] = None,
) -> Dict[str, Any]:
    """PATCH /streams/{stream_id}"""
    data: Dict[str, Any] = {}
    if new_name is not None:
        data["new_name"] = new_name
    if description is not None:
        data["description"] = description
    if is_private is not None:
        data["is_private"] = json.dumps(is_private)
    return ZulipClient().request("PATCH", f"/streams/{stream_id}", data=data)


def archive_stream(stream_id: int) -> Dict[str, Any]:
    """DELETE /streams/{stream_id}"""
    return ZulipClient().request("DELETE", f"/streams/{stream_id}")


def get_subscriptions(include_subscribers: Optional[bool] = None) -> Dict[str, Any]:
    """GET /users/me/subscriptions"""
    params: Dict[str, Any] = {}
    if include_subscribers is not None:
        params["include_subscribers"] = json.dumps(include_subscribers)
    return ZulipClient().request("GET", "/users/me/subscriptions", params=params)


def subscribe(
    subscriptions: List[Dict[str, Any]],
    principals: Optional[List[Union[int, str]]] = None,
    authorization_errors_fatal: Optional[bool] = None,
    invite_only: Optional[bool] = None,
    announce: Optional[bool] = None,
    is_web_public: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /users/me/subscriptions"""
    data: Dict[str, Any] = {"subscriptions": json.dumps(subscriptions)}
    if principals is not None:
        data["principals"] = json.dumps(principals)
    if authorization_errors_fatal is not None:
        data["authorization_errors_fatal"] = json.dumps(authorization_errors_fatal)
    if invite_only is not None:
        data["invite_only"] = json.dumps(invite_only)
    if announce is not None:
        data["announce"] = json.dumps(announce)
    if is_web_public is not None:
        data["is_web_public"] = json.dumps(is_web_public)
    return ZulipClient().request("POST", "/users/me/subscriptions", data=data)


def unsubscribe(subscriptions: List[str], principals: Optional[List[Union[int, str]]] = None) -> Dict[str, Any]:
    """DELETE /users/me/subscriptions"""
    data: Dict[str, Any] = {"subscriptions": json.dumps(subscriptions)}
    if principals is not None:
        data["principals"] = json.dumps(principals)
    return ZulipClient().request("DELETE", "/users/me/subscriptions", data=data)


def get_subscribers(stream_id: int) -> Dict[str, Any]:
    """GET /streams/{stream_id}/members"""
    return ZulipClient().request("GET", f"/streams/{stream_id}/members")


def get_stream_topics(stream_id: int) -> Dict[str, Any]:
    """GET /users/me/{stream_id}/topics"""
    return ZulipClient().request("GET", f"/users/me/{stream_id}/topics")


def delete_topic(stream_id: int, topic_name: str) -> Dict[str, Any]:
    """POST /streams/{stream_id}/delete_topic"""
    return ZulipClient().request(
        "POST",
        f"/streams/{stream_id}/delete_topic",
        data={"topic_name": topic_name},
    )
