from mcp.server.fastmcp import FastMCP

from generated_tools.accounts import (
    follow_account,
    get_account,
    get_account_followers,
    get_account_following,
    unfollow_account,
    verify_credentials,
)
from generated_tools.bookmarks import (
    bookmark_status,
    list_bookmarks,
    list_favourites,
    unbookmark_status,
)
from generated_tools.instance import get_instance_activity, get_instance_info
from generated_tools.lists import (
    add_accounts_to_list,
    create_list,
    delete_list,
    get_list,
    get_lists,
    remove_accounts_from_list,
    update_list,
)
from generated_tools.media import upload_media
from generated_tools.notifications import (
    clear_notifications,
    dismiss_notification,
    get_notification,
    list_notifications,
)
from generated_tools.search import search
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
from generated_tools.timelines import (
    get_hashtag_timeline,
    get_home_timeline,
    get_list_timeline,
    get_public_timeline,
)

mcp = FastMCP("mastodon")

mcp.tool()(create_status)
mcp.tool()(get_status)
mcp.tool()(delete_status)
mcp.tool()(reblog_status)
mcp.tool()(unreblog_status)
mcp.tool()(favourite_status)
mcp.tool()(unfavourite_status)
mcp.tool()(get_status_context)

mcp.tool()(verify_credentials)
mcp.tool()(get_account)
mcp.tool()(follow_account)
mcp.tool()(unfollow_account)
mcp.tool()(get_account_followers)
mcp.tool()(get_account_following)

mcp.tool()(get_home_timeline)
mcp.tool()(get_public_timeline)
mcp.tool()(get_hashtag_timeline)
mcp.tool()(get_list_timeline)

mcp.tool()(list_notifications)
mcp.tool()(get_notification)
mcp.tool()(dismiss_notification)
mcp.tool()(clear_notifications)

mcp.tool()(search)

mcp.tool()(get_lists)
mcp.tool()(create_list)
mcp.tool()(get_list)
mcp.tool()(update_list)
mcp.tool()(delete_list)
mcp.tool()(add_accounts_to_list)
mcp.tool()(remove_accounts_from_list)

mcp.tool()(list_bookmarks)
mcp.tool()(bookmark_status)
mcp.tool()(unbookmark_status)
mcp.tool()(list_favourites)

mcp.tool()(upload_media)

mcp.tool()(get_instance_info)
mcp.tool()(get_instance_activity)

if __name__ == "__main__":
    mcp.run()
