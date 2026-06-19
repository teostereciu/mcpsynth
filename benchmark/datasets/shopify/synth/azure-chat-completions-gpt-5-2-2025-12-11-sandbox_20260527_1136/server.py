from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.products import (
    count_products,
    create_product,
    create_product_image,
    create_product_variant,
    delete_product,
    delete_product_image,
    delete_variant,
    get_product,
    get_product_image,
    get_variant,
    list_product_images,
    list_product_variants,
    list_products,
    update_product,
    update_product_image,
    update_variant,
)
from generated_tools.orders import (
    cancel_order,
    close_order,
    count_draft_orders,
    count_orders,
    create_draft_order,
    create_order,
    delete_draft_order,
    delete_order,
    get_draft_order,
    get_order,
    list_draft_orders,
    list_orders,
    open_order,
    send_draft_order_invoice,
    complete_draft_order,
    update_draft_order,
    update_order,
)
from generated_tools.customers import (
    bulk_customer_addresses_set,
    count_customers,
    create_customer,
    create_customer_account_activation_url,
    create_customer_address,
    delete_customer_address,
    get_customer_address,
    get_customer_orders,
    list_customer_addresses,
    list_customers,
    search_customers,
    send_customer_invite,
    set_default_customer_address,
    update_customer,
    update_customer_address,
)
from generated_tools.inventory import (
    adjust_inventory_level,
    connect_inventory_level,
    count_locations,
    get_inventory_item,
    get_location,
    list_inventory_items,
    list_inventory_levels,
    list_location_inventory_levels,
    list_locations,
    set_inventory_level,
    delete_inventory_level,
    update_inventory_item,
)
from generated_tools.discounts import (
    count_discount_codes,
    count_price_rules,
    create_discount_code,
    create_discount_code_batch,
    create_price_rule,
    delete_discount_code,
    delete_price_rule,
    get_discount_code,
    get_discount_code_batch,
    get_price_rule,
    list_discount_codes,
    list_discount_codes_for_batch,
    list_price_rules,
    lookup_discount_code,
    update_discount_code,
    update_price_rule,
)
from generated_tools.webhooks_metafields import (
    count_metafields,
    count_webhooks,
    create_metafield,
    create_webhook,
    delete_metafield,
    delete_webhook,
    get_metafield,
    get_webhook,
    list_metafields,
    list_webhooks,
    update_metafield,
    update_webhook,
)


mcp = FastMCP("shopify-admin-rest")


# Products
@mcp.tool()
def shopify_create_product(product: Dict[str, Any]) -> Dict[str, Any]:
    return create_product(product)


