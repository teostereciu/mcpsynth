"""
MCP Server for the Mastodon API.

Runs over stdio using FastMCP.
All tools are registered individually so they appear in list_tools().

Environment variables required:
  MASTODON_ACCESS_TOKEN  — OAuth 2.0 Bearer token
  MASTODON_BASE_URL      — Instance base URL, e.g. https://mastodon.social
"""

from mcp.server.fastmcp import FastMCP

# ── domain modules ──────────────────────────────────────────────────────────
from generated_tools.statuses import (
    post_status,
    get_status,
    delete_status,
    boost_status,
    unboost_status,
    favourite_status,
    unfavourite_status,
    get_status_context,
    get_status_reblogged_by,
    get_status_favourited_by,
    bookmark_status,
    unbookmark_status,
)
from generated_tools.accounts import (
    get_authenticated_account,
    get_account,
    follow_account,
    unfollow_account,
    get_account_followers,
    get_account_following,
    get_account_statuses,
    get_relationships,
    mute_account,
    unmute_account,
    block_account,
    unblock_account,
    update_credentials,
)
from generated_tools.timelines import (
    get_home_timeline,
    get_public_timeline,
    get_hashtag_timeline,
    get_list_timeline,
)
from generated_tools.notifications import (
    list_notifications,
    get_notification,
    dismiss_notification,
    clear_all_notifications,
)
from generated_tools.search import (
    search,
    search_accounts,
    search_hashtags,
    search_statuses,
)
from generated_tools.lists import (
    get_lists,
    get_list,
    create_list,
    update_list,
    delete_list,
    get_list_accounts,
    add_accounts_to_list,
    remove_accounts_from_list,
)
from generated_tools.bookmarks import get_bookmarks
from generated_tools.favourites import get_favourites
from generated_tools.media import upload_media, get_media, update_media
from generated_tools.instance import (
    get_instance,
    get_instance_peers,
    get_instance_activity,
    get_instance_rules,
)

# ── server setup ────────────────────────────────────────────────────────────
mcp = FastMCP(
    name="mastodon",
    description="MCP server exposing the Mastodon REST API as callable tools.",
)

# ============================================================================
# STATUSES
# ============================================================================

@mcp.tool()
def tool_post_status(
    status: str,
    in_reply_to_id: str = None,
    media_ids: list = None,
    sensitive: bool = False,
    spoiler_text: str = None,
    visibility: str = "public",
    language: str = None,
) -> dict:
    """
    Publish a new status (toot).

    Args:
        status: The text content of the status.
        in_reply_to_id: ID of the status being replied to.
        media_ids: List of media attachment IDs to attach (up to 4).
        sensitive: Mark the media as sensitive.
        spoiler_text: Content warning / subject text.
        visibility: 'public', 'unlisted', 'private', or 'direct'.
        language: ISO 639-1 language code for the status.
    """
    return post_status(
        status=status,
        in_reply_to_id=in_reply_to_id,
        media_ids=media_ids,
        sensitive=sensitive,
        spoiler_text=spoiler_text,
        visibility=visibility,
        language=language,
    )


@mcp.tool()
def tool_get_status(status_id: str) -> dict:
    """
    Fetch a single status by its ID.

    Args:
        status_id: The ID of the status.
    """
    return get_status(status_id)


@mcp.tool()
def tool_delete_status(status_id: str) -> dict:
    """
    Delete a status authored by the authenticated account.

    Args:
        status_id: The ID of the status to delete.
    """
    return delete_status(status_id)


@mcp.tool()
def tool_boost_status(status_id: str, visibility: str = "public") -> dict:
    """
    Boost (reblog) a status.

    Args:
        status_id: The ID of the status to boost.
        visibility: Visibility of the boost ('public', 'unlisted', 'private').
    """
    return boost_status(status_id, visibility=visibility)


