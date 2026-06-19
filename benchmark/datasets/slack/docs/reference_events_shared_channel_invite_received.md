# shared_channel_invite_received

*Source: https://docs.slack.dev/reference/events/shared_channel_invite_received*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This event will fire if you use the [conversations.inviteShared](/reference/methods/conversations.inviteShared) API call with the `user_ids` argument to invite a bot or an app to a Slack Connect channel. This will not fire if you invite a user via email.

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `shared_channel_invite_received` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "shared_channel_invite_received",
            "invite": {
                "id": "I028YDERZSQ",
                "date_created": 1626876000,
                "date_invalid": 1628085600,
                "inviting_team": {
                    "id": "T12345678",
                    "name": "Corgis",
                    "icon": {},
                    "is_verified": false,
                    "domain": "corgis",
                    "date_created": 1480946400
                },
                "inviting_user": {
                    "id": "U12345678",
                    "team_id": "T12345678",
                    "name": "crus",
                    "updated": 1608081902,
                    "profile": {
                        "real_name": "Corgis Rus",
                        "display_name": "Corgis Rus",
                        "real_name_normalized": "Corgis Rus",
                        "display_name_normalized": "Corgis Rus",
                        "team": "T12345678",
                        "avatar_hash": "gcfh83a4c72k",
                        "email": "corgisrus@slack-corp.com",
                        "image_24": "https://placekitten.com/24/24",
                        "image_32": "https://placekitten.com/32/32",
                        "image_48": "https://placekitten.com/48/48",
                        "image_72": "https://placekitten.com/72/72",
                        "image_192": "https://placekitten.com/192/192",
                        "image_512": "https://placekitten.com/512/512"
                    }
                },
                "recipient_user_id": "U87654321"
            },
            "channel": {
                "id": "C12345678",
                "is_private": false,
                "is_im": false,
                "name": "test-slack-connect"
            },
            "event_ts": "1626876010.000100"
        },
        "type": "event_callback",
        "authorizations": [
            {
                "team_id": "T123ABC456",
                "user_id": "U12345678",
                "is_bot": false,
                "is_enterprise_install": false,
            }
        ],
        "event_id": "Ev123ABC456",
        "event_time": 123456789
    }