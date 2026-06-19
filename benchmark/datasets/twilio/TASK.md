# Task: Build an MCP Server for Twilio REST APIs

## What You're Building

An MCP server with comprehensive coverage of the Twilio REST APIs, suitable for use by an autonomous agent completing real-world tasks.

Choose your implementation language and framework:
- **Python**: FastMCP (`from mcp.server.fastmcp import FastMCP`)
- **TypeScript**: official MCP SDK (`@modelcontextprotocol/sdk`)

The server must run over stdio and expose tools callable via the MCP protocol.

## What You Have

- **118 API endpoint documentation files** in `docs/`
- **Environment variables** for authentication:
  - `TWILIO_ACCOUNT_SID` — account SID (used as username in Basic Auth)
  - `TWILIO_AUTH_TOKEN` — auth token (used as password in Basic Auth)
- **Base URLs (each product has its own):**
  - Messaging/Voice/Phone Numbers: `https://api.twilio.com/2010-04-01/Accounts/{AccountSid}`
  - Verify: `https://verify.twilio.com/v2`
  - Conversations: `https://conversations.twilio.com/v1`

## Authentication

Twilio uses HTTP Basic Auth (Account SID as username, Auth Token as password). Request bodies are form-encoded, not JSON. See the docs for details.

## Coverage Expectations

- Aim for broad coverage of the most important operations, not minimal coverage
- Prioritize: create, read, update, delete operations on core resources
- Include tools useful for multi-step workflows
- Cover: Messaging (send/list/delete SMS/MMS), Voice (initiate/list calls), Phone Numbers (search available, list purchased), Verify v2 (services, send verification, check verification), Conversations (create, send messages, manage participants)

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
