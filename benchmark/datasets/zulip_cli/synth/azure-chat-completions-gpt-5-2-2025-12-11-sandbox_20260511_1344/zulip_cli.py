#!/usr/bin/env python3

import json
import os
import sys
from typing import Any, Dict, Optional, Tuple

import click
import requests
from dateutil import parser as date_parser


def _env(name: str) -> str:
    val = os.environ.get(name)
    if not val:
        raise click.ClickException(f"Missing required environment variable: {name}")
    return val


def _client() -> Tuple[str, Tuple[str, str]]:
    site = _env("ZULIP_SITE").rstrip("/")
    email = _env("ZULIP_EMAIL")
    api_key = _env("ZULIP_API_KEY")
    return f"{site}/api/v1", (email, api_key)


def _request(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, data: Optional[Dict[str, Any]] = None) -> Any:
    base, auth = _client()
    url = f"{base}{path}"
    try:
        resp = requests.request(method, url, auth=auth, params=params, data=data, timeout=60)
    except requests.RequestException as e:
        raise click.ClickException(str(e))

    ctype = resp.headers.get("content-type", "")
    if "application/json" in ctype:
        payload = resp.json()
    else:
        payload = resp.text

    if resp.status_code >= 400:
        raise click.ClickException(f"HTTP {resp.status_code}: {payload}")
    return payload


def _print(obj: Any) -> None:
    if isinstance(obj, (dict, list)):
        click.echo(json.dumps(obj, indent=2, sort_keys=True))
    else:
        click.echo(str(obj))


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def cli() -> None:
    """Zulip CLI (uses ZULIP_SITE, ZULIP_EMAIL, ZULIP_API_KEY)."""


@cli.group()
def messages() -> None:
    """Send/fetch/edit/delete messages, flags, reactions."""


@messages.command("send")
@click.option("--type", "msg_type", type=click.Choice(["stream", "private"], case_sensitive=False), required=True)
@click.option("--to", multiple=True, required=True, help="Stream name/id (stream) or recipient emails/user_ids (private). Repeatable.")
@click.option("--topic", default=None, help="Topic (required for stream messages).")
@click.option("--content", required=True)
def messages_send(msg_type: str, to: Tuple[str, ...], topic: Optional[str], content: str) -> None:
    data: Dict[str, Any] = {"type": msg_type, "content": content}
    if msg_type.lower() == "stream":
        if not topic:
            raise click.ClickException("--topic is required for stream messages")
        data["to"] = to[0]
        data["topic"] = topic
    else:
        data["to"] = json.dumps(list(to))
    _print(_request("POST", "/messages", data=data))


@messages.command("get")
@click.option("--anchor", default="newest")
@click.option("--num-before", type=int, default=30)
@click.option("--num-after", type=int, default=0)
@click.option("--narrow", default=None, help='JSON narrow, e.g. "[[\"stream\",\"general\"],[\"topic\",\"test\"]]"')
@click.option("--apply-markdown/--no-apply-markdown", default=True)
def messages_get(anchor: str, num_before: int, num_after: int, narrow: Optional[str], apply_markdown: bool) -> None:
    params: Dict[str, Any] = {
        "anchor": anchor,
        "num_before": num_before,
        "num_after": num_after,
        "apply_markdown": json.dumps(apply_markdown),
    }
    if narrow:
        params["narrow"] = narrow
    _print(_request("GET", "/messages", params=params))


@messages.command("edit")
@click.argument("message_id", type=int)
@click.option("--content", default=None)
@click.option("--topic", default=None)
@click.option("--propagate-mode", type=click.Choice(["change_one", "change_later", "change_all"], case_sensitive=False), default=None)
def messages_edit(message_id: int, content: Optional[str], topic: Optional[str], propagate_mode: Optional[str]) -> None:
    data: Dict[str, Any] = {}
    if content is not None:
        data["content"] = content
    if topic is not None:
        data["topic"] = topic
    if propagate_mode is not None:
        data["propagate_mode"] = propagate_mode
    if not data:
        raise click.ClickException("Provide at least one of --content/--topic")
    _print(_request("PATCH", f"/messages/{message_id}", data=data))


@messages.command("delete")
@click.argument("message_id", type=int)
def messages_delete(message_id: int) -> None:
    _print(_request("DELETE", f"/messages/{message_id}"))


@messages.command("flags")
@click.option("--op", type=click.Choice(["add", "remove"], case_sensitive=False), required=True)
@click.option("--flag", "flag_name", required=True)
@click.option("--messages", "message_ids", required=True, help="JSON list of message IDs, e.g. [1,2,3]")
def messages_flags(op: str, flag_name: str, message_ids: str) -> None:
    data = {"op": op, "flag": flag_name, "messages": message_ids}
    _print(_request("POST", "/messages/flags", data=data))


@messages.command("reaction-add")
@click.argument("message_id", type=int)
@click.option("--emoji-name", required=True)
@click.option("--emoji-code", default=None)
@click.option("--reaction-type", default=None)
def reaction_add(message_id: int, emoji_name: str, emoji_code: Optional[str], reaction_type: Optional[str]) -> None:
    data: Dict[str, Any] = {"emoji_name": emoji_name}
    if emoji_code:
        data["emoji_code"] = emoji_code
    if reaction_type:
        data["reaction_type"] = reaction_type
    _print(_request("POST", f"/messages/{message_id}/reactions", data=data))


@messages.command("reaction-remove")
@click.argument("message_id", type=int)
@click.option("--emoji-name", required=True)
@click.option("--emoji-code", default=None)
@click.option("--reaction-type", default=None)
def reaction_remove(message_id: int, emoji_name: str, emoji_code: Optional[str], reaction_type: Optional[str]) -> None:
    data: Dict[str, Any] = {"emoji_name": emoji_name}
    if emoji_code:
        data["emoji_code"] = emoji_code
    if reaction_type:
        data["reaction_type"] = reaction_type
    _print(_request("DELETE", f"/messages/{message_id}/reactions", data=data))


