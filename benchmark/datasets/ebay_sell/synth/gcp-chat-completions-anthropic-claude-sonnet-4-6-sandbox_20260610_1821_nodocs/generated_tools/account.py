"""
eBay Sell Account API tools.
Covers: fulfillment policies, payment policies, return policies,
        seller profiles, programs, privileges, sales tax, subscription.
"""

from mcp.server.fastmcp import FastMCP
from .auth import ebay_request

mcp = FastMCP("ebay-account")

# ---------------------------------------------------------------------------
# Fulfillment Policies
# ---------------------------------------------------------------------------

@mcp.tool()
def get_fulfillment_policies(marketplace_id: str) -> dict:
    """
    Retrieve all fulfillment policies for a given marketplace.

    Args:
        marketplace_id: eBay marketplace ID, e.g. 'EBAY_US'.
    """
    return ebay_request(
        "GET",
        "/sell/account/v1/fulfillment_policy",
        params={"marketplace_id": marketplace_id},
    )


@mcp.tool()
def get_fulfillment_policy(fulfillment_policy_id: str) -> dict:
    """
    Retrieve a specific fulfillment policy by its ID.

    Args:
        fulfillment_policy_id: The unique identifier of the fulfillment policy.
    """
    return ebay_request(
        "GET",
        f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}",
    )


@mcp.tool()
def get_fulfillment_policy_by_name(marketplace_id: str, name: str) -> dict:
    """
    Retrieve a fulfillment policy by its name and marketplace.

    Args:
        marketplace_id: eBay marketplace ID, e.g. 'EBAY_US'.
        name: The name of the fulfillment policy.
    """
    return ebay_request(
        "GET",
        "/sell/account/v1/fulfillment_policy/get_by_policy_name",
        params={"marketplace_id": marketplace_id, "name": name},
    )


@mcp.tool()
def create_fulfillment_policy(policy: dict) -> dict:
    """
    Create a new fulfillment policy.

    Args:
        policy: Fulfillment policy object with name, marketplaceId,
                categoryTypes, handlingTime, shippingOptions, etc.
                Example: {
                  "name": "Standard Shipping",
                  "marketplaceId": "EBAY_US",
                  "categoryTypes": [{"name": "ALL_EXCLUDING_MOTORS_VEHICLES"}],
                  "handlingTime": {"value": 1, "unit": "DAY"},
                  "shippingOptions": [{
                    "optionType": "DOMESTIC",
                    "costType": "FLAT_RATE",
                    "shippingServices": [{
                      "shippingCarrierCode": "USPS",
                      "shippingServiceCode": "USPSPriority",
                      "shippingCost": {"value": "5.99", "currency": "USD"}
                    }]
                  }]
                }
    """
    return ebay_request("POST", "/sell/account/v1/fulfillment_policy", json=policy)


@mcp.tool()
def update_fulfillment_policy(fulfillment_policy_id: str, policy: dict) -> dict:
    """
    Update an existing fulfillment policy.

    Args:
        fulfillment_policy_id: The unique identifier of the policy to update.
        policy: Updated fulfillment policy object.
    """
    return ebay_request(
        "PUT",
        f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}",
        json=policy,
    )


@mcp.tool()
def delete_fulfillment_policy(fulfillment_policy_id: str) -> dict:
    """
    Delete a fulfillment policy.

    Args:
        fulfillment_policy_id: The unique identifier of the policy to delete.
    """
    return ebay_request(
        "DELETE",
        f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}",
    )


# ---------------------------------------------------------------------------
# Payment Policies
# ---------------------------------------------------------------------------

@mcp.tool()
def get_payment_policies(marketplace_id: str) -> dict:
    """
    Retrieve all payment policies for a given marketplace.

    Args:
        marketplace_id: eBay marketplace ID, e.g. 'EBAY_US'.
    """
    return ebay_request(
        "GET",
        "/sell/account/v1/payment_policy",
        params={"marketplace_id": marketplace_id},
    )


@mcp.tool()
def get_payment_policy(payment_policy_id: str) -> dict:
    """
    Retrieve a specific payment policy by its ID.

    Args:
        payment_policy_id: The unique identifier of the payment policy.
    """
    return ebay_request(
        "GET",
        f"/sell/account/v1/payment_policy/{payment_policy_id}",
    )


@mcp.tool()
def get_payment_policy_by_name(marketplace_id: str, name: str) -> dict:
    """
    Retrieve a payment policy by its name and marketplace.

    Args:
        marketplace_id: eBay marketplace ID, e.g. 'EBAY_US'.
        name: The name of the payment policy.
    """
    return ebay_request(
        "GET",
        "/sell/account/v1/payment_policy/get_by_policy_name",
        params={"marketplace_id": marketplace_id, "name": name},
    )


