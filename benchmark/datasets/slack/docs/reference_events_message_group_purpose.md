# group_purposemessage

*Source: https://docs.slack.dev/reference/events/message/group_purpose*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `group_purpose` message subtype event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "message",
            "subtype": "group_purpose",
            "ts": "1358877455.000010",
            "user": "U2147483828",
            "purpose": "whatever",
            "text": "<@U2147483828|cal> set the group purpose: whatever"
        },
        "type": "event_callback",
        "authorizations": [
            {
                "team_id": "T123ABC456",
                "user_id": "U2147483828",
                "is_bot": false,
                "is_enterprise_install": false,
            }
        ],
        "event_id": "Ev123ABC456",
        "event_time": 123456789
    }


A `group_purpose` message is sent when the purpose for a private group is changed using the [`group.setPurpose` method](/reference/methods/group.setPurpose).