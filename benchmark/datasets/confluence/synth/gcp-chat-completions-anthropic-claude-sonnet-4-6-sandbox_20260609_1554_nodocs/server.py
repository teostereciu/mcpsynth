"""
MCP Server for Confluence Cloud REST API
Runs over stdio using FastMCP.
"""
from mcp.server.fastmcp import FastMCP

# Domain modules
from generated_tools.pages import (
    get_page_by_id,
    get_pages_in_space,
    create_page,
    update_page,
    delete_page,
    get_page_children,
    get_page_ancestors,
    move_page,
    get_page_by_title,
)
from generated_tools.spaces import (
    list_spaces,
    get_space_by_key,
    get_space_by_id,
    create_space,
    delete_space,
    get_space_content,
)
from generated_tools.search import (
    search_content,
    search_users,
)
from generated_tools.labels import (
    get_page_labels,
    add_labels_to_page,
    remove_label_from_page,
    get_blogpost_labels,
    add_labels_to_blogpost,
    remove_label_from_blogpost,
)
from generated_tools.attachments import (
    list_page_attachments,
    upload_attachment_to_page,
    get_attachment_by_id,
    download_attachment,
    delete_attachment,
)
from generated_tools.comments import (
    list_page_footer_comments,
    create_page_footer_comment,
    get_footer_comment_by_id,
    update_footer_comment,
    delete_footer_comment,
    list_page_inline_comments,
    create_page_inline_comment,
    get_inline_comment_by_id,
    delete_inline_comment,
)
from generated_tools.versions import (
    list_page_versions,
    get_page_version,
    restore_page_version,
    delete_page_version,
)
from generated_tools.content_properties import (
    list_page_properties,
    get_page_property,
    create_page_property,
    update_page_property,
    delete_page_property,
    list_content_properties,
    get_content_property,
    set_content_property,
    delete_content_property,
)
from generated_tools.blogposts import (
    list_blogposts,
    get_blogpost_by_id,
    create_blogpost,
    update_blogpost,
    delete_blogpost,
)
from generated_tools.users import (
    get_current_user,
    get_user_by_account_id,
    get_user_groups,
    get_user_by_username,
    list_group_members,
    get_anonymous_user,
)

# ---------------------------------------------------------------------------
# Initialise FastMCP server
# ---------------------------------------------------------------------------
mcp = FastMCP(
    name="confluence-cloud",
    instructions=(
        "Tools for interacting with Confluence Cloud REST API (v1 and v2). "
        "Supports pages, spaces, search, labels, attachments, comments, "
        "versions, content properties, blog posts, and users. "
        "Set CONFLUENCE_BASE_URL, CONFLUENCE_SPACE_KEY, JIRA_EMAIL, and "
        "JIRA_API_TOKEN environment variables before use."
    ),
)

# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------
mcp.tool()(get_page_by_id)
mcp.tool()(get_pages_in_space)
mcp.tool()(create_page)
mcp.tool()(update_page)
mcp.tool()(delete_page)
mcp.tool()(get_page_children)
mcp.tool()(get_page_ancestors)
mcp.tool()(move_page)
mcp.tool()(get_page_by_title)

# ---------------------------------------------------------------------------
# Spaces
# ---------------------------------------------------------------------------
mcp.tool()(list_spaces)
mcp.tool()(get_space_by_key)
mcp.tool()(get_space_by_id)
mcp.tool()(create_space)
mcp.tool()(delete_space)
mcp.tool()(get_space_content)

# ---------------------------------------------------------------------------
# Search
# ---------------------------------------------------------------------------
mcp.tool()(search_content)
mcp.tool()(search_users)

# ---------------------------------------------------------------------------
# Labels
# ---------------------------------------------------------------------------
mcp.tool()(get_page_labels)
mcp.tool()(add_labels_to_page)
mcp.tool()(remove_label_from_page)
mcp.tool()(get_blogpost_labels)
mcp.tool()(add_labels_to_blogpost)
mcp.tool()(remove_label_from_blogpost)

# ---------------------------------------------------------------------------
# Attachments
# ---------------------------------------------------------------------------
mcp.tool()(list_page_attachments)
mcp.tool()(upload_attachment_to_page)
mcp.tool()(get_attachment_by_id)
mcp.tool()(download_attachment)
mcp.tool()(delete_attachment)

# ---------------------------------------------------------------------------
# Comments
# ---------------------------------------------------------------------------
mcp.tool()(list_page_footer_comments)
mcp.tool()(create_page_footer_comment)
mcp.tool()(get_footer_comment_by_id)
mcp.tool()(update_footer_comment)
mcp.tool()(delete_footer_comment)
mcp.tool()(list_page_inline_comments)
mcp.tool()(create_page_inline_comment)
mcp.tool()(get_inline_comment_by_id)
mcp.tool()(delete_inline_comment)

# ---------------------------------------------------------------------------
# Versions
# ---------------------------------------------------------------------------
mcp.tool()(list_page_versions)
mcp.tool()(get_page_version)
mcp.tool()(restore_page_version)
mcp.tool()(delete_page_version)

# ---------------------------------------------------------------------------
# Content Properties
# ---------------------------------------------------------------------------
mcp.tool()(list_page_properties)
mcp.tool()(get_page_property)
mcp.tool()(create_page_property)
mcp.tool()(update_page_property)
mcp.tool()(delete_page_property)
mcp.tool()(list_content_properties)
mcp.tool()(get_content_property)
mcp.tool()(set_content_property)
mcp.tool()(delete_content_property)

# ---------------------------------------------------------------------------
# Blog Posts
# ---------------------------------------------------------------------------
mcp.tool()(list_blogposts)
mcp.tool()(get_blogpost_by_id)
mcp.tool()(create_blogpost)
mcp.tool()(update_blogpost)
mcp.tool()(delete_blogpost)

# ---------------------------------------------------------------------------
# Users
# ---------------------------------------------------------------------------
mcp.tool()(get_current_user)
mcp.tool()(get_user_by_account_id)
mcp.tool()(get_user_groups)
mcp.tool()(get_user_by_username)
mcp.tool()(list_group_members)
mcp.tool()(get_anonymous_user)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    mcp.run(transport="stdio")
