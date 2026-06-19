#!/usr/bin/env python3

import json
import os
from dataclasses import dataclass
from typing import Any, Dict, Optional, Sequence, Tuple

import click
import requests


API_V1_PREFIX = "/api/v1"
API_V2_PREFIX = "/api/v2"


class MastodonCliError(click.ClickException):
    pass


@dataclass
class ClientConfig:
    base_url: str
    access_token: str
    timeout_s: int = 30


class MastodonClient:
    def __init__(self, cfg: ClientConfig):
        self.cfg = cfg
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {cfg.access_token}",
                "User-Agent": "mastodon-cli/1.0",
            }
        )

    def _url(self, path: str) -> str:
        return self.cfg.base_url.rstrip("/") + path

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        files: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        url = self._url(path)
        resp = self.session.request(
            method,
            url,
            params=params,
            data=data,
            json=json_body,
            files=files,
            headers=headers,
            timeout=self.cfg.timeout_s,
        )
        if resp.status_code >= 400:
            try:
                payload = resp.json()
            except Exception:
                payload = resp.text
            raise MastodonCliError(f"HTTP {resp.status_code} {method} {path}: {payload}")

        if resp.status_code == 204:
            return None
        ctype = resp.headers.get("Content-Type", "")
        if "application/json" in ctype:
            return resp.json()
        return resp.text


def _client_from_env(timeout: int) -> MastodonClient:
    base_url = os.environ.get("MASTODON_BASE_URL")
    token = os.environ.get("MASTODON_ACCESS_TOKEN")
    if not base_url:
        raise MastodonCliError("MASTODON_BASE_URL is not set")
    if not token:
        raise MastodonCliError("MASTODON_ACCESS_TOKEN is not set")
    return MastodonClient(ClientConfig(base_url=base_url, access_token=token, timeout_s=timeout))


def _echo(obj: Any, raw: bool):
    if raw and isinstance(obj, str):
        click.echo(obj)
    else:
        click.echo(json.dumps(obj, indent=2, ensure_ascii=False))


@click.group()
@click.option("--timeout", type=int, default=30, show_default=True)
@click.pass_context
def cli(ctx: click.Context, timeout: int):
    """Mastodon CLI (opinionated, no generic passthrough commands)."""
    ctx.obj = {"client": _client_from_env(timeout)}


@cli.group()
def statuses():
    """Statuses: create, show, delete, boost, favourite, bookmark, context."""


@statuses.command("create")
@click.option("--text", "text", required=True, help="Status text")
@click.option("--in-reply-to-id", type=str)
@click.option("--quoted-status-id", type=str)
@click.option("--visibility", type=click.Choice(["public", "unlisted", "private", "direct"], case_sensitive=False))
@click.option("--sensitive", is_flag=True, default=False)
@click.option("--spoiler-text", type=str)
@click.option("--language", type=str)
@click.option("--scheduled-at", type=str, help="ISO8601 timestamp")
@click.option("--media-id", "media_ids", multiple=True)
@click.option("--allowed-mention", "allowed_mentions", multiple=True)
@click.option("--poll-option", "poll_options", multiple=True)
@click.option("--poll-expires-in", type=int)
@click.option("--poll-multiple", is_flag=True, default=False)
@click.option("--poll-hide-totals", is_flag=True, default=False)
@click.option("--idempotency-key", type=str)
@click.pass_context
def statuses_create(
    ctx: click.Context,
    text: str,
    in_reply_to_id: Optional[str],
    quoted_status_id: Optional[str],
    visibility: Optional[str],
    sensitive: bool,
    spoiler_text: Optional[str],
    language: Optional[str],
    scheduled_at: Optional[str],
    media_ids: Sequence[str],
    allowed_mentions: Sequence[str],
    poll_options: Sequence[str],
    poll_expires_in: Optional[int],
    poll_multiple: bool,
    poll_hide_totals: bool,
    idempotency_key: Optional[str],
):
    client: MastodonClient = ctx.obj["client"]
    payload: Dict[str, Any] = {
        "status": text,
        "sensitive": sensitive,
    }
    if in_reply_to_id:
        payload["in_reply_to_id"] = in_reply_to_id
    if quoted_status_id:
        payload["quoted_status_id"] = quoted_status_id
    if visibility:
        payload["visibility"] = visibility
    if spoiler_text is not None:
        payload["spoiler_text"] = spoiler_text
    if language:
        payload["language"] = language
    if scheduled_at:
        payload["scheduled_at"] = scheduled_at
    if media_ids:
        payload["media_ids"] = list(media_ids)
    if allowed_mentions:
        payload["allowed_mentions"] = list(allowed_mentions)
    if poll_options or poll_expires_in is not None:
        poll: Dict[str, Any] = {
            "options": list(poll_options),
            "multiple": poll_multiple,
            "hide_totals": poll_hide_totals,
        }
        if poll_expires_in is not None:
            poll["expires_in"] = poll_expires_in
        payload["poll"] = poll

    headers = {}
    if idempotency_key:
        headers["Idempotency-Key"] = idempotency_key

    res = client.request("POST", f"{API_V1_PREFIX}/statuses", data=payload, headers=headers or None)
    _echo(res, raw=False)


