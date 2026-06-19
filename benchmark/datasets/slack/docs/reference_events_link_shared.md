# link_shared

*Source: https://docs.slack.dev/reference/events/link_shared*

---

## Facts

**Required Scopes**

[`links:read`](/reference/scopes/links.read)

**Compatible APIs**

[`Events`](/apis/events-api)

## Usage info​

The `link_shared` event is sent over the [Events API](/apis/events-api/) when a link—matching the registered URL domain your app is setup to track—is posted.

Your app will receive this event **both** when the link is written into the message composer before being posted, and when the link is posted into a Slack channel. The exception is if you are working within an Enterprise organization. In this case, `link_shared` events are not dispatched for previews when URLs are simply entered in the composer as opposed to actually sent.

The `link_shared` event is dispatched when a message posted includes a matching domain, with the exception of messages posted by classic apps. Apps will also not receive `link_shared` events for their own messages. Refer to [Differences between classic apps and Slack apps](/legacy/legacy-app-migration/differences-between-classic-apps-and-granular-slack-apps) for more information.

For context on these events, [learn more about unfurling links in messages](/messaging/unfurling-links-in-messages).

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `link_shared` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "link_shared",
            "channel": "C123ABC456",
            "is_bot_user_member": true,
            "is_unfurl_refresh": true,
            "user": "U123ABC456",
            "message_ts": "123456789.9875",
            "unfurl_id": "C123456.123456789.987501.1b90fa1278528ce6e2f6c5c2bfa1abc9a41d57d02b29d173f40399c9ffdecf4b",
            "thread_ts": "123456621.1855",
            "source": "conversations_history",
            "links": [
                {
                    "domain": "example.com",
                    "url": "https://example.com/12345"
                },
                {
                    "domain": "example.com",
                    "url": "https://example.com/67890"
                },
                {
                    "domain": "another-example.com",
                    "url": "https://yet.another-example.com/v/abcde"
                }
            ],
            "user_locale": "en-US"
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


The `thread_ts` field only appears when the link was shared within a [message thread](/messaging#threading).

`is_bot_user_member` is a boolean field indicating whether the app’s bot user is a member of the conversation.

`unfurl_id` identifies the link and can be used to supply the [`chat.unfurl`](/reference/methods/chat.unfurl) method (along with `source`). This field will not be present within an Enterprise organization.

`source` is an enumerated string that tells you whether the event happened in composer (`"source": "composer"`) or in a sent message (`"source": "conversations_history`). This field will not be present within an Enterprise organization.

Take care with the `message_ts` and `channel` fields. When the source of this event is the message composer, rather than a posted message, these values don't correspond to typical timestamps and channels. No matter what, the values of `message_ts` and `channel` always work to supply [`chat.unfurl`](/reference/methods/chat.unfurl), but if you attempt to use _other_ Slack API methods with these timestamps and channels, the calls will fail.

The `user_locale` field is the user's locale in Slack that you can use when supplying blocks or metadata in the [`chat.unfurl`](/reference/methods/chat.unfurl) API method.

The `is_unfurl_refresh` field is used when a user makes a request to refresh an existing [Work Object unfurl](/messaging/work-objects-implementation#refreshing-unfurls). Slack will dispatch a new `link_shared` event with `"is_unfurl_refresh": true`. This indicates that the event is for refreshing an existing unfurl, rather than creating an initial unfurl.

A full payload for the `link_shared` event sent when a link is typed into the message **composer** is:


    {
        "type": "link_shared",
        "channel": "COMPOSER",
        "is_bot_user_member": true,
        "user": "U123ABC456",
        "message_ts": "U123ABC456-909b5454-75f8-4ac4-b325-1b40e230bbd8-gryl3kb80b3wm49ihzoo35fyqoq08n2y",
        "unfurl_id": "U123ABC456-909b5454-75f8-4ac4-b325-1b40e230bbd8-gryl3kb80b3wm49ihzoo35fyqoq08n2y",
        "source": "composer",
        "links": [
            {
                "domain": "example.com",
                "url": "https://example.com/12345"
            },
            {
                "domain": "example.com",
                "url": "https://example.com/67890"
            },
            {
                "domain": "another-example.com",
                "url": "https://yet.another-example.com/v/abcde"
            }
        ],
         "user_locale": "en-US"
    }



[Learn more about unfurling links in messages](/messaging/unfurling-links-in-messages).