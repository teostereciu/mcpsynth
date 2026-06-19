from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("ShopifyAdmin")

# Import tools
import generated_tools.products
import generated_tools.orders
import generated_tools.fulfillment
import generated_tools.customers
import generated_tools.inventory
import generated_tools.discounts
import generated_tools.webhooks
import generated_tools.metafields

# Register tools
generated_tools.products.register(mcp)
generated_tools.orders.register(mcp)
generated_tools.fulfillment.register(mcp)
generated_tools.customers.register(mcp)
generated_tools.inventory.register(mcp)
generated_tools.discounts.register(mcp)
generated_tools.webhooks.register(mcp)
generated_tools.metafields.register(mcp)

if __name__ == "__main__":
    mcp.run()
