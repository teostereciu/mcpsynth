# file_unshared

*Source: https://docs.slack.dev/reference/events/file_unshared*

---

## Facts

**Required Scopes**

[`files:read`](/reference/scopes/files.read)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `file_unshared` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "file_unshared",
            "file_id": "F2147483862",
            "file": {
                "id": "F2147483862"
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


The `file_unshared` event is sent when a file is unshared. It is sent to all connected clients for all users that had permission to see the file. The `file` property includes the file ID, as well as a top-level `file_id`. To obtain additional information about the unshared file, use the [`files.info`](/reference/methods/files.info) API method.

_This event is not raised if the reason for a file's removal is due to a workspace's[file retention](https://slack.com/help/articles/203457187-Customize-message-and-file-retention) policy, as opposed to a user unsharing the file_.