from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ebay-buy-api")


@mcp.tool()
def health() -> dict:
    return {"status": "ok", "message": "eBay Buy API MCP server"}


if __name__ == "__main__":
    mcp.run()
