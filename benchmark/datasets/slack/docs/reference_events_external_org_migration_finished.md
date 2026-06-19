# external_org_migration_finished

*Source: https://docs.slack.dev/reference/events/external_org_migration_finished*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `external_org_migration_finished` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "external_org_migration_finished",
            "team": {
                "id": "TXXXXXXXX",
                "is_migrating": false
            },
            "date_started": 1551398400,
            "date_finished": 1551409200
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


The `external_org_migration_finished` event is sent to all connections when an external workspace completes to migrate to an [Enterprise organization](/enterprise).

The `team` indicates the external workspace that is migrating.

The `date_started` indicates the time the external workspace started to migrate.

The `date_finished` indicates the time the external workspace finished to migrate.