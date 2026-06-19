# Task: Build an MCP Server for Forgejo/Codeberg API

## What You're Building

An MCP server with comprehensive coverage of the Forgejo REST API, suitable for use by an autonomous agent completing real-world tasks. The server will be tested against a Codeberg.org account (Codeberg runs Forgejo).

Choose your implementation language and framework:
- **Python**: FastMCP (`from mcp.server.fastmcp import FastMCP`)
- **TypeScript**: official MCP SDK (`@modelcontextprotocol/sdk`)

The server must run over stdio and expose tools callable via the MCP protocol.

## What You Have

- **7 API endpoint documentation files** in `docs/`
- **Environment variables** for authentication:
  - `CODEBERG_TOKEN` — Forgejo API token
  - `CODEBERG_BASE_URL` — base URL (e.g. `https://codeberg.org`)
- **API Base URL:** `{CODEBERG_BASE_URL}/api/v1`

## Authentication

Forgejo API uses token authentication via a request header:
```
Authorization: token YOUR_TOKEN
```

## Coverage Expectations

- **Repositories**: list (user's repos, org repos), get, create, delete, fork
- **Issues**: list, get, create, update, close, add labels, add comments
- **Pull Requests**: list, get, create, merge
- **Users**: get authenticated user, get user by username, search users
- **Organizations**: list, get org info
- **Branches**: list, get, create
- **Commits**: list, get
- **Releases**: list, create, get

## Technical Requirements

- **Discoverability**: all tools accessible via `list_tools()`
- **Return format**: JSON-serializable results (dicts, lists, or strings)
- **Error handling**: return errors as dicts (e.g. `{"error": "..."}`) — do not raise unhandled exceptions
- **No generic passthrough tools**: every tool must correspond to a specific named operation

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
