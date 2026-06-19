import json
from typing import Any, Dict

from mcp.server.fastmcp import FastMCP

from generated_tools import customers, discounts, fulfillment, inventory, orders, products, webhooks_metafields

mcp = FastMCP("shopify-admin-rest")


def _unwrap(result: Dict[str, Any]) -> Any:
    # Keep full envelope for pagination headers, but surface errors cleanly.
    return result


# Products
@mcp.tool()
def list_products(**kwargs):
    return _unwrap(products.list_products(**kwargs))


@mcp.tool()
def get_product(product_id: int, fields: str | None = None):
    return _unwrap(products.get_product(product_id=product_id, fields=fields))


@mcp.tool()
def count_products(status: str | None = None, vendor: str | None = None, product_type: str | None = None):
    return _unwrap(products.count_products(status=status, vendor=vendor, product_type=product_type))


@mcp.tool()
def create_product(product: Dict[str, Any]):
    return _unwrap(products.create_product(product=product))


@mcp.tool()
def update_product(product_id: int, product: Dict[str, Any]):
    return _unwrap(products.update_product(product_id=product_id, product=product))


@mcp.tool()
def delete_product(product_id: int):
    return _unwrap(products.delete_product(product_id=product_id))


@mcp.tool()
def list_product_variants(product_id: int, limit: int | None = 50, since_id: int | None = None, fields: str | None = None):
    return _unwrap(products.list_product_variants(product_id=product_id, limit=limit, since_id=since_id, fields=fields))


@mcp.tool()
def get_variant(variant_id: int, fields: str | None = None):
    return _unwrap(products.get_variant(variant_id=variant_id, fields=fields))


@mcp.tool()
def create_variant(product_id: int, variant: Dict[str, Any]):
    return _unwrap(products.create_variant(product_id=product_id, variant=variant))


@mcp.tool()
def update_variant(variant_id: int, variant: Dict[str, Any]):
    return _unwrap(products.update_variant(variant_id=variant_id, variant=variant))


@mcp.tool()
def delete_variant(product_id: int, variant_id: int):
    return _unwrap(products.delete_variant(product_id=product_id, variant_id=variant_id))


# Orders + Draft orders
@mcp.tool()
def list_orders(**kwargs):
    return _unwrap(orders.list_orders(**kwargs))


@mcp.tool()
def get_order(order_id: int, fields: str | None = None):
    return _unwrap(orders.get_order(order_id=order_id, fields=fields))


@mcp.tool()
def count_orders(status: str = "any", financial_status: str | None = None, fulfillment_status: str | None = None):
    return _unwrap(orders.count_orders(status=status, financial_status=financial_status, fulfillment_status=fulfillment_status))


@mcp.tool()
def create_order(order: Dict[str, Any]):
    return _unwrap(orders.create_order(order=order))


@mcp.tool()
def update_order(order_id: int, order: Dict[str, Any]):
    return _unwrap(orders.update_order(order_id=order_id, order=order))


@mcp.tool()
def delete_order(order_id: int):
    return _unwrap(orders.delete_order(order_id=order_id))


@mcp.tool()
def cancel_order(order_id: int, amount: str | None = None, email: bool | None = None, reason: str | None = None, restock: bool | None = None):
    return _unwrap(orders.cancel_order(order_id=order_id, amount=amount, email=email, reason=reason, restock=restock))


@mcp.tool()
def close_order(order_id: int):
    return _unwrap(orders.close_order(order_id=order_id))


@mcp.tool()
def open_order(order_id: int):
    return _unwrap(orders.open_order(order_id=order_id))


@mcp.tool()
def list_draft_orders(limit: int | None = 50, since_id: int | None = None, status: str | None = None):
    return _unwrap(orders.list_draft_orders(limit=limit, since_id=since_id, status=status))


@mcp.tool()
def get_draft_order(draft_order_id: int):
    return _unwrap(orders.get_draft_order(draft_order_id=draft_order_id))


@mcp.tool()
def count_draft_orders():
    return _unwrap(orders.count_draft_orders())


@mcp.tool()
def create_draft_order(draft_order: Dict[str, Any]):
    return _unwrap(orders.create_draft_order(draft_order=draft_order))


@mcp.tool()
def update_draft_order(draft_order_id: int, draft_order: Dict[str, Any]):
    return _unwrap(orders.update_draft_order(draft_order_id=draft_order_id, draft_order=draft_order))


@mcp.tool()
def delete_draft_order(draft_order_id: int):
    return _unwrap(orders.delete_draft_order(draft_order_id=draft_order_id))


