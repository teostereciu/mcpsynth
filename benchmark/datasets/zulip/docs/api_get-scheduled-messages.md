# Get scheduled messages | Zulip API documentation

*Source: https://zulip.com/api/get-scheduled-messages*

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

# Get scheduled messages
GET https://your-org.zulipchat.com/api/v1/scheduled_messages
Fetch allscheduled messagesfor
the current user.
Scheduled messages are messages the user has scheduled to be
sent in the future via the send later feature.
Changes: New in Zulip 7.0 (feature level 173).

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
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/scheduled_messages \
    -u EMAIL_ADDRESS:API_KEY
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/scheduled_messages \
    -u EMAIL_ADDRESS:API_KEY
```

## Parameters
This endpoint does not accept any parameters.

## Response

#### Return values
- scheduled_messages:(object)[]Returns all of the current user's undelivered scheduled
messages, ordered byscheduled_delivery_timestamp(ascending).scheduled_message_id:integerThe unique ID of the scheduled message, which can be used to
modify or delete the scheduled message.This is different from the unique ID that the message will have
after it is sent.type:stringThe type of the scheduled message. Either"stream"or"private".to:integer | (integer)[]The scheduled message's tentative target audience.For channel messages, it will be the unique ID of the target
channel. For direct messages, it will be an array with the
target users' IDs.topic:stringOnly present iftypeis"stream".The topic for the channel message.content:stringThe content/body of the scheduled message, inZulip-flavored Markdownformat.SeeMarkdown message formattingfor details on Zulip's HTML format.rendered_content:stringThe content/body of the scheduled message rendered in HTML.scheduled_delivery_timestamp:integerThe UNIX timestamp for when the message will be sent
by the server, in UTC seconds.failed:booleanWhether the server has tried to send the scheduled message
and it failed to successfully send.Clients that support unscheduling and editing scheduled messages
should display scheduled messages with"failed": truewith an
indicator that the server failed to send the message at the
scheduled time, so that the user is aware of the failure and can
get the content of the scheduled message.Changes: New in Zulip 7.0 (feature level 181).
- scheduled_message_id:integerThe unique ID of the scheduled message, which can be used to
modify or delete the scheduled message.This is different from the unique ID that the message will have
after it is sent.
- type:stringThe type of the scheduled message. Either"stream"or"private".
- to:integer | (integer)[]The scheduled message's tentative target audience.For channel messages, it will be the unique ID of the target
channel. For direct messages, it will be an array with the
target users' IDs.
- topic:stringOnly present iftypeis"stream".The topic for the channel message.
- content:stringThe content/body of the scheduled message, inZulip-flavored Markdownformat.SeeMarkdown message formattingfor details on Zulip's HTML format.
- rendered_content:stringThe content/body of the scheduled message rendered in HTML.
- scheduled_delivery_timestamp:integerThe UNIX timestamp for when the message will be sent
by the server, in UTC seconds.
- failed:booleanWhether the server has tried to send the scheduled message
and it failed to successfully send.Clients that support unscheduling and editing scheduled messages
should display scheduled messages with"failed": truewith an
indicator that the server failed to send the message at the
scheduled time, so that the user is aware of the failure and can
get the content of the scheduled message.Changes: New in Zulip 7.0 (feature level 181).

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"msg":"","result":"success","scheduled_messages":[{"content":"Hi","failed":false,"rendered_content":"<p>Hi</p>","scheduled_delivery_timestamp":1681662420,"scheduled_message_id":27,"to":14,"topic":"Introduction","type":"stream"}]}
```

```
{"msg":"","result":"success","scheduled_messages":[{"content":"Hi","failed":false,"rendered_content":"<p>Hi</p>","scheduled_delivery_timestamp":1681662420,"scheduled_message_id":27,"to":14,"topic":"Introduction","type":"stream"}]}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.