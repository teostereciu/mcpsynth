"""Stripe MCP Server — entry point."""
import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("stripe")

# Register all tool modules
from generated_tools.payment_intents import register_payment_intent_tools
from generated_tools.customers import register_customer_tools
from generated_tools.charges import register_charge_tools
from generated_tools.refunds import register_refund_tools
from generated_tools.subscriptions import register_subscription_tools
from generated_tools.invoices import register_invoice_tools
from generated_tools.products_prices import register_product_price_tools
from generated_tools.checkout_sessions import register_checkout_session_tools
from generated_tools.connect import register_connect_tools
from generated_tools.misc import register_misc_tools
from generated_tools.billing_extras import register_billing_extra_tools
from generated_tools.webhooks_credit_notes import register_webhook_credit_note_tools

register_payment_intent_tools(mcp)
register_customer_tools(mcp)
register_charge_tools(mcp)
register_refund_tools(mcp)
register_subscription_tools(mcp)
register_invoice_tools(mcp)
register_product_price_tools(mcp)
register_checkout_session_tools(mcp)
register_connect_tools(mcp)
register_misc_tools(mcp)
register_billing_extra_tools(mcp)
register_webhook_credit_note_tools(mcp)

if __name__ == "__main__":
    mcp.run(transport="stdio")
