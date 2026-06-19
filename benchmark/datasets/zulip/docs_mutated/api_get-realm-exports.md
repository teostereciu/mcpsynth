# Get all data exports | Zulip API documentation

*Source: https://zulip.com/api/get-realm-exports*

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

# Get all data exports
This endpoint is only available to organization administrators.
GET https://your-org.zulipchat.com/api/v1/export/realm
Fetch all the public and standarddata exportsof the organization.
Changes: Prior to Zulip 10.0 (feature level 304), only
public data exports could be fetched using this endpoint.
New in Zulip 2.1.

## Usage examples
Pythoncurl
- Python
- curl

```
#!/usr/bin/env pythonimportzulip# The user for this zuliprc file must be an organization administratorclient=zulip.Client(config_file="~/zuliprc-admin")# Get organization's public data exports.result=client.call_endpoint(url="/export/realm",method="GET")print(result)
```

```
#!/usr/bin/env pythonimportzulip# The user for this zuliprc file must be an organization administratorclient=zulip.Client(config_file="~/zuliprc-admin")# Get organization's public data exports.result=client.call_endpoint(url="/export/realm",method="GET")print(result)
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/export/realm \
    -u EMAIL_ADDRESS:API_KEY
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/export/realm \
    -u EMAIL_ADDRESS:API_KEY
```

## Parameters
This endpoint does not accept any parameters.

## Response

#### Return values
- exports:(object)[]An array of dictionaries where each dictionary contains
details about a data export of the organization.id:integerThe ID of the data export.acting_user_id:integerThe ID of the user who created the data export.export_time:numberThe UNIX timestamp of when the data export was started.deleted_timestamp:number | nullThe UNIX timestamp of when the data export was deleted.Will benullif the data export has not been deleted.failed_timestamp:number | nullThe UNIX timestamp of when the data export failed.Will benullif the data export succeeded, or if it's
still being generated.export_url:string | nullThe URL to download the generated data export.Will benullif the data export failed, or if it's
still being generated.pending:booleanWhether the data export is pending, which indicates it
is still being generated, or if it succeeded, failed or
was deleted before being generated.Depending on the size of the organization, it can take
anywhere from seconds to an hour to generate the data
export.export_type:stringWhether the data export is public, full with consent, or full without consent.public= Public data export.full_with_consent= Public and private data export (with consent), which includes private data
  for users who have granted consent.full_without_consent= All public and private data, which includes private data for all users.Changes: Zulip 12.0 (feature level 449) changed the type of
this field from int to string with1being replaced bypublicand2being replaced byfull_with_consent. The optionfull_without_consentwas added for full exports without member consent.Changes: New in Zulip 10.0 (feature level 304). Previously,
the export type was not included in these objects because only
public data exports could be created or listed via the API or UI.
- id:integerThe ID of the data export.
- acting_user_id:integerThe ID of the user who created the data export.
- export_time:numberThe UNIX timestamp of when the data export was started.
- deleted_timestamp:number | nullThe UNIX timestamp of when the data export was deleted.Will benullif the data export has not been deleted.
- failed_timestamp:number | nullThe UNIX timestamp of when the data export failed.Will benullif the data export succeeded, or if it's
still being generated.
- export_url:string | nullThe URL to download the generated data export.Will benullif the data export failed, or if it's
still being generated.
- pending:booleanWhether the data export is pending, which indicates it
is still being generated, or if it succeeded, failed or
was deleted before being generated.Depending on the size of the organization, it can take
anywhere from seconds to an hour to generate the data
export.
- export_type:stringWhether the data export is public, full with consent, or full without consent.public= Public data export.full_with_consent= Public and private data export (with consent), which includes private data
  for users who have granted consent.full_without_consent= All public and private data, which includes private data for all users.Changes: Zulip 12.0 (feature level 449) changed the type of
this field from int to string with1being replaced bypublicand2being replaced byfull_with_consent. The optionfull_without_consentwas added for full exports without member consent.Changes: New in Zulip 10.0 (feature level 304). Previously,
the export type was not included in these objects because only
public data exports could be created or listed via the API or UI.
- public= Public data export.
- full_with_consent= Public and private data export (with consent), which includes private data
  for users who have granted consent.
- full_without_consent= All public and private data, which includes private data for all users.

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"exports":[{"acting_user_id":11,"deleted_timestamp":null,"export_time":1722243168.134179,"export_type":"public","export_url":"http://example.zulipchat.com/user_avatars/exports/2/FprbwiF0c_sCN0O-rf-ryFtc/zulip-export-p6yuxc45.tar.gz","failed_timestamp":null,"id":323,"pending":false}],"msg":"","result":"success"}
```

```
{"exports":[{"acting_user_id":11,"deleted_timestamp":null,"export_time":1722243168.134179,"export_type":"public","export_url":"http://example.zulipchat.com/user_avatars/exports/2/FprbwiF0c_sCN0O-rf-ryFtc/zulip-export-p6yuxc45.tar.gz","failed_timestamp":null,"id":323,"pending":false}],"msg":"","result":"success"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.