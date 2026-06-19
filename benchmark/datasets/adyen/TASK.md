# Task: Build an MCP Server for Adyen

## What You're Building

An MCP server with comprehensive coverage of the Adyen payment processing API, suitable for use by an autonomous agent completing real-world tasks.

Choose your implementation language and framework:
- **Python**: FastMCP (`from mcp.server.fastmcp import FastMCP`)
- **TypeScript**: official MCP SDK (`@modelcontextprotocol/sdk`)

The server must run over stdio and expose tools callable via the MCP protocol.

## What You Have

- **593 API endpoint documentation files** in `docs/`
- **Environment variables** for authentication:
  - `ADYEN_API_KEY` — API key for authentication
  - `ADYEN_MERCHANT_ACCOUNT` — merchant account identifier
  - `ADYEN_COMPANY_ACCOUNT` — company account (for Management API)
  - `ADYEN_BALANCE_PLATFORM` — balance platform ID
  - `ADYEN_ENVIRONMENT` — `test` or `live` (default: `test`)
- **Base URLs:**
  - Checkout API: `https://checkout-test.adyen.com/v71`
  - Payment API: `https://pal-test.adyen.com/pal/servlet/Payment/v68`
  - Management API: `https://management-test.adyen.com/v3`

## Authentication

Adyen uses API key authentication. See the docs for header details.

## Coverage Expectations

- Aim for broad coverage of the most important operations, not minimal coverage
- Prioritize: create, read, update, delete operations on core resources
- Include tools useful for multi-step workflows
- Cover all three API services: Checkout (sessions, payment methods, payment links), Payment (authorize, capture, refund, cancel), and Management (merchant accounts, stores, webhooks, API credentials)

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
