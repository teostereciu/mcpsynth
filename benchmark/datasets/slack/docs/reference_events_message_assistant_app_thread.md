# assistant_app_threadmessage

*Source: https://docs.slack.dev/reference/events/message/assistant_app_thread*

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

The `assistant_app_thread` subtype is the subtype of the root message of an [assistant](/ai/) thread started by the end user.

This subtype is used with the root messages that are created when a user clicks the assistant entry point (triggering an [`assistant_thread_started`](/reference/events/assistant_thread_started) event) or starts a new chat with the app. This subtype is included in other message subtype payloads too, such that filtering it in a message listener would look like this:


    message.message.subtype === 'assistant_app_thread'


This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `assistant_app_thread` message subtype event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "message",
            "subtype": "message_changed",
            "message": {
                "text": "Chats from 2024-09-28T00:41:31.923Z",
                "subtype": "assistant_app_thread",
                "user": "U123456ABCD",
                "type": "message",
                "edited": {
                    "user": "U123456ABCD",
                    "ts": "1727484103.000000"
                },
                "team": "T123456ABCD",
                "thread_ts": "1727484091.821349",
                "reply_count": 1,
                "reply_users_count": 1,
                "latest_reply": "1727484101.719749",
                "reply_users": [
                    "U123456ABCD"
                ],
                "is_locked": false,
                "blocks": [
                    {}
                ],
                "assistant_app_thread": {
                    "title": "Chats from 2024-09-28T00:41:31.923Z",
                    "title_blocks": [],
                    "artifacts": []
                },
                "ts": "1727484091.821349"
            },
            "previous_message": {
                "text": "Chats from 2024-09-28T00:41:31.923Z",
                "subtype": "assistant_app_thread",
                "user": "U123456ABCD",
                "type": "message",
                "ts": "1727484091.821349",
                "team": "T123456ABCD",
                "thread_ts": "1727484091.821349",
                "reply_count": 1,
                "reply_users_count": 1,
                "latest_reply": "1727484101.719749",
                "reply_users": [
                    "U123456ABCD"
                ],
                "is_locked": false,
                "blocks": [
                    {}
                ],
                "assistant_app_thread": {
                    "title": "Chats from 2024-09-28T00:41:31.923Z",
                    "title_blocks": [],
                    "artifacts": []
                }
            },
            "channel": "D987654ABCD",
            "hidden": true,
            "ts": "1727484103.018100",
            "event_ts": "1727484103.018100",
            "channel_type": "im"
        },
        "type": "event_callback",
        "authorizations": [
            {
                "team_id": "T123ABC456",
                "user_id": "U123456ABCD",
                "is_bot": false,
                "is_enterprise_install": false,
            }
        ],
        "event_id": "Ev123ABC456",
        "event_time": 123456789
    }


The `assistant_app_thread` subtype message can also be useful for storing metadata about the conversation itself, like an external session ID or pointers to artifacts created during the conversation. Read more about sending message metadata in the [Using message metadata](/messaging/message-metadata) guide.