from __future__ import annotations

from typing import Any, Dict, List, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools import accounts, bookmarks, favourites, instance, lists, media, notifications, search, statuses, timelines

mcp = FastMCP("mastodon")


# --- Statuses ---
@mcp.tool()
def create_status(
    status: Optional[str] = None,
    media_ids: Optional[List[str]] = None,
    in_reply_to_id: Optional[str] = None,
    sensitive: Optional[bool] = None,
    spoiler_text: Optional[str] = None,
    visibility: Optional[str] = None,
    language: Optional[str] = None,
    scheduled_at: Optional[str] = None,
    poll_options: Optional[List[str]] = None,
    poll_expires_in: Optional[int] = None,
    poll_multiple: Optional[bool] = None,
    poll_hide_totals: Optional[bool] = None,
    quoted_status_id: Optional[str] = None,
    quote_approval_policy: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return statuses.create_status(
        status=status,
        media_ids=media_ids,
        in_reply_to_id=in_reply_to_id,
        sensitive=sensitive,
        spoiler_text=spoiler_text,
        visibility=visibility,
        language=language,
        scheduled_at=scheduled_at,
        poll_options=poll_options,
        poll_expires_in=poll_expires_in,
        poll_multiple=poll_multiple,
        poll_hide_totals=poll_hide_totals,
        quoted_status_id=quoted_status_id,
        quote_approval_policy=quote_approval_policy,
        idempotency_key=idempotency_key,
    )


@mcp.tool()
def get_status(status_id: str) -> Dict[str, Any]:
    return statuses.get_status(status_id)


@mcp.tool()
def delete_status(status_id: str, delete_media: Optional[bool] = None) -> Dict[str, Any]:
    return statuses.delete_status(status_id, delete_media=delete_media)


@mcp.tool()
def get_status_context(status_id: str) -> Dict[str, Any]:
    return statuses.get_status_context(status_id)


@mcp.tool()
def favourite_status(status_id: str) -> Dict[str, Any]:
    return statuses.favourite_status(status_id)


@mcp.tool()
def unfavourite_status(status_id: str) -> Dict[str, Any]:
    return statuses.unfavourite_status(status_id)


@mcp.tool()
def reblog_status(status_id: str) -> Dict[str, Any]:
    return statuses.reblog_status(status_id)


@mcp.tool()
def unreblog_status(status_id: str) -> Dict[str, Any]:
    return statuses.unreblog_status(status_id)


@mcp.tool()
def bookmark_status(status_id: str) -> Dict[str, Any]:
    return statuses.bookmark_status(status_id)


@mcp.tool()
def unbookmark_status(status_id: str) -> Dict[str, Any]:
    return statuses.unbookmark_status(status_id)


# --- Accounts ---
@mcp.tool()
def verify_account_credentials() -> Dict[str, Any]:
    return accounts.verify_account_credentials()


@mcp.tool()
def get_account(account_id: str) -> Dict[str, Any]:
    return accounts.get_account(account_id)


@mcp.tool()
def follow_account(
    account_id: str,
    reblogs: Optional[bool] = None,
    notify: Optional[bool] = None,
    languages: Optional[List[str]] = None,
) -> Dict[str, Any]:
    return accounts.follow_account(account_id, reblogs=reblogs, notify=notify, languages=languages)


@mcp.tool()
def unfollow_account(account_id: str) -> Dict[str, Any]:
    return accounts.unfollow_account(account_id)


@mcp.tool()
def get_account_followers(account_id: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None) -> Dict[str, Any]:
    return accounts.get_account_followers(account_id, limit=limit, max_id=max_id, since_id=since_id)


@mcp.tool()
def get_account_following(account_id: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None) -> Dict[str, Any]:
    return accounts.get_account_following(account_id, limit=limit, max_id=max_id, since_id=since_id)


# --- Timelines ---
@mcp.tool()
def get_home_timeline(limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Dict[str, Any]:
    return timelines.get_home_timeline(limit=limit, max_id=max_id, since_id=since_id, min_id=min_id)


@mcp.tool()
def get_public_timeline(
    local: Optional[bool] = None,
    remote: Optional[bool] = None,
    only_media: Optional[bool] = None,
    limit: Optional[int] = None,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
) -> Dict[str, Any]:
    return timelines.get_public_timeline(local=local, remote=remote, only_media=only_media, limit=limit, max_id=max_id, since_id=since_id, min_id=min_id)


@mcp.tool()
def get_hashtag_timeline(
    hashtag: str,
    local: Optional[bool] = None,
    remote: Optional[bool] = None,
    only_media: Optional[bool] = None,
    limit: Optional[int] = None,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    any_tags: Optional[List[str]] = None,
    all_tags: Optional[List[str]] = None,
    none_tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    return timelines.get_hashtag_timeline(
        hashtag=hashtag,
        local=local,
        remote=remote,
        only_media=only_media,
        limit=limit,
        max_id=max_id,
        since_id=since_id,
        min_id=min_id,
        any_tags=any_tags,
        all_tags=all_tags,
        none_tags=none_tags,
    )


@mcp.tool()
def get_list_timeline(list_id: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Dict[str, Any]:
    return timelines.get_list_timeline(list_id=list_id, limit=limit, max_id=max_id, since_id=since_id, min_id=min_id)


# --- Notifications ---
@mcp.tool()
def list_notifications(
    limit: Optional[int] = None,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    types: Optional[List[str]] = None,
    exclude_types: Optional[List[str]] = None,
    account_id: Optional[str] = None,
    include_filtered: Optional[bool] = None,
) -> Dict[str, Any]:
    return notifications.list_notifications(
        limit=limit,
        max_id=max_id,
        since_id=since_id,
        min_id=min_id,
        types=types,
        exclude_types=exclude_types,
        account_id=account_id,
        include_filtered=include_filtered,
    )


@mcp.tool()
def get_notification(notification_id: str) -> Dict[str, Any]:
    return notifications.get_notification(notification_id)


@mcp.tool()
def dismiss_notification(notification_id: str) -> Dict[str, Any]:
    return notifications.dismiss_notification(notification_id)


@mcp.tool()
def clear_notifications() -> Dict[str, Any]:
    return notifications.clear_notifications()


# --- Search ---
@mcp.tool()
def search_content(
    q: str,
    type: Optional[str] = None,
    resolve: Optional[bool] = None,
    following: Optional[bool] = None,
    account_id: Optional[str] = None,
    exclude_unreviewed: Optional[bool] = None,
    max_id: Optional[str] = None,
    min_id: Optional[str] = None,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> Dict[str, Any]:
    return search.search(
        q=q,
        type=type,
        resolve=resolve,
        following=following,
        account_id=account_id,
        exclude_unreviewed=exclude_unreviewed,
        max_id=max_id,
        min_id=min_id,
        limit=limit,
        offset=offset,
    )


# --- Lists ---
@mcp.tool()
def list_lists() -> Dict[str, Any]:
    return lists.list_lists()


@mcp.tool()
def get_list(list_id: str) -> Dict[str, Any]:
    return lists.get_list(list_id)


@mcp.tool()
def create_list(title: str, replies_policy: Optional[str] = None, exclusive: Optional[bool] = None) -> Dict[str, Any]:
    return lists.create_list(title=title, replies_policy=replies_policy, exclusive=exclusive)


@mcp.tool()
def update_list(list_id: str, title: str, replies_policy: Optional[str] = None, exclusive: Optional[bool] = None) -> Dict[str, Any]:
    return lists.update_list(list_id=list_id, title=title, replies_policy=replies_policy, exclusive=exclusive)


@mcp.tool()
def delete_list(list_id: str) -> Dict[str, Any]:
    return lists.delete_list(list_id)


@mcp.tool()
def get_list_accounts(list_id: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Dict[str, Any]:
    return lists.get_list_accounts(list_id, limit=limit, max_id=max_id, since_id=since_id, min_id=min_id)


@mcp.tool()
def add_accounts_to_list(list_id: str, account_ids: List[str]) -> Dict[str, Any]:
    return lists.add_accounts_to_list(list_id, account_ids)


@mcp.tool()
def remove_accounts_from_list(list_id: str, account_ids: List[str]) -> Dict[str, Any]:
    return lists.remove_accounts_from_list(list_id, account_ids)


# --- Bookmarks/Favourites ---
@mcp.tool()
def list_bookmarks(limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Dict[str, Any]:
    return bookmarks.list_bookmarks(limit=limit, max_id=max_id, since_id=since_id, min_id=min_id)


@mcp.tool()
def list_favourites(limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Dict[str, Any]:
    return favourites.list_favourites(limit=limit, max_id=max_id, since_id=since_id, min_id=min_id)


# --- Media ---
@mcp.tool()
def upload_media(file_path: str, description: Optional[str] = None, focus: Optional[str] = None, thumbnail_path: Optional[str] = None) -> Dict[str, Any]:
    return media.upload_media(file_path=file_path, description=description, focus=focus, thumbnail_path=thumbnail_path)


@mcp.tool()
def get_media(media_id: str) -> Dict[str, Any]:
    return media.get_media(media_id)


# --- Instance ---
@mcp.tool()
def get_instance_info() -> Dict[str, Any]:
    return instance.get_instance_info()


if __name__ == "__main__":
    mcp.run()
