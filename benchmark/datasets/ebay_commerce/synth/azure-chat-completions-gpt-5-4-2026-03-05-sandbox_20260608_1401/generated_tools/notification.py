from typing import Any, Dict, Optional

from generated_tools.catalog import client


NOTIFICATION_BASE = "/commerce/notification/v1"


def _nrequest(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json_body: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return client.request(method, f"{NOTIFICATION_BASE}{path}", token_type="app", params=params, json_body=json_body, headers={"Content-Type": "application/json"} if json_body is not None else None)


def create_destination(endpoint: str, verification_token: str, status: str, name: Optional[str] = None) -> Dict[str, Any]:
    body: Dict[str, Any] = {
        "deliveryConfig": {"endpoint": endpoint, "verificationToken": verification_token},
        "status": status,
    }
    if name is not None:
        body["name"] = name
    return _nrequest("POST", "/destination", json_body=body)


def get_destinations(limit: Optional[int] = None, continuation_token: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if continuation_token is not None:
        params["continuation_token"] = continuation_token
    return _nrequest("GET", "/destination", params=params)


def get_destination(destination_id: str) -> Dict[str, Any]:
    return _nrequest("GET", f"/destination/{destination_id}")


def update_destination(destination_id: str, endpoint: str, verification_token: str, status: str, name: Optional[str] = None) -> Dict[str, Any]:
    body: Dict[str, Any] = {
        "deliveryConfig": {"endpoint": endpoint, "verificationToken": verification_token},
        "status": status,
    }
    if name is not None:
        body["name"] = name
    return _nrequest("PUT", f"/destination/{destination_id}", json_body=body)


def delete_destination(destination_id: str) -> Dict[str, Any]:
    return _nrequest("DELETE", f"/destination/{destination_id}")


def get_config() -> Dict[str, Any]:
    return _nrequest("GET", "/config")


def update_config(alert_email: str) -> Dict[str, Any]:
    return _nrequest("PUT", "/config", json_body={"alertEmail": alert_email})


def get_public_key(public_key_id: str) -> Dict[str, Any]:
    return _nrequest("GET", f"/public_key/{public_key_id}")
