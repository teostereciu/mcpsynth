# Generated tools

This server exposes:

- `shopify_admin_request`: a generic Admin REST caller for any documented endpoint.
- Convenience tools for common workflows:
  - `orders_list`, `orders_get`, `orders_create`, `orders_update`, `orders_cancel`
  - `customers_list`, `customers_get`, `customers_create`
  - `products_list`, `products_get`
  - `locations_list`, `inventory_levels_list`
  - `webhooks_list`, `webhooks_create`, `webhooks_delete`

Because Shopify Admin REST has a very large surface area, comprehensive coverage is achieved via the generic request tool, which can call any endpoint from the docs by providing the correct `path`, `method`, `query`, and `body`.
