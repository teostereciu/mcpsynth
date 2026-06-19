import os
from mcp.server.fastmcp import FastMCP

import generated_tools.payment_intents as payment_intents
import generated_tools.charges as charges
import generated_tools.refunds as refunds
import generated_tools.customers as customers
import generated_tools.products as products
import generated_tools.prices as prices
import generated_tools.subscriptions as subscriptions
import generated_tools.invoices as invoices
import generated_tools.checkout_sessions as checkout_sessions
import generated_tools.payment_links as payment_links

TOOLS = [
    payment_intents.create_payment_intent,
    payment_intents.retrieve_payment_intent,
    payment_intents.update_payment_intent,
    charges.retrieve_charge,
    charges.update_charge,
    refunds.create_refund,
    refunds.retrieve_refund,
    refunds.update_refund,
    customers.create_customer,
    customers.retrieve_customer,
    customers.update_customer,
    products.create_product,
    products.retrieve_product,
    products.update_product,
    prices.create_price,
    prices.retrieve_price,
    prices.update_price,
    subscriptions.create_subscription,
    subscriptions.retrieve_subscription,
    subscriptions.update_subscription,
    invoices.retrieve_invoice,
    invoices.create_invoice_preview,
    checkout_sessions.create_checkout_session,
    checkout_sessions.retrieve_checkout_session,
    payment_links.create_payment_link,
    payment_links.retrieve_payment_link,
]

if __name__ == "__main__":
    FastMCP(
        tools=TOOLS,
        tool_discovery="list_tools",
        stdio=True,
    ).run()
