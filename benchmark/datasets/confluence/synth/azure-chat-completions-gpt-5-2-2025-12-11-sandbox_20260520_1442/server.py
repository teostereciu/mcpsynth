import json

from mcp.server.fastmcp import FastMCP

from generated_tools.pages import list_pages, get_page, create_page, update_page, delete_page
from generated_tools.spaces import list_spaces, get_space, create_space
from generated_tools.search import search_content, search_users
from generated_tools.labels import add_labels_to_content, remove_label_from_content_by_query, remove_label_from_content
from generated_tools.attachments import list_attachments, get_attachment, delete_attachment, list_page_attachments
from generated_tools.comments import (
    list_page_footer_comments,
    list_page_inline_comments,
    create_footer_comment,
    create_inline_comment,
)
from generated_tools.versions import list_page_versions, get_page_version_details, restore_content_version
from generated_tools.content_properties import (
    list_page_properties,
    create_page_property,
    get_page_property,
    update_page_property,
    delete_page_property,
)
from generated_tools.blog_posts import (
    list_blog_posts,
    get_blog_post,
    create_blog_post,
    update_blog_post,
    delete_blog_post,
)
from generated_tools.users import get_current_user, get_user_by_account_id, get_users_bulk


mcp = FastMCP("confluence-cloud")


# Pages
mcp.tool()(list_pages)
mcp.tool()(get_page)
mcp.tool()(create_page)
mcp.tool()(update_page)
mcp.tool()(delete_page)

# Spaces
mcp.tool()(list_spaces)
mcp.tool()(get_space)
mcp.tool()(create_space)

# Search
mcp.tool()(search_content)
mcp.tool()(search_users)

# Labels
mcp.tool()(add_labels_to_content)
mcp.tool()(remove_label_from_content_by_query)
mcp.tool()(remove_label_from_content)

# Attachments
mcp.tool()(list_attachments)
mcp.tool()(get_attachment)
mcp.tool()(delete_attachment)
mcp.tool()(list_page_attachments)

# Comments
mcp.tool()(list_page_footer_comments)
mcp.tool()(list_page_inline_comments)
mcp.tool()(create_footer_comment)
mcp.tool()(create_inline_comment)

# Versions
mcp.tool()(list_page_versions)
mcp.tool()(get_page_version_details)
mcp.tool()(restore_content_version)

# Content properties
mcp.tool()(list_page_properties)
mcp.tool()(create_page_property)
mcp.tool()(get_page_property)
mcp.tool()(update_page_property)
mcp.tool()(delete_page_property)

# Blog posts
mcp.tool()(list_blog_posts)
mcp.tool()(get_blog_post)
mcp.tool()(create_blog_post)
mcp.tool()(update_blog_post)
mcp.tool()(delete_blog_post)

# Users
mcp.tool()(get_current_user)
mcp.tool()(get_user_by_account_id)
mcp.tool()(get_users_bulk)


if __name__ == "__main__":
    mcp.run()
