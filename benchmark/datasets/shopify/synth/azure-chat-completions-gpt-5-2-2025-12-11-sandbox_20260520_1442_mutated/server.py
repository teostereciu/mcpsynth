from mcp.server.fastmcp import FastMCP

from generated_tools.products import (
    create_product,
    list_products,
    get_product,
    count_products,
    update_product,
    delete_product,
)
from generated_tools.product_variants import (
    create_product_variant,
    list_product_variants,
    count_product_variants,
    get_product_variant,
    update_product_variant,
    delete_product_variant,
)
from generated_tools.product_images import (
    create_product_image,
    list_product_images,
    get_product_image,
    count_product_images,
    update_product_image,
    delete_product_image,
)
from generated_tools.orders import (
    create_order,
    list_orders,
    get_order,
    count_orders,
    update_order,
    delete_order,
    cancel_order,
    close_order,
    open_order,
)
from generated_tools.draft_orders import (
    create_draft_order,
    list_draft_orders,
    get_draft_order,
    count_draft_orders,
    update_draft_order,
    delete_draft_order,
    complete_draft_order,
    send_draft_order_invoice,
)
from generated_tools.refunds import (
    calculate_refund,
    create_refund,
    list_refunds,
    get_refund,
)
from generated_tools.transactions import (
    create_transaction,
    list_transactions,
    get_transaction,
    count_transactions,
)
from generated_tools.customers import (
    create_customer,
    list_customers,
    count_customers,
    search_customers,
    get_customer_orders,
    update_customer,
    create_customer_account_activation_url,
    send_customer_invite,
)
from generated_tools.inventory_items import (
    list_inventory_items,
    get_inventory_item,
    update_inventory_item,
)
from generated_tools.inventory_levels import (
    list_inventory_levels,
    adjust_inventory_level,
    set_inventory_level,
    connect_inventory_level,
    delete_inventory_level,
)
from generated_tools.locations import (
    list_locations,
    get_location,
    count_locations,
    list_location_inventory_levels,
)
from generated_tools.fulfillment_orders import (
    list_fulfillment_orders_for_order,
    get_fulfillment_order,
    cancel_fulfillment_order,
    close_fulfillment_order,
    open_fulfillment_order,
    hold_fulfillment_order,
    release_fulfillment_order_hold,
    move_fulfillment_order,
    reschedule_fulfillment_order,
    set_fulfillment_orders_deadline,
)
from generated_tools.fulfillments import (
    create_fulfillment,
    list_fulfillments_for_order,
    get_fulfillment,
    count_fulfillments_for_order,
    list_fulfillments_for_fulfillment_order,
    cancel_fulfillment,
    update_fulfillment_tracking,
)
from generated_tools.webhooks import (
    create_webhook,
    list_webhooks,
    get_webhook,
    count_webhooks,
    update_webhook,
    delete_webhook,
)
from generated_tools.metafields import (
    create_metafield,
    list_metafields,
    get_metafield,
    count_metafields,
    update_metafield,
    delete_metafield,
)
from generated_tools.price_rules import (
    create_price_rule,
    list_price_rules,
    get_price_rule,
    count_price_rules,
    update_price_rule,
    delete_price_rule,
)
from generated_tools.discount_codes import (
    create_discount_code,
    list_discount_codes,
    get_discount_code,
    update_discount_code,
    delete_discount_code,
    count_discount_codes,
    lookup_discount_code,
    create_discount_code_batch,
    get_discount_code_batch,
    list_discount_codes_for_batch,
)
from generated_tools.collections import (
    get_collection,
    list_collection_products,
)
from generated_tools.custom_collections import (
    create_custom_collection,
    list_custom_collections,
    get_custom_collection,
    count_custom_collections,
    update_custom_collection,
    delete_custom_collection,
)
from generated_tools.smart_collections import (
    create_smart_collection,
    list_smart_collections,
    get_smart_collection,
    count_smart_collections,
    update_smart_collection,
    delete_smart_collection,
    reorder_smart_collection_products,
)
from generated_tools.collects import (
    create_collect,
    list_collects,
    get_collect,
    count_collects,
    delete_collect,
)
from generated_tools.shop import get_shop


mcp = FastMCP("shopify_admin_rest")

# Products
mcp.tool()(create_product)
mcp.tool()(list_products)
mcp.tool()(get_product)
mcp.tool()(count_products)
mcp.tool()(update_product)
mcp.tool()(delete_product)

# Variants
mcp.tool()(create_product_variant)
mcp.tool()(list_product_variants)
mcp.tool()(count_product_variants)
mcp.tool()(get_product_variant)
mcp.tool()(update_product_variant)
mcp.tool()(delete_product_variant)

# Product images
mcp.tool()(create_product_image)
mcp.tool()(list_product_images)
mcp.tool()(get_product_image)
mcp.tool()(count_product_images)
mcp.tool()(update_product_image)
mcp.tool()(delete_product_image)

