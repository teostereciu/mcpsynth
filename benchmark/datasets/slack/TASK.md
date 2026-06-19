# Task: Build an MCP Server for Slack Web API

## What You're Building

An MCP server with comprehensive coverage of the Slack Web API, suitable for use by an autonomous agent completing real-world tasks.

Choose your implementation language and framework:
- **Python**: FastMCP (`from mcp.server.fastmcp import FastMCP`)
- **TypeScript**: official MCP SDK (`@modelcontextprotocol/sdk`)

The server must run over stdio and expose tools callable via the MCP protocol.

## What You Have

- **445 API endpoint documentation files** in `docs/`
- **Environment variables** for authentication:
  - `SLACK_BOT_TOKEN` — bot token (`xoxb-...`)
- **Base URL:** `https://slack.com/api`

## Authentication

Slack uses Bearer token authentication. See the docs for header details.

## Coverage Expectations

- Aim for broad coverage of the most important operations, not minimal coverage
- Prioritize: create, read, update, delete operations on core resources
- Include tools useful for multi-step workflows
- Cover: Messages (post, update, delete, schedule), Conversations (list channels, history, members, replies, create, invite), Users (list, lookup, presence), Reactions, Files (upload, list), Search, Pins, Reminders, Team info

## Technical Requirements

- **Discoverability**: all tools accessible via `list_tools()`
- **Return format**: JSON-serializable results (dicts, lists, or strings)
- **Error handling**: return errors as dicts (e.g. `{"error": "..."}`) — do not raise unhandled exceptions for expected errors (404s, invalid IDs, etc.)
- **No generic passthrough tools**: do NOT expose a generic `api_request`, `raw_request`, or similar tool that accepts arbitrary HTTP method/path/params. Every exposed tool must correspond to a specific, named operation. Internal HTTP client helpers are fine as implementation details but must not be registered as MCP tools.

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
