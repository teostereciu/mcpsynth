from mcp.server.fastmcp import FastMCP
from .common import request


def register(mcp: FastMCP) -> None:
    @mcp.tool()
    def initiate_guest_checkout_session(payload: dict):
        return request("POST", "/buy/order/v2/guest_checkout_session/initiate", json=payload, extra_headers={"Content-Type": "application/json"})
