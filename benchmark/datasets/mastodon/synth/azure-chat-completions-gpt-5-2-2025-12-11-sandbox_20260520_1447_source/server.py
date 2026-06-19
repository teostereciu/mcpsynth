import os
from typing import Any, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.client import MastodonClient
from generated_tools.statuses import (
    statuses_get,
    statuses_create,
    statuses_update,
    statuses_delete,
    statuses_context,
    statuses_reblog,
    statuses_unreblog,
    statuses_favourite,
    statuses_unfavourite,
    statuses_bookmark,
    statuses_unbookmark,
)
from generated_tools.accounts import (
    accounts_verify_credentials,
    accounts_get,
    accounts_follow,
    accounts_unfollow,
    accounts_followers,
    accounts_following,
)
from generated_tools.timelines import (
    timelines_home,
    timelines_public,
    timelines_tag,
    timelines_list,
)
from generated_tools.notifications import (
    notifications_list,
    notifications_get,
    notifications_dismiss,
    notifications_clear,
    notifications_unread_count,
)
from generated_tools.search import search_v2
from generated_tools.lists import (
    lists_list,
    lists_get,
    lists_create,
    lists_update,
    lists_delete,
    lists_accounts_get,
    lists_accounts_add,
    lists_accounts_remove,
)
from generated_tools.bookmarks import bookmarks_list
from generated_tools.favourites import favourites_list
from generated_tools.media import media_upload, media_get, media_update, media_delete
from generated_tools.instance import instance_get_v1, instance_get_v2


mcp = FastMCP("mastodon")


def _client(base_url: Optional[str] = None, access_token: Optional[str] = None) -> MastodonClient:
    return MastodonClient(base_url=base_url, access_token=access_token)


# Statuses
@mcp.tool()
def mastodon_statuses_get(status_id: str, base_url: str | None = None, access_token: str | None = None) -> Any:
    return statuses_get(_client(base_url, access_token), status_id)


@mcp.tool()
def mastodon_statuses_create(
    status: str,
    in_reply_to_id: str | None = None,
    quoted_status_id: str | None = None,
    quote_approval_policy: str | None = None,
    media_ids: list[str] | None = None,
    sensitive: bool | None = None,
    spoiler_text: str | None = None,
    visibility: str | None = None,
    language: str | None = None,
    scheduled_at: str | None = None,
    allowed_mentions: list[str] | None = None,
    poll: dict | None = None,
    base_url: str | None = None,
    access_token: str | None = None,
) -> Any:
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
def mastodon_statuses_update(
    status_id: str,
    status: str | None = None,
    media_ids: list[str] | None = None,
    media_attributes: list[dict] | None = None,
    sensitive: bool | None = None,
    spoiler_text: str | None = None,
    language: str | None = None,
    poll: dict | None = None,
    quote_approval_policy: str | None = None,
    base_url: str | None = None,
    access_token: str | None = None,
) -> Any:
    return statuses_update(
        _client(base_url, access_token),
        status_id,
        status=status,
        media_ids=media_ids,
        media_attributes=media_attributes,
        sensitive=sensitive,
        spoiler_text=spoiler_text,
        language=language,
        poll=poll,
        quote_approval_policy=quote_approval_policy,
    )


@mcp.tool()
def mastodon_statuses_delete(status_id: str, delete_media: bool | None = None, base_url: str | None = None, access_token: str | None = None) -> Any:
    return statuses_delete(_client(base_url, access_token), status_id, delete_media=delete_media)


@mcp.tool()
def mastodon_statuses_context(status_id: str, base_url: str | None = None, access_token: str | None = None) -> Any:
    return statuses_context(_client(base_url, access_token), status_id)


@mcp.tool()
def mastodon_statuses_reblog(status_id: str, visibility: str | None = None, base_url: str | None = None, access_token: str | None = None) -> Any:
    return statuses_reblog(_client(base_url, access_token), status_id, visibility=visibility)


@mcp.tool()
def mastodon_statuses_unreblog(status_id: str, base_url: str | None = None, access_token: str | None = None) -> Any:
    return statuses_unreblog(_client(base_url, access_token), status_id)


@mcp.tool()
def mastodon_statuses_favourite(status_id: str, base_url: str | None = None, access_token: str | None = None) -> Any:
    return statuses_favourite(_client(base_url, access_token), status_id)


@mcp.tool()
def mastodon_statuses_unfavourite(status_id: str, base_url: str | None = None, access_token: str | None = None) -> Any:
    return statuses_unfavourite(_client(base_url, access_token), status_id)


@mcp.tool()
def mastodon_statuses_bookmark(status_id: str, base_url: str | None = None, access_token: str | None = None) -> Any:
    return statuses_bookmark(_client(base_url, access_token), status_id)


