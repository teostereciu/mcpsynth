# Task: Build an MCP Server for Alpha Vantage API

## What You're Building

An MCP server with comprehensive coverage of the Alpha Vantage financial data API, suitable for use by an autonomous agent completing real-world tasks.

Choose your implementation language and framework:
- **Python**: FastMCP (`from mcp.server.fastmcp import FastMCP`)
- **TypeScript**: official MCP SDK (`@modelcontextprotocol/sdk`)

The server must run over stdio and expose tools callable via the MCP protocol.

## What You Have

- **9 API endpoint documentation files** in `docs/`
- **Environment variables** for authentication:
  - `ALPHAVANTAGE_API_KEY` — API key for Alpha Vantage
- **Base URL:** `https://www.alphavantage.co/query`

## Authentication

All Alpha Vantage API calls are made to a single base URL with the `apikey` query parameter appended to every request:
```
https://www.alphavantage.co/query?function=...&apikey=YOUR_KEY
```

## Coverage Expectations

- **Stock time series**: intraday, daily, weekly, monthly OHLCV data
- **Quote endpoint**: latest price and volume for a symbol
- **Search**: symbol search / ticker lookup
- **Forex (FX)**: exchange rates, FX time series (daily, weekly, monthly)
- **Cryptocurrency**: digital currency exchange rates, crypto time series
- **Technical indicators**: SMA, EMA, RSI, MACD, Bollinger Bands
- **Fundamental data**: company overview, income statement, balance sheet, earnings
- **Economic indicators**: CPI, inflation, GDP, unemployment, treasury yields
- **Sector performance**: real-time sector performance across S&P 500

## Technical Requirements

- **Discoverability**: all tools accessible via `list_tools()`
- **Return format**: JSON-serializable results (dicts, lists, or strings)
- **Error handling**: return errors as dicts (e.g. `{"error": "..."}`) — do not raise unhandled exceptions for API errors or missing data
- **No generic passthrough tools**: every tool must correspond to a specific named operation

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
