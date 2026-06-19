# app_requested

*Source: https://docs.slack.dev/reference/events/app_requested*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`Events`](/apis/events-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `app_requested` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "app_requested",
            "app_request": {
                "id": "1234",
                "app": {
                    "id": "A5678",
                    "name": "Brent's app",
                    "description": "They're good apps, Bront.",
                    "help_url": "brontsapp.com",
                    "privacy_policy_url": "brontsapp.com",
                    "app_homepage_url": "brontsapp.com",
                    "app_directory_url": "https://slack.slack.com/apps/A102ARD7Y",
                    "is_granular_bot_app": true,
                    "is_app_directory_approved": true,
                    "is_internal": false,
                    "additional_info": "none"
                },
                "previous_resolution": {
                    "status": "approved",
                    "scopes": [
                        {
                            "name": "app_requested",
                            "description": "allows this app to listen for app install requests",
                            "is_sensitive": false,
                            "token_type": "user"
                        }
                    ]
                },
                "user": {
                    "id": "U1234",
                    "name": "Bront",
                    "email": "bront@brent.com"
                },
                "team": {
                    "id": "T1234",
                    "name": "Brant App Team",
                    "domain": "brantappteam"
                },
                "enterprise": null,
                "scopes": [
                    {
                        "name": "app_requested",
                        "description": "allows this app to listen for app install requests",
                        "is_sensitive": false,
                        "token_type": "user"
                    }
                ],
                "message": "none"
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


The `app_requested` event payload contains info about an app that a user on a team has requested to install.Field| Description| `app`| Info on the app that the user has requested. Nested inside the `app` field, the `help_url`, `privacy_policy_url`, `app_homepage_url`, and `app_directory_url` fields contain links to more info.| `previous_resolution`| Indicates whether the app was previously approved or restricted in this org. If the app installation has not been requested before, `previous_resolution` won't appear in the payload.| `user`| User ID of the user requesting the install.| `team`| Team ID of of the team that the app will be approved for. If `null`, then the approval request is for the whole enterprise.| `enterprise`| If not `null`, conveys that the _approval_ is for whole enterprise.| `scopes`| The scopes that the app requests.| `message`| An optional message from the app.
---|---