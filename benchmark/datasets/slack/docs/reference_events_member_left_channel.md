# member_left_channel

*Source: https://docs.slack.dev/reference/events/member_left_channel*

---

## Facts

**Required Scopes**

[`channels:read`](/reference/scopes/channels.read)

[`groups:read`](/reference/scopes/groups.read)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `member_left_channel` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "member_left_channel",
            "user": "W123ABC456",
            "channel": "C123ABC456",
            "channel_type": "C",
            "team": "T123ABC456"
        },
        "type": "event_callback",
        "authorizations": [
            {
                "team_id": "T123ABC456",
                "user_id": "W123ABC456",
                "is_bot": false,
                "is_enterprise_install": false,
            }
        ],
        "event_id": "Ev123ABC456",
        "event_time": 123456789
    }


The `member_left_channel` event is sent to all websocket connections and event subscriptions when users leave public or private channels.Property| Description| `user`| User ID belonging to the user that left the channel.| `channel`| Channel ID for a public channel or private channel (AKA `group`).| `channel_type`| A single letter indicating the type of channel used in `channel`. Private channels created before March 2021 have a `G` prefix. Both public and private channels created after March 2021 have a `C` prefix. If you need to know the channel type, use the [conversations.info](/reference/methods/conversations.info) method.| `team`| Team ID, identifying which workspace the user is from.
---|---

This event is supported as a bot user subscription in the [Events API](/apis/events-api/). Workspace event subscriptions are also available for tokens holding at least one of the `channels:read` or `groups:read` scopes. Which events your app will receive depends on the scopes and their context. For instance, you'll only receive `member_left_channel` events for private channels if your app has the `groups:read` permission.