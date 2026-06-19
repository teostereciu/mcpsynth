# thread_broadcastmessage

*Source: https://docs.slack.dev/reference/events/message/thread_broadcast*

---

## Facts

**Required Scopes**

[`channels:history`](/reference/scopes/channels.history)

[`groups:history`](/reference/scopes/groups.history)

[`im:history`](/reference/scopes/im.history)

[`mpim:history`](/reference/scopes/mpim.history)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `thread_broadcast` message subtype event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "message",
            "subtype": "thread_broadcast",
            "text": "broadcasting this reply",
            "user": "U123ABC456",
            "ts": "1673464745.620769",
            "thread_ts": "1673464730.703009",
            "root": {
                "client_msg_id": "123abc456-...",
                "type": "message",
                "text": "This is the original message",
                "user": "U123ABC456",
                "ts": "1673464730.703009",
                "blocks": [
                    {
                        "type": "rich_text",
                        "block_id": "qTg",
                        "elements": [
                            {
                                "type": "rich_text_section",
                                "elements": [
                                    {
                                        "type": "text",
                                        "text": "This is the original message"
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "team": "T123ABC456",
                "thread_ts": "1673464730.703009",
                "reply_count": 1,
                "reply_users_count": 1,
                "latest_reply": "1673464745.620769",
                "reply_users": [
                    "U123ABC456"
                ],
                "is_locked": false
            },
            "blocks": [
                {
                    "type": "rich_text",
                    "block_id": "BVp",
                    "elements": [
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "text",
                                    "text": "broadcasting this reply"
                                }
                            ]
                        }
                    ]
                }
            ],
            "client_msg_id": "123abc456-...",
            "channel": "C123ABC456",
            "event_ts": "1673464745.620769",
            "channel_type": "channel"
        },
        "type": "event_callback",
        "authorizations": [
            {
                "team_id": "T123ABC456",
                "user_id": "U123ABC456",
                "is_bot": false,
                "is_enterprise_install": false,
            }
        ],
        "event_id": "Ev123ABC456",
        "event_time": 123456789
    }


The `thread_broadcast` message subtype is sent when a user or bot user has indicated their reply should be broadcast to the whole channel.

It's a pointer or reference to the actual thread and is meant more to be informational than to fully describe the message. The reference cannot contain attachments or message buttons.

The `message` includes a `root` field with a modified form of the original message in the thread, meant for use in rendering by Slack client applications.

See [message threading](/messaging#threading) for more information.