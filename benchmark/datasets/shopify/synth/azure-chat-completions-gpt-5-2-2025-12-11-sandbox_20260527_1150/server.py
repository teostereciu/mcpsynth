from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools import customers, discounts, inventory, metafields, orders, products, webhooks


mcp = FastMCP("shopify-admin-rest")


# Products
@mcp.tool()
def create_product(product: Dict[str, Any], api_version: str = "2026-01") -> Dict[str, Any]:
    return products.create_product(product, api_version=api_version)


@mcp.tool()
def list_products(
    api_version: str = "2026-01",
    ids: Optional[str] = None,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    title: Optional[str] = None,
    vendor: Optional[str] = None,
    handle: Optional[str] = None,
    product_type: Optional[str] = None,
    status: Optional[str] = None,
    collection_id: Optional[int] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    published_at_min: Optional[str] = None,
    published_at_max: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    return products.list_products(
        api_version=api_version,
        ids=ids,
        limit=limit,
        since_id=since_id,
        title=title,
        vendor=vendor,
        handle=handle,
        product_type=product_type,
        status=status,
        collection_id=collection_id,
        created_at_min=created_at_min,
        created_at_max=created_at_max,
        updated_at_min=updated_at_min,
        updated_at_max=updated_at_max,
        published_at_min=published_at_min,
        published_at_max=published_at_max,
        fields=fields,
    )


@mcp.tool()
def get_product(product_id: int, api_version: str = "2026-01", fields: Optional[str] = None) -> Dict[str, Any]:
    return products.get_product(product_id, api_version=api_version, fields=fields)


@mcp.tool()
def count_products(api_version: str = "2026-01", vendor: Optional[str] = None, product_type: Optional[str] = None, status: Optional[str] = None) -> Dict[str, Any]:
    return products.count_products(api_version=api_version, vendor=vendor, product_type=product_type, status=status)


@mcp.tool()
def update_product(product_id: int, product: Dict[str, Any], api_version: str = "2026-01") -> Dict[str, Any]:
    return products.update_product(product_id, product, api_version=api_version)


@mcp.tool()
def delete_product(product_id: int, api_version: str = "2026-01") -> Dict[str, Any]:
    return products.delete_product(product_id, api_version=api_version)


@mcp.tool()
def create_product_variant(product_id: int, variant: Dict[str, Any], api_version: str = "2026-01") -> Dict[str, Any]:
    return products.create_product_variant(product_id, variant, api_version=api_version)


@mcp.tool()
def list_product_variants(product_id: int, api_version: str = "2026-01", limit: Optional[int] = None, since_id: Optional[int] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    return products.list_product_variants(product_id, api_version=api_version, limit=limit, since_id=since_id, fields=fields)


@mcp.tool()
def get_variant(variant_id: int, api_version: str = "2026-01", fields: Optional[str] = None) -> Dict[str, Any]:
    return products.get_variant(variant_id, api_version=api_version, fields=fields)


@mcp.tool()
def update_variant(variant_id: int, variant: Dict[str, Any], api_version: str = "2026-01") -> Dict[str, Any]:
    return products.update_variant(variant_id, variant, api_version=api_version)


@mcp.tool()
def delete_variant(product_id: int, variant_id: int, api_version: str = "2026-01") -> Dict[str, Any]:
    return products.delete_variant(product_id, variant_id, api_version=api_version)


@mcp.tool()
def create_product_image(product_id: int, image: Dict[str, Any], api_version: str = "2026-01") -> Dict[str, Any]:
    return products.create_product_image(product_id, image, api_version=api_version)


@mcp.tool()
def list_product_images(product_id: int, api_version: str = "2026-01", limit: Optional[int] = None, since_id: Optional[int] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    return products.list_product_images(product_id, api_version=api_version, limit=limit, since_id=since_id, fields=fields)


@mcp.tool()
def get_product_image(product_id: int, image_id: int, api_version: str = "2026-01", fields: Optional[str] = None) -> Dict[str, Any]:
    return products.get_product_image(product_id, image_id, api_version=api_version, fields=fields)


@mcp.tool()
def update_product_image(product_id: int, image_id: int, image: Dict[str, Any], api_version: str = "2026-01") -> Dict[str, Any]:
    return products.update_product_image(product_id, image_id, image, api_version=api_version)


@mcp.tool()
def delete_product_image(product_id: int, image_id: int, api_version: str = "2026-01") -> Dict[str, Any]:
    return products.delete_product_image(product_id, image_id, api_version=api_version)


# Orders
@mcp.tool()
def create_order(order: Dict[str, Any], api_version: str = "2026-01") -> Dict[str, Any]:
    return orders.create_order(order, api_version=api_version)


@mcp.tool()
def list_orders(
    api_version: str = "2026-01",
    status: Optional[str] = None,
    ids: Optional[str] = None,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    processed_at_min: Optional[str] = None,
    processed_at_max: Optional[str] = None,
    attribution_app_id: Optional[int] = None,
    financial_status: Optional[str] = None,
    fulfillment_status: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    return orders.list_orders(
        api_version=api_version,
        status=status,
        ids=ids,
        limit=limit,
        since_id=since_id,
        created_at_min=created_at_min,
        created_at_max=created_at_max,
        updated_at_min=updated_at_min,
        updated_at_max=updated_at_max,
        processed_at_min=processed_at_min,
        processed_at_max=processed_at_max,
        attribution_app_id=attribution_app_id,
        financial_status=financial_status,
        fulfillment_status=fulfillment_status,
        fields=fields,
    )


@mcp.tool()
def get_order(order_id: int, api_version: str = "2026-01", fields: Optional[str] = None) -> Dict[str, Any]:
    return orders.get_order(order_id, api_version=api_version, fields=fields)


@mcp.tool()
def count_orders(
    api_version: str = "2026-01",
    status: Optional[str] = None,
    financial_status: Optional[str] = None,
    fulfillment_status: Optional[str] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
) -> Dict[str, Any]:
    return orders.count_orders(
        api_version=api_version,
        status=status,
        financial_status=financial_status,
        fulfillment_status=fulfillment_status,
        created_at_min=created_at_min,
        created_at_max=created_at_max,
        updated_at_min=updated_at_min,
        updated_at_max=updated_at_max,
    )


@mcp.tool()
def update_order(order_id: int, order: Dict[str, Any], api_version: str = "2026-01") -> Dict[str, Any]:
    return orders.update_order(order_id, order, api_version=api_version)


@mcp.tool()
def delete_order(order_id: int, api_version: str = "2026-01") -> Dict[str, Any]:
    return orders.delete_order(order_id, api_version=api_version)


@mcp.tool()
def cancel_order(order_id: int, cancel: Optional[Dict[str, Any]] = None, api_version: str = "2026-01") -> Dict[str, Any]:
    return orders.cancel_order(order_id, cancel=cancel, api_version=api_version)


@mcp.tool()
def close_order(order_id: int, api_version: str = "2026-01") -> Dict[str, Any]:
    return orders.close_order(order_id, api_version=api_version)


@mcp.tool()
def open_order(order_id: int, api_version: str = "2026-01") -> Dict[str, Any]:
    return orders.open_order(order_id, api_version=api_version)


# Customers
@mcp.tool()
def create_customer(customer: Dict[str, Any], api_version: str = "2026-01") -> Dict[str, Any]:
    return customers.create_customer(customer, api_version=api_version)


@mcp.tool()
def list_customers(
    api_version: str = "2026-01",
    ids: Optional[str] = None,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    return customers.list_customers(
        api_version=api_version,
        ids=ids,
        limit=limit,
        since_id=since_id,
        created_at_min=created_at_min,
        created_at_max=created_at_max,
        updated_at_min=updated_at_min,
        updated_at_max=updated_at_max,
        fields=fields,
    )


@mcp.tool()
def get_customer(customer_id: int, api_version: str = "2026-01", fields: Optional[str] = None) -> Dict[str, Any]:
    return customers.get_customer(customer_id, api_version=api_version, fields=fields)


@mcp.tool()
def count_customers(api_version: str = "2026-01") -> Dict[str, Any]:
    return customers.count_customers(api_version=api_version)


@mcp.tool()
def search_customers(query: str, api_version: str = "2026-01", limit: Optional[int] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    return customers.search_customers(query, api_version=api_version, limit=limit, fields=fields)


@mcp.tool()
def update_customer(customer_id: int, customer: Dict[str, Any], api_version: str = "2026-01") -> Dict[str, Any]:
    return customers.update_customer(customer_id, customer, api_version=api_version)


@mcp.tool()
def create_customer_account_activation_url(customer_id: int, api_version: str = "2026-01") -> Dict[str, Any]:
    return customers.create_customer_account_activation_url(customer_id, api_version=api_version)


@mcp.tool()
def send_customer_invite(customer_id: int, invite: Optional[Dict[str, Any]] = None, api_version: str = "2026-01") -> Dict[str, Any]:
    return customers.send_customer_invite(customer_id, invite=invite, api_version=api_version)


@mcp.tool()
def list_customer_orders(customer_id: int, api_version: str = "2026-01", limit: Optional[int] = None, since_id: Optional[int] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    return customers.list_customer_orders(customer_id, api_version=api_version, limit=limit, since_id=since_id, fields=fields)


# Inventory + Locations
@mcp.tool()
def list_inventory_levels(api_version: str = "2026-01", inventory_item_ids: Optional[str] = None, location_ids: Optional[str] = None, limit: Optional[int] = None, updated_at_min: Optional[str] = None) -> Dict[str, Any]:
    return inventory.list_inventory_levels(
        api_version=api_version,
        inventory_item_ids=inventory_item_ids,
        location_ids=location_ids,
        limit=limit,
        updated_at_min=updated_at_min,
    )


@mcp.tool()
def adjust_inventory_level(location_id: int, inventory_item_id: int, available_adjustment: int, api_version: str = "2026-01") -> Dict[str, Any]:
    return inventory.adjust_inventory_level(location_id, inventory_item_id, available_adjustment, api_version=api_version)


@mcp.tool()
def set_inventory_level(location_id: int, inventory_item_id: int, available: int, api_version: str = "2026-01", disconnect_if_necessary: Optional[bool] = None) -> Dict[str, Any]:
    return inventory.set_inventory_level(
        location_id,
        inventory_item_id,
        available,
        api_version=api_version,
        disconnect_if_necessary=disconnect_if_necessary,
    )


@mcp.tool()
def connect_inventory_item(location_id: int, inventory_item_id: int, api_version: str = "2026-01", relocate_if_necessary: Optional[bool] = None) -> Dict[str, Any]:
    return inventory.connect_inventory_item(location_id, inventory_item_id, api_version=api_version, relocate_if_necessary=relocate_if_necessary)


@mcp.tool()
def delete_inventory_level(location_id: int, inventory_item_id: int, api_version: str = "2026-01") -> Dict[str, Any]:
    return inventory.delete_inventory_level(location_id, inventory_item_id, api_version=api_version)


@mcp.tool()
def list_locations(api_version: str = "2026-01", limit: Optional[int] = None) -> Dict[str, Any]:
    return inventory.list_locations(api_version=api_version, limit=limit)


@mcp.tool()
def get_location(location_id: int, api_version: str = "2026-01") -> Dict[str, Any]:
    return inventory.get_location(location_id, api_version=api_version)


@mcp.tool()
def count_locations(api_version: str = "2026-01") -> Dict[str, Any]:
    return inventory.count_locations(api_version=api_version)


@mcp.tool()
def list_location_inventory_levels(location_id: int, api_version: str = "2026-01", limit: Optional[int] = None, updated_at_min: Optional[str] = None) -> Dict[str, Any]:
    return inventory.list_location_inventory_levels(location_id, api_version=api_version, limit=limit, updated_at_min=updated_at_min)


# Discounts
@mcp.tool()
def create_price_rule(price_rule: Dict[str, Any], api_version: str = "2026-01") -> Dict[str, Any]:
    return discounts.create_price_rule(price_rule, api_version=api_version)


@mcp.tool()
def list_price_rules(api_version: str = "2026-01", limit: Optional[int] = None, since_id: Optional[int] = None) -> Dict[str, Any]:
    return discounts.list_price_rules(api_version=api_version, limit=limit, since_id=since_id)


@mcp.tool()
def get_price_rule(price_rule_id: int, api_version: str = "2026-01") -> Dict[str, Any]:
    return discounts.get_price_rule(price_rule_id, api_version=api_version)


@mcp.tool()
def count_price_rules(api_version: str = "2026-01") -> Dict[str, Any]:
    return discounts.count_price_rules(api_version=api_version)


@mcp.tool()
def update_price_rule(price_rule_id: int, price_rule: Dict[str, Any], api_version: str = "2026-01") -> Dict[str, Any]:
    return discounts.update_price_rule(price_rule_id, price_rule, api_version=api_version)


@mcp.tool()
def delete_price_rule(price_rule_id: int, api_version: str = "2026-01") -> Dict[str, Any]:
    return discounts.delete_price_rule(price_rule_id, api_version=api_version)


@mcp.tool()
def create_discount_code(price_rule_id: int, discount_code: Dict[str, Any], api_version: str = "2026-01") -> Dict[str, Any]:
    return discounts.create_discount_code(price_rule_id, discount_code, api_version=api_version)


@mcp.tool()
def list_discount_codes(price_rule_id: int, api_version: str = "2026-01", limit: Optional[int] = None, since_id: Optional[int] = None) -> Dict[str, Any]:
    return discounts.list_discount_codes(price_rule_id, api_version=api_version, limit=limit, since_id=since_id)


@mcp.tool()
def get_discount_code(price_rule_id: int, discount_code_id: int, api_version: str = "2026-01") -> Dict[str, Any]:
    return discounts.get_discount_code(price_rule_id, discount_code_id, api_version=api_version)


@mcp.tool()
def update_discount_code(price_rule_id: int, discount_code_id: int, discount_code: Dict[str, Any], api_version: str = "2026-01") -> Dict[str, Any]:
    return discounts.update_discount_code(price_rule_id, discount_code_id, discount_code, api_version=api_version)


@mcp.tool()
def delete_discount_code(price_rule_id: int, discount_code_id: int, api_version: str = "2026-01") -> Dict[str, Any]:
    return discounts.delete_discount_code(price_rule_id, discount_code_id, api_version=api_version)


@mcp.tool()
def create_discount_code_batch(price_rule_id: int, discount_codes: list[Dict[str, Any]], api_version: str = "2026-01") -> Dict[str, Any]:
    return discounts.create_discount_code_batch(price_rule_id, discount_codes, api_version=api_version)


@mcp.tool()
def get_discount_code_batch(price_rule_id: int, batch_id: int, api_version: str = "2026-01") -> Dict[str, Any]:
    return discounts.get_discount_code_batch(price_rule_id, batch_id, api_version=api_version)


@mcp.tool()
def list_discount_codes_for_batch(price_rule_id: int, batch_id: int, api_version: str = "2026-01") -> Dict[str, Any]:
    return discounts.list_discount_codes_for_batch(price_rule_id, batch_id, api_version=api_version)


@mcp.tool()
def count_discount_codes(api_version: str = "2026-01", times_used: Optional[int] = None, times_used_min: Optional[int] = None, times_used_max: Optional[int] = None) -> Dict[str, Any]:
    return discounts.count_discount_codes(api_version=api_version, times_used=times_used, times_used_min=times_used_min, times_used_max=times_used_max)


@mcp.tool()
def lookup_discount_code(code: str, api_version: str = "2026-01") -> Dict[str, Any]:
    return discounts.lookup_discount_code(code, api_version=api_version)


# Webhooks
@mcp.tool()
def create_webhook(webhook: Dict[str, Any], api_version: str = "2026-01") -> Dict[str, Any]:
    return webhooks.create_webhook(webhook, api_version=api_version)


@mcp.tool()
def list_webhooks(api_version: str = "2026-01", address: Optional[str] = None, topic: Optional[str] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    return webhooks.list_webhooks(api_version=api_version, address=address, topic=topic, fields=fields)


@mcp.tool()
def get_webhook(webhook_id: int, api_version: str = "2026-01", fields: Optional[str] = None) -> Dict[str, Any]:
    return webhooks.get_webhook(webhook_id, api_version=api_version, fields=fields)


@mcp.tool()
def count_webhooks(api_version: str = "2026-01", topic: Optional[str] = None, address: Optional[str] = None) -> Dict[str, Any]:
    return webhooks.count_webhooks(api_version=api_version, topic=topic, address=address)


@mcp.tool()
def update_webhook(webhook_id: int, webhook: Dict[str, Any], api_version: str = "2026-01") -> Dict[str, Any]:
    return webhooks.update_webhook(webhook_id, webhook, api_version=api_version)


@mcp.tool()
def delete_webhook(webhook_id: int, api_version: str = "2026-01") -> Dict[str, Any]:
    return webhooks.delete_webhook(webhook_id, api_version=api_version)


# Metafields
@mcp.tool()
def create_product_metafield(product_id: int, metafield: Dict[str, Any], api_version: str = "2026-01") -> Dict[str, Any]:
    return metafields.create_product_metafield(product_id, metafield, api_version=api_version)


@mcp.tool()
def list_product_metafields(product_id: int, api_version: str = "2026-01", namespace: Optional[str] = None, key: Optional[str] = None) -> Dict[str, Any]:
    return metafields.list_product_metafields(product_id, api_version=api_version, namespace=namespace, key=key)


@mcp.tool()
def get_product_metafield(product_id: int, metafield_id: int, api_version: str = "2026-01") -> Dict[str, Any]:
    return metafields.get_product_metafield(product_id, metafield_id, api_version=api_version)


@mcp.tool()
def update_product_metafield(product_id: int, metafield_id: int, metafield: Dict[str, Any], api_version: str = "2026-01") -> Dict[str, Any]:
    return metafields.update_product_metafield(product_id, metafield_id, metafield, api_version=api_version)


@mcp.tool()
def delete_product_metafield(product_id: int, metafield_id: int, api_version: str = "2026-01") -> Dict[str, Any]:
    return metafields.delete_product_metafield(product_id, metafield_id, api_version=api_version)


@mcp.tool()
def create_variant_metafield(variant_id: int, metafield: Dict[str, Any], api_version: str = "2026-01") -> Dict[str, Any]:
    return metafields.create_variant_metafield(variant_id, metafield, api_version=api_version)


@mcp.tool()
def list_variant_metafields(variant_id: int, api_version: str = "2026-01", namespace: Optional[str] = None, key: Optional[str] = None) -> Dict[str, Any]:
    return metafields.list_variant_metafields(variant_id, api_version=api_version, namespace=namespace, key=key)


@mcp.tool()
def create_order_metafield(order_id: int, metafield: Dict[str, Any], api_version: str = "2026-01") -> Dict[str, Any]:
    return metafields.create_order_metafield(order_id, metafield, api_version=api_version)


@mcp.tool()
def list_order_metafields(order_id: int, api_version: str = "2026-01", namespace: Optional[str] = None, key: Optional[str] = None) -> Dict[str, Any]:
    return metafields.list_order_metafields(order_id, api_version=api_version, namespace=namespace, key=key)


@mcp.tool()
def create_customer_metafield(customer_id: int, metafield: Dict[str, Any], api_version: str = "2026-01") -> Dict[str, Any]:
    return metafields.create_customer_metafield(customer_id, metafield, api_version=api_version)


@mcp.tool()
def list_customer_metafields(customer_id: int, api_version: str = "2026-01", namespace: Optional[str] = None, key: Optional[str] = None) -> Dict[str, Any]:
    return metafields.list_customer_metafields(customer_id, api_version=api_version, namespace=namespace, key=key)


@mcp.tool()
def list_shop_metafields(api_version: str = "2026-01", namespace: Optional[str] = None, key: Optional[str] = None) -> Dict[str, Any]:
    return metafields.list_shop_metafields(api_version=api_version, namespace=namespace, key=key)


if __name__ == "__main__":
    mcp.run()
