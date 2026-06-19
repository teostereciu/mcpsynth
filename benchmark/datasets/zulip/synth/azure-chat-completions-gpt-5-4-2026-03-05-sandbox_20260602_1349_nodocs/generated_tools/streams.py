from typing import Any, Dict, List, Optional

from generated_tools.common import client, json_dumps


def get_streams(include_public: bool = True, include_subscribed: bool = True, include_all_active: bool = False) -> Dict[str, Any]:
    params = {
        "include_public": str(include_public).lower(),
        "include_subscribed": str(include_subscribed).lower(),
        "include_all_active": str(include_all_active).lower(),
    }
    return client.request("GET", "/streams", params=params)


def create_streams(stream_names: List[str], description: Optional[str] = None, invite_only: Optional[bool] = None, is_web_public: Optional[bool] = None) -> Dict[str, Any]:
    subscriptions = []
    for name in stream_names:
        item: Dict[str, Any] = {"name": name}
        if description is not None:
            item["description"] = description
        subscriptions.append(item)
    params: Dict[str, Any] = {"subscriptions": json_dumps(subscriptions)}
    if invite_only is not None:
        params["invite_only"] = str(invite_only).lower()
    if is_web_public is not None:
        params["is_web_public"] = str(is_web_public).lower()
    return client.request("POST", "/users/me/subscriptions", params=params)


def subscribe_streams(stream_names: List[str], principals: Optional[List[str]] = None) -> Dict[str, Any]:
    subscriptions = [{"name": name} for name in stream_names]
    params: Dict[str, Any] = {"subscriptions": json_dumps(subscriptions)}
    if principals is not None:
        params["principals"] = json_dumps(principals)
    return client.request("POST", "/users/me/subscriptions", params=params)


def unsubscribe_streams(stream_names: List[str], principals: Optional[List[str]] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {"subscriptions": json_dumps(stream_names)}
    if principals is not None:
        params["principals"] = json_dumps(principals)
    return client.request("DELETE", "/users/me/subscriptions", params=params)


def get_stream_id(stream: str) -> Dict[str, Any]:
    return client.request("GET", f"/get_stream_id", params={"stream": stream})


def archive_stream(stream_id: int) -> Dict[str, Any]:
    return client.request("DELETE", f"/streams/{stream_id}")


def update_stream(stream_id: int, description: Optional[str] = None, new_name: Optional[str] = None, is_private: Optional[bool] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if description is not None:
        params["description"] = description
    if new_name is not None:
        params["new_name"] = new_name
    if is_private is not None:
        params["is_private"] = str(is_private).lower()
    return client.request("PATCH", f"/streams/{stream_id}", params=params)


def get_topics(stream_id: int) -> Dict[str, Any]:
    return client.request("GET", f"/users/me/{stream_id}/topics")
