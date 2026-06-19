# team_migration_started

*Source: https://docs.slack.dev/reference/events/team_migration_started*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `team_migration_started` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "team_migration_started"
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


The `team_migration_started` event is sent when a Slack workspace is about to be migrated between servers. **The websocket connection will close immediately after it is sent.**

Occasionally we need to move Slack workspaces to a new server. To avoid any data synchronization bugs or race conditions we disconnect all clients from a workspace before starting this process. By the time a client has reconnected the process is usually complete, so the impact is minimal.

When clients receive this event, immediately start a reconnection process by calling [`rtm.start`](/reference/methods/rtm.start) again. You may receive occasional `migration_in_progress` errors when re-calling `rtm.start`. If this happens you should wait a few seconds and try again. If the error continues you should wait longer before retrying, and so on.