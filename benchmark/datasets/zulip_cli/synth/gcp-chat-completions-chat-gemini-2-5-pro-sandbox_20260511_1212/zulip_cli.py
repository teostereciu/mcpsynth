sh
import os
import requests
import argparse

ZULIP_EMAIL = os.environ.get("ZULIP_EMAIL")
ZULIP_API_KEY = os.environ.get("ZULIP_API_KEY")
ZULIP_SITE = os.environ.get("ZULIP_SITE")

def zulip_request(endpoint, method, params=None):
    response = requests.request(
        method,
        f"{ZULIP_SITE}/api/v1{endpoint}",
        auth=(ZULIP_EMAIL, ZULIP_API_KEY),
        json=params,
    )
    response.raise_for_status()
    return response.json()

def send_message(args):
    params = {
        "type": args.type,
        "to": args.to,
        "content": args.content,
    }
    if args.type == "stream":
        params["topic"] = args.topic
    zulip_request("/messages", "POST", params)


def edit_message(args):
    params = {
        "content": args.content,
    }
    if args.topic:
        params["topic"] = args.topic
    zulip_request(f"/messages/{args.message_id}", "PATCH", params)


def delete_message(args):
    zulip_request(f"/messages/{args.message_id}", "DELETE")


def get_messages(args):
    params = {
        "num_before": args.num_before,
        "num_after": args.num_after,
        "anchor": args.anchor,
    }
    print(zulip_request("/messages", "GET", params))


def get_streams(args):
    print(zulip_request("/streams", "GET"))


def get_users(args):
    print(zulip_request("/users", "GET"))


def add_reaction(args):
    zulip_request(f"/messages/{args.message_id}/reactions", "POST", {"emoji_name": args.emoji_name})


def schedule_message(args):
    params = {
        "type": args.type,
        "to": args.to,
        "content": args.content,
        "scheduled_delivery_timestamp": args.timestamp,
    }
    if args.type == "stream":
        params["topic"] = args.topic
    zulip_request("/scheduled_messages", "POST", params)



def create_stream(args):
    subscriptions = [{'name': args.stream_name, 'description': args.description}]
    params = {
        'subscriptions': subscriptions,
        'principals': args.principals,
        'announce': args.announce,
        'invite_only': args.invite_only,
        'history_public_to_subscribers': args.history_public_to_subscribers,
    }
    zulip_request("/streams", "POST", params)


def update_stream(args):
    params = {}
    if args.description:
        params["description"] = args.description
    if args.new_name:
        params["new_name"] = args.new_name
    if args.is_private is not None:
        params["is_private"] = args.is_private
    if args.is_announcement_only is not None:
        params["is_announcement_only"] = args.is_announcement_only

    zulip_request(f"/streams/{args.stream_id}", "PATCH", params)


def update_message_flags(args):
    params = {
        "messages": args.message_ids,
        "op": args.op,
        "flag": args.flag,
    }
    zulip_request("/messages/flags", "POST", params)


def subscribe_to_streams(args):
    params = {
        "subscriptions": [{"name": stream} for stream in args.stream_names],
    }
    zulip_request("/users/me/subscriptions", "POST", params)

