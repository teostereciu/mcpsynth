# Get all custom profile fields | Zulip API documentation

*Source: https://zulip.com/api/get-custom-profile-fields*

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

# Get all custom profile fields
GET https://your-org.zulipchat.com/api/v1/realm/profile_fields
Get all thecustom profile fieldsconfigured for the user's organization.

## Usage examples
Pythoncurl
- Python
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Fetch all the custom profile fields in the user's organization.result=client.call_endpoint(url="/realm/profile_fields",method="GET",)print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Fetch all the custom profile fields in the user's organization.result=client.call_endpoint(url="/realm/profile_fields",method="GET",)print(result)
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/realm/profile_fields \
    -u EMAIL_ADDRESS:API_KEY
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/realm/profile_fields \
    -u EMAIL_ADDRESS:API_KEY
```

## Parameters
This endpoint does not accept any parameters.

## Response

#### Return values
- custom_fields:(object)[]An array containing all the custom profile fields defined in this
Zulip organization.id:integerThe ID of the custom profile field. This will be referenced in the custom
profile fields section of user objects.type:integerAn integer indicating the type of the custom profile field, which determines
how it is configured and displayed to users.See theCustom profile fieldsarticle for details on what each type means.1: Short text2: Paragraph3: Dropdown4: Date picker5: Link6: Person picker7: External account8: PronounsChanges: Field type8added in Zulip 6.0 (feature level 151).order:integerCustom profile fields are displayed in both settings UI and
UI showing users' profiles in increasingorder.name:stringThe name of the custom profile field.hint:stringThe help text to be displayed for the custom profile field in user-facing
settings UI for configuring custom profile fields.field_data:stringField types 3 (Dropdown) and 7 (External account) support storing
additional configuration for the field type in thefield_dataattribute.For field type 3 (Dropdown), this attribute is a JSON dictionary
defining the choices and the order they will be displayed in the
dropdown UI for individual users to select an option.The interface for field type 7 is not yet stabilized.display_in_profile_summary:booleanWhether the custom profile field, display or not on the user card.Must be false forPerson pickerprofile field types.This field is only included when its value istrue.Changes: Before Zulip 12.0 (feature level 476), the
"Paragraph" field type was not supported.New in Zulip 6.0 (feature level 146).required:booleanWhether an organization administrator has configured this profile field as
required.Because the required property is mutable, clients cannot assume that a required
custom profile field has a value. The Zulip web application displays a prominent
banner to any user who has not set a value for a required field.Changes: New in Zulip 9.0 (feature level 244).editable_by_user:booleanWhether regular users can edit this profile field on their own account.Note that organization administrators can edit custom profile fields for any user
regardless of this setting.Changes: New in Zulip 10.0 (feature level 296).use_for_user_matching:booleanWhether this custom profile field should be used to match users in typeahead
suggestions. Only allowed for Short Text and External Accountprofile field types.This field is only included when its value istrue.Changes: New in Zulip 12.0 (feature level 455).
- id:integerThe ID of the custom profile field. This will be referenced in the custom
profile fields section of user objects.
- type:integerAn integer indicating the type of the custom profile field, which determines
how it is configured and displayed to users.See theCustom profile fieldsarticle for details on what each type means.1: Short text2: Paragraph3: Dropdown4: Date picker5: Link6: Person picker7: External account8: PronounsChanges: Field type8added in Zulip 6.0 (feature level 151).
- order:integerCustom profile fields are displayed in both settings UI and
UI showing users' profiles in increasingorder.
- name:stringThe name of the custom profile field.
- hint:stringThe help text to be displayed for the custom profile field in user-facing
settings UI for configuring custom profile fields.
- field_data:stringField types 3 (Dropdown) and 7 (External account) support storing
additional configuration for the field type in thefield_dataattribute.For field type 3 (Dropdown), this attribute is a JSON dictionary
defining the choices and the order they will be displayed in the
dropdown UI for individual users to select an option.The interface for field type 7 is not yet stabilized.
- display_in_profile_summary:booleanWhether the custom profile field, display or not on the user card.Must be false forPerson pickerprofile field types.This field is only included when its value istrue.Changes: Before Zulip 12.0 (feature level 476), the
"Paragraph" field type was not supported.New in Zulip 6.0 (feature level 146).
- required:booleanWhether an organization administrator has configured this profile field as
required.Because the required property is mutable, clients cannot assume that a required
custom profile field has a value. The Zulip web application displays a prominent
banner to any user who has not set a value for a required field.Changes: New in Zulip 9.0 (feature level 244).
- editable_by_user:booleanWhether regular users can edit this profile field on their own account.Note that organization administrators can edit custom profile fields for any user
regardless of this setting.Changes: New in Zulip 10.0 (feature level 296).
- use_for_user_matching:booleanWhether this custom profile field should be used to match users in typeahead
suggestions. Only allowed for Short Text and External Accountprofile field types.This field is only included when its value istrue.Changes: New in Zulip 12.0 (feature level 455).
- 1: Short text
- 2: Paragraph
- 3: Dropdown
- 4: Date picker
- 5: Link
- 6: Person picker
- 7: External account
- 8: Pronouns

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"custom_fields":[{"editable_by_user":false,"field_data":"","hint":"","id":1,"name":"Phone number","order":1,"required":true,"type":1},{"editable_by_user":true,"field_data":"","hint":"What are you known for?","id":2,"name":"Biography","order":2,"required":true,"type":2},{"editable_by_user":true,"field_data":"","hint":"Or drink, if you'd prefer","id":3,"name":"Favorite food","order":3,"required":false,"type":1},{"display_in_profile_summary":true,"editable_by_user":true,"field_data":"{\"0\":{\"text\":\"Vim\",\"order\":\"1\"},\"1\":{\"text\":\"Emacs\",\"order\":\"2\"}}","hint":"","id":4,"name":"Favorite editor","order":4,"required":true,"type":3},{"editable_by_user":false,"field_data":"","hint":"","id":5,"name":"Birthday","order":5,"required":false,"type":4},{"display_in_profile_summary":true,"editable_by_user":true,"field_data":"","hint":"Or your personal blog's URL","id":6,"name":"Favorite website","order":6,"required":false,"type":5},{"editable_by_user":false,"field_data":"","hint":"","id":7,"name":"Mentor","order":7,"required":true,"type":6},{"editable_by_user":true,"field_data":"{\"subtype\":\"github\"}","hint":"Enter your GitHub username","id":8,"name":"GitHub","order":8,"required":true,"type":7,"use_for_user_matching":true},{"editable_by_user":true,"hint":"What pronouns should people use to refer to you?","id":9,"name":"Pronouns","order":9,"required":false,"type":8}],"msg":"","result":"success"}
```

