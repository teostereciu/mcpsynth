# bot_messagemessage

*Source: https://docs.slack.dev/reference/events/message/bot_message*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `bot_message` message subtype event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "message",
            "subtype": "bot_message",
            "ts": "1358877455.000010",
            "text": "Pushing is the answer",
            "bot_id": "BB12033",
            "username": "github",
            "icons": {}
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


In [classic Slack apps](/legacy/legacy-app-migration/migrating-classic-apps), the `bot_message` event is sent when a message is sent to a channel by an integration "bot". It is like a normal user message, except it has no associated user. With current Slack apps, also known as granular bot permissions (GBP) apps, you can detect if a message was sent by a bot by the presence of the `bot_id` and `bot_profile` fields in the event payload.

The `bot_id` tells you which bot sent this message. The username and icon to use can be looked up by passing this to [bots.info](/reference/methods/bots.info). Some `bot_message` events also include `username` or `icons` properties. If present, these override the default username or icon for this bot.