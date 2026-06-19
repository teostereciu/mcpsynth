# assistant_thread_context_changed

*Source: https://docs.slack.dev/reference/events/assistant_thread_context_changed*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`Events`](/apis/events-api)

## Usage info​

[Assistant apps](/ai/) will receive this event when a user opens a new channel while the container is open. This can be used to track the active context of a user in Slack.

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `assistant_thread_context_changed` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "assistant_thread_context_changed",
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
            "event_ts": "17298244.022142"
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