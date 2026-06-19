# Generated tools

This server intentionally exposes a **generic** Shopify Admin REST tool (`shopify_request`) plus a small set of convenience tools for common workflows.

Why not generate one tool per endpoint?
- Shopify Admin REST has a very large surface area.
- A generic request tool provides comprehensive coverage immediately, while still allowing higher-level helpers for common tasks.

If you want additional convenience tools, add thin wrappers that call `shopify_request`.
