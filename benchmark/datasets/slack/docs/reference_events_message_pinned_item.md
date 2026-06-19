# pinned_itemmessage

*Source: https://docs.slack.dev/reference/events/message/pinned_item*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `pinned_item` message subtype event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "message",
            "subtype": "pinned_item",
            "user": "U123ABC456",
            "item_type": "F",
            "text": "<@U024BE7LH|cal> pinned their Image <https:...7.png|7.png> to this channel.",
            "item": {},
            "channel": "C123ABC456",
            "ts": "1360782804.083113"
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


The `pinned_item` message is sent when an item is pinned to a channel.