"""Tools for Stripe Coupons and Promotion Codes APIs."""
import os
import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.stripe.com"

def _get_headers():
    api_key = os.environ.get("STRIPE_API_KEY", "")
    return {"Authorization": f"Bearer {api_key}"}

def _req(method, path, params=None, data=None):
    url = f"{BASE_URL}{path}"
    try:
        resp = requests.request(
            method, url,
            headers=_get_headers(),
            params=params,
            data=data,
            timeout=30,
        )
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def register_coupon_promotion_tools(mcp: FastMCP):

    # ── Coupons ────────────────────────────────────────────────────────────

    @mcp.tool()
    def create_coupon(
        duration: str,
        amount_off: int = None,
        currency: str = None,
        percent_off: float = None,
        name: str = None,
        duration_in_months: int = None,
        max_redemptions: int = None,
        redeem_by: int = None,
        metadata: dict = None,
    ) -> dict:
        """Create a Coupon for discounts on subscriptions or invoices.

        Args:
            duration: 'forever', 'once', or 'repeating'.
            amount_off: Amount to subtract from invoice total (in smallest currency unit).
            currency: Currency for amount_off (required if amount_off is set).
            percent_off: Percentage discount (0-100). Required if amount_off not set.
            name: Name displayed to customers on invoices/receipts.
            duration_in_months: Number of months for 'repeating' duration.
            max_redemptions: Maximum number of times this coupon can be redeemed.
            redeem_by: Unix timestamp after which the coupon can no longer be redeemed.
            metadata: Key-value pairs to attach.
        """
        data = {"duration": duration}
        if amount_off is not None: data["amount_off"] = amount_off
        if currency: data["currency"] = currency
        if percent_off is not None: data["percent_off"] = percent_off
        if name: data["name"] = name
        if duration_in_months is not None: data["duration_in_months"] = duration_in_months
        if max_redemptions is not None: data["max_redemptions"] = max_redemptions
        if redeem_by is not None: data["redeem_by"] = redeem_by
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/coupons", data=data)

    @mcp.tool()
    def retrieve_coupon(coupon_id: str) -> dict:
        """Retrieve a Coupon by ID.

        Args:
            coupon_id: The ID of the coupon to retrieve.
        """
        return _req("GET", f"/v1/coupons/{coupon_id}")

    @mcp.tool()
    def update_coupon(
        coupon_id: str,
        name: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update a Coupon's name or metadata.

        Args:
            coupon_id: The ID of the coupon to update.
            name: New name for the coupon.
            metadata: Key-value pairs to attach.
        """
        data = {}
        if name: data["name"] = name
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/coupons/{coupon_id}", data=data)

    @mcp.tool()
    def delete_coupon(coupon_id: str) -> dict:
        """Delete a Coupon.

        Args:
            coupon_id: The ID of the coupon to delete.
        """
        return _req("DELETE", f"/v1/coupons/{coupon_id}")

    @mcp.tool()
    def list_coupons(
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List all Coupons.

        Args:
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
        params = {}
        if limit is not None: params["limit"] = limit
        if starting_after: params["starting_after"] = starting_after
        if ending_before: params["ending_before"] = ending_before
        return _req("GET", "/v1/coupons", params=params)

    # ── Promotion Codes ────────────────────────────────────────────────────

    @mcp.tool()
    def create_promotion_code(
        coupon: str,
        code: str = None,
        customer: str = None,
        active: bool = None,
        expires_at: int = None,
        max_redemptions: int = None,
        metadata: dict = None,
    ) -> dict:
        """Create a Promotion Code for a Coupon.

        Args:
            coupon: ID of the coupon this promotion code points to.
            code: Customer-facing code (auto-generated if not provided).
            customer: Restrict to a specific customer ID.
            active: Whether the promotion code is active.
            expires_at: Unix timestamp after which the code can no longer be redeemed.
            max_redemptions: Maximum number of times this code can be redeemed.
            metadata: Key-value pairs to attach.
        """
        data = {
            "promotion[type]": "coupon",
            "promotion[coupon]": coupon,
        }
        if code: data["code"] = code
        if customer: data["customer"] = customer
        if active is not None: data["active"] = str(active).lower()
        if expires_at is not None: data["expires_at"] = expires_at
        if max_redemptions is not None: data["max_redemptions"] = max_redemptions
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/promotion_codes", data=data)

    @mcp.tool()
    def retrieve_promotion_code(promotion_code_id: str) -> dict:
        """Retrieve a Promotion Code by ID.

        Args:
            promotion_code_id: The ID of the promotion code to retrieve.
        """
        return _req("GET", f"/v1/promotion_codes/{promotion_code_id}")

    @mcp.tool()
    def update_promotion_code(
        promotion_code_id: str,
        active: bool = None,
        metadata: dict = None,
    ) -> dict:
        """Update a Promotion Code.

        Args:
            promotion_code_id: The ID of the promotion code to update.
            active: Whether the promotion code is active.
            metadata: Key-value pairs to attach.
        """
        data = {}
        if active is not None: data["active"] = str(active).lower()
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/promotion_codes/{promotion_code_id}", data=data)

    @mcp.tool()
    def list_promotion_codes(
        active: bool = None,
        code: str = None,
        coupon: str = None,
        customer: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List all Promotion Codes.

        Args:
            active: Filter by active status.
            code: Filter by customer-facing code string.
            coupon: Filter by coupon ID.
            customer: Filter by customer ID.
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
        params = {}
        if active is not None: params["active"] = str(active).lower()
        if code: params["code"] = code
        if coupon: params["coupon"] = coupon
        if customer: params["customer"] = customer
        if limit is not None: params["limit"] = limit
        if starting_after: params["starting_after"] = starting_after
        if ending_before: params["ending_before"] = ending_before
        return _req("GET", "/v1/promotion_codes", params=params)
