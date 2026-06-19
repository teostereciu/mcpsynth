from mcp.server.fastmcp import FastMCP

from generated_tools.accounts import create_account, retrieve_account, update_account
from generated_tools.charges import create_charge, update_charge
from generated_tools.checkout_sessions import (
    create_checkout_session,
    retrieve_checkout_session,
    update_checkout_session,
)
from generated_tools.coupons import create_coupon, retrieve_coupon, update_coupon
from generated_tools.customers import create_customer, retrieve_customer, update_customer
from generated_tools.invoices import create_preview_invoice
from generated_tools.payment_links import (
    create_payment_link,
    list_payment_link_line_items,
    update_payment_link,
)
from generated_tools.payouts import create_payout, retrieve_payout, update_payout
from generated_tools.prices import create_price, retrieve_price, update_price
from generated_tools.promotion_codes import (
    create_promotion_code,
    retrieve_promotion_code,
    update_promotion_code,
)
from generated_tools.refunds import create_refund, retrieve_refund, update_refund
from generated_tools.setup_intents import create_setup_intent, retrieve_setup_intent, update_setup_intent
from generated_tools.subscriptions import create_subscription
from generated_tools.transfers import create_transfer, retrieve_transfer, update_transfer


mcp = FastMCP("stripe-mcp")

# Charges
mcp.tool()(create_charge)
mcp.tool()(update_charge)

# Refunds
mcp.tool()(create_refund)
mcp.tool()(update_refund)
mcp.tool()(retrieve_refund)

# Customers
mcp.tool()(create_customer)
mcp.tool()(update_customer)
mcp.tool()(retrieve_customer)

# Products/Prices
mcp.tool()(create_price)
mcp.tool()(update_price)
mcp.tool()(retrieve_price)

# Products
from generated_tools.products import create_product, retrieve_product, update_product

mcp.tool()(create_product)
mcp.tool()(update_product)
mcp.tool()(retrieve_product)

# Subscriptions
mcp.tool()(create_subscription)

# Invoices
mcp.tool()(create_preview_invoice)

# Checkout Sessions
mcp.tool()(create_checkout_session)
mcp.tool()(retrieve_checkout_session)
mcp.tool()(update_checkout_session)

# Payment Links
mcp.tool()(create_payment_link)
mcp.tool()(update_payment_link)
mcp.tool()(list_payment_link_line_items)

# Connect: Accounts, Transfers, Payouts
mcp.tool()(create_account)
mcp.tool()(update_account)
mcp.tool()(retrieve_account)

mcp.tool()(create_transfer)
mcp.tool()(update_transfer)
mcp.tool()(retrieve_transfer)

mcp.tool()(create_payout)
mcp.tool()(update_payout)
mcp.tool()(retrieve_payout)

# Setup Intents
mcp.tool()(create_setup_intent)
mcp.tool()(update_setup_intent)
mcp.tool()(retrieve_setup_intent)

# Coupons / Promotion Codes
mcp.tool()(create_coupon)
mcp.tool()(update_coupon)
mcp.tool()(retrieve_coupon)

mcp.tool()(create_promotion_code)
mcp.tool()(update_promotion_code)
mcp.tool()(retrieve_promotion_code)


if __name__ == "__main__":
    mcp.run()
