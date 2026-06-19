from mcp.server.fastmcp import FastMCP

from generated_tools.accounts import (
    follow_account,
    get_account,
    get_account_followers,
    get_account_following,
    unfollow_account,
    verify_account_credentials,
)
from generated_tools.bookmarks import get_bookmarks
from generated_tools.favourites import get_favourites
from generated_tools.instance import get_instance_info
from generated_tools.lists import (
    add_accounts_to_list,
    create_list,
    delete_list,
    get_list,
    get_list_accounts,
    get_lists,
    remove_accounts_from_list,
    update_list,
)
from generated_tools.media import delete_media, get_media, update_media, upload_media
from generated_tools.notifications import (
    clear_notifications,
    dismiss_notification,
    get_notification,
    list_notifications,
)
from generated_tools.search import search_content
from generated_tools.statuses import (
    bookmark_status,
    boost_status,
    create_status,
    delete_status,
    favourite_status,
    get_status,
    get_status_context,
    unbookmark_status,
    unboost_status,
    unfavourite_status,
)
from generated_tools.timelines import (
    get_hashtag_timeline,
    get_home_timeline,
    get_list_timeline,
    get_public_timeline,
)


mcp = FastMCP("mastodon")

mcp.tool()(verify_account_credentials)
mcp.tool()(get_account)
mcp.tool()(follow_account)
mcp.tool()(unfollow_account)
mcp.tool()(get_account_followers)
mcp.tool()(get_account_following)

mcp.tool()(create_status)
mcp.tool()(get_status)
mcp.tool()(delete_status)
mcp.tool()(get_status_context)
mcp.tool()(favourite_status)
mcp.tool()(unfavourite_status)
mcp.tool()(boost_status)
mcp.tool()(unboost_status)
mcp.tool()(bookmark_status)
mcp.tool()(unbookmark_status)

mcp.tool()(get_home_timeline)
mcp.tool()(get_public_timeline)
mcp.tool()(get_hashtag_timeline)
mcp.tool()(get_list_timeline)

mcp.tool()(list_notifications)
mcp.tool()(get_notification)
mcp.tool()(dismiss_notification)
mcp.tool()(clear_notifications)

mcp.tool()(search_content)

mcp.tool()(get_lists)
mcp.tool()(get_list)
mcp.tool()(create_list)
mcp.tool()(update_list)
mcp.tool()(delete_list)
mcp.tool()(get_list_accounts)
mcp.tool()(add_accounts_to_list)
mcp.tool()(remove_accounts_from_list)

mcp.tool()(upload_media)
mcp.tool()(get_media)
mcp.tool()(update_media)
mcp.tool()(delete_media)

mcp.tool()(get_bookmarks)
mcp.tool()(get_favourites)
mcp.tool()(get_instance_info)


if __name__ == "__main__":
    mcp.run()
