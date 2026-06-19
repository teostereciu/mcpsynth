"""
Zulip CLI tool.
"""

import argparse
import os
import json
import sys

import requests
from dotenv import load_dotenv

load_dotenv()

ZULIP_EMAIL = os.environ.get("ZULIP_EMAIL")
ZULIP_API_KEY = os.environ.get("ZULIP_API_KEY")
ZULIP_SITE = os.environ.get("ZULIP_SITE")

if not all([ZULIP_EMAIL, ZULIP_API_KEY, ZULIP_SITE]):
    print("Error: ZULIP_EMAIL, ZULIP_API_KEY, and ZULIP_SITE environment variables must be set.")
    sys.exit(1)

BASE_URL = f"{ZULIP_SITE}/api/v1"


def call_api(method, endpoint, **kwargs):
    """
    Make an API call to the Zulip server.
    """
    url = f"{BASE_URL}/{endpoint}"
    auth = (ZULIP_EMAIL, ZULIP_API_KEY)
    try:
        response = requests.request(method, url, auth=auth, **kwargs)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
        sys.exit(1)


def get_stream_id(stream_name):
    """
    Get the ID of a stream from its name.
    """
    result = call_api("GET", "streams")
    for stream in result.get("streams", []):
        if stream["name"] == stream_name:
            return stream["stream_id"]
    print(f"Error: Stream '{stream_name}' not found.")
    sys.exit(1)


