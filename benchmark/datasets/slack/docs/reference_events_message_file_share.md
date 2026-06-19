# file_sharemessage

*Source: https://docs.slack.dev/reference/events/message/file_share*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This event is no longer served.

File share events have been phased out in favor of regular messages and threads — read [our changelog entry](/changelog/2018-05-file-threads-soon-tread) for more information.

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `file_share` message subtype event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "message",
            "text": "We got one!",
            "files": [
                {
                    "id": "F0RDC39U1",
                    "created": 1529342081,
                    "timestamp": 1529342081,
                    "name": "ghostrap.png",
                    "title": "ghostrap.png",
                    "mimetype": "image/png",
                    "filetype": "png",
                    "pretty_type": "PNG",
                    "user": "U061F7AUR",
                    "editable": false,
                    "size": 196920,
                    "mode": "hosted",
                    "is_external": false,
                    "external_type": "",
                    "is_public": false,
                    "public_url_shared": false,
                    "display_as_bot": false,
                    "username": "",
                    "url_private": "https://files.slack.com/files-pri/T061EG9R6-F0RDC39U1/ghostrap.png",
                    "url_private_download": "https://files.slack.com/files-pri/T061EG9R6-F0RDC39U1/download/ghostrap.png",
                    "thumb_64": "https://files.slack.com/files-tmb/T061EG9R6-F0RDC39U1-f8c7b072da/ghostrap_64.png",
                    "thumb_80": "https://files.slack.com/files-tmb/T061EG9R6-F0RDC39U1-f8c7b072da/ghostrap_80.png",
                    "thumb_360": "https://files.slack.com/files-tmb/T061EG9R6-F0RDC39U1-f8c7b072da/ghostrap_360.png",
                    "thumb_360_w": 360,
                    "thumb_360_h": 360,
                    "thumb_480": "https://files.slack.com/files-tmb/T061EG9R6-F0RDC39U1-f8c7b072da/ghostrap_480.png",
                    "thumb_480_w": 480,
                    "thumb_480_h": 480,
                    "thumb_160": "https://files.slack.com/files-tmb/T061EG9R6-F0RDC39U1-f8c7b072da/ghostrap_160.png",
                    "image_exif_rotation": 1,
                    "original_w": 512,
                    "original_h": 512,
                    "pjpeg": "https://files.slack.com/files-tmb/T061EG9R6-F0RDC39U1-f8c7b072da/ghostrap_pjpeg.jpg",
                    "permalink": "https://episod-slackform.slack.com/files/U061F7AUR/F0RDC39U1/ghostrap.png",
                    "permalink_public": "https://slack-files.com/T061EG9R6-F0RDC39U1-815d735817",
                    "has_rich_preview": false
                }
            ],
            "user": "U123ABC456",
            "upload": true,
            "display_as_bot": false,
            "bot_id": null,
            "ts": "1529342088.000086",
            "channel": "D0L4B9P0Q",
            "event_ts": "1529342088.000086",
            "channel_type": "im"
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


A `file_share` message is sent when a file is shared into a channel, group or direct message.

This event no longer dispatches in the RTM API. In the Events API, subscriptions and deliveries will continue.

However, the shape of the event has changed: instead of including a `file` node, you'll find an array in the `files` attribute instead.

### Slack Connect files​

When a file is uploaded into a Slack Connect channel, [file object](/reference/objects/file-object) properties are not immediately accessible to apps listening via the Events API. Instead, the payload will contain a file object with the key-value pair `"file_access": "check_file_info"` meaning that further action is required from your app in order to view an uploaded file's metadata.


    {
        "files": [
            {
                "id": "F12345678",
                "mode": "file_access",
                "file_access": "check_file_info",
                "created": 0,
                "timestamp": 0,
                "user": ""
            }
        ]
    }


See [Slack Connect: working with channels between organizations](/apis/slack-connect/#check_file_info) for more details on how to handle this scenario.

### Field notes​

The `user` property contains the User ID of the user that shared the file, which may differ from the user that uploaded the file.

The `upload` property indicates whether this share happened at upload time, or some time later.

The `files` property contains an array of tidy [file objects](/reference/objects/file-object).