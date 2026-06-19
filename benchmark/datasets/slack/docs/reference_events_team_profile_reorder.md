# team_profile_reorder

*Source: https://docs.slack.dev/reference/events/team_profile_reorder*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `team_profile_reorder` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "team_profile_reorder",
            "profile": {
                "fields": [
                    {
                        "id": "Xf06054AAA",
                        "ordering": 0
                    }
                ]
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


The `team_profile_reorder` event is sent to all connections for a workspace when Workspace Admin reorders the field definitions in the profile. The payload includes only the `id` and the `ordering` for each field definition that is reordered. Where appropriate, clients should update to reflect new changes immediately.