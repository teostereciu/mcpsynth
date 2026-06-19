# User presence and status

*Source: https://docs.slack.dev/apis/web-api/user-presence-and-status*

---

Slack users can toggle whether they are marked active or away. They can also set their own custom status, informing their workspace not only that they are _at lunch_ , but exactly what they are eating.

## Custom status​

Users can declare their status by selecting a custom emoji icon and string of text to represent their "current status" — maybe they're in another office, on the good old telephone, sailing, vacationing in the sticks, or possibly eaten by a grue.

Some users want to fly the freak flag and use this space to wax poetic while others won't touch the stuff, or only in the most perfunctory way.

We encourage developers to embrace all the ways users and workspaces enjoy utilizing custom status. Slack is where workplay happens.

Custom status is part of a user's profile and setting status requires the `users.profile:write` scope. At this time, bot users do not have a user profile and do not have a status.

Admins on paid teams may also set a user's status by passing the `user` parameter to the [`users.profile.set`](/reference/methods/users.profile.set) method.

### Reading statuses​

Determine a user's currently set custom status by consulting their profile. You'll find profiles attached to user objects returned by [`users.list`](/reference/methods/users.list) and [`users.info`](/reference/methods/users.info). Both methods require the `users:read` OAuth scope.

More directly retrieve status for a specific user with [`users.profile.get`](/reference/methods/users.profile.get) with the `users.profile:read` scope.

A user's custom status is represented by the `status_text`, `status_emoji`, and `status_expiration` profile attributes.

  * `status_text` \- a string of no more than 100 characters; does not support markup or other formatting, like user mentions. May contain `:emoji:` references.
  * `status_emoji` \- a string corresponding to an emoji installed on the workspace. Animated emoji will appear frozen. When clearing the attribute, a default emoji (currently `💬` / `:speech_balloon:`) will be selected for the user.
  * `status_expiration` \- an integer specifying seconds since the epoch, more commonly known as "UNIX time". When it becomes this time, the status will be reset. When `0` or omitted, the status does not expire.


To be notified when status and other profile fields change, subscribe to [`user_change`](/reference/events/user_change) events in the [Events API](/apis/events-api/) or use the [RTM API](/legacy/legacy-rtm-api) to stream and monitor.

### Writing custom statuses​

Set a user's custom status by using their access token with [`users.profile.set`](/reference/methods/users.profile.set) and the `users.profile:write` scope.

You'll need to provide the `profile` parameter a URL-encoded JSON string containing at least the `status_text` attribute.

For example, to set a non-expiring custom status of `riding a train` with an emoji set to this idyllic scene: `🚞`, build a JSON payload like this:


    {
        "status_text": "riding a train",
        "status_emoji": ":mountain_railway:",
        "status_expiration": 0
    }


Next, place the custom status fields within the user's `profile` and use [`users.profile.set`](/reference/methods/users.profile.set). In this example, we're posting with JSON and using a user token :


    POST /api/users.profile.set
    Host: slack.com
    Content-type: application/json; charset=utf-8
    Authorization: Bearer xoxp_secret_token
    {
        "profile": {
            "status_text": "riding a train",
            "status_emoji": ":mountain_railway:",
            "status_expiration": 0
        }
    }


As with other profile fields, these fields may be set on their own or while updating multiple profile fields.

To unset a user's custom status, set both `status_text` and `status_emoji` to empty strings: `""`.

When sending a `application/x-www-form-urlencoded`-based HTTP POST instead, you must provide the `profile` parameter as a URL-encoded string of JSON. We recommend using `application/json` to avoid any encoding errors.

### Expiring custom statuses​

Automatically expire a custom status by setting `status_expiration` to an integer-based Unix timestamp, like `1532627506`.

For example, to set a custom status of `🚞 riding the train home` and have it expire on July 26th, 2018 at 17:51:46 UTC, construct this JSON payload:


    {
        "status_text": "riding the train home",
        "status_emoji": ":mountain_railway:",
        "status_expiration": 1532627506
    }


That's how to sync status with calendars, cubicles, conference calls, and bathroom stalls.

* * *

## User presence​

A user can have one of two possible presence values, `active` or `away`. A user is active if they have at least one client connected to Slack, and they are not marked as "away". There are two ways a user can be marked as away: automatic and manual.

### Automatic away​

