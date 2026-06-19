# channel_leavemessage

*Source: https://docs.slack.dev/reference/events/message/channel_leave*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `channel_leave` message subtype event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "message",
            "subtype": "channel_leave",
            "ts": "1358877455.000010",
            "user": "U2147483828",
            "text": "<@U2147483828|cal> has left the channel"
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


A `channel_leave` message is sent when a member of a channel leaves that channel.

If you prefer a more atomic event, use [`member_left_channel`](/reference/events/member_left_channel) instead. Consult [the changelog](/changelog/2017-05-rethinking-channel-entrance-and-exit-events-and-messages) for further guidance.