"""
eBay Sell Account API tools.
Covers: fulfillment policies, payment policies, return policies,
        sales tax, shipping rate tables, programs, privileges, subscriptions.
"""

from mcp.server.fastmcp import FastMCP
from .auth import api_get, api_post, api_put, api_delete

mcp = FastMCP("ebay-account")


# ── Fulfillment Policies ─────────────────────────────────────────────────────

@mcp.tool()
def get_fulfillment_policies(marketplace_id: str) -> dict:
    """
    Retrieve all fulfillment policies for a marketplace.

    Args:
        marketplace_id: eBay marketplace ID (e.g. EBAY_US).
    """
    return api_get("/sell/account/v1/fulfillment_policy",
                   params={"marketplace_id": marketplace_id})


@mcp.tool()
def get_fulfillment_policy(fulfillment_policy_id: str) -> dict:
    """Retrieve a fulfillment policy by ID."""
    return api_get(f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}")


@mcp.tool()
def get_fulfillment_policy_by_name(marketplace_id: str, name: str) -> dict:
    """
    Retrieve a fulfillment policy by name.

    Args:
        marketplace_id: eBay marketplace ID.
        name: Policy name.
    """
    return api_get("/sell/account/v1/fulfillment_policy/get_by_policy_name",
                   params={"marketplace_id": marketplace_id, "name": name})


@mcp.tool()
def create_fulfillment_policy(marketplace_id: str, name: str,
                               handling_time: dict,
                               shipping_options: list[dict],
                               category_types: list[dict],
                               description: str | None = None,
                               global_shipping: bool = False,
                               pickup_drop_off: bool = False,
                               freight_shipping: bool = False) -> dict:
    """
    Create a new fulfillment policy.

    Args:
        marketplace_id: eBay marketplace ID.
        name: Policy name.
        handling_time: Dict with value and unit (e.g. {"value": 1, "unit": "DAY"}).
        shipping_options: List of shipping option dicts.
        category_types: List of category type dicts (e.g. [{"name": "ALL_EXCLUDING_MOTORS_VEHICLES"}]).
        description: Optional description.
        global_shipping: Enable eBay Global Shipping Program.
        pickup_drop_off: Enable Click & Collect.
        freight_shipping: Enable freight shipping.
    """
    body: dict = {
        "marketplaceId": marketplace_id,
        "name": name,
        "handlingTime": handling_time,
        "shippingOptions": shipping_options,
        "categoryTypes": category_types,
        "globalShipping": global_shipping,
        "pickupDropOff": pickup_drop_off,
        "freightShipping": freight_shipping,
    }
    if description:
        body["description"] = description
    return api_post("/sell/account/v1/fulfillment_policy", body=body)


@mcp.tool()
def update_fulfillment_policy(fulfillment_policy_id: str,
                               marketplace_id: str,
                               name: str,
                               handling_time: dict,
                               shipping_options: list[dict],
                               category_types: list[dict],
                               description: str | None = None) -> dict:
    """
    Update an existing fulfillment policy.

    Args:
        fulfillment_policy_id: ID of the policy to update.
        marketplace_id: eBay marketplace ID.
        name: Policy name.
        handling_time: Handling time dict.
        shipping_options: List of shipping option dicts.
        category_types: List of category type dicts.
        description: Optional description.
    """
    body: dict = {
        "marketplaceId": marketplace_id,
        "name": name,
        "handlingTime": handling_time,
        "shippingOptions": shipping_options,
        "categoryTypes": category_types,
    }
    if description:
        body["description"] = description
    return api_put(f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}", body=body)


@mcp.tool()
def delete_fulfillment_policy(fulfillment_policy_id: str) -> dict:
    """Delete a fulfillment policy by ID."""
    return api_delete(f"/sell/account/v1/fulfillment_policy/{fulfillment_policy_id}")


# ── Payment Policies ─────────────────────────────────────────────────────────

@mcp.tool()
def get_payment_policies(marketplace_id: str) -> dict:
    """Retrieve all payment policies for a marketplace."""
    return api_get("/sell/account/v1/payment_policy",
                   params={"marketplace_id": marketplace_id})


@mcp.tool()
def get_payment_policy(payment_policy_id: str) -> dict:
    """Retrieve a payment policy by ID."""
    return api_get(f"/sell/account/v1/payment_policy/{payment_policy_id}")