@statuses.command("show")
@click.argument("status_id")
@click.pass_context
def statuses_show(ctx: click.Context, status_id: str):
    client: MastodonClient = ctx.obj["client"]
    res = client.request("GET", f"{API_V1_PREFIX}/statuses/{status_id}")
    _echo(res, raw=False)


@statuses.command("delete")
@click.argument("status_id")
@click.option("--delete-media", is_flag=True, default=False, help="If set, delete media too")
@click.pass_context
def statuses_delete(ctx: click.Context, status_id: str, delete_media: bool):
    client: MastodonClient = ctx.obj["client"]
    res = client.request(
        "DELETE",
        f"{API_V1_PREFIX}/statuses/{status_id}",
        params={"delete_media": "true"} if delete_media else None,
    )
    _echo(res, raw=False)


@statuses.command("context")
@click.argument("status_id")
@click.pass_context
def statuses_context(ctx: click.Context, status_id: str):
    client: MastodonClient = ctx.obj["client"]
    res = client.request("GET", f"{API_V1_PREFIX}/statuses/{status_id}/context")
    _echo(res, raw=False)


@statuses.command("boost")
@click.argument("status_id")
@click.pass_context
def statuses_boost(ctx: click.Context, status_id: str):
    client: MastodonClient = ctx.obj["client"]
    res = client.request("POST", f"{API_V1_PREFIX}/statuses/{status_id}/reblog")
    _echo(res, raw=False)


@statuses.command("unboost")
@click.argument("status_id")
@click.pass_context
def statuses_unboost(ctx: click.Context, status_id: str):
    client: MastodonClient = ctx.obj["client"]
    res = client.request("POST", f"{API_V1_PREFIX}/statuses/{status_id}/unreblog")
    _echo(res, raw=False)


@statuses.command("favourite")
@click.argument("status_id")
@click.pass_context
def statuses_favourite(ctx: click.Context, status_id: str):
    client: MastodonClient = ctx.obj["client"]
    res = client.request("POST", f"{API_V1_PREFIX}/statuses/{status_id}/favourite")
    _echo(res, raw=False)


@statuses.command("unfavourite")
@click.argument("status_id")
@click.pass_context
def statuses_unfavourite(ctx: click.Context, status_id: str):
    client: MastodonClient = ctx.obj["client"]
    res = client.request("POST", f"{API_V1_PREFIX}/statuses/{status_id}/unfavourite")
    _echo(res, raw=False)


@statuses.command("bookmark")
@click.argument("status_id")
@click.pass_context
def statuses_bookmark(ctx: click.Context, status_id: str):
    client: MastodonClient = ctx.obj["client"]
    res = client.request("POST", f"{API_V1_PREFIX}/statuses/{status_id}/bookmark")
    _echo(res, raw=False)


@statuses.command("unbookmark")
@click.argument("status_id")
@click.pass_context
def statuses_unbookmark(ctx: click.Context, status_id: str):
    client: MastodonClient = ctx.obj["client"]
    res = client.request("POST", f"{API_V1_PREFIX}/statuses/{status_id}/unbookmark")
    _echo(res, raw=False)


@cli.group()
def accounts():
    """Accounts: verify credentials, show, follow/unfollow, followers/following."""


@accounts.command("me")
@click.pass_context
def accounts_me(ctx: click.Context):
    client: MastodonClient = ctx.obj["client"]
    res = client.request("GET", f"{API_V1_PREFIX}/accounts/verify_credentials")
    _echo(res, raw=False)


@accounts.command("show")
@click.argument("account_id")
@click.pass_context
def accounts_show(ctx: click.Context, account_id: str):
    client: MastodonClient = ctx.obj["client"]
    res = client.request("GET", f"{API_V1_PREFIX}/accounts/{account_id}")
    _echo(res, raw=False)


