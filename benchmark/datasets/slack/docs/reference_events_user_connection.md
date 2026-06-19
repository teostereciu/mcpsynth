# user_connection

*Source: https://docs.slack.dev/reference/events/user_connection*

---

## Facts

**Required Scopes**

[`users:write`](/reference/scopes/users.write)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This event has a `subtype` field (can be either `connect` or `disconnect`) that dictates what tasks an app must perform to satisfy the request from the end-user.

Subtype: `connect`

This subtype notifies the app that a user is requesting to connect with the app. This event contains a `trigger_id` that allows the app to open a modal containing the steps, links, or buttons to get the user through its connection flow.

### Example payload​


    {
        "token": "P1GEyKehpM8yI998PLwq0P66",
        "team_id": "E012A3BC4DE",
        "api_app_id": "A012ABC34DE",
        "event": {
            "type": "user_connection",
            "subtype": "connect",
            "user": "U012A3BC4DE",
            "trigger_id": "1293638028594.1249184885746.0d121a0e01d2e7a795ecc7a62880a406",
            "event_ts": "1764264284.841251"
        },
        "type": "event_callback",
        "event_id": "Ev012A3BCDEF",
        "event_time": 1764264284
    }


Subtype: `disconnect`

This subtype informs the app that a user is requesting to disconnect from the app. This event contains the required information to identify the user.


    {
        "token": "P1GEyKehpM8yI998PLwq0P66",
        "team_id": "E012A3BC4DE",
        "api_app_id": "A012ABC34DE",
        "event": {
            "type": "user_connection",
            "subtype": "disconnect",
            "enterprise_id": "E012A3BC4DE",
            "user": "U012A3BC4DE",
            "event_ts": "1764264317.061589"
        },
        "type": "event_callback",
        "event_id": "Ev012A3BCDEF",
        "event_time": 1764264317
    }