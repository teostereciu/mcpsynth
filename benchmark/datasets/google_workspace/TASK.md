# Task: Build an MCP Server for Google Workspace APIs

## What You're Building

An MCP server with comprehensive coverage of the Google Workspace APIs, suitable for use by an autonomous agent completing real-world tasks.

Choose your implementation language and framework:
- **Python**: FastMCP (`from mcp.server.fastmcp import FastMCP`)
- **TypeScript**: official MCP SDK (`@modelcontextprotocol/sdk`)

The server must run over stdio and expose tools callable via the MCP protocol.

## What You Have

- **115 API endpoint documentation files** in `docs/`
- **Environment variables** for authentication:
  - `GOOGLE_ACCESS_TOKEN` — pre-fetched OAuth 2.0 access token
  - `GOOGLE_WORKSPACE_CREDENTIALS` — path to service account JSON key file
- **Base URLs (each API has its own):**
  - Gmail: `https://gmail.googleapis.com/gmail/v1/users/{userId}`
  - Calendar: `https://www.googleapis.com/calendar/v3`
  - Drive: `https://www.googleapis.com/drive/v3`
  - Docs: `https://docs.googleapis.com/v1/documents`
  - Slides: `https://slides.googleapis.com/v1/presentations`
  - Sheets: `https://sheets.googleapis.com/v4/spreadsheets`

## Authentication

Google Workspace APIs use OAuth 2.0 Bearer token. See the docs for header details.

## Coverage Expectations

- Aim for broad coverage of the most important operations, not minimal coverage
- Prioritize: create, read, update, delete operations on core resources
- Include tools useful for multi-step workflows
- Cover all six APIs: Gmail (messages, drafts, labels, threads), Calendar (events, calendars, free/busy), Drive (files, folders, permissions, sharing), Docs (create, read, batchUpdate), Slides (presentations, batchUpdate), Sheets (read/write values, batch operations)

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
