# Notion Reference MCP Server

Official Notion MCP server: [@notionhq/notion-mcp-server](https://github.com/makenotion/notion-mcp-server)

## Required env var

The server reads auth from `OPENAPI_MCP_HEADERS`. Set it to:

```
OPENAPI_MCP_HEADERS={"Authorization": "Bearer ntn_YOUR_KEY", "Notion-Version": "2022-06-28"}
```

Or the simpler alias:

```
NOTION_TOKEN=ntn_YOUR_KEY
```

## Running

The harness launches this via `npx -y @notionhq/notion-mcp-server` automatically when
`--impl reference` is passed for the notion dataset.
