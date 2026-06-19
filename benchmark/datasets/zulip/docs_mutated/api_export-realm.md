# Create a data export | Zulip API documentation

*Source: https://zulip.com/api/export-realm*

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

# Create a data export
This endpoint is only available to organization administrators.
POST https://your-org.zulipchat.com/api/v1/export/realm
Create a public or a standarddata exportof the organization.
Note: If you're the administrator of a self-hosted installation,
you may be looking for the documentation onserver data export and
importorserver backups.
Changes: Prior to Zulip 10.0 (feature level 304), only
public data exports could be created using this endpoint.
New in Zulip 2.1.

## Usage examples
Pythoncurl
- Python
- curl

```
#!/usr/bin/env pythonimportzulip# The user for this zuliprc file must be an organization administratorclient=zulip.Client(config_file="~/zuliprc-admin")# Create a public data export of the organization.result=client.call_endpoint(url="/export/realm",method="POST")print(result)
```

```
#!/usr/bin/env pythonimportzulip# The user for this zuliprc file must be an organization administratorclient=zulip.Client(config_file="~/zuliprc-admin")# Create a public data export of the organization.result=client.call_endpoint(url="/export/realm",method="POST")print(result)
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/export/realm \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode export_type=full_with_consent
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/export/realm \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode export_type=full_with_consent
```

## Parameters
export_typestringoptional

```
"full_with_consent"
```
Whether the data export should be public, full with consent,
or full without consent.
- public= Public data only export.
- full_with_consent= Public and private data export (with consent), which includes
  private data for users who have granted consent.
- full_without_consent= All public and private data export, which includes private data for
  all users. This option requires the organization to have
  theowner_full_content_accessfeature enabled.
If not specified, defaults topublic.
Changes: Zulip 12.0 (feature level 449) changed the type of
this field from int to string with1being replaced bypublicand2being replaced byfull_with_consent. The optionfull_without_consentwas added for full exports without member consent.
Changes: New in Zulip 10.0 (feature level 304). Previously,
all export requests were public data exports.
Must be one of:"public","full_with_consent","full_without_consent". 
Defaults to"public".

## Response

#### Return values
- id:integerThe ID of the data export created.Changes: New in Zulip 7.0 (feature level 182).

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"id":1,"msg":"","result":"success"}
```

```
{"id":1,"msg":"","result":"success"}
```
An example JSON error response for when the data export
exceeds the maximum allowed data export size.

```
{"code":"BAD_REQUEST","msg":"Please request a manual export from zulip-admin@example.com.","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"Please request a manual export from zulip-admin@example.com.","result":"error"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.