# channel_convert_to_privatemessage

*Source: https://docs.slack.dev/reference/events/message/channel_convert_to_private*

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

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `channel_convert_to_private` message subtype event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "subtype": "channel_convert_to_private",
            "user": "U1234ABCD",
            "text": "made this channel *private*. Now, it can only be viewed or joined by invitation.",
            "type": "message",
            "ts": "1730984822.596869",
            "channel": "C1234ABCD",
            "event_ts": "1730984822.596869",
            "channel_type": "group"
        },
        "type": "event_callback",
        "authorizations": [
            {
                "team_id": "T123ABC456",
                "user_id": "U1234ABCD",
                "is_bot": false,
                "is_enterprise_install": false,
            }
        ],
        "event_id": "Ev123ABC456",
        "event_time": 123456789
    }


A `channel_convert_to_private` message is sent when a channel is made private. Now, it can only be viewed or joined by invitation.