# Task: Build an MCP Server for HubSpot CRM API

## What You're Building

An MCP server with comprehensive coverage of the HubSpot CRM REST API, suitable for use by an autonomous agent completing real-world tasks.

Choose your implementation language and framework:
- **Python**: FastMCP (`from mcp.server.fastmcp import FastMCP`)
- **TypeScript**: official MCP SDK (`@modelcontextprotocol/sdk`)

The server must run over stdio and expose tools callable via the MCP protocol.

## What You Have

- **174 API endpoint documentation files** in `docs/`
- **Environment variables** for authentication:
  - `HUBSPOT_ACCESS_TOKEN` — private app access token
- **Base URL:** `https://api.hubapi.com`

## Authentication

HubSpot uses Bearer token authentication. See the docs for header details.

## Coverage Expectations

- Aim for broad coverage of the most important operations, not minimal coverage
- Prioritize: create, read, update, delete operations on core resources
- Include tools useful for multi-step workflows
- Cover: Contacts, Companies, Deals, Tickets (full CRUD + search + batch ops), Associations (v3 and v4), Owners, Pipelines, Properties, Engagements (notes, tasks, calls, meetings)

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
