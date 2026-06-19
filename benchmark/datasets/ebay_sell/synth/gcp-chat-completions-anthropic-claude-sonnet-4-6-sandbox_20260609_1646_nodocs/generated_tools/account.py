"""
eBay Sell Account API tools.
Covers: fulfillment policies, payment policies, return policies,
        sales tax, custom policies, programs, privileges, subscriptions.
"""

from typing import Optional
from auth import api_get, api_post, api_put, api_delete


# ---------------------------------------------------------------------------
# Fulfillment Policies
# ---------------------------------------------------------------------------

def get_fulfillment_policies(marketplace_id: str) -> dict:
    """Get all fulfillment policies for a marketplace."""
    return api_get("/sell/account/v1/fulfillment_policy",
                   params={"marketplace_id": marketplace_id})


def get_fulfillment_policy(fulfillment_policy_id: str) -> dict:
    """Get a fulfillment policy by ID."""
    return api_get(f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}")


def get_fulfillment_policy_by_name(marketplace_id: str, name: str) -> dict:
    """Get a fulfillment policy by name."""
    return api_get("/sell/account/v1/fulfillment_policy/get_by_policy_name",
                   params={"marketplace_id": marketplace_id, "name": name})


def create_fulfillment_policy(body: dict) -> dict:
    """
    Create a fulfillment policy.

    body fields:
      name: str
      marketplaceId: str
      categoryTypes: list of dicts with name (e.g. "ALL_EXCLUDING_MOTORS_VEHICLES")
      handlingTime: dict with unit and value
      shippingOptions: list of dicts with costType, optionType, shippingServices
      globalShipping: bool
      pickupDropOff: bool
      freightShipping: bool
    """
    return api_post("/sell/account/v1/fulfillment_policy", body=body)


def update_fulfillment_policy(fulfillment_policy_id: str, body: dict) -> dict:
    """Update a fulfillment policy."""
    return api_put(f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}", body=body)


def delete_fulfillment_policy(fulfillment_policy_id: str) -> dict:
    """Delete a fulfillment policy."""
    return api_delete(f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}")


# ---------------------------------------------------------------------------
# Payment Policies
# ---------------------------------------------------------------------------

def get_payment_policies(marketplace_id: str) -> dict:
    """Get all payment policies for a marketplace."""
    return api_get("/sell/account/v1/payment_policy",
                   params={"marketplace_id": marketplace_id})


def get_payment_policy(payment_policy_id: str) -> dict:
    """Get a payment policy by ID."""
    return api_get(f"/sell/account/v1/payment_policy/{payment_policy_id}")


def get_payment_policy_by_name(marketplace_id: str, name: str) -> dict:
    """Get a payment policy by name."""
    return api_get("/sell/account/v1/payment_policy/get_by_policy_name",
                   params={"marketplace_id": marketplace_id, "name": name})


def create_payment_policy(body: dict) -> dict:
    """
    Create a payment policy.

    body fields:
      name: str
      marketplaceId: str
      categoryTypes: list of dicts
      paymentMethods: list of dicts with paymentMethodType
      immediatePay: bool
    """
    return api_post("/sell/account/v1/payment_policy", body=body)


def update_payment_policy(payment_policy_id: str, body: dict) -> dict:
    """Update a payment policy."""
    return api_put(f"/sell/account/v1/payment_policy/{payment_policy_id}", body=body)


def delete_payment_policy(payment_policy_id: str) -> dict:
    """Delete a payment policy."""
    return api_delete(f"/sell/account/v1/payment_policy/{payment_policy_id}")


# ---------------------------------------------------------------------------
# Return Policies
# ---------------------------------------------------------------------------

def get_return_policies(marketplace_id: str) -> dict:
    """Get all return policies for a marketplace."""
    return api_get("/sell/account/v1/return_policy",
                   params={"marketplace_id": marketplace_id})


def get_return_policy(return_policy_id: str) -> dict:
    """Get a return policy by ID."""
    return api_get(f"/sell/account/v1/return_policy/{return_policy_id}")


def get_return_policy_by_name(marketplace_id: str, name: str) -> dict:
    """Get a return policy by name."""
    return api_get("/sell/account/v1/return_policy/get_by_policy_name",
                   params={"marketplace_id": marketplace_id, "name": name})


