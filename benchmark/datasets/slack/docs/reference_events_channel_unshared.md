# channel_unshared

*Source: https://docs.slack.dev/reference/events/channel_unshared*

---

## Facts

**Required Scopes**

[`channels:read`](/reference/scopes/channels.read)

[`groups:read`](/reference/scopes/groups.read)

**Compatible APIs**

[`Events`](/apis/events-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `channel_unshared` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "channel_unshared",
            "previously_connected_team_id": "E163Q94DX",
            "channel": "C123ABC456",
            "is_ext_shared": false,
            "event_ts": "1561064063.001100"
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


The `channel_unshared` event is sent to all event subscriptions when an external workspace has been removed from an existing shared channel.

The `previously_connected_team_id` value is the team ID of the workspace that has been removed from the channel. Note that this ID may start with `E`, indicating that it is the ID of the organization that has been removed from the channel.

The `channel` value is the ID for the public or private channel.

The `is_ext_shared` value is `true` if the channel is still externally shared, and `false` otherwise.

This event is supported as a bot user subscription in the [Events API](/apis/events-api/). Workspace event subscriptions are also available for tokens holding at least one of the `channels:read` or `groups:read` scopes. Which events your app will receive depends on the scopes and their context. For instance, you'll only receive `channel_unshared` events for private channels if your app has the `groups:read` permission.