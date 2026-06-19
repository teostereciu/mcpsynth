# ekm_access_deniedmessage

*Source: https://docs.slack.dev/reference/events/message/ekm_access_denied*

---

## Facts

**Required Scopes**

[`channels:history`](/reference/scopes/channels.history)

[`groups:history`](/reference/scopes/groups.history)

[`im:history`](/reference/scopes/im.history)

[`mpim:history`](/reference/scopes/mpim.history)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `ekm_access_denied` message subtype event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "message",
            "subtype": "ekm_access_denied",
            "ts": "1358877455.000010",
            "text": "Your admins have suspended everyone's access to this content.",
            "user": "U123ABC456"
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


This message subtype appears when an original piece of content is redacted by a workspace's administrators. The actual message content is unavailable.

The author of so-called "tombstoned" content will be indicated with the user ID `UREVOKEDU`. This virtual user ID cannot be looked up with `users.info` or `users.list`.