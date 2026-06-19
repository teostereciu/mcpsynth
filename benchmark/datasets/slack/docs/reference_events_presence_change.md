# presence_change

*Source: https://docs.slack.dev/reference/events/presence_change*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

These examples include both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `presence_change` event.

Single-user presence change event:


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "presence_change",
            "user": "U123ABC456",
            "presence": "away"
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


Multiple-user batch presence change event (still one user shown; use the [`apps.event.authorizations.list`](/reference/methods/apps.event.authorizations.list) API method to find all authorizations):


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "presence_change",
            "users": [
                "U123ABC456",
                "U012EA2U1"
            ],
            "presence": "away"
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


The `presence_change` event is sent to connections for a workspace when a user changes [presence status](/apis/web-api/user-presence-and-status) and the app has subscribed using [`presence_sub`](/reference/events/presence_sub). Clients can use this to update their local list of users' presence.

RTM API Presence is now only available via subscription.

As of January 2018, [`presence_change`](/reference/events/presence_change) events are not dispatched without [_presence subscriptions_](/apis/web-api/user-presence-and-status) established with [`presence_sub`](/reference/events/presence_sub). Relatedly, current user presence status is no longer communicated in [`rtm.start`](/reference/methods/rtm.start). [Learn more](/changelog/2018-01-presence-present-and-future).

If a user updates their presence manually, the [`manual_presence_change`](/reference/events/manual_presence_change) event will also be sent to all connected clients for that user.

There are **two forms** of this event. When only one user's presence is being communicated, you'll receive a `user` field with a single user ID present within. This form is deprecated.

Pass the `batch_presence_aware=1` parameter to [`rtm.start`](/reference/methods/rtm.start) or [`rtm.connect`](/reference/methods/rtm.connect) to instruct the Slack message server to batch your presence messages and send a `users` attribute instead, containing an array of users changing to the same status.

Sometimes you'll get a single event for a single user but if you use `batch_presence_aware=1`, that single user event will be single item in the `users` array.

**_In case you missed that_ : if you send `batch_presence_aware=1` then the shape of `presence_change` events _changes_. Instead of a string-based `user` field, you'll get `users`, an array.**

If you're writing a library that supports `presence_change` events, you should be prepared to handle **both** kinds of presence events.