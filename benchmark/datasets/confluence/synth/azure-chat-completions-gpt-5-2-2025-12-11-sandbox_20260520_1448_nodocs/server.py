from mcp.server.fastmcp import FastMCP

from generated_tools.attachments import (
    download_attachment,
    get_attachment,
    list_attachments,
    upload_attachment,
)
from generated_tools.blog_posts import (
    create_blog_post,
    delete_blog_post,
    get_blog_post,
    update_blog_post,
)
from generated_tools.comments import create_footer_comment, create_inline_comment, list_comments
from generated_tools.content_properties import get_content_property, set_content_property
from generated_tools.labels import add_labels, list_labels, remove_label
from generated_tools.pages import (
    create_page,
    delete_page,
    get_page,
    get_page_ancestors,
    get_page_children,
    list_pages,
    move_page,
    update_page,
)
from generated_tools.search import cql_search
from generated_tools.spaces import create_space, delete_space, get_space, list_spaces
from generated_tools.users import get_current_user, get_user
from generated_tools.versions import get_page_version, list_page_versions, restore_page_version

mcp = FastMCP("confluence-cloud")


# Pages
mcp.tool()(list_pages)
mcp.tool()(get_page)
mcp.tool()(create_page)
mcp.tool()(update_page)
mcp.tool()(delete_page)
mcp.tool()(get_page_children)
mcp.tool()(get_page_ancestors)
mcp.tool()(move_page)

# Spaces
mcp.tool()(list_spaces)
mcp.tool()(get_space)
mcp.tool()(create_space)
mcp.tool()(delete_space)

# Search
mcp.tool()(cql_search)

# Labels
mcp.tool()(list_labels)
mcp.tool()(add_labels)
mcp.tool()(remove_label)

# Attachments
mcp.tool()(list_attachments)
mcp.tool()(upload_attachment)
mcp.tool()(get_attachment)
mcp.tool()(download_attachment)

# Comments
mcp.tool()(list_comments)
mcp.tool()(create_footer_comment)
mcp.tool()(create_inline_comment)

# Versions
mcp.tool()(list_page_versions)
mcp.tool()(get_page_version)
mcp.tool()(restore_page_version)

# Content properties
mcp.tool()(get_content_property)
mcp.tool()(set_content_property)

# Blog posts
mcp.tool()(get_blog_post)
mcp.tool()(create_blog_post)
mcp.tool()(update_blog_post)
mcp.tool()(delete_blog_post)

# Users
mcp.tool()(get_current_user)
mcp.tool()(get_user)


if __name__ == "__main__":
    mcp.run()
