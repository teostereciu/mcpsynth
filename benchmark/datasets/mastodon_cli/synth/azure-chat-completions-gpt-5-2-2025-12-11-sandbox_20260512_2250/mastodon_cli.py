#!/usr/bin/env python3
import json
import os
from typing import Any, Dict, Optional, Tuple

import click
import requests
from dotenv import load_dotenv


def _env(name: str, default: Optional[str] = None) -> str:
    v = os.getenv(name, default)
    if v is None or v == "":
        raise click.ClickException(f"Missing required environment variable: {name}")
    return v


def _client() -> Tuple[str, Dict[str, str]]:
    load_dotenv()
    base_url = _env("MASTODON_BASE_URL").rstrip("/")
    token = _env("MASTODON_ACCESS_TOKEN")
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    return base_url, headers


def _request(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, data: Optional[Dict[str, Any]] = None,
             json_body: Optional[Dict[str, Any]] = None, files: Optional[Dict[str, Any]] = None) -> Any:
    base_url, headers = _client()
    url = f"{base_url}{path}"
    resp = requests.request(method, url, headers=headers, params=params, data=data, json=json_body, files=files, timeout=60)
    if resp.status_code >= 400:
        try:
            err = resp.json()
        except Exception:
            err = resp.text
        raise click.ClickException(f"HTTP {resp.status_code} error for {method} {path}: {err}")
    if resp.status_code == 204:
        return None
    if resp.headers.get("Content-Type", "").startswith("application/json"):
        return resp.json()
    return resp.text


def _print(obj: Any, raw: bool = False):
    if raw and isinstance(obj, str):
        click.echo(obj)
    else:
        click.echo(json.dumps(obj, indent=2, ensure_ascii=False))


@click.group()
def cli():
    """Mastodon CLI (uses MASTODON_BASE_URL and MASTODON_ACCESS_TOKEN)."""


@cli.group()
def accounts():
    pass


@accounts.command("verify-credentials")
def accounts_verify_credentials():
    _print(_request("GET", "/api/v1/accounts/verify_credentials"))


@accounts.command("get")
@click.argument("account_id")
def accounts_get(account_id: str):
    _print(_request("GET", f"/api/v1/accounts/{account_id}"))


@accounts.command("follow")
@click.argument("account_id")
@click.option("--reblogs/--no-reblogs", default=None)
@click.option("--notify/--no-notify", default=None)
@click.option("--languages", help="Comma-separated list")
def accounts_follow(account_id: str, reblogs: Optional[bool], notify: Optional[bool], languages: Optional[str]):
    data: Dict[str, Any] = {}
    if reblogs is not None:
        data["reblogs"] = str(reblogs).lower()
    if notify is not None:
        data["notify"] = str(notify).lower()
    if languages:
        data["languages"] = [s.strip() for s in languages.split(",") if s.strip()]
    _print(_request("POST", f"/api/v1/accounts/{account_id}/follow", data=data))


@accounts.command("unfollow")
@click.argument("account_id")
def accounts_unfollow(account_id: str):
    _print(_request("POST", f"/api/v1/accounts/{account_id}/unfollow"))


@accounts.command("followers")
@click.argument("account_id")
@click.option("--limit", type=int)
@click.option("--max-id")
@click.option("--since-id")
def accounts_followers(account_id: str, limit: Optional[int], max_id: Optional[str], since_id: Optional[str]):
    params = {k: v for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id}.items() if v is not None}
    _print(_request("GET", f"/api/v1/accounts/{account_id}/followers", params=params))


@accounts.command("following")
@click.argument("account_id")
@click.option("--limit", type=int)
@click.option("--max-id")
@click.option("--since-id")
def accounts_following(account_id: str, limit: Optional[int], max_id: Optional[str], since_id: Optional[str]):
    params = {k: v for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id}.items() if v is not None}
    _print(_request("GET", f"/api/v1/accounts/{account_id}/following", params=params))


@cli.group()
def statuses():
    pass


