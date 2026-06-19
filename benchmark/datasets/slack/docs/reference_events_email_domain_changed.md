# email_domain_changed

*Source: https://docs.slack.dev/reference/events/email_domain_changed*

---

## Facts

**Required Scopes**

[`team:read`](/reference/scopes/team.read)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `email_domain_changed` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "email_domain_changed",
            "email_domain": "example.com",
            "event_ts": "1360782804.083113"
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


The `email_domain_changed` event is sent to all connections for a workspace when the email domain settings for a workspace change. Most clients can ignore this event.