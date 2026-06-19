# star_removed

*Source: https://docs.slack.dev/reference/events/star_removed*

---

## Facts

**Required Scopes**

[`stars:read`](/reference/scopes/stars.read)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `star_removed` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "star_removed",
            "user": "U123ABC456",
            "item": {
                "..."
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


When an item was unstarred, the `star_removed` event was sent to all connected clients for users who can see the content that was unstarred.

See the [`stars.list`](/reference/methods/stars.list) method for details of the structure of the `item` property.