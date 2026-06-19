# group_rename

*Source: https://docs.slack.dev/reference/events/group_rename*

---

## Facts

**Required Scopes**

[`groups:read`](/reference/scopes/groups.read)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `group_rename` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "group_rename",
            "channel": {
                "id": "G02ELGNBH",
                "name": "new_name",
                "created": 1360782804
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


When a private channel is renamed, the `group_rename` event is sent to all connections for members of a private channel. Clients can use this to update their local list of private channels.