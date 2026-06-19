# Send an E2EE test notification to mobile device(s) | Zulip API documentation

*Source: https://zulip.com/api/e2ee-test-notify*

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

# Send an E2EE test notification to mobile device(s)
POST https://your-org.zulipchat.com/api/v1/mobile_push/e2ee/test_notification
Trigger sending an end-to-end encrypted (E2EE) test push notification
to the user's selected mobile device or all of their mobile devices.
Changes: New in Zulip 11.0 (feature level 420).

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
curl -sSX POST https://your-org.zulipchat.com/api/v1/mobile_push/e2ee/test_notification \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode device_id=1144
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/mobile_push/e2ee/test_notification \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode device_id=1144
```

## Parameters
device_idintegeroptional
The ID for the device to which to send the test notification.
If this parameter is not submitted, the E2EE test notification will
be sent to all of the user's devices registered on the server.
A mobile client should pass this parameter, to avoid triggering a test
notification for other clients.
SeePOST /register_client_devicefor details on device ID.

```
POST /register_client_device
```
Changes: New in Zulip 12.0 (feature level 468).
Previously,push_account_idwas used.

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

## No active push device
A typical failed JSON response for when no registered device is available
for the user (andpush_account_id) to receive a push notification.

```
{"code":"NO_ACTIVE_PUSH_DEVICE","msg":"No active registered push device","result":"error"}
```

```
{"code":"NO_ACTIVE_PUSH_DEVICE","msg":"No active registered push device","result":"error"}
```

## Admin action required
A typical failed JSON response for when there is a push notification
configuration issue on the server, such as invalid credentials,
an expired plan, or an unregistered organization. Admin action is required.

```
{"code":"ADMIN_ACTION_REQUIRED","msg":"Push notification configuration issue on server, contact the server administrator or retry later.","result":"error"}
```

```
{"code":"ADMIN_ACTION_REQUIRED","msg":"Push notification configuration issue on server, contact the server administrator or retry later.","result":"error"}
```

## Failed to connect bouncer
A typical failed JSON response for when a network error occurs
while the server attempts to connect to the bouncer server.

```
{"code":"FAILED_TO_CONNECT_BOUNCER","msg":"Network error while connecting to Zulip push notification service.","result":"error"}
```

```
{"code":"FAILED_TO_CONNECT_BOUNCER","msg":"Network error while connecting to Zulip push notification service.","result":"error"}
```

## Internal bouncer server error
A typical failed JSON response for when a 5xx error occurs on the bouncer server.

```
{"code":"INTERNAL_SERVER_ERROR_ON_BOUNCER","msg":"Internal server error on Zulip push notification service, retry later.","result":"error"}
```

```
{"code":"INTERNAL_SERVER_ERROR_ON_BOUNCER","msg":"Internal server error on Zulip push notification service, retry later.","result":"error"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.