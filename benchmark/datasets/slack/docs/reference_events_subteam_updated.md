# subteam_updated

*Source: https://docs.slack.dev/reference/events/subteam_updated*

---

## Facts

**Required Scopes**

[`usergroups:read`](/reference/scopes/usergroups.read)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `subteam_updated` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "subteam_updated",
            "subteam": {
                "id": "S516MPG9X",
                "team_id": "T0GMXV71T",
                "is_usergroup": true,
                "is_subteam": true,
                "name": "My User Group Test",
                "description": "User Group Test",
                "handle": "user-group-test",
                "is_external": false,
                "date_create": 1492655498,
                "date_update": 1595814882,
                "date_delete": 0,
                "auto_type": null,
                "auto_provision": false,
                "enterprise_subteam_id": "",
                "created_by": "U0GN26UBG",
                "updated_by": "U0GN26UBG",
                "deleted_by": null,
                "prefs": {
                    "channels": [
                        "CJG07GZDK"
                    ],
                    "groups": []
                },
                "users": [
                    "U123ABC456",
                    "U0GNBSG1G",
                    "U0K0XMM2R",
                    "U1FLR7FB8",
                    "U3S7347ED",
                    "U5ZR5M0FM",
                    "U600XRXS9"
                ],
                "user_count": 7,
                "channel_count": 0
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


The `subteam_updated` event is sent to all connections for a workspace when an existing User Group is updated. This event is triggered for changes to the User Group information (name, description, or handle) as well as the members of the group. Clients can use this to update their local list of groups and group members. The `users` field is truncated at 500, however the `user_count` field will still show the actual count.

If you are only interested in User Group membership changes, consider using the [`subteam_members_changed`](/reference/events/subteam_members_changed) event instead.

This [event type](/reference/events) may also arise when a subteam has been disabled.