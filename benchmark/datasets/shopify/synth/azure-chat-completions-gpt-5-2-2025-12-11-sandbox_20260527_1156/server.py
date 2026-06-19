from mcp.server.fastmcp import FastMCP

from generated_tools import (
    customers,
    customer_addresses,
    discount_codes,
    draft_orders,
    inventory_items,
    inventory_levels,
    locations,
    metafields,
    orders,
    price_rules,
    product_images,
    product_variants,
    products,
    refunds,
    webhooks,
)

mcp = FastMCP("shopify-admin-rest")


# Products
@mcp.tool()
def create_product(product: dict):
    return products.create_product(product)


@mcp.tool()
def list_products(**kwargs):
    return products.list_products(**kwargs)


@mcp.tool()
def get_product(product_id: int, fields: str | None = None):
    return products.get_product(product_id, fields=fields)


@mcp.tool()
def count_products(**kwargs):
    return products.count_products(**kwargs)


@mcp.tool()
def update_product(product_id: int, product: dict):
    return products.update_product(product_id, product)


@mcp.tool()
def delete_product(product_id: int):
    return products.delete_product(product_id)


# Product variants
@mcp.tool()
def create_product_variant(product_id: int, variant: dict):
    return product_variants.create_product_variant(product_id, variant)


@mcp.tool()
def list_product_variants(product_id: int, **kwargs):
    return product_variants.list_product_variants(product_id, **kwargs)


@mcp.tool()
def count_product_variants(product_id: int):
    return product_variants.count_product_variants(product_id)


@mcp.tool()
def get_variant(variant_id: int, fields: str | None = None):
    return product_variants.get_variant(variant_id, fields=fields)


@mcp.tool()
def update_variant(variant_id: int, variant: dict):
    return product_variants.update_variant(variant_id, variant)


@mcp.tool()
def delete_product_variant(product_id: int, variant_id: int):
    return product_variants.delete_product_variant(product_id, variant_id)


# Product images
@mcp.tool()
def create_product_image(product_id: int, image: dict):
    return product_images.create_product_image(product_id, image)


@mcp.tool()
def list_product_images(product_id: int, **kwargs):
    return product_images.list_product_images(product_id, **kwargs)


@mcp.tool()
def get_product_image(product_id: int, image_id: int, fields: str | None = None):
    return product_images.get_product_image(product_id, image_id, fields=fields)


@mcp.tool()
def count_product_images(product_id: int):
    return product_images.count_product_images(product_id)


@mcp.tool()
def update_product_image(product_id: int, image_id: int, image: dict):
    return product_images.update_product_image(product_id, image_id, image)


@mcp.tool()
def delete_product_image(product_id: int, image_id: int):
    return product_images.delete_product_image(product_id, image_id)


# Orders
@mcp.tool()
def create_order(order: dict):
    return orders.create_order(order)


@mcp.tool()
def list_orders(**kwargs):
    return orders.list_orders(**kwargs)


@mcp.tool()
def get_order(order_id: int, fields: str | None = None):
    return orders.get_order(order_id, fields=fields)


@mcp.tool()
def count_orders(**kwargs):
    return orders.count_orders(**kwargs)


@mcp.tool()
def update_order(order_id: int, order: dict):
    return orders.update_order(order_id, order)


@mcp.tool()
def delete_order(order_id: int):
    return orders.delete_order(order_id)


@mcp.tool()
def cancel_order(order_id: int, cancel: dict | None = None):
    return orders.cancel_order(order_id, cancel)


@mcp.tool()
def close_order(order_id: int):
    return orders.close_order(order_id)


@mcp.tool()
def open_order(order_id: int):
    return orders.open_order(order_id)


# Draft orders
@mcp.tool()
def create_draft_order(draft_order: dict):
    return draft_orders.create_draft_order(draft_order)


@mcp.tool()
def list_draft_orders(**kwargs):
    return draft_orders.list_draft_orders(**kwargs)


@mcp.tool()
def get_draft_order(draft_order_id: int, fields: str | None = None):
    return draft_orders.get_draft_order(draft_order_id, fields=fields)


@mcp.tool()
def count_draft_orders(status: str | None = None):
    return draft_orders.count_draft_orders(status=status)


@mcp.tool()
def update_draft_order(draft_order_id: int, draft_order: dict):
    return draft_orders.update_draft_order(draft_order_id, draft_order)


@mcp.tool()
def delete_draft_order(draft_order_id: int):
    return draft_orders.delete_draft_order(draft_order_id)


@mcp.tool()
def send_draft_order_invoice(draft_order_id: int, invoice: dict | None = None):
    return draft_orders.send_draft_order_invoice(draft_order_id, invoice)


@mcp.tool()
def complete_draft_order(draft_order_id: int, payment_pending: bool | None = None):
    return draft_orders.complete_draft_order(draft_order_id, payment_pending=payment_pending)


