# Update personal message flags for narrow | Zulip API documentation

*Source: https://zulip.com/api/update-message-flags-for-narrow*

---

# Zulip homepage

# API documentation home

## REST API
- Overview
- Installation instructions
- API keys
- Configuring the Python bindings
- HTTP headers
- Error handling
- Roles and permissions
- Group-setting values
- Message formatting
- Zulip URLs
- Client libraries
- API changelog

#### Messages
- Send a message
- Upload a file
- Edit a message
- Delete a message
- Get messages
- Construct a narrow
- Add an emoji reaction
- Remove an emoji reaction
- Render a message
- Fetch a single message
- Check if messages match a narrow
- Get a message's edit history
- Update personal message flags
- Update personal message flags for narrow
- Mark all messages as read
- Mark messages in a channel as read
- Mark messages in a topic as read
- Get a message's read receipts
- Get temporary URL for an uploaded file
- Report a message

#### Scheduled messages
- Get scheduled messages
- Create a scheduled message
- Edit a scheduled message
- Delete a scheduled message

#### Message reminders
- Create a message reminder
- Get reminders
- Delete a reminder

#### Drafts
- Get drafts
- Create drafts
- Edit a draft
- Delete a draft
- Get all saved snippets
- Create a saved snippet
- Edit a saved snippet
- Delete a saved snippet

#### Navigation views
- Get all navigation views
- Add a navigation view
- Update the navigation view
- Remove a navigation view

#### Channels
- Get subscribed channels
- Subscribe to a channel
- Unsubscribe from a channel
- Get subscription status
- Get channel subscribers
- Get a user's subscribed channels
- Update a subscription setting
- Bulk update subscription settings
- Get all channels
- Get a channel by ID
- Get channel ID
- Create a channel
- Update a channel
- Archive a channel
- Get channel's email address
- Get topics in a channel
- Topic muting
- Update personal preferences for a topic
- Delete a topic
- Add a default channel
- Remove a default channel
- Create a channel folder
- Get channel folders
- Reorder channel folders
- Update a channel folder

#### Users
- Get a user
- Get a user by email
- Get own user
- Get users
- Create a user
- Update a user
- Update a user by email
- Deactivate a user
- Deactivate own user
- Reactivate a user
- Get a user's status
- Update your status
- Update user status
- Set "typing" status
- Set "typing" status for message editing
- Get a user's presence
- Get presence of all users
- Update your presence
- Get attachments
- Delete an attachment
- Update settings
- Get user groups
- Create a user group
- Update a user group
- Deactivate a user group
- Update user group members
- Update subgroups of a user group
- Get user group membership status
- Get user group members
- Get subgroups of a user group
- Mute a user
- Unmute a user
- Get all alert words
- Add alert words
- Remove alert words
- Regenerate your API key
- Get a bot's API key
- Regenerate a bot's API key

#### Invitations
- Get all invitations
- Send invitations
- Create a reusable invitation link
- Resend an email invitation
- Revoke an email invitation
- Revoke a reusable invitation link

#### Server & organizations
- Get server settings
- Get linkifiers
- Add a linkifier
- Update a linkifier
- Remove a linkifier
- Reorder linkifiers
- Add a code playground
- Remove a code playground
- Get all custom emoji
- Upload custom emoji
- Deactivate custom emoji
- Get all custom profile fields
- Reorder custom profile fields
- Create a custom profile field
- Update realm-level defaults of user settings
- Get all data exports
- Create a data export
- Get data export consent state
- Test welcome bot custom message

#### Real-time events
- Real time events API
- Register an event queue
- Get events from an event queue
- Delete an event queue

#### Specialty endpoints
- Fetch an API key (production)
- Fetch an API key (development only)
- Fetch an API key (JWT)
- Register a logged-in device
- Remove a registered device
- Send an E2EE test notification to mobile device(s)
- Register E2EE push device
- Register E2EE push device to bouncer
- Mobile notifications
- Send a test notification to mobile device(s)
- Add an APNs device token
- Remove an APNs device token
- Add an FCM registration token
- Remove an FCM registration token
- Create BigBlueButton video call
- Create Constructor Groups video call
- Create Nextcloud Talk video call
- Outgoing webhook payloads

