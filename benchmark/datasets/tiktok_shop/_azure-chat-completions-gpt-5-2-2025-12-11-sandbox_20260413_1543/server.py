from __future__ import annotations

import inspect
from typing import Any, Callable, Dict

from mcp.server.fastmcp import FastMCP

import generated_tools as tools


mcp = FastMCP("tiktok-shop")


def _register(fn: Callable[..., Any], name: str | None = None) -> None:
    tool_name = name or fn.__name__
    doc = inspect.getdoc(fn) or ""

    @mcp.tool(name=tool_name, description=doc)
    def _tool(**kwargs: Any) -> Any:
        return fn(**kwargs)


# Seller
_register(tools.get_authorized_shops)

# Products
_register(tools.get_categories)
_register(tools.create_product)
_register(tools.search_products)
_register(tools.get_product)
_register(tools.update_inventory)
_register(tools.update_price)

# Orders
_register(tools.get_order_list)
_register(tools.get_order_detail)

# Fulfillment
_register(tools.get_warehouse_list)
_register(tools.search_packages)
_register(tools.ship_package)
_register(tools.get_package_shipping_document)

# Promotions
_register(tools.create_activity)

# Finance
_register(tools.get_payments)

# Customer service
_register(tools.get_conversations)
_register(tools.send_message)


if __name__ == "__main__":
    mcp.run()
