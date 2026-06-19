# emoji_changed

*Source: https://docs.slack.dev/reference/events/emoji_changed*

---

## Facts

**Required Scopes**

[`emoji:read`](/reference/scopes/emoji.read)

**Compatible APIs**

[`Events`](/apis/events-api)

[`RTM`](/legacy/legacy-rtm-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `emoji_changed` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "emoji_changed",
            "subtype": "remove",
            "names": [
                "picard_facepalm"
            ],
            "event_ts": "1361482916.000004"
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


The `emoji_changed` event is sent to all connections for a workspace when that a custom emoji is updated. When they receive this event, clients may either process the `subtype` if present and of a known value or should update their local cache of emoji by calling [the emoji.list method](/reference/methods/emoji.list) again.

An `emoji_changed` event will always have an `event_ts` field specified in addition to `type`. `subtype` is optional and the presence of additional fields depends on `subtype`.

## `emoji_changed` subtypes​

An `emoji_changed` event may have a subtype specified. An absent subtype or unrecognized subtype should be handled by reloading all emojis via [the emoji.list method](/reference/methods/emoji.list).

The following is the current list of defined subtypes:

### add​


    {
        "type": "emoji_changed",
        "subtype": "add",
        "name": "picard_facepalm",
        "value": "https://my.slack.com/emoji/picard_facepalm/db8e287430eaa459.gif",
        "event_ts" : "1361482916.000004"
    }


An emoji has been added to the emoji list. Note that, like in `emoji.list`, `value` is either the URI to fetch the image from or an alias to an existing name as indicated by the `alias:` pseudo-protocol.

### remove​


    {
        "type": "emoji_changed",
        "subtype": "remove",
        "names": ["picard_facepalm"],
        "event_ts" : "1361482916.000004"
    }


One or more emojis have been removed from the emoji list. Note that `names` is always an array of at least one name, and that aliased emoji entries are always removed when the emoji name they alias to is removed.

### rename​


    {
        "type": "emoji_changed",
        "subtype": "rename",
        "old_name": "grin",
        "new_name": "cheese-grin",
        "value": "https://my.slack.com/emoji/picard_facepalm/db8e287430eaa459.gif",
        "event_ts" : "1361482916.000004"
    }


An emoji has been renamed. It will contain the `old_name` and `new_name`.