# Register E2EE push device to bouncer | Zulip API documentation

*Source: https://zulip.com/api/register-remote-push-device*

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

# Register E2EE push device to bouncer
POST https://push.zulipchat.com/api/v1/remotes/push/e2ee/register
Register a push device to bouncer to receive end-to-end encrypted
mobile push notifications.
Self-hosted servers use this endpoint to asynchronously register
a push device to the bouncer server after receiving a request from
the mobile client toregister E2EE push device.
It is not meant to be used by mobile clients directly.
Changes: New in Zulip 11.0 (feature level 406).

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
curl -sSX POST https://push.zulipchat.com/api/v1/remotes/push/e2ee/register \
    -u ZULIP_ORG_ID:ZULIP_ORG_KEY \
    --data-urlencode realm_uuid=9aa61d0b-8ce5-488d-8e9e-fedc346e6836 \
    --data-urlencode token_id=+wKIhyAx/Eg= \
    --data-urlencode encrypted_push_registration=encrypted-push-registration-data \
    --data-urlencode bouncer_public_key=bouncer-public-key
```

```
curl -sSX POST https://push.zulipchat.com/api/v1/remotes/push/e2ee/register \
    -u ZULIP_ORG_ID:ZULIP_ORG_KEY \
    --data-urlencode realm_uuid=9aa61d0b-8ce5-488d-8e9e-fedc346e6836 \
    --data-urlencode token_id=+wKIhyAx/Eg= \
    --data-urlencode encrypted_push_registration=encrypted-push-registration-data \
    --data-urlencode bouncer_public_key=bouncer-public-key
```

## Parameters
realm_uuidstringrequired

```
"9aa61d0b-8ce5-488d-8e9e-fedc346e6836"
```
The UUID of the realm to which the push device
being registered belongs.
token_idstringrequired

```
"+wKIhyAx/Eg="
```
Thetoken_idvalue provided by the mobile client
toregister E2EE push device.
Changes: New in Zulip 12.0 (feature level 468),
replacingpush_account_id.
encrypted_push_registrationstringrequired

```
"encrypted-push-registration-data"
```
Theencrypted_push_registrationvalue provided by the mobile client
toregister E2EE push device.
bouncer_public_keystringrequired

```
"bouncer-public-key"
```
Thebouncer_public_keyvalue provided by the mobile client
toregister E2EE push device.

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
An example JSON response for when the givenbouncer_public_keyis invalid:

```
{"code":"INVALID_BOUNCER_PUBLIC_KEY","msg":"Invalid bouncer_public_key","result":"error"}
```

```
{"code":"INVALID_BOUNCER_PUBLIC_KEY","msg":"Invalid bouncer_public_key","result":"error"}
```
An example JSON response for when the givenencrypted_push_registrationis stale:

```
{"code":"REQUEST_EXPIRED","msg":"Request expired","result":"error"}
```

```
{"code":"REQUEST_EXPIRED","msg":"Request expired","result":"error"}
```
An example JSON response for when either the bouncer fails to decrypt
the givenencrypted_push_registrationor the decrypted data is invalid:

```
{"code":"BAD_REQUEST","msg":"Invalid encrypted_push_registration","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"Invalid encrypted_push_registration","result":"error"}
```
An example JSON response for when no realm is registered for
the authenticated server on the bouncer for the givenrealm_uuid:

```
{"code":"MISSING_REMOTE_REALM","msg":"Organization not registered","result":"error"}
```

```
{"code":"MISSING_REMOTE_REALM","msg":"Organization not registered","result":"error"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.