def create_return_policy(body: dict) -> dict:
    """
    Create a return policy.

    body fields:
      name: str
      marketplaceId: str
      categoryTypes: list of dicts
      returnsAccepted: bool
      returnPeriod: dict with unit and value
      returnShippingCostPayer: str ("BUYER" or "SELLER")
      refundMethod: str (e.g. "MONEY_BACK")
      returnMethod: str (e.g. "EXCHANGE")
      internationalOverride: dict
    """
    return api_post("/sell/account/v1/return_policy", body=body)


def update_return_policy(return_policy_id: str, body: dict) -> dict:
    """Update a return policy."""
    return api_put(f"/sell/account/v1/return_policy/{return_policy_id}", body=body)


def delete_return_policy(return_policy_id: str) -> dict:
    """Delete a return policy."""
    return api_delete(f"/sell/account/v1/return_policy/{return_policy_id}")


# ---------------------------------------------------------------------------
# Sales Tax
# ---------------------------------------------------------------------------

def get_sales_taxes(marketplace_id: str) -> dict:
    """Get all sales tax entries for a marketplace."""
    return api_get("/sell/account/v1/sales_tax",
                   params={"marketplace_id": marketplace_id})


def get_sales_tax(country_code: str, jurisdiction_id: str) -> dict:
    """Get a sales tax entry for a specific jurisdiction."""
    return api_get(f"/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}")


def create_or_replace_sales_tax(country_code: str, jurisdiction_id: str, body: dict) -> dict:
    """
    Create or replace a sales tax entry.

    body fields:
      salesTaxPercentage: str (e.g. "7.5")
      shippingAndHandlingTaxed: bool
    """
    return api_put(f"/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}", body=body)


def delete_sales_tax(country_code: str, jurisdiction_id: str) -> dict:
    """Delete a sales tax entry."""
    return api_delete(f"/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}")


# ---------------------------------------------------------------------------
# Custom Policies
# ---------------------------------------------------------------------------

def get_custom_policies(marketplace_id: str, policy_types: Optional[str] = None) -> dict:
    """Get all custom policies for a marketplace."""
    params: dict = {"marketplace_id": marketplace_id}
    if policy_types:
        params["policy_types"] = policy_types
    return api_get("/sell/account/v1/custom_policy", params=params)


def get_custom_policy(custom_policy_id: str) -> dict:
    """Get a custom policy by ID."""
    return api_get(f"/sell/account/v1/custom_policy/{custom_policy_id}")


def create_custom_policy(body: dict) -> dict:
    """
    Create a custom policy.

    body fields:
      name: str
      label: str
      description: str
      policyType: str (e.g. "PRODUCT_COMPLIANCE", "TAKE_BACK")
    """
    return api_post("/sell/account/v1/custom_policy", body=body)


def update_custom_policy(custom_policy_id: str, body: dict) -> dict:
    """Update a custom policy."""
    return api_put(f"/sell/account/v1/custom_policy/{custom_policy_id}", body=body)


# ---------------------------------------------------------------------------
# Programs
# ---------------------------------------------------------------------------

def get_opted_in_programs() -> dict:
    """Get all seller programs the seller is opted into."""
    return api_get("/sell/account/v1/program/get_opted_in_programs")


def opt_in_to_program(body: dict) -> dict:
    """
    Opt into a seller program.

    body fields:
      programType: str (e.g. "OUT_OF_STOCK_CONTROL", "SELLING_POLICY_MANAGEMENT")
    """
    return api_post("/sell/account/v1/program/opt_in", body=body)


def opt_out_of_program(body: dict) -> dict:
    """
    Opt out of a seller program.

    body fields:
      programType: str
    """
    return api_post("/sell/account/v1/program/opt_out", body=body)


# ---------------------------------------------------------------------------
# Privileges & Subscriptions
# ---------------------------------------------------------------------------

def get_seller_privileges() -> dict:
    """Get the selling privileges of the authenticated seller."""
    return api_get("/sell/account/v1/privilege")


def get_subscriptions() -> dict:
    """Get all active subscriptions for the seller."""
    return api_get("/sell/account/v1/subscription")


# ---------------------------------------------------------------------------
# Advertising Rates (Rate Tables)
# ---------------------------------------------------------------------------

def get_rate_tables(country_code: Optional[str] = None) -> dict:
    """Get shipping rate tables, optionally filtered by country code."""
    params = {}
    if country_code:
        params["country_code"] = country_code
    return api_get("/sell/account/v1/rate_table", params=params or None)
