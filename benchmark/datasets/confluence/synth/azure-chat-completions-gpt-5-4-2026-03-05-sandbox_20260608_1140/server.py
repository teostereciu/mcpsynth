from mcp.server.fastmcp import FastMCP

from generated_tools.labels import (
    add_labels_to_content,
    remove_label_from_content,
    remove_label_from_content_by_query,
)
from generated_tools.pages import (
    create_page,
    delete_page,
    get_page,
    get_pages_for_label,
    get_pages_in_space,
    list_pages,
    update_page,
    update_page_title,
)
from generated_tools.search import search_content, search_users
from generated_tools.spaces import create_space, get_space, list_spaces
from generated_tools.users import (
    get_anonymous_user,
    get_current_user,
    get_user,
    get_user_email,
    get_user_emails_bulk,
    get_user_group_memberships,
    get_users_bulk,
)
from generated_tools.versions import delete_content_version, restore_content_version

mcp = FastMCP("confluence-cloud")

mcp.tool()(list_pages)
mcp.tool()(create_page)
mcp.tool()(get_page)
mcp.tool()(update_page)
mcp.tool()(delete_page)
mcp.tool()(update_page_title)
mcp.tool()(get_pages_for_label)
mcp.tool()(get_pages_in_space)

mcp.tool()(list_spaces)
mcp.tool()(create_space)
mcp.tool()(get_space)

mcp.tool()(search_content)
mcp.tool()(search_users)

mcp.tool()(add_labels_to_content)
mcp.tool()(remove_label_from_content_by_query)
mcp.tool()(remove_label_from_content)

mcp.tool()(restore_content_version)
mcp.tool()(delete_content_version)

mcp.tool()(get_user)
mcp.tool()(get_anonymous_user)
mcp.tool()(get_current_user)
mcp.tool()(get_user_group_memberships)
mcp.tool()(get_users_bulk)
mcp.tool()(get_user_email)
mcp.tool()(get_user_emails_bulk)


if __name__ == "__main__":
    mcp.run()
