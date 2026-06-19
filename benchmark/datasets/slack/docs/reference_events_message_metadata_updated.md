# message_metadata_updated

*Source: https://docs.slack.dev/reference/events/message_metadata_updated*

---

## Facts

**Required Scopes**

[`metadata.message:read`](/reference/scopes/metadata.message.read)

**Compatible APIs**

[`Events`](/apis/events-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `message_metadata_updated` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "message_metadata_updated",
            "channel_id": "CJN879K8A",
            "event_ts": "1658906295.002200",
            "previous_metadata": {
                "event_type": "task_created",
                "event_payload": {
                    "id": "TK-2132",
                    "summary": "New issue with the display of mobile element",
                    "description": "An end user has found a problem with the new mobile container for data entry. It was reproduced in the current version of IOS.",
                    "priority": "HIGH",
                    "resource_type": "TASK"
                }
            },
            "app_id": "AQF4F123M",
            "bot_id": "B8241P2B34D",
            "user_id": "U123ABC456",
            "team_id": "T12F3JCAP",
            "message_ts": "1658905974.587109",
            "metadata": {
                "event_type": "task_created",
                "event_payload": {
                    "id": "TK-2135",
                    "summary": "New issue with the display of mobile element",
                    "description": "An end user has found a problem with the new mobile container for data entry. It was reproduced in the current version of IOS.",
                    "priority": "HIGH",
                    "resource_type": "TASK"
                }
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


The `message_metadata_updated` event is sent when a message's metadata has been updated. Within the payload you'll notice an extra `previous_metadata` in addition to the `metadata` section, notifying you of what was changed.

Similar to `message_metadata_posted` and `message_metadata_deleted`, your app will only subscribe to the event types defined within the `metadata_subscriptions` key within your app's manifest file (in this example, the `task_created` event). For more information about this, check out the [metadata documentation](/messaging/message-metadata#specific_events).