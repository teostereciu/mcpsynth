# message.channels

*Source: https://docs.slack.dev/reference/events/message.channels*

---

## Facts

**Required Scopes**

[`channels:history`](/reference/scopes/channels.history)

**Compatible APIs**

[`Events`](/apis/events-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `message.channels` event.


    {
        "token": "one-long-verification-token",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "message",
            "channel": "C123ABC456",
            "user": "U123ABC456",
            "text": "Live long and prospect.",
            "ts": "1355517523.000005",
            "event_ts": "1355517523.000005",
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
        "event_time": 1355517523
    }


The semantics for this message event type are similar to the core [message](/reference/events/message) event sent through the RTM API. Messages often include many more fields than those shown above.

Differentiate public channel messages from other `message.*` events by looking for the `event`'s `channel_type` field set to `"channel"`.

To receive only messages sent to your app, subscribe to [`app_mention`](/reference/events/app_mention) events instead.