#!/usr/bin/env python3
import json
import os
from dataclasses import dataclass
from typing import Any, Dict, Optional

import click
import requests


@dataclass
class ZulipConfig:
    site: str
    email: str
    api_key: str

    @staticmethod
    def from_env() -> "ZulipConfig":
        site = os.environ.get("ZULIP_SITE")
        email = os.environ.get("ZULIP_EMAIL")
        api_key = os.environ.get("ZULIP_API_KEY")
        missing = [k for k, v in [("ZULIP_SITE", site), ("ZULIP_EMAIL", email), ("ZULIP_API_KEY", api_key)] if not v]
        if missing:
            raise click.ClickException(f"Missing environment variables: {', '.join(missing)}")
        return ZulipConfig(site=site.rstrip("/"), email=email, api_key=api_key)


class ZulipClient:
    def __init__(self, cfg: ZulipConfig, timeout: int = 30):
        self.cfg = cfg
        self.base = f"{cfg.site}/api/v1"
        self.session = requests.Session()
        self.session.auth = (cfg.email, cfg.api_key)
        self.timeout = timeout

    def request(self, method: str, path: str, *, params: Optional[Dict[str, Any]] = None, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = self.base + (path if path.startswith("/") else f"/{path}")
        resp = self.session.request(method, url, params=params, data=data, timeout=self.timeout)
        ctype = resp.headers.get("content-type", "")
        if "application/json" in ctype:
            payload = resp.json()
        else:
            payload = {"raw": resp.text}
        if resp.status_code >= 400:
            msg = payload.get("msg") if isinstance(payload, dict) else None
            raise click.ClickException(f"HTTP {resp.status_code}: {msg or resp.text}")
        return payload


def _echo(obj: Any, raw: bool) -> None:
    if raw and isinstance(obj, dict) and "raw" in obj:
        click.echo(obj["raw"])
    else:
        click.echo(json.dumps(obj, indent=2, sort_keys=True))


@click.group()
@click.option("--raw", is_flag=True, help="Print raw response when not JSON")
@click.pass_context
def cli(ctx: click.Context, raw: bool) -> None:
    ctx.ensure_object(dict)
    ctx.obj["raw"] = raw
    ctx.obj["client"] = ZulipClient(ZulipConfig.from_env())


@cli.group()
def messages() -> None:
    """Message operations."""


@messages.command("send")
@click.option("--type", "msg_type", type=click.Choice(["stream", "private"], case_sensitive=False), required=True)
@click.option("--to", required=True, help="Stream name/id (stream) or comma-separated emails/user_ids (private)")
@click.option("--topic", help="Topic (required for stream messages)")
@click.option("--content", required=True)
@click.pass_context
def messages_send(ctx: click.Context, msg_type: str, to: str, topic: Optional[str], content: str) -> None:
    client: ZulipClient = ctx.obj["client"]
    data: Dict[str, Any] = {"type": msg_type, "to": to, "content": content}
    if msg_type.lower() == "stream":
        if not topic:
            raise click.ClickException("--topic is required for stream messages")
        data["topic"] = topic
    res = client.request("POST", "/messages", data=data)
    _echo(res, ctx.obj["raw"])


@messages.command("get")
@click.option("--anchor", default="newest")
@click.option("--num-before", default=10, type=int)
@click.option("--num-after", default=0, type=int)
@click.option("--narrow", help="JSON narrow array, e.g. '[{""operator"":""stream"",""operand"":""general""}]'")
@click.option("--apply-markdown", type=bool, default=True)
@click.pass_context
def messages_get(ctx: click.Context, anchor: str, num_before: int, num_after: int, narrow: Optional[str], apply_markdown: bool) -> None:
    client: ZulipClient = ctx.obj["client"]
    params: Dict[str, Any] = {
        "anchor": anchor,
        "num_before": num_before,
        "num_after": num_after,
        "apply_markdown": json.dumps(apply_markdown),
    }
    if narrow:
        params["narrow"] = narrow
    res = client.request("GET", "/messages", params=params)
    _echo(res, ctx.obj["raw"])


@messages.command("edit")
@click.argument("message_id", type=int)
@click.option("--content")
@click.option("--topic")
@click.option("--propagate-mode", type=click.Choice(["change_one", "change_later", "change_all"], case_sensitive=False))
@click.pass_context
def messages_edit(ctx: click.Context, message_id: int, content: Optional[str], topic: Optional[str], propagate_mode: Optional[str]) -> None:
    if not content and not topic:
        raise click.ClickException("Provide --content and/or --topic")
    client: ZulipClient = ctx.obj["client"]
    data: Dict[str, Any] = {}
    if content is not None:
        data["content"] = content
    if topic is not None:
        data["topic"] = topic
    if propagate_mode is not None:
        data["propagate_mode"] = propagate_mode
    res = client.request("PATCH", f"/messages/{message_id}", data=data)
    _echo(res, ctx.obj["raw"])


@messages.command("delete")
@click.argument("message_id", type=int)
@click.pass_context
def messages_delete(ctx: click.Context, message_id: int) -> None:
    client: ZulipClient = ctx.obj["client"]
    res = client.request("DELETE", f"/messages/{message_id}")
    _echo(res, ctx.obj["raw"])


@messages.command("flags")
@click.option("--messages", "message_ids", required=True, help="Comma-separated message IDs")
@click.option("--op", "op", type=click.Choice(["add", "remove"], case_sensitive=False), required=True)
@click.option("--flag", "flag", required=True)
@click.pass_context
def messages_flags(ctx: click.Context, message_ids: str, op: str, flag: str) -> None:
    client: ZulipClient = ctx.obj["client"]
    ids = [int(x) for x in message_ids.split(",") if x.strip()]
    data = {"messages": json.dumps(ids), "op": op, "flag": flag}
    res = client.request("POST", "/messages/flags", data=data)
    _echo(res, ctx.obj["raw"])


@messages.command("reaction-add")
@click.argument("message_id", type=int)
@click.option("--emoji-name", required=True)
@click.option("--emoji-code")
@click.option("--reaction-type")
@click.pass_context
def reaction_add(ctx: click.Context, message_id: int, emoji_name: str, emoji_code: Optional[str], reaction_type: Optional[str]) -> None:
    client: ZulipClient = ctx.obj["client"]
    data: Dict[str, Any] = {"emoji_name": emoji_name}
    if emoji_code:
        data["emoji_code"] = emoji_code
    if reaction_type:
        data["reaction_type"] = reaction_type
    res = client.request("POST", f"/messages/{message_id}/reactions", data=data)
    _echo(res, ctx.obj["raw"])


@messages.command("reaction-remove")
@click.argument("message_id", type=int)
@click.option("--emoji-name", required=True)
@click.option("--emoji-code")
@click.option("--reaction-type")
@click.pass_context
def reaction_remove(ctx: click.Context, message_id: int, emoji_name: str, emoji_code: Optional[str], reaction_type: Optional[str]) -> None:
    client: ZulipClient = ctx.obj["client"]
    data: Dict[str, Any] = {"emoji_name": emoji_name}
    if emoji_code:
        data["emoji_code"] = emoji_code
    if reaction_type:
        data["reaction_type"] = reaction_type
    res = client.request("DELETE", f"/messages/{message_id}/reactions", data=data)
    _echo(res, ctx.obj["raw"])


@cli.group()
def streams() -> None:
    """Stream/channel operations."""


@streams.command("list")
@click.pass_context
def streams_list(ctx: click.Context) -> None:
    client: ZulipClient = ctx.obj["client"]
    res = client.request("GET", "/streams")
    _echo(res, ctx.obj["raw"])


@streams.command("create")
@click.option("--name", required=True)
@click.option("--description", default="")
@click.option("--is-private", is_flag=True)
@click.pass_context
def streams_create(ctx: click.Context, name: str, description: str, is_private: bool) -> None:
    client: ZulipClient = ctx.obj["client"]
    data = {"name": name, "description": description, "is_private": json.dumps(is_private)}
    res = client.request("POST", "/users/me/subscriptions", data=data)
    _echo(res, ctx.obj["raw"])


@streams.command("subscribe")
@click.option("--streams", required=True, help="JSON list of stream objects, e.g. '[{""name"":""general""}]'")
@click.pass_context
def streams_subscribe(ctx: click.Context, streams: str) -> None:
    client: ZulipClient = ctx.obj["client"]
    data = {"subscriptions": streams}
    res = client.request("POST", "/users/me/subscriptions", data=data)
    _echo(res, ctx.obj["raw"])


@cli.group()
def users() -> None:
    """User operations."""


@users.command("me")
@click.pass_context
def users_me(ctx: click.Context) -> None:
    client: ZulipClient = ctx.obj["client"]
    res = client.request("GET", "/users/me")
    _echo(res, ctx.obj["raw"])


@users.command("list")
@click.option("--client-gravatar", is_flag=True)
@click.option("--include-custom-profile-fields", is_flag=True)
@click.pass_context
def users_list(ctx: click.Context, client_gravatar: bool, include_custom_profile_fields: bool) -> None:
    client: ZulipClient = ctx.obj["client"]
    params = {
        "client_gravatar": json.dumps(client_gravatar),
        "include_custom_profile_fields": json.dumps(include_custom_profile_fields),
    }
    res = client.request("GET", "/users", params=params)
    _echo(res, ctx.obj["raw"])


@users.command("presence")
@click.argument("user", required=True)
@click.pass_context
def users_presence(ctx: click.Context, user: str) -> None:
    client: ZulipClient = ctx.obj["client"]
    res = client.request("GET", f"/users/{user}/presence")
    _echo(res, ctx.obj["raw"])


@cli.group()
def scheduled() -> None:
    """Scheduled messages."""


@scheduled.command("list")
@click.pass_context
def scheduled_list(ctx: click.Context) -> None:
    client: ZulipClient = ctx.obj["client"]
    res = client.request("GET", "/scheduled_messages")
    _echo(res, ctx.obj["raw"])


@scheduled.command("create")
@click.option("--type", "msg_type", type=click.Choice(["stream", "private"], case_sensitive=False), required=True)
@click.option("--to", required=True)
@click.option("--topic")
@click.option("--content", required=True)
@click.option("--scheduled-delivery-timestamp", required=True, type=int)
@click.pass_context
def scheduled_create(ctx: click.Context, msg_type: str, to: str, topic: Optional[str], content: str, scheduled_delivery_timestamp: int) -> None:
    client: ZulipClient = ctx.obj["client"]
    data: Dict[str, Any] = {
        "type": msg_type,
        "to": to,
        "content": content,
        "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
    }
    if msg_type.lower() == "stream":
        if not topic:
            raise click.ClickException("--topic is required for stream messages")
        data["topic"] = topic
    res = client.request("POST", "/scheduled_messages", data=data)
    _echo(res, ctx.obj["raw"])


@scheduled.command("delete")
@click.argument("scheduled_message_id", type=int)
@click.pass_context
def scheduled_delete(ctx: click.Context, scheduled_message_id: int) -> None:
    client: ZulipClient = ctx.obj["client"]
    res = client.request("DELETE", f"/scheduled_messages/{scheduled_message_id}")
    _echo(res, ctx.obj["raw"])


@cli.group()
def drafts() -> None:
    """Drafts."""


@drafts.command("list")
@click.pass_context
def drafts_list(ctx: click.Context) -> None:
    client: ZulipClient = ctx.obj["client"]
    res = client.request("GET", "/drafts")
    _echo(res, ctx.obj["raw"])


@drafts.command("create")
@click.option("--drafts", required=True, help="JSON list of draft objects")
@click.pass_context
def drafts_create(ctx: click.Context, drafts: str) -> None:
    client: ZulipClient = ctx.obj["client"]
    data = {"drafts": drafts}
    res = client.request("POST", "/drafts", data=data)
    _echo(res, ctx.obj["raw"])


@drafts.command("delete")
@click.argument("draft_id", type=int)
@click.pass_context
def drafts_delete(ctx: click.Context, draft_id: int) -> None:
    client: ZulipClient = ctx.obj["client"]
    res = client.request("DELETE", f"/drafts/{draft_id}")
    _echo(res, ctx.obj["raw"])


@cli.group()
def alert_words() -> None:
    """Alert words."""


@alert_words.command("list")
@click.pass_context
def alert_words_list(ctx: click.Context) -> None:
    client: ZulipClient = ctx.obj["client"]
    res = client.request("GET", "/users/me/alert_words")
    _echo(res, ctx.obj["raw"])


@alert_words.command("add")
@click.option("--word", required=True)
@click.pass_context
def alert_words_add(ctx: click.Context, word: str) -> None:
    client: ZulipClient = ctx.obj["client"]
    res = client.request("POST", "/users/me/alert_words", data={"alert_words": json.dumps([word])})
    _echo(res, ctx.obj["raw"])


@alert_words.command("remove")
@click.option("--word", required=True)
@click.pass_context
def alert_words_remove(ctx: click.Context, word: str) -> None:
    client: ZulipClient = ctx.obj["client"]
    res = client.request("DELETE", "/users/me/alert_words", data={"alert_word": word})
    _echo(res, ctx.obj["raw"])


if __name__ == "__main__":
    cli()
