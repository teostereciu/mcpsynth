from mcp.server.fastmcp import FastMCP

from generated_tools.ingredients import *
from generated_tools.meal_planning import *
from generated_tools.menu_items import *
from generated_tools.misc import *
from generated_tools.products import *
from generated_tools.recipes import *
from generated_tools.wine import *

mcp = FastMCP("spoonacular")

for name, fn in list(globals().items()):
    if callable(fn) and getattr(fn, "__module__", "").startswith("generated_tools."):
        mcp.tool()(fn)


if __name__ == "__main__":
    mcp.run()
