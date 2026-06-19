"""Stripe MCP Server — entry point."""
import os
from mcp.server.fastmcp import FastMCP

from generated_tools.payment_intents import register_payment_intent_tools
from generated_tools.customers import register_customer_tools
from generated_tools.products_prices import register_product_price_tools
from generated_tools.subscriptions_invoices import register_subscription_invoice_tools
from generated_tools.checkout_payment_links import register_checkout_payment_link_tools
from generated_tools.connect import register_connect_tools
from generated_tools.coupons_promotions import register_coupon_promotion_tools
from generated_tools.payment_methods_disputes import register_payment_method_dispute_tools
from generated_tools.balance_events import register_balance_event_tools
from generated_tools.subscription_items_webhooks import register_subscription_item_webhook_tools

mcp = FastMCP(
    name="stripe",
    instructions=(
        "MCP server for the Stripe API. "
        "Provides tools for Payment Intents, Customers, Charges, Refunds, "
        "Products, Prices, Subscriptions, Invoices, Checkout Sessions, "
        "Payment Links, Connect (Accounts, Transfers, Payouts), Setup Intents, "
        "Coupons, Promotion Codes, Payment Methods, Disputes, Balance, Events, "
        "Subscription Items, and Webhook Endpoints. "
        "All monetary amounts are in the smallest currency unit (e.g. cents for USD). "
        "Requires STRIPE_API_KEY environment variable."
    ),
)

# Register all tool groups
register_payment_intent_tools(mcp)
register_customer_tools(mcp)
register_product_price_tools(mcp)
register_subscription_invoice_tools(mcp)
register_checkout_payment_link_tools(mcp)
register_connect_tools(mcp)
register_coupon_promotion_tools(mcp)
register_payment_method_dispute_tools(mcp)
register_balance_event_tools(mcp)
register_subscription_item_webhook_tools(mcp)

if __name__ == "__main__":
    mcp.run(transport="stdio")
