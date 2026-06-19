"""
Stripe MCP Server
=================
Runs over stdio and exposes Stripe API operations as MCP tools.

Usage:
    STRIPE_API_KEY=sk_test_... python server.py
"""

import os
from mcp.server.fastmcp import FastMCP

# Validate API key is present at startup
if not os.environ.get("STRIPE_API_KEY"):
    raise EnvironmentError(
        "STRIPE_API_KEY environment variable is required. "
        "Set it to your Stripe secret key (sk_test_... or sk_live_...)."
    )

mcp = FastMCP(
    name="stripe",
    instructions=(
        "This server exposes Stripe API operations as tools. "
        "Use these tools to manage payments, customers, subscriptions, invoices, "
        "products, prices, refunds, disputes, and more. "
        "All monetary amounts are in the smallest currency unit (e.g. cents for USD). "
        "Metadata is passed as comma-separated key=value pairs (e.g. 'order_id=123,env=prod'). "
        "Pagination uses cursor-based starting_after / ending_before parameters."
    ),
)

# Register all domain modules
from generated_tools import (
    payment_intents,
    customers,
    charges,
    refunds,
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
    disputes,
    balance,
    webhooks,
    subscription_items,
    tax_rates,
    events,
    tokens,
)

payment_intents.register(mcp)
customers.register(mcp)
charges.register(mcp)
refunds.register(mcp)
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
disputes.register(mcp)
balance.register(mcp)
webhooks.register(mcp)
subscription_items.register(mcp)
tax_rates.register(mcp)
events.register(mcp)
tokens.register(mcp)

if __name__ == "__main__":
    mcp.run(transport="stdio")