@mcp.tool()
def tool_unboost_status(status_id: str) -> dict:
    """
    Undo a boost of a status.

    Args:
        status_id: The ID of the status to unboost.
    """
    return unboost_status(status_id)


@mcp.tool()
def tool_favourite_status(status_id: str) -> dict:
    """
    Favourite (like) a status.

    Args:
        status_id: The ID of the status to favourite.
    """
    return favourite_status(status_id)


@mcp.tool()
def tool_unfavourite_status(status_id: str) -> dict:
    """
    Remove a favourite from a status.

    Args:
        status_id: The ID of the status to unfavourite.
    """
    return unfavourite_status(status_id)


@mcp.tool()
def tool_get_status_context(status_id: str) -> dict:
    """
    Retrieve the ancestors and descendants of a status (the thread).

    Args:
        status_id: The ID of the status.
    """
    return get_status_context(status_id)


@mcp.tool()
def tool_get_status_reblogged_by(status_id: str) -> list:
    """
    List accounts that boosted a given status.

    Args:
        status_id: The ID of the status.
    """
    return get_status_reblogged_by(status_id)


@mcp.tool()
def tool_get_status_favourited_by(status_id: str) -> list:
    """
    List accounts that favourited a given status.

    Args:
        status_id: The ID of the status.
    """
    return get_status_favourited_by(status_id)


@mcp.tool()
def tool_bookmark_status(status_id: str) -> dict:
    """
    Bookmark a status for the authenticated account.

    Args:
        status_id: The ID of the status to bookmark.
    """
    return bookmark_status(status_id)


@mcp.tool()
def tool_unbookmark_status(status_id: str) -> dict:
    """
    Remove a bookmark from a status.

    Args:
        status_id: The ID of the status to unbookmark.
    """
    return unbookmark_status(status_id)


# ============================================================================
# ACCOUNTS
# ============================================================================

@mcp.tool()
def tool_get_authenticated_account() -> dict:
    """Return the account of the currently authenticated user."""
    return get_authenticated_account()


@mcp.tool()
def tool_get_account(account_id: str) -> dict:
    """
    Fetch a public account by its ID.

    Args:
        account_id: The ID of the account.
    """
    return get_account(account_id)


@mcp.tool()
def tool_follow_account(
    account_id: str, reblogs: bool = True, notify: bool = False
) -> dict:
    """
    Follow an account.

    Args:
        account_id: The ID of the account to follow.
        reblogs: Whether to show boosts from this account in the home timeline.
        notify: Whether to receive notifications when this account posts.
    """
    return follow_account(account_id, reblogs=reblogs, notify=notify)


@mcp.tool()
def tool_unfollow_account(account_id: str) -> dict:
    """
    Unfollow an account.

    Args:
        account_id: The ID of the account to unfollow.
    """
    return unfollow_account(account_id)


@mcp.tool()
def tool_get_account_followers(
    account_id: str,
    max_id: str = None,
    since_id: str = None,
    limit: int = 40,
) -> list:
    """
    List accounts that follow the given account.

    Args:
        account_id: The ID of the account.
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
        limit: Maximum number of results (default 40, max 80).
    """
    return get_account_followers(
        account_id, max_id=max_id, since_id=since_id, limit=limit
    )


@mcp.tool()
def tool_get_account_following(
    account_id: str,
    max_id: str = None,
    since_id: str = None,
    limit: int = 40,
) -> list:
    """
    List accounts that the given account follows.

    Args:
        account_id: The ID of the account.
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
        limit: Maximum number of results (default 40, max 80).
    """
    return get_account_following(
        account_id, max_id=max_id, since_id=since_id, limit=limit
    )


