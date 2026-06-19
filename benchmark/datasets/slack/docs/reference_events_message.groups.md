# message.groups

*Source: https://docs.slack.dev/reference/events/message.groups*

---

## Facts

**Required Scopes**

[`groups:history`](/reference/scopes/groups.history)

**Compatible APIs**

[`Events`](/apis/events-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `message.groups` event.


    {
        "token": "one-long-verification-token",
        "team_id": "T061EG9R6",
        "api_app_id": "A0PNCHHK2",
        "event": {
            "type": "message",
            "channel": "G024BE91L",
            "user": "U2147483697",
            "text": "One cannot programmatically detect the difference between `message.mpim` and `message.groups`.",
            "ts": "1355517523.000005",
            "event_ts": "1355517523.000005",
            "channel_type": "group"
        },
        "type": "event_callback",
        "authorizations": [
            {
                "team_id": "T061EG9R6",
                "user_id": "U2147483697",
                "is_bot": false,
                "is_enterprise_install": false,
            }
        ],
        "event_id": "Ev0PV52K21",
        "event_time": 1355517523
    }


The semantics for this message event type are similar to the core [message](/reference/events/message) event sent through the RTM API. Messages often include many more fields than those shown above.

Differentiate private channels from other `message.*` events by looking for the `event`'s `channel_type` field set to `"group"`.

To receive only messages sent to your app, subscribe to [`app_mention`](/reference/events/app_mention) events instead.