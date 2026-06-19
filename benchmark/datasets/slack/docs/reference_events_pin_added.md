# pin_added

*Source: https://docs.slack.dev/reference/events/pin_added*

---

## Facts

**Required Scopes**

[`pins:read`](/reference/scopes/pins.read)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `pin_added` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "pin_added",
            "user": "U123ABC456",
            "channel_id": "C02ELGNBH",
            "item": {
                ...
            },
            "event_ts": "1360782804.083113"
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


When an item is pinned in a channel, the `pin_added` event is sent to all members of that channel.