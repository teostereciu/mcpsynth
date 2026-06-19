from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.payment_intents import (
    payment_intents_cancel,
    payment_intents_capture,
    payment_intents_confirm,
    payment_intents_create,
    payment_intents_list,
    payment_intents_list_all,
    payment_intents_retrieve,
    payment_intents_update,
)
from generated_tools.charges import (
    charges_capture,
    charges_list,
    charges_list_all,
    charges_retrieve,
    charges_update,
)
from generated_tools.refunds import (
    refunds_create,
    refunds_list,
    refunds_list_all,
    refunds_retrieve,
    refunds_update,
)
from generated_tools.customers import (
    customers_create,
    customers_delete,
    customers_list,
    customers_list_all,
    customers_retrieve,
    customers_search,
    customers_update,
)
from generated_tools.products import (
    products_create,
    products_delete,
    products_list,
    products_list_all,
    products_retrieve,
    products_search,
    products_update,
)
from generated_tools.prices import (
    prices_create,
    prices_list,
    prices_list_all,
    prices_retrieve,
    prices_search,
    prices_update,
)
from generated_tools.subscriptions import (
    subscriptions_cancel,
    subscriptions_create,
    subscriptions_list,
    subscriptions_list_all,
    subscriptions_retrieve,
    subscriptions_search,
    subscriptions_update,
)
from generated_tools.invoices import (
    invoiceitems_create,
    invoiceitems_list,
    invoices_create,
    invoices_finalize,
    invoices_list,
    invoices_list_all,
    invoices_mark_uncollectible,
    invoices_pay,
    invoices_retrieve,
    invoices_update,
    invoices_void,
)
from generated_tools.checkout_sessions import (
    checkout_sessions_create,
    checkout_sessions_expire,
    checkout_sessions_list,
    checkout_sessions_list_all,
    checkout_sessions_retrieve,
    checkout_sessions_update,
)
from generated_tools.payment_links import (
    payment_links_create,
    payment_links_list,
    payment_links_list_all,
    payment_links_retrieve,
    payment_links_update,
)
from generated_tools.connect import (
    accounts_create,
    accounts_delete,
    accounts_list,
    accounts_retrieve,
    accounts_update,
    payouts_cancel,
    payouts_create,
    payouts_list,
    payouts_retrieve,
    payouts_update,
    transfers_create,
    transfers_list,
    transfers_retrieve,
    transfers_update,
)
from generated_tools.setup_intents import (
    setup_intents_cancel,
    setup_intents_confirm,
    setup_intents_create,
    setup_intents_list,
    setup_intents_list_all,
    setup_intents_retrieve,
    setup_intents_update,
)
from generated_tools.coupons import (
    coupons_create,
    coupons_delete,
    coupons_list,
    coupons_list_all,
    coupons_retrieve,
    coupons_update,
)
from generated_tools.promotion_codes import (
    promotion_codes_create,
    promotion_codes_list,
    promotion_codes_list_all,
    promotion_codes_retrieve,
    promotion_codes_update,
)


mcp = FastMCP("stripe")


# Payment Intents
mcp.tool()(payment_intents_create)
mcp.tool()(payment_intents_retrieve)
mcp.tool()(payment_intents_update)
mcp.tool()(payment_intents_confirm)
mcp.tool()(payment_intents_capture)
mcp.tool()(payment_intents_cancel)
mcp.tool()(payment_intents_list)
mcp.tool()(payment_intents_list_all)

# Charges
mcp.tool()(charges_retrieve)
mcp.tool()(charges_update)
mcp.tool()(charges_capture)
mcp.tool()(charges_list)
mcp.tool()(charges_list_all)

# Refunds
mcp.tool()(refunds_create)
mcp.tool()(refunds_retrieve)
mcp.tool()(refunds_update)
mcp.tool()(refunds_list)
mcp.tool()(refunds_list_all)

# Customers
mcp.tool()(customers_create)
mcp.tool()(customers_retrieve)
mcp.tool()(customers_update)
mcp.tool()(customers_delete)
mcp.tool()(customers_list)
mcp.tool()(customers_list_all)
mcp.tool()(customers_search)

# Products
mcp.tool()(products_create)
mcp.tool()(products_retrieve)
mcp.tool()(products_update)
mcp.tool()(products_delete)
mcp.tool()(products_list)
mcp.tool()(products_list_all)
mcp.tool()(products_search)

# Prices
mcp.tool()(prices_create)
mcp.tool()(prices_retrieve)
mcp.tool()(prices_update)
mcp.tool()(prices_list)
mcp.tool()(prices_list_all)
mcp.tool()(prices_search)

# Subscriptions
mcp.tool()(subscriptions_create)
mcp.tool()(subscriptions_retrieve)
mcp.tool()(subscriptions_update)
mcp.tool()(subscriptions_cancel)
mcp.tool()(subscriptions_list)
mcp.tool()(subscriptions_list_all)
mcp.tool()(subscriptions_search)

# Invoices + Invoice Items
mcp.tool()(invoices_create)
mcp.tool()(invoices_retrieve)
mcp.tool()(invoices_update)
mcp.tool()(invoices_finalize)
mcp.tool()(invoices_pay)
mcp.tool()(invoices_void)
mcp.tool()(invoices_mark_uncollectible)
mcp.tool()(invoices_list)
mcp.tool()(invoices_list_all)
mcp.tool()(invoiceitems_create)
mcp.tool()(invoiceitems_list)

# Checkout Sessions
mcp.tool()(checkout_sessions_create)
mcp.tool()(checkout_sessions_retrieve)
mcp.tool()(checkout_sessions_update)
mcp.tool()(checkout_sessions_expire)
mcp.tool()(checkout_sessions_list)
mcp.tool()(checkout_sessions_list_all)

# Payment Links
mcp.tool()(payment_links_create)
mcp.tool()(payment_links_retrieve)
mcp.tool()(payment_links_update)
mcp.tool()(payment_links_list)
mcp.tool()(payment_links_list_all)

# Connect
mcp.tool()(accounts_create)
mcp.tool()(accounts_retrieve)
mcp.tool()(accounts_update)
mcp.tool()(accounts_delete)
mcp.tool()(accounts_list)

mcp.tool()(transfers_create)
mcp.tool()(transfers_retrieve)
mcp.tool()(transfers_update)
mcp.tool()(transfers_list)

mcp.tool()(payouts_create)
mcp.tool()(payouts_retrieve)
mcp.tool()(payouts_update)
mcp.tool()(payouts_cancel)
mcp.tool()(payouts_list)

# Setup Intents
mcp.tool()(setup_intents_create)
mcp.tool()(setup_intents_retrieve)
mcp.tool()(setup_intents_update)
mcp.tool()(setup_intents_confirm)
mcp.tool()(setup_intents_cancel)
mcp.tool()(setup_intents_list)
mcp.tool()(setup_intents_list_all)

# Coupons
mcp.tool()(coupons_create)
mcp.tool()(coupons_retrieve)
mcp.tool()(coupons_update)
mcp.tool()(coupons_delete)
mcp.tool()(coupons_list)
mcp.tool()(coupons_list_all)

# Promotion Codes
mcp.tool()(promotion_codes_create)
mcp.tool()(promotion_codes_retrieve)
mcp.tool()(promotion_codes_update)
mcp.tool()(promotion_codes_list)
mcp.tool()(promotion_codes_list_all)


if __name__ == "__main__":
    mcp.run()
