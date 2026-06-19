# group_open

*Source: https://docs.slack.dev/reference/events/group_open*

---

## Facts

**Required Scopes**

[`groups:read`](/reference/scopes/groups.read)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `group_open` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "group_open",
            "user": "U024BE7LH",
            "channel": "G024BE91L"
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


The `group_open` event is sent to all connections for a user when a group Direct Message (or `mpim`) is opened by that user.

This event is not available to bot users subscriptions in the [Events API](/apis/events-api/).