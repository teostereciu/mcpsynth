# Scenario solutions (examples)

These are example tool sequences an autonomous agent can use.

## 1) Create a product with an image
1. `create_product({"title":"T-Shirt","status":"active","variants":[{"price":"19.99","sku":"TS-001"}]})`
2. From the response, take `product.id`.
3. `create_product_image(product_id=<id>, image={"src":"https://example.com/image.jpg"})`

## 2) Adjust inventory for a variant at a location
1. `get_variant(variant_id=...)` → read `variant.inventory_item_id`
2. `list_locations()` → pick a `location.id`
3. `adjust_inventory_level(inventory_item_id=..., location_id=..., available_adjustment=5)`

## 3) Fulfill an order
1. `list_fulfillment_orders(order_id=...)` → choose fulfillment order / line items per your workflow
2. `create_fulfillment({"line_items_by_fulfillment_order":[{"fulfillment_order_id":...,"fulfillment_order_line_items":[{"id":...,"quantity":1}]}],"tracking_info":{"number":"1Z...","company":"UPS"}})`

## 4) Create a draft order and complete it
1. `create_draft_order({"line_items":[{"variant_id":...,"quantity":1}],"customer":{"id":...}})`
2. `complete_draft_order(draft_order_id=..., payment_pending=false)`

## 5) Create a discount code
1. `create_price_rule({"title":"10OFF","target_type":"line_item","target_selection":"all","allocation_method":"across","value_type":"percentage","value":"-10.0","customer_selection":"all","starts_at":"2026-01-01T00:00:00Z"})`
2. `create_discount_code(price_rule_id=..., discount_code={"code":"10OFF"})`

## 6) Add a metafield to a product
1. `create_metafield(resource="products", owner_id=<product_id>, metafield={"namespace":"custom","key":"material","type":"single_line_text_field","value":"cotton"})`
