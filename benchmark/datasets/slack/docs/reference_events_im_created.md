# im_created

*Source: https://docs.slack.dev/reference/events/im_created*

---

## Facts

**Required Scopes**

[`im:read`](/reference/scopes/im.read)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `im_created` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "im_created",
            "user": "U024BE7LH",
            "channel": {
                "id": "C0123456",
                "is_im": true,
                "user": "U0123456",
                "created": 1355517521,
                "is_org_shared": false
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


The `im_created` event is sent to all connections for a user when a new direct message channel is created that they are a member of.

This message lets the client know that a channel has been created, but the client should show no changes based on this, just update its internal list of IM channels. Usually this event is followed by an [`im_open`](/reference/events/im_open) event.