@mcp.tool()
def tool_get_account_statuses(
    account_id: str,
    max_id: str = None,
    since_id: str = None,
    min_id: str = None,
    limit: int = 20,
    only_media: bool = False,
    exclude_replies: bool = False,
    exclude_reblogs: bool = False,
    pinned: bool = False,
    tagged: str = None,
) -> list:
    """
    List statuses posted by the given account.

    Args:
        account_id: The ID of the account.
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
        min_id: Return results immediately newer than this ID.
        limit: Maximum number of results (default 20, max 40).
        only_media: Only return statuses with media attachments.
        exclude_replies: Skip statuses that are replies.
        exclude_reblogs: Skip statuses that are boosts.
        pinned: Only return pinned statuses.
        tagged: Only return statuses with this hashtag.
    """
    return get_account_statuses(
        account_id,
        max_id=max_id,
        since_id=since_id,
        min_id=min_id,
        limit=limit,
        only_media=only_media,
        exclude_replies=exclude_replies,
        exclude_reblogs=exclude_reblogs,
        pinned=pinned,
        tagged=tagged,
    )


@mcp.tool()
def tool_get_relationships(account_ids: list) -> list:
    """
    Return relationship info between the authenticated account and the given accounts.

    Args:
        account_ids: A list of account IDs to check.
    """
    return get_relationships(account_ids)


@mcp.tool()
def tool_mute_account(
    account_id: str, notifications: bool = True, duration: int = 0
) -> dict:
    """
    Mute an account.

    Args:
        account_id: The ID of the account to mute.
        notifications: Whether to mute notifications from this account.
        duration: Duration of the mute in seconds (0 = indefinite).
    """
    return mute_account(account_id, notifications=notifications, duration=duration)


@mcp.tool()
def tool_unmute_account(account_id: str) -> dict:
    """
    Unmute an account.

    Args:
        account_id: The ID of the account to unmute.
    """
    return unmute_account(account_id)


@mcp.tool()
def tool_block_account(account_id: str) -> dict:
    """
    Block an account.

    Args:
        account_id: The ID of the account to block.
    """
    return block_account(account_id)


@mcp.tool()
def tool_unblock_account(account_id: str) -> dict:
    """
    Unblock an account.

    Args:
        account_id: The ID of the account to unblock.
    """
    return unblock_account(account_id)


@mcp.tool()
def tool_update_credentials(
    display_name: str = None,
    note: str = None,
    avatar: str = None,
    header: str = None,
    locked: bool = None,
    bot: bool = None,
    discoverable: bool = None,
) -> dict:
    """
    Update the authenticated account's profile.

    Args:
        display_name: New display name.
        note: New bio / profile note.
        avatar: Base64-encoded avatar image (data URI).
        header: Base64-encoded header image (data URI).
        locked: Whether the account requires follow approval.
        bot: Whether the account is a bot.
        discoverable: Whether the account is listed in the directory.
    """
    return update_credentials(
        display_name=display_name,
        note=note,
        avatar=avatar,
        header=header,
        locked=locked,
        bot=bot,
        discoverable=discoverable,
    )


# ============================================================================
# TIMELINES
# ============================================================================

@mcp.tool()
def tool_get_home_timeline(
    max_id: str = None,
    since_id: str = None,
    min_id: str = None,
    limit: int = 20,
) -> list:
    """
    Return statuses from accounts the authenticated user follows.

    Args:
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
        min_id: Return results immediately newer than this ID.
        limit: Maximum number of results (default 20, max 40).
    """
    return get_home_timeline(
        max_id=max_id, since_id=since_id, min_id=min_id, limit=limit
    )


@mcp.tool()
def tool_get_public_timeline(
    local: bool = False,
    remote: bool = False,
    only_media: bool = False,
    max_id: str = None,
    since_id: str = None,
    min_id: str = None,
    limit: int = 20,
) -> list:
    """
    Return statuses from the public (federated) timeline.

    Args:
        local: Only return statuses from the local instance.
        remote: Only return statuses from remote instances.
        only_media: Only return statuses with media attachments.
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
        min_id: Return results immediately newer than this ID.
        limit: Maximum number of results (default 20, max 40).
    """
    return get_public_timeline(
        local=local,
        remote=remote,
        only_media=only_media,
        max_id=max_id,
        since_id=since_id,
        min_id=min_id,
        limit=limit,
    )