@mcp.tool()
def shopify_list_products(
    ids: Optional[str] = None,
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    title: Optional[str] = None,
    vendor: Optional[str] = None,
    handle: Optional[str] = None,
    product_type: Optional[str] = None,
    status: Optional[str] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    published_at_min: Optional[str] = None,
    published_at_max: Optional[str] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    return list_products(
        ids=ids,
        limit=limit,
        since_id=since_id,
        title=title,
        vendor=vendor,
        handle=handle,
        product_type=product_type,
        status=status,
        created_at_min=created_at_min,
        created_at_max=created_at_max,
        updated_at_min=updated_at_min,
        updated_at_max=updated_at_max,
        published_at_min=published_at_min,
        published_at_max=published_at_max,
        fields=fields,
    )


@mcp.tool()
def shopify_get_product(product_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    return get_product(product_id, fields=fields)


@mcp.tool()
def shopify_count_products(status: Optional[str] = None) -> Dict[str, Any]:
    return count_products(status=status)


@mcp.tool()
def shopify_update_product(product_id: int, product: Dict[str, Any]) -> Dict[str, Any]:
    return update_product(product_id, product)


@mcp.tool()
def shopify_delete_product(product_id: int) -> Dict[str, Any]:
    return delete_product(product_id)


@mcp.tool()
def shopify_create_product_variant(product_id: int, variant: Dict[str, Any]) -> Dict[str, Any]:
    return create_product_variant(product_id, variant)


@mcp.tool()
def shopify_list_product_variants(product_id: int, limit: Optional[int] = None, since_id: Optional[int] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    return list_product_variants(product_id, limit=limit, since_id=since_id, fields=fields)


@mcp.tool()
def shopify_get_variant(variant_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    return get_variant(variant_id, fields=fields)


@mcp.tool()
def shopify_update_variant(variant_id: int, variant: Dict[str, Any]) -> Dict[str, Any]:
    return update_variant(variant_id, variant)


@mcp.tool()
def shopify_delete_variant(product_id: int, variant_id: int) -> Dict[str, Any]:
    return delete_variant(product_id, variant_id)


@mcp.tool()
def shopify_create_product_image(product_id: int, image: Dict[str, Any]) -> Dict[str, Any]:
    return create_product_image(product_id, image)


@mcp.tool()
def shopify_list_product_images(product_id: int, limit: Optional[int] = None, since_id: Optional[int] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    return list_product_images(product_id, limit=limit, since_id=since_id, fields=fields)


@mcp.tool()
def shopify_get_product_image(product_id: int, image_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    return get_product_image(product_id, image_id, fields=fields)


@mcp.tool()
def shopify_update_product_image(product_id: int, image_id: int, image: Dict[str, Any]) -> Dict[str, Any]:
    return update_product_image(product_id, image_id, image)


@mcp.tool()
def shopify_delete_product_image(product_id: int, image_id: int) -> Dict[str, Any]:
    return delete_product_image(product_id, image_id)


# Orders
@mcp.tool()
def shopify_create_order(order: Dict[str, Any]) -> Dict[str, Any]:
    return create_order(order)


@mcp.tool()
def shopify_list_orders(
    status: str = "any",
    limit: Optional[int] = None,
    since_id: Optional[int] = None,
    created_at_min: Optional[str] = None,
    created_at_max: Optional[str] = None,
    updated_at_min: Optional[str] = None,
    updated_at_max: Optional[str] = None,
    processed_at_min: Optional[str] = None,
    processed_at_max: Optional[str] = None,
    attribution_app_id: Optional[int] = None,
    fields: Optional[str] = None,
) -> Dict[str, Any]:
    return list_orders(
        status=status,
        limit=limit,
        since_id=since_id,
        created_at_min=created_at_min,
        created_at_max=created_at_max,
        updated_at_min=updated_at_min,
        updated_at_max=updated_at_max,
        processed_at_min=processed_at_min,
        processed_at_max=processed_at_max,
        attribution_app_id=attribution_app_id,
        fields=fields,
    )


@mcp.tool()
def shopify_get_order(order_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    return get_order(order_id, fields=fields)


@mcp.tool()
def shopify_count_orders(status: str = "any") -> Dict[str, Any]:
    return count_orders(status=status)


@mcp.tool()
def shopify_update_order(order_id: int, order: Dict[str, Any]) -> Dict[str, Any]:
    return update_order(order_id, order)


@mcp.tool()
def shopify_delete_order(order_id: int) -> Dict[str, Any]:
    return delete_order(order_id)


@mcp.tool()
def shopify_cancel_order(order_id: int, cancel: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return cancel_order(order_id, cancel)


@mcp.tool()
def shopify_close_order(order_id: int) -> Dict[str, Any]:
    return close_order(order_id)


@mcp.tool()
def shopify_open_order(order_id: int) -> Dict[str, Any]:
    return open_order(order_id)


# Draft orders
@mcp.tool()
def shopify_create_draft_order(draft_order: Dict[str, Any]) -> Dict[str, Any]:
    return create_draft_order(draft_order)


@mcp.tool()
def shopify_list_draft_orders(limit: Optional[int] = None, since_id: Optional[int] = None, updated_at_min: Optional[str] = None, updated_at_max: Optional[str] = None, status: Optional[str] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    return list_draft_orders(limit=limit, since_id=since_id, updated_at_min=updated_at_min, updated_at_max=updated_at_max, status=status, fields=fields)


@mcp.tool()
def shopify_get_draft_order(draft_order_id: int, fields: Optional[str] = None) -> Dict[str, Any]:
    return get_draft_order(draft_order_id, fields=fields)


@mcp.tool()
def shopify_count_draft_orders() -> Dict[str, Any]:
    return count_draft_orders()


@mcp.tool()
def shopify_update_draft_order(draft_order_id: int, draft_order: Dict[str, Any]) -> Dict[str, Any]:
    return update_draft_order(draft_order_id, draft_order)


@mcp.tool()
def shopify_complete_draft_order(draft_order_id: int, payment_pending: Optional[bool] = None) -> Dict[str, Any]:
    return complete_draft_order(draft_order_id, payment_pending=payment_pending)


@mcp.tool()
def shopify_send_draft_order_invoice(draft_order_id: int, invoice: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return send_draft_order_invoice(draft_order_id, invoice)


@mcp.tool()
def shopify_delete_draft_order(draft_order_id: int) -> Dict[str, Any]:
    return delete_draft_order(draft_order_id)


# Customers
@mcp.tool()
def shopify_create_customer(customer: Dict[str, Any]) -> Dict[str, Any]:
    return create_customer(customer)


@mcp.tool()
def shopify_list_customers(ids: Optional[str] = None, limit: Optional[int] = None, since_id: Optional[int] = None, created_at_min: Optional[str] = None, created_at_max: Optional[str] = None, updated_at_min: Optional[str] = None, updated_at_max: Optional[str] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    return list_customers(ids=ids, limit=limit, since_id=since_id, created_at_min=created_at_min, created_at_max=created_at_max, updated_at_min=updated_at_min, updated_at_max=updated_at_max, fields=fields)


@mcp.tool()
def shopify_search_customers(query: str, limit: Optional[int] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    return search_customers(query, limit=limit, fields=fields)


@mcp.tool()
def shopify_count_customers() -> Dict[str, Any]:
    return count_customers()


@mcp.tool()
def shopify_update_customer(customer_id: int, customer: Dict[str, Any]) -> Dict[str, Any]:
    return update_customer(customer_id, customer)


@mcp.tool()
def shopify_get_customer_orders(customer_id: int, limit: Optional[int] = None, since_id: Optional[int] = None, fields: Optional[str] = None) -> Dict[str, Any]:
    return get_customer_orders(customer_id, limit=limit, since_id=since_id, fields=fields)


@mcp.tool()
def shopify_create_customer_account_activation_url(customer_id: int) -> Dict[str, Any]:
    return create_customer_account_activation_url(customer_id)


@mcp.tool()
def shopify_send_customer_invite(customer_id: int, invite: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    return send_customer_invite(customer_id, invite)


@mcp.tool()
def shopify_create_customer_address(customer_id: int, address: Dict[str, Any]) -> Dict[str, Any]:
    return create_customer_address(customer_id, address)


@mcp.tool()
def shopify_list_customer_addresses(customer_id: int, limit: Optional[int] = None) -> Dict[str, Any]:
    return list_customer_addresses(customer_id, limit=limit)


@mcp.tool()
def shopify_get_customer_address(customer_id: int, address_id: int) -> Dict[str, Any]:
    return get_customer_address(customer_id, address_id)


@mcp.tool()
def shopify_update_customer_address(customer_id: int, address_id: int, address: Dict[str, Any]) -> Dict[str, Any]:
    return update_customer_address(customer_id, address_id, address)


@mcp.tool()
def shopify_set_default_customer_address(customer_id: int, address_id: int) -> Dict[str, Any]:
    return set_default_customer_address(customer_id, address_id)


@mcp.tool()
def shopify_bulk_customer_addresses_set(customer_id: int, address_ids: list[int], operation: str) -> Dict[str, Any]:
    return bulk_customer_addresses_set(customer_id, address_ids, operation)


@mcp.tool()
def shopify_delete_customer_address(customer_id: int, address_id: int) -> Dict[str, Any]:
    return delete_customer_address(customer_id, address_id)


# Inventory & locations
@mcp.tool()
def shopify_list_inventory_items(ids: str, limit: Optional[int] = None) -> Dict[str, Any]:
    return list_inventory_items(ids, limit=limit)


@mcp.tool()
def shopify_get_inventory_item(inventory_item_id: int) -> Dict[str, Any]:
    return get_inventory_item(inventory_item_id)


@mcp.tool()
def shopify_update_inventory_item(inventory_item_id: int, inventory_item: Dict[str, Any]) -> Dict[str, Any]:
    return update_inventory_item(inventory_item_id, inventory_item)


@mcp.tool()
def shopify_list_inventory_levels(location_ids: Optional[str] = None, inventory_item_ids: Optional[str] = None, limit: Optional[int] = None) -> Dict[str, Any]:
    return list_inventory_levels(location_ids=location_ids, inventory_item_ids=inventory_item_ids, limit=limit)


@mcp.tool()
def shopify_adjust_inventory_level(location_id: int, inventory_item_id: int, available_adjustment: int) -> Dict[str, Any]:
    return adjust_inventory_level(location_id, inventory_item_id, available_adjustment)


@mcp.tool()
def shopify_connect_inventory_level(location_id: int, inventory_item_id: int, relocate_if_necessary: Optional[bool] = None) -> Dict[str, Any]:
    return connect_inventory_level(location_id, inventory_item_id, relocate_if_necessary=relocate_if_necessary)


@mcp.tool()
def shopify_set_inventory_level(location_id: int, inventory_item_id: int, available: int, disconnect_if_necessary: Optional[bool] = None) -> Dict[str, Any]:
    return set_inventory_level(location_id, inventory_item_id, available, disconnect_if_necessary=disconnect_if_necessary)


@mcp.tool()
def shopify_delete_inventory_level(location_id: int, inventory_item_id: int) -> Dict[str, Any]:
    return delete_inventory_level(location_id, inventory_item_id)


@mcp.tool()
def shopify_list_locations(limit: Optional[int] = None) -> Dict[str, Any]:
    return list_locations(limit=limit)


@mcp.tool()
def shopify_get_location(location_id: int) -> Dict[str, Any]:
    return get_location(location_id)


@mcp.tool()
def shopify_count_locations() -> Dict[str, Any]:
    return count_locations()


@mcp.tool()
def shopify_list_location_inventory_levels(location_id: int) -> Dict[str, Any]:
    return list_location_inventory_levels(location_id)


# Discounts
@mcp.tool()
def shopify_create_price_rule(price_rule: Dict[str, Any]) -> Dict[str, Any]:
    return create_price_rule(price_rule)


@mcp.tool()
def shopify_list_price_rules(limit: Optional[int] = None, since_id: Optional[int] = None) -> Dict[str, Any]:
    return list_price_rules(limit=limit, since_id=since_id)


@mcp.tool()
def shopify_get_price_rule(price_rule_id: int) -> Dict[str, Any]:
    return get_price_rule(price_rule_id)


@mcp.tool()
def shopify_count_price_rules() -> Dict[str, Any]:
    return count_price_rules()


@mcp.tool()
def shopify_update_price_rule(price_rule_id: int, price_rule: Dict[str, Any]) -> Dict[str, Any]:
    return update_price_rule(price_rule_id, price_rule)


@mcp.tool()
def shopify_delete_price_rule(price_rule_id: int) -> Dict[str, Any]:
    return delete_price_rule(price_rule_id)


@mcp.tool()
def shopify_create_discount_code(price_rule_id: int, discount_code: Dict[str, Any]) -> Dict[str, Any]:
    return create_discount_code(price_rule_id, discount_code)


@mcp.tool()
def shopify_list_discount_codes(price_rule_id: int, limit: Optional[int] = None, since_id: Optional[int] = None) -> Dict[str, Any]:
    return list_discount_codes(price_rule_id, limit=limit, since_id=since_id)


@mcp.tool()
def shopify_get_discount_code(price_rule_id: int, discount_code_id: int) -> Dict[str, Any]:
    return get_discount_code(price_rule_id, discount_code_id)


@mcp.tool()
def shopify_update_discount_code(price_rule_id: int, discount_code_id: int, discount_code: Dict[str, Any]) -> Dict[str, Any]:
    return update_discount_code(price_rule_id, discount_code_id, discount_code)


@mcp.tool()
def shopify_delete_discount_code(price_rule_id: int, discount_code_id: int) -> Dict[str, Any]:
    return delete_discount_code(price_rule_id, discount_code_id)


@mcp.tool()
def shopify_create_discount_code_batch(price_rule_id: int, discount_codes: list[Dict[str, Any]]) -> Dict[str, Any]:
    return create_discount_code_batch(price_rule_id, discount_codes)


@mcp.tool()
def shopify_get_discount_code_batch(price_rule_id: int, batch_id: int) -> Dict[str, Any]:
    return get_discount_code_batch(price_rule_id, batch_id)


@mcp.tool()
def shopify_list_discount_codes_for_batch(price_rule_id: int, batch_id: int) -> Dict[str, Any]:
    return list_discount_codes_for_batch(price_rule_id, batch_id)


@mcp.tool()
def shopify_count_discount_codes(times_used: Optional[bool] = None, times_used_min: Optional[int] = None, times_used_max: Optional[int] = None) -> Dict[str, Any]:
    return count_discount_codes(times_used=times_used, times_used_min=times_used_min, times_used_max=times_used_max)


@mcp.tool()
def shopify_lookup_discount_code(code: str) -> Dict[str, Any]:
    return lookup_discount_code(code)


# Webhooks
@mcp.tool()
def shopify_create_webhook(webhook: Dict[str, Any]) -> Dict[str, Any]:
    return create_webhook(webhook)


@mcp.tool()
def shopify_list_webhooks(limit: Optional[int] = None, since_id: Optional[int] = None, topic: Optional[str] = None) -> Dict[str, Any]:
    return list_webhooks(limit=limit, since_id=since_id, topic=topic)


@mcp.tool()
def shopify_get_webhook(webhook_id: int) -> Dict[str, Any]:
    return get_webhook(webhook_id)


@mcp.tool()
def shopify_count_webhooks(topic: Optional[str] = None) -> Dict[str, Any]:
    return count_webhooks(topic=topic)


@mcp.tool()
def shopify_update_webhook(webhook_id: int, webhook: Dict[str, Any]) -> Dict[str, Any]:
    return update_webhook(webhook_id, webhook)


@mcp.tool()
def shopify_delete_webhook(webhook_id: int) -> Dict[str, Any]:
    return delete_webhook(webhook_id)


# Metafields (generic)
@mcp.tool()
def shopify_create_metafield(resource_path_prefix: str, resource_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    return create_metafield(resource_path_prefix, resource_id, metafield)


@mcp.tool()
def shopify_list_metafields(resource_path_prefix: str, resource_id: int, limit: Optional[int] = None, since_id: Optional[int] = None) -> Dict[str, Any]:
    return list_metafields(resource_path_prefix, resource_id, limit=limit, since_id=since_id)


@mcp.tool()
def shopify_get_metafield(resource_path_prefix: str, resource_id: int, metafield_id: int) -> Dict[str, Any]:
    return get_metafield(resource_path_prefix, resource_id, metafield_id)


@mcp.tool()
def shopify_count_metafields(resource_path_prefix: str, resource_id: int) -> Dict[str, Any]:
    return count_metafields(resource_path_prefix, resource_id)


@mcp.tool()
def shopify_update_metafield(resource_path_prefix: str, resource_id: int, metafield_id: int, metafield: Dict[str, Any]) -> Dict[str, Any]:
    return update_metafield(resource_path_prefix, resource_id, metafield_id, metafield)


@mcp.tool()
def shopify_delete_metafield(resource_path_prefix: str, resource_id: int, metafield_id: int) -> Dict[str, Any]:
    return delete_metafield(resource_path_prefix, resource_id, metafield_id)


if __name__ == "__main__":
    mcp.run()
