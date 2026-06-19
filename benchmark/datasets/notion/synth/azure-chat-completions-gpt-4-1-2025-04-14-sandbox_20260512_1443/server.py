import os
from mcp.server.fastmcp import FastMCP

import generated_tools.pages as pages
import generated_tools.databases as databases
import generated_tools.blocks as blocks
import generated_tools.comments as comments
import generated_tools.users as users
import generated_tools.search as search

TOOLS = {
    # Pages
    "create_page": pages.create_page,
    "update_page": pages.update_page,
    "trash_page": pages.trash_page,
    "restore_page": pages.restore_page,
    "retrieve_page": pages.retrieve_page,
    # Databases
    "create_database": databases.create_database,
    "retrieve_database": databases.retrieve_database,
    "query_database": databases.query_database,
    # Blocks
    "retrieve_block": blocks.retrieve_block,
    "get_block_children": blocks.get_block_children,
    "delete_block": blocks.delete_block,
    "update_block": blocks.update_block,
    # Comments
    "create_comment": comments.create_comment,
    "retrieve_comment": comments.retrieve_comment,
    "list_comments": comments.list_comments,
    # Users
    "list_users": users.list_users,
    "retrieve_user": users.retrieve_user,
    # Search
    "search": search.search,
}

def list_tools():
    """List all available tools."""
    return list(TOOLS.keys())

TOOLS["list_tools"] = list_tools

if __name__ == "__main__":
    FastMCP(TOOLS).run_stdio()
