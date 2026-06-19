# app_deleted

*Source: https://docs.slack.dev/reference/events/app_deleted*

---

## Facts

**Required Scopes**

[`admin.apps:read`](/reference/scopes/admin.apps.read)

**Compatible APIs**

[`Events`](/apis/events-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `app_deleted` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "app_deleted",
            "app_id": "A015CA1LGHG",
            "app_name": "my-admin-app",
            "app_owner_id": "U013B64J7MSZ",
            "team_id": "E073D7H7BBE",
            "team_domain": "ACME Enterprises",
            "event_ts": "1700001891.279278"
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


The `app_deleted` event payload contains information about an app that has been deleted from a team or organization it belongs to.

Only [organization-wide](/enterprise/organization-ready-apps#:~:text=An%20organization%2Dwide%20app%20is,the%20app%20on%20many%20workspaces) apps can subscribe to this event.Field| Description| `app_id`| The app that was deleted from the team.| `app_name`| The name of the app the was deleted from the team.| `app_owner_id`| The owner of the app that was deleted from the team.| `team_id`| The team that the app was deleted from.| `team_domain`| The domain of the team that the app was deleted from.| `event_ts`| Time the app was deleted.
---|---