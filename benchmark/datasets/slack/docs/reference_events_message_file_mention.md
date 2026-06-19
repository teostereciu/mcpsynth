# file_mentionmessage

*Source: https://docs.slack.dev/reference/events/message/file_mention*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This event is no longer served.

File mentions have been phased out in favor of regular messages and threads — read [our changelog entry](/changelog/2018-05-file-threads-soon-tread) for more information.

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `file_mention` message subtype event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "message",
            "subtype": "file_mention",
            "ts": "1358877455.000010",
            "text": "<@cal> mentioned a file: <https:...7.png|7.png>",
            "file": {},
            "user": "U123ABC456"
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


A `file_mention` message is sent when a file is mentioned in a channel, group or direct message.

The `file` property contains a [file object](/reference/objects/file-object). The `user` property contains the User ID of the user that mentioned the file (which may differ from the user that uploaded the file).