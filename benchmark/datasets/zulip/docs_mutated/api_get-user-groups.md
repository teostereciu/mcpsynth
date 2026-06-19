# Get user groups | Zulip API documentation

*Source: https://zulip.com/api/get-user-groups*

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

# Get user groups
GET https://your-org.zulipchat.com/api/v1/user_groups
Fetches all of the user groups in the organization.
Note: This endpoint is only available tomembers and
administrators; bots and guests
cannot use this endpoint.

## Usage examples
Pythoncurl
- Python
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Get all user groups of the organization.result=client.get_user_groups()print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Get all user groups of the organization.result=client.get_user_groups()print(result)
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/user_groups \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode include_deactivated_groups=true
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/user_groups \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode include_deactivated_groups=true
```

## Parameters
include_deactivated_groupsbooleanoptional
Whether to include deactivated user groups in the response.
Changes: In Zulip 10.0 (feature level 294), renamedallow_deactivatedtoinclude_deactivated_groups.
New in Zulip 10.0 (feature level 290). Previously, deactivated
user groups did not exist and thus would never be included in
the response.
Defaults tofalse.

## Response

#### Return values
- user_groups:(object)[]A list ofuser_groupobjects.description:stringThe human-readable description of the user group.id:integerThe user group's integer ID.date_created:integer | nullThe UNIX timestamp for when the user group was created, in UTC seconds.Anullvalue means the user group has no recorded date, which is often
because the group predates the metadata being tracked starting in Zulip 8.0,
or because it was created via a data import tool
ormanagement command.Changes: New in Zulip 10.0 (feature level 292).creator_id:integer | nullThe ID of the user who created this user group.Anullvalue means the user group has no recorded creator, which is often
because the group predates the metadata being tracked starting in Zulip 8.0,
or because it was created via a data import tool
ormanagement command.Changes: New in Zulip 10.0 (feature level 292).members:(integer)[]The integer user IDs of the user group's members, which
are guaranteed to be non-deactivated users in the organization.Changes: Prior to Zulip 10.0 (feature level 303), this
list also included deactivated users who were members of
the user group before being deactivated.direct_subgroup_ids:(integer)[]The integer user group IDs of the direct subgroups.Changes: New in Zulip 6.0 (feature level 131).
Introduced in feature level 127 assubgroups, but
clients can ignore older events as this feature level
predates subgroups being fully implemented.name:stringUser group name.is_system_group:booleanWhether the user group is a system group which cannot be
modified by users.Changes: New in Zulip 5.0 (feature level 93).can_add_members_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to add members to this user group.Changes: New in Zulip 10.0 (feature level 305). Previously, this
permission was controlled by thecan_manage_groupsetting.Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_join_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to join this user group.Changes: New in Zulip 10.0 (feature level 301).Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_leave_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to leave this user group.Changes: New in Zulip 10.0 (feature level 308).Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_manage_group:integer | objectAgroup-setting valuedefining the set of users who
have permission tomanage this user group.Changes: New in Zulip 10.0 (feature level 283).Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_mention_group:integer | objectAgroup-setting valuedefining the set of users who
have permission tomention this user group.Changes: Before Zulip 9.0 (feature level 258), this setting was
always the integer form of agroup-setting value.Before Zulip 8.0 (feature level 198), this setting was namedcan_mention_group_id.New in Zulip 8.0 (feature level 191). Previously, groups could be
mentioned only if they were notsystem groups.Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.can_remove_members_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to remove members from this user group.Changes: New in Zulip 10.0 (feature level 324). Previously, this
permission was controlled by thecan_manage_groupsetting.Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.deactivated:booleanWhether the user group is deactivated. Deactivated groups
cannot be used as a subgroup of another group or used for
any other purpose.Changes: New in Zulip 10.0 (feature level 290).
- description:stringThe human-readable description of the user group.
- id:integerThe user group's integer ID.
- date_created:integer | nullThe UNIX timestamp for when the user group was created, in UTC seconds.Anullvalue means the user group has no recorded date, which is often
because the group predates the metadata being tracked starting in Zulip 8.0,
or because it was created via a data import tool
ormanagement command.Changes: New in Zulip 10.0 (feature level 292).
- creator_id:integer | nullThe ID of the user who created this user group.Anullvalue means the user group has no recorded creator, which is often
because the group predates the metadata being tracked starting in Zulip 8.0,
or because it was created via a data import tool
ormanagement command.Changes: New in Zulip 10.0 (feature level 292).
- members:(integer)[]The integer user IDs of the user group's members, which
are guaranteed to be non-deactivated users in the organization.Changes: Prior to Zulip 10.0 (feature level 303), this
list also included deactivated users who were members of
the user group before being deactivated.
- direct_subgroup_ids:(integer)[]The integer user group IDs of the direct subgroups.Changes: New in Zulip 6.0 (feature level 131).
Introduced in feature level 127 assubgroups, but
clients can ignore older events as this feature level
predates subgroups being fully implemented.
- name:stringUser group name.
- is_system_group:booleanWhether the user group is a system group which cannot be
modified by users.Changes: New in Zulip 5.0 (feature level 93).
- can_add_members_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to add members to this user group.Changes: New in Zulip 10.0 (feature level 305). Previously, this
permission was controlled by thecan_manage_groupsetting.Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_join_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to join this user group.Changes: New in Zulip 10.0 (feature level 301).Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_leave_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to leave this user group.Changes: New in Zulip 10.0 (feature level 308).Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_manage_group:integer | objectAgroup-setting valuedefining the set of users who
have permission tomanage this user group.Changes: New in Zulip 10.0 (feature level 283).Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_mention_group:integer | objectAgroup-setting valuedefining the set of users who
have permission tomention this user group.Changes: Before Zulip 9.0 (feature level 258), this setting was
always the integer form of agroup-setting value.Before Zulip 8.0 (feature level 198), this setting was namedcan_mention_group_id.New in Zulip 8.0 (feature level 191). Previously, groups could be
mentioned only if they were notsystem groups.Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- can_remove_members_group:integer | objectAgroup-setting valuedefining the set of users who
have permission to remove members from this user group.Changes: New in Zulip 10.0 (feature level 324). Previously, this
permission was controlled by thecan_manage_groupsetting.Will be one of the following:The ID of theuser groupwith this permission.An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- deactivated:booleanWhether the user group is deactivated. Deactivated groups
cannot be used as a subgroup of another group or used for
any other purpose.Changes: New in Zulip 10.0 (feature level 290).
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- The ID of theuser groupwith this permission.
- An object with these fields:direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.
- direct_members:(integer)[]The list of IDs of individual users in the collection of users with this permission.Changes: Prior to Zulip 10.0 (feature level 303), this list would include
deactivated users who had the permission before being deactivated.
- direct_subgroups:(integer)[]The list of IDs of the groups in the collection of users with this permission.

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"msg":"","result":"success","user_groups":[{"can_add_members_group":16,"can_join_group":16,"can_leave_group":15,"can_manage_group":16,"can_mention_group":11,"can_remove_members_group":16,"creator_id":null,"date_created":null,"description":"Owners of this organization","direct_subgroup_ids":[],"id":1,"is_system_group":true,"members":[1],"name":"role:owners"},{"can_add_members_group":17,"can_join_group":17,"can_leave_group":15,"can_manage_group":17,"can_mention_group":12,"can_remove_members_group":16,"creator_id":null,"date_created":null,"description":"Administrators of this organization, including owners","direct_subgroup_ids":[1],"id":2,"is_system_group":true,"members":[2],"name":"role:administrators"},{"can_add_members_group":20,"can_join_group":20,"can_leave_group":15,"can_manage_group":20,"can_mention_group":13,"can_remove_members_group":16,"creator_id":null,"date_created":1717484476,"description":"Characters of Hamlet","direct_subgroup_ids":[],"id":3,"is_system_group":false,"members":[3,4],"name":"hamletcharacters"}]}
```

```
{"msg":"","result":"success","user_groups":[{"can_add_members_group":16,"can_join_group":16,"can_leave_group":15,"can_manage_group":16,"can_mention_group":11,"can_remove_members_group":16,"creator_id":null,"date_created":null,"description":"Owners of this organization","direct_subgroup_ids":[],"id":1,"is_system_group":true,"members":[1],"name":"role:owners"},{"can_add_members_group":17,"can_join_group":17,"can_leave_group":15,"can_manage_group":17,"can_mention_group":12,"can_remove_members_group":16,"creator_id":null,"date_created":null,"description":"Administrators of this organization, including owners","direct_subgroup_ids":[1],"id":2,"is_system_group":true,"members":[2],"name":"role:administrators"},{"can_add_members_group":20,"can_join_group":20,"can_leave_group":15,"can_manage_group":20,"can_mention_group":13,"can_remove_members_group":16,"creator_id":null,"date_created":1717484476,"description":"Characters of Hamlet","direct_subgroup_ids":[],"id":3,"is_system_group":false,"members":[3,4],"name":"hamletcharacters"}]}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.