@mcp.tool()
def mastodon_statuses_unbookmark(status_id: str, base_url: str | None = None, access_token: str | None = None) -> Any:
    return statuses_unbookmark(_client(base_url, access_token), status_id)


# Accounts
@mcp.tool()
def mastodon_accounts_verify_credentials(base_url: str | None = None, access_token: str | None = None) -> Any:
    return accounts_verify_credentials(_client(base_url, access_token))


@mcp.tool()
def mastodon_accounts_get(account_id: str, base_url: str | None = None, access_token: str | None = None) -> Any:
    return accounts_get(_client(base_url, access_token), account_id)


@mcp.tool()
def mastodon_accounts_follow(
    account_id: str,
    reblogs: bool | None = None,
    notify: bool | None = None,
    languages: list[str] | None = None,
    base_url: str | None = None,
    access_token: str | None = None,
) -> Any:
    return accounts_follow(_client(base_url, access_token), account_id, reblogs=reblogs, notify=notify, languages=languages)


@mcp.tool()
def mastodon_accounts_unfollow(account_id: str, base_url: str | None = None, access_token: str | None = None) -> Any:
    return accounts_unfollow(_client(base_url, access_token), account_id)


@mcp.tool()
def mastodon_accounts_followers(
    account_id: str,
    limit: int | None = None,
    max_id: str | None = None,
    since_id: str | None = None,
    base_url: str | None = None,
    access_token: str | None = None,
) -> Any:
    return accounts_followers(_client(base_url, access_token), account_id, limit=limit, max_id=max_id, since_id=since_id)


@mcp.tool()
def mastodon_accounts_following(
    account_id: str,
    limit: int | None = None,
    max_id: str | None = None,
    since_id: str | None = None,
    base_url: str | None = None,
    access_token: str | None = None,
) -> Any:
    return accounts_following(_client(base_url, access_token), account_id, limit=limit, max_id=max_id, since_id=since_id)


# Timelines
@mcp.tool()
def mastodon_timelines_home(
    limit: int | None = None,
    max_id: str | None = None,
    since_id: str | None = None,
    min_id: str | None = None,
    local: bool | None = None,
    base_url: str | None = None,
    access_token: str | None = None,
) -> Any:
    return timelines_home(_client(base_url, access_token), limit=limit, max_id=max_id, since_id=since_id, min_id=min_id, local=local)


@mcp.tool()
def mastodon_timelines_public(
    local: bool | None = None,
    remote: bool | None = None,
    only_media: bool | None = None,
    limit: int | None = None,
    max_id: str | None = None,
    since_id: str | None = None,
    min_id: str | None = None,
    base_url: str | None = None,
    access_token: str | None = None,
) -> Any:
    return timelines_public(_client(base_url, access_token), local=local, remote=remote, only_media=only_media, limit=limit, max_id=max_id, since_id=since_id, min_id=min_id)


@mcp.tool()
def mastodon_timelines_tag(
    hashtag: str,
    local: bool | None = None,
    only_media: bool | None = None,
    limit: int | None = None,
    max_id: str | None = None,
    since_id: str | None = None,
    min_id: str | None = None,
    base_url: str | None = None,
    access_token: str | None = None,
) -> Any:
    return timelines_tag(_client(base_url, access_token), hashtag, local=local, only_media=only_media, limit=limit, max_id=max_id, since_id=since_id, min_id=min_id)


@mcp.tool()
def mastodon_timelines_list(
    list_id: str,
    limit: int | None = None,
    max_id: str | None = None,
    since_id: str | None = None,
    min_id: str | None = None,
    base_url: str | None = None,
    access_token: str | None = None,
) -> Any:
    return timelines_list(_client(base_url, access_token), list_id, limit=limit, max_id=max_id, since_id=since_id, min_id=min_id)


# Notifications
@mcp.tool()
def mastodon_notifications_list(
    limit: int | None = None,
    max_id: str | None = None,
    since_id: str | None = None,
    min_id: str | None = None,
    account_id: str | None = None,
    types: list[str] | None = None,
    exclude_types: list[str] | None = None,
    include_filtered: bool | None = None,
    base_url: str | None = None,
    access_token: str | None = None,
) -> Any:
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
def mastodon_notifications_get(notification_id: str, base_url: str | None = None, access_token: str | None = None) -> Any:
    return notifications_get(_client(base_url, access_token), notification_id)


@mcp.tool()
def mastodon_notifications_dismiss(notification_id: str, base_url: str | None = None, access_token: str | None = None) -> Any:
    return notifications_dismiss(_client(base_url, access_token), notification_id)


@mcp.tool()
def mastodon_notifications_clear(base_url: str | None = None, access_token: str | None = None) -> Any:
    return notifications_clear(_client(base_url, access_token))


