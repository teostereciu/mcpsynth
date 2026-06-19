# team_join

*Source: https://docs.slack.dev/reference/events/team_join*

---

## Facts

**Required Scopes**

[`users:read`](/reference/scopes/users.read)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `team_join` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "team_join",
            "user": {
                ...
            }
        },
        "type": "event_callback",
        "authorizations": [
            {
                "team_id": "T123ABC456",
                "is_bot": false,
                "is_enterprise_install": false,
            }
        ],
        "event_id": "Ev123ABC456",
        "event_time": 123456789
    }


The `team_join` event is sent to all connections for a workspace when a new member joins. Clients can use this to update their local cache of members.