def main():
    parser = argparse.ArgumentParser(description="Zulip CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    send_message_parser = subparsers.add_parser("send-message", help="Send a message")
    send_message_parser.add_argument("--type", required=True, choices=["private", "stream"], help="The type of message")
    send_message_parser.add_argument("--to", required=True, help="The recipient of the message")
    send_message_parser.add_argument("--content", required=True, help="The content of the message")
    send_message_parser.add_argument("--topic", help="The topic of the message (for stream messages)")
    send_message_parser.set_defaults(func=send_message)

    
    edit_message_parser = subparsers.add_parser("edit-message", help="Edit a message")
    edit_message_parser.add_argument("--message-id", required=True, help="The ID of the message to edit")
    edit_message_parser.add_argument("--content", required=True, help="The new content of the message")
    edit_message_parser.add_argument("--topic", help="The new topic of the message")
    edit_message_parser.set_defaults(func=edit_message)

    
    delete_message_parser = subparsers.add_parser("delete-message", help="Delete a message")
    delete_message_parser.add_argument("--message-id", required=True, help="The ID of the message to delete")
    delete_message_parser.set_defaults(func=delete_message)

    
    get_messages_parser = subparsers.add_parser("get-messages", help="Get messages")
    get_messages_parser.add_argument("--num-before", type=int, default=0, help="Number of messages to fetch before the anchor")
    get_messages_parser.add_argument("--num-after", type=int, default=0, help="Number of messages to fetch after the anchor")
    get_messages_parser.add_argument("--anchor", default="newest", help="The anchor message ID or 'newest'")
    get_messages_parser.set_defaults(func=get_messages)

    
    get_streams_parser = subparsers.add_parser("get-streams", help="Get all streams")
    get_streams_parser.set_defaults(func=get_streams)

    
    get_users_parser = subparsers.add_parser("get-users", help="Get all users")
    get_users_parser.set_defaults(func=get_users)

    
    add_reaction_parser = subparsers.add_parser("add-reaction", help="Add a reaction to a message")
    add_reaction_parser.add_argument("--message-id", required=True, help="The ID of the message to react to")
    add_reaction_parser.add_argument("--emoji-name", required=True, help="The name of the emoji to react with")
    add_reaction_parser.set_defaults(func=add_reaction)

    
    schedule_message_parser = subparsers.add_parser("schedule-message", help="Schedule a message to be sent in the future")
    schedule_message_parser.add_argument("--type", required=True, choices=["private", "stream"], help="The type of message")
    schedule_message_parser.add_argument("--to", required=True, help="The recipient of the message")
    schedule_message_parser.add_argument("--content", required=True, help="The content of the message")
    schedule_message_parser.add_argument("--timestamp", required=True, type=int, help="Unix timestamp for when the message should be sent")
    schedule_message_parser.add_argument("--topic", help="The topic of the message (for stream messages)")
    schedule_message_parser.set_defaults(func=schedule_message)

    
    create_stream_parser = subparsers.add_parser("create-stream", help="Create a new stream")
    create_stream_parser.add_argument("--stream-name", required=True, help="The name of the new stream")
    create_stream_parser.add_argument("--description", default="", help="A description for the new stream")
    create_stream_parser.add_argument("--principals", nargs='+', help="A list of user emails to subscribe to the stream")
    create_stream_parser.add_argument("--announce", action="store_true", help="Announce the new stream in #announce")
    create_stream_parser.add_argument("--invite-only", action="store_true", help="Make the stream invite-only")
    create_stream_parser.add_argument("--history-public-to-subscribers", action="store_true", help="Make message history public to new subscribers")
    create_stream_parser.set_defaults(func=create_stream)

    
    update_stream_parser = subparsers.add_parser("update-stream", help="Update a stream")
    update_stream_parser.add_argument("--stream-id", required=True, type=int, help="The ID of the stream to update")
    update_stream_parser.add_argument("--description", help="A new description for the stream")
    update_stream_parser.add_argument("--new-name", help="The new name of the stream")
    update_stream_parser.add_argument("--is-private", type=bool, help="Whether the stream is private")
    update_stream_parser.add_argument("--is-announcement-only", type=bool, help="Whether the stream is for announcements only")
    update_stream_parser.set_defaults(func=update_stream)

    
    update_flags_parser = subparsers.add_parser("update-flags", help="Update message flags")
    update_flags_parser.add_argument("--message-ids", nargs='+', required=True, help="A list of message IDs to update")
    update_flags_parser.add_argument("--op", required=True, choices=["add", "remove"], help="Whether to add or remove the flag")
    update_flags_parser.add_argument("--flag", required=True, help="The flag to update")
    update_flags_parser.set_defaults(func=update_message_flags)

    
    subscribe_parser = subparsers.add_parser("subscribe", help="Subscribe to one or more streams")
    subscribe_parser.add_argument("--stream-names", nargs='+', required=True, help="A list of stream names to subscribe to")
    subscribe_parser.set_defaults(func=subscribe_to_streams)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