@statuses.command("post")
@click.option("--status", required=True, help="Text content")
@click.option("--in-reply-to-id")
@click.option("--sensitive/--no-sensitive", default=None)
@click.option("--spoiler-text")
@click.option("--visibility", type=click.Choice(["public", "unlisted", "private", "direct"], case_sensitive=False))
@click.option("--language")
@click.option("--media-ids", help="Comma-separated media IDs")
@click.option("--poll-options", help="Comma-separated options")
@click.option("--poll-expires-in", type=int)
@click.option("--scheduled-at", help="ISO8601 timestamp")
def statuses_post(status: str, in_reply_to_id: Optional[str], sensitive: Optional[bool], spoiler_text: Optional[str],
                 visibility: Optional[str], language: Optional[str], media_ids: Optional[str],
                 poll_options: Optional[str], poll_expires_in: Optional[int], scheduled_at: Optional[str]):
    data: Dict[str, Any] = {"status": status}
    if in_reply_to_id:
        data["in_reply_to_id"] = in_reply_to_id
    if sensitive is not None:
        data["sensitive"] = str(sensitive).lower()
    if spoiler_text is not None:
        data["spoiler_text"] = spoiler_text
    if visibility:
        data["visibility"] = visibility
    if language:
        data["language"] = language
    if media_ids:
        data["media_ids"] = [s.strip() for s in media_ids.split(",") if s.strip()]
    if poll_options:
        data["poll"] = {"options": [s.strip() for s in poll_options.split(",") if s.strip()]}
        if poll_expires_in is not None:
            data["poll"]["expires_in"] = poll_expires_in
    if scheduled_at:
        data["scheduled_at"] = scheduled_at
    _print(_request("POST", "/api/v1/statuses", data=data))


@statuses.command("get")
@click.argument("status_id")
def statuses_get(status_id: str):
    _print(_request("GET", f"/api/v1/statuses/{status_id}"))


@statuses.command("delete")
@click.argument("status_id")
def statuses_delete(status_id: str):
    _print(_request("DELETE", f"/api/v1/statuses/{status_id}"))


@statuses.command("context")
@click.argument("status_id")
def statuses_context(status_id: str):
    _print(_request("GET", f"/api/v1/statuses/{status_id}/context"))


@statuses.command("reblog")
@click.argument("status_id")
def statuses_reblog(status_id: str):
    _print(_request("POST", f"/api/v1/statuses/{status_id}/reblog"))


@statuses.command("unreblog")
@click.argument("status_id")
def statuses_unreblog(status_id: str):
    _print(_request("POST", f"/api/v1/statuses/{status_id}/unreblog"))


@statuses.command("favourite")
@click.argument("status_id")
def statuses_favourite(status_id: str):
    _print(_request("POST", f"/api/v1/statuses/{status_id}/favourite"))


@statuses.command("unfavourite")
@click.argument("status_id")
def statuses_unfavourite(status_id: str):
    _print(_request("POST", f"/api/v1/statuses/{status_id}/unfavourite"))


@statuses.command("bookmark")
@click.argument("status_id")
def statuses_bookmark(status_id: str):
    _print(_request("POST", f"/api/v1/statuses/{status_id}/bookmark"))


@statuses.command("unbookmark")
@click.argument("status_id")
def statuses_unbookmark(status_id: str):
    _print(_request("POST", f"/api/v1/statuses/{status_id}/unbookmark"))


@cli.group()
def timelines():
    pass


@timelines.command("home")
@click.option("--limit", type=int)
@click.option("--max-id")
@click.option("--since-id")
@click.option("--min-id")
def timelines_home(limit: Optional[int], max_id: Optional[str], since_id: Optional[str], min_id: Optional[str]):
    params = {k: v for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}.items() if v is not None}
    _print(_request("GET", "/api/v1/timelines/home", params=params))


