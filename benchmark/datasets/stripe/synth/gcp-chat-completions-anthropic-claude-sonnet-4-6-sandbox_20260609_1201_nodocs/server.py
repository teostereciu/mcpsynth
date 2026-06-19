"""
Stripe MCP Server
=================
Runs over stdio and exposes Stripe API operations as MCP tools.

Usage:
    STRIPE_API_KEY=sk_test_... python server.py

All tools are registered via domain-specific modules in generated_tools/.
"""

from mcp.server.fastmcp import FastMCP

# Import all domain registration functions
from generated_tools import (
    payment_intents,
    charges,
    refunds,
    customers,
    products,
    prices,
    subscriptions,
    invoices,
    checkout,
    payment_links,
    setup_intents,
    coupons,
    connect,
    payment_methods,
    subscription_items,
    subscription_schedules,
    disputes,
    balance,
    webhooks,
    tax_rates,
    files,
    events,
    account,
    search,
    application_fees,
)

mcp = FastMCP(
    name="stripe",
    instructions=(
        "This server exposes Stripe API operations as MCP tools. "
        "Authenticate by setting the STRIPE_API_KEY environment variable. "
        "All monetary amounts are in the smallest currency unit (e.g. cents for USD). "
        "Form-encoded bodies are handled automatically."
    ),
)

# Register all domain tools
payment_intents.register(mcp)
charges.register(mcp)
refunds.register(mcp)
customers.register(mcp)
products.register(mcp)
prices.register(mcp)
subscriptions.register(mcp)
invoices.register(mcp)
checkout.register(mcp)
payment_links.register(mcp)
setup_intents.register(mcp)
coupons.register(mcp)
connect.register(mcp)
payment_methods.register(mcp)
subscription_items.register(mcp)
subscription_schedules.register(mcp)
disputes.register(mcp)
balance.register(mcp)
webhooks.register(mcp)
tax_rates.register(mcp)
files.register(mcp)
events.register(mcp)
account.register(mcp)
search.register(mcp)
application_fees.register(mcp)

if __name__ == "__main__":
    mcp.run(transport="stdio")
