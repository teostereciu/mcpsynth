# Task: Build an MCP Server for Zendesk REST APIs

## What You're Building

An MCP server with comprehensive coverage of the Zendesk Support and Help Center REST APIs, suitable for use by an autonomous agent completing real-world tasks.

Choose your implementation language and framework:
- **Python**: FastMCP (`from mcp.server.fastmcp import FastMCP`)
- **TypeScript**: official MCP SDK (`@modelcontextprotocol/sdk`)

The server must run over stdio and expose tools callable via the MCP protocol.

## What You Have

- **150 API endpoint documentation files** in `docs/`
- **Environment variables** for authentication:
  - `ZENDESK_SUBDOMAIN` — your Zendesk subdomain (e.g. `your-org`)
  - `ZENDESK_EMAIL` — account email address
  - `ZENDESK_API_TOKEN` — API token
- **Base URLs:**
  - Support/Ticketing: `https://{ZENDESK_SUBDOMAIN}.zendesk.com/api/v2`
  - Help Center: `https://{ZENDESK_SUBDOMAIN}.zendesk.com/api/v2/help_center`

## Authentication

Zendesk uses HTTP Basic Auth with `{email}/token` as the username and the API token as the password. See the docs for details.

## Coverage Expectations

- Aim for broad coverage of the most important operations, not minimal coverage
- Prioritize: create, read, update, delete operations on core resources
- Include tools useful for multi-step workflows
- Cover: Tickets (CRUD, comments, tags, forms, fields, audits, metrics), Users, Organizations, Groups, Search, Views, Macros, Satisfaction Ratings; Help Center (Articles, Sections, Categories)

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