The Slack message servers will automatically detect activity in the client. After 10 minutes with no activity, the user is automatically marked as `away`. There is some additional nuance to that dependent on the client, explained in detail in our [Help Center](https://slack.com/help/articles/201864558#desktop-3).

These auto-away rules do not apply to [Bot Users](/authentication/tokens#bot).

### Manual away​

An application can call [`users.setPresence`](/reference/methods/users.setPresence) to manually mark a user as `away` or `auto`. A manual status set using this method will persist between connections.

A manual `away` status set using this method overrides the automatic presence determined by the message server.

Setting presence back to `auto` indicates that the automatic status should be used instead. There's no way to force a user status to `active`.

## Bot presence​

[Bot users](/authentication/tokens#bot) have their own form of being present on Slack.

When marked `away`, bots will have a grey circle next to their name. Many users interpret this demarcation to mean your bot is not currently available.

And when they are `active`, bots will have a green dot there. Users have been known to consider your green dot a badge of conversational readiness.

It's either/or. `away` or `active`. Grey or green (or maybe grey and orange — the color of the active dot may vary when [different Slack client themes](https://slack.com/intl/en-ie/help/articles/205166337-Change-your-Slack-theme) are used).

Please don't use presence to telegraph Morse code or teach your bot to speak the binary language of moisture vaporators. Use [`chat.postMessage`](/reference/methods/chat.postMessage) for that.

### Events API bots​

If your bot user runs on the [Events API](/apis/events-api/), you can only toggle your bot's `active` or `away` status by [managing your app](https://api.slack.com/apps) and its _Bot Users_ panel, or for apps published in the Slack Marketplace, on the _Live App Settings_ panel.

When set to _Off_ , your bot user is only marked as online if it's connected to the RTM API.

When set to _On_ , your bot user will be marked as _active_ and present. That green dot is all yours. Just toggle back _Off_ again to be marked _away_.

Your bot user's [profile](/reference/methods/users.profile.get) will include a `always_active` field set to `true`. Counter-intuitively, your bot's `presence` field will remain `away`. That's the bad news.

The good news is that `always_active` will be interpreted by Slack clients as if the bot user's presence were `active`. Yes, you're awarded that green dot.

### RTM bots​

If your bot user runs on the [RTM API](/legacy/legacy-rtm-api), your bot will be marked `active` to users whenever connected to the RTM API.

Bots cannot set their presence to `active` with [`users.setPresence`](/reference/methods/users.setPresence). RTM bots _can_ use it to set it to `away`. Or you can always automatically mark your bot as `away` by disconnecting from your websocket.

## Determining user presence​

RTM API Presence is now only available via subscription

As of January 2018, [`presence_change`](/reference/events/presence_change) events are not dispatched without [_presence subscriptions_](/apis/web-api/user-presence-and-status) established with [`presence_sub`](/reference/events/presence_sub). Relatedly, current user presence status is no longer communicated in [`rtm.start`](/reference/methods/rtm.start). [Learn more](/changelog/2018-01-presence-present-and-future).

### Presence subscriptions over RTM​

Presence subscriptions are required to track `presence_change` events over RTM.

Subscribe to `presence_change` events for specific users by sending a [`presence_sub`](/reference/events/presence_sub) event into the websocket.

For instance, to subscribe to `presence_change` events for users `U123456` and `W123456`, write the following JSON blob into an established websocket:


    {
        "type": "presence_sub",
        "ids": [
            "U123456",
            "W123456"
        ]
    }


The message server will respond with `presence_change` events indicating the current presence state of any users added to the presence subscription.

Here's what you need to know about presence subscriptions:

  * You must declare your entire list of user IDs to subscribe to in _**each**_ request.
    * Add users by appending them to your array of `ids`.
    * Remove users by removing them from your array of `ids`.
  * Subscribing to all user's presence events requires specifying every user's ID. This is not recommended, especially on large workspaces.
    * For best results, limit subscriptions to only those users you absolutely need presence information for. 500 users is a good maximum.
  * Presence subscriptions work best with batched `presence_change` events.
  * Upon connecting, your app will have no presence subscriptions.
  * Presence subscriptions only last the duration of a websocket session. Disconnecting means needing to subscribe again.
  * By specifying an [Enterprise org](/enterprise) user ID belonging to a user on another workspace within the same Enterprise organization, your app can subscribe to cross-workspace `presence_change` events.


Presence subscriptions are now effectively required, as of January 2018. [Learn more](/changelog/2018-01-presence-present-and-future).

`presence_sub` is rate limited and there are upper bounds to the amount of data posted in a single event.

### Presence querying with the RTM API​

Writing a [`presence_query`](/reference/events/presence_query) event to the WebSocket will perform a query operation for a list of up to 500 user IDs.

To look up users `U123456` and `W123456`, send a query like:


    {
        "type": "presence_query",
        "ids": [
            "U123456",
            "W123456"
        ]
    }


In response, you'll receive [`presence_change`](/reference/events/presence_change) events for the matching users.

`presence_query` is rate limited and there are upper bounds to the amount of data posted in a single event.

### Presence querying with the Web API​

When using our [Web API](/apis/web-api/), you can call the [`users.getPresence`](/reference/methods/users.getPresence) method to get the user's current presence value.

### Presence subscriptions over Events API​

Presence-related events cannot be tracked using the [Events API](/apis/events-api/) at this time.

### Batched presence events​

Traditionally, using the [Real Time Messaging API](/legacy/legacy-rtm-api) the initial call to [`rtm.start`](/reference/methods/rtm.start) or [`rtm.connect`](/reference/methods/rtm.connect) would include the current presence value for every member of your workspace. If their presence value changes after that, a [`presence_change`](/reference/events/presence_change) event would be sent.

Now presence events must be batched together into a special version of the `presence_change` event that includes a `users` array instead of a singular `user` field. You must enable this new behavior by passing the `batch_presence_aware=1` parameter to `rtm.start` or `rtm.connect`. `presence_change` events will otherwise no longer dispatch after November 15, 2017.

Initial presence state is no longer described when connecting to [`rtm.start`](/reference/methods/rtm.start).