@accounts.command("follow")
@click.argument("account_id")
@click.option("--reblogs/--no-reblogs", default=True, show_default=True)
@click.option("--notify/--no-notify", default=False, show_default=True)
@click.option("--languages", multiple=True, help="Limit to these languages")
@click.pass_context
def accounts_follow(ctx: click.Context, account_id: str, reblogs: bool, notify: bool, languages: Sequence[str]):
    client: MastodonClient = ctx.obj["client"]
    data: Dict[str, Any] = {"reblogs": str(reblogs).lower(), "notify": str(notify).lower()}
    if languages:
        data["languages"] = list(languages)
    res = client.request("POST", f"{API_V1_PREFIX}/accounts/{account_id}/follow", data=data)
    _echo(res, raw=False)


@accounts.command("unfollow")
@click.argument("account_id")
@click.pass_context
def accounts_unfollow(ctx: click.Context, account_id: str):
    client: MastodonClient = ctx.obj["client"]
    res = client.request("POST", f"{API_V1_PREFIX}/accounts/{account_id}/unfollow")
    _echo(res, raw=False)


@accounts.command("followers")
@click.argument("account_id")
@click.option("--limit", type=int)
@click.option("--max-id", type=str)
@click.option("--since-id", type=str)
@click.pass_context
def accounts_followers(ctx: click.Context, account_id: str, limit: Optional[int], max_id: Optional[str], since_id: Optional[str]):
    client: MastodonClient = ctx.obj["client"]
    params = {k: v for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id}.items() if v is not None}
    res = client.request("GET", f"{API_V1_PREFIX}/accounts/{account_id}/followers", params=params or None)
    _echo(res, raw=False)


@accounts.command("following")
@click.argument("account_id")
@click.option("--limit", type=int)
@click.option("--max-id", type=str)
@click.option("--since-id", type=str)
@click.pass_context
def accounts_following(ctx: click.Context, account_id: str, limit: Optional[int], max_id: Optional[str], since_id: Optional[str]):
    client: MastodonClient = ctx.obj["client"]
    params = {k: v for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id}.items() if v is not None}
    res = client.request("GET", f"{API_V1_PREFIX}/accounts/{account_id}/following", params=params or None)
    _echo(res, raw=False)


@cli.group()
def timelines():
    """Timelines: home, public, hashtag, list."""


@timelines.command("home")
@click.option("--limit", type=int)
@click.option("--max-id", type=str)
@click.option("--since-id", type=str)
@click.option("--min-id", type=str)
@click.pass_context
def timelines_home(ctx: click.Context, limit: Optional[int], max_id: Optional[str], since_id: Optional[str], min_id: Optional[str]):
    client: MastodonClient = ctx.obj["client"]
    params = {k: v for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}.items() if v is not None}
    res = client.request("GET", f"{API_V1_PREFIX}/timelines/home", params=params or None)
    _echo(res, raw=False)


@timelines.command("public")
@click.option("--local", is_flag=True, default=False)
@click.option("--remote", is_flag=True, default=False)
@click.option("--only-media", is_flag=True, default=False)
@click.option("--limit", type=int)
@click.option("--max-id", type=str)
@click.option("--since-id", type=str)
@click.option("--min-id", type=str)
@click.pass_context
def timelines_public(
    ctx: click.Context,
    local: bool,
    remote: bool,
    only_media: bool,
    limit: Optional[int],
    max_id: Optional[str],
    since_id: Optional[str],
    min_id: Optional[str],
):
    client: MastodonClient = ctx.obj["client"]
    params: Dict[str, Any] = {k: v for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}.items() if v is not None}
    if local:
        params["local"] = "true"
    if remote:
        params["remote"] = "true"
    if only_media:
        params["only_media"] = "true"
    res = client.request("GET", f"{API_V1_PREFIX}/timelines/public", params=params or None)
    _echo(res, raw=False)


@timelines.command("hashtag")
@click.argument("tag")
@click.option("--local", is_flag=True, default=False)
@click.option("--only-media", is_flag=True, default=False)
@click.option("--limit", type=int)
@click.option("--max-id", type=str)
@click.option("--since-id", type=str)
@click.option("--min-id", type=str)
@click.pass_context
def timelines_hashtag(
    ctx: click.Context,
    tag: str,
    local: bool,
    only_media: bool,
    limit: Optional[int],
    max_id: Optional[str],
    since_id: Optional[str],
    min_id: Optional[str],
):
    client: MastodonClient = ctx.obj["client"]
    params: Dict[str, Any] = {k: v for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}.items() if v is not None}
    if local:
        params["local"] = "true"
    if only_media:
        params["only_media"] = "true"
    res = client.request("GET", f"{API_V1_PREFIX}/timelines/tag/{tag}", params=params or None)
    _echo(res, raw=False)