@cli.group()
def streams() -> None:
    """Streams/channels."""


@streams.command("list")
@click.option("--include-public/--no-include-public", default=True)
@click.option("--include-subscribed/--no-include-subscribed", default=True)
@click.option("--include-all-active/--no-include-all-active", default=False)
def streams_list(include_public: bool, include_subscribed: bool, include_all_active: bool) -> None:
    params = {
        "include_public": json.dumps(include_public),
        "include_subscribed": json.dumps(include_subscribed),
        "include_all_active": json.dumps(include_all_active),
    }
    _print(_request("GET", "/streams", params=params))


@streams.command("create")
@click.option("--name", required=True)
@click.option("--description", default="")
@click.option("--is-private/--is-public", default=False)
def streams_create(name: str, description: str, is_private: bool) -> None:
    data = {
        "subscriptions": json.dumps([{ "name": name, "description": description }]),
        "is_private": json.dumps(is_private),
    }
    _print(_request("POST", "/users/me/subscriptions", data=data))


@streams.command("subscribe")
@click.option("--stream", multiple=True, required=True, help="Stream name(s). Repeatable.")
def streams_subscribe(stream: Tuple[str, ...]) -> None:
    data = {"subscriptions": json.dumps([{ "name": s } for s in stream])}
    _print(_request("POST", "/users/me/subscriptions", data=data))


@streams.command("topics")
@click.option("--stream-id", type=int, required=True)
def streams_topics(stream_id: int) -> None:
    _print(_request("GET", f"/users/me/{stream_id}/topics"))


@streams.command("update")
@click.option("--stream-id", type=int, required=True)
@click.option("--new-name", default=None)
@click.option("--description", default=None)
@click.option("--is-private", type=bool, default=None)
def streams_update(stream_id: int, new_name: Optional[str], description: Optional[str], is_private: Optional[bool) -> None:
    data: Dict[str, Any] = {}
    if new_name is not None:
        data["new_name"] = new_name
    if description is not None:
        data["description"] = description
    if is_private is not None:
        data["is_private"] = json.dumps(is_private)
    if not data:
        raise click.ClickException("Provide at least one field to update")
    _print(_request("PATCH", f"/streams/{stream_id}", data=data))


@cli.group()
def users() -> None:
    """Users, profiles, presence."""


@users.command("me")
def users_me() -> None:
    _print(_request("GET", "/users/me"))


@users.command("list")
@click.option("--client-gravatar/--no-client-gravatar", default=False)
@click.option("--include-custom-profile-fields/--no-include-custom-profile-fields", default=False)
def users_list(client_gravatar: bool, include_custom_profile_fields: bool) -> None:
    params = {
        "client_gravatar": json.dumps(client_gravatar),
        "include_custom_profile_fields": json.dumps(include_custom_profile_fields),
    }
    _print(_request("GET", "/users", params=params))


@users.command("presence")
@click.argument("user_id_or_email")
def users_presence(user_id_or_email: str) -> None:
    _print(_request("GET", f"/users/{user_id_or_email}/presence"))


@cli.group()
def drafts() -> None:
    """Drafts."""


@drafts.command("list")
def drafts_list() -> None:
    _print(_request("GET", "/drafts"))


@drafts.command("create")
@click.option("--draft", multiple=True, required=True, help='Draft JSON object. Repeatable. e.g. {"type":"stream","to":"general","topic":"t","content":"c"}')
def drafts_create(draft: Tuple[str, ...]) -> None:
    drafts_payload = [json.loads(d) for d in draft]
    _print(_request("POST", "/drafts", data={"drafts": json.dumps(drafts_payload)}))


@cli.group()
def scheduled() -> None:
    """Scheduled messages and reminders."""


@scheduled.command("list")
def scheduled_list() -> None:
    _print(_request("GET", "/scheduled_messages"))


@scheduled.command("send")
@click.option("--type", "msg_type", type=click.Choice(["stream", "private"], case_sensitive=False), required=True)
@click.option("--to", multiple=True, required=True)
@click.option("--topic", default=None)
@click.option("--content", required=True)
@click.option("--scheduled-at", required=True, help="Datetime (ISO8601) or unix timestamp")
def scheduled_send(msg_type: str, to: Tuple[str, ...], topic: Optional[str], content: str, scheduled_at: str) -> None:
    try:
        when = int(scheduled_at)
    except ValueError:
        when = int(date_parser.isoparse(scheduled_at).timestamp())

    data: Dict[str, Any] = {"type": msg_type, "content": content, "scheduled_delivery_timestamp": when}
    if msg_type.lower() == "stream":
        if not topic:
            raise click.ClickException("--topic is required for stream messages")
        data["to"] = to[0]
        data["topic"] = topic
    else:
        data["to"] = json.dumps(list(to))

    _print(_request("POST", "/scheduled_messages", data=data))


@cli.group()
def alert_words() -> None:
    """Alert words."""


@alert_words.command("list")
def alert_words_list() -> None:
    _print(_request("GET", "/users/me/alert_words"))


@alert_words.command("add")
@click.option("--word", multiple=True, required=True)
def alert_words_add(word: Tuple[str, ...]) -> None:
    _print(_request("POST", "/users/me/alert_words", data={"alert_words": json.dumps(list(word))}))


@alert_words.command("remove")
@click.option("--word", multiple=True, required=True)
def alert_words_remove(word: Tuple[str, ...]) -> None:
    _print(_request("DELETE", "/users/me/alert_words", data={"alert_words": json.dumps(list(word))}))


if __name__ == "__main__":
    cli()
