from mcp.server.fastmcp import FastMCP
from generated_tools.mastodon_tools import *

mcp = FastMCP("mastodon")

for name, fn in list(globals().items()):
    if callable(fn) and name not in {"FastMCP", "mcp"} and not name.startswith("_"):
        mcp.tool()(fn)

if __name__ == "__main__":
    mcp.run()
