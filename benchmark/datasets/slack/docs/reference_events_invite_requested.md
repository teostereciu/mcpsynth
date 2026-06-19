# invite_requested

*Source: https://docs.slack.dev/reference/events/invite_requested*

---

When an application subscribed to the `invite_requested` event is installed to an org, workspace owners and admins will no longer receive invite notifications from Slackbot.

## Facts

**Required Scopes**

[`admin.invites:read`](/reference/scopes/admin.invites.read)

**Compatible APIs**

[`Events`](/apis/events-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `invite_requested` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "invite_requested",
            "invite_request": {
                "id": "12345",
                "email": "bront@puppies.com",
                "date_created": 123455,
                "requester_ids": [
                    "U123ABC456"
                ],
                "channel_ids": [
                    "C123ABC456"
                ],
                "invite_type": "full_member",
                "real_name": "Brent",
                "date_expire": 123456,
                "request_reason": "They're good dogs, Brant",
                "team": {
                    "id": "T12345",
                    "name": "Puppy ratings workspace incorporated",
                    "domain": "puppiesrus"
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