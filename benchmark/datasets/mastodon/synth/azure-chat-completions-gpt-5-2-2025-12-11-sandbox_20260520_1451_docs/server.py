import inspect
from typing import Any, Callable, Dict

from mcp.server.fastmcp import FastMCP

from generated_tools import accounts, bookmarks, favourites, instance, lists, media, notifications, search, statuses, timelines

mcp = FastMCP("mastodon")


def _register_module_functions(module, prefix: str = "") -> Dict[str, Callable[..., Any]]:
    out: Dict[str, Callable[..., Any]] = {}
    for name, fn in inspect.getmembers(module, inspect.isfunction):
        if name.startswith("_"):
            continue
        tool_name = f"{prefix}{name}" if prefix else name
        out[tool_name] = fn
    return out


TOOLS: Dict[str, Callable[..., Any]] = {}
TOOLS.update(_register_module_functions(statuses))
TOOLS.update(_register_module_functions(accounts))
TOOLS.update(_register_module_functions(timelines))
TOOLS.update(_register_module_functions(notifications))
TOOLS.update(_register_module_functions(search))
TOOLS.update(_register_module_functions(lists))
TOOLS.update(_register_module_functions(bookmarks))
TOOLS.update(_register_module_functions(favourites))
TOOLS.update(_register_module_functions(media))
TOOLS.update(_register_module_functions(instance))

for tool_name, fn in sorted(TOOLS.items()):
    mcp.tool(name=tool_name)(fn)


if __name__ == "__main__":
    mcp.run()
