import os
from typing import Any, Dict

from mcp.server.fastmcp import FastMCP

from generated_tools.customers import (
    customers_create,
    customers_delete,
    customers_list,
    customers_retrieve,
    customers_update,
)
from generated_tools.payment_intents import (
    payment_intents_cancel,
    payment_intents_capture,
    payment_intents_confirm,
    payment_intents_create,
    payment_intents_list,
    payment_intents_retrieve,
    payment_intents_update,
)
from generated_tools.charges import charges_list, charges_retrieve, charges_update
from generated_tools.refunds import refunds_create, refunds_list, refunds_retrieve, refunds_update
from generated_tools.products import products_create, products_delete, products_list, products_retrieve, products_update
from generated_tools.prices import prices_create, prices_list, prices_retrieve, prices_update
from generated_tools.subscriptions import (
    subscriptions_cancel,
    subscriptions_create,
    subscriptions_list,
    subscriptions_retrieve,
    subscriptions_update,
)
from generated_tools.invoices import (
    invoices_create,
    invoices_finalize,
    invoices_list,
    invoices_pay,
    invoices_retrieve,
    invoices_update,
    invoices_void,
)
from generated_tools.checkout_sessions import checkout_sessions_create, checkout_sessions_list, checkout_sessions_retrieve
from generated_tools.payment_links import payment_links_create, payment_links_list, payment_links_retrieve, payment_links_update
from generated_tools.setup_intents import (
    setup_intents_cancel,
    setup_intents_confirm,
    setup_intents_create,
    setup_intents_list,
    setup_intents_retrieve,
)
from generated_tools.coupons import coupons_create, coupons_delete, coupons_list, coupons_retrieve, coupons_update
from generated_tools.promotion_codes import (
    promotion_codes_create,
    promotion_codes_list,
    promotion_codes_retrieve,
    promotion_codes_update,
)
from generated_tools.connect import (
    accounts_create,
    accounts_list,
    accounts_retrieve,
    accounts_update,
    payouts_create,
    payouts_list,
    payouts_retrieve,
    transfers_create,
    transfers_list,
    transfers_retrieve,
)

mcp = FastMCP("stripe-mcp")


@mcp.tool()
def stripe_healthcheck() -> Dict[str, Any]:
    """Basic configuration check (does not call Stripe)."""
    key = os.getenv("STRIPE_API_KEY")
    if not key:
        return {"ok": False, "error": "STRIPE_API_KEY is not set"}
    return {"ok": True, "stripe_api_key_prefix": key[:7]}


# Customers
mcp.tool()(customers_create)
mcp.tool()(customers_retrieve)
mcp.tool()(customers_update)
mcp.tool()(customers_delete)
mcp.tool()(customers_list)

# Payment Intents
mcp.tool()(payment_intents_create)
mcp.tool()(payment_intents_retrieve)
mcp.tool()(payment_intents_update)
mcp.tool()(payment_intents_confirm)
mcp.tool()(payment_intents_capture)
mcp.tool()(payment_intents_cancel)
mcp.tool()(payment_intents_list)

# Charges
mcp.tool()(charges_retrieve)
mcp.tool()(charges_update)
mcp.tool()(charges_list)

# Refunds
mcp.tool()(refunds_create)
mcp.tool()(refunds_retrieve)
mcp.tool()(refunds_update)
mcp.tool()(refunds_list)

# Products
mcp.tool()(products_create)
mcp.tool()(products_retrieve)
mcp.tool()(products_update)
mcp.tool()(products_delete)
mcp.tool()(products_list)

# Prices
mcp.tool()(prices_create)
mcp.tool()(prices_retrieve)
mcp.tool()(prices_update)
mcp.tool()(prices_list)

# Subscriptions
mcp.tool()(subscriptions_create)
mcp.tool()(subscriptions_retrieve)
mcp.tool()(subscriptions_update)
mcp.tool()(subscriptions_cancel)
mcp.tool()(subscriptions_list)

# Invoices
mcp.tool()(invoices_create)
mcp.tool()(invoices_retrieve)
mcp.tool()(invoices_update)
mcp.tool()(invoices_finalize)
mcp.tool()(invoices_pay)
mcp.tool()(invoices_void)
mcp.tool()(invoices_list)

# Checkout Sessions
mcp.tool()(checkout_sessions_create)
mcp.tool()(checkout_sessions_retrieve)
mcp.tool()(checkout_sessions_list)

# Payment Links
mcp.tool()(payment_links_create)
mcp.tool()(payment_links_retrieve)
mcp.tool()(payment_links_update)
mcp.tool()(payment_links_list)

# Setup Intents
mcp.tool()(setup_intents_create)
mcp.tool()(setup_intents_retrieve)
mcp.tool()(setup_intents_confirm)
mcp.tool()(setup_intents_cancel)
mcp.tool()(setup_intents_list)

# Coupons
mcp.tool()(coupons_create)
mcp.tool()(coupons_retrieve)
mcp.tool()(coupons_update)
mcp.tool()(coupons_delete)
mcp.tool()(coupons_list)

# Promotion Codes
mcp.tool()(promotion_codes_create)
mcp.tool()(promotion_codes_retrieve)
mcp.tool()(promotion_codes_update)
mcp.tool()(promotion_codes_list)

# Connect
mcp.tool()(accounts_create)
mcp.tool()(accounts_retrieve)
mcp.tool()(accounts_update)
mcp.tool()(accounts_list)

mcp.tool()(transfers_create)
mcp.tool()(transfers_retrieve)
mcp.tool()(transfers_list)

mcp.tool()(payouts_create)
mcp.tool()(payouts_retrieve)
mcp.tool()(payouts_list)


if __name__ == "__main__":
    mcp.run()
