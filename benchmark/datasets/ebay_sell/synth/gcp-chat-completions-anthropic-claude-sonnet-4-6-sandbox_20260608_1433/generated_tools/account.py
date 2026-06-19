"""eBay Sell Account API tools."""
from typing import Optional
from .client import get_client


def create_fulfillment_policy(body: dict) -> dict:
    """Create a new fulfillment policy for an eBay marketplace."""
    client = get_client()
    return client.request("POST", "/sell/account/v1/fulfillment_policy/", json=body)


def get_fulfillment_policies(marketplace_id: str) -> dict:
    """Retrieve all fulfillment policies for a marketplace."""
    client = get_client()
    return client.request("GET", "/sell/account/v1/fulfillment_policy", params={"marketplace_id": marketplace_id})


def get_fulfillment_policy(fulfillment_policy_id: str) -> dict:
    """Retrieve a specific fulfillment policy by ID."""
    client = get_client()
    return client.request("GET", f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}")


def get_fulfillment_policy_by_name(marketplace_id: str, name: str) -> dict:
    """Retrieve a fulfillment policy by name and marketplace."""
    client = get_client()
    return client.request("GET", "/sell/account/v1/fulfillment_policy/get_by_policy_name",
                          params={"marketplace_id": marketplace_id, "name": name})


def update_fulfillment_policy(fulfillment_policy_id: str, body: dict) -> dict:
    """Update an existing fulfillment policy."""
    client = get_client()
    return client.request("PUT", f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}", json=body)


def delete_fulfillment_policy(fulfillment_policy_id: str) -> dict:
    """Delete a fulfillment policy."""
    client = get_client()
    return client.request("DELETE", f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}")


def create_payment_policy(body: dict) -> dict:
    """Create a new payment policy."""
    client = get_client()
    return client.request("POST", "/sell/account/v1/payment_policy", json=body)


def get_payment_policies(marketplace_id: str) -> dict:
    """Retrieve all payment policies for a marketplace."""
    client = get_client()
    return client.request("GET", "/sell/account/v1/payment_policy", params={"marketplace_id": marketplace_id})


def get_payment_policy(payment_policy_id: str) -> dict:
    """Retrieve a specific payment policy by ID."""
    client = get_client()
    return client.request("GET", f"/sell/account/v1/payment_policy/{payment_policy_id}")


def get_payment_policy_by_name(marketplace_id: str, name: str) -> dict:
    """Retrieve a payment policy by name and marketplace."""
    client = get_client()
    return client.request("GET", "/sell/account/v1/payment_policy/get_by_policy_name",
                          params={"marketplace_id": marketplace_id, "name": name})


def update_payment_policy(payment_policy_id: str, body: dict) -> dict:
    """Update an existing payment policy."""
    client = get_client()
    return client.request("PUT", f"/sell/account/v1/payment_policy/{payment_policy_id}", json=body)


def delete_payment_policy(payment_policy_id: str) -> dict:
    """Delete a payment policy."""
    client = get_client()
    return client.request("DELETE", f"/sell/account/v1/payment_policy/{payment_policy_id}")


def create_return_policy(body: dict) -> dict:
    """Create a new return policy."""
    client = get_client()
    return client.request("POST", "/sell/account/v1/return_policy", json=body)


def get_return_policies(marketplace_id: str) -> dict:
    """Retrieve all return policies for a marketplace."""
    client = get_client()
    return client.request("GET", "/sell/account/v1/return_policy", params={"marketplace_id": marketplace_id})


def get_return_policy(return_policy_id: str) -> dict:
    """Retrieve a specific return policy by ID."""
    client = get_client()
    return client.request("GET", f"/sell/account/v1/return_policy/{return_policy_id}")


def get_return_policy_by_name(marketplace_id: str, name: str) -> dict:
    """Retrieve a return policy by name and marketplace."""
    client = get_client()
    return client.request("GET", "/sell/account/v1/return_policy/get_by_policy_name",
                          params={"marketplace_id": marketplace_id, "name": name})


def update_return_policy(return_policy_id: str, body: dict) -> dict:
    """Update an existing return policy."""
    client = get_client()
    return client.request("PUT", f"/sell/account/v1/return_policy/{return_policy_id}", json=body)


def delete_return_policy(return_policy_id: str) -> dict:
    """Delete a return policy."""
    client = get_client()
    return client.request("DELETE", f"/sell/account/v1/return_policy/{return_policy_id}")


def get_privileges() -> dict:
    """Retrieve the seller's current set of privileges."""
    client = get_client()
    return client.request("GET", "/sell/account/v1/privilege")


def get_opted_in_programs() -> dict:
    """Get a list of seller programs the seller has opted into."""
    client = get_client()
    return client.request("GET", "/sell/account/v1/program/get_opted_in_programs")


def opt_in_to_program(body: dict) -> dict:
    """Opt the seller into an eBay seller program."""
    client = get_client()
    return client.request("POST", "/sell/account/v1/program/opt_in", json=body)


def opt_out_of_program(body: dict) -> dict:
    """Opt the seller out of an eBay seller program."""
    client = get_client()
    return client.request("POST", "/sell/account/v1/program/opt_out", json=body)


def get_sales_taxes(country_code: str) -> dict:
    """Retrieve all sales tax table entries for a country."""
    client = get_client()
    return client.request("GET", "/sell/account/v1/sales_tax", params={"country_code": country_code})


def get_sales_tax(country_code: str, jurisdiction_id: str) -> dict:
    """Retrieve a specific sales tax table entry."""
    client = get_client()
    return client.request("GET", f"/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}")


def create_or_replace_sales_tax(country_code: str, jurisdiction_id: str, body: dict) -> dict:
    """Create or update a sales tax table entry for a jurisdiction."""
    client = get_client()
    return client.request("PUT", f"/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}", json=body)


def delete_sales_tax(country_code: str, jurisdiction_id: str) -> dict:
    """Delete a sales tax table entry for a jurisdiction."""
    client = get_client()
    return client.request("DELETE", f"/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}")


def get_rate_tables(country_code: Optional[str] = None) -> dict:
    """Retrieve seller's shipping rate tables."""
    client = get_client()
    params = {}
    if country_code:
        params["country_code"] = country_code
    return client.request("GET", "/sell/account/v1/rate_table", params=params)


def get_subscription() -> dict:
    """Retrieve a list of subscriptions associated with the seller account."""
    client = get_client()
    return client.request("GET", "/sell/account/v1/subscription")


def create_custom_policy(body: dict) -> dict:
    """Create a new custom policy for regulatory compliance."""
    client = get_client()
    return client.request("POST", "/sell/account/v1/custom_policy/", json=body)


def get_custom_policies(policy_types: Optional[str] = None) -> dict:
    """Retrieve the list of custom policies defined for a seller's account."""
    client = get_client()
    params = {}
    if policy_types:
        params["policy_types"] = policy_types
    return client.request("GET", "/sell/account/v1/custom_policy/", params=params)


def get_custom_policy(custom_policy_id: str) -> dict:
    """Retrieve a specific custom policy by ID."""
    client = get_client()
    return client.request("GET", f"/sell/account/v1/custom_policy/{custom_policy_id}")


def update_custom_policy(custom_policy_id: str, body: dict) -> dict:
    """Update an existing custom policy."""
    client = get_client()
    return client.request("PUT", f"/sell/account/v1/custom_policy/{custom_policy_id}", json=body)