# Orders
mcp.tool()(create_order)
mcp.tool()(list_orders)
mcp.tool()(get_order)
mcp.tool()(count_orders)
mcp.tool()(update_order)
mcp.tool()(delete_order)
mcp.tool()(cancel_order)
mcp.tool()(close_order)
mcp.tool()(open_order)

# Draft orders
mcp.tool()(create_draft_order)
mcp.tool()(list_draft_orders)
mcp.tool()(get_draft_order)
mcp.tool()(count_draft_orders)
mcp.tool()(update_draft_order)
mcp.tool()(delete_draft_order)
mcp.tool()(complete_draft_order)
mcp.tool()(send_draft_order_invoice)

# Refunds
mcp.tool()(calculate_refund)
mcp.tool()(create_refund)
mcp.tool()(list_refunds)
mcp.tool()(get_refund)

# Transactions
mcp.tool()(create_transaction)
mcp.tool()(list_transactions)
mcp.tool()(get_transaction)
mcp.tool()(count_transactions)

# Customers
mcp.tool()(create_customer)
mcp.tool()(list_customers)
mcp.tool()(count_customers)
mcp.tool()(search_customers)
mcp.tool()(get_customer_orders)
mcp.tool()(update_customer)
mcp.tool()(create_customer_account_activation_url)
mcp.tool()(send_customer_invite)

# Inventory
mcp.tool()(list_inventory_items)
mcp.tool()(get_inventory_item)
mcp.tool()(update_inventory_item)

mcp.tool()(list_inventory_levels)
mcp.tool()(adjust_inventory_level)
mcp.tool()(set_inventory_level)
mcp.tool()(connect_inventory_level)
mcp.tool()(delete_inventory_level)

# Locations
mcp.tool()(list_locations)
mcp.tool()(get_location)
mcp.tool()(count_locations)
mcp.tool()(list_location_inventory_levels)

# Fulfillment orders
mcp.tool()(list_fulfillment_orders_for_order)
mcp.tool()(get_fulfillment_order)
mcp.tool()(cancel_fulfillment_order)
mcp.tool()(close_fulfillment_order)
mcp.tool()(open_fulfillment_order)
mcp.tool()(hold_fulfillment_order)
mcp.tool()(release_fulfillment_order_hold)
mcp.tool()(move_fulfillment_order)
mcp.tool()(reschedule_fulfillment_order)
mcp.tool()(set_fulfillment_orders_deadline)

# Fulfillments
mcp.tool()(create_fulfillment)
mcp.tool()(list_fulfillments_for_order)
mcp.tool()(get_fulfillment)
mcp.tool()(count_fulfillments_for_order)
mcp.tool()(list_fulfillments_for_fulfillment_order)
mcp.tool()(cancel_fulfillment)
mcp.tool()(update_fulfillment_tracking)

# Webhooks
mcp.tool()(create_webhook)
mcp.tool()(list_webhooks)
mcp.tool()(get_webhook)
mcp.tool()(count_webhooks)
mcp.tool()(update_webhook)
mcp.tool()(delete_webhook)

# Metafields
mcp.tool()(create_metafield)
mcp.tool()(list_metafields)
mcp.tool()(get_metafield)
mcp.tool()(count_metafields)
mcp.tool()(update_metafield)
mcp.tool()(delete_metafield)

# Discounts
mcp.tool()(create_price_rule)
mcp.tool()(list_price_rules)
mcp.tool()(get_price_rule)
mcp.tool()(count_price_rules)
mcp.tool()(update_price_rule)
mcp.tool()(delete_price_rule)

mcp.tool()(create_discount_code)
mcp.tool()(list_discount_codes)
mcp.tool()(get_discount_code)
mcp.tool()(update_discount_code)
mcp.tool()(delete_discount_code)
mcp.tool()(count_discount_codes)
mcp.tool()(lookup_discount_code)
mcp.tool()(create_discount_code_batch)
mcp.tool()(get_discount_code_batch)
mcp.tool()(list_discount_codes_for_batch)

# Collections
mcp.tool()(get_collection)
mcp.tool()(list_collection_products)

mcp.tool()(create_custom_collection)
mcp.tool()(list_custom_collections)
mcp.tool()(get_custom_collection)
mcp.tool()(count_custom_collections)
mcp.tool()(update_custom_collection)
mcp.tool()(delete_custom_collection)

mcp.tool()(create_smart_collection)
mcp.tool()(list_smart_collections)
mcp.tool()(get_smart_collection)
mcp.tool()(count_smart_collections)
mcp.tool()(update_smart_collection)
mcp.tool()(delete_smart_collection)
mcp.tool()(reorder_smart_collection_products)

mcp.tool()(create_collect)
mcp.tool()(list_collects)
mcp.tool()(get_collect)
mcp.tool()(count_collects)
mcp.tool()(delete_collect)

# Shop
mcp.tool()(get_shop)


if __name__ == "__main__":
    mcp.run()
