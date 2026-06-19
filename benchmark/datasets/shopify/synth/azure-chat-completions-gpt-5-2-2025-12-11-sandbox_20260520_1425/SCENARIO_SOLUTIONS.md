# Scenario solutions (Shopify Admin REST MCP)

## Environment setup

Set:

- `SHOPIFY_SHOP` (e.g. `your-store.myshopify.com` or `your-store`)
- `SHOPIFY_ACCESS_TOKEN` (Admin API access token)
- `SHOPIFY_API_VERSION` (optional, default `2026-01`)

## 1) List recent orders and fetch details

1. List orders:

- Tool: `orders_list`
- Args: `{ "status": "any", "limit": 50 }`

2. Fetch one order:

- Tool: `orders_get`
- Args: `{ "order_id": "450789469", "fields": "id,name,line_items,total_price" }`

## 2) Create an order (manual order)

- Tool: `orders_create`
- Args:

```json
{
  "order": {
    "email": "customer@example.com",
    "line_items": [
      {"title": "Big Brown Bear Boots", "price": 74.99, "quantity": 1}
    ],
    "send_receipt": false,
    "send_fulfillment_receipt": false
  }
}
```

## 3) Cancel an order

- Tool: `orders_cancel`
- Args: `{ "order_id": "450789469", "reason": "customer" }`

(Any additional request body fields supported by Shopify can be passed as extra args.)

## 4) Create a webhook subscription

- Tool: `webhooks_create`
- Args:

```json
{
  "webhook": {
    "topic": "orders/create",
    "address": "https://example.com/webhooks/orders-create",
    "format": "json"
  }
}
```

## 5) Use an endpoint not covered by a convenience tool

Use `shopify_admin_request`.

Example: calculate a refund (from Refund docs):

- Method: `POST`
- Path: `/orders/{order_id}/refunds/calculate.json`

```json
{
  "method": "POST",
  "path": "/orders/450789469/refunds/calculate.json",
  "body": {
    "refund": {
      "shipping": {"full_refund": true},
      "refund_line_items": [
        {"line_item_id": 518995019, "quantity": 1, "restock_type": "return", "location_id": 487838322}
      ]
    }
  }
}
```

## 6) Pagination

Shopify REST pagination uses the `Link` response header. The server returns it under `headers.link`.

- Parse the `Link` header for `rel="next"` and call `shopify_admin_request` with the `page_info` query parameter from that URL.

Example:

1. First call:

```json
{ "method": "GET", "path": "/orders.json", "query": {"limit": 50, "status": "any"} }
```

2. Next call (example):

```json
{ "method": "GET", "path": "/orders.json", "query": {"limit": 50, "status": "any", "page_info": "<from Link header>"} }
```