def main():
    """
    Main function for the Zulip CLI tool.
    """
    parser = argparse.ArgumentParser(description="Zulip CLI tool.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Messages
    messages_parser = subparsers.add_parser("messages", help="Manage messages.")
    messages_subparsers = messages_parser.add_subparsers(dest="subcommand", required=True)

    # Send a message
    send_message_parser = messages_subparsers.add_parser("send", help="Send a message.")
    send_message_parser.add_argument("--type", required=True, choices=["private", "stream"], help="The type of message to send.")
    send_message_parser.add_argument("--to", required=True, help="The recipient of the message.")
    send_message_parser.add_argument("--content", required=True, help="The content of the message.")
    send_message_parser.add_argument("--topic", help="The topic of the message (for stream messages).")

    # Edit a message
    edit_message_parser = messages_subparsers.add_parser("edit", help="Edit a message.")
    edit_message_parser.add_argument("--message-id", required=True, type=int, help="The ID of the message to edit.")
    edit_message_parser.add_argument("--content", required=True, help="The new content of the message.")
    edit_message_parser.add_argument("--topic", help="The new topic of the message.")

    # Delete a message
    delete_message_parser = messages_subparsers.add_parser("delete", help="Delete a message.")
    delete_message_parser.add_argument("--message-id", required=True, type=int, help="The ID of the message to delete.")

    # Fetch a message
    fetch_message_parser = messages_subparsers.add_parser("fetch", help="Fetch a message.")
    fetch_message_parser.add_argument("--message-id", required=True, type=int, help="The ID of the message to fetch.")

    # Add/remove flags
    flags_parser = messages_subparsers.add_parser("flags", help="Add or remove flags from messages.")
    flags_parser.add_argument("--message-ids", required=True, help="Comma-separated list of message IDs.")
    flags_parser.add_argument("--op", required=True, choices=["add", "remove"], help="Whether to add or remove the flag.")
    flags_parser.add_argument("--flag", required=True, help="The flag to add or remove.")

    # Get message history
    history_parser = messages_subparsers.add_parser("history", help="Get the edit history of a message.")
    history_parser.add_argument("--message-id", required=True, type=int, help="The ID of the message to get the history of.")

    # Reactions
    reactions_parser = subparsers.add_parser("reactions", help="Manage reactions to a message.")
    reactions_subparsers = reactions_parser.add_subparsers(dest="subcommand", required=True)

    # Add a reaction
    add_reaction_parser = reactions_subparsers.add_parser("add", help="Add a reaction to a message.")
    add_reaction_parser.add_argument("--message-id", required=True, type=int, help="The ID of the message to react to.")
    add_reaction_parser.add_argument("--emoji-name", required=True, help="The name of the emoji to react with.")

    # Remove a reaction
    remove_reaction_parser = reactions_subparsers.add_parser("remove", help="Remove a reaction from a message.")
    remove_reaction_parser.add_argument("--message-id", required=True, type=int, help="The ID of the message to remove the reaction from.")
    remove_reaction_parser.add_argument("--emoji-name", required=True, help="The name of the emoji to remove.")

    # Streams
    streams_parser = subparsers.add_parser("streams", help="Manage streams.")
    streams_subparsers = streams_parser.add_subparsers(dest="subcommand", required=True)

    # Create a stream
    create_stream_parser = streams_subparsers.add_parser("create", help="Create a stream.")
    create_stream_parser.add_argument("--name", required=True, help="The name of the stream.")
    create_stream_parser.add_argument("--description", default="", help="The description of the stream.")
    create_stream_parser.add_argument("--private", action="store_true", help="Whether the stream should be private.")

    # List streams
    list_streams_parser = streams_subparsers.add_parser("list", help="List streams.")

    # Subscribe to a stream
    subscribe_stream_parser = streams_subparsers.add_parser("subscribe", help="Subscribe to a stream.")
    subscribe_stream_parser.add_argument("--streams", required=True, help="Comma-separated list of stream names to subscribe to.")

    # Update a stream
    update_stream_parser = streams_subparsers.add_parser("update", help="Update a stream.")
    update_stream_parser.add_argument("--stream-name", required=True, help="The name of the stream to update.")
    update_stream_parser.add_argument("--new-name", help="The new name of the stream.")
    update_stream_parser.add_argument("--new-description", help="The new description of the stream.")

    # Get stream topics
    topics_parser = streams_subparsers.add_parser("topics", help="Get topics in a stream.")
    topics_parser.add_argument("--stream-name", required=True, help="The name of the stream.")

    # Users
    users_parser = subparsers.add_parser("users", help="Manage users.")
    users_subparsers = users_parser.add_subparsers(dest="subcommand", required=True)

    # Get user profile
    get_user_parser = users_subparsers.add_parser("get", help="Get a user's profile.")
    get_user_parser.add_argument("--email", help="The email of the user to get.")

    # Get user presence
    get_presence_parser = users_subparsers.add_parser("presence", help="Get a user's presence.")
    get_presence_parser.add_argument("--email", required=True, help="The email of the user.")

    # List users
    list_users_parser = users_subparsers.add_parser("list", help="List users.")

    # Scheduled Messages
    scheduled_messages_parser = subparsers.add_parser("scheduled-messages", help="Manage scheduled messages.")
    scheduled_messages_subparsers = scheduled_messages_parser.add_subparsers(dest="subcommand", required=True)

    # Schedule a message
    schedule_message_parser = scheduled_messages_subparsers.add_parser("schedule", help="Schedule a message.")
    schedule_message_parser.add_argument("--type", required=True, choices=["private", "stream"], help="The type of message to send.")
    schedule_message_parser.add_argument("--to", required=True, help="The recipient of the message.")
    schedule_message_parser.add_argument("--content", required=True, help="The content of the message.")
    schedule_message_parser.add_argument("--topic", help="The topic of the message (for stream messages).")
    schedule_message_parser.add_argument("--scheduled-delivery-timestamp", required=True, type=int, help="The Unix timestamp for when the message should be sent.")

    # Get scheduled messages
    get_scheduled_messages_parser = scheduled_messages_subparsers.add_parser("get", help="Get scheduled messages.")

    # Edit a scheduled message
    edit_scheduled_message_parser = scheduled_messages_subparsers.add_parser("edit", help="Edit a scheduled message.")
    edit_scheduled_message_parser.add_argument("--message-id", required=True, type=int, help="The ID of the scheduled message to edit.")
    edit_scheduled_message_parser.add_argument("--scheduled-delivery-timestamp", required=True, type=int, help="The new Unix timestamp for when the message should be sent.")

    # Delete a scheduled message
    delete_scheduled_message_parser = scheduled_messages_subparsers.add_parser("delete", help="Delete a scheduled message.")
    delete_scheduled_message_parser.add_argument("--message-id", required=True, type=int, help="The ID of the scheduled message to delete.")

    # Drafts
    drafts_parser = subparsers.add_parser("drafts", help="Manage drafts.")
    drafts_subparsers = drafts_parser.add_subparsers(dest="subcommand", required=True)

    # Create a draft
    create_draft_parser = drafts_subparsers.add_parser("create", help="Create a draft.")
    create_draft_parser.add_argument("--type", required=True, choices=["private", "stream"], help="The type of message to draft.")
    create_draft_parser.add_argument("--to", required=True, help="The recipient of the message.")
    create_draft_parser.add_argument("--content", required=True, help="The content of the message.")
    create_draft_parser.add_argument("--topic", help="The topic of the message (for stream messages).")

    # Get drafts
    get_drafts_parser = drafts_subparsers.add_parser("get", help="Get drafts.")

    # Edit a draft
    edit_draft_parser = drafts_subparsers.add_parser("edit", help="Edit a draft.")
    edit_draft_parser.add_argument("--draft-id", required=True, type=int, help="The ID of the draft to edit.")
    edit_draft_parser.add_argument("--content", required=True, help="The new content of the draft.")

    # Delete a draft
    delete_draft_parser = drafts_subparsers.add_parser("delete", help="Delete a draft.")
    delete_draft_parser.add_argument("--draft-id", required=True, type=int, help="The ID of the draft to delete.")

    # Alert Words
    alert_words_parser = subparsers.add_parser("alert-words", help="Manage alert words.")
    alert_words_subparsers = alert_words_parser.add_subparsers(dest="subcommand", required=True)

    # Get alert words
    get_alert_words_parser = alert_words_subparsers.add_parser("get", help="Get alert words.")

    # Add alert words
    add_alert_words_parser = alert_words_subparsers.add_parser("add", help="Add alert words.")
    add_alert_words_parser.add_argument("--words", required=True, help="Comma-separated list of words to add.")

    # Remove alert words
    remove_alert_words_parser = alert_words_subparsers.add_parser("remove", help="Remove alert words.")
    remove_alert_words_parser.add_argument("--words", required=True, help="Comma-separated list of words to remove.")

    args = parser.parse_args()

    if args.command == "messages":
        if args.subcommand == "send":
            if args.type == "stream":
                if not args.topic:
                    print("Error: --topic is required for stream messages.")
                    sys.exit(1)
                data = {
                    "type": "stream",
                    "to": args.to,
                    "topic": args.topic,
                    "content": args.content,
                }
            else:
                data = {
                    "type": "private",
                    "to": args.to,
                    "content": args.content,
                }
        elif args.subcommand == "edit":
            data = {
                "content": args.content,
            }
            if args.topic:
                data["topic"] = args.topic
            result = call_api("PATCH", f"messages/{args.message_id}", data=data)
            print(result)

        elif args.subcommand == "delete":
            result = call_api("DELETE", f"messages/{args.message_id}")
            print(result)

        elif args.subcommand == "fetch":
            result = call_api("GET", f"messages/{args.message_id}")
            print(result)


        elif args.subcommand == "flags":
            data = {
                "messages": [int(mid) for mid in args.message_ids.split(",")],
                "op": args.op,
                "flag": args.flag,
            }
            result = call_api("POST", "messages/flags", json=data)
            print(result)

        elif args.subcommand == "history":
            result = call_api("GET", f"messages/{args.message_id}/history")
            print(result)

    elif args.command == "reactions":
        if args.subcommand == "add":
            data = {
                "emoji_name": args.emoji_name,
            }
            result = call_api("POST", f"messages/{args.message_id}/reactions", data=data)
            print(result)

        elif args.subcommand == "remove":
            data = {
                "emoji_name": args.emoji_name,
            }
            result = call_api("DELETE", f"messages/{args.message_id}/reactions", data=data)
            print(result)

    elif args.command == "streams":
        if args.subcommand == "create":
            data = {
                "subscriptions": json.dumps([{"name": args.name, "description": args.description}]),
                "invite_only": args.private,
            }
            result = call_api("POST", "users/me/subscriptions", data=data)
            print(result)

        elif args.subcommand == "list":
            result = call_api("GET", "streams")
            print(result)

        elif args.subcommand == "subscribe":
            data = {
                "subscriptions": json.dumps([{"name": stream} for stream in args.streams.split(",")])
            }
            result = call_api("POST", "users/me/subscriptions", data=data)
            print(result)

        elif args.subcommand == "update":
            stream_id = get_stream_id(args.stream_name)
            data = {}
            if args.new_name:
                data["new_name"] = args.new_name
            if args.new_description:
                data["description"] = args.new_description
            result = call_api("PATCH", f"streams/{stream_id}", data=data)
            print(result)

        elif args.subcommand == "topics":
            stream_id = get_stream_id(args.stream_name)
            result = call_api("GET", f"users/me/{stream_id}/topics")
            print(result)

    elif args.command == "users":
        if args.subcommand == "get":
            if args.email:
                result = call_api("GET", f"users/{args.email}")
            else:
                result = call_api("GET", "users/me")
            print(result)

        elif args.subcommand == "presence":
            result = call_api("GET", f"users/{args.email}/presence")
            print(result)

        elif args.subcommand == "list":
            result = call_api("GET", "users")
            print(result)

    elif args.command == "scheduled-messages":
        if args.subcommand == "schedule":
            if args.type == "stream":
                if not args.topic:
                    print("Error: --topic is required for stream messages.")
                    sys.exit(1)
                data = {
                    "type": "stream",
                    "to": args.to,
                    "topic": args.topic,
                    "content": args.content,
                    "scheduled_delivery_timestamp": args.scheduled_delivery_timestamp,
                }
            else:
                data = {
                    "type": "private",
                    "to": args.to,
                    "content": args.content,
                    "scheduled_delivery_timestamp": args.scheduled_delivery_timestamp,
                }
            result = call_api("POST", "scheduled_messages", data=data)
            print(result)

        elif args.subcommand == "get":
            result = call_api("GET", "scheduled_messages")
            print(result)

        elif args.subcommand == "edit":
            data = {
                "scheduled_delivery_timestamp": args.scheduled_delivery_timestamp,
            }
            result = call_api("PATCH", f"scheduled_messages/{args.message_id}", data=data)
            print(result)

        elif args.subcommand == "delete":
            result = call_api("DELETE", f"scheduled_messages/{args.message_id}")
            print(result)

    elif args.command == "drafts":
        if args.subcommand == "create":
            if args.type == "stream":
                if not args.topic:
                    print("Error: --topic is required for stream messages.")
                    sys.exit(1)
                data = {
                    "type": "stream",
                    "to": args.to,
                    "topic": args.topic,
                    "content": args.content,
                }
            else:
                data = {
                    "type": "private",
                    "to": args.to,
                    "content": args.content,
                }
            result = call_api("POST", "drafts", data=data)
            print(result)

        elif args.subcommand == "get":
            result = call_api("GET", "drafts")
            print(result)

        elif args.subcommand == "edit":
            data = {
                "content": args.content,
            }
            result = call_api("PATCH", f"drafts/{args.draft_id}", data=data)
            print(result)

        elif args.subcommand == "delete":
            result = call_api("DELETE", f"drafts/{args.draft_id}")
            print(result)

    elif args.command == "alert-words":
        if args.subcommand == "get":
            result = call_api("GET", "users/me/alert_words")
            print(result)

        elif args.subcommand == "add":
            data = {
                "alert_words": args.words.split(","),
            }
            result = call_api("POST", "users/me/alert_words", json=data)
            print(result)

        elif args.subcommand == "remove":
            data = {
                "alert_words": args.words.split(","),
            }
            result = call_api("DELETE", "users/me/alert_words", json=data)
            print(result)


if __name__ == "__main__":
    main()