@timelines.command("public")
@click.option("--local/--no-local", default=None)
@click.option("--remote/--no-remote", default=None)
@click.option("--only-media/--no-only-media", default=None)
@click.option("--limit", type=int)
@click.option("--max-id")
@click.option("--since-id")
@click.option("--min-id")
def timelines_public(local: Optional[bool], remote: Optional[bool], only_media: Optional[bool], limit: Optional[int],
                    max_id: Optional[str], since_id: Optional[str], min_id: Optional[str]):
    params: Dict[str, Any] = {}
    for k, v in {"local": local, "remote": remote, "only_media": only_media, "limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}.items():
        if v is None:
            continue
        params[k] = str(v).lower() if isinstance(v, bool) else v
    _print(_request("GET", "/api/v1/timelines/public", params=params))


@timelines.command("hashtag")
@click.argument("tag")
@click.option("--local/--no-local", default=None)
@click.option("--only-media/--no-only-media", default=None)
@click.option("--limit", type=int)
@click.option("--max-id")
@click.option("--since-id")
@click.option("--min-id")
def timelines_hashtag(tag: str, local: Optional[bool], only_media: Optional[bool], limit: Optional[int],
                     max_id: Optional[str], since_id: Optional[str], min_id: Optional[str]):
    params: Dict[str, Any] = {}
    for k, v in {"local": local, "only_media": only_media, "limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}.items():
        if v is None:
            continue
        params[k] = str(v).lower() if isinstance(v, bool) else v
    _print(_request("GET", f"/api/v1/timelines/tag/{tag}", params=params))


@timelines.command("list")
@click.argument("list_id")
@click.option("--limit", type=int)
@click.option("--max-id")
@click.option("--since-id")
@click.option("--min-id")
def timelines_list(list_id: str, limit: Optional[int], max_id: Optional[str], since_id: Optional[str], min_id: Optional[str]):
    params = {k: v for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}.items() if v is not None}
    _print(_request("GET", f"/api/v1/timelines/list/{list_id}", params=params))


@cli.group()
def notifications():
    pass


@notifications.command("list")
@click.option("--types", help="Comma-separated types")
@click.option("--exclude-types", help="Comma-separated types")
@click.option("--account-id")
@click.option("--limit", type=int)
@click.option("--max-id")
@click.option("--since-id")
@click.option("--min-id")
def notifications_list(types: Optional[str], exclude_types: Optional[str], account_id: Optional[str], limit: Optional[int],
                       max_id: Optional[str], since_id: Optional[str], min_id: Optional[str]):
    params: Dict[str, Any] = {}
    if types:
        params["types"] = [s.strip() for s in types.split(",") if s.strip()]
    if exclude_types:
        params["exclude_types"] = [s.strip() for s in exclude_types.split(",") if s.strip()]
    for k, v in {"account_id": account_id, "limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}.items():
        if v is not None:
            params[k] = v
    _print(_request("GET", "/api/v1/notifications", params=params))


@notifications.command("get")
@click.argument("notification_id")
def notifications_get(notification_id: str):
    _print(_request("GET", f"/api/v1/notifications/{notification_id}"))


@notifications.command("dismiss")
@click.argument("notification_id")
def notifications_dismiss(notification_id: str):
    _print(_request("POST", f"/api/v1/notifications/{notification_id}/dismiss"))


@notifications.command("clear")
def notifications_clear():
    _print(_request("POST", "/api/v1/notifications/clear"))


@cli.group()
def search():
    pass


@search.command("v2")
@click.option("--q", required=True)
@click.option("--type", "type_", type=click.Choice(["accounts", "hashtags", "statuses"], case_sensitive=False))
@click.option("--resolve/--no-resolve", default=None)
@click.option("--limit", type=int)
@click.option("--offset", type=int)
@click.option("--following/--no-following", default=None)
def search_v2(q: str, type_: Optional[str], resolve: Optional[bool], limit: Optional[int], offset: Optional[int], following: Optional[bool]):
    params: Dict[str, Any] = {"q": q}
    if type_:
        params["type"] = type_
    if resolve is not None:
        params["resolve"] = str(resolve).lower()
    if following is not None:
        params["following"] = str(following).lower()
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    _print(_request("GET", "/api/v2/search", params=params))


@cli.group()
def lists():
    pass


@lists.command("list")
def lists_list():
    _print(_request("GET", "/api/v1/lists"))


@lists.command("create")
@click.option("--title", required=True)
@click.option("--replies-policy", type=click.Choice(["followed", "list", "none"], case_sensitive=False))
def lists_create(title: str, replies_policy: Optional[str]):
    data: Dict[str, Any] = {"title": title}
    if replies_policy:
        data["replies_policy"] = replies_policy
    _print(_request("POST", "/api/v1/lists", data=data))


@lists.command("get")
@click.argument("list_id")
def lists_get(list_id: str):
    _print(_request("GET", f"/api/v1/lists/{list_id}"))


@lists.command("update")
@click.argument("list_id")
@click.option("--title")
@click.option("--replies-policy", type=click.Choice(["followed", "list", "none"], case_sensitive=False))
def lists_update(list_id: str, title: Optional[str], replies_policy: Optional[str]):
    data: Dict[str, Any] = {}
    if title is not None:
        data["title"] = title
    if replies_policy is not None:
        data["replies_policy"] = replies_policy
    _print(_request("PUT", f"/api/v1/lists/{list_id}", data=data))


@lists.command("delete")
@click.argument("list_id")
def lists_delete(list_id: str):
    _print(_request("DELETE", f"/api/v1/lists/{list_id}"))


@lists.group("accounts")
def lists_accounts():
    pass


@lists_accounts.command("list")
@click.argument("list_id")
def lists_accounts_list(list_id: str):
    _print(_request("GET", f"/api/v1/lists/{list_id}/accounts"))


@lists_accounts.command("add")
@click.argument("list_id")
@click.option("--account-ids", required=True, help="Comma-separated account IDs")
def lists_accounts_add(list_id: str, account_ids: str):
    data = {"account_ids": [s.strip() for s in account_ids.split(",") if s.strip()]}
    _print(_request("POST", f"/api/v1/lists/{list_id}/accounts", data=data))


@lists_accounts.command("remove")
@click.argument("list_id")
@click.option("--account-ids", required=True, help="Comma-separated account IDs")
def lists_accounts_remove(list_id: str, account_ids: str):
    data = {"account_ids": [s.strip() for s in account_ids.split(",") if s.strip()]}
    _print(_request("DELETE", f"/api/v1/lists/{list_id}/accounts", data=data))


@cli.group()
def bookmarks():
    pass


@bookmarks.command("list")
@click.option("--limit", type=int)
@click.option("--max-id")
@click.option("--since-id")
@click.option("--min-id")
def bookmarks_list(limit: Optional[int], max_id: Optional[str], since_id: Optional[str], min_id: Optional[str]):
    params = {k: v for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}.items() if v is not None}
    _print(_request("GET", "/api/v1/bookmarks", params=params))


@cli.group()
def favourites():
    pass


@favourites.command("list")
@click.option("--limit", type=int)
@click.option("--max-id")
@click.option("--since-id")
@click.option("--min-id")
def favourites_list(limit: Optional[int], max_id: Optional[str], since_id: Optional[str], min_id: Optional[str]):
    params = {k: v for k, v in {"limit": limit, "max_id": max_id, "since_id": since_id, "min_id": min_id}.items() if v is not None}
    _print(_request("GET", "/api/v1/favourites", params=params))


@cli.group()
def media():
    pass


@media.command("upload")
@click.option("--file", "file_path", required=True, type=click.Path(exists=True, dir_okay=False))
@click.option("--description")
@click.option("--focus", help="e.g. '0.0,-0.5'")
def media_upload(file_path: str, description: Optional[str], focus: Optional[str]):
    data: Dict[str, Any] = {}
    if description is not None:
        data["description"] = description
    if focus is not None:
        data["focus"] = focus
    with open(file_path, "rb") as f:
        files = {"file": f}
        _print(_request("POST", "/api/v1/media", data=data, files=files))


@cli.group()
def instance():
    pass


@instance.command("get")
def instance_get():
    _print(_request("GET", "/api/v1/instance"))


if __name__ == "__main__":
    cli()
