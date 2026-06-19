from mcp.server.fastmcp import FastMCP

from generated_tools.customers import (
    create_customer,
    delete_customer,
    list_customers,
    retrieve_customer,
    update_customer,
)
from generated_tools.payment_intents import (
    cancel_payment_intent,
    capture_payment_intent,
    confirm_payment_intent,
    create_payment_intent,
    list_payment_intents,
    retrieve_payment_intent,
    update_payment_intent,
)

mcp = FastMCP("stripe")


# Customers
mcp.tool()(create_customer)
mcp.tool()(retrieve_customer)
mcp.tool()(update_customer)
mcp.tool()(delete_customer)
mcp.tool()(list_customers)

# PaymentIntents
mcp.tool()(create_payment_intent)
mcp.tool()(retrieve_payment_intent)
mcp.tool()(update_payment_intent)
mcp.tool()(list_payment_intents)
mcp.tool()(confirm_payment_intent)
mcp.tool()(capture_payment_intent)
mcp.tool()(cancel_payment_intent)


if __name__ == "__main__":
    mcp.run()
