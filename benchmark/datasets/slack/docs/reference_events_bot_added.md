# bot_added

*Source: https://docs.slack.dev/reference/events/bot_added*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `bot_added` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "bot_added",
            "bot": {
                "id": "B024BE7LH",
                "app_id": "A4H1JB4AZ",
                "name": "hugbot",
                "icons": {
                    "image_48": "https://slack.com/path/to/hugbot_48.png"
                }
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


The `bot_added` event is sent to all connections for a workspace when an integration "bot" is added. Clients can use this to update their local list of bots. If the bot belongs to a Slack app, the event will also include an `app_id` pointing to its parent app.