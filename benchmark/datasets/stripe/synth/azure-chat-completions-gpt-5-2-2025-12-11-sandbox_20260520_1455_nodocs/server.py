from mcp.server.fastmcp import FastMCP

from generated_tools import billing, checkout, connect, core, discounts, payments

mcp = FastMCP("stripe-mcp")

# Core
mcp.tool()(core.create_customer)
mcp.tool()(core.get_customer)
mcp.tool()(core.update_customer)
mcp.tool()(core.delete_customer)
mcp.tool()(core.list_customers)

mcp.tool()(core.create_product)
mcp.tool()(core.get_product)
mcp.tool()(core.update_product)
mcp.tool()(core.delete_product)
mcp.tool()(core.list_products)

mcp.tool()(core.create_price)
mcp.tool()(core.get_price)
mcp.tool()(core.update_price)
mcp.tool()(core.list_prices)

# Payments
mcp.tool()(payments.create_payment_intent)
mcp.tool()(payments.get_payment_intent)
mcp.tool()(payments.update_payment_intent)
mcp.tool()(payments.confirm_payment_intent)
mcp.tool()(payments.cancel_payment_intent)
mcp.tool()(payments.list_payment_intents)

mcp.tool()(payments.get_charge)
mcp.tool()(payments.list_charges)

mcp.tool()(payments.create_refund)
mcp.tool()(payments.get_refund)
mcp.tool()(payments.update_refund)
mcp.tool()(payments.list_refunds)

mcp.tool()(payments.create_setup_intent)
mcp.tool()(payments.get_setup_intent)
mcp.tool()(payments.confirm_setup_intent)
mcp.tool()(payments.cancel_setup_intent)
mcp.tool()(payments.list_setup_intents)

# Billing
mcp.tool()(billing.create_subscription)
mcp.tool()(billing.get_subscription)
mcp.tool()(billing.update_subscription)
mcp.tool()(billing.cancel_subscription)
mcp.tool()(billing.list_subscriptions)

mcp.tool()(billing.create_invoice)
mcp.tool()(billing.get_invoice)
mcp.tool()(billing.update_invoice)
mcp.tool()(billing.finalize_invoice)
mcp.tool()(billing.pay_invoice)
mcp.tool()(billing.void_invoice)
mcp.tool()(billing.list_invoices)

mcp.tool()(billing.create_invoice_item)
mcp.tool()(billing.list_invoice_items)

# Checkout
mcp.tool()(checkout.create_checkout_session)
mcp.tool()(checkout.get_checkout_session)
mcp.tool()(checkout.list_checkout_sessions)

mcp.tool()(checkout.create_payment_link)
mcp.tool()(checkout.get_payment_link)
mcp.tool()(checkout.update_payment_link)
mcp.tool()(checkout.list_payment_links)

# Connect
mcp.tool()(connect.create_account)
mcp.tool()(connect.get_account)
mcp.tool()(connect.update_account)
mcp.tool()(connect.list_accounts)

mcp.tool()(connect.create_transfer)
mcp.tool()(connect.get_transfer)
mcp.tool()(connect.list_transfers)

mcp.tool()(connect.create_payout)
mcp.tool()(connect.get_payout)
mcp.tool()(connect.cancel_payout)
mcp.tool()(connect.list_payouts)

# Discounts
mcp.tool()(discounts.create_coupon)
mcp.tool()(discounts.get_coupon)
mcp.tool()(discounts.update_coupon)
mcp.tool()(discounts.delete_coupon)
mcp.tool()(discounts.list_coupons)

mcp.tool()(discounts.create_promotion_code)
mcp.tool()(discounts.get_promotion_code)
mcp.tool()(discounts.update_promotion_code)
mcp.tool()(discounts.list_promotion_codes)


if __name__ == "__main__":
    mcp.run_stdio()
