# message.app_home

*Source: https://docs.slack.dev/reference/events/message.app_home*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`Events`](/apis/events-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `message.app_home` event.


    {
        "token": "one-long-verification-token",
        "team_id": "T012345678",
        "api_app_id": "A0PNCHHK2",
        "event": {
            "type": "message",
            "user": "U012345ABCD",
            "text": "How many cats did we herd yesterday?",
            "ts": "1525215129.000001",
            "channel": "D0PNCRP9N",
            "event_ts": "1525215129.000001",
            "channel_type": "app_home"
        },
        "type": "event_callback",
        "authorizations": [
            {
                "enterprise_id": "E123ABC456",
                "user_id": "U012345ABCD",
                "team_id": "T012345678",
                "is_bot": false,
                "is_enterprise_install": false,
            }
        ],
        "event_id": "Ev0PV52K25",
        "event_time": 1525215129
    }


This event is sent to subscribers when a user engages with the application via the direct message-like [_App Home_](/changelog/2021-01-workspace-apps-retiring-the-platform-graveyard-in-aug-2021#app_home) interface, exclusive to the now defunct _workspace apps_ project. Traditional Slack apps with a bot user can treat 1:1 direct messages with users as a kind of "app home" by subscribing to the [`app_home_opened`](/reference/events/app_home_opened) and [`message.im`](/reference/events/message.im) events.

Apps grant apps a dedicated space within Slack where members can interact directly— we call it your **_App Home_**. Apps can use this space for personal notifications, onboarding information, and other helpful features.

When your app is installed, the _App Home_ between your app and the installing user is automatically established. Other people in a workspace can engage your app at any time, creating another _App Home_ between your app and the user.

This event does not require any specific OAuth scope to function. Apps allow each user in workspace to open a conversation with your app and add it to their _App Home_ sidebar category in Slack.

Differentiate app home messages from other `message.*` events by looking for the `event`'s `channel_type` field set to `"app_home"`.

The semantics for this message event type are similar to the core [message](/reference/events/message) event sent through the RTM API.