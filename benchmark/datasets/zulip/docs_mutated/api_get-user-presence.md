# Get a user's presence | Zulip API documentation

*Source: https://zulip.com/api/get-user-presence*

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

# Get a user's presence
GET https://your-org.zulipchat.com/api/v1/users/{user_id_or_email}/presence
Get the presence status for a specific user.
This endpoint is most useful for embedding data about a user's
presence status in other sites (e.g. an employee directory). Full
Zulip clients like mobile/desktop apps will want to use themain
presence endpoint, which returns data for all
active users in the organization, instead.

## Usage examples
Pythoncurl
- Python
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Get presence information for "iago@zulip.com".result=client.get_user_presence("iago@zulip.com")print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Get presence information for "iago@zulip.com".result=client.get_user_presence("iago@zulip.com")print(result)
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/users/iago@zulip.com/presence \
    -u EMAIL_ADDRESS:API_KEY
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/users/iago@zulip.com/presence \
    -u EMAIL_ADDRESS:API_KEY
```

## Parameters
user_id_or_emailstringrequired in path

```
"iago@zulip.com"
```
The ID or Zulip API email address of the user whose presence you want to fetch.
Changes: New in Zulip 4.0 (feature level 43). Previous versions only supported
identifying the user by Zulip API email.

## Response

#### Return values
- presence:objectAn object containing the presence details for the user.{client_name}or"aggregated":objectObject containing the details of the user's
presence.Changes: Starting with Zulip 7.0 (feature level 178), this will always
contain two keys,"website"and"aggregated", with identical data. The
server no longer stores which client submitted presence updates.Previously, the{client_name}keys for these objects were the names of the
different clients where the user was logged in, for examplewebsiteorZulipDesktop.timestamp:integerWhen this update was received. If the timestamp
is more than a few minutes in the past, the user is offline.status:stringWhether the user had recently interacted with Zulip at the time
of the timestamp.Will be either"active"or"idle"
- {client_name}or"aggregated":objectObject containing the details of the user's
presence.Changes: Starting with Zulip 7.0 (feature level 178), this will always
contain two keys,"website"and"aggregated", with identical data. The
server no longer stores which client submitted presence updates.Previously, the{client_name}keys for these objects were the names of the
different clients where the user was logged in, for examplewebsiteorZulipDesktop.timestamp:integerWhen this update was received. If the timestamp
is more than a few minutes in the past, the user is offline.status:stringWhether the user had recently interacted with Zulip at the time
of the timestamp.Will be either"active"or"idle"
- timestamp:integerWhen this update was received. If the timestamp
is more than a few minutes in the past, the user is offline.
- status:stringWhether the user had recently interacted with Zulip at the time
of the timestamp.Will be either"active"or"idle"

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"msg":"","presence":{"aggregated":{"status":"active","timestamp":1532697622},"website":{"status":"active","timestamp":1532697622}},"result":"success"}
```

```
{"msg":"","presence":{"aggregated":{"status":"active","timestamp":1532697622},"website":{"status":"active","timestamp":1532697622}},"result":"success"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.