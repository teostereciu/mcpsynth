# team_profile_change

*Source: https://docs.slack.dev/reference/events/team_profile_change*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `team_profile_change` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "team_profile_change",
            "profile": {
                "fields": [
                    {
                        "id": "Xf06054AAA",
                        ...
                    },
                    ...
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


The `team_profile_change` event is sent to all connections for a workspace when Workspace Admin updates the field definitions in the profile. Only the modified field definitions are included in the payload. Where appropriate, clients should update to reflect new changes immediately.