from mcp.server.fastmcp import FastMCP

from generated_tools.attachments import download_attachment, list_attachments, upload_attachment
from generated_tools.blog_posts import create_blog_post, delete_blog_post, get_blog_post, update_blog_post
from generated_tools.comments import create_footer_comment, create_inline_comment, list_footer_comments
from generated_tools.labels import add_label, list_labels, remove_label
from generated_tools.pages import (
    create_page,
    delete_page,
    get_page,
    get_page_ancestors,
    get_page_children,
    get_page_version,
    list_page_versions,
    list_pages,
    move_page,
    restore_page_version,
    update_page,
)
from generated_tools.properties import get_page_property, set_page_property
from generated_tools.search import search_content
from generated_tools.spaces import create_space, delete_space, get_space, list_spaces
from generated_tools.users import get_current_user, get_user_by_account_id


mcp = FastMCP("confluence-cloud")

mcp.tool()(list_pages)
mcp.tool()(get_page)
mcp.tool()(create_page)
mcp.tool()(update_page)
mcp.tool()(delete_page)
mcp.tool()(get_page_children)
mcp.tool()(get_page_ancestors)
mcp.tool()(move_page)
mcp.tool()(list_page_versions)
mcp.tool()(get_page_version)
mcp.tool()(restore_page_version)

mcp.tool()(list_spaces)
mcp.tool()(get_space)
mcp.tool()(create_space)
mcp.tool()(delete_space)

mcp.tool()(search_content)

mcp.tool()(list_labels)
mcp.tool()(add_label)
mcp.tool()(remove_label)

mcp.tool()(list_attachments)
mcp.tool()(upload_attachment)
mcp.tool()(download_attachment)

mcp.tool()(list_footer_comments)
mcp.tool()(create_footer_comment)
mcp.tool()(create_inline_comment)

mcp.tool()(get_page_property)
mcp.tool()(set_page_property)

mcp.tool()(create_blog_post)
mcp.tool()(get_blog_post)
mcp.tool()(update_blog_post)
mcp.tool()(delete_blog_post)

mcp.tool()(get_current_user)
mcp.tool()(get_user_by_account_id)


if __name__ == "__main__":
    mcp.run()
