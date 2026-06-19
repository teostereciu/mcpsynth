# subteam_self_added

*Source: https://docs.slack.dev/reference/events/subteam_self_added*

---

## Facts

**Required Scopes**

[`usergroups:read`](/reference/scopes/usergroups.read)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `subteam_self_added` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "subteam_self_added",
            "subteam_id": "S0615G0KT"
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


The `subteam_self_added` event is sent to you when you have been added to an existing User Group. Clients can use this to update their local list of User Groups.

This event is not available to bot users subscriptions in the [Events API](/apis/events-api/).