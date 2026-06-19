# Task: Build an MCP Server for Google Sheets API

## What You're Building

An MCP server with comprehensive coverage of the Google Sheets API, suitable for use by an autonomous agent completing real-world tasks.

Choose your implementation language and framework:
- **Python**: FastMCP (`from mcp.server.fastmcp import FastMCP`)
- **TypeScript**: official MCP SDK (`@modelcontextprotocol/sdk`)

The server must run over stdio and expose tools callable via the MCP protocol.

## What You Have

- **37 API endpoint documentation files** in `docs/`
- **Environment variables** for authentication:
  - `GOOGLE_ACCESS_TOKEN` — pre-fetched OAuth 2.0 access token
  - `GOOGLE_WORKSPACE_CREDENTIALS` — path to service account JSON key file (alternative)
- **Base URL:** `https://sheets.googleapis.com/v4/spreadsheets`

## Authentication

Google Sheets API uses OAuth 2.0 Bearer token authentication:
```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

Use `GOOGLE_ACCESS_TOKEN` if set, otherwise load the service account from `GOOGLE_WORKSPACE_CREDENTIALS`.

## Coverage Expectations

- **Spreadsheets**: create, get metadata (including sheets, named ranges, formatting)
- **Values**: read range, read multiple ranges (batchGet), write range, batch write, append, clear
- **Sheet management**: add sheet, rename sheet, delete sheet, copy sheet to another spreadsheet
- **Formatting**: apply cell formats (bold, color, number format), freeze rows/columns
- **Data operations**: sort range, apply formulas
- **Named ranges**: create and list named ranges

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
  google-auth==2.29.0
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
