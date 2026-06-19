# file_deleted

*Source: https://docs.slack.dev/reference/events/file_deleted*

---

## Facts

**Required Scopes**

[`files:read`](/reference/scopes/files.read)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `file_deleted` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "file_deleted",
            "file_id": "F2147483862",
            "event_ts": "1361482916.000004"
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


The `file_deleted` event is sent to all connected clients for a workspace when a file is deleted. Unlike most file events, the `file` property contains a file ID and not a full file object.

_This event is not raised if the reason for a file's removal is due to a workspace's[file retention](https://slack.com/help/articles/203457187-Customize-message-and-file-retention) policy, as opposed to a user deleting the file_.