@mcp.tool()
def tool_get_hashtag_timeline(
    hashtag: str,
    local: bool = False,
    remote: bool = False,
    only_media: bool = False,
    max_id: str = None,
    since_id: str = None,
    min_id: str = None,
    limit: int = 20,
) -> list:
    """
    Return statuses containing the given hashtag.

    Args:
        hashtag: The hashtag to search (without the '#' prefix).
        local: Only return statuses from the local instance.
        remote: Only return statuses from remote instances.
        only_media: Only return statuses with media attachments.
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
        min_id: Return results immediately newer than this ID.
        limit: Maximum number of results (default 20, max 40).
    """
    return get_hashtag_timeline(
        hashtag,
        local=local,
        remote=remote,
        only_media=only_media,
        max_id=max_id,
        since_id=since_id,
        min_id=min_id,
        limit=limit,
    )


@mcp.tool()
def tool_get_list_timeline(
    list_id: str,
    max_id: str = None,
    since_id: str = None,
    min_id: str = None,
    limit: int = 20,
) -> list:
    """
    Return statuses from accounts in the given list.

    Args:
        list_id: The ID of the list.
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
        min_id: Return results immediately newer than this ID.
        limit: Maximum number of results (default 20, max 40).
    """
    return get_list_timeline(
        list_id, max_id=max_id, since_id=since_id, min_id=min_id, limit=limit
    )


# ============================================================================
# NOTIFICATIONS
# ============================================================================

@mcp.tool()
def tool_list_notifications(
    max_id: str = None,
    since_id: str = None,
    min_id: str = None,
    limit: int = 15,
    types: list = None,
    exclude_types: list = None,
    account_id: str = None,
) -> list:
    """
    Return notifications for the authenticated account.

    Args:
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
        min_id: Return results immediately newer than this ID.
        limit: Maximum number of results (default 15, max 30).
        types: List of notification types to include
               ('mention', 'status', 'reblog', 'follow', 'follow_request',
                'favourite', 'poll', 'update').
        exclude_types: List of notification types to exclude.
        account_id: Only return notifications from this account.
    """
    return list_notifications(
        max_id=max_id,
        since_id=since_id,
        min_id=min_id,
        limit=limit,
        types=types,
        exclude_types=exclude_types,
        account_id=account_id,
    )


@mcp.tool()
def tool_get_notification(notification_id: str) -> dict:
    """
    Fetch a single notification by its ID.

    Args:
        notification_id: The ID of the notification.
    """
    return get_notification(notification_id)


@mcp.tool()
def tool_dismiss_notification(notification_id: str) -> dict:
    """
    Dismiss (delete) a single notification.

    Args:
        notification_id: The ID of the notification to dismiss.
    """
    return dismiss_notification(notification_id)


@mcp.tool()
def tool_clear_all_notifications() -> dict:
    """Delete all notifications for the authenticated account."""
    return clear_all_notifications()


# ============================================================================
# SEARCH
# ============================================================================

@mcp.tool()
def tool_search(
    query: str,
    search_type: str = None,
    resolve: bool = False,
    following: bool = False,
    account_id: str = None,
    max_id: str = None,
    min_id: str = None,
    limit: int = 20,
    offset: int = 0,
) -> dict:
    """
    Search for accounts, statuses, and hashtags.

    Args:
        query: The search query string.
        search_type: Restrict results to 'accounts', 'statuses', or 'hashtags'.
        resolve: Attempt to resolve non-local accounts and statuses via WebFinger.
        following: Only include accounts the authenticated user follows.
        account_id: Restrict statuses to those from this account.
        max_id: Return results older than this ID (statuses only).
        min_id: Return results immediately newer than this ID (statuses only).
        limit: Maximum number of results per category (default 20, max 40).
        offset: Skip the first N results (for pagination).
    """
    return search(
        query=query,
        search_type=search_type,
        resolve=resolve,
        following=following,
        account_id=account_id,
        max_id=max_id,
        min_id=min_id,
        limit=limit,
        offset=offset,
    )


