from mcp.server.fastmcp import FastMCP

from generated_tools.products import (
    list_products,
    get_product,
    create_product,
    update_product,
    delete_product,
    list_product_variants,
    get_variant,
    create_variant,
    update_variant,
    delete_variant,
    list_product_images,
    get_product_image,
    create_product_image,
    update_product_image,
    delete_product_image,
)
from generated_tools.orders import (
    list_orders,
    get_order,
    update_order,
    close_order,
    open_order,
    cancel_order,
    list_draft_orders,
    get_draft_order,
    create_draft_order,
    update_draft_order,
    complete_draft_order,
    delete_draft_order,
    calculate_refund,
    create_refund,
    list_transactions,
)
from generated_tools.customers import (
    list_customers,
    search_customers,
    get_customer,
    create_customer,
    update_customer,
    delete_customer,
)
from generated_tools.inventory import (
    list_inventory_items,
    get_inventory_item,
    update_inventory_item,
    list_inventory_levels,
    adjust_inventory_level,
    set_inventory_level,
    connect_inventory_level,
)
from generated_tools.fulfillment import (
    list_locations,
    list_fulfillment_orders,
    get_fulfillment_order,
    move_fulfillment_order,
    cancel_fulfillment_order,
    create_fulfillment,
    get_fulfillment,
    update_fulfillment,
    cancel_fulfillment,
    create_fulfillment_event,
)
from generated_tools.discounts import (
    list_price_rules,
    get_price_rule,
    create_price_rule,
    update_price_rule,
    delete_price_rule,
    list_discount_codes,
    get_discount_code,
    create_discount_code,
    update_discount_code,
    delete_discount_code,
)
from generated_tools.webhooks import (
    list_webhooks,
    get_webhook,
    create_webhook,
    update_webhook,
    delete_webhook,
)
from generated_tools.metafields import (
    list_metafields,
    get_metafield,
    create_metafield,
    update_metafield,
    delete_metafield,
    list_product_metafields,
    list_order_metafields,
    list_customer_metafields,
)
from generated_tools.collections import (
    list_custom_collections,
    get_custom_collection,
    create_custom_collection,
    update_custom_collection,
    delete_custom_collection,
    list_smart_collections,
    get_smart_collection,
    create_smart_collection,
    update_smart_collection,
    delete_smart_collection,
    list_collects,
    create_collect,
    delete_collect,
)


mcp = FastMCP("shopify_admin_rest")

# Products
mcp.tool()(list_products)
mcp.tool()(get_product)
mcp.tool()(create_product)
mcp.tool()(update_product)
mcp.tool()(delete_product)

mcp.tool()(list_product_variants)
mcp.tool()(get_variant)
mcp.tool()(create_variant)
mcp.tool()(update_variant)
mcp.tool()(delete_variant)

mcp.tool()(list_product_images)
mcp.tool()(get_product_image)
mcp.tool()(create_product_image)
mcp.tool()(update_product_image)
mcp.tool()(delete_product_image)

# Orders
mcp.tool()(list_orders)
mcp.tool()(get_order)
mcp.tool()(update_order)
mcp.tool()(close_order)
mcp.tool()(open_order)
mcp.tool()(cancel_order)

mcp.tool()(list_draft_orders)
mcp.tool()(get_draft_order)
mcp.tool()(create_draft_order)
mcp.tool()(update_draft_order)
mcp.tool()(complete_draft_order)
mcp.tool()(delete_draft_order)

mcp.tool()(calculate_refund)
mcp.tool()(create_refund)
mcp.tool()(list_transactions)

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

# Fulfillment
mcp.tool()(list_locations)
mcp.tool()(list_fulfillment_orders)
mcp.tool()(get_fulfillment_order)
mcp.tool()(move_fulfillment_order)
mcp.tool()(cancel_fulfillment_order)
mcp.tool()(create_fulfillment)
mcp.tool()(get_fulfillment)
mcp.tool()(update_fulfillment)
mcp.tool()(cancel_fulfillment)
mcp.tool()(create_fulfillment_event)

# Discounts
mcp.tool()(list_price_rules)
mcp.tool()(get_price_rule)
mcp.tool()(create_price_rule)
mcp.tool()(update_price_rule)
mcp.tool()(delete_price_rule)

mcp.tool()(list_discount_codes)
mcp.tool()(get_discount_code)
mcp.tool()(create_discount_code)
mcp.tool()(update_discount_code)
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
mcp.tool()(list_product_metafields)
mcp.tool()(list_order_metafields)
mcp.tool()(list_customer_metafields)

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

mcp.tool()(list_collects)
mcp.tool()(create_collect)
mcp.tool()(delete_collect)


if __name__ == "__main__":
    mcp.run()
