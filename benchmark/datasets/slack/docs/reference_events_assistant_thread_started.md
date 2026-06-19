# assistant_thread_started

*Source: https://docs.slack.dev/reference/events/assistant_thread_started*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`Events`](/apis/events-api)

## Usage info​

[Assistant apps](/ai/) will receive this event when users start a new assistant thread. You can listen to this event to know when a user opens the container, at which point the `context` will also be sent. This will contain the channel the user is currently viewing, as well as the team and enterprise IDs. It is not required to do anything with the `context`; in fact, some applications will have no use for it. But if you want to use it for app logic, you need to first call [`conversations.info`](/reference/methods/conversations.info) to see if your app has access to the channel.

To get notifications when the user moves around Slack once the container is open, subscribe to the [`assistant_thread_context_changed`](/reference/events/assistant_thread_context_changed) event.

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `assistant_thread_started` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "assistant_thread_started",
            "assistant_thread": {
                "user_id": "U123ABC456",
                "context": {
                    "channel_id": "C123ABC456",
                    "team_id": "T07XY8FPJ5C",
                    "enterprise_id": "E480293PS82"
                },
                "channel_id": "D123ABC456",
                "thread_ts": "1729999327.187299"
            },
            "event_ts": "1715873754.429808"
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