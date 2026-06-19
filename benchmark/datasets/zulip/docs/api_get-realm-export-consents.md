# Get data export consent state | Zulip API documentation

*Source: https://zulip.com/api/get-realm-export-consents*

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

# Get data export consent state
This endpoint is only available to organization administrators.
GET https://your-org.zulipchat.com/api/v1/export/realm/consents
Fetches which users haveconsentedfor their private data to be exported by organization administrators.
Changes: Changes in Zulip 12.0 (feature level 430). Added an
integer fieldemail_address_visibilityto the objects in theexport_consentsarray.
New in Zulip 10.0 (feature level 295).

## Usage examples
Pythoncurl
- Python
- curl

```
#!/usr/bin/env pythonimportzulip# The user for this zuliprc file must be an organization administratorclient=zulip.Client(config_file="~/zuliprc-admin")# Get the consents of users for their private data exports.result=client.call_endpoint(url="/export/realm/consents",method="GET")print(result)
```

```
#!/usr/bin/env pythonimportzulip# The user for this zuliprc file must be an organization administratorclient=zulip.Client(config_file="~/zuliprc-admin")# Get the consents of users for their private data exports.result=client.call_endpoint(url="/export/realm/consents",method="GET")print(result)
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/export/realm/consents \
    -u EMAIL_ADDRESS:API_KEY
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/export/realm/consents \
    -u EMAIL_ADDRESS:API_KEY
```

## Parameters
This endpoint does not accept any parameters.

## Response

#### Return values
- export_consents:(object)[]An array of objects where each object contains a user ID, whether the
user has consented for their private data to be exported, and their
email visibility policy.user_id:integerThe user ID.consented:booleanWhether the user has consented for their private data export.email_address_visibility:integerThepolicyforwhich other usersin this organization can see the user's real email address.1 = Everyone2 = Members only3 = Administrators only4 = Nobody5 = Moderators onlyChanges: New in Zulip 7.0 (feature level 163), replacing the
realm-level setting.
- user_id:integerThe user ID.
- consented:booleanWhether the user has consented for their private data export.
- email_address_visibility:integerThepolicyforwhich other usersin this organization can see the user's real email address.1 = Everyone2 = Members only3 = Administrators only4 = Nobody5 = Moderators onlyChanges: New in Zulip 7.0 (feature level 163), replacing the
realm-level setting.
- 1 = Everyone
- 2 = Members only
- 3 = Administrators only
- 4 = Nobody
- 5 = Moderators only

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"export_consents":[{"consented":true,"email_address_visibility":1,"user_id":11},{"consented":false,"email_address_visibility":2,"user_id":6}],"msg":"","result":"success"}
```

```
{"export_consents":[{"consented":true,"email_address_visibility":1,"user_id":11},{"consented":false,"email_address_visibility":2,"user_id":6}],"msg":"","result":"success"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.