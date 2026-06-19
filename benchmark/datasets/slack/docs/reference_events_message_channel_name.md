# channel_namemessage

*Source: https://docs.slack.dev/reference/events/message/channel_name*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `channel_name` message subtype event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "message",
            "subtype": "channel_name",
            "ts": "1358877455.000010",
            "user": "U2147483828",
            "old_name": "random",
            "name": "watercooler",
            "text": "<@U2147483828|cal> has renamed the channek from \"random\" to \"watercooler\""
        },
        "type": "event_callback",
        "authorizations": [
            {
                "team_id": "T123ABC456",
                "user_id": "U2147483828",
                "is_bot": false,
                "is_enterprise_install": false,
            }
        ],
        "event_id": "Ev123ABC456",
        "event_time": 123456789
    }


A `channel_name` message is sent when a channel is renamed.