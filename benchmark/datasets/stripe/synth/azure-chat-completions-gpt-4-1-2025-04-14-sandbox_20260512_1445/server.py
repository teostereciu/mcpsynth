import os
from fastmcp import FastMCP

# Import all tool modules
import generated_tools.payment_intents
import generated_tools.charges
import generated_tools.refunds
import generated_tools.customers
import generated_tools.products
import generated_tools.prices
import generated_tools.subscriptions
import generated_tools.invoices
import generated_tools.checkout_sessions
import generated_tools.payment_links
import generated_tools.promotion_codes
import generated_tools.coupons

if __name__ == "__main__":
    FastMCP().run_stdio()
