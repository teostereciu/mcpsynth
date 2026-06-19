from typing import Any, Optional

from generated_tools.common import client, compact_kwargs, parse_json_body


API_BASE = "/sell/fulfillment/v1"


def get_orders(field_groups: Optional[str] = None, filter: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, order_ids: Optional[str] = None) -> Any:
    try:
        return client.request(API_BASE, "GET", "/order", params=compact_kwargs(fieldGroups=field_groups, filter=filter, limit=limit, offset=offset, orderIds=order_ids))
    except Exception as e:
        return {"error": str(e)}


def get_order(order_id: str, field_groups: Optional[str] = None) -> Any:
    try:
        return client.request(API_BASE, "GET", f"/order/{order_id}", params=compact_kwargs(fieldGroups=field_groups))
    except Exception as e:
        return {"error": str(e)}


def create_shipping_fulfillment(order_id: str, body: str) -> Any:
    try:
        return client.request(API_BASE, "POST", f"/order/{order_id}/shipping_fulfillment", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def get_shipping_fulfillments(order_id: str) -> Any:
    try:
        return client.request(API_BASE, "GET", f"/order/{order_id}/shipping_fulfillment")
    except Exception as e:
        return {"error": str(e)}


def get_shipping_fulfillment(order_id: str, fulfillment_id: str) -> Any:
    try:
        return client.request(API_BASE, "GET", f"/order/{order_id}/shipping_fulfillment/{fulfillment_id}")
    except Exception as e:
        return {"error": str(e)}


def issue_refund(order_id: str, body: str) -> Any:
    try:
        return client.request(API_BASE, "POST", f"/order/{order_id}/issue_refund", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def get_payment_dispute_summaries(limit: Optional[int] = None, offset: Optional[int] = None) -> Any:
    try:
        return client.request(API_BASE, "GET", "/payment_dispute_summary", params=compact_kwargs(limit=limit, offset=offset))
    except Exception as e:
        return {"error": str(e)}


def get_payment_dispute(payment_dispute_id: str) -> Any:
    try:
        return client.request(API_BASE, "GET", f"/payment_dispute/{payment_dispute_id}")
    except Exception as e:
        return {"error": str(e)}


def get_activities(payment_dispute_id: str) -> Any:
    try:
        return client.request(API_BASE, "GET", f"/payment_dispute/{payment_dispute_id}/activity")
    except Exception as e:
        return {"error": str(e)}


def accept_payment_dispute(payment_dispute_id: str, body: Optional[str] = None) -> Any:
    try:
        return client.request(API_BASE, "POST", f"/payment_dispute/{payment_dispute_id}/accept", json_body=parse_json_body(body) if body else None)
    except Exception as e:
        return {"error": str(e)}


def contest_payment_dispute(payment_dispute_id: str, body: str) -> Any:
    try:
        return client.request(API_BASE, "POST", f"/payment_dispute/{payment_dispute_id}/contest", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def add_evidence(payment_dispute_id: str, body: str) -> Any:
    try:
        return client.request(API_BASE, "POST", f"/payment_dispute/{payment_dispute_id}/add_evidence", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def update_evidence(payment_dispute_id: str, body: str) -> Any:
    try:
        return client.request(API_BASE, "POST", f"/payment_dispute/{payment_dispute_id}/update_evidence", json_body=parse_json_body(body))
    except Exception as e:
        return {"error": str(e)}


def fetch_evidence_content(payment_dispute_id: str) -> Any:
    try:
        return client.request(API_BASE, "GET", f"/payment_dispute/{payment_dispute_id}/fetch_evidence_content")
    except Exception as e:
        return {"error": str(e)}


def upload_evidence_file(payment_dispute_id: str, content: str, content_type: str = "application/octet-stream") -> Any:
    try:
        return client.request(API_BASE, "POST", f"/payment_dispute/{payment_dispute_id}/upload_evidence_file", headers={"Content-Type": content_type}, data=content)
    except Exception as e:
        return {"error": str(e)}
