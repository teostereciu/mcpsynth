# presence_query

*Source: https://docs.slack.dev/reference/events/presence_query*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

Ask the message server about the current [presence status](/apis/web-api/user-presence-and-status) for the specified list of users.

Instead of _receiving_ this event type, your app must post it into the websocket. Present an array labeled `ids` containing all of the user IDs you want presence status for, up to 500.

To use this event, you'll need to first connect with [`rtm.connect`](/reference/methods/rtm.connect) or [`rtm.start`](/reference/methods/rtm.start).

For instance, to query presence status for users `U123456` and `W123456`, present JSON like so:


    {
        "type": "presence_query",
        "ids": [
            "U061F7AUR",
            "W123456"
        ]
    }


In response, you'll receive singular or batch [`presence_change`](/reference/events/presence_change) events declaring the current presence status of each queried user ID.


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


`presence_query` is rate limited.

See [presence](/apis/web-api/user-presence-and-status) for more information.

To subscribe to `presence_change` events, use [`presence_sub`](/reference/events/presence_sub).