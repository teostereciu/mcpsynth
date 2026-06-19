# Task: Build an MCP Server for eBay Commerce API

## What You're Building

An MCP server with comprehensive coverage of the eBay Commerce API, suitable for use by an autonomous agent completing real-world tasks.

Choose your implementation language and framework:
- **Python**: FastMCP (`from mcp.server.fastmcp import FastMCP`)
- **TypeScript**: official MCP SDK (`@modelcontextprotocol/sdk`)

The server must run over stdio and expose tools callable via the MCP protocol.

## What You Have

- **48 API endpoint documentation files** in `docs/`
- **Environment variables** for authentication:
  - `EBAY_APP_ID` — application client ID
  - `EBAY_CERT_ID` — application client secret
  - `EBAY_REFRESH_TOKEN` — user refresh token (for user-scoped APIs)
  - `EBAY_ENVIRONMENT` — `SANDBOX` or `PRODUCTION` (default: `SANDBOX`)
- **Base URLs:**
  - Standard APIs: `https://api.sandbox.ebay.com`
  - Media API: `https://apim.sandbox.ebay.com` (different subdomain)

## Authentication

eBay Commerce API uses OAuth 2.0 with **two distinct token types** — you must implement both and use the correct one per API namespace:

**App token (Client Credentials grant — `client_credentials`):**
- Obtain by POSTing to `https://api.sandbox.ebay.com/identity/v1/oauth2/token` with `grant_type=client_credentials` and `scope=https://api.ebay.com/oauth/api_scope`
- Use `Authorization: Bearer <app_token>` header
- **Required for:** Taxonomy (`/commerce/taxonomy/...`), Catalog (`/commerce/catalog/...`)
- These are public APIs — they do not require user identity

**User token (Refresh Token grant — `refresh_token`):**
- Obtain by POSTing to `https://api.sandbox.ebay.com/identity/v1/oauth2/token` with `grant_type=refresh_token` and `refresh_token=<EBAY_REFRESH_TOKEN>`
- Use `Authorization: Bearer <user_token>` header
- **Required for:** Identity (`/commerce/identity/...`), Media (`/commerce/media/...`), Notification (`/commerce/notification/...`)

Credentials: `EBAY_APP_ID` (client ID), `EBAY_CERT_ID` (client secret), `EBAY_REFRESH_TOKEN`.

## Coverage Expectations

- Aim for broad coverage of the most important operations, not minimal coverage
- Prioritize: create, read, update, delete operations on core resources
- Include tools useful for multi-step workflows
- Cover all Commerce namespaces: Catalog (products), Charity, Identity (user info), Media (images, video, documents — note: different base domain), Notification (webhooks, subscriptions), Taxonomy (category trees, aspects, compatibility), Translation

## Technical Requirements

- **Discoverability**: all tools accessible via `list_tools()`
- **Return format**: JSON-serializable results (dicts, lists, or strings)
- **Error handling**: return errors as dicts (e.g. `{"error": "..."}`) — do not raise unhandled exceptions for expected errors (404s, invalid IDs, etc.)

## Deliverables

**You must always produce (regardless of language):**
- `grounding.json` — maps every tool you implement to its source documentation. One entry per tool:
  ```json
  {
    "get_item": {
      "doc": "docs/category/get-item.md",
      "endpoint": "GET /items/{id}"
    },
    "create_item": {
      "doc": "docs/category/create-item.md",
      "endpoint": "POST /items"
    }
  }
  ```
  - `doc`: path relative to this directory of the documentation file you used
  - `endpoint`: HTTP method and path template for the API call this tool makes
  - Every tool registered with the MCP server must have a corresponding entry

**If Python:**
- `server.py` — entry point, runs the MCP server over stdio
- `requirements.txt` — pinned dependencies:
  ```
  fastmcp==3.2.4
  requests==2.32.3
  ```

**If TypeScript:**
- `src/index.ts` — entry point, compiled to `build/index.js`
- `package.json` — pinned dependencies:
  ```json
  {
    "dependencies": {
      "@modelcontextprotocol/sdk": "1.29.0"
    }
  }
  ```
