# Task: Build an MCP Server for Confluence Cloud REST API

## What You're Building

An MCP server with comprehensive coverage of the Confluence Cloud REST API, suitable for use by an autonomous agent completing real-world tasks.

Choose your implementation language and framework:
- **Python**: FastMCP (`from mcp.server.fastmcp import FastMCP`)
- **TypeScript**: official MCP SDK (`@modelcontextprotocol/sdk`)

The server must run over stdio and expose tools callable via the MCP protocol.

## What You Have

- **47 API endpoint documentation files** in `docs/` covering both v1 and v2 Confluence Cloud REST APIs
- **Environment variables** for authentication:
  - `CONFLUENCE_BASE_URL` — base URL including `/wiki` (e.g. `https://yoursite.atlassian.net/wiki`)
  - `CONFLUENCE_SPACE_KEY` — default space key for operations (e.g. `SYNTH`)
  - `JIRA_EMAIL` — Atlassian account email (used for Basic auth)
  - `JIRA_API_TOKEN` — Atlassian API token (used for Basic auth)

## Authentication

Confluence Cloud REST API uses HTTP Basic authentication with:
- Username: Atlassian account email (`JIRA_EMAIL`)
- Password: Atlassian API token (`JIRA_API_TOKEN`)

Both v1 (`/wiki/rest/api/`) and v2 (`/wiki/api/v2/`) endpoints use the same credentials.

## API Versions

Two REST API versions are available:
- **v1** (`{CONFLUENCE_BASE_URL}/rest/api/`): mature, broad coverage including spaces, content, labels, attachments, comments, restrictions, templates, search, users
- **v2** (`{CONFLUENCE_BASE_URL}/api/v2/`): newer, cleaner design; prefer v2 for pages, blog posts, comments, attachments, labels, space operations where available

Use whichever version best fits each operation. Prefer v2 for page and space management where it provides equivalent coverage.

## Coverage Expectations

- **Pages**: create, get, update, delete, get children, get ancestors, move
- **Spaces**: list, get, create, delete
- **Search**: CQL-based search across content
- **Labels**: add/list/remove labels on content
- **Attachments**: list, upload, download
- **Comments**: create/list footer comments and inline comments on pages
- **Versions**: list page versions, get specific version, restore version
- **Content properties**: get/set metadata properties on pages
- **Blog posts**: create, get, update, delete
- **Users**: get current user, get user by account ID

## Technical Requirements

- **Discoverability**: all tools accessible via `list_tools()`
- **Return format**: JSON-serializable results (dicts, lists, or strings)
- **Error handling**: return errors as dicts (e.g. `{"error": "..."}`) — do not raise unhandled exceptions for expected errors (404s, permission errors, etc.)
- **No generic passthrough tools**: do NOT expose a generic `api_request` or similar tool that accepts arbitrary HTTP method/path/params. Every exposed tool must correspond to a specific, named operation.

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
