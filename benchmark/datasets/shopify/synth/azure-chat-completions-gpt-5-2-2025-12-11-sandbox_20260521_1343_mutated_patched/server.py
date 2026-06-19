from mcp.server.fastmcp import FastMCP

from generated_tools.customers import (
    count_customers,
    create_customer,
    create_customer_account_activation_url,
    get_customer,
    list_customer_orders,
    list_customers,
    search_customers,
    send_customer_invite,
    update_customer,
)
from generated_tools.customer_addresses import (
    bulk_customer_addresses_set,
    create_customer_address,
    delete_customer_address,
    get_customer_address,
    list_customer_addresses,
    set_default_customer_address,
    update_customer_address,
)
from generated_tools.discount_codes import (
    count_discount_codes,
    create_discount_code,
    create_discount_code_batch,
    delete_discount_code,
    get_discount_code,
    get_discount_code_batch,
    list_discount_codes,
    list_discount_codes_for_batch,
    lookup_discount_code,
    update_discount_code,
)
from generated_tools.draft_orders import (
    complete_draft_order,
    count_draft_orders,
    create_draft_order,
    delete_draft_order,
    get_draft_order,
    list_draft_orders,
    send_draft_order_invoice,
    update_draft_order,
)
from generated_tools.inventory_items import get_inventory_item, list_inventory_items, update_inventory_item
from generated_tools.inventory_levels import (
    adjust_inventory_level,
    connect_inventory_level,
    delete_inventory_level,
    list_inventory_levels,
    set_inventory_level,
)
from generated_tools.locations import count_locations, get_location, list_location_inventory_levels, list_locations
from generated_tools.metafields import (
    count_metafields,
    create_metafield,
    delete_metafield,
    get_metafield,
    list_metafields,
    update_metafield,
)
from generated_tools.orders import (
    cancel_order,
    close_order,
    count_orders,
    create_order,
    delete_order,
    get_order,
    list_orders,
    open_order,
    update_order,
)
from generated_tools.price_rules import (
    count_price_rules,
    create_price_rule,
    delete_price_rule,
    get_price_rule,
    list_price_rules,
    update_price_rule,
)
from generated_tools.product_images import (
    count_product_images,
    create_product_image,
    delete_product_image,
    get_product_image,
    list_product_images,
    update_product_image,
)
from generated_tools.product_variants import (
    count_product_variants,
    create_product_variant,
    delete_product_variant,
    get_variant,
    list_product_variants,
    update_variant,
)
from generated_tools.products import (
    count_products,
    create_product,
    delete_product,
    get_product,
    list_products,
    update_product,
)
from generated_tools.refunds import calculate_refund, create_refund, get_refund, list_refunds
from generated_tools.transactions import count_transactions, create_transaction, get_transaction, list_transactions
from generated_tools.webhooks import count_webhooks, create_webhook, delete_webhook, get_webhook, list_webhooks, update_webhook


mcp = FastMCP("shopify-admin-rest")

# Products
mcp.tool()(create_product)
mcp.tool()(list_products)
mcp.tool()(get_product)
mcp.tool()(count_products)
mcp.tool()(update_product)
mcp.tool()(delete_product)

# Product variants
mcp.tool()(create_product_variant)
mcp.tool()(list_product_variants)
mcp.tool()(count_product_variants)
mcp.tool()(get_variant)
mcp.tool()(update_variant)
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
mcp.tool()(complete_draft_order)
mcp.tool()(send_draft_order_invoice)
mcp.tool()(delete_draft_order)

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
mcp.tool()(search_customers)
mcp.tool()(get_customer)
mcp.tool()(count_customers)
mcp.tool()(update_customer)
mcp.tool()(list_customer_orders)
mcp.tool()(create_customer_account_activation_url)
mcp.tool()(send_customer_invite)

# Customer addresses
mcp.tool()(create_customer_address)
mcp.tool()(list_customer_addresses)
mcp.tool()(get_customer_address)
mcp.tool()(update_customer_address)
mcp.tool()(set_default_customer_address)
mcp.tool()(bulk_customer_addresses_set)
mcp.tool()(delete_customer_address)

# Inventory
mcp.tool()(list_inventory_items)
mcp.tool()(get_inventory_item)
mcp.tool()(update_inventory_item)

mcp.tool()(list_inventory_levels)
mcp.tool()(adjust_inventory_level)
mcp.tool()(connect_inventory_level)
mcp.tool()(set_inventory_level)
mcp.tool()(delete_inventory_level)

# Locations
mcp.tool()(list_locations)
mcp.tool()(count_locations)
mcp.tool()(get_location)
mcp.tool()(list_location_inventory_levels)

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


if __name__ == "__main__":
    mcp.run()
