from mcp.server.fastmcp import FastMCP

mcp = FastMCP("jira-cloud")


@mcp.tool()
def health() -> dict:
    return {"ok": True, "message": "Jira Cloud MCP server is available."}


if __name__ == "__main__":
    mcp.run()