```
{"custom_fields":[{"editable_by_user":false,"field_data":"","hint":"","id":1,"name":"Phone number","order":1,"required":true,"type":1},{"editable_by_user":true,"field_data":"","hint":"What are you known for?","id":2,"name":"Biography","order":2,"required":true,"type":2},{"editable_by_user":true,"field_data":"","hint":"Or drink, if you'd prefer","id":3,"name":"Favorite food","order":3,"required":false,"type":1},{"display_in_profile_summary":true,"editable_by_user":true,"field_data":"{\"0\":{\"text\":\"Vim\",\"order\":\"1\"},\"1\":{\"text\":\"Emacs\",\"order\":\"2\"}}","hint":"","id":4,"name":"Favorite editor","order":4,"required":true,"type":3},{"editable_by_user":false,"field_data":"","hint":"","id":5,"name":"Birthday","order":5,"required":false,"type":4},{"display_in_profile_summary":true,"editable_by_user":true,"field_data":"","hint":"Or your personal blog's URL","id":6,"name":"Favorite website","order":6,"required":false,"type":5},{"editable_by_user":false,"field_data":"","hint":"","id":7,"name":"Mentor","order":7,"required":true,"type":6},{"editable_by_user":true,"field_data":"{\"subtype\":\"github\"}","hint":"Enter your GitHub username","id":8,"name":"GitHub","order":8,"required":true,"type":7,"use_for_user_matching":true},{"editable_by_user":true,"hint":"What pronouns should people use to refer to you?","id":9,"name":"Pronouns","order":9,"required":false,"type":8}],"msg":"","result":"success"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.