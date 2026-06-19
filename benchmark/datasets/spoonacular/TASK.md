# Task: Build an MCP Server for Spoonacular Food API

## What You're Building

An MCP server with comprehensive coverage of the Spoonacular food and recipe API, suitable for use by an autonomous agent completing real-world tasks.

Choose your implementation language and framework:
- **Python**: FastMCP (`from mcp.server.fastmcp import FastMCP`)
- **TypeScript**: official MCP SDK (`@modelcontextprotocol/sdk`)

The server must run over stdio and expose tools callable via the MCP protocol.

## What You Have

- **7 API endpoint documentation files** in `docs/`
- **Environment variables** for authentication:
  - `SPOONACULAR_API_KEY` — API key for Spoonacular
- **Base URL:** `https://api.spoonacular.com`

## Authentication

All Spoonacular API calls require the API key as a query parameter:
```
https://api.spoonacular.com/recipes/complexSearch?apiKey=YOUR_KEY&...
```

## Coverage Expectations

- **Recipe search**: search by query, by ingredients, by nutrients; complex search with filters
- **Recipe information**: get recipe details, ingredients, nutrition, instructions, similar recipes
- **Ingredient search**: search ingredients, get ingredient info, parse ingredients
- **Meal planning**: generate meal plans (daily, weekly), get meal plan
- **Nutrition**: get nutrition by ID, visualize nutrition
- **Wine pairing**: get wine pairing for a dish, wine description
- **Autocomplete**: autocomplete recipe/ingredient search

## Technical Requirements

- **Discoverability**: all tools accessible via `list_tools()`
- **Return format**: JSON-serializable results (dicts, lists, or strings)
- **Error handling**: return errors as dicts (e.g. `{"error": "..."}`) — do not raise unhandled exceptions
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
