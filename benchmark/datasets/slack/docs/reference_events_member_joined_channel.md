# member_joined_channel

*Source: https://docs.slack.dev/reference/events/member_joined_channel*

---

## Facts

**Required Scopes**

[`channels:read`](/reference/scopes/channels.read)

[`groups:read`](/reference/scopes/groups.read)

[`mpim:read`](/reference/scopes/mpim.read)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `member_joined_channel` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "member_joined_channel",
            "user": "W123ABC456",
            "channel": "C123ABC456",
            "channel_type": "C",
            "team": "T123ABC456",
            "inviter": "U123456789",
            "enterprise": "E123456789"
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


The `member_joined_channel` event is sent when users join any channel type, including public and private channels, with the exception of direct messages between two users. For direct messages, there can only ever be two users, and additional members cannot be added.

This event requires membership in the conversation in order to receive events. It is supported as a bot user subscription in the [Events API](/apis/events-api/). Bot users will receive this event when a new member joins a channel your bot or app is already a member of.

Which events your bot or app will receive depends on the scopes granted and their context. For example, if your bot or app has the `channels:read` scope, it will receive events for public channels. If it has `groups:read`, it will receive events for private channels.

This event is also triggered when creating a new channel.Property| Description| `user`| User ID belonging to the user that joined the channel.| `channel`| Channel ID for a public channel or private channel (AKA `group`).| `channel_type`| A single letter indicating the type of channel used in `channel`. Private channels created before March 2021 have a `G` prefix. Both public and private channels created after March 2021 have a `C` prefix. If you need to know the channel type, use the [conversations.info](/reference/methods/conversations.info) method.| `team`| Team ID, identifying which workspace the user is from.| `inviter`| User ID of the inviting user. The value will be blank if a user manually joins a channel, is added by default, or the channel is converted from a public channel to a private channel.| `enterprise`| Enterprise ID, identifying which org the user is from. The value will be blank if the user's team is not an Enterprise organization.
---|---

This example illustrates an absent `inviter` property, a result of a channel being converted from public to private:


    {
        "type": "member_joined_channel",
        "user": "W123ABC456",
        "channel": "G123ABC456",
        "channel_type": "G",
        "team": "T123ABC456"
    }