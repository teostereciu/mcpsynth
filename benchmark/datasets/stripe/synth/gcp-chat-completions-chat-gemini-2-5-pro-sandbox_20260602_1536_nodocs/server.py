from mcp.server.fastmcp import FastMCP
from generated_tools.customers import create_customer, retrieve_customer, update_customer, delete_customer, list_customers
from generated_tools.products import create_product, retrieve_product, update_product, delete_product, list_products
from generated_tools.prices import create_price, retrieve_price, update_price, list_prices
from generated_tools.subscriptions import create_subscription, retrieve_subscription, update_subscription, cancel_subscription, list_subscriptions
from generated_tools.payment_intents import create_payment_intent, retrieve_payment_intent, update_payment_intent, confirm_payment_intent, capture_payment_intent, cancel_payment_intent, list_payment_intents

if __name__ == "__main__":
    mcp_server = FastMCP()
    mcp_server.register_tool(create_customer)
    mcp_server.register_tool(retrieve_customer)
    mcp_server.register_tool(update_customer)
    mcp_server.register_tool(delete_customer)
    mcp_server.register_tool(list_customers)
    mcp_server.register_tool(create_product)
    mcp_server.register_tool(retrieve_product)
    mcp_server.register_tool(update_product)
    mcp_server.register_tool(delete_product)
    mcp_server.register_tool(list_products)
    mcp_server.register_tool(create_price)
    mcp_server.register_tool(retrieve_price)
    mcp_server.register_tool(update_price)
    mcp_server.register_tool(list_prices)
    mcp_server.register_tool(create_subscription)
    mcp_server.register_tool(retrieve_subscription)
    mcp_server.register_tool(update_subscription)
    mcp_server.register_tool(cancel_subscription)
    mcp_server.register_tool(list_subscriptions)
    mcp_server.register_tool(create_payment_intent)
    mcp_server.register_tool(retrieve_payment_intent)
    mcp_server.register_tool(update_payment_intent)
    mcp_server.register_tool(confirm_payment_intent)
    mcp_server.register_tool(capture_payment_intent)
    mcp_server.register_tool(cancel_payment_intent)
    mcp_server.register_tool(list_payment_intents)
    mcp_server.run()
