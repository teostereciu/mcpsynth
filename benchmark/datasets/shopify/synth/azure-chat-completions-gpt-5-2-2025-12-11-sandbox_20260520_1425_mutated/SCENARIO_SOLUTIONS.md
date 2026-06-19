# Scenario solutions (Shopify Admin REST MCP)

## Auth / configuration

Set environment variables:

- `SHOPIFY_SHOP` (e.g. `your-store.myshopify.com` or `your-store`)
- `SHOPIFY_ACCESS_TOKEN`
- `SHOPIFY_API_VERSION` (default `2026-01`)

All tools also accept `shop`, `access_token`, and `api_version` overrides.

---

## 1) List recent paid orders

Tool: `orders_list`

Example input:
```json
{
  "query": {
    "status": "any",
    "financial_status": "paid",
    "limit": 50
  }
}
```

Pagination: use the returned `link` header to follow `rel="next"`.

---

## 2) Get a specific order

Tool: `orders_get`

```json
{ "order_id": "450789469" }
```

---

## 3) Find customers by email

Tool: `customers_list`

```json
{ "query": { "email": "alice@example.com", "limit": 50 } }
```

---

## 4) Set inventory for an item at a location

Tool: `inventory_levels_set`

```json
{
  "inventory_item_id": "808950810",
  "location_id": "49202758",
  "available": 25
}
```

---

## 5) Create a webhook

Tool: `webhooks_create`

```json
{
  "topic": "orders/create",
  "address": "https://example.com/webhooks/orders-create",
  "format": "json"
}
```

---

## 6) Call any endpoint not covered by convenience tools

Tool: `shopify_request`

Example: create a custom collection (from docs `CustomCollection`):

```json
{
  "method": "POST",
  "path": "/custom_collections.json",
  "body": {
    "custom_collection": {
      "title": "IPods"
    }
  }
}
```

Example: list fulfillments for an order (from docs `Fulfillment`):

```json
{
  "method": "GET",
  "path": "/orders/450789469/fulfillments.json"
}
```
