"""
Stripe Payment Methods tools.
Endpoints covered:
  POST   /v1/payment_methods
  GET    /v1/payment_methods/{id}
  POST   /v1/payment_methods/{id}
  POST   /v1/payment_methods/{id}/attach
  POST   /v1/payment_methods/{id}/detach
  GET    /v1/payment_methods
"""

from mcp.server.fastmcp import FastMCP
from .client import stripe_request


def register(mcp: FastMCP):

    @mcp.tool()
    def create_payment_method(
        type: str,
        card_number: str = None,
        card_exp_month: int = None,
        card_exp_year: int = None,
        card_cvc: str = None,
        card_token: str = None,
        billing_details_name: str = None,
        billing_details_email: str = None,
        billing_details_phone: str = None,
        billing_details_address_line1: str = None,
        billing_details_address_city: str = None,
        billing_details_address_state: str = None,
        billing_details_address_postal_code: str = None,
        billing_details_address_country: str = None,
        metadata: dict = None,
    ) -> dict:
        """
        Create a PaymentMethod.
        type: card | us_bank_account | sepa_debit | ideal | etc.
        For card type, provide card_number/exp_month/exp_year/cvc or card_token.
        """
        data = {"type": type}
        if card_token:
            data["card[token]"] = card_token
        else:
            if card_number:
                data["card[number]"] = card_number
            if card_exp_month is not None:
                data["card[exp_month]"] = card_exp_month
            if card_exp_year is not None:
                data["card[exp_year]"] = card_exp_year
            if card_cvc:
                data["card[cvc]"] = card_cvc
        if billing_details_name:
            data["billing_details[name]"] = billing_details_name
        if billing_details_email:
            data["billing_details[email]"] = billing_details_email
        if billing_details_phone:
            data["billing_details[phone]"] = billing_details_phone
        if billing_details_address_line1:
            data["billing_details[address][line1]"] = billing_details_address_line1
        if billing_details_address_city:
            data["billing_details[address][city]"] = billing_details_address_city
        if billing_details_address_state:
            data["billing_details[address][state]"] = billing_details_address_state
        if billing_details_address_postal_code:
            data["billing_details[address][postal_code]"] = billing_details_address_postal_code
        if billing_details_address_country:
            data["billing_details[address][country]"] = billing_details_address_country
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", "/v1/payment_methods", data=data)

    @mcp.tool()
    def get_payment_method(payment_method_id: str) -> dict:
        """Retrieve a PaymentMethod by ID."""
        return stripe_request("GET", f"/v1/payment_methods/{payment_method_id}")

    @mcp.tool()
    def update_payment_method(
        payment_method_id: str,
        billing_details_name: str = None,
        billing_details_email: str = None,
        billing_details_phone: str = None,
        card_exp_month: int = None,
        card_exp_year: int = None,
        metadata: dict = None,
    ) -> dict:
        """Update a PaymentMethod's billing details or card expiry."""
        data = {}
        if billing_details_name:
            data["billing_details[name]"] = billing_details_name
        if billing_details_email:
            data["billing_details[email]"] = billing_details_email
        if billing_details_phone:
            data["billing_details[phone]"] = billing_details_phone
        if card_exp_month is not None:
            data["card[exp_month]"] = card_exp_month
        if card_exp_year is not None:
            data["card[exp_year]"] = card_exp_year
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return stripe_request("POST", f"/v1/payment_methods/{payment_method_id}", data=data)

    @mcp.tool()
    def attach_payment_method(payment_method_id: str, customer: str) -> dict:
        """Attach a PaymentMethod to a Customer."""
        return stripe_request(
            "POST",
            f"/v1/payment_methods/{payment_method_id}/attach",
            data={"customer": customer},
        )

    @mcp.tool()
    def detach_payment_method(payment_method_id: str) -> dict:
        """Detach a PaymentMethod from its Customer."""
        return stripe_request("POST", f"/v1/payment_methods/{payment_method_id}/detach")

    @mcp.tool()
    def list_payment_methods(
        customer: str = None,
        type: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List PaymentMethods. Provide customer to list attached methods."""
        params = {}
        if customer:
            params["customer"] = customer
        if type:
            params["type"] = type
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return stripe_request("GET", "/v1/payment_methods", params=params)
