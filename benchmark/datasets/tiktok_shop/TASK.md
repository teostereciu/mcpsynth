# Task: Build an MCP Server for TikTok Shop Partner Open API

## What You're Building

An MCP server with comprehensive coverage of the TikTok Shop Partner Open API, suitable for use by an autonomous agent completing real-world tasks.

Choose your implementation language and framework:
- **Python**: FastMCP (`from mcp.server.fastmcp import FastMCP`)
- **TypeScript**: official MCP SDK (`@modelcontextprotocol/sdk`)

The server must run over stdio and expose tools callable via the MCP protocol.

## What You Have

- **494 API endpoint documentation files** in `docs/`
- **Environment variables** for authentication:
  - `TIKTOK_APP_KEY` — application key
  - `TIKTOK_APP_SECRET` — application secret (used for HMAC-SHA256 signing)
  - `TIKTOK_ACCESS_TOKEN` — access token for user-scoped calls
  - `TIKTOK_SHOP_CIPHER` — shop cipher for shop-scoped calls
- **Base URL:** `https://open-api.tiktokglobalshop.com`

## Authentication

TikTok Shop API uses HMAC-SHA256 request signing plus an access token header. Every request requires `app_key`, `timestamp`, and `sign` query parameters. See the docs for the signing algorithm details.

## Coverage Expectations

- Aim for broad coverage of the most important operations, not minimal coverage
- Prioritize: create, read, update, delete operations on core resources
- Include tools useful for multi-step workflows
- Cover the major domains: Products (listings, SKUs, inventory), Orders (management, status), Fulfillment (shipping, packages), Returns/Refunds, Finance (settlements, transactions), Promotions, Analytics

## Technical Requirements

- **Discoverability**: all tools accessible via `list_tools()`
- **Return format**: JSON-serializable results (dicts, lists, or strings)
- **Error handling**: return errors as dicts (e.g. `{"error": "..."}`) — do not raise unhandled exceptions for expected errors (404s, invalid IDs, etc.)

## Deliverables

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
