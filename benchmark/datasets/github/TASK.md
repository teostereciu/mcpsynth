# Task: Build an MCP Server for GitHub REST API

## What You're Building

An MCP server with comprehensive coverage of the GitHub REST API, suitable for use by an autonomous agent completing real-world tasks.

Choose your implementation language and framework:
- **Python**: FastMCP (`from mcp.server.fastmcp import FastMCP`)
- **TypeScript**: official MCP SDK (`@modelcontextprotocol/sdk`)

The server must run over stdio and expose tools callable via the MCP protocol.

## What You Have

- **181 API endpoint documentation files** in `docs/`
- **Environment variables** for authentication:
  - `GITHUB_TOKEN` — personal access token
  - `GITHUB_API_BASE_URL` — override for GitHub Enterprise (default: `https://api.github.com`)
  - `GITHUB_TEST_REPO` — test repository in `owner/repo` format
- **Base URL:** `https://api.github.com` (or `GITHUB_API_BASE_URL` if set)

## Authentication

GitHub REST API uses Bearer token authentication with a required `Accept` header. See the docs for header details.

## Coverage Expectations

- Aim for broad coverage of the most important operations, not minimal coverage
- Prioritize: create, read, update, delete operations on core resources
- Include tools useful for multi-step workflows
- Cover: Issues (CRUD, labels, assignees, comments), Pull Requests (create, review, merge), Repositories (create, fork, branches, commits, contents), Releases, Actions (workflows, runs), Code Search, Webhooks, Branch Protection

## Technical Requirements

- **Discoverability**: all tools accessible via `list_tools()`
- **Return format**: JSON-serializable results (dicts, lists, or strings)
- **Error handling**: return errors as dicts (e.g. `{"error": "..."}`) — do not raise unhandled exceptions for expected errors (404s, invalid IDs, etc.)
- **No generic passthrough tools**: do NOT expose a generic `api_request`, `raw_request`, or similar tool that accepts arbitrary HTTP method/path/params. Every exposed tool must correspond to a specific, named operation. Internal HTTP client helpers are fine as implementation details but must not be registered as MCP tools.

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