@mcp.tool()
def send_draft_order_invoice(draft_order_id: int, invoice: Dict[str, Any] | None = None):
    return _unwrap(orders.send_draft_order_invoice(draft_order_id=draft_order_id, invoice=invoice))


@mcp.tool()
def complete_draft_order(draft_order_id: int, payment_pending: bool | None = None):
    return _unwrap(orders.complete_draft_order(draft_order_id=draft_order_id, payment_pending=payment_pending))


# Customers + addresses
@mcp.tool()
def list_customers(**kwargs):
    return _unwrap(customers.list_customers(**kwargs))


@mcp.tool()
def search_customers(query: str, limit: int | None = 50, fields: str | None = None):
    return _unwrap(customers.search_customers(query=query, limit=limit, fields=fields))


@mcp.tool()
def get_customer(customer_id: int, fields: str | None = None):
    return _unwrap(customers.get_customer(customer_id=customer_id, fields=fields))


@mcp.tool()
def count_customers():
    return _unwrap(customers.count_customers())


@mcp.tool()
def create_customer(customer: Dict[str, Any]):
    return _unwrap(customers.create_customer(customer=customer))


@mcp.tool()
def update_customer(customer_id: int, customer: Dict[str, Any]):
    return _unwrap(customers.update_customer(customer_id=customer_id, customer=customer))


@mcp.tool()
def get_customer_orders(customer_id: int, limit: int | None = 50, since_id: int | None = None, fields: str | None = None):
    return _unwrap(customers.get_customer_orders(customer_id=customer_id, limit=limit, since_id=since_id, fields=fields))


@mcp.tool()
def create_account_activation_url(customer_id: int):
    return _unwrap(customers.create_account_activation_url(customer_id=customer_id))


@mcp.tool()
def send_customer_invite(customer_id: int, invite: Dict[str, Any] | None = None):
    return _unwrap(customers.send_customer_invite(customer_id=customer_id, invite=invite))


@mcp.tool()
def list_customer_addresses(customer_id: int, limit: int | None = None):
    return _unwrap(customers.list_customer_addresses(customer_id=customer_id, limit=limit))


@mcp.tool()
def get_customer_address(customer_id: int, address_id: int):
    return _unwrap(customers.get_customer_address(customer_id=customer_id, address_id=address_id))


@mcp.tool()
def create_customer_address(customer_id: int, address: Dict[str, Any]):
    return _unwrap(customers.create_customer_address(customer_id=customer_id, address=address))


@mcp.tool()
def update_customer_address(customer_id: int, address_id: int, address: Dict[str, Any]):
    return _unwrap(customers.update_customer_address(customer_id=customer_id, address_id=address_id, address=address))


@mcp.tool()
def set_default_customer_address(customer_id: int, address_id: int):
    return _unwrap(customers.set_default_customer_address(customer_id=customer_id, address_id=address_id))


@mcp.tool()
def delete_customer_address(customer_id: int, address_id: int):
    return _unwrap(customers.delete_customer_address(customer_id=customer_id, address_id=address_id))


@mcp.tool()
def bulk_customer_addresses(customer_id: int, address_ids: list[int], operation: str):
    return _unwrap(customers.bulk_customer_addresses(customer_id=customer_id, address_ids=address_ids, operation=operation))


# Inventory
@mcp.tool()
def list_inventory_items(ids: str, limit: int | None = 50):
    return _unwrap(inventory.list_inventory_items(ids=ids, limit=limit))


@mcp.tool()
def get_inventory_item(inventory_item_id: int):
    return _unwrap(inventory.get_inventory_item(inventory_item_id=inventory_item_id))


@mcp.tool()
def update_inventory_item(inventory_item_id: int, inventory_item: Dict[str, Any]):
    return _unwrap(inventory.update_inventory_item(inventory_item_id=inventory_item_id, inventory_item=inventory_item))


@mcp.tool()
def list_inventory_levels(location_ids: str | None = None, inventory_item_ids: str | None = None, limit: int | None = 50, updated_at_min: str | None = None):
    return _unwrap(inventory.list_inventory_levels(location_ids=location_ids, inventory_item_ids=inventory_item_ids, limit=limit, updated_at_min=updated_at_min))


@mcp.tool()
def adjust_inventory_level(location_id: int, inventory_item_id: int, available_adjustment: int):
    return _unwrap(inventory.adjust_inventory_level(location_id=location_id, inventory_item_id=inventory_item_id, available_adjustment=available_adjustment))


@mcp.tool()
def set_inventory_level(location_id: int, inventory_item_id: int, available: int, disconnect_if_necessary: bool | None = None):
    return _unwrap(inventory.set_inventory_level(location_id=location_id, inventory_item_id=inventory_item_id, available=available, disconnect_if_necessary=disconnect_if_necessary))


