from mcp.server.fastmcp import FastMCP

from generated_tools.payment_intents import create_payment_intent, retrieve_payment_intent, update_payment_intent
from generated_tools.charges import list_charges, retrieve_charge, update_charge
from generated_tools.refunds import create_refund, retrieve_refund, update_refund
from generated_tools.customers import create_customer, retrieve_customer, update_customer
from generated_tools.products import create_product, retrieve_product, update_product
from generated_tools.prices import create_price, retrieve_price, update_price
from generated_tools.subscriptions import create_subscription, retrieve_subscription, update_subscription
from generated_tools.invoices import create_invoice, create_preview_invoice, update_invoice
from generated_tools.checkout_sessions import create_checkout_session, retrieve_checkout_session
from generated_tools.payment_links import create_payment_link, retrieve_payment_link_line_items, update_payment_link
from generated_tools.coupons import create_coupon, retrieve_coupon, update_coupon
from generated_tools.promotion_codes import create_promotion_code, retrieve_promotion_code, update_promotion_code
from generated_tools.setup_intents import create_setup_intent, retrieve_setup_intent, update_setup_intent
from generated_tools.payment_methods import create_payment_method, retrieve_customer_payment_method, update_payment_method

mcp = FastMCP("stripe-mcp")

# Payment Intents
mcp.tool()(create_payment_intent)
mcp.tool()(update_payment_intent)
mcp.tool()(retrieve_payment_intent)

# Charges
mcp.tool()(list_charges)
mcp.tool()(update_charge)
mcp.tool()(retrieve_charge)

# Refunds
mcp.tool()(create_refund)
mcp.tool()(update_refund)
mcp.tool()(retrieve_refund)

# Customers
mcp.tool()(create_customer)
mcp.tool()(update_customer)
mcp.tool()(retrieve_customer)

# Products
mcp.tool()(create_product)
mcp.tool()(update_product)
mcp.tool()(retrieve_product)

# Prices
mcp.tool()(create_price)
mcp.tool()(update_price)
mcp.tool()(retrieve_price)

# Subscriptions
mcp.tool()(create_subscription)
mcp.tool()(update_subscription)
mcp.tool()(retrieve_subscription)

# Invoices
mcp.tool()(create_preview_invoice)
mcp.tool()(create_invoice)
mcp.tool()(update_invoice)

# Checkout Sessions
mcp.tool()(create_checkout_session)
mcp.tool()(retrieve_checkout_session)

# Payment Links
mcp.tool()(create_payment_link)
mcp.tool()(update_payment_link)
mcp.tool()(retrieve_payment_link_line_items)

# Coupons
mcp.tool()(create_coupon)
mcp.tool()(update_coupon)
mcp.tool()(retrieve_coupon)

# Promotion Codes
mcp.tool()(create_promotion_code)
mcp.tool()(update_promotion_code)
mcp.tool()(retrieve_promotion_code)

# Setup Intents
mcp.tool()(create_setup_intent)
mcp.tool()(update_setup_intent)
mcp.tool()(retrieve_setup_intent)

# Payment Methods
mcp.tool()(create_payment_method)
mcp.tool()(update_payment_method)
mcp.tool()(retrieve_customer_payment_method)


if __name__ == "__main__":
    mcp.run()
