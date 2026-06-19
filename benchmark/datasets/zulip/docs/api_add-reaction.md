# Add an emoji reaction | Zulip API documentation

*Source: https://zulip.com/api/add-reaction*

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

# Add an emoji reaction
POST https://your-org.zulipchat.com/api/v1/messages/{message_id}/reactions
Add anemoji reactionto a message.

## Usage examples
Pythoncurl
- Python
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Add an emoji reaction.request={"message_id":message_id,"emoji_name":"octopus",}result=client.add_reaction(request)print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Add an emoji reaction.request={"message_id":message_id,"emoji_name":"octopus",}result=client.add_reaction(request)print(result)
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/messages/43/reactions \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode emoji_name=octopus
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/messages/43/reactions \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode emoji_name=octopus
```

## Parameters
message_idintegerrequired in path
The target message's ID.
emoji_namestringrequired
The target emoji's human-readable name.
To find an emoji's name, hover over a message to reveal
three icons on the right, then click the smiley face icon.
Images of available reaction emojis appear. Hover over the
emoji you want, and note that emoji's text name.
emoji_codestringoptional
A unique identifier, defining the specific emoji codepoint requested,
within the namespace of thereaction_type.
For most API clients, you won't need this, but it's important
for Zulip apps to handle rare corner cases when
adding/removing votes on an emoji reaction added previously by
another user.
If the existing reaction was added when the Zulip server was
using a previous version of the emoji data mapping between
Unicode codepoints and human-readable names, sending theemoji_codein the data for the original reaction allows the
Zulip server to correctly interpret your upvote as an upvote
rather than a reaction with a "different" emoji.
reaction_typestringoptional

```
"unicode_emoji"
```
A string indicating the type of emoji. Each emojireaction_typehas an independent namespace for values ofemoji_code.
If an API client is adding/removing a vote on an existing reaction,
it should pass this parameter using the value the server provided
for the existing reaction for specificity. Supported values:
- unicode_emoji: In this namespace,emoji_codewill be a
  dash-separated hex encoding of the sequence of Unicode codepoints
  that define this emoji in the Unicode specification.
- realm_emoji: In this namespace,emoji_codewill be the ID of
  the uploadedcustom emoji.
- zulip_extra_emoji: These are special emoji included with Zulip.
  In this namespace,emoji_codewill be the name of the emoji (e.g.
  "zulip").
Changes: In Zulip 3.0 (feature level 2), this parameter became
optional forcustom emoji;
previously, this endpoint assumedunicode_emojiif this
parameter was not specified.

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
An example JSON error response for when the emoji code is invalid:

```
{"code":"BAD_REQUEST","msg":"Invalid emoji code","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"Invalid emoji code","result":"error"}
```
An example JSON error response for when the reaction already exists.
Changes: New in Zulip 8.0 (feature level 193). Previously, this
error returned the"BAD_REQUEST"code.

```
{"code":"REACTION_ALREADY_EXISTS","msg":"Reaction already exists.","result":"error"}
```

```
{"code":"REACTION_ALREADY_EXISTS","msg":"Reaction already exists.","result":"error"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.