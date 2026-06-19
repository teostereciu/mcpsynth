import json
from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.http_client import MastodonClient
from generated_tools import (
    accounts,
    bookmarks,
    favourites,
    instance,
    lists,
    media,
    notifications,
    search,
    statuses,
    timelines,
)

mcp = FastMCP("mastodon")


def _client(base_url: Optional[str] = None, access_token: Optional[str] = None) -> MastodonClient:
    return MastodonClient(base_url=base_url, access_token=access_token)


@mcp.tool()
def mastodon_status_create(
    status: str,
    in_reply_to_id: Optional[str] = None,
    media_ids: Optional[list[str]] = None,
    sensitive: Optional[bool] = None,
    spoiler_text: Optional[str] = None,
    visibility: Optional[str] = None,
    language: Optional[str] = None,
    scheduled_at: Optional[str] = None,
    poll: Optional[Dict[str, Any]] = None,
    quote_id: Optional[str] = None,
    base_url: Optional[str] = None,
    access_token: Optional[str] = None,
) -> Any:
    return statuses.create_status(
        status=status,
        in_reply_to_id=in_reply_to_id,
        media_ids=media_ids,
        sensitive=sensitive,
        spoiler_text=spoiler_text,
        visibility=visibility,
        language=language,
        scheduled_at=scheduled_at,
        poll=poll,
        quote_id=quote_id,
        client=_client(base_url, access_token),
    )


@mcp.tool()
def mastodon_status_get(status_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return statuses.get_status(status_id=status_id, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_status_delete(status_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return statuses.delete_status(status_id=status_id, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_status_boost(status_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return statuses.reblog_status(status_id=status_id, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_status_unboost(status_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return statuses.unreblog_status(status_id=status_id, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_status_favourite(status_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return statuses.favourite_status(status_id=status_id, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_status_unfavourite(status_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return statuses.unfavourite_status(status_id=status_id, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_status_bookmark(status_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return statuses.bookmark_status(status_id=status_id, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_status_unbookmark(status_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return statuses.unbookmark_status(status_id=status_id, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_status_context(status_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return statuses.get_status_context(status_id=status_id, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_account_verify_credentials(base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return accounts.verify_credentials(client=_client(base_url, access_token))


@mcp.tool()
def mastodon_account_get(account_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return accounts.get_account(account_id=account_id, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_account_follow(account_id: str, params: Optional[Dict[str, Any]] = None, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return accounts.follow_account(account_id=account_id, params=params, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_account_unfollow(account_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return accounts.unfollow_account(account_id=account_id, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_account_followers(account_id: str, params: Optional[Dict[str, Any]] = None, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return accounts.get_followers(account_id=account_id, params=params, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_account_following(account_id: str, params: Optional[Dict[str, Any]] = None, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return accounts.get_following(account_id=account_id, params=params, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_timeline_home(params: Optional[Dict[str, Any]] = None, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return timelines.home_timeline(params=params, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_timeline_public(params: Optional[Dict[str, Any]] = None, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return timelines.public_timeline(params=params, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_timeline_hashtag(hashtag: str, params: Optional[Dict[str, Any]] = None, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return timelines.hashtag_timeline(hashtag=hashtag, params=params, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_timeline_list(list_id: str, params: Optional[Dict[str, Any]] = None, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return timelines.list_timeline(list_id=list_id, params=params, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_notifications_list(params: Optional[Dict[str, Any]] = None, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return notifications.list_notifications(params=params, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_notifications_get(notification_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return notifications.get_notification(notification_id=notification_id, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_notifications_dismiss(notification_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return notifications.dismiss_notification(notification_id=notification_id, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_notifications_clear(base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return notifications.clear_notifications(client=_client(base_url, access_token))


@mcp.tool()
def mastodon_search(q: str, params: Optional[Dict[str, Any]] = None, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return search.search_v2(q=q, params=params, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_lists_list(base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return lists.list_lists(client=_client(base_url, access_token))


@mcp.tool()
def mastodon_lists_create(title: str, replies_policy: Optional[str] = None, exclusive: Optional[bool] = None, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return lists.create_list(title=title, replies_policy=replies_policy, exclusive=exclusive, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_lists_get(list_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return lists.get_list(list_id=list_id, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_lists_update(list_id: str, params: Dict[str, Any], base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return lists.update_list(list_id=list_id, params=params, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_lists_delete(list_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return lists.delete_list(list_id=list_id, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_lists_accounts_get(list_id: str, params: Optional[Dict[str, Any]] = None, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return lists.get_list_accounts(list_id=list_id, params=params, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_lists_accounts_add(list_id: str, account_ids: list[str], base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return lists.add_list_accounts(list_id=list_id, account_ids=account_ids, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_lists_accounts_remove(list_id: str, account_ids: list[str], base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return lists.remove_list_accounts(list_id=list_id, account_ids=account_ids, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_bookmarks_list(params: Optional[Dict[str, Any]] = None, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return bookmarks.list_bookmarks(params=params, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_favourites_list(params: Optional[Dict[str, Any]] = None, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return favourites.list_favourites(params=params, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_media_upload(file_path: str, description: Optional[str] = None, focus: Optional[str] = None, base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return media.upload_media(file_path=file_path, description=description, focus=focus, client=_client(base_url, access_token))


@mcp.tool()
def mastodon_instance_get(base_url: Optional[str] = None, access_token: Optional[str] = None) -> Any:
    return instance.get_instance(client=_client(base_url, access_token))


if __name__ == "__main__":
    mcp.run()
