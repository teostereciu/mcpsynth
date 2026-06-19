import os
from typing import Any, Dict, List, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.client import MastodonClient
from generated_tools import accounts, bookmarks, favourites, instance, lists, media, notifications, search, statuses, timelines


mcp = FastMCP("mastodon")


def _client() -> MastodonClient:
    return MastodonClient(
        base_url=os.getenv("MASTODON_BASE_URL"),
        access_token=os.getenv("MASTODON_ACCESS_TOKEN"),
    )


@mcp.tool()
def statuses_create_status(
    status: str,
    in_reply_to_id: Optional[str] = None,
    media_ids: Optional[List[str]] = None,
    sensitive: Optional[bool] = None,
    spoiler_text: Optional[str] = None,
    visibility: Optional[str] = None,
    language: Optional[str] = None,
    scheduled_at: Optional[str] = None,
    poll: Optional[Dict[str, Any]] = None,
) -> Any:
    return statuses.create_status(_client(), status, in_reply_to_id, media_ids, sensitive, spoiler_text, visibility, language, scheduled_at, poll)


@mcp.tool()
def statuses_get_status(status_id: str) -> Any:
    return statuses.get_status(_client(), status_id)


@mcp.tool()
def statuses_delete_status(status_id: str) -> Any:
    return statuses.delete_status(_client(), status_id)


@mcp.tool()
def statuses_reblog_status(status_id: str) -> Any:
    return statuses.reblog_status(_client(), status_id)


@mcp.tool()
def statuses_unreblog_status(status_id: str) -> Any:
    return statuses.unreblog_status(_client(), status_id)


@mcp.tool()
def statuses_favourite_status(status_id: str) -> Any:
    return statuses.favourite_status(_client(), status_id)


@mcp.tool()
def statuses_unfavourite_status(status_id: str) -> Any:
    return statuses.unfavourite_status(_client(), status_id)


@mcp.tool()
def statuses_get_status_context(status_id: str) -> Any:
    return statuses.get_status_context(_client(), status_id)


@mcp.tool()
def accounts_verify_credentials() -> Any:
    return accounts.verify_credentials(_client())


@mcp.tool()
def accounts_get_account(account_id: str) -> Any:
    return accounts.get_account(_client(), account_id)


@mcp.tool()
def accounts_follow_account(account_id: str, reblogs: Optional[bool] = None, notify: Optional[bool] = None, languages: Optional[list] = None) -> Any:
    return accounts.follow_account(_client(), account_id, reblogs=reblogs, notify=notify, languages=languages)


@mcp.tool()
def accounts_unfollow_account(account_id: str) -> Any:
    return accounts.unfollow_account(_client(), account_id)


@mcp.tool()
def accounts_get_followers(account_id: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None) -> Any:
    return accounts.get_followers(_client(), account_id, limit=limit, max_id=max_id, since_id=since_id)


@mcp.tool()
def accounts_get_following(account_id: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None) -> Any:
    return accounts.get_following(_client(), account_id, limit=limit, max_id=max_id, since_id=since_id)


@mcp.tool()
def timelines_get_home_timeline(limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    return timelines.get_home_timeline(_client(), limit=limit, max_id=max_id, since_id=since_id, min_id=min_id)


@mcp.tool()
def timelines_get_public_timeline(local: Optional[bool] = None, remote: Optional[bool] = None, only_media: Optional[bool] = None, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    return timelines.get_public_timeline(_client(), local=local, remote=remote, only_media=only_media, limit=limit, max_id=max_id, since_id=since_id, min_id=min_id)


@mcp.tool()
def timelines_get_hashtag_timeline(hashtag: str, local: Optional[bool] = None, only_media: Optional[bool] = None, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    return timelines.get_hashtag_timeline(_client(), hashtag=hashtag, local=local, only_media=only_media, limit=limit, max_id=max_id, since_id=since_id, min_id=min_id)


@mcp.tool()
def timelines_get_list_timeline(list_id: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    return timelines.get_list_timeline(_client(), list_id=list_id, limit=limit, max_id=max_id, since_id=since_id, min_id=min_id)


@mcp.tool()
def notifications_list_notifications(limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, types: Optional[list] = None, exclude_types: Optional[list] = None) -> Any:
    return notifications.list_notifications(_client(), limit=limit, max_id=max_id, since_id=since_id, min_id=min_id, types=types, exclude_types=exclude_types)


@mcp.tool()
def notifications_get_notification(notification_id: str) -> Any:
    return notifications.get_notification(_client(), notification_id)


@mcp.tool()
def notifications_dismiss_notification(notification_id: str) -> Any:
    return notifications.dismiss_notification(_client(), notification_id)


@mcp.tool()
def notifications_clear_notifications() -> Any:
    return notifications.clear_notifications(_client())


@mcp.tool()
def search_search(q: str, resolve: Optional[bool] = None, limit: Optional[int] = None, offset: Optional[int] = None, following: Optional[bool] = None, type: Optional[str] = None) -> Any:
    return search.search(_client(), q=q, resolve=resolve, limit=limit, offset=offset, following=following, type=type)


@mcp.tool()
def lists_list_lists() -> Any:
    return lists.list_lists(_client())


@mcp.tool()
def lists_get_list(list_id: str) -> Any:
    return lists.get_list(_client(), list_id)


@mcp.tool()
def lists_create_list(title: str, replies_policy: Optional[str] = None) -> Any:
    return lists.create_list(_client(), title=title, replies_policy=replies_policy)


@mcp.tool()
def lists_update_list(list_id: str, title: Optional[str] = None, replies_policy: Optional[str] = None) -> Any:
    return lists.update_list(_client(), list_id=list_id, title=title, replies_policy=replies_policy)


@mcp.tool()
def lists_delete_list(list_id: str) -> Any:
    return lists.delete_list(_client(), list_id)


@mcp.tool()
def lists_add_accounts_to_list(list_id: str, account_ids: list) -> Any:
    return lists.add_accounts_to_list(_client(), list_id=list_id, account_ids=account_ids)


@mcp.tool()
def lists_remove_accounts_from_list(list_id: str, account_ids: list) -> Any:
    return lists.remove_accounts_from_list(_client(), list_id=list_id, account_ids=account_ids)


@mcp.tool()
def lists_get_list_accounts(list_id: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None) -> Any:
    return lists.get_list_accounts(_client(), list_id=list_id, limit=limit, max_id=max_id, since_id=since_id)


@mcp.tool()
def bookmarks_list_bookmarks(limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    return bookmarks.list_bookmarks(_client(), limit=limit, max_id=max_id, since_id=since_id, min_id=min_id)


@mcp.tool()
def bookmarks_bookmark_status(status_id: str) -> Any:
    return bookmarks.bookmark_status(_client(), status_id)


@mcp.tool()
def bookmarks_unbookmark_status(status_id: str) -> Any:
    return bookmarks.unbookmark_status(_client(), status_id)


@mcp.tool()
def favourites_list_favourites(limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Any:
    return favourites.list_favourites(_client(), limit=limit, max_id=max_id, since_id=since_id, min_id=min_id)


@mcp.tool()
def media_upload_media(file_path: str, description: Optional[str] = None, focus: Optional[str] = None) -> Any:
    return media.upload_media(_client(), file_path=file_path, description=description, focus=focus)


@mcp.tool()
def instance_get_instance_info() -> Any:
    return instance.get_instance_info(_client())


def main():
    mcp.run()


if __name__ == "__main__":
    main()
