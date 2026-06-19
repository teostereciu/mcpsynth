# subteam_members_changed

*Source: https://docs.slack.dev/reference/events/subteam_members_changed*

---

## Facts

**Required Scopes**

[`usergroups:read`](/reference/scopes/usergroups.read)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `subteam_members_changed` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "subteam_members_changed",
            "subteam_id": "S123ABC456",
            "team_id": "T060RNRCH",
            "date_previous_update": 1446670362,
            "date_update": 1492906952,
            "added_users": [
                "U060RNRCZ",
                "U060ULRC0",
                "U061309JM"
            ],
            "added_users_count": "3",
            "removed_users": [
                "U06129G2V"
            ],
            "removed_users_count": "1"
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


The `subteam_members_changed` event is sent to all connections for a workspace when users are added or removed from an existing User Group. Clients can use the timestamp information to detect if they are out of sync with the user list.

Unlike [`subteam_updated`](/reference/events/subteam_updated), this only shows the delta of added or removed members and does not include a snapshot of the User Group.