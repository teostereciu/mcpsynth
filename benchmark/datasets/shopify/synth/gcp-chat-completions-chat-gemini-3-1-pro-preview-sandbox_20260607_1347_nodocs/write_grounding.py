import json

data = {
  "get_products": {
    "doc": "general knowledge",
    "endpoint": "GET /products.json"
  },
  "get_product": {
    "doc": "general knowledge",
    "endpoint": "GET /products/{id}.json"
  },
  "create_product": {
    "doc": "general knowledge",
    "endpoint": "POST /products.json"
  },
  "update_product": {
    "doc": "general knowledge",
    "endpoint": "PUT /products/{id}.json"
  },
  "delete_product": {
    "doc": "general knowledge",
    "endpoint": "DELETE /products/{id}.json"
  },
  "get_product_variants": {
    "doc": "general knowledge",
    "endpoint": "GET /products/{id}/variants.json"
  },
  "create_product_variant": {
    "doc": "general knowledge",
    "endpoint": "POST /products/{id}/variants.json"
  },
  "get_product_images": {
    "doc": "general knowledge",
    "endpoint": "GET /products/{id}/images.json"
  },
  "create_product_image": {
    "doc": "general knowledge",
    "endpoint": "POST /products/{id}/images.json"
  },
  "get_orders": {
    "doc": "general knowledge",
    "endpoint": "GET /orders.json"
  },
  "get_order": {
    "doc": "general knowledge",
    "endpoint": "GET /orders/{id}.json"
  },
  "create_order": {
    "doc": "general knowledge",
    "endpoint": "POST /orders.json"
  },
  "update_order": {
    "doc": "general knowledge",
    "endpoint": "PUT /orders/{id}.json"
  },
  "delete_order": {
    "doc": "general knowledge",
    "endpoint": "DELETE /orders/{id}.json"
  },
  "get_draft_orders": {
    "doc": "general knowledge",
    "endpoint": "GET /draft_orders.json"
  },
  "create_draft_order": {
    "doc": "general knowledge",
    "endpoint": "POST /draft_orders.json"
  },
  "calculate_refund": {
    "doc": "general knowledge",
    "endpoint": "POST /orders/{id}/refunds/calculate.json"
  },
  "create_refund": {
    "doc": "general knowledge",
    "endpoint": "POST /orders/{id}/refunds.json"
  },
  "get_transactions": {
    "doc": "general knowledge",
    "endpoint": "GET /orders/{id}/transactions.json"
  },
  "create_transaction": {
    "doc": "general knowledge",
    "endpoint": "POST /orders/{id}/transactions.json"
  },
  "get_fulfillment_orders": {
    "doc": "general knowledge",
    "endpoint": "GET /orders/{id}/fulfillment_orders.json"
  },
  "create_fulfillment": {
    "doc": "general knowledge",
    "endpoint": "POST /fulfillments.json"
  },
  "get_customers": {
    "doc": "general knowledge",
    "endpoint": "GET /customers.json"
  },
  "get_customer": {
    "doc": "general knowledge",
    "endpoint": "GET /customers/{id}.json"
  },
  "create_customer": {
    "doc": "general knowledge",
    "endpoint": "POST /customers.json"
  },
  "update_customer": {
    "doc": "general knowledge",
    "endpoint": "PUT /customers/{id}.json"
  },
  "delete_customer": {
    "doc": "general knowledge",
    "endpoint": "DELETE /customers/{id}.json"
  },
  "get_inventory_items": {
    "doc": "general knowledge",
    "endpoint": "GET /inventory_items.json"
  },
  "get_inventory_levels": {
    "doc": "general knowledge",
    "endpoint": "GET /inventory_levels.json"
  },
  "set_inventory_level": {
    "doc": "general knowledge",
    "endpoint": "POST /inventory_levels/set.json"
  },
  "get_locations": {
    "doc": "general knowledge",
    "endpoint": "GET /locations.json"
  },
  "get_custom_collections": {
    "doc": "general knowledge",
    "endpoint": "GET /custom_collections.json"
  },
  "get_smart_collections": {
    "doc": "general knowledge",
    "endpoint": "GET /smart_collections.json"
  },
  "get_price_rules": {
    "doc": "general knowledge",
    "endpoint": "GET /price_rules.json"
  },
  "create_price_rule": {
    "doc": "general knowledge",
    "endpoint": "POST /price_rules.json"
  },
  "get_discount_codes": {
    "doc": "general knowledge",
    "endpoint": "GET /price_rules/{id}/discount_codes.json"
  },
  "create_discount_code": {
    "doc": "general knowledge",
    "endpoint": "POST /price_rules/{id}/discount_codes.json"
  },
  "get_webhooks": {
    "doc": "general knowledge",
    "endpoint": "GET /webhooks.json"
  },
  "create_webhook": {
    "doc": "general knowledge",
    "endpoint": "POST /webhooks.json"
  },
  "get_metafields": {
    "doc": "general knowledge",
    "endpoint": "GET /metafields.json"
  },
  "create_metafield": {
    "doc": "general knowledge",
    "endpoint": "POST /metafields.json"
  }
}

with open("grounding.json", "w") as f:
    json.dump(data, f, indent=2)
