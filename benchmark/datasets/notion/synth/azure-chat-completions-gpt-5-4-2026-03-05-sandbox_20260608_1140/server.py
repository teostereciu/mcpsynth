from mcp.server.fastmcp import FastMCP

from generated_tools.blocks import append_block_children, delete_block, get_block_children, retrieve_block, update_block
from generated_tools.comments import create_comment, list_comments, retrieve_comment
from generated_tools.data_sources import create_data_source, list_data_source_templates, retrieve_data_source, update_data_source
from generated_tools.databases import create_database, query_data_source, retrieve_database, update_database
from generated_tools.file_uploads import complete_file_upload, create_file_upload, list_file_uploads, retrieve_file_upload
from generated_tools.pages import create_page, move_page, retrieve_page, retrieve_page_property, update_page
from generated_tools.search_users import get_self, get_user, list_users, search

mcp = FastMCP("notion")

mcp.tool()(retrieve_page)
mcp.tool()(create_page)
mcp.tool()(update_page)
mcp.tool()(retrieve_page_property)
mcp.tool()(move_page)

mcp.tool()(create_database)
mcp.tool()(retrieve_database)
mcp.tool()(update_database)
mcp.tool()(query_data_source)

mcp.tool()(create_data_source)
mcp.tool()(retrieve_data_source)
mcp.tool()(update_data_source)
mcp.tool()(list_data_source_templates)

mcp.tool()(get_block_children)
mcp.tool()(append_block_children)
mcp.tool()(retrieve_block)
mcp.tool()(update_block)
mcp.tool()(delete_block)

mcp.tool()(create_comment)
mcp.tool()(retrieve_comment)
mcp.tool()(list_comments)

mcp.tool()(search)
mcp.tool()(list_users)
mcp.tool()(get_user)
mcp.tool()(get_self)

mcp.tool()(create_file_upload)
mcp.tool()(complete_file_upload)
mcp.tool()(retrieve_file_upload)
mcp.tool()(list_file_uploads)

if __name__ == "__main__":
    mcp.run()
