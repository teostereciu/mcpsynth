#!/usr/bin/env python3
import json
import os
import sys
from dataclasses import dataclass
from typing import Any, Dict, Optional

import click
import requests


@dataclass
class ZulipClient:
    site: str
    email: str
    api_key: str

    @property
    def base_url(self) -> str:
        return self.site.rstrip("/") + "/api/v1"

    def request(self, method: str, path: str, *, params: Optional[Dict[str, Any]] = None, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = self.base_url + ("/" + path.lstrip("/"))
        resp = requests.request(
            method,
            url,
            params=params,
            data=data,
            auth=(self.email, self.api_key),
            headers={"User-Agent": "zulip-cli"},
            timeout=60,
        )
        try:
            payload = resp.json()
        except Exception:
            resp.raise_for_status()
            raise
        if resp.status_code >= 400:
            # Zulip returns JSON errors with msg/code
            raise click.ClickException(json.dumps(payload, indent=2, sort_keys=True))
        return payload


def get_client() -> ZulipClient:
    site = os.environ.get("ZULIP_SITE")
    email = os.environ.get("ZULIP_EMAIL")
    api_key = os.environ.get("ZULIP_API_KEY")
    missing = [k for k, v in [("ZULIP_SITE", site), ("ZULIP_EMAIL", email), ("ZULIP_API_KEY", api_key)] if not v]
    if missing:
        raise click.ClickException(f"Missing env vars: {', '.join(missing)}")
    return ZulipClient(site=site, email=email, api_key=api_key)


def echo_json(obj: Any) -> None:
    click.echo(json.dumps(obj, indent=2, sort_keys=True))


@click.group()
def cli() -> None:
    """Zulip CLI (API v1). Auth via env: ZULIP_SITE, ZULIP_EMAIL, ZULIP_API_KEY."""


@cli.group()
def messages() -> None:
    """Message operations."""


@messages.command("send")
@click.option("--type", "msg_type", type=click.Choice(["stream", "private"], case_sensitive=False), required=True)
@click.option("--to", required=True, help="Stream name/id (stream) or comma-separated emails/user_ids (private)")
@click.option("--topic", required=False, help="Topic (required for stream messages)")
@click.option("--content", required=True)
def messages_send(msg_type: str, to: str, topic: Optional[str], content: str) -> None:
    c = get_client()
    data: Dict[str, Any] = {"type": msg_type, "content": content}
    if msg_type == "stream":
        if not topic:
            raise click.ClickException("--topic is required for stream messages")
        data["to"] = to
        data["topic"] = topic
    else:
        # Zulip expects JSON array for private recipients; accept comma-separated
        recips = [x.strip() for x in to.split(",") if x.strip()]
        data["to"] = json.dumps(recips)
    echo_json(c.request("POST", "/messages", data=data))


@messages.command("get")
@click.option("--anchor", default="newest")
@click.option("--num-before", type=int, default=50)
@click.option("--num-after", type=int, default=0)
@click.option("--narrow", required=False, help="JSON narrow array")
@click.option("--apply-markdown/--no-apply-markdown", default=True)
def messages_get(anchor: str, num_before: int, num_after: int, narrow: Optional[str], apply_markdown: bool) -> None:
    c = get_client()
    params: Dict[str, Any] = {
        "anchor": anchor,
        "num_before": num_before,
        "num_after": num_after,
        "apply_markdown": json.dumps(apply_markdown),
    }
    if narrow:
        params["narrow"] = narrow
    echo_json(c.request("GET", "/messages", params=params))


@messages.command("edit")
@click.argument("message_id", type=int)
@click.option("--content")
@click.option("--topic")
@click.option("--propagate-mode", type=click.Choice(["change_one", "change_later", "change_all"], case_sensitive=False))
def messages_edit(message_id: int, content: Optional[str], topic: Optional[str], propagate_mode: Optional[str]) -> None:
    if not content and not topic:
        raise click.ClickException("Provide --content and/or --topic")
    c = get_client()
    data: Dict[str, Any] = {}
    if content is not None:
        data["content"] = content
    if topic is not None:
        data["topic"] = topic
    if propagate_mode is not None:
        data["propagate_mode"] = propagate_mode
    echo_json(c.request("PATCH", f"/messages/{message_id}", data=data))


@messages.command("delete")
@click.argument("message_id", type=int)
def messages_delete(message_id: int) -> None:
    c = get_client()
    echo_json(c.request("DELETE", f"/messages/{message_id}"))


@messages.command("history")
@click.argument("message_id", type=int)
def messages_history(message_id: int) -> None:
    c = get_client()
    echo_json(c.request("GET", f"/messages/{message_id}/history"))


@messages.command("flags")
@click.option("--messages", "message_ids", required=True, help="Comma-separated message IDs")
@click.option("--op", type=click.Choice(["add", "remove"], case_sensitive=False), required=True)
@click.option("--flag", "flag_name", required=True)
def messages_flags(message_ids: str, op: str, flag_name: str) -> None:
    c = get_client()
    ids = [int(x) for x in message_ids.split(",") if x.strip()]
    data = {"messages": json.dumps(ids), "op": op, "flag": flag_name}
    echo_json(c.request("POST", "/messages/flags", data=data))


@messages.command("reaction-add")
@click.argument("message_id", type=int)
@click.option("--emoji-name", required=True)
@click.option("--emoji-code")
@click.option("--reaction-type")
def messages_reaction_add(message_id: int, emoji_name: str, emoji_code: Optional[str], reaction_type: Optional[str]) -> None:
    c = get_client()
    data: Dict[str, Any] = {"emoji_name": emoji_name}
    if emoji_code:
        data["emoji_code"] = emoji_code
    if reaction_type:
        data["reaction_type"] = reaction_type
    echo_json(c.request("POST", f"/messages/{message_id}/reactions", data=data))


@messages.command("reaction-remove")
@click.argument("message_id", type=int)
@click.option("--emoji-name", required=True)
@click.option("--emoji-code")
@click.option("--reaction-type")
def messages_reaction_remove(message_id: int, emoji_name: str, emoji_code: Optional[str], reaction_type: Optional[str]) -> None:
    c = get_client()
    data: Dict[str, Any] = {"emoji_name": emoji_name}
    if emoji_code:
        data["emoji_code"] = emoji_code
    if reaction_type:
        data["reaction_type"] = reaction_type
    echo_json(c.request("DELETE", f"/messages/{message_id}/reactions", data=data))


@cli.group()
def streams() -> None:
    """Stream/channel operations."""


@streams.command("list")
@click.option("--include-public/--no-include-public", default=True)
@click.option("--include-subscribed/--no-include-subscribed", default=True)
@click.option("--include-all-active/--no-include-all-active", default=False)
def streams_list(include_public: bool, include_subscribed: bool, include_all_active: bool) -> None:
    c = get_client()
    params = {
        "include_public": json.dumps(include_public),
        "include_subscribed": json.dumps(include_subscribed),
        "include_all_active": json.dumps(include_all_active),
    }
    echo_json(c.request("GET", "/streams", params=params))


@streams.command("subscribed")
def streams_subscribed() -> None:
    c = get_client()
    echo_json(c.request("GET", "/users/me/subscriptions"))


@streams.command("create")
@click.option("--name", required=True)
@click.option("--description", default="")
@click.option("--is-private/--is-public", default=False)
def streams_create(name: str, description: str, is_private: bool) -> None:
    c = get_client()
    stream = {"name": name, "description": description, "invite_only": is_private}
    data = {"subscriptions": json.dumps([stream])}
    echo_json(c.request("POST", "/users/me/subscriptions", data=data))


@streams.command("subscribe")
@click.option("--name", required=True, help="Stream name")
@click.option("--principals", required=False, help="JSON list of user_ids/emails to subscribe")
def streams_subscribe(name: str, principals: Optional[str]) -> None:
    c = get_client()
    data: Dict[str, Any] = {"subscriptions": json.dumps([{"name": name}])}
    if principals:
        data["principals"] = principals
    echo_json(c.request("POST", "/users/me/subscriptions", data=data))


@streams.command("unsubscribe")
@click.option("--name", required=True, help="Stream name")
def streams_unsubscribe(name: str) -> None:
    c = get_client()
    data = {"subscriptions": json.dumps([name])}
    echo_json(c.request("DELETE", "/users/me/subscriptions", data=data))


@streams.command("update")
@click.option("--stream-id", type=int, required=True)
@click.option("--new-name")
@click.option("--description")
@click.option("--is-private/--is-public", default=None)
def streams_update(stream_id: int, new_name: Optional[str], description: Optional[str], is_private: Optional[bool]) -> None:
    if new_name is None and description is None and is_private is None:
        raise click.ClickException("Provide --new-name and/or --description and/or --is-private/--is-public")
    c = get_client()
    data: Dict[str, Any] = {}
    if new_name is not None:
        data["new_name"] = new_name
    if description is not None:
        data["description"] = description
    if is_private is not None:
        data["is_private"] = json.dumps(is_private)
    echo_json(c.request("PATCH", f"/streams/{stream_id}", data=data))


@streams.command("topics")
@click.option("--stream-id", type=int, required=True)
def streams_topics(stream_id: int) -> None:
    c = get_client()
    echo_json(c.request("GET", f"/users/me/{stream_id}/topics"))


@cli.group()
def users() -> None:
    """User operations."""


@users.command("me")
def users_me() -> None:
    c = get_client()
    echo_json(c.request("GET", "/users/me"))


@users.command("list")
@click.option("--client-gravatar/--no-client-gravatar", default=False)
@click.option("--include-custom-profile-fields/--no-include-custom-profile-fields", default=False)
def users_list(client_gravatar: bool, include_custom_profile_fields: bool) -> None:
    c = get_client()
    params = {
        "client_gravatar": json.dumps(client_gravatar),
        "include_custom_profile_fields": json.dumps(include_custom_profile_fields),
    }
    echo_json(c.request("GET", "/users", params=params))


@users.command("presence")
@click.argument("user_id_or_email")
def users_presence(user_id_or_email: str) -> None:
    c = get_client()
    echo_json(c.request("GET", f"/users/{user_id_or_email}/presence"))


@cli.group()
def scheduled() -> None:
    """Scheduled messages."""


@scheduled.command("list")
def scheduled_list() -> None:
    c = get_client()
    echo_json(c.request("GET", "/scheduled_messages"))


@scheduled.command("create")
@click.option("--type", "msg_type", type=click.Choice(["stream", "private"], case_sensitive=False), required=True)
@click.option("--to", required=True)
@click.option("--topic", required=False)
@click.option("--content", required=True)
@click.option("--scheduled-delivery-timestamp", type=int, required=True)
def scheduled_create(msg_type: str, to: str, topic: Optional[str], content: str, scheduled_delivery_timestamp: int) -> None:
    c = get_client()
    data: Dict[str, Any] = {
        "type": msg_type,
        "content": content,
        "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
    }
    if msg_type == "stream":
        if not topic:
            raise click.ClickException("--topic is required for stream messages")
        data["to"] = to
        data["topic"] = topic
    else:
        recips = [x.strip() for x in to.split(",") if x.strip()]
        data["to"] = json.dumps(recips)
    echo_json(c.request("POST", "/scheduled_messages", data=data))


@scheduled.command("update")
@click.argument("scheduled_message_id", type=int)
@click.option("--scheduled-delivery-timestamp", type=int, required=True)
def scheduled_update(scheduled_message_id: int, scheduled_delivery_timestamp: int) -> None:
    c = get_client()
    data = {"scheduled_delivery_timestamp": scheduled_delivery_timestamp}
    echo_json(c.request("PATCH", f"/scheduled_messages/{scheduled_message_id}", data=data))


@scheduled.command("delete")
@click.argument("scheduled_message_id", type=int)
def scheduled_delete(scheduled_message_id: int) -> None:
    c = get_client()
    echo_json(c.request("DELETE", f"/scheduled_messages/{scheduled_message_id}"))


@cli.group()
def drafts() -> None:
    """Drafts."""


@drafts.command("list")
def drafts_list() -> None:
    c = get_client()
    echo_json(c.request("GET", "/drafts"))


@drafts.command("create")
@click.option("--drafts", required=True, help="JSON list of draft objects")
def drafts_create(drafts: str) -> None:
    c = get_client()
    data = {"drafts": drafts}
    echo_json(c.request("POST", "/drafts", data=data))


@drafts.command("edit")
@click.argument("draft_id", type=int)
@click.option("--draft", required=True, help="JSON draft object")
def drafts_edit(draft_id: int, draft: str) -> None:
    c = get_client()
    data = {"draft": draft}
    echo_json(c.request("PATCH", f"/drafts/{draft_id}", data=data))


@drafts.command("delete")
@click.argument("draft_id", type=int)
def drafts_delete(draft_id: int) -> None:
    c = get_client()
    echo_json(c.request("DELETE", f"/drafts/{draft_id}"))


@cli.group()
def alert_words() -> None:
    """Alert words."""


@alert_words.command("list")
def alert_words_list() -> None:
    c = get_client()
    echo_json(c.request("GET", "/users/me/alert_words"))


@alert_words.command("add")
@click.option("--word", required=True)
def alert_words_add(word: str) -> None:
    c = get_client()
    echo_json(c.request("POST", "/users/me/alert_words", data={"alert_words": json.dumps([word])}))


@alert_words.command("remove")
@click.option("--word", required=True)
def alert_words_remove(word: str) -> None:
    c = get_client()
    echo_json(c.request("DELETE", "/users/me/alert_words", data={"alert_words": json.dumps([word])}))


def main() -> None:
    cli(standalone_mode=True)


if __name__ == "__main__":
    main()
