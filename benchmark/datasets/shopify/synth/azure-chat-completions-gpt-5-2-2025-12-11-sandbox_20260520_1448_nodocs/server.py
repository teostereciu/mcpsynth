from mcp.server.fastmcp import FastMCP

# Tools are conditionally registered because docs/ are not present in this workspace.
# This server provides a minimal, safe skeleton.

mcp = FastMCP("shopify_admin_rest")


@mcp.tool()
def health_check() -> dict:
    """Basic server health check."""
    return {"ok": True, "name": "shopify_admin_rest"}


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