# Refunds
@mcp.tool()
def calculate_refund(order_id: int, refund: dict):
    return refunds.calculate_refund(order_id, refund)


@mcp.tool()
def create_refund(order_id: int, refund: dict):
    return refunds.create_refund(order_id, refund)


@mcp.tool()
def list_refunds(order_id: int):
    return refunds.list_refunds(order_id)


@mcp.tool()
def get_refund(order_id: int, refund_id: int):
    return refunds.get_refund(order_id, refund_id)


# Customers
@mcp.tool()
def create_customer(customer: dict):
    return customers.create_customer(customer)


@mcp.tool()
def list_customers(**kwargs):
    return customers.list_customers(**kwargs)


@mcp.tool()
def get_customer(customer_id: int, fields: str | None = None):
    return customers.get_customer(customer_id, fields=fields)


@mcp.tool()
def count_customers(created_at_min: str | None = None, created_at_max: str | None = None):
    return customers.count_customers(created_at_min=created_at_min, created_at_max=created_at_max)


@mcp.tool()
def search_customers(query: str, fields: str | None = None):
    return customers.search_customers(query, fields=fields)


@mcp.tool()
def update_customer(customer_id: int, customer: dict):
    return customers.update_customer(customer_id, customer)


@mcp.tool()
def get_customer_orders(customer_id: int, **kwargs):
    return customers.get_customer_orders(customer_id, **kwargs)


@mcp.tool()
def create_customer_account_activation_url(customer_id: int):
    return customers.create_customer_account_activation_url(customer_id)


@mcp.tool()
def send_customer_invite(customer_id: int, invite: dict | None = None):
    return customers.send_customer_invite(customer_id, invite)


# Customer addresses
@mcp.tool()
def create_customer_address(customer_id: int, address: dict):
    return customer_addresses.create_customer_address(customer_id, address)


@mcp.tool()
def list_customer_addresses(customer_id: int, **kwargs):
    return customer_addresses.list_customer_addresses(customer_id, **kwargs)


@mcp.tool()
def get_customer_address(customer_id: int, address_id: int):
    return customer_addresses.get_customer_address(customer_id, address_id)


@mcp.tool()
def update_customer_address(customer_id: int, address_id: int, address: dict):
    return customer_addresses.update_customer_address(customer_id, address_id, address)


@mcp.tool()
def set_default_customer_address(customer_id: int, address_id: int):
    return customer_addresses.set_default_customer_address(customer_id, address_id)


@mcp.tool()
def bulk_customer_addresses_set(customer_id: int, address_ids: list[int], operation: str):
    return customer_addresses.bulk_customer_addresses_set(customer_id, address_ids, operation)


@mcp.tool()
def delete_customer_address(customer_id: int, address_id: int):
    return customer_addresses.delete_customer_address(customer_id, address_id)


# Inventory
@mcp.tool()
def list_inventory_items(ids: str, limit: int | None = None):
    return inventory_items.list_inventory_items(ids, limit=limit)


@mcp.tool()
def get_inventory_item(inventory_item_id: int):
    return inventory_items.get_inventory_item(inventory_item_id)


@mcp.tool()
def update_inventory_item(inventory_item_id: int, inventory_item: dict):
    return inventory_items.update_inventory_item(inventory_item_id, inventory_item)


@mcp.tool()
def list_inventory_levels(**kwargs):
    return inventory_levels.list_inventory_levels(**kwargs)


@mcp.tool()
def adjust_inventory_level(location_id: int, inventory_item_id: int, available_adjustment: int):
    return inventory_levels.adjust_inventory_level(location_id, inventory_item_id, available_adjustment)


@mcp.tool()
def connect_inventory_level(
    location_id: int, inventory_item_id: int, relocate_if_necessary: bool | None = None
):
    return inventory_levels.connect_inventory_level(
        location_id, inventory_item_id, relocate_if_necessary=relocate_if_necessary
    )


@mcp.tool()
def set_inventory_level(
    location_id: int,
    inventory_item_id: int,
    available: int,
    disconnect_if_necessary: bool | None = None,
):
    return inventory_levels.set_inventory_level(
        location_id, inventory_item_id, available, disconnect_if_necessary=disconnect_if_necessary
    )


@mcp.tool()
def delete_inventory_level(location_id: int, inventory_item_id: int):
    return inventory_levels.delete_inventory_level(location_id, inventory_item_id)


# Locations
@mcp.tool()
def list_locations(limit: int | None = None):
    return locations.list_locations(limit=limit)


@mcp.tool()
def get_location(location_id: int):
    return locations.get_location(location_id)


@mcp.tool()
def count_locations():
    return locations.count_locations()


