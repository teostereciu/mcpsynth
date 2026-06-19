import inspect
from typing import Any, Callable, Dict, List

from mcp.server.fastmcp import FastMCP

from generated_tools import (
    account_links,
    charges,
    checkout_sessions,
    connect_accounts,
    coupons,
    customers,
    invoiceitems,
    invoices,
    payment_intents,
    payment_links,
    payment_methods,
    payouts,
    promotion_codes,
    refunds,
    prices,
    products,
    setup_intents,
    subscriptions,
    transfers,
)


mcp = FastMCP("stripe")


def _register_module_functions(module) -> None:
    for name, fn in inspect.getmembers(module, inspect.isfunction):
        if name.startswith("_"):
            continue
        # Register as tool with same name
        mcp.tool(name=name)(fn)


for mod in [
    customers,
    payment_intents,
    charges,
    refunds,
    products,
    prices,
    subscriptions,
    invoices,
    invoiceitems,
    checkout_sessions,
    payment_links,
    coupons,
    promotion_codes,
    payment_methods,
    setup_intents,
    connect_accounts,
    account_links,
    transfers,
    payouts,
]:
    _register_module_functions(mod)


if __name__ == "__main__":
    mcp.run()
