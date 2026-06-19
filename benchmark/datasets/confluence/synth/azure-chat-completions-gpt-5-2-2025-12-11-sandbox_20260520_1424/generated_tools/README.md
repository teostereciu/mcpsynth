# Generated tools

This server intentionally exposes a small set of high-leverage tools plus a generic request tool.

- `confluence_request`: call any Confluence Cloud REST API endpoint (v1 or v2) by method/path.
- Convenience tools cover common agent workflows (search, spaces, pages CRUD, labels, users).

If you need an endpoint not covered by a convenience tool, use `confluence_request`.
