# channel_posting_permissionsevent

*Source: https://docs.slack.dev/reference/events/message/channel_posting_permissions*

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

The posting permissions for a channel have been modified by a user.

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `channel_posting_permissions` message subtype event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "message",
            "subtype": "channel_posting_permissions",
            "ts": "1614215651.001300",
            "user": "U123ABC456",
            "text": "changed channel posting permissions.",
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