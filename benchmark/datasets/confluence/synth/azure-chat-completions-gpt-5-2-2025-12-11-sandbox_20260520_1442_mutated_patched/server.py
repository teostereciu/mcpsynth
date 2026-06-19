from mcp.server.fastmcp import FastMCP

from generated_tools.attachments import (
    delete_attachment,
    download_attachment_to_file,
    get_attachment,
    list_attachments,
    list_page_attachments,
)
from generated_tools.blog_posts import (
    create_blog_post,
    delete_blog_post,
    get_blog_post,
    list_blog_posts,
    update_blog_post,
)
from generated_tools.comments import create_footer_comment, list_page_footer_comments, list_page_inline_comments
from generated_tools.content_properties import (
    create_page_property,
    delete_page_property,
    get_page_property,
    list_page_properties,
    update_page_property,
)
from generated_tools.labels import add_labels_to_content, remove_label_from_content, remove_label_from_content_by_name
from generated_tools.pages import (
    create_page,
    delete_page,
    get_page,
    list_pages,
    update_page,
    update_page_title,
)
from generated_tools.search import cql_search, cql_search_users
from generated_tools.spaces import create_space, get_space, list_spaces
from generated_tools.users import get_current_user, get_user_by_account_id, get_users_bulk
from generated_tools.versions import get_page_version_details, list_page_versions

mcp = FastMCP("confluence-cloud")


# Pages
mcp.tool()(list_pages)
mcp.tool()(get_page)
mcp.tool()(create_page)
mcp.tool()(update_page)
mcp.tool()(delete_page)
mcp.tool()(update_page_title)

# Spaces
mcp.tool()(list_spaces)
mcp.tool()(get_space)
mcp.tool()(create_space)

# Search
mcp.tool()(cql_search)
mcp.tool()(cql_search_users)

# Labels
mcp.tool()(add_labels_to_content)
mcp.tool()(remove_label_from_content_by_name)
mcp.tool()(remove_label_from_content)

# Attachments
mcp.tool()(list_attachments)
mcp.tool()(list_page_attachments)
mcp.tool()(get_attachment)
mcp.tool()(delete_attachment)
mcp.tool()(download_attachment_to_file)

# Comments
mcp.tool()(list_page_footer_comments)
mcp.tool()(list_page_inline_comments)
mcp.tool()(create_footer_comment)

# Versions
mcp.tool()(list_page_versions)
mcp.tool()(get_page_version_details)

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
