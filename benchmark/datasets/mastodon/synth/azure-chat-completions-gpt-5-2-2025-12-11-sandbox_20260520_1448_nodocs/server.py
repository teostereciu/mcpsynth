from mcp.server.fastmcp import FastMCP

from generated_tools.statuses import (
    create_status,
    delete_status,
    favourite_status,
    get_status,
    get_status_context,
    reblog_status,
    unfavourite_status,
    unreblog_status,
)
from generated_tools.accounts import (
    follow_account,
    get_account,
    get_followers,
    get_following,
    unfollow_account,
    verify_credentials,
)
from generated_tools.timelines import (
    get_hashtag_timeline,
    get_home_timeline,
    get_list_timeline,
    get_public_timeline,
)
from generated_tools.notifications import (
    clear_notifications,
    dismiss_notification,
    get_notification,
    list_notifications,
)
from generated_tools.search import search
from generated_tools.lists import (
    add_accounts_to_list,
    create_list,
    delete_list,
    get_list,
    get_list_accounts,
    list_lists,
    remove_accounts_from_list,
    update_list,
)
from generated_tools.bookmarks import list_bookmarks, bookmark_status, unbookmark_status
from generated_tools.favourites import list_favourites
from generated_tools.media import upload_media
from generated_tools.instance import get_instance


mcp = FastMCP("mastodon")

# Statuses
mcp.tool()(create_status)
mcp.tool()(get_status)
mcp.tool()(delete_status)
mcp.tool()(reblog_status)
mcp.tool()(unreblog_status)
mcp.tool()(favourite_status)
mcp.tool()(unfavourite_status)
mcp.tool()(get_status_context)

# Accounts
mcp.tool()(verify_credentials)
mcp.tool()(get_account)
mcp.tool()(follow_account)
mcp.tool()(unfollow_account)
mcp.tool()(get_followers)
mcp.tool()(get_following)

# Timelines
mcp.tool()(get_home_timeline)
mcp.tool()(get_public_timeline)
mcp.tool()(get_hashtag_timeline)
mcp.tool()(get_list_timeline)

# Notifications
mcp.tool()(list_notifications)
mcp.tool()(get_notification)
mcp.tool()(dismiss_notification)
mcp.tool()(clear_notifications)

# Search
mcp.tool()(search)

# Lists
mcp.tool()(list_lists)
mcp.tool()(get_list)
mcp.tool()(create_list)
mcp.tool()(update_list)
mcp.tool()(delete_list)
mcp.tool()(get_list_accounts)
mcp.tool()(add_accounts_to_list)
mcp.tool()(remove_accounts_from_list)

# Bookmarks
mcp.tool()(list_bookmarks)
mcp.tool()(bookmark_status)
mcp.tool()(unbookmark_status)

# Favourites
mcp.tool()(list_favourites)

# Media
mcp.tool()(upload_media)

# Instance
mcp.tool()(get_instance)


if __name__ == "__main__":
    mcp.run()