@mcp.tool()
def list_location_inventory_levels(location_id: int):
    return locations.list_location_inventory_levels(location_id)


# Discounts
@mcp.tool()
def create_price_rule(price_rule: dict):
    return price_rules.create_price_rule(price_rule)


@mcp.tool()
def list_price_rules(limit: int | None = None, since_id: int | None = None):
    return price_rules.list_price_rules(limit=limit, since_id=since_id)


@mcp.tool()
def get_price_rule(price_rule_id: int):
    return price_rules.get_price_rule(price_rule_id)


@mcp.tool()
def count_price_rules():
    return price_rules.count_price_rules()


@mcp.tool()
def update_price_rule(price_rule_id: int, price_rule: dict):
    return price_rules.update_price_rule(price_rule_id, price_rule)


@mcp.tool()
def delete_price_rule(price_rule_id: int):
    return price_rules.delete_price_rule(price_rule_id)


@mcp.tool()
def create_discount_code(price_rule_id: int, discount_code: dict):
    return discount_codes.create_discount_code(price_rule_id, discount_code)


@mcp.tool()
def list_discount_codes(price_rule_id: int, limit: int | None = None, since_id: int | None = None):
    return discount_codes.list_discount_codes(price_rule_id, limit=limit, since_id=since_id)


@mcp.tool()
def get_discount_code(price_rule_id: int, discount_code_id: int):
    return discount_codes.get_discount_code(price_rule_id, discount_code_id)


@mcp.tool()
def update_discount_code(price_rule_id: int, discount_code_id: int, discount_code: dict):
    return discount_codes.update_discount_code(price_rule_id, discount_code_id, discount_code)


@mcp.tool()
def delete_discount_code(price_rule_id: int, discount_code_id: int):
    return discount_codes.delete_discount_code(price_rule_id, discount_code_id)


@mcp.tool()
def create_discount_code_batch(price_rule_id: int, discount_codes_list: list[dict]):
    return discount_codes.create_discount_code_batch(price_rule_id, discount_codes_list)


@mcp.tool()
def get_discount_code_batch(price_rule_id: int, batch_id: int):
    return discount_codes.get_discount_code_batch(price_rule_id, batch_id)


@mcp.tool()
def list_discount_codes_for_batch(price_rule_id: int, batch_id: int):
    return discount_codes.list_discount_codes_for_batch(price_rule_id, batch_id)


@mcp.tool()
def count_discount_codes(
    times_used: int | None = None, times_used_min: int | None = None, times_used_max: int | None = None
):
    return discount_codes.count_discount_codes(
        times_used=times_used, times_used_min=times_used_min, times_used_max=times_used_max
    )


@mcp.tool()
def lookup_discount_code(code: str):
    return discount_codes.lookup_discount_code(code)


# Webhooks
@mcp.tool()
def create_webhook(webhook: dict):
    return webhooks.create_webhook(webhook)


@mcp.tool()
def list_webhooks(**kwargs):
    return webhooks.list_webhooks(**kwargs)


@mcp.tool()
def get_webhook(webhook_id: int):
    return webhooks.get_webhook(webhook_id)


@mcp.tool()
def count_webhooks(topic: str | None = None, address: str | None = None):
    return webhooks.count_webhooks(topic=topic, address=address)


@mcp.tool()
def update_webhook(webhook_id: int, webhook: dict):
    return webhooks.update_webhook(webhook_id, webhook)


@mcp.tool()
def delete_webhook(webhook_id: int):
    return webhooks.delete_webhook(webhook_id)


# Metafields (common)
@mcp.tool()
def create_product_metafield(product_id: int, metafield: dict):
    return metafields.create_product_metafield(product_id, metafield)


@mcp.tool()
def list_product_metafields(product_id: int, limit: int | None = None, since_id: int | None = None):
    return metafields.list_product_metafields(product_id, limit=limit, since_id=since_id)


@mcp.tool()
def get_product_metafield(product_id: int, metafield_id: int):
    return metafields.get_product_metafield(product_id, metafield_id)


@mcp.tool()
def count_product_metafields(product_id: int):
    return metafields.count_product_metafields(product_id)


@mcp.tool()
def update_product_metafield(product_id: int, metafield_id: int, metafield: dict):
    return metafields.update_product_metafield(product_id, metafield_id, metafield)


@mcp.tool()
def delete_product_metafield(product_id: int, metafield_id: int):
    return metafields.delete_product_metafield(product_id, metafield_id)


@mcp.tool()
def create_order_metafield(order_id: int, metafield: dict):
    return metafields.create_order_metafield(order_id, metafield)


@mcp.tool()
def list_order_metafields(order_id: int, limit: int | None = None, since_id: int | None = None):
    return metafields.list_order_metafields(order_id, limit=limit, since_id=since_id)


if __name__ == "__main__":
    mcp.run()
