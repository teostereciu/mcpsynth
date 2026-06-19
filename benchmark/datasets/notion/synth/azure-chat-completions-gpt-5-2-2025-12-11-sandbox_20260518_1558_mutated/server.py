from mcp.server.fastmcp import FastMCP

from generated_tools.users import users_me, users_list, users_retrieve
from generated_tools.search import search
from generated_tools.pages import (
    pages_create,
    pages_retrieve,
    pages_update,
    pages_archive,
    pages_restore,
    pages_retrieve_property_item,
    pages_move,
    pages_retrieve_markdown,
    pages_update_markdown,
)
from generated_tools.databases import (
    databases_create,
    databases_retrieve,
    databases_update,
    databases_list,
    databases_query,
)
from generated_tools.blocks import (
    blocks_retrieve,
    blocks_children_list,
    blocks_children_append,
    blocks_update,
    blocks_delete,
)
from generated_tools.comments import comments_create, comments_retrieve, comments_list
from generated_tools.data_sources import (
    data_sources_create,
    data_sources_retrieve,
    data_sources_update,
    data_sources_list_templates,
    data_sources_query,
)
from generated_tools.file_uploads import (
    file_uploads_create,
    file_uploads_send,
    file_uploads_complete,
    file_uploads_retrieve,
    file_uploads_list,
)
from generated_tools.views import (
    views_create,
    views_retrieve,
    views_update,
    views_delete,
    views_list,
    view_queries_create,
    view_queries_delete,
    view_queries_results,
)


mcp = FastMCP("notion")

# Users
mcp.tool()(users_me)
mcp.tool()(users_list)
mcp.tool()(users_retrieve)

# Search
mcp.tool()(search)

# Pages
mcp.tool()(pages_create)
mcp.tool()(pages_retrieve)
mcp.tool()(pages_update)
mcp.tool()(pages_archive)
mcp.tool()(pages_restore)
mcp.tool()(pages_retrieve_property_item)
mcp.tool()(pages_move)
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

# Data sources
mcp.tool()(data_sources_create)
mcp.tool()(data_sources_retrieve)
mcp.tool()(data_sources_update)
mcp.tool()(data_sources_list_templates)
mcp.tool()(data_sources_query)

# File uploads
mcp.tool()(file_uploads_create)
mcp.tool()(file_uploads_send)
mcp.tool()(file_uploads_complete)
mcp.tool()(file_uploads_retrieve)
mcp.tool()(file_uploads_list)

# Views
mcp.tool()(views_create)
mcp.tool()(views_retrieve)
mcp.tool()(views_update)
mcp.tool()(views_delete)
mcp.tool()(views_list)
mcp.tool()(view_queries_create)
mcp.tool()(view_queries_delete)
mcp.tool()(view_queries_results)


if __name__ == "__main__":
    mcp.run()
