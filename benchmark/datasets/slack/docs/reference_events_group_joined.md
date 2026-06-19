# group_joined

*Source: https://docs.slack.dev/reference/events/group_joined*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `group_joined` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "group_joined",
            "channel": {
                "id": "C024242424",
                "name": "secret-plans",
                "is_group": true,
                "created": 1360782804,
                "creator": "U012121212",
                "is_archived": false,
                "is_mpim": false,
                "members": [
                    "U012121212"
                ],
                "topic": {
                    "value": "Plan the world domination",
                    "creator": "U012121212",
                    "last_set": 1360782804
                },
                "purpose": {
                    "value": "To take over the world",
                    "creator": "U012121212",
                    "last_set": 1360782804
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


The `group_joined` event is sent to all connections for a user when that user joins a private channel.

The `channel` value is the string identifier for the private channel.

In addition to this message, all existing members of the private channel will receive a [`group_join` message](/reference/events/message/group_join) event.