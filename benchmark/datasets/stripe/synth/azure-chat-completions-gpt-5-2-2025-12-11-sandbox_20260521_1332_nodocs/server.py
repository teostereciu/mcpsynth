from mcp.server.fastmcp import FastMCP

from stripe_mcp import tools_billing, tools_checkout_connect, tools_core

mcp = FastMCP("stripe-mcp")

# Core
mcp.tool()(tools_core.create_customer)
mcp.tool()(tools_core.get_customer)
mcp.tool()(tools_core.update_customer)
mcp.tool()(tools_core.delete_customer)
mcp.tool()(tools_core.list_customers)

mcp.tool()(tools_core.create_payment_intent)
mcp.tool()(tools_core.get_payment_intent)
mcp.tool()(tools_core.update_payment_intent)
mcp.tool()(tools_core.confirm_payment_intent)
mcp.tool()(tools_core.cancel_payment_intent)
mcp.tool()(tools_core.capture_payment_intent)
mcp.tool()(tools_core.list_payment_intents)

mcp.tool()(tools_core.list_charges)
mcp.tool()(tools_core.get_charge)

mcp.tool()(tools_core.create_refund)
mcp.tool()(tools_core.get_refund)
mcp.tool()(tools_core.list_refunds)

# Billing
mcp.tool()(tools_billing.create_product)
mcp.tool()(tools_billing.get_product)
mcp.tool()(tools_billing.update_product)
mcp.tool()(tools_billing.list_products)

mcp.tool()(tools_billing.create_price)
mcp.tool()(tools_billing.get_price)
mcp.tool()(tools_billing.update_price)
mcp.tool()(tools_billing.list_prices)

mcp.tool()(tools_billing.create_subscription)
mcp.tool()(tools_billing.get_subscription)
mcp.tool()(tools_billing.update_subscription)
mcp.tool()(tools_billing.cancel_subscription)
mcp.tool()(tools_billing.list_subscriptions)

mcp.tool()(tools_billing.create_invoice)
mcp.tool()(tools_billing.get_invoice)
mcp.tool()(tools_billing.finalize_invoice)
mcp.tool()(tools_billing.pay_invoice)
mcp.tool()(tools_billing.void_invoice)
mcp.tool()(tools_billing.list_invoices)

# Checkout + Connect
mcp.tool()(tools_checkout_connect.create_checkout_session)
mcp.tool()(tools_checkout_connect.get_checkout_session)
mcp.tool()(tools_checkout_connect.list_checkout_sessions)

mcp.tool()(tools_checkout_connect.create_payment_link)
mcp.tool()(tools_checkout_connect.get_payment_link)
mcp.tool()(tools_checkout_connect.list_payment_links)

mcp.tool()(tools_checkout_connect.create_setup_intent)
mcp.tool()(tools_checkout_connect.get_setup_intent)
mcp.tool()(tools_checkout_connect.confirm_setup_intent)

mcp.tool()(tools_checkout_connect.create_connect_account)
mcp.tool()(tools_checkout_connect.get_connect_account)
mcp.tool()(tools_checkout_connect.update_connect_account)
mcp.tool()(tools_checkout_connect.list_connect_accounts)

mcp.tool()(tools_checkout_connect.create_transfer)
mcp.tool()(tools_checkout_connect.get_transfer)
mcp.tool()(tools_checkout_connect.list_transfers)

mcp.tool()(tools_checkout_connect.create_payout)
mcp.tool()(tools_checkout_connect.get_payout)
mcp.tool()(tools_checkout_connect.list_payouts)

mcp.tool()(tools_checkout_connect.create_coupon)
mcp.tool()(tools_checkout_connect.get_coupon)
mcp.tool()(tools_checkout_connect.list_coupons)

mcp.tool()(tools_checkout_connect.create_promotion_code)
mcp.tool()(tools_checkout_connect.get_promotion_code)
mcp.tool()(tools_checkout_connect.list_promotion_codes)


if __name__ == "__main__":
    mcp.run()
