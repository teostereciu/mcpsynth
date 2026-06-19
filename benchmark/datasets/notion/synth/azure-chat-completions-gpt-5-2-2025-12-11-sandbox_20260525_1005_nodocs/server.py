from mcp.server.fastmcp import FastMCP

from generated_tools.pages import pages_create, pages_retrieve, pages_update
from generated_tools.databases import (
    databases_create,
    databases_query,
    databases_retrieve,
    databases_update,
)
from generated_tools.blocks import (
    blocks_children_append,
    blocks_children_list,
    blocks_delete,
    blocks_retrieve,
    blocks_update,
)
from generated_tools.comments import comments_create, comments_list
from generated_tools.users import users_list, users_me, users_retrieve
from generated_tools.search import search


mcp = FastMCP("notion-mcp")

# Pages
mcp.tool()(pages_retrieve)
mcp.tool()(pages_create)
mcp.tool()(pages_update)

# Databases
mcp.tool()(databases_retrieve)
mcp.tool()(databases_query)
mcp.tool()(databases_create)
mcp.tool()(databases_update)

# Blocks
mcp.tool()(blocks_retrieve)
mcp.tool()(blocks_update)
mcp.tool()(blocks_delete)
mcp.tool()(blocks_children_list)
mcp.tool()(blocks_children_append)

# Comments
mcp.tool()(comments_list)
mcp.tool()(comments_create)

# Users
mcp.tool()(users_list)
mcp.tool()(users_retrieve)
mcp.tool()(users_me)

# Search
mcp.tool()(search)


if __name__ == "__main__":
    mcp.run()