@mcp.tool()
def create_payment_policy(policy: dict) -> dict:
    """
    Create a new payment policy.

    Args:
        policy: Payment policy object with name, marketplaceId,
                categoryTypes, and paymentMethods fields.
    """
    return ebay_request("POST", "/sell/account/v1/payment_policy", json=policy)


@mcp.tool()
def update_payment_policy(payment_policy_id: str, policy: dict) -> dict:
    """
    Update an existing payment policy.

    Args:
        payment_policy_id: The unique identifier of the policy to update.
        policy: Updated payment policy object.
    """
    return ebay_request(
        "PUT",
        f"/sell/account/v1/payment_policy/{payment_policy_id}",
        json=policy,
    )


@mcp.tool()
def delete_payment_policy(payment_policy_id: str) -> dict:
    """
    Delete a payment policy.

    Args:
        payment_policy_id: The unique identifier of the policy to delete.
    """
    return ebay_request(
        "DELETE",
        f"/sell/account/v1/payment_policy/{payment_policy_id}",
    )


# ---------------------------------------------------------------------------
# Return Policies
# ---------------------------------------------------------------------------

@mcp.tool()
def get_return_policies(marketplace_id: str) -> dict:
    """
    Retrieve all return policies for a given marketplace.

    Args:
        marketplace_id: eBay marketplace ID, e.g. 'EBAY_US'.
    """
    return ebay_request(
        "GET",
        "/sell/account/v1/return_policy",
        params={"marketplace_id": marketplace_id},
    )


@mcp.tool()
def get_return_policy(return_policy_id: str) -> dict:
    """
    Retrieve a specific return policy by its ID.

    Args:
        return_policy_id: The unique identifier of the return policy.
    """
    return ebay_request(
        "GET",
        f"/sell/account/v1/return_policy/{return_policy_id}",
    )


@mcp.tool()
def get_return_policy_by_name(marketplace_id: str, name: str) -> dict:
    """
    Retrieve a return policy by its name and marketplace.

    Args:
        marketplace_id: eBay marketplace ID, e.g. 'EBAY_US'.
        name: The name of the return policy.
    """
    return ebay_request(
        "GET",
        "/sell/account/v1/return_policy/get_by_policy_name",
        params={"marketplace_id": marketplace_id, "name": name},
    )


@mcp.tool()
def create_return_policy(policy: dict) -> dict:
    """
    Create a new return policy.

    Args:
        policy: Return policy object with name, marketplaceId, categoryTypes,
                returnsAccepted, returnPeriod, refundMethod, etc.
                Example: {
                  "name": "30-Day Returns",
                  "marketplaceId": "EBAY_US",
                  "categoryTypes": [{"name": "ALL_EXCLUDING_MOTORS_VEHICLES"}],
                  "returnsAccepted": true,
                  "returnPeriod": {"value": 30, "unit": "DAY"},
                  "refundMethod": "MONEY_BACK",
                  "returnShippingCostPayer": "BUYER"
                }
    """
    return ebay_request("POST", "/sell/account/v1/return_policy", json=policy)


@mcp.tool()
def update_return_policy(return_policy_id: str, policy: dict) -> dict:
    """
    Update an existing return policy.

    Args:
        return_policy_id: The unique identifier of the policy to update.
        policy: Updated return policy object.
    """
    return ebay_request(
        "PUT",
        f"/sell/account/v1/return_policy/{return_policy_id}",
        json=policy,
    )


@mcp.tool()
def delete_return_policy(return_policy_id: str) -> dict:
    """
    Delete a return policy.

    Args:
        return_policy_id: The unique identifier of the policy to delete.
    """
    return ebay_request(
        "DELETE",
        f"/sell/account/v1/return_policy/{return_policy_id}",
    )


# ---------------------------------------------------------------------------
# Seller Programs
# ---------------------------------------------------------------------------

@mcp.tool()
def get_opted_in_programs() -> dict:
    """
    Retrieve all seller programs the seller is currently opted into
    (e.g. eBay Plus, eBay Green).
    """
    return ebay_request("GET", "/sell/account/v1/program/get_opted_in_programs")


@mcp.tool()
def opt_in_to_program(program_type: str) -> dict:
    """
    Opt the seller into a specific seller program.

    Args:
        program_type: The program to opt into, e.g. 'SELLING_POLICY_MANAGEMENT',
                      'EBAY_PLUS', 'OUT_OF_STOCK_CONTROL'.
    """
    return ebay_request(
        "POST",
        "/sell/account/v1/program/opt_in",
        json={"programType": program_type},
    )


@mcp.tool()
def opt_out_of_program(program_type: str) -> dict:
    """
    Opt the seller out of a specific seller program.

    Args:
        program_type: The program to opt out of.
    """
    return ebay_request(
        "POST",
        "/sell/account/v1/program/opt_out",
        json={"programType": program_type},
    )


