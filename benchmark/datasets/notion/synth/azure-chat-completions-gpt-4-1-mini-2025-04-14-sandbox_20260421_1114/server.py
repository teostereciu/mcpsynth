import sys
import json
from fastmcp import FastMCP

from generated_tools import (
    pages,
    databases,
    blocks,
    comments,
    users,
    search,
    file_uploads,
    authentication,
    database_query_filter,
)


class NotionMCPServer(FastMCP):
    def list_tools(self):
        tools = []
        tools.extend(pages.list_tools())
        tools.extend(databases.list_tools())
        tools.extend(blocks.list_tools())
        tools.extend(comments.list_tools())
        tools.extend(users.list_tools())
        tools.extend(search.list_tools())
        tools.extend(file_uploads.list_tools())
        tools.extend(authentication.list_tools())
        tools.extend(database_query_filter.list_tools())
        return tools

    # Pages
    def create_page(self, *args, **kwargs):
        return pages.create_page(*args, **kwargs)

    def retrieve_page(self, *args, **kwargs):
        return pages.retrieve_page(*args, **kwargs)

    def update_page(self, *args, **kwargs):
        return pages.update_page(*args, **kwargs)

    def trash_page(self, *args, **kwargs):
        return pages.trash_page(*args, **kwargs)

    def restore_page(self, *args, **kwargs):
        return pages.restore_page(*args, **kwargs)

    # Databases
    def create_database(self, *args, **kwargs):
        return databases.create_database(*args, **kwargs)

    def retrieve_database(self, *args, **kwargs):
        return databases.retrieve_database(*args, **kwargs)

    def update_database(self, *args, **kwargs):
        return databases.update_database(*args, **kwargs)

    def query_database(self, *args, **kwargs):
        return databases.query_database(*args, **kwargs)

    # Blocks
    def retrieve_block(self, *args, **kwargs):
        return blocks.retrieve_block(*args, **kwargs)

    def retrieve_block_children(self, *args, **kwargs):
        return blocks.retrieve_block_children(*args, **kwargs)

    def append_block_children(self, *args, **kwargs):
        return blocks.append_block_children(*args, **kwargs)

    def update_block(self, *args, **kwargs):
        return blocks.update_block(*args, **kwargs)

    def delete_block(self, *args, **kwargs):
        return blocks.delete_block(*args, **kwargs)

    # Comments
    def create_comment(self, *args, **kwargs):
        return comments.create_comment(*args, **kwargs)

    def retrieve_comment(self, *args, **kwargs):
        return comments.retrieve_comment(*args, **kwargs)

    def list_comments(self, *args, **kwargs):
        return comments.list_comments(*args, **kwargs)

    # Users
    def retrieve_user(self, *args, **kwargs):
        return users.retrieve_user(*args, **kwargs)

    def list_users(self, *args, **kwargs):
        return users.list_users(*args, **kwargs)

    def retrieve_bot_user(self, *args, **kwargs):
        return users.retrieve_bot_user(*args, **kwargs)

    # Search
    def search(self, *args, **kwargs):
        return search.search(*args, **kwargs)

    # File uploads
    def create_file_upload(self, *args, **kwargs):
        return file_uploads.create_file_upload(*args, **kwargs)

    def send_file_upload(self, *args, **kwargs):
        return file_uploads.send_file_upload(*args, **kwargs)

    def complete_file_upload(self, *args, **kwargs):
        return file_uploads.complete_file_upload(*args, **kwargs)

    def retrieve_file_upload(self, *args, **kwargs):
        return file_uploads.retrieve_file_upload(*args, **kwargs)

    def list_file_uploads(self, *args, **kwargs):
        return file_uploads.list_file_uploads(*args, **kwargs)

    # Authentication
    def create_token(self, *args, **kwargs):
        return authentication.create_token(*args, **kwargs)

    def introspect_token(self, *args, **kwargs):
        return authentication.introspect_token(*args, **kwargs)

    def revoke_token(self, *args, **kwargs):
        return authentication.revoke_token(*args, **kwargs)

    def refresh_token(self, *args, **kwargs):
        return authentication.refresh_token(*args, **kwargs)


if __name__ == "__main__":
    server = NotionMCPServer()
    server.run()
