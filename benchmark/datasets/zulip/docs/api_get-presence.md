# Get presence of all users | Zulip API documentation

*Source: https://zulip.com/api/get-presence*

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

# Get presence of all users
GET https://your-org.zulipchat.com/api/v1/realm/presence
Get the presence information of all the users in an organization.
If theCAN_ACCESS_ALL_USERS_GROUP_LIMITS_PRESENCEserver-level
setting is set totrue, presence information of only accessible
users are returned.
Complete Zulip apps are recommended to fetch presence
information when they post their own state using thePOST
/presenceAPI endpoint.

```
POST
/presence
```

## Usage examples
Pythoncurl
- Python
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Get presence information of all the users in an organization.result=client.get_realm_presence()print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Get presence information of all the users in an organization.result=client.get_realm_presence()print(result)
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/realm/presence \
    -u EMAIL_ADDRESS:API_KEY
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/realm/presence \
    -u EMAIL_ADDRESS:API_KEY
```

## Parameters
This endpoint does not accept any parameters.

## Response

#### Return values
- server_timestamp:numberThe time when the server fetched thepresencesdata included
in the response.
- presences:objectA dictionary where each entry describes the presence details
of a user in the Zulip organization.{user_email}:objectObject containing the details of a user's presence.
The object's key is the user's Zulip API email.{client_name}or"aggregated":objectObject containing the details of the user's
presence.Changes: Starting with Zulip 7.0 (feature level 178), this will always
contain two keys,"website"and"aggregated", with identical data. The
server no longer stores which client submitted presence updates.Previously, the{client_name}keys for these objects were the names of the
different clients where the user was logged in, for examplewebsiteorZulipDesktop.client:stringThe client's platform name.Changes: Starting with Zulip 7.0 (feature level 178), this will
always be"website"as the server no longer stores which client
submitted presence data.status:stringThe status of the user on this client. Will be either"idle"or"active".timestamp:integerThe UNIX timestamp of when this client sent the user's presence
to the server with the precision of a second.pushable:booleanWhether the client is capable of showing mobile/push notifications
to the user.Not present in objects with the"aggregated"key.Changes: Starting with Zulip 7.0 (feature level 178), alwaysfalsewhen present as the server no longer stores which client
submitted presence data.
- {user_email}:objectObject containing the details of a user's presence.
The object's key is the user's Zulip API email.{client_name}or"aggregated":objectObject containing the details of the user's
presence.Changes: Starting with Zulip 7.0 (feature level 178), this will always
contain two keys,"website"and"aggregated", with identical data. The
server no longer stores which client submitted presence updates.Previously, the{client_name}keys for these objects were the names of the
different clients where the user was logged in, for examplewebsiteorZulipDesktop.client:stringThe client's platform name.Changes: Starting with Zulip 7.0 (feature level 178), this will
always be"website"as the server no longer stores which client
submitted presence data.status:stringThe status of the user on this client. Will be either"idle"or"active".timestamp:integerThe UNIX timestamp of when this client sent the user's presence
to the server with the precision of a second.pushable:booleanWhether the client is capable of showing mobile/push notifications
to the user.Not present in objects with the"aggregated"key.Changes: Starting with Zulip 7.0 (feature level 178), alwaysfalsewhen present as the server no longer stores which client
submitted presence data.
- {client_name}or"aggregated":objectObject containing the details of the user's
presence.Changes: Starting with Zulip 7.0 (feature level 178), this will always
contain two keys,"website"and"aggregated", with identical data. The
server no longer stores which client submitted presence updates.Previously, the{client_name}keys for these objects were the names of the
different clients where the user was logged in, for examplewebsiteorZulipDesktop.client:stringThe client's platform name.Changes: Starting with Zulip 7.0 (feature level 178), this will
always be"website"as the server no longer stores which client
submitted presence data.status:stringThe status of the user on this client. Will be either"idle"or"active".timestamp:integerThe UNIX timestamp of when this client sent the user's presence
to the server with the precision of a second.pushable:booleanWhether the client is capable of showing mobile/push notifications
to the user.Not present in objects with the"aggregated"key.Changes: Starting with Zulip 7.0 (feature level 178), alwaysfalsewhen present as the server no longer stores which client
submitted presence data.
- client:stringThe client's platform name.Changes: Starting with Zulip 7.0 (feature level 178), this will
always be"website"as the server no longer stores which client
submitted presence data.
- status:stringThe status of the user on this client. Will be either"idle"or"active".
- timestamp:integerThe UNIX timestamp of when this client sent the user's presence
to the server with the precision of a second.
- pushable:booleanWhether the client is capable of showing mobile/push notifications
to the user.Not present in objects with the"aggregated"key.Changes: Starting with Zulip 7.0 (feature level 178), alwaysfalsewhen present as the server no longer stores which client
submitted presence data.

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"msg":"","presences":{"iago@zulip.com":{"aggregated":{"client":"website","status":"active","timestamp":1656958485},"website":{"client":"website","pushable":false,"status":"active","timestamp":1656958485}}},"result":"success","server_timestamp":1656958539.6287155}
```

```
{"msg":"","presences":{"iago@zulip.com":{"aggregated":{"client":"website","status":"active","timestamp":1656958485},"website":{"client":"website","pushable":false,"status":"active","timestamp":1656958485}}},"result":"success","server_timestamp":1656958539.6287155}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.