# Back to Zulip

# Update personal message flags for narrow
POST https://your-org.zulipchat.com/api/v1/messages/flags/narrow
Add or remove personal message flags likereadandstarredon a range of messages within a narrow.
See alsothe endpoint for updating flags on specific message
IDs.
Changes: New in Zulip 6.0 (feature level 155).

## Usage examples
curl
- curl
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/messages/flags/narrow \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode anchor=43 \
    --data-urlencode num_before=4 \
    --data-urlencode num_after=8 \
    --data-urlencode 'narrow=[{"operand": "Denmark", "operator": "channel"}]' \
    --data-urlencode op=add \
    --data-urlencode flag=read
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/messages/flags/narrow \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode anchor=43 \
    --data-urlencode num_before=4 \
    --data-urlencode num_after=8 \
    --data-urlencode 'narrow=[{"operand": "Denmark", "operator": "channel"}]' \
    --data-urlencode op=add \
    --data-urlencode flag=read
```

## Parameters
anchorstringrequired
Integer message ID to anchor updating of flags. Supports special
string values for when the client wants the server to compute the anchor
to use:
- newest: The most recent message.
- oldest: The oldest message.
- first_unread: The oldest unread message matching the
  query, if any; otherwise, the most recent message.
include_anchorbooleanoptional
Whether a message with the specified ID matching the narrow
should be included in the update range.
Defaults totrue.
num_beforeintegerrequired
Limit the number of messages preceding the anchor in the
update range. The server may decrease this to bound
transaction sizes.
num_afterintegerrequired
Limit the number of messages following the anchor in the
update range. The server may decrease this to bound
transaction sizes.
narrow(object | (string)[])[]required

```
[{"operand": "Denmark", "operator": "channel"}]
```
The narrow you want update flags within. See how toconstruct a narrow.
Note that, when adding thereadflag to messages, clients should
consider including a narrow with theis:unreadfilter as an
optimization. Including that filter takes advantage of the fact that
the server has a database index for unread messages.
Changes: Seechanges sectionof search/narrow filter documentation.
Defaults to[].
opstringrequired
Whether toaddthe flag orremoveit.
Must be one of:"add","remove".
flagstringrequired
The flag that should be added/removed. Seeavailable
flags.

## Response

#### Return values
- processed_count:integerThe number of messages that were within the
update range (at mostnum_before + 1 +
num_after).
- updated_count:integerThe number of messages where the flag's
value was changed (at mostprocessed_count).
- first_processed_id:integer | nullThe ID of the oldest message within the
update range, ornullif the range was
empty.
- last_processed_id:integer | nullThe ID of the newest message within the
update range, ornullif the range was
empty.
- found_oldest:booleanWhether the update range reached backward
far enough to include very oldest message
matching the narrow (used by clients doing a
bulk update to decide whether to issue
another request anchored atfirst_processed_id).
- found_newest:booleanWhether the update range reached forward far
enough to include very oldest message
matching the narrow (used by clients doing a
bulk update to decide whether to issue
another request anchored atlast_processed_id).
- ignored_because_not_subscribed_channels:(integer)[]Only present if the flag isreadand the operation isremove.Zulip has an invariant that all unread messages must be in channels
the user is subscribed to. This field will contain a list of the
channels whose messages were skipped to mark as unread because the
user is not subscribed to them.Changes: New in Zulip 10.0 (feature level 355).

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"first_processed_id":35,"found_newest":true,"found_oldest":false,"ignored_because_not_subscribed_channels":[12,13,9],"last_processed_id":55,"msg":"","processed_count":11,"result":"success","updated_count":8}
```

```
{"first_processed_id":35,"found_newest":true,"found_oldest":false,"ignored_because_not_subscribed_channels":[12,13,9],"last_processed_id":55,"msg":"","processed_count":11,"result":"success","updated_count":8}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.