@mcp.tool()
def get_payment_policy_by_name(marketplace_id: str, name: str) -> dict:
    """Retrieve a payment policy by name."""
    return api_get("/sell/account/v1/payment_policy/get_by_policy_name",
                   params={"marketplace_id": marketplace_id, "name": name})


@mcp.tool()
def create_payment_policy(marketplace_id: str, name: str,
                           category_types: list[dict],
                           payment_methods: list[dict] | None = None,
                           description: str | None = None,
                           immediate_pay: bool = False) -> dict:
    """
    Create a new payment policy.

    Args:
        marketplace_id: eBay marketplace ID.
        name: Policy name.
        category_types: List of category type dicts.
        payment_methods: List of accepted payment method dicts.
        description: Optional description.
        immediate_pay: Require immediate payment.
    """
    body: dict = {
        "marketplaceId": marketplace_id,
        "name": name,
        "categoryTypes": category_types,
        "immediatePay": immediate_pay,
    }
    if payment_methods:
        body["paymentMethods"] = payment_methods
    if description:
        body["description"] = description
    return api_post("/sell/account/v1/payment_policy", body=body)


@mcp.tool()
def update_payment_policy(payment_policy_id: str, marketplace_id: str,
                           name: str, category_types: list[dict],
                           payment_methods: list[dict] | None = None,
                           description: str | None = None,
                           immediate_pay: bool = False) -> dict:
    """Update an existing payment policy."""
    body: dict = {
        "marketplaceId": marketplace_id,
        "name": name,
        "categoryTypes": category_types,
        "immediatePay": immediate_pay,
    }
    if payment_methods:
        body["paymentMethods"] = payment_methods
    if description:
        body["description"] = description
    return api_put(f"/sell/account/v1/payment_policy/{payment_policy_id}", body=body)


@mcp.tool()
def delete_payment_policy(payment_policy_id: str) -> dict:
    """Delete a payment policy by ID."""
    return api_delete(f"/sell/account/v1/payment_policy/{payment_policy_id}")


# ── Return Policies ──────────────────────────────────────────────────────────

@mcp.tool()
def get_return_policies(marketplace_id: str) -> dict:
    """Retrieve all return policies for a marketplace."""
    return api_get("/sell/account/v1/return_policy",
                   params={"marketplace_id": marketplace_id})


@mcp.tool()
def get_return_policy(return_policy_id: str) -> dict:
    """Retrieve a return policy by ID."""
    return api_get(f"/sell/account/v1/return_policy/{return_policy_id}")


@mcp.tool()
def get_return_policy_by_name(marketplace_id: str, name: str) -> dict:
    """Retrieve a return policy by name."""
    return api_get("/sell/account/v1/return_policy/get_by_policy_name",
                   params={"marketplace_id": marketplace_id, "name": name})


@mcp.tool()
def create_return_policy(marketplace_id: str, name: str,
                          category_types: list[dict],
                          returns_accepted: bool,
                          return_period: dict | None = None,
                          return_shipping_cost_payer: str | None = None,
                          description: str | None = None,
                          extended_holiday_returns_offered: bool = False) -> dict:
    """
    Create a new return policy.

    Args:
        marketplace_id: eBay marketplace ID.
        name: Policy name.
        category_types: List of category type dicts.
        returns_accepted: Whether returns are accepted.
        return_period: Dict with value and unit (e.g. {"value": 30, "unit": "DAY"}).
        return_shipping_cost_payer: BUYER or SELLER.
        description: Optional description.
        extended_holiday_returns_offered: Offer extended holiday returns.
    """
    body: dict = {
        "marketplaceId": marketplace_id,
        "name": name,
        "categoryTypes": category_types,
        "returnsAccepted": returns_accepted,
        "extendedHolidayReturnsOffered": extended_holiday_returns_offered,
    }
    if return_period:
        body["returnPeriod"] = return_period
    if return_shipping_cost_payer:
        body["returnShippingCostPayer"] = return_shipping_cost_payer
    if description:
        body["description"] = description
    return api_post("/sell/account/v1/return_policy", body=body)


