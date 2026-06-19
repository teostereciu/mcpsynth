from mcp.server.fastmcp import FastMCP

from generated_tools.accounts import (
    follow_account,
    get_account,
    get_account_followers,
    get_account_following,
    unfollow_account,
    verify_account_credentials,
)
from generated_tools.bookmarks import list_bookmarks
from generated_tools.favourites import list_favourites
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
from generated_tools.media import delete_media, get_media, update_media, upload_media
from generated_tools.notifications import clear_notifications, dismiss_notification, get_notification, list_notifications
from generated_tools.polls import get_poll, vote_poll
from generated_tools.scheduled_statuses import cancel_scheduled_status, get_scheduled_status, list_scheduled_statuses, update_scheduled_status
from generated_tools.search import search
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
from generated_tools.timelines import get_hashtag_timeline, get_home_timeline, get_list_timeline, get_public_timeline

mcp = FastMCP("mastodon")

for fn in [
    verify_account_credentials,
    get_account,
    follow_account,
    unfollow_account,
    get_account_followers,
    get_account_following,
    create_status,
    get_status,
    delete_status,
    get_status_context,
    favourite_status,
    unfavourite_status,
    boost_status,
    unboost_status,
    bookmark_status,
    unbookmark_status,
    get_home_timeline,
    get_public_timeline,
    get_hashtag_timeline,
    get_list_timeline,
    list_notifications,
    get_notification,
    dismiss_notification,
    clear_notifications,
    upload_media,
    get_media,
    update_media,
    delete_media,
    search,
    list_bookmarks,
    list_favourites,
    get_poll,
    vote_poll,
    list_scheduled_statuses,
    get_scheduled_status,
    update_scheduled_status,
    cancel_scheduled_status,
    list_lists,
    get_list,
    create_list,
    update_list,
    delete_list,
    get_list_accounts,
    add_accounts_to_list,
    remove_accounts_from_list,
]:
    mcp.tool()(fn)


if __name__ == "__main__":
    mcp.run()
