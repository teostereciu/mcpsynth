#!/usr/bin/env python3
import json
import os
import sys
from typing import Any, Dict, Optional

import click
import requests
from dateutil import parser as date_parser


def _env(name: str) -> str:
    val = os.environ.get(name)
    if not val:
        raise click.ClickException(f"Missing required environment variable: {name}")
    return val


class ZulipClient:
    def __init__(self, site: str, email: str, api_key: str):
        self.base = site.rstrip("/") + "/api/v1"
        self.auth = (email, api_key)

    def request(self, method: str, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        url = self.base + ("/" + path.lstrip("/"))
        method = method.upper()
        if method in {"GET", "DELETE"}:
            r = requests.request(method, url, auth=self.auth, params=params, timeout=60)
        else:
            r = requests.request(method, url, auth=self.auth, data=params or {}, timeout=60)
        try:
            data = r.json()
        except Exception:
            r.raise_for_status()
            return r.text
        if r.status_code >= 400 or (isinstance(data, dict) and data.get("result") == "error"):
            msg = data.get("msg") if isinstance(data, dict) else str(data)
            raise click.ClickException(f"HTTP {r.status_code}: {msg}")
        return data


def _client() -> ZulipClient:
    return ZulipClient(_env("ZULIP_SITE"), _env("ZULIP_EMAIL"), _env("ZULIP_API_KEY"))


def _print(obj: Any) -> None:
    click.echo(json.dumps(obj, indent=2, sort_keys=True))


@click.group()
def cli() -> None:
    """Zulip CLI (uses ZULIP_SITE, ZULIP_EMAIL, ZULIP_API_KEY)."""


@cli.group()
def messages() -> None:
    """Send, fetch, edit, delete messages and related operations."""


@messages.command("send")
@click.option("--type", "msg_type", type=click.Choice(["stream", "private"], case_sensitive=False), required=True)
@click.option("--to", multiple=True, required=True, help="Stream name (for stream) or recipient email(s)/user_id(s) (for private). Repeatable.")
@click.option("--topic", default=None, help="Topic (required for stream messages).")
@click.option("--content", required=True)
def messages_send(msg_type: str, to: tuple[str, ...], topic: Optional[str], content: str) -> None:
    c = _client()
    params: Dict[str, Any] = {"type": msg_type, "content": content}
    if msg_type.lower() == "stream":
        if not topic:
            raise click.ClickException("--topic is required for stream messages")
        params["to"] = to[0]
        params["topic"] = topic
    else:
        params["to"] = json.dumps(list(to))
    _print(c.request("POST", "/messages", params))


@messages.command("get")
@click.option("--anchor", default="newest")
@click.option("--num-before", type=int, default=20)
@click.option("--num-after", type=int, default=0)
@click.option("--narrow", default=None, help="JSON narrow array, e.g. '[{"operator":"stream","operand":"general"}]'")
@click.option("--apply-markdown/--no-apply-markdown", default=True)
def messages_get(anchor: str, num_before: int, num_after: int, narrow: Optional[str], apply_markdown: bool) -> None:
    c = _client()
    params: Dict[str, Any] = {
        "anchor": anchor,
        "num_before": num_before,
        "num_after": num_after,
        "apply_markdown": json.dumps(apply_markdown),
    }
    if narrow:
        params["narrow"] = narrow
    _print(c.request("GET", "/messages", params))


@messages.command("edit")
@click.argument("message_id", type=int)
@click.option("--content", default=None)
@click.option("--topic", default=None)
@click.option("--propagate-mode", type=click.Choice(["change_one", "change_later", "change_all"], case_sensitive=False), default=None)
def messages_edit(message_id: int, content: Optional[str], topic: Optional[str], propagate_mode: Optional[str]) -> None:
    if not content and not topic:
        raise click.ClickException("Provide --content and/or --topic")
    c = _client()
    params: Dict[str, Any] = {}
    if content is not None:
        params["content"] = content
    if topic is not None:
        params["topic"] = topic
    if propagate_mode is not None:
        params["propagate_mode"] = propagate_mode
    _print(c.request("PATCH", f"/messages/{message_id}", params))


@messages.command("delete")
@click.argument("message_id", type=int)
def messages_delete(message_id: int) -> None:
    c = _client()
    _print(c.request("DELETE", f"/messages/{message_id}"))


@messages.command("history")
@click.argument("message_id", type=int)
def messages_history(message_id: int) -> None:
    c = _client()
    _print(c.request("GET", f"/messages/{message_id}/history"))


@messages.command("flags")
@click.option("--messages", required=True, help="JSON list of message IDs")
@click.option("--op", "operation", type=click.Choice(["add", "remove"], case_sensitive=False), required=True)
@click.option("--flag", required=True)
def messages_flags(messages: str, operation: str, flag: str) -> None:
    c = _client()
    params = {"messages": messages, "op": operation, "flag": flag}
    _print(c.request("POST", "/messages/flags", params))


@messages.command("reaction-add")
@click.argument("message_id", type=int)
@click.option("--emoji-name", required=True)
@click.option("--emoji-code", default=None)
@click.option("--reaction-type", default=None)
def messages_reaction_add(message_id: int, emoji_name: str, emoji_code: Optional[str], reaction_type: Optional[str]) -> None:
    c = _client()
    params: Dict[str, Any] = {"emoji_name": emoji_name}
    if emoji_code:
        params["emoji_code"] = emoji_code
    if reaction_type:
        params["reaction_type"] = reaction_type
    _print(c.request("POST", f"/messages/{message_id}/reactions", params))


@messages.command("reaction-remove")
@click.argument("message_id", type=int)
@click.option("--emoji-name", required=True)
@click.option("--emoji-code", default=None)
@click.option("--reaction-type", default=None)
def messages_reaction_remove(message_id: int, emoji_name: str, emoji_code: Optional[str], reaction_type: Optional[str]) -> None:
    c = _client()
    params: Dict[str, Any] = {"emoji_name": emoji_name}
    if emoji_code:
        params["emoji_code"] = emoji_code
    if reaction_type:
        params["reaction_type"] = reaction_type
    _print(c.request("DELETE", f"/messages/{message_id}/reactions", params))


@cli.group()
def streams() -> None:
    """Streams/channels operations."""


@streams.command("list")
@click.option("--include-public/--no-include-public", default=True)
@click.option("--include-subscribed/--no-include-subscribed", default=True)
@click.option("--include-all-active/--no-include-all-active", default=False)
def streams_list(include_public: bool, include_subscribed: bool, include_all_active: bool) -> None:
    c = _client()
    params = {
        "include_public": json.dumps(include_public),
        "include_subscribed": json.dumps(include_subscribed),
        "include_all_active": json.dumps(include_all_active),
    }
    _print(c.request("GET", "/streams", params))


@streams.command("create")
@click.option("--name", required=True)
@click.option("--description", default="")
@click.option("--is-private/--is-public", default=False)
def streams_create(name: str, description: str, is_private: bool) -> None:
    c = _client()
    params = {
        "subscriptions": json.dumps([{ "name": name, "description": description }]),
        "is_private": json.dumps(is_private),
    }
    _print(c.request("POST", "/users/me/subscriptions", params))


@streams.command("subscribe")
@click.option("--stream", "streams_", multiple=True, required=True, help="Stream name(s). Repeatable.")
@click.option("--principals", default=None, help="JSON list of user IDs/emails to subscribe (optional)")
def streams_subscribe(streams_: tuple[str, ...], principals: Optional[str]) -> None:
    c = _client()
    params: Dict[str, Any] = {"subscriptions": json.dumps([{ "name": s } for s in streams_])}
    if principals:
        params["principals"] = principals
    _print(c.request("POST", "/users/me/subscriptions", params))


@streams.command("unsubscribe")
@click.option("--stream", "streams_", multiple=True, required=True)
def streams_unsubscribe(streams_: tuple[str, ...]) -> None:
    c = _client()
    params = {"subscriptions": json.dumps(list(streams_))}
    _print(c.request("DELETE", "/users/me/subscriptions", params))


@streams.command("topics")
@click.argument("stream_id", type=int)
def streams_topics(stream_id: int) -> None:
    c = _client()
    _print(c.request("GET", f"/users/me/{stream_id}/topics"))


@streams.command("subscriptions")
def streams_subscriptions() -> None:
    c = _client()
    _print(c.request("GET", "/users/me/subscriptions"))


@cli.group()
def users() -> None:
    """User/profile/presence operations."""


@users.command("me")
def users_me() -> None:
    c = _client()
    _print(c.request("GET", "/users/me"))


@users.command("list")
@click.option("--client-gravatar/--no-client-gravatar", default=False)
@click.option("--include-custom-profile-fields/--no-include-custom-profile-fields", default=False)
def users_list(client_gravatar: bool, include_custom_profile_fields: bool) -> None:
    c = _client()
    params = {
        "client_gravatar": json.dumps(client_gravatar),
        "include_custom_profile_fields": json.dumps(include_custom_profile_fields),
    }
    _print(c.request("GET", "/users", params))


@users.command("presence")
@click.argument("user", type=str)
def users_presence(user: str) -> None:
    c = _client()
    _print(c.request("GET", f"/users/{user}/presence"))


@cli.group()
def drafts() -> None:
    """Drafts operations."""


@drafts.command("list")
def drafts_list() -> None:
    c = _client()
    _print(c.request("GET", "/drafts"))


@drafts.command("create")
@click.option("--drafts", "drafts_json", required=True, help="JSON list of draft objects")
def drafts_create(drafts_json: str) -> None:
    c = _client()
    _print(c.request("POST", "/drafts", {"drafts": drafts_json}))


@drafts.command("delete")
@click.argument("draft_id", type=int)
def drafts_delete(draft_id: int) -> None:
    c = _client()
    _print(c.request("DELETE", f"/drafts/{draft_id}"))


@cli.group()
def scheduled() -> None:
    """Scheduled messages and reminders."""


@scheduled.command("list")
def scheduled_list() -> None:
    c = _client()
    _print(c.request("GET", "/scheduled_messages"))


@scheduled.command("send")
@click.option("--type", "msg_type", type=click.Choice(["stream", "private"], case_sensitive=False), required=True)
@click.option("--to", multiple=True, required=True)
@click.option("--topic", default=None)
@click.option("--content", required=True)
@click.option("--scheduled-at", required=True, help="Datetime (ISO8601) or unix timestamp")
def scheduled_send(msg_type: str, to: tuple[str, ...], topic: Optional[str], content: str, scheduled_at: str) -> None:
    c = _client()
    try:
        ts = int(scheduled_at)
    except ValueError:
        ts = int(date_parser.parse(scheduled_at).timestamp())
    params: Dict[str, Any] = {"type": msg_type, "content": content, "scheduled_delivery_timestamp": ts}
    if msg_type.lower() == "stream":
        if not topic:
            raise click.ClickException("--topic is required for stream messages")
        params["to"] = to[0]
        params["topic"] = topic
    else:
        params["to"] = json.dumps(list(to))
    _print(c.request("POST", "/scheduled_messages", params))


@scheduled.command("delete")
@click.argument("scheduled_message_id", type=int)
def scheduled_delete(scheduled_message_id: int) -> None:
    c = _client()
    _print(c.request("DELETE", f"/scheduled_messages/{scheduled_message_id}"))


@cli.group()
def alert_words() -> None:
    """Alert words operations."""


@alert_words.command("list")
def alert_words_list() -> None:
    c = _client()
    _print(c.request("GET", "/users/me/alert_words"))


@alert_words.command("add")
@click.option("--word", required=True)
def alert_words_add(word: str) -> None:
    c = _client()
    _print(c.request("POST", "/users/me/alert_words", {"alert_words": json.dumps([word])}))


@alert_words.command("remove")
@click.option("--word", required=True)
def alert_words_remove(word: str) -> None:
    c = _client()
    _print(c.request("DELETE", "/users/me/alert_words", {"alert_words": json.dumps([word])}))


if __name__ == "__main__":
    cli()
