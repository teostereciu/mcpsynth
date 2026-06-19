# Task: Build an MCP Server for Clockify API

## What You're Building

An MCP server with comprehensive coverage of the Clockify time tracking API, suitable for use by an autonomous agent completing real-world tasks.

Choose your implementation language and framework:
- **Python**: FastMCP (`from mcp.server.fastmcp import FastMCP`)
- **TypeScript**: official MCP SDK (`@modelcontextprotocol/sdk`)

The server must run over stdio and expose tools callable via the MCP protocol.

## What You Have

- **16 API endpoint documentation files** in `docs/`
- **Environment variables** for authentication:
  - `CLOCKIFY_API_KEY` — Clockify API key
- **Base URL:** `https://api.clockify.me/api/v1`

## Authentication

Clockify uses API key authentication via a request header:
```
X-Api-Key: YOUR_API_KEY
```

## Coverage Expectations

- **Workspaces**: list workspaces, get workspace details
- **Users**: get current user, list workspace users
- **Projects**: list, create, update, delete projects in a workspace
- **Time entries**: list, create, update, delete, stop running timer
- **Clients**: list and create clients
- **Tags**: list and create tags
- **Tasks**: list and create tasks within a project

## Technical Requirements

- **Discoverability**: all tools accessible via `list_tools()`
- **Return format**: JSON-serializable results (dicts, lists, or strings)
- **Error handling**: return errors as dicts (e.g. `{"error": "..."}`) — do not raise unhandled exceptions
- **No generic passthrough tools**: every tool must correspond to a specific named operation
- **Workspace resolution**: many endpoints require a `workspaceId`. Tools should accept it as a parameter; the agent will discover it by calling the workspaces endpoint first.

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
