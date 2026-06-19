# Task: Build an MCP Server for Mastodon API

## What You're Building

An MCP server with comprehensive coverage of the Mastodon REST API, suitable for use by an autonomous agent completing real-world tasks.

Choose your implementation language and framework:
- **Python**: FastMCP (`from mcp.server.fastmcp import FastMCP`)
- **TypeScript**: official MCP SDK (`@modelcontextprotocol/sdk`)

The server must run over stdio and expose tools callable via the MCP protocol.

## What You Have

- **35 API endpoint documentation files** in `docs/`
- **Environment variables** for authentication:
  - `MASTODON_ACCESS_TOKEN` — OAuth access token
  - `MASTODON_BASE_URL` — instance base URL (e.g. `https://mastodon.social`)
- **API Base URL:** `{MASTODON_BASE_URL}/api/v1`

## Authentication

Mastodon API uses OAuth 2.0 Bearer token authentication:
```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## Coverage Expectations

- **Statuses**: post, get, delete, boost (reblog), favourite, get context/thread
- **Accounts**: get authenticated account, get account by ID, follow, unfollow, get followers/following
- **Timelines**: home timeline, public timeline, hashtag timeline, list timeline
- **Notifications**: list, get, dismiss, clear all
- **Search**: search accounts, statuses, hashtags
- **Lists**: create, read, update, delete lists; add/remove accounts from lists
- **Bookmarks**: list, add, remove
- **Favourites**: list favourited statuses
- **Media**: upload media attachment (for use in statuses)
- **Instance**: get instance info and statistics

## Technical Requirements

- **Discoverability**: all tools accessible via `list_tools()`
- **Return format**: JSON-serializable results (dicts, lists, or strings)
- **Error handling**: return errors as dicts (e.g. `{"error": "..."}`) — do not raise unhandled exceptions
- **No generic passthrough tools**: every tool must correspond to a specific named operation

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
