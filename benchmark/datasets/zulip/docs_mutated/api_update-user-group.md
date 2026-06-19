# Update a user group | Zulip API documentation

*Source: https://zulip.com/api/update-user-group*

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

# Update a user group
PATCH https://your-org.zulipchat.com/api/v1/user_groups/{user_group_id}
Update the name, description or any of the permission settings
of auser group.
This endpoint is also used to reactivate a user group.
Note that while permissions settings of deactivated groups can
be edited by this API endpoint, and those permissions settings
do affect the ability to modify the deactivated group and its
membership, the deactivated group itself cannot be mentioned
or used in the value of any permission without first being reactivated.
Changes: Starting with Zulip 11.0 (feature level 386), this
endpoint can be used to reactivate a user group.
Prior to Zulip 10.0 (feature level 340), only the name field
of deactivated groups could be modified.

## Usage examples
Pythoncurl
- Python
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")request={"group_id":user_group_id,"name":"leadership","description":"The leadership team.",}result=client.update_user_group(request)print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")request={"group_id":user_group_id,"name":"leadership","description":"The leadership team.",}result=client.update_user_group(request)print(result)
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX PATCH https://your-org.zulipchat.com/api/v1/user_groups/38 \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'name=marketing team' \
    --data-urlencode 'description=The marketing team.' \
    --data-urlencode 'can_add_members_group={"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 11}' \
    --data-urlencode 'can_join_group={"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 11}' \
    --data-urlencode 'can_leave_group={"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 15}' \
    --data-urlencode 'can_manage_group={"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 11}' \
    --data-urlencode 'can_mention_group={"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 11}' \
    --data-urlencode 'can_remove_members_group={"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 11}' \
    --data-urlencode deactivated=false
```

```
curl -sSX PATCH https://your-org.zulipchat.com/api/v1/user_groups/38 \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'name=marketing team' \
    --data-urlencode 'description=The marketing team.' \
    --data-urlencode 'can_add_members_group={"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 11}' \
    --data-urlencode 'can_join_group={"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 11}' \
    --data-urlencode 'can_leave_group={"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 15}' \
    --data-urlencode 'can_manage_group={"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 11}' \
    --data-urlencode 'can_mention_group={"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 11}' \
    --data-urlencode 'can_remove_members_group={"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 11}' \
    --data-urlencode deactivated=false
```

## Parameters
user_group_idintegerrequired in path
The ID of the target user group.
namestringoptional

```
"marketing team"
```
The new name of the group.
Changes: Before Zulip 7.0 (feature level 165), this was
a required field.
descriptionstringoptional

```
"The marketing team."
```
The new description of the group.
Changes: Before Zulip 7.0 (feature level 165), this was
a required field.
can_add_members_groupobjectoptional

```
{"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 11}
```
The set of users who have permission to add members to this user group
expressed as anupdate to a group-setting value.
Changes: New in Zulip 10.0 (feature level 305). Previously, this
permission was controlled by thecan_manage_groupsetting.
can_add_members_groupobject details:
- new:integer | objectrequiredThe newgroup-setting valuefor who would
have this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- old:integer | objectoptionalThe expected currentgroup-setting valuefor who has this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
can_join_groupobjectoptional

```
{"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 11}
```
The set of users who have permission to join this user group
expressed as anupdate to a group-setting value.
Changes: New in Zulip 10.0 (feature level 301).
can_join_groupobject details:
- new:integer | objectrequiredThe newgroup-setting valuefor who would
have this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- old:integer | objectoptionalThe expected currentgroup-setting valuefor who has this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
can_leave_groupobjectoptional

```
{"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 15}
```
The set of users who have permission to leave this user group
expressed as anupdate to a group-setting value.
Changes: New in Zulip 10.0 (feature level 308).
can_leave_groupobject details:
- new:integer | objectrequiredThe newgroup-setting valuefor who would
have this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- old:integer | objectoptionalThe expected currentgroup-setting valuefor who has this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
can_manage_groupobjectoptional

```
{"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 11}
```
The set of users who have permission tomanage this user groupexpressed as anupdate to a group-setting value.
This setting cannot be set to"role:internet"and"role:everyone"system groups.
Changes: New in Zulip 10.0 (feature level 283).
can_manage_groupobject details:
- new:integer | objectrequiredThe newgroup-setting valuefor who would
have this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- old:integer | objectoptionalThe expected currentgroup-setting valuefor who has this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
can_mention_groupobjectoptional

```
{"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 11}
```
The set of users who have permission tomention this group,
expressed as anupdate to a group-setting value.
This setting cannot be set to"role:internet"and"role:owners"system groups.
Changes: In Zulip 9.0 (feature level 260), this parameter was
updated to only accept an object with theoldandnewfields
described below. Prior to this feature level, this parameter could be
either of the two forms of agroup-setting value.
Before Zulip 9.0 (feature level 258), this parameter could only be the
integer form of agroup-setting value.
Before Zulip 8.0 (feature level 198), this parameter was namedcan_mention_group_id.
New in Zulip 8.0 (feature level 191). Previously, groups could be
mentioned only if they were notsystem groups.
can_mention_groupobject details:
- new:integer | objectrequiredThe newgroup-setting valuefor who would
have this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- old:integer | objectoptionalThe expected currentgroup-setting valuefor who has this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
can_remove_members_groupobjectoptional

```
{"new": {"direct_members": [10], "direct_subgroups": [11]}, "old": 11}
```
The set of users who have permission to remove members from this user group
expressed as anupdate to a group-setting value.
Changes: New in Zulip 10.0 (feature level 324). Previously, this
permission was controlled by thecan_manage_groupsetting.
can_remove_members_groupobject details:
- new:integer | objectrequiredThe newgroup-setting valuefor who would
have this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- old:integer | objectoptionalThe expected currentgroup-setting valuefor who has this permission.This parameter must be one of the following:The ID of theuser groupwith this permission.An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
1. The ID of theuser groupwith this permission.
2. An object with the following fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
deactivatedbooleanoptional
A deactivated user group can be reactivated by passing this
parameter asfalse.
Passingtruedoes nothing as user group is deactivated
usingPOST /user_groups/{user_group_id}/deactivateendpoint.

```
POST /user_groups/{user_group_id}/deactivate
```
Changes: New in Zulip 11.0 (feature level 386).

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
An example JSON response when the user group ID is invalid:

```
{"code":"BAD_REQUEST","msg":"Invalid user group","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"Invalid user group","result":"error"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.