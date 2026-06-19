# dnd_updated

*Source: https://docs.slack.dev/reference/events/dnd_updated*

---

## Facts

**Required Scopes**

[`dnd:read`](/reference/scopes/dnd.read)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `dnd_updated` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "dnd_updated",
            "user": "U1234",
            "dnd_status": {
                "dnd_enabled": true,
                "next_dnd_start_ts": 1450387800,
                "next_dnd_end_ts": 1450423800,
                "snooze_enabled": true,
                "snooze_endtime": 1450373897
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


The `dnd_updated` event is sent to the current user when their Do Not Disturb settings have changed.

This event is not available to bot user subscriptions in the [Events API](/apis/events-api/).