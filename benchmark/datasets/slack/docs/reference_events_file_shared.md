# file_shared

*Source: https://docs.slack.dev/reference/events/file_shared*

---

## Facts

**Required Scopes**

[`files:read`](/reference/scopes/files.read)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `file_shared` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "file_shared",
            "channel_id": "D01315BHHSN",
            "file_id": "F2147483862",
            "user_id": "U0Z7K8SRH",
            "file": {
                "id": "F2147483862"
            },
            "event_ts": "1617804931.000300"
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


The `file_shared` event is sent when a file is shared. It is sent to all connected clients for all users that have permission to see the file. The `file` property includes the file ID, as well as a top-level `file_id`. To obtain additional information about the file, use the [`files.info`](/reference/methods/files.info) API method.