# message.mpim

*Source: https://docs.slack.dev/reference/events/message.mpim*

---

## Facts

**Required Scopes**

[`mpim:history`](/reference/scopes/mpim.history)

**Compatible APIs**

[`Events`](/apis/events-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `message.mpim` event.


    {
        "token": "one-long-verification-token",
        "team_id": "T061EG9R6",
        "api_app_id": "A0PNCHHK2",
        "event": {
            "type": "message",
            "channel": "G024BE91L",
            "user": "U2147483697",
            "text": "Let's make a pact.",
            "ts": "1355517523.000005",
            "event_ts": "1355517523.000005",
            "channel_type": "mpim"
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

Differentiate multi-party direct messages from other `message.*` events by looking for the `event`'s `channel_type` field set to `"mpim"`.