from mcp.server.fastmcp import FastMCP

from generated_tools.blocks import append_block_children, delete_block, list_block_children, retrieve_block, update_block
from generated_tools.comments import create_comment, list_comments, retrieve_comment
from generated_tools.databases import create_database, query_database, retrieve_database, update_database
from generated_tools.pages import archive_page, create_page, retrieve_page, trash_page, update_page
from generated_tools.users import get_self, get_user, get_users

mcp = FastMCP("notion")

mcp.tool()(create_page)
mcp.tool()(retrieve_page)
mcp.tool()(update_page)
mcp.tool()(archive_page)
mcp.tool()(trash_page)
mcp.tool()(create_database)
mcp.tool()(retrieve_database)
mcp.tool()(update_database)
mcp.tool()(query_database)
mcp.tool()(retrieve_block)
mcp.tool()(list_block_children)
mcp.tool()(append_block_children)
mcp.tool()(update_block)
mcp.tool()(delete_block)
mcp.tool()(create_comment)
mcp.tool()(list_comments)
mcp.tool()(retrieve_comment)
mcp.tool()(get_self)
mcp.tool()(get_user)
mcp.tool()(get_users)

if __name__ == "__main__":
    mcp.run()
