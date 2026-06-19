# group_left

*Source: https://docs.slack.dev/reference/events/group_left*

---

## Facts

**Required Scopes**

[`groups:read`](/reference/scopes/groups.read)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `group_left` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "group_left",
            "channel": "G02ELGNBH"
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


The `group_left` event is sent to all connections for a user when that user leaves a private channel. Clients should respond to this message by closing the private channel - this means that when a private channel is left from client A, it will automatically be closed in client B.

The `channel` value is the string identifier for the private channel.

In addition to this message, all existing members of the group will receive a [`group_leave` message](/reference/events/message/group_leave) event.