# call_rejected

*Source: https://docs.slack.dev/reference/events/call_rejected*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`Events`](/apis/events-api)

## Usage info​

If a call has been shared with a user in DM (and unfurled with the help of the [`link_shared`](/reference/events/link_shared) event) this event is sent if the user _rejects_ the call.

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `call_rejected` event.


    {
        "token": "12345FVmRUzNDOAu12345h",
        "team_id": "T123ABC456",
        "api_app_id": "BBBU04BB4",
        "event": {
            "type": "call_rejected",
            "call_id": "R123ABC456",
            "user_id": "U123ABC456",
            "channel_id": "D123ABC456",
            "external_unique_id": "123-456-7890"
        },
        "type": "event_callback",
        "event_id": "Ev123ABC456",
        "event_time": 1563448153,
        "authorizations": [
            {
                "team_id": "T123ABC456",
                "user_id": "U123ABC456",
                "is_bot": false,
                "is_enterprise_install": false,
            }
        ],
    }