@mcp.tool()
def connect_inventory_level(location_id: int, inventory_item_id: int, relocate_if_necessary: bool | None = None):
    return _unwrap(inventory.connect_inventory_level(location_id=location_id, inventory_item_id=inventory_item_id, relocate_if_necessary=relocate_if_necessary))


@mcp.tool()
def delete_inventory_level(inventory_item_id: int, location_id: int):
    return _unwrap(inventory.delete_inventory_level(inventory_item_id=inventory_item_id, location_id=location_id))


# Locations + fulfillment orders
@mcp.tool()
def list_locations(limit: int | None = 50):
    return _unwrap(fulfillment.list_locations(limit=limit))


@mcp.tool()
def get_location(location_id: int):
    return _unwrap(fulfillment.get_location(location_id=location_id))


@mcp.tool()
def count_locations():
    return _unwrap(fulfillment.count_locations())


@mcp.tool()
def list_location_inventory_levels(location_id: int):
    return _unwrap(fulfillment.list_location_inventory_levels(location_id=location_id))


@mcp.tool()
def list_fulfillment_orders_for_order(order_id: int):
    return _unwrap(fulfillment.list_fulfillment_orders_for_order(order_id=order_id))


@mcp.tool()
def get_fulfillment_order(fulfillment_order_id: int):
    return _unwrap(fulfillment.get_fulfillment_order(fulfillment_order_id=fulfillment_order_id))


@mcp.tool()
def cancel_fulfillment_order(fulfillment_order_id: int, message: str | None = None):
    return _unwrap(fulfillment.cancel_fulfillment_order(fulfillment_order_id=fulfillment_order_id, message=message))


@mcp.tool()
def close_fulfillment_order(fulfillment_order_id: int, message: str | None = None):
    return _unwrap(fulfillment.close_fulfillment_order(fulfillment_order_id=fulfillment_order_id, message=message))


@mcp.tool()
def open_fulfillment_order(fulfillment_order_id: int):
    return _unwrap(fulfillment.open_fulfillment_order(fulfillment_order_id=fulfillment_order_id))


@mcp.tool()
def hold_fulfillment_order(fulfillment_order_id: int, hold: Dict[str, Any]):
    return _unwrap(fulfillment.hold_fulfillment_order(fulfillment_order_id=fulfillment_order_id, hold=hold))


@mcp.tool()
def release_fulfillment_order_hold(fulfillment_order_id: int):
    return _unwrap(fulfillment.release_fulfillment_order_hold(fulfillment_order_id=fulfillment_order_id))


@mcp.tool()
def move_fulfillment_order(fulfillment_order_id: int, new_location_id: int):
    return _unwrap(fulfillment.move_fulfillment_order(fulfillment_order_id=fulfillment_order_id, new_location_id=new_location_id))


@mcp.tool()
def reschedule_fulfillment_order(fulfillment_order_id: int, fulfill_at: str):
    return _unwrap(fulfillment.reschedule_fulfillment_order(fulfillment_order_id=fulfillment_order_id, fulfill_at=fulfill_at))


@mcp.tool()
def set_fulfillment_orders_deadline(fulfillment_order_ids: list[int], fulfill_by: str):
    return _unwrap(fulfillment.set_fulfillment_orders_deadline(fulfillment_order_ids=fulfillment_order_ids, fulfill_by=fulfill_by))


# Webhooks
@mcp.tool()
def list_webhooks(limit: int | None = 50, since_id: int | None = None, topic: str | None = None):
    return _unwrap(webhooks_metafields.list_webhooks(limit=limit, since_id=since_id, topic=topic))


@mcp.tool()
def get_webhook(webhook_id: int):
    return _unwrap(webhooks_metafields.get_webhook(webhook_id=webhook_id))


@mcp.tool()
def count_webhooks(topic: str | None = None):
    return _unwrap(webhooks_metafields.count_webhooks(topic=topic))


@mcp.tool()
def create_webhook(webhook: Dict[str, Any]):
    return _unwrap(webhooks_metafields.create_webhook(webhook=webhook))


@mcp.tool()
def update_webhook(webhook_id: int, webhook: Dict[str, Any]):
    return _unwrap(webhooks_metafields.update_webhook(webhook_id=webhook_id, webhook=webhook))


@mcp.tool()
def delete_webhook(webhook_id: int):
    return _unwrap(webhooks_metafields.delete_webhook(webhook_id=webhook_id))


# Metafields
@mcp.tool()
def list_metafields(owner_resource: str, owner_id: int, limit: int | None = 50):
    return _unwrap(webhooks_metafields.list_metafields(owner_resource=owner_resource, owner_id=owner_id, limit=limit))


