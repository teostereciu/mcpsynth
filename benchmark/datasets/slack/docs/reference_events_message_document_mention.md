# document_mentionmessage

*Source: https://docs.slack.dev/reference/events/message/document_mention*

---

## Facts

**Required Scopes**

[`channels:history`](/reference/scopes/channels.history)

[`groups:history`](/reference/scopes/groups.history)

[`im:history`](/reference/scopes/im.history)

[`mpim:history`](/reference/scopes/mpim.history)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `document_mention` message subtype event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "user": "UA1BCD3EF",
            "subtype": "document_mention",
            "document_mention": {
                "file_id": "F123ABCDEFG",
                "section_id": "temp:C:GQL71204e5bd23942c79f0a22a51",
                "mentioning_user_ids": [
                    "UA1BCD3EF"
                ]
            },
            "type": "app_mention",
            "ts": "1716411280.657549",
            "text": "<@U123456ABC7> was mentioned in a canvas",
            "team": "T1ABC2DE3",
            "blocks": [
                {
                    "type": "section",
                    "block_id": "gcn3v",
                    "text": {
                        "type": "mrkdwn",
                        "text": "&gt;&gt;&gt;Hey <@U123456ABC7>",
                        "verbatim": false
                    }
                }
            ],
            "channel": "C012ABCDEFG",
            "event_ts": "1716411280.657549"
        },
        "type": "event_callback",
        "authorizations": [
            {
                "team_id": "T123ABC456",
                "user_id": "UA1BCD3EF",
                "is_bot": false,
                "is_enterprise_install": false,
            }
        ],
        "event_id": "Ev123ABC456",
        "event_time": 123456789
    }


The `document_mention` event subtype is sent to your event subscription when your bot is mentioned in the body of a canvas. It will always have both a `file_id` and a `section_id` property.

Otherwise, if your bot is mentioned in a threaded comment, your app will receive an [`app_mention`](/reference/events/app_mention) event.