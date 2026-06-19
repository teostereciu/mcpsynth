# channel_id_changed

*Source: https://docs.slack.dev/reference/events/channel_id_changed*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`Events`](/apis/events-api)

## Usage info​

This example includes both the [event wrapper](/apis/events-api/#callback-field) and the [event structure](/apis/events-api/#event-type-structure) for the `channel_id_changed` event.


    {
        "token": "XXYYZZ",
        "team_id": "T123ABC456",
        "api_app_id": "A123ABC456",
        "event": {
            "type": "channel_id_changed",
            "old_channel_id": "G012Y48650T",
            "new_channel_id": "C012Y48650T",
            "event_ts": "1612206778.000000"
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


A `channel_id_changed` event is sent when a user initiates sharing a private channel externally with [Slack Connect](/apis/slack-connect/). When a private channel is shared, the existing private channel's unique channel ID _changes_ to a new identifier permanently. This event is only sent for private channels your app has access to.

When receiving this event, you should update any records you have stored about the original private channel ID (`old_channel_id`) with this `new_channel_id`. From now on, all messages and other happenstance around the channel will be associated with the new ID. If you attempt to post messages, perform lookups, or other operations with the channel you will need the channel's new ID.

While there are other reasons a channel ID may change, this event currently applies to only the circumstances with Slack Connect described above.