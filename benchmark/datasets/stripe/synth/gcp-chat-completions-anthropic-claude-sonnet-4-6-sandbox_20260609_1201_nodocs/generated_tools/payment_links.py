"""
Stripe Payment Links tools.
Endpoints covered:
  POST   /v1/payment_links
  GET    /v1/payment_links/{id}
  POST   /v1/payment_links/{id}
  GET    /v1/payment_links/{id}/line_items
  GET    /v1/payment_links
"""

from mcp.server.fastmcp import FastMCP
from .client import stripe_request


def register(mcp: FastMCP):

    @mcp.tool()
    def create_payment_link(
        line_items: list,
        allow_promotion_codes: bool = None,
        application_fee_amount: int = None,
        application_fee_percent: float = None,
        billing_address_collection: str = None,
        currency: str = None,
        customer_creation: str = None,
        metadata: dict = None,
        on_behalf_of: str = None,
        payment_method_types: list = None,
        phone_number_collection_enabled: bool = None,
        shipping_address_collection_allowed_countries: list = None,
        submit_type: str = None,
        subscription_data_trial_period_days: int = None,
        after_completion_type: str = None,
        after_completion_redirect_url: str = None,
    ) -> dict:
        """
        Create a Payment Link.
        line_items: list of dicts with 'price' and 'quantity'.
        submit_type: auto | pay | book | donate
        customer_creation: always | if_required
        """
        data = {}
        for i, item in enumerate(line_items):
            if "price" in item:
                data[f"line_items[{i}][price]"] = item["price"]
            if "quantity" in item:
                data[f"line_items[{i}][quantity]"] = item["quantity"]
        if allow_promotion_codes is not None:
            data["allow_promotion_codes"] = str(allow_promotion_codes).lower()
        if application_fee_amount is not None:
            data["application_fee_amount"] = application_fee_amount
        if application_fee_percent is not None:
            data["application_fee_percent"] = application_fee_percent
        if billing_address_collection:
            data["billing_address_collection"] = billing_address_collection
        if currency:
            data["currency"] = currency
        if customer_creation:
            data["customer_creation"] = customer_creation
        if on_behalf_of:
            data["on_behalf_of"] = on_behalf_of
        if payment_method_types:
            for i, pm in enumerate(payment_method_types):
                data[f"payment_method_types[{i}]"] = pm
        if phone_number_collection_enabled is not None:
            data["phone_number_collection[enabled]"] = str(phone_number_collection_enabled).lower()
        if shipping_address_collection_allowed_countries:
            for i, c in enumerate(shipping_address_collection_allowed_countries):
                data[f"shipping_address_collection[allowed_countries][{i}]"] = c
        if submit_type:
            data["submit_type"] = submit_type
        if subscription_data_trial_period_days is not None:
            data["subscription_data[trial_period_days]"] = subscription_data_trial_period_days
        if after_completion_type:
            data["after_completion[type]"] = after_completion_type
        if after_completion_redirect_url:
            data["after_completion[redirect][url]"] = after_completion_redirect_url
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", "/v1/payment_links", data=data)

    @mcp.tool()
    def get_payment_link(payment_link_id: str) -> dict:
        """Retrieve a Payment Link by ID."""
        return stripe_request("GET", f"/v1/payment_links/{payment_link_id}")

    @mcp.tool()
    def update_payment_link(
        payment_link_id: str,
        active: bool = None,
        line_items: list = None,
        allow_promotion_codes: bool = None,
        metadata: dict = None,
        payment_method_types: list = None,
        after_completion_type: str = None,
        after_completion_redirect_url: str = None,
    ) -> dict:
        """Update a Payment Link."""
        data = {}
        if active is not None:
            data["active"] = str(active).lower()
        if line_items:
            for i, item in enumerate(line_items):
                if "id" in item:
                    data[f"line_items[{i}][id]"] = item["id"]
                if "quantity" in item:
                    data[f"line_items[{i}][quantity]"] = item["quantity"]
        if allow_promotion_codes is not None:
            data["allow_promotion_codes"] = str(allow_promotion_codes).lower()
        if payment_method_types:
            for i, pm in enumerate(payment_method_types):
                data[f"payment_method_types[{i}]"] = pm
        if after_completion_type:
            data["after_completion[type]"] = after_completion_type
        if after_completion_redirect_url:
            data["after_completion[redirect][url]"] = after_completion_redirect_url
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", f"/v1/payment_links/{payment_link_id}", data=data)

    @mcp.tool()
    def list_payment_link_line_items(
        payment_link_id: str,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List line items for a Payment Link."""
        params = {}
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return stripe_request("GET", f"/v1/payment_links/{payment_link_id}/line_items", params=params)

    @mcp.tool()
    def list_payment_links(
        active: bool = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List Payment Links."""
        params = {}
        if active is not None:
            params["active"] = str(active).lower()
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return stripe_request("GET", "/v1/payment_links", params=params)
