import os
from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.payment_intents import (
    cancel_payment_intent,
    capture_payment_intent,
    confirm_payment_intent,
    create_payment_intent,
    list_payment_intents,
    retrieve_payment_intent,
    update_payment_intent,
)
from generated_tools.charges import capture_charge, list_charges, retrieve_charge, update_charge
from generated_tools.refunds import cancel_refund, create_refund, list_refunds, retrieve_refund, update_refund
from generated_tools.customers import (
    create_customer,
    delete_customer,
    list_customers,
    retrieve_customer,
    search_customers,
    update_customer,
)
from generated_tools.products import create_product, delete_product, list_products, retrieve_product, update_product
from generated_tools.prices import create_price, list_prices, retrieve_price, update_price
from generated_tools.subscriptions import (
    cancel_subscription,
    create_subscription,
    list_subscriptions,
    retrieve_subscription,
    update_subscription,
)
from generated_tools.invoices import (
    create_invoice,
    finalize_invoice,
    list_invoices,
    mark_invoice_uncollectible,
    pay_invoice,
    retrieve_invoice,
    update_invoice,
    void_invoice,
)
from generated_tools.checkout_sessions import create_checkout_session, list_checkout_sessions, retrieve_checkout_session
from generated_tools.payment_links import create_payment_link, list_payment_links, retrieve_payment_link, update_payment_link
from generated_tools.setup_intents import (
    cancel_setup_intent,
    confirm_setup_intent,
    create_setup_intent,
    list_setup_intents,
    retrieve_setup_intent,
    update_setup_intent,
)
from generated_tools.coupons import create_coupon, delete_coupon, list_coupons, retrieve_coupon, update_coupon
from generated_tools.promotion_codes import (
    create_promotion_code,
    list_promotion_codes,
    retrieve_promotion_code,
    update_promotion_code,
)
from generated_tools.connect import (
    cancel_payout,
    create_account,
    create_account_link,
    create_payout,
    create_transfer,
    list_accounts,
    list_transfers,
    retrieve_account,
    retrieve_payout,
    retrieve_transfer,
    reverse_transfer,
    update_account,
)

mcp = FastMCP("stripe-mcp")


@mcp.tool
def stripe_healthcheck() -> Dict[str, Any]:
    """Basic environment validation."""
    key = os.getenv("STRIPE_API_KEY")
    if not key:
        return {"ok": False, "error": "STRIPE_API_KEY is not set"}
    return {"ok": True, "stripe_api_key_prefix": key[:7]}


# Payment Intents
mcp.tool()(create_payment_intent)
mcp.tool()(retrieve_payment_intent)
mcp.tool()(update_payment_intent)
mcp.tool()(confirm_payment_intent)
mcp.tool()(capture_payment_intent)
mcp.tool()(cancel_payment_intent)
mcp.tool()(list_payment_intents)

# Charges
mcp.tool()(retrieve_charge)
mcp.tool()(update_charge)
mcp.tool()(list_charges)
mcp.tool()(capture_charge)

# Refunds
mcp.tool()(create_refund)
mcp.tool()(retrieve_refund)
mcp.tool()(update_refund)
mcp.tool()(list_refunds)
mcp.tool()(cancel_refund)

# Customers
mcp.tool()(create_customer)
mcp.tool()(retrieve_customer)
mcp.tool()(update_customer)
mcp.tool()(delete_customer)
mcp.tool()(list_customers)
mcp.tool()(search_customers)

# Products
mcp.tool()(create_product)
mcp.tool()(retrieve_product)
mcp.tool()(update_product)
mcp.tool()(delete_product)
mcp.tool()(list_products)

# Prices
mcp.tool()(create_price)
mcp.tool()(retrieve_price)
mcp.tool()(update_price)
mcp.tool()(list_prices)

# Subscriptions
mcp.tool()(create_subscription)
mcp.tool()(retrieve_subscription)
mcp.tool()(update_subscription)
mcp.tool()(cancel_subscription)
mcp.tool()(list_subscriptions)

# Invoices
mcp.tool()(create_invoice)
mcp.tool()(retrieve_invoice)
mcp.tool()(update_invoice)
mcp.tool()(finalize_invoice)
mcp.tool()(pay_invoice)
mcp.tool()(void_invoice)
mcp.tool()(mark_invoice_uncollectible)
mcp.tool()(list_invoices)

# Checkout Sessions
mcp.tool()(create_checkout_session)
mcp.tool()(retrieve_checkout_session)
mcp.tool()(list_checkout_sessions)

# Payment Links
mcp.tool()(create_payment_link)
mcp.tool()(retrieve_payment_link)
mcp.tool()(update_payment_link)
mcp.tool()(list_payment_links)

# Setup Intents
mcp.tool()(create_setup_intent)
mcp.tool()(retrieve_setup_intent)
mcp.tool()(update_setup_intent)
mcp.tool()(confirm_setup_intent)
mcp.tool()(cancel_setup_intent)
mcp.tool()(list_setup_intents)

# Coupons
mcp.tool()(create_coupon)
mcp.tool()(retrieve_coupon)
mcp.tool()(update_coupon)
mcp.tool()(delete_coupon)
mcp.tool()(list_coupons)

# Promotion Codes
mcp.tool()(create_promotion_code)
mcp.tool()(retrieve_promotion_code)
mcp.tool()(update_promotion_code)
mcp.tool()(list_promotion_codes)

# Connect
mcp.tool()(create_account)
mcp.tool()(retrieve_account)
mcp.tool()(update_account)
mcp.tool()(list_accounts)
mcp.tool()(create_account_link)
mcp.tool()(create_transfer)
mcp.tool()(retrieve_transfer)
mcp.tool()(list_transfers)
mcp.tool()(reverse_transfer)
mcp.tool()(create_payout)
mcp.tool()(retrieve_payout)
mcp.tool()(cancel_payout)


if __name__ == "__main__":
    mcp.run()
