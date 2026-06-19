# Update user status | Zulip API documentation

*Source: https://zulip.com/api/update-status-for-user*

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

# Update user status
This endpoint is only available to organization administrators.
POST https://your-org.zulipchat.com/api/v1/users/{user_id}/status
Administrator endpoint for changing thestatusof
another user.
Changes: Prior to Zulip 12.0 (feature level 473), only
bots could not access this API endpoint, regardless of the
role of the bot.
New in Zulip 11.0 (feature level 407).

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
curl -sSX POST https://your-org.zulipchat.com/api/v1/users/12/status \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'status_text=on vacation' \
    --data-urlencode emoji_name=car \
    --data-urlencode emoji_code=1f697 \
    --data-urlencode reaction_type=unicode_emoji
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/users/12/status \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'status_text=on vacation' \
    --data-urlencode emoji_name=car \
    --data-urlencode emoji_code=1f697 \
    --data-urlencode reaction_type=unicode_emoji
```

## Parameters
user_idintegerrequired in path
The target user's ID.
status_textstringoptional

```
"on vacation"
```
The text content of the status message. Sending the empty string
will clear the user's status.
Note: The limit on the size of the message is 60 Unicode code points.
emoji_namestringoptional
The name for the emoji to associate with this status.
Changes: New in Zulip 5.0 (feature level 86).
emoji_codestringoptional
A unique identifier, defining the specific emoji codepoint requested,
within the namespace of thereaction_type.
Changes: New in Zulip 5.0 (feature level 86).
reaction_typestringoptional

```
"unicode_emoji"
```
A string indicating the type of emoji. Each emojireaction_typehas an independent namespace for values ofemoji_code.
Must be one of the following values:
- unicode_emoji: In this namespace,emoji_codewill be a
  dash-separated hex encoding of the sequence of Unicode codepoints
  that define this emoji in the Unicode specification.
- realm_emoji: In this namespace,emoji_codewill be the ID of
  the uploadedcustom emoji.
- zulip_extra_emoji: These are special emoji included with Zulip.
  In this namespace,emoji_codewill be the name of the emoji (e.g.
  "zulip").
Changes: New in Zulip 5.0 (feature level 86).

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
An example JSON error response user making request does not have permission to update other user's status.:

```
{"code":"BAD_REQUEST","msg":"Insufficient permission","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"Insufficient permission","result":"error"}
```
An example JSON error response when no changes were requested:

```
{"code":"BAD_REQUEST","msg":"Client did not pass any new values.","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"Client did not pass any new values.","result":"error"}
```
An example JSON error response when thestatus_textmessage exceeds the limit of
60 characters:

```
{"code":"BAD_REQUEST","msg":"status_text is too long (limit: 60 characters)","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"status_text is too long (limit: 60 characters)","result":"error"}
```
An example JSON error response whenemoji_nameis not specified
butemoji_codeorreaction_typeis specified:

```
{"code":"BAD_REQUEST","msg":"Client must pass emoji_name if they pass either emoji_code or reaction_type.","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"Client must pass emoji_name if they pass either emoji_code or reaction_type.","result":"error"}
```
An example JSON error response when the emoji name does not exist:

```
{"code":"BAD_REQUEST","msg":"Emoji 'invalid' does not exist","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"Emoji 'invalid' does not exist","result":"error"}
```
An example JSON error response when the emoji name is invalid:

```
{"code":"BAD_REQUEST","msg":"Invalid emoji name.","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"Invalid emoji name.","result":"error"}
```
An example JSON error response when the custom emoji is invalid:

```
{"code":"BAD_REQUEST","msg":"Invalid custom emoji.","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"Invalid custom emoji.","result":"error"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.