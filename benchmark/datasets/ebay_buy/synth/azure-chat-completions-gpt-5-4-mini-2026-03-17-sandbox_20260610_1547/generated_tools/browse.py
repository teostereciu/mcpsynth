from mcp.server.fastmcp import FastMCP
from .common import request


def register(mcp: FastMCP) -> None:
    @mcp.tool()
    def search(q: str | None = None, limit: int | None = None, offset: int | None = None, **kwargs):
        params = {k: v for k, v in {"q": q, "limit": limit, "offset": offset, **kwargs}.items() if v is not None}
        return request("GET", "/buy/browse/v1/item_summary/search", params=params)

    @mcp.tool()
    def get_item(item_id: str):
        return request("GET", f"/buy/browse/v1/item/{item_id}")
