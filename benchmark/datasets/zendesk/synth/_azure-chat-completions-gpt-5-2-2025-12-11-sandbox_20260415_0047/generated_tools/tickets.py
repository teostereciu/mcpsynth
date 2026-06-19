"""Ticketing: Tickets tools."""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import zendesk_delete, zendesk_get, zendesk_post, zendesk_put


def _unwrap(obj: Dict[str, Any], key: str) -> Dict[str, Any]:
    if not isinstance(obj, dict):
        return {"error": "invalid_response", "description": "Expected dict response"}
    if "error" in obj and "status" in obj:
        return obj
    return obj.get(key) or obj


def tickets_list(per_page: int = 25, page: Optional[int] = None, sort_by: Optional[str] = None, sort_order: Optional[str] = None) -> Dict[str, Any]:
    """List tickets.

    Maps to GET /api/v2/tickets
    """
    params: Dict[str, Any] = {"per_page": per_page}
    if page is not None:
        params["page"] = page
    if sort_by:
        params["sort_by"] = sort_by
    if sort_order:
        params["sort_order"] = sort_order
    return zendesk_get("/tickets", params=params)


def tickets_list_recent(per_page: int = 25, page: Optional[int] = None) -> Dict[str, Any]:
    """List recent tickets.

    Maps to GET /api/v2/tickets/recent
    """
    params: Dict[str, Any] = {"per_page": per_page}
    if page is not None:
        params["page"] = page
    return zendesk_get("/tickets/recent", params=params)


def tickets_show(ticket_id: int) -> Dict[str, Any]:
    """Show a ticket by id.

    Maps to GET /api/v2/tickets/{id}
    """
    return _unwrap(zendesk_get(f"/tickets/{ticket_id}"), "ticket")


def tickets_create(subject: Optional[str] = None, comment_body: Optional[str] = None, priority: Optional[str] = None, requester_id: Optional[int] = None, requester: Optional[Any] = None, additional_fields: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Create a ticket.

    Maps to POST /api/v2/tickets

    Args:
      subject: Ticket subject
      comment_body: First comment body
      priority: urgent|high|normal|low
      requester_id: requester user id
      requester: alternative requester spec (email string, user id, or {name,email})
      additional_fields: merged into ticket payload (e.g., group_id, assignee_id, tags, custom_fields)
    """
    ticket: Dict[str, Any] = {}
    if subject is not None:
        ticket["subject"] = subject
    if comment_body is not None:
        ticket["comment"] = {"body": comment_body}
    if priority is not None:
        ticket["priority"] = priority
    if requester_id is not None:
        ticket["requester_id"] = requester_id
    if requester is not None:
        ticket["requester"] = requester
    if additional_fields:
        ticket.update(additional_fields)

    return _unwrap(zendesk_post("/tickets", {"ticket": ticket}), "ticket")


def tickets_update(ticket_id: int, fields: Dict[str, Any]) -> Dict[str, Any]:
    """Update a ticket.

    Maps to PUT /api/v2/tickets/{id}

    Use fields to set any writable ticket properties. To add a comment:
      fields={"comment": {"body": "...", "public": True}}
    """
    return _unwrap(zendesk_put(f"/tickets/{ticket_id}", {"ticket": fields}), "ticket")


def tickets_delete(ticket_id: int) -> Dict[str, Any]:
    """Delete a ticket.

    Maps to DELETE /api/v2/tickets/{id}
    """
    return zendesk_delete(f"/tickets/{ticket_id}")
