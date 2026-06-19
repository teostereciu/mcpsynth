# channel_joinmessage

*Source: https://docs.slack.dev/reference/events/message/channel_join*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `channel_join` message subtype event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "message",
            "subtype": "channel_join",
            "ts": "1358877458.000011",
            "user": "U2147483828",
            "text": "<@U2147483828|cal> has joined the channel",
            "inviter": "U123456789"
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


The `channel_join` event is sometimes sent to all connections for a user when that user leaves a channel. It is sometimes withheld.

If the user was invited, the message will include an `inviter` property containing the user ID of the inviting user. The property will otherwise be absent.

If you prefer a more atomic event, use [`member_joined_channel`](/reference/events/member_joined_channel) instead. Consult [the changelog](/changelog/2017-05-rethinking-channel-entrance-and-exit-events-and-messages) for further guidance.