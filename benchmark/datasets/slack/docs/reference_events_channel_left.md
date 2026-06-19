# channel_left

*Source: https://docs.slack.dev/reference/events/channel_left*

---

## Facts

**Required Scopes**

[`channels:read`](/reference/scopes/channels.read)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `channel_left` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "channel_left",
            "channel": "C123ABC456"
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


The `channel_left` event is sometimes sent to all connections for a user when that user leaves a public channel. It is sometimes withheld.

Clients should respond to this message by closing the channel — this means that when a channel is left from client A, it will automatically be closed in client B.

In addition to this message, all existing members of the channel will receive a [`channel_leave` message](/reference/events/message/channel_leave) event.