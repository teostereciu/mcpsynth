from mcp.server.fastmcp import FastMCP

from generated_tools.blocks import (
    blocks_children_append,
    blocks_children_list,
    blocks_delete,
    blocks_retrieve,
    blocks_update,
)
from generated_tools.comments import comments_create, comments_list, comments_retrieve
from generated_tools.data_sources import (
    data_sources_create,
    data_sources_list_templates,
    data_sources_query,
    data_sources_retrieve,
    data_sources_update,
)
from generated_tools.databases import (
    databases_create,
    databases_list,
    databases_query,
    databases_retrieve,
    databases_update,
)
from generated_tools.file_uploads import (
    file_uploads_complete,
    file_uploads_create,
    file_uploads_list,
    file_uploads_retrieve,
    file_uploads_send,
)
from generated_tools.pages import (
    pages_create,
    pages_move,
    pages_properties_retrieve,
    pages_restore,
    pages_retrieve,
    pages_retrieve_markdown,
    pages_trash,
    pages_update,
    pages_update_markdown,
)
from generated_tools.search import search
from generated_tools.users import users_list, users_me, users_retrieve
from generated_tools.views import (
    view_queries_create,
    view_queries_delete,
    view_queries_results,
    views_create,
    views_delete,
    views_list,
    views_retrieve,
    views_update,
)


mcp = FastMCP("notion")

# Pages
mcp.tool()(pages_create)
mcp.tool()(pages_retrieve)
mcp.tool()(pages_update)
mcp.tool()(pages_trash)
mcp.tool()(pages_restore)
mcp.tool()(pages_move)
mcp.tool()(pages_properties_retrieve)
mcp.tool()(pages_retrieve_markdown)
mcp.tool()(pages_update_markdown)

# Databases
mcp.tool()(databases_create)
mcp.tool()(databases_retrieve)
mcp.tool()(databases_update)
mcp.tool()(databases_list)
mcp.tool()(databases_query)

# Blocks
mcp.tool()(blocks_retrieve)
mcp.tool()(blocks_children_list)
mcp.tool()(blocks_children_append)
mcp.tool()(blocks_update)
mcp.tool()(blocks_delete)

# Comments
mcp.tool()(comments_create)
mcp.tool()(comments_retrieve)
mcp.tool()(comments_list)

# Users
mcp.tool()(users_list)
mcp.tool()(users_retrieve)
mcp.tool()(users_me)

# Search
mcp.tool()(search)

# Data sources
mcp.tool()(data_sources_create)
mcp.tool()(data_sources_retrieve)
mcp.tool()(data_sources_update)
mcp.tool()(data_sources_list_templates)
mcp.tool()(data_sources_query)

# Views
mcp.tool()(views_create)
mcp.tool()(views_retrieve)
mcp.tool()(views_update)
mcp.tool()(views_delete)
mcp.tool()(views_list)
mcp.tool()(view_queries_create)
mcp.tool()(view_queries_results)
mcp.tool()(view_queries_delete)

# File uploads
mcp.tool()(file_uploads_create)
mcp.tool()(file_uploads_send)
mcp.tool()(file_uploads_complete)
mcp.tool()(file_uploads_retrieve)
mcp.tool()(file_uploads_list)


if __name__ == "__main__":
    mcp.run()
