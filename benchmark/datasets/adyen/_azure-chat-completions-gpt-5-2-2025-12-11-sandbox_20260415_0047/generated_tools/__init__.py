from __future__ import annotations

from fastmcp import FastMCP

from . import checkout as checkout_tools
from . import management as management_tools
from . import payment as payment_tools

mcp = FastMCP("adyen-mcp")

# Checkout tools
mcp.tool()(checkout_tools.checkout_payment_methods)
mcp.tool()(checkout_tools.checkout_create_session)
mcp.tool()(checkout_tools.checkout_get_session)
mcp.tool()(checkout_tools.checkout_create_payment_link)
mcp.tool()(checkout_tools.checkout_get_payment_link)
mcp.tool()(checkout_tools.checkout_update_payment_link)
mcp.tool()(checkout_tools.checkout_list_stored_payment_methods)
mcp.tool()(checkout_tools.checkout_delete_stored_payment_method)

# Management tools
mcp.tool()(management_tools.management_list_companies)
mcp.tool()(management_tools.management_get_company)
mcp.tool()(management_tools.management_list_merchants)
mcp.tool()(management_tools.management_get_merchant)
mcp.tool()(management_tools.management_list_stores)
mcp.tool()(management_tools.management_get_store)
mcp.tool()(management_tools.management_list_merchant_webhooks)
mcp.tool()(management_tools.management_get_merchant_webhook)
mcp.tool()(management_tools.management_list_company_webhooks)
mcp.tool()(management_tools.management_get_company_webhook)

# Payment tools
mcp.tool()(payment_tools.payment_authorise)
mcp.tool()(payment_tools.payment_capture)
mcp.tool()(payment_tools.payment_refund)
mcp.tool()(payment_tools.payment_cancel)
mcp.tool()(payment_tools.payment_cancel_or_refund)
