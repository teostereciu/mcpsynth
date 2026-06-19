# file_commentmessage

*Source: https://docs.slack.dev/reference/events/message/file_comment*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This event is no longer served.

File comments have been phased out in favor of regular messages and threads — read [our changelog entry](/changelog/2018-05-file-threads-soon-tread) for more information.

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `file_comment` message subtype event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "message",
            "subtype": "file_comment",
            "ts": "1361482916.000003",
            "text": "<@cal> commented on a file: ...",
            "file": {},
            "comment": {}
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


A `file_comment` message is sent when a new comment is added to a file shared into a channel, group or direct message.