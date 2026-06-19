from mcp.server.fastmcp import FastMCP

from generated_tools.collections import (
    create_custom_collection,
    create_smart_collection,
    delete_custom_collection,
    delete_smart_collection,
    get_custom_collection,
    get_smart_collection,
    list_custom_collections,
    list_smart_collections,
    update_custom_collection,
    update_smart_collection,
)
from generated_tools.customers import (
    create_customer,
    delete_customer,
    get_customer,
    list_customers,
    search_customers,
    update_customer,
)
from generated_tools.discounts import (
    create_discount_code,
    create_price_rule,
    delete_discount_code,
    delete_price_rule,
    get_price_rule,
    list_discount_codes,
    list_price_rules,
    update_price_rule,
)
from generated_tools.fulfillment import (
    create_fulfillment,
    get_fulfillment,
    get_fulfillment_order,
    list_fulfillment_orders,
    list_locations,
    update_fulfillment_tracking,
)
from generated_tools.inventory import (
    adjust_inventory_level,
    connect_inventory_level,
    get_inventory_item,
    list_inventory_items,
    list_inventory_levels,
    set_inventory_level,
    update_inventory_item,
)
from generated_tools.metafields import (
    create_metafield,
    delete_metafield,
    get_metafield,
    list_metafields,
    update_metafield,
)
from generated_tools.orders import (
    cancel_order,
    close_order,
    complete_draft_order,
    create_draft_order,
    create_order_refund,
    get_draft_order,
    get_order,
    list_draft_orders,
    list_order_transactions,
    list_orders,
    open_order,
    update_draft_order,
    update_order,
)
from generated_tools.products import (
    create_product,
    create_product_image,
    delete_product,
    get_product,
    get_variant,
    list_product_images,
    list_product_variants,
    list_products,
    update_product,
    update_variant,
)
from generated_tools.webhooks import (
    create_webhook,
    delete_webhook,
    get_webhook,
    list_webhooks,
    update_webhook,
)

mcp = FastMCP("shopify-admin-rest")

# Products
mcp.tool()(list_products)
mcp.tool()(get_product)
mcp.tool()(create_product)
mcp.tool()(update_product)
mcp.tool()(delete_product)
mcp.tool()(list_product_variants)
mcp.tool()(get_variant)
mcp.tool()(update_variant)
mcp.tool()(list_product_images)
mcp.tool()(create_product_image)

# Collections
mcp.tool()(list_custom_collections)
mcp.tool()(get_custom_collection)
mcp.tool()(create_custom_collection)
mcp.tool()(update_custom_collection)
mcp.tool()(delete_custom_collection)
mcp.tool()(list_smart_collections)
mcp.tool()(get_smart_collection)
mcp.tool()(create_smart_collection)
mcp.tool()(update_smart_collection)
mcp.tool()(delete_smart_collection)

# Orders
mcp.tool()(list_orders)
mcp.tool()(get_order)
mcp.tool()(update_order)
mcp.tool()(close_order)
mcp.tool()(open_order)
mcp.tool()(cancel_order)
mcp.tool()(list_order_transactions)
mcp.tool()(create_order_refund)

# Draft orders
mcp.tool()(list_draft_orders)
mcp.tool()(get_draft_order)
mcp.tool()(create_draft_order)
mcp.tool()(update_draft_order)
mcp.tool()(complete_draft_order)

# Fulfillment
mcp.tool()(list_locations)
mcp.tool()(list_fulfillment_orders)
mcp.tool()(get_fulfillment_order)
mcp.tool()(create_fulfillment)
mcp.tool()(get_fulfillment)
mcp.tool()(update_fulfillment_tracking)

# Customers
mcp.tool()(list_customers)
mcp.tool()(search_customers)
mcp.tool()(get_customer)
mcp.tool()(create_customer)
mcp.tool()(update_customer)
mcp.tool()(delete_customer)

# Inventory
mcp.tool()(list_inventory_items)
mcp.tool()(get_inventory_item)
mcp.tool()(update_inventory_item)
mcp.tool()(list_inventory_levels)
mcp.tool()(adjust_inventory_level)
mcp.tool()(set_inventory_level)
mcp.tool()(connect_inventory_level)

# Discounts
mcp.tool()(list_price_rules)
mcp.tool()(get_price_rule)
mcp.tool()(create_price_rule)
mcp.tool()(update_price_rule)
mcp.tool()(delete_price_rule)
mcp.tool()(list_discount_codes)
mcp.tool()(create_discount_code)
mcp.tool()(delete_discount_code)

# Webhooks
mcp.tool()(list_webhooks)
mcp.tool()(get_webhook)
mcp.tool()(create_webhook)
mcp.tool()(update_webhook)
mcp.tool()(delete_webhook)

# Metafields
mcp.tool()(list_metafields)
mcp.tool()(get_metafield)
mcp.tool()(create_metafield)
mcp.tool()(update_metafield)
mcp.tool()(delete_metafield)


if __name__ == "__main__":
    mcp.run()
