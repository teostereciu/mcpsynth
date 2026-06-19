# team_access_granted

*Source: https://docs.slack.dev/reference/events/team_access_granted*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`Events`](/apis/events-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `team_access_granted` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "team_id": null,
            "enterprise_id": "EXXXXX",
            "api_app_id": "AXXXX",
            "event": {
                "type": "team_access_granted",
                "team_ids": [
                    "T1XX3",
                    "TXX34"
                ]
            }
        },
        "type": "event_callback",
        "authorizations": [
            {
                "enterprise_id": "EXXXXX",
                "team_id": "T123ABC456",
                "is_bot": false,
                "is_enterprise_install": false,
            }
        ],
        "event_id": "Ev123ABC456",
        "event_time": 123456789
    }


The `team_access_granted` event is sent to your [organization-ready app](/enterprise/organization-ready-apps) when your token is given access to a new workspace.