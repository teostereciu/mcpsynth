from mcp.server.fastmcp import FastMCP

from generated_tools import accounts, bookmarks, favourites, instance, lists, media, notifications, search, statuses, timelines

mcp = FastMCP("mastodon")

# Statuses
mcp.tool()(statuses.create_status)
mcp.tool()(statuses.get_status)
mcp.tool()(statuses.delete_status)
mcp.tool()(statuses.reblog_status)
mcp.tool()(statuses.unreblog_status)
mcp.tool()(statuses.favourite_status)
mcp.tool()(statuses.unfavourite_status)
mcp.tool()(statuses.get_status_context)

# Accounts
mcp.tool()(accounts.verify_credentials)
mcp.tool()(accounts.get_account)
mcp.tool()(accounts.follow_account)
mcp.tool()(accounts.unfollow_account)
mcp.tool()(accounts.get_followers)
mcp.tool()(accounts.get_following)

# Timelines
mcp.tool()(timelines.get_home_timeline)
mcp.tool()(timelines.get_public_timeline)
mcp.tool()(timelines.get_hashtag_timeline)
mcp.tool()(timelines.get_list_timeline)

# Notifications
mcp.tool()(notifications.list_notifications)
mcp.tool()(notifications.get_notification)
mcp.tool()(notifications.dismiss_notification)
mcp.tool()(notifications.clear_notifications)

# Search
mcp.tool()(search.search)

# Lists
mcp.tool()(lists.list_lists)
mcp.tool()(lists.get_list)
mcp.tool()(lists.create_list)
mcp.tool()(lists.update_list)
mcp.tool()(lists.delete_list)
mcp.tool()(lists.add_accounts_to_list)
mcp.tool()(lists.remove_accounts_from_list)
mcp.tool()(lists.get_list_accounts)

# Bookmarks
mcp.tool()(bookmarks.list_bookmarks)
mcp.tool()(bookmarks.bookmark_status)
mcp.tool()(bookmarks.unbookmark_status)

# Favourites
mcp.tool()(favourites.list_favourites)

# Media
mcp.tool()(media.upload_media)

# Instance
mcp.tool()(instance.get_instance)
mcp.tool()(instance.get_instance_activity)
mcp.tool()(instance.get_instance_peers)


if __name__ == "__main__":
    mcp.run()
