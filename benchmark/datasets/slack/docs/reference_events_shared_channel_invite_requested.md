# shared_channel_invite_requested

*Source: https://docs.slack.dev/reference/events/shared_channel_invite_requested*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`Events`](/apis/events-api)

## Usage info​

A customer must opt-in to receive this event. When enabled, external user invitations will not be sent until approved. To approve an invitation, use the [`conversations.requestSharedInvite.approve`](/reference/methods/conversations.requestSharedInvite.approve) API method. To deny an invitation use the [`conversations.requestSharedInvite.deny`](/reference/methods/conversations.requestSharedInvite.deny) API method.Example of workflow trigger payload


    {
        "actor": {
            "id": "U012345ABCD",
            "name": "primary-owner",
            "is_bot": false,
            "team_id": "E0123456ABC",
            "timezone": "",
            "real_name": "primary-owner",
            "display_name": ""
        },
        "channel_id": "C0123ABCDEF",
        "event_type": "slack#/events/shared_channel_invite_requested",
        "channel_name": "our-channel",
        "channel_type": "public",
        "target_users": [
            {
                "email": "user@some-corp.com",
                "invite_id": "I0123456ABC"
            }
        ],
        "teams_in_channel": [
            {
                "id": "E0123456ABC",
                "icon": {
                    "image_34": "https://slack.com/some-corp/v123/img/abc_0123.png",
                    "image_default": true
                },
                "name": "some_enterprise",
                "domain": "someenterprise",
                "is_verified": false,
                "date_created": 1637947110,
                "avatar_base_url": "https://slack.com/some-corp/",
                "requires_sponsorship": false
            },
            {
                "id": "T012345ABCD",
                "icon": {
                    "image_34": "https://slack.com/another-corp/v456/img/def_4567.png",
                    "image_default": true
                },
                "name": "another_enterprise",
                "domain": "anotherenterprise",
                "is_verified": false,
                "date_created": 1645550933,
                "avatar_base_url": "https://slack.com/another-corp/",
                "requires_sponsorship": false
            }
        ],
        "is_external_limited": true,
        "channel_date_created": 1718725442,
        "channel_message_latest_counted_timestamp": 1718745614025449
    }


Example of Events API payload

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `shared_channel_invite_requested` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "shared_channel_invite_requested",
            "channel": {
                "id": "C0123ABCDEF",
                "is_im": false,
                "is_private": false,
                "date_created": 1564642828,
                "message_latest_counted_timestamp": 1564642836000009,
                "name": "host-team12345678999"
            },
            "actor": {
                "id": "U012345ABCD",
                "team_id": "E01234ABC",
                "name": "username-012345ABCD",
                "updated": 1564642800,
                "who_can_share_contact_card": "EVERYONE",
                "profile": {
                    "real_name": "User Name",
                    "display_name": "Username",
                    "real_name_normalized": "User Name",
                    "display_name_normalized": "Username",
                    "team": "E01234ABC",
                    "avatar_hash": "g12345678910",
                    "email": "mock-user@some-corp.com",
                    "image_24": "https://secure.gravatar.com/avatar/5efa915c16f10de52e23f4a8b8da612e.jpg?s=24&d=https%3A%2F%2Fdev.slack.com%2Fdev-cdn%2Fv1718734113%2Fimg%2Favatars%2Fuser_shapes%2Fava_0010-24.png"
                }
            },
            "is_external_limited": true,
            "target_users": [
                {
                    "invite_id": "I01234ABC",
                    "email": "mock-user@some-corp.com"
                }
            ],
            "teams_in_channel": [
                {
                    "id": "E01234ABC",
                    "name": "Team Name",
                    "icon": {
                        "image_34": "https://some-corp.com/v123/img/avatars-teams/ava_123.png",
                        "image_default": true
                    },
                    "avatar_base_url": "https://some-corp.com",
                    "is_verified": false,
                    "domain": "domain-10000000000",
                    "date_created": 1564642800,
                    "requires_sponsorship": false
                },
                {
                    "id": "E56789DEF",
                    "name": "Team Name",
                    "icon": {
                        "image_34": "https://some-corp.com/v456/img/avatars-teams/ava_456.png",
                        "image_default": true
                    },
                    "avatar_base_url": "https://some-corp.com",
                    "is_verified": false,
                    "domain": "domain-10000000123",
                    "date_created": 1564642800,
                    "requires_sponsorship": false
                }
            ]
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