@timelines.command("list")
@click.argument("list_id")
@click.option("--limit", type=int)
@click.option("--max-id", type=str)
@click.option("--since-id", type=str)
@click.option("--min-id", type=str)
@click.pass_context
def timelines_list(ctx: click.Context, list_id: str, limit: Optional[int], max_id: Optional[str], since_id: Optional[str], min_id: Optional[str]):
    client: MastodonClient = ctx.obj["client"]
    params = {k: v for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}.items() if v is not None}
    res = client.request("GET", f"{API_V1_PREFIX}/timelines/list/{list_id}", params=params or None)
    _echo(res, raw=False)


@cli.group()
def notifications():
    """Notifications: list, show, dismiss, clear."""


@notifications.command("list")
@click.option("--limit", type=int)
@click.option("--max-id", type=str)
@click.option("--since-id", type=str)
@click.option("--min-id", type=str)
@click.option("--types", multiple=True, help="Filter by types")
@click.option("--exclude-types", multiple=True, help="Exclude types")
@click.pass_context
def notifications_list(
    ctx: click.Context,
    limit: Optional[int],
    max_id: Optional[str],
    since_id: Optional[str],
    min_id: Optional[str],
    types: Sequence[str],
    exclude_types: Sequence[str],
):
    client: MastodonClient = ctx.obj["client"]
    params: Dict[str, Any] = {k: v for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}.items() if v is not None}
    if types:
        params["types[]"] = list(types)
    if exclude_types:
        params["exclude_types[]"] = list(exclude_types)
    res = client.request("GET", f"{API_V1_PREFIX}/notifications", params=params or None)
    _echo(res, raw=False)


@notifications.command("show")
@click.argument("notification_id")
@click.pass_context
def notifications_show(ctx: click.Context, notification_id: str):
    client: MastodonClient = ctx.obj["client"]
    res = client.request("GET", f"{API_V1_PREFIX}/notifications/{notification_id}")
    _echo(res, raw=False)


@notifications.command("dismiss")
@click.argument("notification_id")
@click.pass_context
def notifications_dismiss(ctx: click.Context, notification_id: str):
    client: MastodonClient = ctx.obj["client"]
    res = client.request("POST", f"{API_V1_PREFIX}/notifications/{notification_id}/dismiss")
    _echo(res, raw=False)


@notifications.command("clear")
@click.pass_context
def notifications_clear(ctx: click.Context):
    client: MastodonClient = ctx.obj["client"]
    res = client.request("POST", f"{API_V1_PREFIX}/notifications/clear")
    _echo(res, raw=False)


@cli.group()
def search():
    """Search (v2): accounts, statuses, hashtags."""


@search.command("query")
@click.argument("q")
@click.option("--type", "qtype", type=click.Choice(["accounts", "hashtags", "statuses"], case_sensitive=False))
@click.option("--resolve", is_flag=True, default=False)
@click.option("--limit", type=int)
@click.option("--offset", type=int)
@click.option("--following", is_flag=True, default=False)
@click.pass_context
def search_query(
    ctx: click.Context,
    q: str,
    qtype: Optional[str],
    resolve: bool,
    limit: Optional[int],
    offset: Optional[int],
    following: bool,
):
    client: MastodonClient = ctx.obj["client"]
    params: Dict[str, Any] = {"q": q}
    if qtype:
        params["type"] = qtype
    if resolve:
        params["resolve"] = "true"
    if following:
        params["following"] = "true"
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    res = client.request("GET", f"{API_V2_PREFIX}/search", params=params)
    _echo(res, raw=False)


@cli.group()
def lists():
    """Lists: CRUD and manage accounts."""


@lists.command("list")
@click.pass_context
def lists_list(ctx: click.Context):
    client: MastodonClient = ctx.obj["client"]
    res = client.request("GET", f"{API_V1_PREFIX}/lists")
    _echo(res, raw=False)


@lists.command("create")
@click.option("--title", required=True)
@click.option("--replies-policy", type=click.Choice(["followed", "list", "none"], case_sensitive=False))
@click.pass_context
def lists_create(ctx: click.Context, title: str, replies_policy: Optional[str]):
    client: MastodonClient = ctx.obj["client"]
    data: Dict[str, Any] = {"title": title}
    if replies_policy:
        data["replies_policy"] = replies_policy
    res = client.request("POST", f"{API_V1_PREFIX}/lists", data=data)
    _echo(res, raw=False)


@lists.command("show")
@click.argument("list_id")
@click.pass_context
def lists_show(ctx: click.Context, list_id: str):
    client: MastodonClient = ctx.obj["client"]
    res = client.request("GET", f"{API_V1_PREFIX}/lists/{list_id}")
    _echo(res, raw=False)


