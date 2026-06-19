#!/usr/bin/env python3
"""
Zulip CLI — human reference implementation (upper bound for the CLI synthesis benchmark).

All output is JSON to stdout so the eval agent can parse it programmatically.
Auth is read from environment variables: ZULIP_EMAIL, ZULIP_API_KEY, ZULIP_SITE.

Usage:
    python zulip_cli.py --help
    python zulip_cli.py <subcommand> --help
    python zulip_cli.py list-streams
    python zulip_cli.py send-message --stream general --topic test --content "hello"
"""

import argparse
import json
import os
import sys
import time

import requests


# ---------------------------------------------------------------------------
# Auth / HTTP helpers
# ---------------------------------------------------------------------------

def _client():
    site = os.environ.get("ZULIP_SITE", "").rstrip("/")
    email = os.environ.get("ZULIP_EMAIL", "")
    api_key = os.environ.get("ZULIP_API_KEY", "")
    if not (site and email and api_key):
        _out({"error": "Missing env vars: ZULIP_SITE, ZULIP_EMAIL, ZULIP_API_KEY"})
        sys.exit(1)
    return site, (email, api_key)


def _get(path, params=None):
    site, auth = _client()
    r = requests.get(f"{site}/api/v1/{path}", auth=auth, params=params or {})
    return r.json()


def _post(path, data=None):
    site, auth = _client()
    r = requests.post(f"{site}/api/v1/{path}", auth=auth, data=data or {})
    return r.json()


def _patch(path, data=None):
    site, auth = _client()
    r = requests.patch(f"{site}/api/v1/{path}", auth=auth, data=data or {})
    return r.json()


def _delete(path, data=None):
    site, auth = _client()
    r = requests.delete(f"{site}/api/v1/{path}", auth=auth, data=data or {})
    return r.json()


def _out(obj):
    print(json.dumps(obj, ensure_ascii=False))


# ---------------------------------------------------------------------------
# Subcommand handlers
# ---------------------------------------------------------------------------

def cmd_list_streams(args):
    _out(_get("streams", {"include_subscribed": "true", "include_all_active": "true"}))


def cmd_get_profile(args):
    _out(_get("users/me"))


def cmd_list_users(args):
    _out(_get("users"))


def cmd_get_server_settings(args):
    _out(_get("server_settings"))


def cmd_get_stream_id(args):
    _out(_get("get_stream_id", {"stream": args.stream}))


def cmd_get_stream_subscribers(args):
    r = _get("get_stream_id", {"stream": args.stream})
    if r.get("result") != "success":
        _out(r)
        return
    stream_id = r["stream_id"]
    _out(_get(f"streams/{stream_id}/members"))


def cmd_get_topics(args):
    r = _get("get_stream_id", {"stream": args.stream})
    if r.get("result") != "success":
        _out(r)
        return
    stream_id = r["stream_id"]
    _out(_get(f"users/me/{stream_id}/topics"))


def cmd_get_messages(args):
    narrow = []
    if args.stream:
        narrow.append({"operator": "channel", "operand": args.stream})
    if args.topic:
        narrow.append({"operator": "topic", "operand": args.topic})
    if args.sender:
        narrow.append({"operator": "sender", "operand": args.sender})
    if args.is_:
        narrow.append({"operator": "is", "operand": args.is_})

    params = {
        "num_before": args.num_before,
        "num_after": args.num_after,
        "anchor": args.anchor,
        "apply_markdown": "false",
    }
    if narrow:
        params["narrow"] = json.dumps(narrow)

    _out(_get("messages", params))


def cmd_send_message(args):
    data = {
        "type": args.type,
        "content": args.content,
    }
    if args.type == "stream":
        data["to"] = args.stream
        data["topic"] = args.topic
    else:
        data["to"] = json.dumps(args.to) if args.to else "[]"
    _out(_post("messages", data))


def cmd_edit_message(args):
    data = {}
    if args.content is not None:
        data["content"] = args.content
    if args.topic is not None:
        data["topic"] = args.topic
    if args.stream_id is not None:
        data["stream_id"] = args.stream_id
    if args.propagate_mode is not None:
        data["propagate_mode"] = args.propagate_mode
    _out(_patch(f"messages/{args.message_id}", data))


