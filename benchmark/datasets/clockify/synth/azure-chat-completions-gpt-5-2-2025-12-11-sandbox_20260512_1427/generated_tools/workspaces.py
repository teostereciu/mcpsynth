from typing import Any, Dict, Optional

from .http import request_json


def list_workspaces(roles: Optional[str] = None) -> Any:
    """Get all my workspaces. Optionally filter by roles (repeatable in API; pass comma-separated)."""
    params: Dict[str, Any] = {}
    if roles:
        # docs show repeated roles=...; accept comma-separated and send as list
        parts = [r.strip() for r in roles.split(",") if r.strip()]
        params["roles"] = parts if len(parts) > 1 else roles
    return request_json("GET", "/workspaces", params=params or None)


def create_workspace(name: str, organizationId: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {"name": name}
    if organizationId is not None:
        body["organizationId"] = organizationId
    return request_json("POST", "/workspaces", json=body)


def get_workspace(workspaceId: str) -> Any:
    return request_json("GET", f"/workspaces/{workspaceId}")


def update_workspace_cost_rate(workspaceId: str, amount: int, since: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {"amount": amount}
    if since is not None:
        body["since"] = since
    return request_json("PUT", f"/workspaces/{workspaceId}/cost-rate", json=body)


def update_workspace_billable_rate(workspaceId: str, amount: int, currency: str = "USD", since: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {"amount": amount, "currency": currency}
    if since is not None:
        body["since"] = since
    return request_json("PUT", f"/workspaces/{workspaceId}/billable-rate", json=body)


def add_user_to_workspace(workspaceId: str, email: str, send_email: bool = True) -> Any:
    params = {"send-email": str(send_email).lower()}
    body = {"email": email}
    return request_json("POST", f"/workspaces/{workspaceId}/users", params=params, json=body)


def update_user_status(workspaceId: str, userId: str, status: str) -> Any:
    return request_json("PUT", f"/workspaces/{workspaceId}/users/{userId}/status", json={"status": status})


def update_user_cost_rate(workspaceId: str, userId: str, amount: int, since: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {"amount": amount}
    if since is not None:
        body["since"] = since
    return request_json("PUT", f"/workspaces/{workspaceId}/users/{userId}/cost-rate", json=body)


def update_user_hourly_rate(workspaceId: str, userId: str, amount: int, since: Optional[str] = None) -> Any:
    body: Dict[str, Any] = {"amount": amount}
    if since is not None:
        body["since"] = since
    return request_json("PUT", f"/workspaces/{workspaceId}/users/{userId}/hourly-rate", json=body)
