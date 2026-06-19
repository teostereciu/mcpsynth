from mcp.server.fastmcp import FastMCP

from generated_tools.blocks import append_block_children, delete_block, list_block_children, retrieve_block, update_block
from generated_tools.databases import create_database, query_database, retrieve_database, update_database
from generated_tools.pages import create_page, move_page, retrieve_page, trash_page, update_page
from generated_tools.search_users_comments import create_comment, get_me, list_comments, list_users, retrieve_user, search

mcp = FastMCP("notion")


@mcp.tool()
def notion_search(body: dict):
    return search(body)


@mcp.tool()
def notion_create_page(body: dict):
    return create_page(body)


@mcp.tool()
def notion_retrieve_page(page_id: str, filter_properties: str | None = None):
    return retrieve_page(page_id, filter_properties)


@mcp.tool()
def notion_update_page(page_id: str, body: dict):
    return update_page(page_id, body)


@mcp.tool()
def notion_trash_page(page_id: str, in_trash: bool = True):
    return trash_page(page_id, in_trash)


@mcp.tool()
def notion_move_page(page_id: str, body: dict):
    return move_page(page_id, body)


@mcp.tool()
def notion_create_database(body: dict):
    return create_database(body)


@mcp.tool()
def notion_retrieve_database(database_id: str):
    return retrieve_database(database_id)


@mcp.tool()
def notion_update_database(database_id: str, body: dict):
    return update_database(database_id, body)


@mcp.tool()
def notion_query_database(database_id: str, body: dict):
    return query_database(database_id, body)


@mcp.tool()
def notion_retrieve_block(block_id: str):
    return retrieve_block(block_id)


@mcp.tool()
def notion_list_block_children(block_id: str, start_cursor: str | None = None, page_size: int | None = None):
    return list_block_children(block_id, start_cursor, page_size)


@mcp.tool()
def notion_append_block_children(block_id: str, body: dict):
    return append_block_children(block_id, body)


@mcp.tool()
def notion_update_block(block_id: str, body: dict):
    return update_block(block_id, body)


@mcp.tool()
def notion_delete_block(block_id: str):
    return delete_block(block_id)


@mcp.tool()
def notion_list_users(start_cursor: str | None = None, page_size: int | None = None):
    return list_users(start_cursor, page_size)


@mcp.tool()
def notion_retrieve_user(user_id: str):
    return retrieve_user(user_id)


@mcp.tool()
def notion_get_me():
    return get_me()


@mcp.tool()
def notion_list_comments(block_id: str | None = None, start_cursor: str | None = None, page_size: int | None = None):
    return list_comments(block_id, start_cursor, page_size)


@mcp.tool()
def notion_create_comment(body: dict):
    return create_comment(body)


if __name__ == "__main__":
    mcp.run()