@mcp.tool()
def get_metafield(owner_resource: str, owner_id: int, metafield_id: int):
    return _unwrap(webhooks_metafields.get_metafield(owner_resource=owner_resource, owner_id=owner_id, metafield_id=metafield_id))


@mcp.tool()
def count_metafields(owner_resource: str, owner_id: int):
    return _unwrap(webhooks_metafields.count_metafields(owner_resource=owner_resource, owner_id=owner_id))


@mcp.tool()
def create_metafield(owner_resource: str, owner_id: int, metafield: Dict[str, Any]):
    return _unwrap(webhooks_metafields.create_metafield(owner_resource=owner_resource, owner_id=owner_id, metafield=metafield))


@mcp.tool()
def update_metafield(owner_resource: str, owner_id: int, metafield_id: int, metafield: Dict[str, Any]):
    return _unwrap(webhooks_metafields.update_metafield(owner_resource=owner_resource, owner_id=owner_id, metafield_id=metafield_id, metafield=metafield))


@mcp.tool()
def delete_metafield(owner_resource: str, owner_id: int, metafield_id: int):
    return _unwrap(webhooks_metafields.delete_metafield(owner_resource=owner_resource, owner_id=owner_id, metafield_id=metafield_id))


# Discounts
@mcp.tool()
def list_price_rules(limit: int | None = 50, since_id: int | None = None):
    return _unwrap(discounts.list_price_rules(limit=limit, since_id=since_id))


@mcp.tool()
def get_price_rule(price_rule_id: int):
    return _unwrap(discounts.get_price_rule(price_rule_id=price_rule_id))


@mcp.tool()
def count_price_rules():
    return _unwrap(discounts.count_price_rules())


@mcp.tool()
def create_price_rule(price_rule: Dict[str, Any]):
    return _unwrap(discounts.create_price_rule(price_rule=price_rule))


@mcp.tool()
def update_price_rule(price_rule_id: int, price_rule: Dict[str, Any]):
    return _unwrap(discounts.update_price_rule(price_rule_id=price_rule_id, price_rule=price_rule))


@mcp.tool()
def delete_price_rule(price_rule_id: int):
    return _unwrap(discounts.delete_price_rule(price_rule_id=price_rule_id))


@mcp.tool()
def create_discount_code(price_rule_id: int, discount_code: Dict[str, Any]):
    return _unwrap(discounts.create_discount_code(price_rule_id=price_rule_id, discount_code=discount_code))


@mcp.tool()
def list_discount_codes(price_rule_id: int, limit: int | None = 50, since_id: int | None = None):
    return _unwrap(discounts.list_discount_codes(price_rule_id=price_rule_id, limit=limit, since_id=since_id))


@mcp.tool()
def get_discount_code(price_rule_id: int, discount_code_id: int):
    return _unwrap(discounts.get_discount_code(price_rule_id=price_rule_id, discount_code_id=discount_code_id))


@mcp.tool()
def update_discount_code(price_rule_id: int, discount_code_id: int, discount_code: Dict[str, Any]):
    return _unwrap(discounts.update_discount_code(price_rule_id=price_rule_id, discount_code_id=discount_code_id, discount_code=discount_code))


@mcp.tool()
def delete_discount_code(price_rule_id: int, discount_code_id: int):
    return _unwrap(discounts.delete_discount_code(price_rule_id=price_rule_id, discount_code_id=discount_code_id))


@mcp.tool()
def count_discount_codes(times_used: int | None = None, times_used_min: int | None = None, times_used_max: int | None = None):
    return _unwrap(discounts.count_discount_codes(times_used=times_used, times_used_min=times_used_min, times_used_max=times_used_max))


@mcp.tool()
def lookup_discount_code(code: str):
    return _unwrap(discounts.lookup_discount_code(code=code))


@mcp.tool()
def create_discount_code_batch(price_rule_id: int, discount_codes: list[Dict[str, Any]]):
    return _unwrap(discounts.create_discount_code_batch(price_rule_id=price_rule_id, discount_codes=discount_codes))


@mcp.tool()
def get_discount_code_batch(price_rule_id: int, batch_id: int):
    return _unwrap(discounts.get_discount_code_batch(price_rule_id=price_rule_id, batch_id=batch_id))


@mcp.tool()
def list_discount_codes_for_batch(price_rule_id: int, batch_id: int, limit: int | None = 50):
    return _unwrap(discounts.list_discount_codes_for_batch(price_rule_id=price_rule_id, batch_id=batch_id, limit=limit))


if __name__ == "__main__":
    mcp.run()
