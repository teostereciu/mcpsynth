"""Tools for Stripe Customers API."""
import os
import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://api.stripe.com"

def _get_headers():
    api_key = os.environ.get("STRIPE_API_KEY", "")
    return {"Authorization": f"Bearer {api_key}"}

def _req(method, path, **kwargs):
    try:
        resp = requests.request(method, f"{BASE_URL}{path}", headers=_get_headers(), **kwargs)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def register_customer_tools(mcp: FastMCP):

    @mcp.tool()
    def create_customer(
        email: str = None,
        name: str = None,
        phone: str = None,
        description: str = None,
        payment_method: str = None,
        metadata: dict = None,
    ) -> dict:
        """Create a new Stripe Customer.

        Args:
            email: Customer's email address (up to 512 chars).
            name: Customer's full name or business name.
            phone: Customer's phone number.
            description: Arbitrary string attached to the object.
            payment_method: ID of the PaymentMethod to attach.
            metadata: Key-value pairs to attach to the object.
        """
        data = {}
        if email:
            data["email"] = email
        if name:
            data["name"] = name
        if phone:
            data["phone"] = phone
        if description:
            data["description"] = description
        if payment_method:
            data["payment_method"] = payment_method
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", "/v1/customers", data=data)

    @mcp.tool()
    def retrieve_customer(customer_id: str) -> dict:
        """Retrieve a Customer by ID.

        Args:
            customer_id: The ID of the customer (e.g. 'cus_...').
        """
        return _req("GET", f"/v1/customers/{customer_id}")

    @mcp.tool()
    def update_customer(
        customer_id: str,
        email: str = None,
        name: str = None,
        phone: str = None,
        description: str = None,
        default_source: str = None,
        metadata: dict = None,
    ) -> dict:
        """Update an existing Customer.

        Args:
            customer_id: The ID of the customer to update.
            email: Customer's email address.
            name: Customer's full name or business name.
            phone: Customer's phone number.
            description: Arbitrary string attached to the object.
            default_source: ID of the default payment source.
            metadata: Key-value pairs to attach to the object.
        """
        data = {}
        if email:
            data["email"] = email
        if name:
            data["name"] = name
        if phone:
            data["phone"] = phone
        if description:
            data["description"] = description
        if default_source:
            data["default_source"] = default_source
        if metadata:
            for k, v in metadata.items():
                data[f"metadata[{k}]"] = v
        return _req("POST", f"/v1/customers/{customer_id}", data=data)

    @mcp.tool()
    def delete_customer(customer_id: str) -> dict:
        """Permanently delete a Customer.

        Args:
            customer_id: The ID of the customer to delete.
        """
        return _req("DELETE", f"/v1/customers/{customer_id}")

    @mcp.tool()
    def list_customers(
        email: str = None,
        limit: int = None,
        starting_after: str = None,
        ending_before: str = None,
    ) -> dict:
        """List all Customers.

        Args:
            email: Filter customers by email address.
            limit: Number of objects to return (1-100).
            starting_after: Cursor for pagination (object ID).
            ending_before: Cursor for pagination (object ID).
        """
        params = {}
        if email:
            params["email"] = email
        if limit is not None:
            params["limit"] = limit
        if starting_after:
            params["starting_after"] = starting_after
        if ending_before:
            params["ending_before"] = ending_before
        return _req("GET", "/v1/customers", params=params)

    @mcp.tool()
    def list_customer_payment_methods(
        customer_id: str,
        type: str = None,
        limit: int = None,
    ) -> dict:
        """List PaymentMethods for a Customer.

        Args:
            customer_id: The ID of the customer.
            type: Filter by payment method type (e.g. 'card').
            limit: Number of objects to return (1-100).
        """
        params = {}
        if type:
            params["type"] = type
        if limit is not None:
            params["limit"] = limit
        return _req("GET", f"/v1/customers/{customer_id}/payment_methods", params=params)