@mcp.tool()
def tool_search_accounts(
    query: str,
    limit: int = 40,
    resolve: bool = False,
    following: bool = False,
) -> list:
    """
    Search for accounts matching the query string.

    Args:
        query: The search query (username, display name, or Webfinger address).
        limit: Maximum number of results (default 40, max 80).
        resolve: Attempt to resolve non-local accounts via WebFinger.
        following: Only include accounts the authenticated user follows.
    """
    return search_accounts(query, limit=limit, resolve=resolve, following=following)


@mcp.tool()
def tool_search_hashtags(query: str, limit: int = 20) -> list:
    """
    Search for hashtags matching the query string.

    Args:
        query: The hashtag search query (without '#').
        limit: Maximum number of results (default 20).
    """
    return search_hashtags(query, limit=limit)


@mcp.tool()
def tool_search_statuses(
    query: str,
    limit: int = 20,
    account_id: str = None,
    max_id: str = None,
    min_id: str = None,
    offset: int = 0,
) -> list:
    """
    Search for statuses matching the query string.

    Args:
        query: The search query.
        limit: Maximum number of results (default 20).
        account_id: Restrict results to statuses from this account.
        max_id: Return results older than this ID.
        min_id: Return results immediately newer than this ID.
        offset: Skip the first N results.
    """
    return search_statuses(
        query,
        limit=limit,
        account_id=account_id,
        max_id=max_id,
        min_id=min_id,
        offset=offset,
    )


# ============================================================================
# LISTS
# ============================================================================

@mcp.tool()
def tool_get_lists() -> list:
    """Return all lists owned by the authenticated account."""
    return get_lists()


@mcp.tool()
def tool_get_list(list_id: str) -> dict:
    """
    Fetch a single list by its ID.

    Args:
        list_id: The ID of the list.
    """
    return get_list(list_id)


@mcp.tool()
def tool_create_list(
    title: str,
    replies_policy: str = "list",
    exclusive: bool = False,
) -> dict:
    """
    Create a new list.

    Args:
        title: The title of the list.
        replies_policy: How replies are handled: 'followed', 'list', or 'none'.
        exclusive: Whether members' posts are removed from the home timeline.
    """
    return create_list(title, replies_policy=replies_policy, exclusive=exclusive)


@mcp.tool()
def tool_update_list(
    list_id: str,
    title: str = None,
    replies_policy: str = None,
    exclusive: bool = None,
) -> dict:
    """
    Update an existing list.

    Args:
        list_id: The ID of the list to update.
        title: New title for the list.
        replies_policy: New replies policy: 'followed', 'list', or 'none'.
        exclusive: Whether members' posts are removed from the home timeline.
    """
    return update_list(
        list_id, title=title, replies_policy=replies_policy, exclusive=exclusive
    )


@mcp.tool()
def tool_delete_list(list_id: str) -> dict:
    """
    Delete a list.

    Args:
        list_id: The ID of the list to delete.
    """
    return delete_list(list_id)


@mcp.tool()
def tool_get_list_accounts(
    list_id: str,
    max_id: str = None,
    since_id: str = None,
    limit: int = 40,
) -> list:
    """
    Return accounts that are members of the given list.

    Args:
        list_id: The ID of the list.
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
        limit: Maximum number of results (default 40, max 80).
    """
    return get_list_accounts(list_id, max_id=max_id, since_id=since_id, limit=limit)


