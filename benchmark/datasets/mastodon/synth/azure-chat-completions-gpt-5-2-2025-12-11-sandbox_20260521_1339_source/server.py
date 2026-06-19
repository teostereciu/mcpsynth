import os
from typing import Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.client import MastodonClient
from generated_tools.statuses import (
    statuses_context,
    statuses_create,
    statuses_delete,
    statuses_favourite,
    statuses_get,
    statuses_reblog,
    statuses_unfavourite,
    statuses_unreblog,
)
from generated_tools.accounts import (
    accounts_follow,
    accounts_followers,
    accounts_following,
    accounts_get,
    accounts_unfollow,
    accounts_verify_credentials,
)
from generated_tools.timelines import timelines_home, timelines_list, timelines_public, timelines_tag
from generated_tools.notifications import (
    notifications_clear,
    notifications_dismiss,
    notifications_get,
    notifications_list,
    notifications_unread_count,
)
from generated_tools.search import search_v2
from generated_tools.lists import (
    lists_accounts_add,
    lists_accounts_list,
    lists_accounts_remove,
    lists_create,
    lists_delete,
    lists_get,
    lists_list,
    lists_update,
)
from generated_tools.bookmarks import bookmarks_list, statuses_bookmark, statuses_unbookmark
from generated_tools.favourites import favourites_list
from generated_tools.media import media_get, media_upload
from generated_tools.instance import instance_v1, instance_v2

mcp = FastMCP("mastodon")


def _client(base_url: Optional[str] = None, access_token: Optional[str] = None) -> MastodonClient:
    return MastodonClient(base_url=base_url, access_token=access_token)


