# group_history_changedmessage

*Source: https://docs.slack.dev/reference/events/group_history_changed*

---

## Facts

**Required Scopes**

[`groups:history`](/reference/scopes/groups.history)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `group_history_changed` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "group_history_changed",
            "latest": "1358877455.000010",
            "ts": "1361482916.000003",
            "event_ts": "1361482916.000004"
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


A `group_history_changed` event is sent to all clients in a private channel when bulk changes have occurred to that group's history. When clients receive this message they should reload chat history for the private channel if they have any cached messages before `latest`.