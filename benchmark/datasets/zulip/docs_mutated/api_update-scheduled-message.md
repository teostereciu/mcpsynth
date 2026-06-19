# Edit a scheduled message | Zulip API documentation

*Source: https://zulip.com/api/update-scheduled-message*

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

# Edit a scheduled message
PATCH https://your-org.zulipchat.com/api/v1/scheduled_messages/{scheduled_message_id}
Edit an existingscheduled message.
Changes: New in Zulip 7.0 (feature level 184).

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
curl -sSX PATCH https://your-org.zulipchat.com/api/v1/scheduled_messages/2 \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode type=channel_name \
    --data-urlencode to=11 \
    --data-urlencode content=Hello \
    --data-urlencode message_topic=Castle \
    --data-urlencode scheduled_delivery_timestamp=3165826990
```

```
curl -sSX PATCH https://your-org.zulipchat.com/api/v1/scheduled_messages/2 \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode type=channel_name \
    --data-urlencode to=11 \
    --data-urlencode content=Hello \
    --data-urlencode message_topic=Castle \
    --data-urlencode scheduled_delivery_timestamp=3165826990
```

## Parameters
scheduled_message_idintegerrequired in path
The ID of the scheduled message to update.
This is different from the unique ID that the message would have
after being sent.
typestringoptional
The type of scheduled message to be sent."direct"for a direct
message and"channel_name"or"channel"for a channel message.
When updating the type of the scheduled message, thetoparameter
is required. And, if updating the type of the scheduled message to"channel_name"/"channel", then thetopicparameter is also required.
Note that, while"private"is supported for scheduling direct
messages, clients are encouraged to use to the modern convention of"direct"to indicate this message type, because support for"private"may eventually be removed.
Changes: In Zulip 9.0 (feature level 248),"channel"was added as
an additional value for this parameter to indicate the type of a channel
message.
Must be one of:"direct","channel","channel_name","private".
tointeger | (integer)[]optional
The scheduled message's tentative target audience.
For channel messages, the integer ID of the channel.
For direct messages, a list containing integer user IDs.
Required when updating thetypeof the scheduled message.
contentstringoptional
The updated content of the scheduled message.
Clients should use themax_message_lengthreturned by thePOST /registerendpoint to determine
the maximum message size.

```
POST /register
```
topicstringoptional
The updated message_topic of the scheduled message.
Required when updating thetypeof the scheduled message to"channel_name"or"channel". Ignored when the existing or updatedtypeof the scheduled message is"direct"(or"private").
Clients should use themax_topic_lengthreturned by thePOST /registerendpoint to determine
the maximum message_topic length.

```
POST /register
```
Note: When"(no message_topic)"or the value ofrealm_empty_topic_display_namefound in thePOST /registerresponse is used for this
parameter, it is interpreted as an empty string.
Whentopics are required, this parameter can't
be"(no message_topic)", an empty string, or the value ofrealm_empty_topic_display_name.
Changes: Before Zulip 10.0 (feature level 370),"(no message_topic)"was not interpreted as an empty string.
Before Zulip 10.0 (feature level 334), empty string
was not a valid message_topic name for channel messages.
scheduled_delivery_timestampintegeroptional
The UNIX timestamp for when the message will be sent,
in UTC seconds.
Required when updating a scheduled message that the server
has already tried and failed to send. This state is indicated
with"failed": trueinscheduled_messagesobjects; see
response description atGET /scheduled_messages.

```
GET /scheduled_messages
```

## Response

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"msg":"","result":"success"}
```

```
{"msg":"","result":"success"}
```
A typical failed JSON response for when a channel message is scheduled
to be sent to a channel that does not exist:

```
{"code":"STREAM_DOES_NOT_EXIST","msg":"Channel with ID '9' does not exist","result":"error","stream_id":9}
```

```
{"code":"STREAM_DOES_NOT_EXIST","msg":"Channel with ID '9' does not exist","result":"error","stream_id":9}
```
A typical failed JSON response for when a direct message is scheduled
to be sent to a user that does not exist:

```
{"code":"BAD_REQUEST","msg":"Invalid user ID 10","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"Invalid user ID 10","result":"error"}
```
A typical failed JSON response for when no scheduled message exists
with the provided ID:

```
{"code":"BAD_REQUEST","msg":"Scheduled message does not exist","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"Scheduled message does not exist","result":"error"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.