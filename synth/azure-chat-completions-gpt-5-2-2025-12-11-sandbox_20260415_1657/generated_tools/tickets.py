from typing import Any, Dict, List, Optional

from ._client import get_client


def list_tickets(
    page: Optional[int] = None,
    per_page: Optional[int] = None,
    sort_by: Optional[str] = None,
    sort_order: Optional[str] = None,
    include: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /api/v2/tickets"""
    client = get_client()
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if per_page is not None:
        params["per_page"] = per_page
    if sort_by is not None:
        params["sort_by"] = sort_by
    if sort_order is not None:
        params["sort_order"] = sort_order
    if include is not None:
        params["include"] = include
    return client.request("GET", f"{client.base_support}/tickets", params=params)  # type: ignore


def show_ticket(ticket_id: int, include: Optional[str] = None) -> Dict[str, Any]:
    """GET /api/v2/tickets/{ticket_id}"""
    client = get_client()
    params: Dict[str, Any] = {}
    if include is not None:
        params["include"] = include
    return client.request("GET", f"{client.base_support}/tickets/{ticket_id}", params=params)  # type: ignore


def show_multiple_tickets(ids: List[int], include: Optional[str] = None) -> Dict[str, Any]:
    """GET /api/v2/tickets/show_many?ids=..."""
    client = get_client()
    params: Dict[str, Any] = {"ids": ",".join(str(i) for i in ids)}
    if include is not None:
        params["include"] = include
    return client.request("GET", f"{client.base_support}/tickets/show_many", params=params)  # type: ignore


def create_ticket(ticket: Dict[str, Any]) -> Dict[str, Any]:
    """POST /api/v2/tickets

    Body should be {"ticket": {...}}.
    """
    client = get_client()
    return client.request("POST", f"{client.base_support}/tickets", json={"ticket": ticket})  # type: ignore


def update_ticket(ticket_id: int, ticket: Dict[str, Any]) -> Dict[str, Any]:
    """PUT /api/v2/tickets/{ticket_id}

    Body should be {"ticket": {...}}.
    """
    client = get_client()
    return client.request(
        "PUT", f"{client.base_support}/tickets/{ticket_id}", json={"ticket": ticket}
    )  # type: ignore


def delete_ticket(ticket_id: int) -> Dict[str, Any]:
    """DELETE /api/v2/tickets/{ticket_id}"""
    client = get_client()
    return client.request("DELETE", f"{client.base_support}/tickets/{ticket_id}")  # type: ignore


def list_recent_tickets() -> Dict[str, Any]:
    """GET /api/v2/tickets/recent"""
    client = get_client()
    return client.request("GET", f"{client.base_support}/tickets/recent")  # type: ignore


def list_organization_tickets(
    organization_id: int,
    page: Optional[int] = None,
    per_page: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /api/v2/organizations/{organization_id}/tickets"""
    client = get_client()
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if per_page is not None:
        params["per_page"] = per_page
    return client.request(
        "GET", f"{client.base_support}/organizations/{organization_id}/tickets", params=params
    )  # type: ignore


def list_user_requested_tickets(user_id: int, page: Optional[int] = None, per_page: Optional[int] = None) -> Dict[str, Any]:
    """GET /api/v2/users/{user_id}/tickets/requested"""
    client = get_client()
    params: Dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if per_page is not None:
        params["per_page"] = per_page
    return client.request(
        "GET", f"{client.base_support}/users/{user_id}/tickets/requested", params=params
    )  # type: ignore


def merge_tickets(target_ticket_id: int, source_ticket_ids: List[int]) -> Dict[str, Any]:
    """POST /api/v2/tickets/{target_ticket_id}/merge

    Body: {"ids": [..]}
    """
    client = get_client()
    return client.request(
        "POST",
        f"{client.base_support}/tickets/{target_ticket_id}/merge",
        json={"ids": source_ticket_ids},
    )  # type: ignore
