# presence_sub

*Source: https://docs.slack.dev/reference/events/presence_sub*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

Ask the message server to subscribe you to [presence](/apis/web-api/user-presence-and-status) events for the specified list of users.

Instead of _receiving_ this event type, your app must post it into the websocket. Present an array labeled `ids` containing all of the user IDs you want presence subscriptions for.

To use this event, you'll need to first connect with [`rtm.connect`](/reference/methods/rtm.connect) or [`rtm.start`](/reference/methods/rtm.start).

For instance, to add subscriptions for users `U123456` and `W123456`, present JSON like so:


    {
        "type": "presence_sub",
        "ids": [
            "U061F7AUR",
            "W123456"
        ]
    }


All subscription requests require the entire subscription list _each invocation. To remove subscriptions, do not include their user ID in a subsequent `presence_sub` request. To add a new subscription, add it to the array.

In response to your presence subscription request, you'll receive singular or batch [`presence_change`](/reference/events/presence_change) events declaring the current presence status of each user _added_ to the subscription.


    {
        "type": "presence_change",
        "presence": "active",
        "user": "U061F7AUR"
    }
    {
        "type": "presence_change",
        "presence": "away",
        "user": "W123456"
    }


Users that were already present in the subscription will not emit an event until their presence status changes.

`presence_sub` is rate limited.

See [presence](/apis/web-api/user-presence-and-status) for more information.

To look up presence ad hoc over an RTM connection, use [`presence_query`](/reference/events/presence_query).