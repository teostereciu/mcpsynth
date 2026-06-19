# GitHub Reference MCP Server

Official GitHub MCP server: [@modelcontextprotocol/server-github](https://github.com/modelcontextprotocol/servers)

## Required env var

```
GITHUB_PERSONAL_ACCESS_TOKEN=ghp_YOUR_TOKEN
```

Note: the harness already passes `GITHUB_TOKEN` from the environment. If the reference
server expects `GITHUB_PERSONAL_ACCESS_TOKEN` instead, add to your `.env`:

```
GITHUB_PERSONAL_ACCESS_TOKEN=ghp_YOUR_TOKEN
```

## Running

The harness launches this via `npx -y @modelcontextprotocol/server-github` automatically
when `--impl reference` is passed for the github dataset.
