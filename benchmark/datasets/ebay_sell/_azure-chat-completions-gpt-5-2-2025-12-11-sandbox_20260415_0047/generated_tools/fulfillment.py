from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json

API_ROOT = "/sell/fulfillment/v1"
SCOPE = "https://api.ebay.com/oauth/api_scope/sell.fulfillment"


def register(mcp):
    @mcp.tool()
    def fulfillment_get_orders(
        *,
        filter: Optional[str] = None,
        order_ids: Optional[str] = None,
        field_groups: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        """GET /order - Search orders."""
        params: Dict[str, Any] = {}
        if filter is not None:
            params["filter"] = filter
        if order_ids is not None:
            params["orderIds"] = order_ids
        if field_groups is not None:
            params["fieldGroups"] = field_groups
        if limit is not None:
            params["limit"] = str(limit)
        if offset is not None:
            params["offset"] = str(offset)
        return request_json("GET", API_ROOT, "/order", scope=SCOPE, params=params or None)

    @mcp.tool()
    def fulfillment_get_order(order_id: str) -> Dict[str, Any]:
        """GET /order/{orderId} - Get an order."""
        return request_json("GET", API_ROOT, f"/order/{order_id}", scope=SCOPE)

    @mcp.tool()
    def fulfillment_create_shipping_fulfillment(order_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /order/{orderId}/shipping_fulfillment - Create shipping fulfillment."""
        return request_json(
            "POST",
            API_ROOT,
            f"/order/{order_id}/shipping_fulfillment",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def fulfillment_get_shipping_fulfillments(order_id: str) -> Dict[str, Any]:
        """GET /order/{orderId}/shipping_fulfillment - Get shipping fulfillments."""
        return request_json("GET", API_ROOT, f"/order/{order_id}/shipping_fulfillment", scope=SCOPE)

    @mcp.tool()
    def fulfillment_get_shipping_fulfillment(order_id: str, fulfillment_id: str) -> Dict[str, Any]:
        """GET /order/{orderId}/shipping_fulfillment/{fulfillmentId} - Get a shipping fulfillment."""
        return request_json(
            "GET",
            API_ROOT,
            f"/order/{order_id}/shipping_fulfillment/{fulfillment_id}",
            scope=SCOPE,
        )

    # Payment disputes
    @mcp.tool()
    def fulfillment_get_payment_dispute_summaries(
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Dict[str, Any]:
        """GET /payment_dispute_summary - Get payment dispute summaries."""
        params: Dict[str, Any] = {}
        if limit is not None:
            params["limit"] = str(limit)
        if offset is not None:
            params["offset"] = str(offset)
        return request_json("GET", API_ROOT, "/payment_dispute_summary", scope=SCOPE, params=params or None)

    @mcp.tool()
    def fulfillment_get_payment_dispute(payment_dispute_id: str) -> Dict[str, Any]:
        """GET /payment_dispute/{payment_dispute_id} - Get a payment dispute."""
        return request_json("GET", API_ROOT, f"/payment_dispute/{payment_dispute_id}", scope=SCOPE)

    @mcp.tool()
    def fulfillment_get_activities(payment_dispute_id: str) -> Dict[str, Any]:
        """GET /payment_dispute/{payment_dispute_id}/activity - Get dispute activities."""
        return request_json("GET", API_ROOT, f"/payment_dispute/{payment_dispute_id}/activity", scope=SCOPE)

    @mcp.tool()
    def fulfillment_accept_payment_dispute(payment_dispute_id: str) -> Dict[str, Any]:
        """POST /payment_dispute/{payment_dispute_id}/accept - Accept dispute."""
        return request_json(
            "POST",
            API_ROOT,
            f"/payment_dispute/{payment_dispute_id}/accept",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body={},
        )

    @mcp.tool()
    def fulfillment_contest_payment_dispute(payment_dispute_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /payment_dispute/{payment_dispute_id}/contest - Contest dispute."""
        return request_json(
            "POST",
            API_ROOT,
            f"/payment_dispute/{payment_dispute_id}/contest",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def fulfillment_add_evidence(payment_dispute_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /payment_dispute/{payment_dispute_id}/add_evidence - Add evidence."""
        return request_json(
            "POST",
            API_ROOT,
            f"/payment_dispute/{payment_dispute_id}/add_evidence",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def fulfillment_update_evidence(payment_dispute_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /payment_dispute/{payment_dispute_id}/update_evidence - Update evidence."""
        return request_json(
            "POST",
            API_ROOT,
            f"/payment_dispute/{payment_dispute_id}/update_evidence",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def fulfillment_fetch_evidence_content(payment_dispute_id: str) -> Dict[str, Any]:
        """GET /payment_dispute/{payment_dispute_id}/fetch_evidence_content - Fetch evidence content."""
        return request_json(
            "GET",
            API_ROOT,
            f"/payment_dispute/{payment_dispute_id}/fetch_evidence_content",
            scope=SCOPE,
        )

    @mcp.tool()
    def fulfillment_upload_evidence_file(payment_dispute_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /payment_dispute/{payment_dispute_id}/upload_evidence_file - Upload evidence file."""
        return request_json(
            "POST",
            API_ROOT,
            f"/payment_dispute/{payment_dispute_id}/upload_evidence_file",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    # Refunds
    @mcp.tool()
    def fulfillment_issue_refund(order_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /order/{order_id}/issue_refund - Issue a refund."""
        return request_json(
            "POST",
            API_ROOT,
            f"/order/{order_id}/issue_refund",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )
