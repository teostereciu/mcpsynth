# file_comment_deleted

*Source: https://docs.slack.dev/reference/events/file_comment_deleted*

---

This event is no longer served.

File comments have been phased out in favor of regular messages and threads — read [our changelog entry](/changelog/2018-05-file-threads-soon-tread) for more information.

## Facts

**Required Scopes**

[`files:read`](/reference/scopes/files.read)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `file_comment_deleted` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "file_comment_deleted",
            "comment": "Fc67890",
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


The `file_comment_deleted` event is sent when a file comment is deleted. It is sent to all connected clients for users who can see the file. Clients can use this notification to update comments in real-time for open files.

The `file` property includes the file ID, as well as a top-level `file_id`. To obtain additional information about the file, use the [`files.info`](/reference/methods/files.info) API method.

Unlike `file_comment_added` and `file_comment_edited` the comment property only contains the ID of the deleted comment, not the full comment object.