@mcp.tool()
def mastodon_notifications_unread_count(limit: int | None = None, base_url: str | None = None, access_token: str | None = None) -> Any:
    return notifications_unread_count(_client(base_url, access_token), limit=limit)


# Search
@mcp.tool()
def mastodon_search(q: str, type: str | None = None, resolve: bool | None = None, following: bool | None = None, account_id: str | None = None, offset: int | None = None, min_id: str | None = None, max_id: str | None = None, exclude_unreviewed: bool | None = None, base_url: str | None = None, access_token: str | None = None) -> Any:
    return search_v2(
        _client(base_url, access_token),
        q,
        type=type,
        resolve=resolve,
        following=following,
        account_id=account_id,
        offset=offset,
        min_id=min_id,
        max_id=max_id,
        exclude_unreviewed=exclude_unreviewed,
    )


# Lists
@mcp.tool()
def mastodon_lists_list(base_url: str | None = None, access_token: str | None = None) -> Any:
    return lists_list(_client(base_url, access_token))


@mcp.tool()
def mastodon_lists_get(list_id: str, base_url: str | None = None, access_token: str | None = None) -> Any:
    return lists_get(_client(base_url, access_token), list_id)


@mcp.tool()
def mastodon_lists_create(title: str, replies_policy: str | None = None, exclusive: bool | None = None, base_url: str | None = None, access_token: str | None = None) -> Any:
    return lists_create(_client(base_url, access_token), title, replies_policy=replies_policy, exclusive=exclusive)


@mcp.tool()
def mastodon_lists_update(list_id: str, title: str | None = None, replies_policy: str | None = None, exclusive: bool | None = None, base_url: str | None = None, access_token: str | None = None) -> Any:
    return lists_update(_client(base_url, access_token), list_id, title=title, replies_policy=replies_policy, exclusive=exclusive)


@mcp.tool()
def mastodon_lists_delete(list_id: str, base_url: str | None = None, access_token: str | None = None) -> Any:
    return lists_delete(_client(base_url, access_token), list_id)


@mcp.tool()
def mastodon_lists_accounts_get(list_id: str, base_url: str | None = None, access_token: str | None = None) -> Any:
    return lists_accounts_get(_client(base_url, access_token), list_id)


@mcp.tool()
def mastodon_lists_accounts_add(list_id: str, account_ids: list[str], base_url: str | None = None, access_token: str | None = None) -> Any:
    return lists_accounts_add(_client(base_url, access_token), list_id, account_ids)


@mcp.tool()
def mastodon_lists_accounts_remove(list_id: str, account_ids: list[str], base_url: str | None = None, access_token: str | None = None) -> Any:
    return lists_accounts_remove(_client(base_url, access_token), list_id, account_ids)


# Bookmarks & favourites
@mcp.tool()
def mastodon_bookmarks_list(limit: int | None = None, max_id: str | None = None, since_id: str | None = None, min_id: str | None = None, base_url: str | None = None, access_token: str | None = None) -> Any:
    return bookmarks_list(_client(base_url, access_token), limit=limit, max_id=max_id, since_id=since_id, min_id=min_id)


@mcp.tool()
def mastodon_favourites_list(limit: int | None = None, max_id: str | None = None, since_id: str | None = None, min_id: str | None = None, base_url: str | None = None, access_token: str | None = None) -> Any:
    return favourites_list(_client(base_url, access_token), limit=limit, max_id=max_id, since_id=since_id, min_id=min_id)


# Media
@mcp.tool()
def mastodon_media_upload(file_path: str, description: str | None = None, focus: str | None = None, base_url: str | None = None, access_token: str | None = None) -> Any:
    return media_upload(_client(base_url, access_token), file_path, description=description, focus=focus)


@mcp.tool()
def mastodon_media_get(media_id: str, base_url: str | None = None, access_token: str | None = None) -> Any:
    return media_get(_client(base_url, access_token), media_id)


@mcp.tool()
def mastodon_media_update(media_id: str, description: str | None = None, focus: str | None = None, base_url: str | None = None, access_token: str | None = None) -> Any:
    return media_update(_client(base_url, access_token), media_id, description=description, focus=focus)


@mcp.tool()
def mastodon_media_delete(media_id: str, base_url: str | None = None, access_token: str | None = None) -> Any:
    return media_delete(_client(base_url, access_token), media_id)


# Instance
@mcp.tool()
def mastodon_instance_get(base_url: str | None = None, access_token: str | None = None, version: int = 1) -> Any:
    if version == 2:
        return instance_get_v2(_client(base_url, access_token))
    return instance_get_v1(_client(base_url, access_token))


if __name__ == "__main__":
    # FastMCP runs over stdio by default
    mcp.run()
