# Deactivate a user | Zulip API documentation

*Source: https://zulip.com/api/deactivate-user*

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

# Deactivate a user
This endpoint is only available to organization administrators.
DELETE https://your-org.zulipchat.com/api/v1/users/{user_id}
Deactivates a
usergiven their user ID.
Note that any bots controlled by the user will be deactivated
before the user; clients that don't want this behavior are
expected to prompt the user to adjust the bot's owners before
making this API request.

## Usage examples
Pythoncurl
- Python
- curl

```
#!/usr/bin/env pythonimportzulip# The user for this zuliprc file must be an organization administratorclient=zulip.Client(config_file="~/zuliprc-admin")# Deactivate a user given a user ID.result=client.deactivate_user_by_id(user_id)print(result)
```

```
#!/usr/bin/env pythonimportzulip# The user for this zuliprc file must be an organization administratorclient=zulip.Client(config_file="~/zuliprc-admin")# Deactivate a user given a user ID.result=client.deactivate_user_by_id(user_id)print(result)
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX DELETE https://your-org.zulipchat.com/api/v1/users/12 \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'actions={"delete_direct_messages": false, "delete_private_channel_messages": false, "delete_profile": false, "delete_public_channel_messages": false}' \
    --data-urlencode 'deactivation_notification_comment=Farewell!
'
```

```
curl -sSX DELETE https://your-org.zulipchat.com/api/v1/users/12 \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'actions={"delete_direct_messages": false, "delete_private_channel_messages": false, "delete_profile": false, "delete_public_channel_messages": false}' \
    --data-urlencode 'deactivation_notification_comment=Farewell!
'
```

## Parameters
user_idintegerrequired in path
The target user's ID.
actionsobjectoptional

```
{"delete_profile": false, "delete_public_channel_messages": false, "delete_private_channel_messages": false, "delete_direct_messages": false}
```
Additional actions for the server to perform while deactivating the user.
As with the actual deactivation, actions are first applied
to any bots controlled by the target user, and then to the
target user.
Changes: New in Zulip 12.0 (feature level 459).
actionsobject details:
- delete_profile:booleanWhether to delete the user's profile by updating their name
to "Deleted user" and removing their profile picture.
- delete_public_channel_messages:booleanWhether to delete messages in public channels.
- delete_private_channel_messages:booleanWhether to delete messages in private channels.
- delete_direct_messages:booleanWhether to delete direct messages.
deactivation_notification_commentstringoptional

```
"Farewell!\n"
```
If notnull, requests that the deactivated user receive
a notification email about their account deactivation.
If not"", encodes custom text written by the administrator
to be included in the notification email.
Changes: New in Zulip 5.0 (feature level 135).

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
An example JSON error response when attempting to deactivate the only
organization owner in an organization:

```
{"code":"BAD_REQUEST","msg":"Cannot deactivate the only organization owner","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"Cannot deactivate the only organization owner","result":"error"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.