# message_repliedmessage

*Source: https://docs.slack.dev/reference/events/message/message_replied*

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

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `message_replied` message subtype event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "message",
            "message": {
                "type": "message",
                "user": "U123ABC456",
                "text": "Was there was there was there what was there was there what was there was there there was there.",
                "thread_ts": "1482960137.003543",
                "reply_count": 1,
                "replies": [
                    {
                        "user": "U2222222",
                        "ts": "1483037603.017503"
                    }
                ],
                "ts": "1482960137.003543"
            },
            "subtype": "message_replied",
            "hidden": true,
            "channel": "C123ABC456",
            "event_ts": "1483037604.017506",
            "ts": "1483037604.017506"
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


A `message_replied` message is sent when a channel's message is a reply to another message (its parent). The message's `thread_ts` value indicates the parent message.

Bug alert!

This event is missing the `subtype` field when dispatched over the Events API. Until it is fixed, examine message events' `thread_ts` value. When present, it's a reply. To be doubly sure, compare a `thread_ts` to the top-level `ts` value, when they differ the latter is a reply to the former.

See [message threading](/messaging#threading) for more information.