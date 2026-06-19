# Get channel folders | Zulip API documentation

*Source: https://zulip.com/api/get-channel-folders*

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

# Get channel folders
GET https://your-org.zulipchat.com/api/v1/channel_folders
Fetches all of thechannel foldersin the
organization, sorted by theorderfield.
Changes: Before Zulip 11.0 (feature level 414), the list of channel
folders was sorted by ID as theorderfield didn't exist.
New in Zulip 11.0 (feature level 389).

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
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/channel_folders \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode include_archived=true
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/channel_folders \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode include_archived=true
```

## Parameters
include_archivedbooleanoptional
Whether to include archived channel folders in the response.
Defaults tofalse.

## Response

#### Return values
- channel_folders:(object)[]A list of channel folder objects.id:integerThe unique ID of the channel folder.name:stringThe name of the channel folder.order:integerThis value determines in which order the channel folder should be
displayed in the UI. The value is 0 indexed, and a channel folder with
a lower value should be displayed before channel folders with higher
values.Changes: New in Zulip 11.0 (feature level 414).date_created:integer | nullThe UNIX timestamp for when the channel folder was created,
in UTC seconds.creator_id:integer | nullThe ID of the user who created the channel folder.description:stringThe description of the channel folder. Can be an empty string.SeeMarkdown message formattingfor details
on Zulip's HTML format.rendered_description:stringThe description of the channel folder rendered as HTML, intended to be
used for UI that displays the channel folder description.Clients should use the standard Zulip rendered_markdown CSS when
displaying this content so that emoji, LaTeX, and other syntax work
correctly. And any client-side security logic for user-generated
message content should be applied when displaying this HTML as though
it were the body of a Zulip message.is_archived:booleanWhether the channel folder is archived or not.
- id:integerThe unique ID of the channel folder.
- name:stringThe name of the channel folder.
- order:integerThis value determines in which order the channel folder should be
displayed in the UI. The value is 0 indexed, and a channel folder with
a lower value should be displayed before channel folders with higher
values.Changes: New in Zulip 11.0 (feature level 414).
- date_created:integer | nullThe UNIX timestamp for when the channel folder was created,
in UTC seconds.
- creator_id:integer | nullThe ID of the user who created the channel folder.
- description:stringThe description of the channel folder. Can be an empty string.SeeMarkdown message formattingfor details
on Zulip's HTML format.
- rendered_description:stringThe description of the channel folder rendered as HTML, intended to be
used for UI that displays the channel folder description.Clients should use the standard Zulip rendered_markdown CSS when
displaying this content so that emoji, LaTeX, and other syntax work
correctly. And any client-side security logic for user-generated
message content should be applied when displaying this HTML as though
it were the body of a Zulip message.
- is_archived:booleanWhether the channel folder is archived or not.

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"channel_folders":[{"creator_id":1,"date_created":1691057093,"description":"Channels for frontend discussions","id":1,"is_archived":false,"name":"Frontend","rendered_description":"<p>Channels for frontend discussions</p>"},{"creator_id":1,"date_created":1791057093,"description":"Channels for **backend** discussions","id":2,"is_archived":false,"name":"Backend","rendered_description":"<p>Channels for <strong>backend</strong> discussions</p>"}],"msg":"","result":"success"}
```

```
{"channel_folders":[{"creator_id":1,"date_created":1691057093,"description":"Channels for frontend discussions","id":1,"is_archived":false,"name":"Frontend","rendered_description":"<p>Channels for frontend discussions</p>"},{"creator_id":1,"date_created":1791057093,"description":"Channels for **backend** discussions","id":2,"is_archived":false,"name":"Backend","rendered_description":"<p>Channels for <strong>backend</strong> discussions</p>"}],"msg":"","result":"success"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.