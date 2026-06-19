from mcp.server.fastmcp import FastMCP

from generated_tools.pages import pages_create, pages_retrieve, pages_update
from generated_tools.databases import (
    databases_create,
    databases_retrieve,
    databases_update,
    databases_query,
)
from generated_tools.blocks import (
    blocks_retrieve,
    blocks_update,
    blocks_delete,
    blocks_children_list,
    blocks_children_append,
)
from generated_tools.comments import comments_create, comments_list
from generated_tools.users import users_list, users_retrieve, users_me
from generated_tools.search import search

mcp = FastMCP("notion")

# Pages
mcp.tool()(pages_create)
mcp.tool()(pages_retrieve)
mcp.tool()(pages_update)

# Databases
mcp.tool()(databases_create)
mcp.tool()(databases_retrieve)
mcp.tool()(databases_update)
mcp.tool()(databases_query)

# Blocks
mcp.tool()(blocks_retrieve)
mcp.tool()(blocks_update)
mcp.tool()(blocks_delete)
mcp.tool()(blocks_children_list)
mcp.tool()(blocks_children_append)

# Comments
mcp.tool()(comments_create)
mcp.tool()(comments_list)

# Users
mcp.tool()(users_list)
mcp.tool()(users_retrieve)
mcp.tool()(users_me)

# Search
mcp.tool()(search)


if __name__ == "__main__":
    mcp.run()
