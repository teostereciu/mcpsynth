# channel_convert_to_publicmessage

*Source: https://docs.slack.dev/reference/events/message/channel_convert_to_public*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `channel_convert_to_public` message subtype event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "message",
            "subtype": "channel_convert_to_public",
            "ts": "1723680078.026719",
            "text": "made this channel *public*. Any member in this workspace can see and join it.",
            "user": "U123ABC456",
            "channel": "C123ABC456",
            "event_ts": "1614215651.001300",
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


A `channel_convert_to_public` message is sent when a channel is made public. Any member in this workspace can see and join it.