def cmd_delete_message(args):
    _out(_delete(f"messages/{args.message_id}"))


def cmd_get_message_history(args):
    _out(_get(f"messages/{args.message_id}/history"))


def cmd_update_message_flags(args):
    _out(_post("messages/flags", {
        "messages": json.dumps(args.messages),
        "op": args.op,
        "flag": args.flag,
    }))


def cmd_add_reaction(args):
    _out(_post(f"messages/{args.message_id}/reactions", {
        "emoji_name": args.emoji_name,
    }))


def cmd_add_scheduled_message(args):
    data = {
        "type": "stream",
        "to": args.stream,
        "topic": args.topic,
        "content": args.content,
        "scheduled_delivery_timestamp": int(time.time()) + int(args.deliver_in),
    }
    _out(_post("scheduled_messages", data))


def cmd_list_scheduled_messages(args):
    _out(_get("scheduled_messages"))


def cmd_create_stream(args):
    subscriptions = [{"name": args.name, "description": args.description or ""}]
    data = {
        "subscriptions": json.dumps(subscriptions),
        "invite_only": "true" if args.private else "false",
    }
    _out(_post("users/me/subscriptions", data))


def cmd_update_stream(args):
    r = _get("get_stream_id", {"stream": args.stream})
    if r.get("result") != "success":
        _out(r)
        return
    stream_id = r["stream_id"]
    data = {}
    if args.description is not None:
        data["description"] = json.dumps(args.description)
    if args.new_name is not None:
        data["new_name"] = json.dumps(args.new_name)
    _out(_patch(f"streams/{stream_id}", data))


def cmd_get_alert_words(args):
    _out(_get("users/me/alert_words"))


def cmd_add_alert_words(args):
    _out(_post("users/me/alert_words", {"alert_words": json.dumps(args.words)}))


def cmd_get_drafts(args):
    _out(_get("drafts"))


def cmd_get_presence(args):
    _out(_get(f"users/{args.email}/presence"))


# ---------------------------------------------------------------------------
# CLI wiring
# ---------------------------------------------------------------------------