# ---------------------------------------------------------------------------
# Privileges
# ---------------------------------------------------------------------------

@mcp.tool()
def get_privileges() -> dict:
    """
    Retrieve the seller's current privileges and selling limits.
    """
    return ebay_request("GET", "/sell/account/v1/privilege")


# ---------------------------------------------------------------------------
# Sales Tax
# ---------------------------------------------------------------------------

@mcp.tool()
def get_sales_taxes(marketplace_id: str) -> dict:
    """
    Retrieve all sales tax entries for a given marketplace.

    Args:
        marketplace_id: eBay marketplace ID, e.g. 'EBAY_US'.
    """
    return ebay_request(
        "GET",
        "/sell/account/v1/sales_tax",
        params={"marketplace_id": marketplace_id},
    )


@mcp.tool()
def get_sales_tax(marketplace_id: str, country_code: str, jurisdiction_id: str) -> dict:
    """
    Retrieve a specific sales tax entry.

    Args:
        marketplace_id: eBay marketplace ID, e.g. 'EBAY_US'.
        country_code: Two-letter country code, e.g. 'US'.
        jurisdiction_id: State/province code, e.g. 'CA' for California.
    """
    return ebay_request(
        "GET",
        f"/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}",
        params={"marketplace_id": marketplace_id},
    )


@mcp.tool()
def create_or_replace_sales_tax(
    country_code: str, jurisdiction_id: str, sales_tax: dict
) -> dict:
    """
    Create or replace a sales tax entry for a jurisdiction.

    Args:
        country_code: Two-letter country code, e.g. 'US'.
        jurisdiction_id: State/province code, e.g. 'CA'.
        sales_tax: Sales tax object with 'salesTaxPercentage' and
                   'shippingAndHandlingTaxed' fields.
    """
    return ebay_request(
        "PUT",
        f"/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}",
        json=sales_tax,
    )


@mcp.tool()
def delete_sales_tax(country_code: str, jurisdiction_id: str) -> dict:
    """
    Delete a sales tax entry for a jurisdiction.

    Args:
        country_code: Two-letter country code, e.g. 'US'.
        jurisdiction_id: State/province code, e.g. 'CA'.
    """
    return ebay_request(
        "DELETE",
        f"/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}",
    )


# ---------------------------------------------------------------------------
# Subscriptions
# ---------------------------------------------------------------------------

@mcp.tool()
def get_subscriptions(limit: int = 20, offset: int = 0) -> dict:
    """
    Retrieve the seller's active eBay store subscriptions.

    Args:
        limit: Number of subscriptions to return (default 20).
        offset: Pagination offset (default 0).
    """
    return ebay_request(
        "GET",
        "/sell/account/v1/subscription",
        params={"limit": limit, "offset": offset},
    )


# ---------------------------------------------------------------------------
# Custom Policies
# ---------------------------------------------------------------------------

@mcp.tool()
def get_custom_policies(marketplace_id: str, policy_types: str | None = None) -> dict:
    """
    Retrieve custom policies for a marketplace.

    Args:
        marketplace_id: eBay marketplace ID, e.g. 'EBAY_US'.
        policy_types: Comma-separated policy types to filter by,
                      e.g. 'PRODUCT_COMPLIANCE,TAKE_BACK'.
    """
    params: dict = {"marketplace_id": marketplace_id}
    if policy_types:
        params["policy_types"] = policy_types
    return ebay_request("GET", "/sell/account/v1/custom_policy", params=params)


@mcp.tool()
def get_custom_policy(custom_policy_id: str, marketplace_id: str) -> dict:
    """
    Retrieve a specific custom policy by its ID.

    Args:
        custom_policy_id: The unique identifier of the custom policy.
        marketplace_id: eBay marketplace ID, e.g. 'EBAY_US'.
    """
    return ebay_request(
        "GET",
        f"/sell/account/v1/custom_policy/{custom_policy_id}",
        params={"marketplace_id": marketplace_id},
    )


@mcp.tool()
def create_custom_policy(policy: dict) -> dict:
    """
    Create a new custom policy (e.g. product compliance or take-back).

    Args:
        policy: Custom policy object with name, label, description,
                policyType, and marketplaceId fields.
    """
    return ebay_request("POST", "/sell/account/v1/custom_policy", json=policy)


@mcp.tool()
def update_custom_policy(custom_policy_id: str, policy: dict) -> dict:
    """
    Update an existing custom policy.

    Args:
        custom_policy_id: The unique identifier of the custom policy.
        policy: Updated custom policy object.
    """
    return ebay_request(
        "PUT",
        f"/sell/account/v1/custom_policy/{custom_policy_id}",
        json=policy,
    )
