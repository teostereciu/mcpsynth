# team_domain_change

*Source: https://docs.slack.dev/reference/events/team_domain_change*

---

## Facts

**Required Scopes**

[`team:read`](/reference/scopes/team.read)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `team_domain_change` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "team_domain_change",
            "url": "https://my.slack.com",
            "domain": "my",
            "team_id": "T1234"
        },
        "type": "event_callback",
        "authorizations": [
            {
                "team_id": "T123ABC456",
                "is_bot": false,
                "is_enterprise_install": false,
            }
        ],
        "event_id": "Ev123ABC456",
        "event_time": 123456789
    }


The `team_domain_change` event is sent to all connections for a workspace when the workspace domain changes.

Since the existing domain will continue to work (causing a redirect) until it is claimed by another workspace, clients don't need to do anything special with this event. It is sent for the benefit of our web client, which needs to reload when the domain changes.