@mcp.tool()
def tool_add_accounts_to_list(list_id: str, account_ids: list) -> dict:
    """
    Add one or more accounts to a list.

    Args:
        list_id: The ID of the list.
        account_ids: A list of account IDs to add.
    """
    return add_accounts_to_list(list_id, account_ids)


@mcp.tool()
def tool_remove_accounts_from_list(list_id: str, account_ids: list) -> dict:
    """
    Remove one or more accounts from a list.

    Args:
        list_id: The ID of the list.
        account_ids: A list of account IDs to remove.
    """
    return remove_accounts_from_list(list_id, account_ids)


# ============================================================================
# BOOKMARKS
# ============================================================================

@mcp.tool()
def tool_get_bookmarks(
    max_id: str = None,
    since_id: str = None,
    min_id: str = None,
    limit: int = 20,
) -> list:
    """
    Return statuses bookmarked by the authenticated account.

    Args:
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
        min_id: Return results immediately newer than this ID.
        limit: Maximum number of results (default 20, max 40).
    """
    return get_bookmarks(max_id=max_id, since_id=since_id, min_id=min_id, limit=limit)


# ============================================================================
# FAVOURITES
# ============================================================================

@mcp.tool()
def tool_get_favourites(
    max_id: str = None,
    since_id: str = None,
    min_id: str = None,
    limit: int = 20,
) -> list:
    """
    Return statuses favourited by the authenticated account.

    Args:
        max_id: Return results older than this ID.
        since_id: Return results newer than this ID.
        min_id: Return results immediately newer than this ID.
        limit: Maximum number of results (default 20, max 40).
    """
    return get_favourites(max_id=max_id, since_id=since_id, min_id=min_id, limit=limit)


# ============================================================================
# MEDIA
# ============================================================================

@mcp.tool()
def tool_upload_media(
    file_path: str,
    description: str = None,
    focus_x: float = None,
    focus_y: float = None,
) -> dict:
    """
    Upload a media file and return a media attachment object.
    The returned 'id' can be passed to tool_post_status() as part of media_ids.

    Args:
        file_path: Local filesystem path to the file to upload.
        description: Plain-text description (alt text) for the media.
        focus_x: Horizontal focal point (-1.0 to 1.0).
        focus_y: Vertical focal point (-1.0 to 1.0).
    """
    return upload_media(
        file_path, description=description, focus_x=focus_x, focus_y=focus_y
    )


@mcp.tool()
def tool_get_media(media_id: str) -> dict:
    """
    Fetch a media attachment by its ID (useful for checking async processing status).

    Args:
        media_id: The ID of the media attachment.
    """
    return get_media(media_id)


@mcp.tool()
def tool_update_media(
    media_id: str,
    description: str = None,
    focus_x: float = None,
    focus_y: float = None,
) -> dict:
    """
    Update the description or focal point of an existing media attachment.

    Args:
        media_id: The ID of the media attachment to update.
        description: New plain-text description (alt text).
        focus_x: New horizontal focal point (-1.0 to 1.0).
        focus_y: New vertical focal point (-1.0 to 1.0).
    """
    return update_media(media_id, description=description, focus_x=focus_x, focus_y=focus_y)


# ============================================================================
# INSTANCE
# ============================================================================

@mcp.tool()
def tool_get_instance() -> dict:
    """
    Return general information about the Mastodon instance
    (title, description, version, stats, languages, contact, rules).
    """
    return get_instance()


@mcp.tool()
def tool_get_instance_peers() -> list:
    """Return a list of domains that the instance is aware of (federated peers)."""
    return get_instance_peers()


@mcp.tool()
def tool_get_instance_activity() -> list:
    """Return weekly activity statistics for the instance (last 12 weeks)."""
    return get_instance_activity()


@mcp.tool()
def tool_get_instance_rules() -> list:
    """Return the rules of the Mastodon instance."""
    return get_instance_rules()


# ============================================================================
# Entry point
# ============================================================================

if __name__ == "__main__":
    mcp.run(transport="stdio")
