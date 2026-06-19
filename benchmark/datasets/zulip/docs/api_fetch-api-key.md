# Fetch an API key (production) | Zulip API documentation

*Source: https://zulip.com/api/fetch-api-key*

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

# Fetch an API key (production)
POST https://your-org.zulipchat.com/api/v1/fetch_api_key
This API endpoint is used by clients such as the Zulip mobile and
terminal apps to implement password-based authentication. Given the
user's Zulip login credentials, it returns a Zulip API key that the client
can use to make requests as the user.
This endpoint is only useful for Zulip servers/organizations with
EmailAuthBackend or LDAPAuthBackend enabled.
The Zulip mobile apps also support SSO/social authentication (GitHub
auth, Google auth, SAML, etc.) that does not use this endpoint. Instead,
the mobile apps reuse the web login flow passing themobile_flow_otpin
a webview, and the credentials are returned to the app (encrypted) via a redirect
to azulip://URL.
Note:If you signed up using passwordless authentication and
never had a password, you canreset your password.
See theAPI keysdocumentation for more details
on how to download an API key manually.
In aZulip development environment,
see alsothe unauthenticated variant.

## Usage examples
curl
- curl

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/fetch_api_key \
    --data-urlencode username=iago@zulip.com \
    --data-urlencode password=abcd1234
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/fetch_api_key \
    --data-urlencode username=iago@zulip.com \
    --data-urlencode password=abcd1234
```

## Parameters
usernamestringrequired

```
"iago@zulip.com"
```
The username to be used for authentication (typically, the email
address, but depending on configuration, it could be an LDAP username).
See therequire_email_format_usernamesparameter documented inGET /server_settingsfor details.
passwordstringrequired
The user's Zulip password (or LDAP password, if LDAP authentication is in use).

## Response

#### Return values
- api_key:stringThe API key that can be used to authenticate as the requested user.
- email:stringThe email address of the user who owns the API key.
- user_id:integerThe unique ID of the user who owns the API key.Changes: New in Zulip 7.0 (feature level 171).

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"api_key":"gjA04ZYcqXKalvYMA8OeXSfzUOLrtbZv","email":"iago@zulip.com","msg":"","result":"success","user_id":5}
```

```
{"api_key":"gjA04ZYcqXKalvYMA8OeXSfzUOLrtbZv","email":"iago@zulip.com","msg":"","result":"success","user_id":5}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.