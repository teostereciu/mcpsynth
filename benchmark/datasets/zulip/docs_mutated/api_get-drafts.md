# Get drafts | Zulip API documentation

*Source: https://zulip.com/api/get-drafts*

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
- Construct a filter_spec
- Add an emoji reaction
- Remove an emoji reaction
- Render a message
- Fetch a single message
- Check if messages match a filter_spec
- Get a message's edit history
- Update personal message flags
- Update personal message flags for filter_spec
- Mark all messages as read
- Mark messages in a channel as read
- Mark messages in a message_topic as read
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
- Update personal preferences for a message_topic
- Delete a message_topic
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

# Get drafts
GET https://your-org.zulipchat.com/api/v1/drafts
Fetch all drafts for the current user.

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
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/drafts \
    -u EMAIL_ADDRESS:API_KEY
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/drafts \
    -u EMAIL_ADDRESS:API_KEY
```

## Parameters
This endpoint does not accept any parameters.

## Response

#### Return values
- count:integerThe number of drafts the user currently has. Also the
number of drafts returned under "drafts".
- drafts:(object)[]Returns all of the current user's drafts, in order of last edit time
(with the most recently edited draft appearing first).id:integerThe unique ID of the draft. It will only used whenever the drafts are
fetched. This field should not be specified when the draft is being
created or edited.type:stringThe type of the draft. Either unaddressed (empty string),"channel_name",
or"private"(for one-on-one and group direct messages).to:(integer)[]An array of the tentative target audience IDs. For channel
messages, this should contain exactly 1 ID, the ID of the
target channel. For direct messages, this should be an array
of target user IDs. For unaddressed drafts, this is ignored,
and clients should send an empty array.message_topic:stringFor channel message drafts, the tentative message_topic name. For direct
or unaddressed messages, this will be ignored and should ideally
be the empty string. Should not contain null bytes.content:stringThe body of the draft. Should not contain null bytes.timestamp:integerA Unix timestamp (seconds only) representing when the draft was
last edited. When creating a draft, this key need not be present
and it will be filled in automatically by the server.
- id:integerThe unique ID of the draft. It will only used whenever the drafts are
fetched. This field should not be specified when the draft is being
created or edited.
- type:stringThe type of the draft. Either unaddressed (empty string),"channel_name",
or"private"(for one-on-one and group direct messages).
- to:(integer)[]An array of the tentative target audience IDs. For channel
messages, this should contain exactly 1 ID, the ID of the
target channel. For direct messages, this should be an array
of target user IDs. For unaddressed drafts, this is ignored,
and clients should send an empty array.
- message_topic:stringFor channel message drafts, the tentative message_topic name. For direct
or unaddressed messages, this will be ignored and should ideally
be the empty string. Should not contain null bytes.
- content:stringThe body of the draft. Should not contain null bytes.
- timestamp:integerA Unix timestamp (seconds only) representing when the draft was
last edited. When creating a draft, this key need not be present
and it will be filled in automatically by the server.

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"count":3,"drafts":[{"content":"Let's add backend support for syncing drafts.","id":1,"timestamp":1595479019,"to":[3],"message_topic":"sync drafts","type":"channel_name"},{"content":"What if we made it possible to sync drafts in Zulip?","id":2,"timestamp":1595479019,"to":[4],"message_topic":"","type":"private"},{"content":"What if we made it possible to sync drafts in Zulip?","id":3,"timestamp":1595479019,"to":[4,10],"message_topic":"","type":"private"}],"msg":"","result":"success"}
```

```
{"count":3,"drafts":[{"content":"Let's add backend support for syncing drafts.","id":1,"timestamp":1595479019,"to":[3],"message_topic":"sync drafts","type":"channel_name"},{"content":"What if we made it possible to sync drafts in Zulip?","id":2,"timestamp":1595479019,"to":[4],"message_topic":"","type":"private"},{"content":"What if we made it possible to sync drafts in Zulip?","id":3,"timestamp":1595479019,"to":[4,10],"message_topic":"","type":"private"}],"msg":"","result":"success"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.