@mcp.tool()
def update_return_policy(return_policy_id: str, marketplace_id: str,
                          name: str, category_types: list[dict],
                          returns_accepted: bool,
                          return_period: dict | None = None,
                          return_shipping_cost_payer: str | None = None,
                          description: str | None = None) -> dict:
    """Update an existing return policy."""
    body: dict = {
        "marketplaceId": marketplace_id,
        "name": name,
        "categoryTypes": category_types,
        "returnsAccepted": returns_accepted,
    }
    if return_period:
        body["returnPeriod"] = return_period
    if return_shipping_cost_payer:
        body["returnShippingCostPayer"] = return_shipping_cost_payer
    if description:
        body["description"] = description
    return api_put(f"/sell/account/v1/return_policy/{return_policy_id}", body=body)


@mcp.tool()
def delete_return_policy(return_policy_id: str) -> dict:
    """Delete a return policy by ID."""
    return api_delete(f"/sell/account/v1/return_policy/{return_policy_id}")


# ── Sales Tax ────────────────────────────────────────────────────────────────

@mcp.tool()
def get_sales_taxes(marketplace_id: str) -> dict:
    """Retrieve all sales tax entries for a marketplace."""
    return api_get("/sell/account/v1/sales_tax",
                   params={"marketplace_id": marketplace_id})


@mcp.tool()
def get_sales_tax(country_code: str, jurisdiction_id: str) -> dict:
    """
    Retrieve a sales tax entry for a specific jurisdiction.

    Args:
        country_code: Two-letter country code (e.g. US).
        jurisdiction_id: State/province code (e.g. CA for California).
    """
    return api_get(f"/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}")


@mcp.tool()
def create_or_replace_sales_tax(country_code: str, jurisdiction_id: str,
                                 sales_tax_percentage: str,
                                 include_shipping_and_handling_in_tax: bool = False) -> dict:
    """
    Create or replace a sales tax entry.

    Args:
        country_code: Two-letter country code.
        jurisdiction_id: State/province code.
        sales_tax_percentage: Tax rate as a string percentage (e.g. "8.5").
        include_shipping_and_handling_in_tax: Apply tax to S&H.
    """
    body = {
        "salesTaxPercentage": sales_tax_percentage,
        "shippingAndHandlingTaxed": include_shipping_and_handling_in_tax,
    }
    return api_put(f"/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}", body=body)


@mcp.tool()
def delete_sales_tax(country_code: str, jurisdiction_id: str) -> dict:
    """Delete a sales tax entry for a jurisdiction."""
    return api_delete(f"/sell/account/v1/sales_tax/{country_code}/{jurisdiction_id}")


# ── Programs ─────────────────────────────────────────────────────────────────

@mcp.tool()
def get_opted_in_programs() -> dict:
    """Retrieve all seller programs the account is opted into."""
    return api_get("/sell/account/v1/program/get_opted_in_programs")


@mcp.tool()
def opt_in_to_program(program_type: str) -> dict:
    """
    Opt the seller account into an eBay seller program.

    Args:
        program_type: Program type (e.g. OUT_OF_STOCK_CONTROL, SELLING_POLICY_MANAGEMENT).
    """
    return api_post("/sell/account/v1/program/opt_in", body={"programType": program_type})


@mcp.tool()
def opt_out_of_program(program_type: str) -> dict:
    """
    Opt the seller account out of an eBay seller program.

    Args:
        program_type: Program type to opt out of.
    """
    return api_post("/sell/account/v1/program/opt_out", body={"programType": program_type})


# ── Privileges & Subscriptions ───────────────────────────────────────────────

@mcp.tool()
def get_seller_privileges() -> dict:
    """Retrieve the selling privileges for the authenticated seller account."""
    return api_get("/sell/account/v1/privilege")


@mcp.tool()
def get_subscriptions() -> dict:
    """Retrieve all active subscriptions for the seller account."""
    return api_get("/sell/account/v1/subscription")


# ── Shipping Rate Tables ─────────────────────────────────────────────────────

@mcp.tool()
def get_rate_tables(country_code: str | None = None) -> dict:
    """
    Retrieve shipping rate tables.

    Args:
        country_code: Optional two-letter country code to filter results.
    """
    params = {}
    if country_code:
        params["country_code"] = country_code
    return api_get("/sell/account/v1/rate_table", params=params or None)


# ── KYC (Know Your Customer) ─────────────────────────────────────────────────

@mcp.tool()
def get_kyc() -> dict:
    """Retrieve KYC (Know Your Customer) verification status for the seller."""
    return api_get("/sell/account/v1/kyc")
