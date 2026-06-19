"""
Stripe Coupons & Promotion Codes tools.
Endpoints covered:
  POST   /v1/coupons
  GET    /v1/coupons/{id}
  POST   /v1/coupons/{id}
  DELETE /v1/coupons/{id}
  GET    /v1/coupons
  POST   /v1/promotion_codes
  GET    /v1/promotion_codes/{id}
  POST   /v1/promotion_codes/{id}
  GET    /v1/promotion_codes
"""

from mcp.server.fastmcp import FastMCP
from .client import stripe_request


def register(mcp: FastMCP):

    # ── Coupons ────────────────────────────────────────────────────────────────

    @mcp.tool()
    def create_coupon(
        id: str = None,
        duration: str = "once",
        amount_off: int = None,
        percent_off: float = None,
        currency: str = None,
        duration_in_months: int = None,
        max_redemptions: int = None,
        name: str = None,
        redeem_by: int = None,
        applies_to_products: list = None,
        metadata: dict = None,
    ) -> dict:
        """
        Create a Coupon.
        duration: forever | once | repeating
        Provide either amount_off (with currency) or percent_off.
        """
        data = {"duration": duration}
        if id:
            data["id"] = id
        if amount_off is not None:
            data["amount_off"] = amount_off
        if percent_off is not None:
            data["percent_off"] = percent_off
        if currency:
            data["currency"] = currency
        if duration_in_months is not None:
            data["duration_in_months"] = duration_in_months
        if max_redemptions is not None:
            data["max_redemptions"] = max_redemptions
        if name:
            data["name"] = name
        if redeem_by is not None:
            data["redeem_by"] = redeem_by
        if applies_to_products:
            for i, p in enumerate(applies_to_products):
                data[f"applies_to[products][{i}]"] = p
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", "/v1/coupons", data=data)

    @mcp.tool()
    def get_coupon(coupon_id: str) -> dict:
        """Retrieve a Coupon by ID."""
        return stripe_request("GET", f"/v1/coupons/{coupon_id}")

    @mcp.tool()
    def update_coupon(
        coupon_id: str,
        name: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update a Coupon's name or metadata."""
        data = {}
        if name:
            data["name"] = name
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", f"/v1/coupons/{coupon_id}", data=data)

    @mcp.tool()
    def delete_coupon(coupon_id: str) -> dict:
        """Delete a Coupon."""
        return stripe_request("DELETE", f"/v1/coupons/{coupon_id}")

    @mcp.tool()
    def list_coupons(
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
        created_gte: int = None,
        created_lte: int = None,
    ) -> dict:
        """List Coupons."""
        params = {}
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        if created_gte is not None:
            params["created[gte]"] = created_gte
        if created_lte is not None:
            params["created[lte]"] = created_lte
        return stripe_request("GET", "/v1/coupons", params=params)

    # ── Promotion Codes ────────────────────────────────────────────────────────

    @mcp.tool()
    def create_promotion_code(
        coupon: str,
        code: str = None,
        active: bool = None,
        customer: str = None,
        expires_at: int = None,
        max_redemptions: int = None,
        restrictions_first_time_transaction: bool = None,
        restrictions_minimum_amount: int = None,
        restrictions_minimum_amount_currency: str = None,
        metadata: dict = None,
    ) -> dict:
        """Create a Promotion Code for a Coupon."""
        data = {"coupon": coupon}
        if code:
            data["code"] = code
        if active is not None:
            data["active"] = str(active).lower()
        if customer:
            data["customer"] = customer
        if expires_at is not None:
            data["expires_at"] = expires_at
        if max_redemptions is not None:
            data["max_redemptions"] = max_redemptions
        if restrictions_first_time_transaction is not None:
            data["restrictions[first_time_transaction]"] = str(restrictions_first_time_transaction).lower()
        if restrictions_minimum_amount is not None:
            data["restrictions[minimum_amount]"] = restrictions_minimum_amount
        if restrictions_minimum_amount_currency:
            data["restrictions[minimum_amount_currency]"] = restrictions_minimum_amount_currency
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", "/v1/promotion_codes", data=data)

    @mcp.tool()
    def get_promotion_code(promotion_code_id: str) -> dict:
        """Retrieve a Promotion Code by ID."""
        return stripe_request("GET", f"/v1/promotion_codes/{promotion_code_id}")

    @mcp.tool()
    def update_promotion_code(
        promotion_code_id: str,
        active: bool = None,
        metadata: dict = None,
    ) -> dict:
        """Update a Promotion Code (active status or metadata)."""
        data = {}
        if active is not None:
            data["active"] = str(active).lower()
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", f"/v1/promotion_codes/{promotion_code_id}", data=data)

    @mcp.tool()
    def list_promotion_codes(
        coupon: str = None,
        customer: str = None,
        code: str = None,
        active: bool = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List Promotion Codes."""
        params = {}
        if coupon:
            params["coupon"] = coupon
        if customer:
            params["customer"] = customer
        if code:
            params["code"] = code
        if active is not None:
            params["active"] = str(active).lower()
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return stripe_request("GET", "/v1/promotion_codes", params=params)
