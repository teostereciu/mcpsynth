# channel_joined

*Source: https://docs.slack.dev/reference/events/channel_joined*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `channel_joined` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "channel_joined",
            "channel": {
                ...
            }
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


The `channel_joined` event is sent to all connections for a user when that user joins a channel.

In addition to this message, all existing members of the channel may receive a [`channel_join` message](/reference/events/message/channel_join) event.

There's also the fresher, more dependable [`member_joined_channel`](/reference/events/member_joined_channel). [This changelog entry](/changelog/2017-05-rethinking-channel-entrance-and-exit-events-and-messages) clears it all up.