@mcp.tool()
def mastodon_status_get(status_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return statuses_get(_client(base_url, access_token), status_id)


@mcp.tool()
def mastodon_status_context(status_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return statuses_context(_client(base_url, access_token), status_id)


@mcp.tool()
def mastodon_status_create(
    status: str,
    in_reply_to_id: Optional[str] = None,
    quoted_status_id: Optional[str] = None,
    quote_approval_policy: Optional[str] = None,
    media_ids: Optional[list[str]] = None,
    sensitive: Optional[bool] = None,
    spoiler_text: Optional[str] = None,
    visibility: Optional[str] = None,
    language: Optional[str] = None,
    scheduled_at: Optional[str] = None,
    allowed_mentions: Optional[list[str]] = None,
    poll: Optional[dict] = None,
    base_url: Optional[str] = None,
    access_token: Optional[str] = None,
):
    return statuses_create(
        _client(base_url, access_token),
        status,
        in_reply_to_id=in_reply_to_id,
        quoted_status_id=quoted_status_id,
        quote_approval_policy=quote_approval_policy,
        media_ids=media_ids,
        sensitive=sensitive,
        spoiler_text=spoiler_text,
        visibility=visibility,
        language=language,
        scheduled_at=scheduled_at,
        allowed_mentions=allowed_mentions,
        poll=poll,
    )


@mcp.tool()
def mastodon_status_delete(status_id: str, delete_media: Optional[bool] = None, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return statuses_delete(_client(base_url, access_token), status_id, delete_media=delete_media)


@mcp.tool()
def mastodon_status_reblog(status_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return statuses_reblog(_client(base_url, access_token), status_id)


@mcp.tool()
def mastodon_status_unreblog(status_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return statuses_unreblog(_client(base_url, access_token), status_id)


@mcp.tool()
def mastodon_status_favourite(status_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return statuses_favourite(_client(base_url, access_token), status_id)


@mcp.tool()
def mastodon_status_unfavourite(status_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return statuses_unfavourite(_client(base_url, access_token), status_id)


@mcp.tool()
def mastodon_status_bookmark(status_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return statuses_bookmark(_client(base_url, access_token), status_id)


@mcp.tool()
def mastodon_status_unbookmark(status_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return statuses_unbookmark(_client(base_url, access_token), status_id)


@mcp.tool()
def mastodon_account_verify_credentials(base_url: Optional[str] = None, access_token: Optional[str] = None):
    return accounts_verify_credentials(_client(base_url, access_token))


@mcp.tool()
def mastodon_account_get(account_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return accounts_get(_client(base_url, access_token), account_id)


@mcp.tool()
def mastodon_account_follow(account_id: str, reblogs: Optional[bool] = None, notify: Optional[bool] = None, languages=None, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return accounts_follow(_client(base_url, access_token), account_id, reblogs=reblogs, notify=notify, languages=languages)


@mcp.tool()
def mastodon_account_unfollow(account_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return accounts_unfollow(_client(base_url, access_token), account_id)


@mcp.tool()
def mastodon_account_followers(account_id: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return accounts_followers(_client(base_url, access_token), account_id, limit=limit, max_id=max_id, since_id=since_id)


@mcp.tool()
def mastodon_account_following(account_id: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return accounts_following(_client(base_url, access_token), account_id, limit=limit, max_id=max_id, since_id=since_id)


@mcp.tool()
def mastodon_timeline_home(limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, local: Optional[bool] = None, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return timelines_home(_client(base_url, access_token), limit=limit, max_id=max_id, since_id=since_id, min_id=min_id, local=local)


@mcp.tool()
def mastodon_timeline_public(limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, local: Optional[bool] = None, remote: Optional[bool] = None, only_media: Optional[bool] = None, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return timelines_public(_client(base_url, access_token), limit=limit, max_id=max_id, since_id=since_id, min_id=min_id, local=local, remote=remote, only_media=only_media)


@mcp.tool()
def mastodon_timeline_hashtag(hashtag: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, local: Optional[bool] = None, only_media: Optional[bool] = None, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return timelines_tag(_client(base_url, access_token), hashtag, limit=limit, max_id=max_id, since_id=since_id, min_id=min_id, local=local, only_media=only_media)


@mcp.tool()
def mastodon_timeline_list(list_id: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return timelines_list(_client(base_url, access_token), list_id, limit=limit, max_id=max_id, since_id=since_id, min_id=min_id)


@mcp.tool()
def mastodon_notifications_list(
    limit: Optional[int] = None,
    max_id: Optional[str] = None,
    since_id: Optional[str] = None,
    min_id: Optional[str] = None,
    account_id: Optional[str] = None,
    types: Optional[list[str]] = None,
    exclude_types: Optional[list[str]] = None,
    include_filtered: Optional[bool] = None,
    base_url: Optional[str] = None,
    access_token: Optional[str] = None,
):
    return notifications_list(
        _client(base_url, access_token),
        limit=limit,
        max_id=max_id,
        since_id=since_id,
        min_id=min_id,
        account_id=account_id,
        types=types,
        exclude_types=exclude_types,
        include_filtered=include_filtered,
    )


@mcp.tool()
def mastodon_notification_get(notification_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return notifications_get(_client(base_url, access_token), notification_id)


@mcp.tool()
def mastodon_notification_dismiss(notification_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return notifications_dismiss(_client(base_url, access_token), notification_id)


@mcp.tool()
def mastodon_notifications_clear(base_url: Optional[str] = None, access_token: Optional[str] = None):
    return notifications_clear(_client(base_url, access_token))


@mcp.tool()
def mastodon_notifications_unread_count(limit: Optional[int] = None, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return notifications_unread_count(_client(base_url, access_token), limit=limit)


@mcp.tool()
def mastodon_search(q: str, type: Optional[str] = None, offset: Optional[int] = None, min_id: Optional[str] = None, max_id: Optional[str] = None, account_id: Optional[str] = None, resolve: Optional[bool] = None, exclude_unreviewed: Optional[bool] = None, following: Optional[bool] = None, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return search_v2(
        _client(base_url, access_token),
        q,
        type=type,
        offset=offset,
        min_id=min_id,
        max_id=max_id,
        account_id=account_id,
        resolve=resolve,
        exclude_unreviewed=exclude_unreviewed,
        following=following,
    )


@mcp.tool()
def mastodon_lists_list(base_url: Optional[str] = None, access_token: Optional[str] = None):
    return lists_list(_client(base_url, access_token))


@mcp.tool()
def mastodon_list_get(list_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return lists_get(_client(base_url, access_token), list_id)


@mcp.tool()
def mastodon_list_create(title: str, replies_policy: Optional[str] = None, exclusive: Optional[bool] = None, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return lists_create(_client(base_url, access_token), title, replies_policy=replies_policy, exclusive=exclusive)


@mcp.tool()
def mastodon_list_update(list_id: str, title: Optional[str] = None, replies_policy: Optional[str] = None, exclusive: Optional[bool] = None, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return lists_update(_client(base_url, access_token), list_id, title=title, replies_policy=replies_policy, exclusive=exclusive)


@mcp.tool()
def mastodon_list_delete(list_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return lists_delete(_client(base_url, access_token), list_id)


@mcp.tool()
def mastodon_list_accounts_list(list_id: str, limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return lists_accounts_list(_client(base_url, access_token), list_id, limit=limit, max_id=max_id, since_id=since_id)


@mcp.tool()
def mastodon_list_accounts_add(list_id: str, account_ids: list[str], base_url: Optional[str] = None, access_token: Optional[str] = None):
    return lists_accounts_add(_client(base_url, access_token), list_id, account_ids)


@mcp.tool()
def mastodon_list_accounts_remove(list_id: str, account_ids: list[str], base_url: Optional[str] = None, access_token: Optional[str] = None):
    return lists_accounts_remove(_client(base_url, access_token), list_id, account_ids)


@mcp.tool()
def mastodon_bookmarks_list(limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return bookmarks_list(_client(base_url, access_token), limit=limit, max_id=max_id, since_id=since_id, min_id=min_id)


@mcp.tool()
def mastodon_favourites_list(limit: Optional[int] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return favourites_list(_client(base_url, access_token), limit=limit, max_id=max_id, since_id=since_id, min_id=min_id)


@mcp.tool()
def mastodon_media_upload(file_path: str, description: Optional[str] = None, focus: Optional[str] = None, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return media_upload(_client(base_url, access_token), file_path, description=description, focus=focus)


@mcp.tool()
def mastodon_media_get(media_id: str, base_url: Optional[str] = None, access_token: Optional[str] = None):
    return media_get(_client(base_url, access_token), media_id)


@mcp.tool()
def mastodon_instance_info_v1(base_url: Optional[str] = None, access_token: Optional[str] = None):
    return instance_v1(_client(base_url, access_token))


@mcp.tool()
def mastodon_instance_info_v2(base_url: Optional[str] = None, access_token: Optional[str] = None):
    return instance_v2(_client(base_url, access_token))


if __name__ == "__main__":
    # Allow running without env vars if passed per-tool.
    os.environ.setdefault("MASTODON_BASE_URL", os.getenv("MASTODON_BASE_URL", ""))
    mcp.run()