def build_parser():
    parser = argparse.ArgumentParser(
        prog="zulip_cli.py",
        description="Zulip CLI — interact with the Zulip API. All output is JSON.",
    )
    sub = parser.add_subparsers(dest="subcommand", metavar="<subcommand>")
    sub.required = True

    # list-streams
    sub.add_parser("list-streams", help="List all streams in the organization")

    # get-profile
    sub.add_parser("get-profile", help="Get your own user profile")

    # list-users
    sub.add_parser("list-users", help="List all users in the organization")

    # get-server-settings
    sub.add_parser("get-server-settings", help="Get server/realm settings")

    # get-stream-id
    p = sub.add_parser("get-stream-id", help="Get the numeric ID of a stream by name")
    p.add_argument("--stream", required=True)

    # get-stream-subscribers
    p = sub.add_parser("get-stream-subscribers", help="List subscribers of a stream")
    p.add_argument("--stream", required=True)

    # get-topics
    p = sub.add_parser("get-topics", help="List topics in a stream")
    p.add_argument("--stream", required=True)

    # get-messages
    p = sub.add_parser("get-messages", help="Fetch messages with optional filters")
    p.add_argument("--stream", default=None)
    p.add_argument("--topic", default=None)
    p.add_argument("--sender", default=None, help="Filter by sender email")
    p.add_argument("--is", dest="is_", default=None, help="'is' narrow operand (e.g. starred)")
    p.add_argument("--anchor", default="newest")
    p.add_argument("--num-before", type=int, default=20, dest="num_before")
    p.add_argument("--num-after", type=int, default=0, dest="num_after")

    # send-message
    p = sub.add_parser("send-message", help="Send a stream or direct message")
    p.add_argument("--type", choices=["stream", "direct"], default="stream")
    p.add_argument("--stream", default=None, help="Target stream (for stream messages)")
    p.add_argument("--topic", default=None, help="Topic (for stream messages)")
    p.add_argument("--to", nargs="+", default=None, help="Recipient emails (for direct messages)")
    p.add_argument("--content", required=True)

    # edit-message
    p = sub.add_parser("edit-message", help="Edit a message's content and/or topic")
    p.add_argument("--message-id", required=True, dest="message_id", type=int)
    p.add_argument("--content", default=None)
    p.add_argument("--topic", default=None)
    p.add_argument("--stream-id", default=None, dest="stream_id", type=int, help="Move to stream")
    p.add_argument("--propagate-mode", default=None, dest="propagate_mode",
                   choices=["change_one", "change_later", "change_all"])

    # delete-message
    p = sub.add_parser("delete-message", help="Delete a message by ID")
    p.add_argument("--message-id", required=True, dest="message_id", type=int)

    # get-message-history
    p = sub.add_parser("get-message-history", help="Get edit history of a message")
    p.add_argument("--message-id", required=True, dest="message_id", type=int)

    # update-message-flags
    p = sub.add_parser("update-message-flags", help="Add or remove a flag on messages")
    p.add_argument("--messages", nargs="+", type=int, required=True)
    p.add_argument("--op", choices=["add", "remove"], required=True)
    p.add_argument("--flag", required=True, help="e.g. starred, read")

    # add-reaction
    p = sub.add_parser("add-reaction", help="Add an emoji reaction to a message")
    p.add_argument("--message-id", required=True, dest="message_id", type=int)
    p.add_argument("--emoji-name", required=True, dest="emoji_name")

    # add-scheduled-message
    p = sub.add_parser("add-scheduled-message", help="Schedule a message for future delivery")
    p.add_argument("--stream", required=True)
    p.add_argument("--topic", required=True)
    p.add_argument("--content", required=True)
    p.add_argument("--deliver-in", required=True, dest="deliver_in",
                   help="Seconds from now to deliver the message")

    # list-scheduled-messages
    sub.add_parser("list-scheduled-messages", help="List pending scheduled messages")

    # create-stream
    p = sub.add_parser("create-stream", help="Create a new stream")
    p.add_argument("--name", required=True)
    p.add_argument("--description", default="")
    p.add_argument("--private", action="store_true", help="Make the stream private")

    # update-stream
    p = sub.add_parser("update-stream", help="Update stream properties")
    p.add_argument("--stream", required=True, help="Current stream name")
    p.add_argument("--description", default=None)
    p.add_argument("--new-name", default=None, dest="new_name")

    # get-alert-words
    sub.add_parser("get-alert-words", help="List your alert words")

    # add-alert-words
    p = sub.add_parser("add-alert-words", help="Add alert words")
    p.add_argument("--words", nargs="+", required=True)

    # get-drafts
    sub.add_parser("get-drafts", help="List your message drafts")

    # get-presence
    p = sub.add_parser("get-presence", help="Get presence status of a user")
    p.add_argument("--email", required=True)

    return parser


_HANDLERS = {
    "list-streams": cmd_list_streams,
    "get-profile": cmd_get_profile,
    "list-users": cmd_list_users,
    "get-server-settings": cmd_get_server_settings,
    "get-stream-id": cmd_get_stream_id,
    "get-stream-subscribers": cmd_get_stream_subscribers,
    "get-topics": cmd_get_topics,
    "get-messages": cmd_get_messages,
    "send-message": cmd_send_message,
    "edit-message": cmd_edit_message,
    "delete-message": cmd_delete_message,
    "get-message-history": cmd_get_message_history,
    "update-message-flags": cmd_update_message_flags,
    "add-reaction": cmd_add_reaction,
    "add-scheduled-message": cmd_add_scheduled_message,
    "list-scheduled-messages": cmd_list_scheduled_messages,
    "create-stream": cmd_create_stream,
    "update-stream": cmd_update_stream,
    "get-alert-words": cmd_get_alert_words,
    "add-alert-words": cmd_add_alert_words,
    "get-drafts": cmd_get_drafts,
    "get-presence": cmd_get_presence,
}


def main():
    parser = build_parser()
    args = parser.parse_args()
    handler = _HANDLERS.get(args.subcommand)
    if handler is None:
        _out({"error": f"Unknown subcommand: {args.subcommand!r}"})
        sys.exit(1)
    try:
        handler(args)
    except Exception as e:
        _out({"error": str(e)})
        sys.exit(1)


if __name__ == "__main__":
    main()
