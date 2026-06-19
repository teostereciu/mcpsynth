# unpinned_itemmessage

*Source: https://docs.slack.dev/reference/events/message/unpinned_item*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `unpinned_item` message subtype event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "message",
            "subtype": "unpinned_item",
            "user": "U123ABC456",
            "item_type": "G",
            "text": "<@U024BE7LH|cal> unpinned the message you pinned to the secretplans group.",
            "item": {},
            "channel": "G024BE91L",
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


When an item is un-pinned from a channel, an `unpinned_item` message is sent via slackbot to the user that initially pinned the item. The message will only be sent if the item was un-pinned by a different user.

Valid `item_type` values include:

  * `C`: channel message
  * `G`: private group message
  * `F`: file
  * `Fc`: file comments