@lists.command("update")
@click.argument("list_id")
@click.option("--title", required=True)
@click.option("--replies-policy", type=click.Choice(["followed", "list", "none"], case_sensitive=False))
@click.pass_context
def lists_update(ctx: click.Context, list_id: str, title: str, replies_policy: Optional[str]):
    client: MastodonClient = ctx.obj["client"]
    data: Dict[str, Any] = {"title": title}
    if replies_policy:
        data["replies_policy"] = replies_policy
    res = client.request("PUT", f"{API_V1_PREFIX}/lists/{list_id}", data=data)
    _echo(res, raw=False)


@lists.command("delete")
@click.argument("list_id")
@click.pass_context
def lists_delete(ctx: click.Context, list_id: str):
    client: MastodonClient = ctx.obj["client"]
    res = client.request("DELETE", f"{API_V1_PREFIX}/lists/{list_id}")
    _echo(res, raw=False)


@lists.command("accounts")
@click.argument("list_id")
@click.pass_context
def lists_accounts(ctx: click.Context, list_id: str):
    client: MastodonClient = ctx.obj["client"]
    res = client.request("GET", f"{API_V1_PREFIX}/lists/{list_id}/accounts")
    _echo(res, raw=False)


@lists.command("add-account")
@click.argument("list_id")
@click.argument("account_id")
@click.pass_context
def lists_add_account(ctx: click.Context, list_id: str, account_id: str):
    client: MastodonClient = ctx.obj["client"]
    res = client.request("POST", f"{API_V1_PREFIX}/lists/{list_id}/accounts", data={"account_ids[]": [account_id]})
    _echo(res, raw=False)


@lists.command("remove-account")
@click.argument("list_id")
@click.argument("account_id")
@click.pass_context
def lists_remove_account(ctx: click.Context, list_id: str, account_id: str):
    client: MastodonClient = ctx.obj["client"]
    res = client.request("DELETE", f"{API_V1_PREFIX}/lists/{list_id}/accounts", data={"account_ids[]": [account_id]})
    _echo(res, raw=False)


@cli.group()
def bookmarks():
    """Bookmarks: list."""


@bookmarks.command("list")
@click.option("--limit", type=int)
@click.option("--max-id", type=str)
@click.option("--since-id", type=str)
@click.option("--min-id", type=str)
@click.pass_context
def bookmarks_list(ctx: click.Context, limit: Optional[int], max_id: Optional[str], since_id: Optional[str], min_id: Optional[str]):
    client: MastodonClient = ctx.obj["client"]
    params = {k: v for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}.items() if v is not None}
    res = client.request("GET", f"{API_V1_PREFIX}/bookmarks", params=params or None)
    _echo(res, raw=False)


@cli.group()
def favourites():
    """Favourites: list."""


@favourites.command("list")
@click.option("--limit", type=int)
@click.option("--max-id", type=str)
@click.option("--since-id", type=str)
@click.option("--min-id", type=str)
@click.pass_context
def favourites_list(ctx: click.Context, limit: Optional[int], max_id: Optional[str], since_id: Optional[str], min_id: Optional[str]):
    client: MastodonClient = ctx.obj["client"]
    params = {k: v for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}.items() if v is not None}
    res = client.request("GET", f"{API_V1_PREFIX}/favourites", params=params or None)
    _echo(res, raw=False)


@cli.group()
def media():
    """Media: upload attachment."""


@media.command("upload")
@click.argument("file_path", type=click.Path(exists=True, dir_okay=False))
@click.option("--description", type=str)
@click.option("--focus", type=str, help="e.g. '0.0,-0.5'")
@click.pass_context
def media_upload(ctx: click.Context, file_path: str, description: Optional[str], focus: Optional[str]):
    client: MastodonClient = ctx.obj["client"]
    with open(file_path, "rb") as f:
        files = {"file": f}
        data: Dict[str, Any] = {}
        if description is not None:
            data["description"] = description
        if focus is not None:
            data["focus"] = focus
        res = client.request("POST", f"{API_V1_PREFIX}/media", data=data or None, files=files)
    _echo(res, raw=False)


@cli.group()
def instance():
    """Instance: get instance info."""


@instance.command("show")
@click.pass_context
def instance_show(ctx: click.Context):
    client: MastodonClient = ctx.obj["client"]
    res = client.request("GET", f"{API_V1_PREFIX}/instance")
    _echo(res, raw=False)


def main():
    cli(prog_name="mastodon")


if __name__ == "__main__":
    main()
