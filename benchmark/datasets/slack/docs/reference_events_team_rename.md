# team_rename

*Source: https://docs.slack.dev/reference/events/team_rename*

---

## Facts

**Required Scopes**

[`team:read`](/reference/scopes/team.read)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `team_rename` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "team_rename",
            "name": "New Team Name Inc.",
            "team_id": "T1234"
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


The `team_rename` event is sent to all connections for a workspace when an admin changes the workspace name.

Clients can use this to update the display of the workspace name as soon as it changes. If they don't the client will receive the new name the next time it calls [`rtm.start`](/reference/methods/rtm.start).