# subteam_created

*Source: https://docs.slack.dev/reference/events/subteam_created*

---

## Facts

**Required Scopes**

[`usergroups:read`](/reference/scopes/usergroups.read)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `subteam_created` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "subteam_created",
            "subteam": {
                "id": "S0615G0KT",
                "team_id": "T060RNRCH",
                "is_usergroup": true,
                "name": "Marketing Team",
                "description": "Marketing gurus, PR experts and product advocates.",
                "handle": "marketing-team",
                "is_external": false,
                "date_create": 1446746793,
                "date_update": 1446746793,
                "date_delete": 0,
                "auto_type": null,
                "created_by": "U060RNRCZ",
                "updated_by": "U060RNRCZ",
                "deleted_by": null,
                "prefs": {
                    "channels": [],
                    "groups": []
                },
                "user_count": "0"
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


The `subteam_created` event is sent to all connections for a workspace when a new User Group is created. Clients can use this to update their local list of User Groups and group members.