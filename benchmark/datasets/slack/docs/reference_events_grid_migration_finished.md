# grid_migration_finished

*Source: https://docs.slack.dev/reference/events/grid_migration_finished*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`Events`](/apis/events-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `grid_migration_finished` event.


    {
        "token": "XXYYZZ",
        "team_id": "TXXXXXXXX",
        "api_app_id": "AXXXXXXXXX",
        "event": {
            "type": "grid_migration_finished",
            "enterprise_id": "EXXXXXXXX"
        },
        "type": "event_callback",
        "event_id": "EvXXXXXXXX",
        "event_time": 1234567890
    }


This Events API-only event is sent via subscription whenever your app is installed by completes migration to an [Enterprise organization](/enterprise).

The example above details the complete Events API payload, including the event wrapper. The `team_id` indicates which workspace is migrating.

By also subscribing to the [`grid_migration_started`](/reference/events/grid_migration_finished) event, you'll receive notice when the migration began.

It's best to cease API and platform operations for a workspace during migration. While duration varies workspace-to-workspace, expect an extended period of unavailability.