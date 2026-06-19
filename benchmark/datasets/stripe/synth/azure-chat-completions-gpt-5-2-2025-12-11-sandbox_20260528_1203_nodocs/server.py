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
    invoices_mark_uncollectible,
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
    setup_intents_update,
)
from generated_tools.coupons import coupons_create, coupons_delete, coupons_list, coupons_retrieve, coupons_update
from generated_tools.promotion_codes import (
    promotion_codes_create,
    promotion_codes_list,
    promotion_codes_retrieve,
    promotion_codes_update,
)
from generated_tools.connect import (
    account_links_create,
    accounts_create,
    accounts_list,
    accounts_retrieve,
    accounts_update,
    payouts_cancel,
    payouts_create,
    payouts_list,
    payouts_retrieve,
    payouts_reverse,
    transfers_create,
    transfers_list,
    transfers_retrieve,
)

mcp = FastMCP("stripe-mcp")


def _wrap(result: Dict[str, Any]) -> Dict[str, Any]:
    return result


# Customers
mcp.tool(name="customers_create")(customers_create)
mcp.tool(name="customers_retrieve")(customers_retrieve)
mcp.tool(name="customers_update")(customers_update)
mcp.tool(name="customers_delete")(customers_delete)
mcp.tool(name="customers_list")(customers_list)

# Payment Intents
mcp.tool(name="payment_intents_create")(payment_intents_create)
mcp.tool(name="payment_intents_retrieve")(payment_intents_retrieve)
mcp.tool(name="payment_intents_update")(payment_intents_update)
mcp.tool(name="payment_intents_confirm")(payment_intents_confirm)
mcp.tool(name="payment_intents_capture")(payment_intents_capture)
mcp.tool(name="payment_intents_cancel")(payment_intents_cancel)
mcp.tool(name="payment_intents_list")(payment_intents_list)

# Charges
mcp.tool(name="charges_retrieve")(charges_retrieve)
mcp.tool(name="charges_update")(charges_update)
mcp.tool(name="charges_list")(charges_list)

# Refunds
mcp.tool(name="refunds_create")(refunds_create)
mcp.tool(name="refunds_retrieve")(refunds_retrieve)
mcp.tool(name="refunds_update")(refunds_update)
mcp.tool(name="refunds_list")(refunds_list)

# Products
mcp.tool(name="products_create")(products_create)
mcp.tool(name="products_retrieve")(products_retrieve)
mcp.tool(name="products_update")(products_update)
mcp.tool(name="products_delete")(products_delete)
mcp.tool(name="products_list")(products_list)

# Prices
mcp.tool(name="prices_create")(prices_create)
mcp.tool(name="prices_retrieve")(prices_retrieve)
mcp.tool(name="prices_update")(prices_update)
mcp.tool(name="prices_list")(prices_list)

# Subscriptions
mcp.tool(name="subscriptions_create")(subscriptions_create)
mcp.tool(name="subscriptions_retrieve")(subscriptions_retrieve)
mcp.tool(name="subscriptions_update")(subscriptions_update)
mcp.tool(name="subscriptions_cancel")(subscriptions_cancel)
mcp.tool(name="subscriptions_list")(subscriptions_list)

# Invoices
mcp.tool(name="invoices_create")(invoices_create)
mcp.tool(name="invoices_retrieve")(invoices_retrieve)
mcp.tool(name="invoices_update")(invoices_update)
mcp.tool(name="invoices_finalize")(invoices_finalize)
mcp.tool(name="invoices_pay")(invoices_pay)
mcp.tool(name="invoices_void")(invoices_void)
mcp.tool(name="invoices_mark_uncollectible")(invoices_mark_uncollectible)
mcp.tool(name="invoices_list")(invoices_list)

# Checkout Sessions
mcp.tool(name="checkout_sessions_create")(checkout_sessions_create)
mcp.tool(name="checkout_sessions_retrieve")(checkout_sessions_retrieve)
mcp.tool(name="checkout_sessions_list")(checkout_sessions_list)

# Payment Links
mcp.tool(name="payment_links_create")(payment_links_create)
mcp.tool(name="payment_links_retrieve")(payment_links_retrieve)
mcp.tool(name="payment_links_update")(payment_links_update)
mcp.tool(name="payment_links_list")(payment_links_list)

# Setup Intents
mcp.tool(name="setup_intents_create")(setup_intents_create)
mcp.tool(name="setup_intents_retrieve")(setup_intents_retrieve)
mcp.tool(name="setup_intents_update")(setup_intents_update)
mcp.tool(name="setup_intents_confirm")(setup_intents_confirm)
mcp.tool(name="setup_intents_cancel")(setup_intents_cancel)
mcp.tool(name="setup_intents_list")(setup_intents_list)

# Coupons
mcp.tool(name="coupons_create")(coupons_create)
mcp.tool(name="coupons_retrieve")(coupons_retrieve)
mcp.tool(name="coupons_update")(coupons_update)
mcp.tool(name="coupons_delete")(coupons_delete)
mcp.tool(name="coupons_list")(coupons_list)

# Promotion Codes
mcp.tool(name="promotion_codes_create")(promotion_codes_create)
mcp.tool(name="promotion_codes_retrieve")(promotion_codes_retrieve)
mcp.tool(name="promotion_codes_update")(promotion_codes_update)
mcp.tool(name="promotion_codes_list")(promotion_codes_list)

# Connect
mcp.tool(name="accounts_create")(accounts_create)
mcp.tool(name="accounts_retrieve")(accounts_retrieve)
mcp.tool(name="accounts_update")(accounts_update)
mcp.tool(name="accounts_list")(accounts_list)
mcp.tool(name="account_links_create")(account_links_create)

mcp.tool(name="transfers_create")(transfers_create)
mcp.tool(name="transfers_retrieve")(transfers_retrieve)
mcp.tool(name="transfers_list")(transfers_list)

mcp.tool(name="payouts_create")(payouts_create)
mcp.tool(name="payouts_retrieve")(payouts_retrieve)
mcp.tool(name="payouts_cancel")(payouts_cancel)
mcp.tool(name="payouts_reverse")(payouts_reverse)
mcp.tool(name="payouts_list")(payouts_list)


if __name__ == "__main__":
    mcp.run()
