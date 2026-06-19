from typing import Any, Dict, Optional

from generated_tools.shopify_client import ShopifyClient

client = ShopifyClient()


def _wrap(resource: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    return {resource: payload}


def list_products(params: Optional[Dict[str, Any]] = None):
    return client.request("GET", "/products.json", params=params)


def get_product(product_id: int, params: Optional[Dict[str, Any]] = None):
    return client.request("GET", f"/products/{product_id}.json", params=params)


def create_product(product: Dict[str, Any]):
    return client.request("POST", "/products.json", json={"product": product})


def update_product(product_id: int, product: Dict[str, Any]):
    return client.request("PUT", f"/products/{product_id}.json", json={"product": product})


def delete_product(product_id: int):
    return client.request("DELETE", f"/products/{product_id}.json")


def list_orders(params: Optional[Dict[str, Any]] = None):
    return client.request("GET", "/orders.json", params=params)


def get_order(order_id: int, params: Optional[Dict[str, Any]] = None):
    return client.request("GET", f"/orders/{order_id}.json", params=params)


def create_order(order: Dict[str, Any]):
    return client.request("POST", "/orders.json", json={"order": order})


def update_order(order_id: int, order: Dict[str, Any]):
    return client.request("PUT", f"/orders/{order_id}.json", json={"order": order})


def cancel_order(order_id: int, body: Dict[str, Any]):
    return client.request("POST", f"/orders/{order_id}/cancel.json", json=body)


def close_order(order_id: int):
    return client.request("POST", f"/orders/{order_id}/close.json")


def open_order(order_id: int):
    return client.request("POST", f"/orders/{order_id}/open.json")


def list_customers(params: Optional[Dict[str, Any]] = None):
    return client.request("GET", "/customers.json", params=params)


def get_customer(customer_id: int, params: Optional[Dict[str, Any]] = None):
    return client.request("GET", f"/customers/{customer_id}.json", params=params)


def create_customer(customer: Dict[str, Any]):
    return client.request("POST", "/customers.json", json={"customer": customer})


def update_customer(customer_id: int, customer: Dict[str, Any]):
    return client.request("PUT", f"/customers/{customer_id}.json", json={"customer": customer})


def list_inventory_levels(params: Optional[Dict[str, Any]] = None):
    return client.request("GET", "/inventory_levels.json", params=params)


def adjust_inventory_level(body: Dict[str, Any]):
    return client.request("POST", "/inventory_levels/adjust.json", json=body)


def connect_inventory_level(body: Dict[str, Any]):
    return client.request("POST", "/inventory_levels/connect.json", json=body)


def set_inventory_level(body: Dict[str, Any]):
    return client.request("POST", "/inventory_levels/set.json", json=body)


def delete_inventory_level(params: Dict[str, Any]):
    return client.request("DELETE", "/inventory_levels.json", params=params)


def list_fulfillment_orders(order_id: int):
    return client.request("GET", f"/orders/{order_id}/fulfillment_orders.json")


def get_fulfillment_order(fulfillment_order_id: int):
    return client.request("GET", f"/fulfillment_orders/{fulfillment_order_id}.json")


def cancel_fulfillment_order(fulfillment_order_id: int, body: Dict[str, Any]):
    return client.request("POST", f"/fulfillment_orders/{fulfillment_order_id}/cancel.json", json=body)


def hold_fulfillment_order(fulfillment_order_id: int, body: Dict[str, Any]):
    return client.request("POST", f"/fulfillment_orders/{fulfillment_order_id}/hold.json", json=body)


def release_hold_fulfillment_order(fulfillment_order_id: int, body: Dict[str, Any]):
    return client.request("POST", f"/fulfillment_orders/{fulfillment_order_id}/release_hold.json", json=body)


def list_discount_codes(params: Optional[Dict[str, Any]] = None):
    return client.request("GET", "/discount_codes/count.json", params=params)


def create_discount_code(price_rule_id: int, discount_code: Dict[str, Any]):
    return client.request("POST", f"/price_rules/{price_rule_id}/discount_codes.json", json={"discount_code": discount_code})


def create_discount_code_batch(price_rule_id: int, discount_codes: Dict[str, Any]):
    return client.request("POST", f"/price_rules/{price_rule_id}/batch.json", json={"discount_codes": discount_codes})


def list_webhooks(params: Optional[Dict[str, Any]] = None):
    return client.request("GET", "/webhooks.json", params=params)


def create_webhook(webhook: Dict[str, Any]):
    return client.request("POST", "/webhooks.json", json={"webhook": webhook})


def update_webhook(webhook_id: int, webhook: Dict[str, Any]):
    return client.request("PUT", f"/webhooks/{webhook_id}.json", json={"webhook": webhook})


def delete_webhook(webhook_id: int):
    return client.request("DELETE", f"/webhooks/{webhook_id}.json")


def list_metafields(resource: str, resource_id: int, params: Optional[Dict[str, Any]] = None):
    return client.request("GET", f"/{resource}/{resource_id}/metafields.json", params=params)


def create_metafield(resource: str, resource_id: int, metafield: Dict[str, Any]):
    return client.request("POST", f"/{resource}/{resource_id}/metafields.json", json={"metafield": metafield})
