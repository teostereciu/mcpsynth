from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ebay-sell-api")


@mcp.tool()
def list_tools():
    return []


if __name__ == "__main__":
    mcp.run()
