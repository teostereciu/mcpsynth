# Create a custom profile field | Zulip API documentation

*Source: https://zulip.com/api/create-custom-profile-field*

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

# Create a custom profile field
This endpoint is only available to organization administrators.
POST https://your-org.zulipchat.com/api/v1/realm/profile_fields
Create a custom profile fieldin the user's organization.

## Usage examples
Pythoncurl
- Python
- curl

```
#!/usr/bin/env pythonimportzulip# The user for this zuliprc file must be an organization administratorclient=zulip.Client(config_file="~/zuliprc-admin")# Create a custom profile field in the user's organization.request={"name":"Phone","hint":"Contact no.","field_type":1}result=client.call_endpoint(url="/realm/profile_fields",method="POST",request=request)print(result)
```

```
#!/usr/bin/env pythonimportzulip# The user for this zuliprc file must be an organization administratorclient=zulip.Client(config_file="~/zuliprc-admin")# Create a custom profile field in the user's organization.request={"name":"Phone","hint":"Contact no.","field_type":1}result=client.call_endpoint(url="/realm/profile_fields",method="POST",request=request)print(result)
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/realm/profile_fields \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'name=Favorite programming language' \
    --data-urlencode 'hint=Your favorite programming language.' \
    --data-urlencode field_type=3 \
    --data-urlencode 'field_data={"java": {"order": "2", "text": "Java"}, "python": {"order": "1", "text": "Python"}}' \
    --data-urlencode display_in_profile_summary=true \
    --data-urlencode required=true \
    --data-urlencode editable_by_user=true \
    --data-urlencode use_for_user_matching=false
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/realm/profile_fields \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'name=Favorite programming language' \
    --data-urlencode 'hint=Your favorite programming language.' \
    --data-urlencode field_type=3 \
    --data-urlencode 'field_data={"java": {"order": "2", "text": "Java"}, "python": {"order": "1", "text": "Python"}}' \
    --data-urlencode display_in_profile_summary=true \
    --data-urlencode required=true \
    --data-urlencode editable_by_user=true \
    --data-urlencode use_for_user_matching=false
```

## Parameters
namestringoptional

```
"Favorite programming language"
```
The name of the custom profile field, which will appear both in
user-facing settings UI for configuring custom profile fields and
in UI displaying a user's profile.
hintstringoptional

```
"Your favorite programming language."
```
The help text to be displayed for the custom profile field in user-facing
settings UI for configuring custom profile fields.
field_typeintegerrequired
The field type can be any of the supported custom profile field types. See thecustom profile fields documentationfor more details on what each type means.
- 1: Short text
- 2: Paragraph
- 3: Dropdown
- 4: Date picker
- 5: Link
- 6: Person picker
- 7: External account
- 8: Pronouns
Changes: Field type8added in Zulip 6.0 (feature level 151).
field_dataobjectoptional

```
{"python": {"text": "Python", "order": "1"}, "java": {"text": "Java", "order": "2"}}
```
Field types 3 (Dropdown) and 7 (External account) support storing
additional configuration for the field type in thefield_dataattribute.
For field type 3 (Dropdown), this attribute is a JSON dictionary
defining the choices and the order they will be displayed in the
dropdown UI for individual users to select an option.
The interface for field type 7 is not yet stabilized.
display_in_profile_summarybooleanoptional
Whether clients should display this profile field in a summary section of a
user's profile (or in a more easily accessible "small profile").
At most 2 profile fields may have this property be true in a given
organization.
The "Person picker" profile field is not supported, but that is likely to
be temporary.
Changes: Before Zulip 12.0 (feature level 476), the
"Paragraph" field type was not supported.
New in Zulip 6.0 (feature level 146).
requiredbooleanoptional
Whether an organization administrator has configured this profile field as
required.
Because the required property is mutable, clients cannot assume that a required
custom profile field has a value. The Zulip web application displays a prominent
banner to any user who has not set a value for a required field.
Changes: New in Zulip 9.0 (feature level 244).
editable_by_userbooleanoptional
Whether regular users can edit this profile field on their own account.
Note that organization administrators can edit custom profile fields for any user
regardless of this setting.
Changes: New in Zulip 10.0 (feature level 296).
use_for_user_matchingbooleanoptional
Whether this custom profile field should be used to match users in typeahead
suggestions. Only allowed for Short Text and External Accountprofile field types.
This field is only included when its value istrue.
Changes: New in Zulip 12.0 (feature level 455).

## Response

#### Return values
- id:integerThe ID for the custom profile field.

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"id":9,"msg":"","result":"success"}
```

```
{"id":9,"msg":"","result":"success"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.