# Create a reusable invitation link | Zulip API documentation

*Source: https://zulip.com/api/create-invite-link*

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

# Create a reusable invitation link
POST https://your-org.zulipchat.com/api/v1/invites/multiuse
Create areusable invitation linkwhich can be used to invite new users to the organization.
Changes: In Zulip 8.0 (feature level 209), added support for non-admin
userswith permissionto use this endpoint. Previously, it was restricted to administrators only.
In Zulip 6.0 (feature level 126), theinvite_expires_in_daysparameter was removed and replaced byinvite_expires_in_minutes.
In Zulip 5.0 (feature level 117), added support for passingnullas
theinvite_expires_in_daysparameter to request an invitation that never
expires.
In Zulip 5.0 (feature level 96), theinvite_expires_in_daysparameter was
added which specified the number of days before the invitation would expire.

## Usage examples
Pythoncurl
- Python
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Create a reusable invitation link.request={"invite_expires_in_minutes":60*24*10,# 10 days"invite_as":400,"stream_ids":stream_ids,}result=client.call_endpoint(url="/invites/multiuse",method="POST",request=request)print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Create a reusable invitation link.request={"invite_expires_in_minutes":60*24*10,# 10 days"invite_as":400,"stream_ids":stream_ids,}result=client.call_endpoint(url="/invites/multiuse",method="POST",request=request)print(result)
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/invites/multiuse \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode invite_expires_in_minutes=14400 \
    --data-urlencode invite_as=600 \
    --data-urlencode 'stream_ids=[1, 10]' \
    --data-urlencode 'group_ids=[]' \
    --data-urlencode include_realm_default_subscriptions=false \
    --data-urlencode 'welcome_message_custom_text=Welcome to Zulip! We'"'"'re excited to have you on board.'
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/invites/multiuse \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode invite_expires_in_minutes=14400 \
    --data-urlencode invite_as=600 \
    --data-urlencode 'stream_ids=[1, 10]' \
    --data-urlencode 'group_ids=[]' \
    --data-urlencode include_realm_default_subscriptions=false \
    --data-urlencode 'welcome_message_custom_text=Welcome to Zulip! We'"'"'re excited to have you on board.'
```

## Parameters
invite_expires_in_minutesinteger | nulloptional
The number of minutes before the invitation will expire. Ifnull, the
invitation will never expire. If unspecified, the server will use a default
value (based on theINVITATION_LINK_VALIDITY_MINUTESserver setting, which
defaults to 14400, i.e. 10 days) for when the invitation will expire.
Changes: New in Zulip 6.0 (feature level 126). Previously, there was aninvite_expires_in_daysparameter, which specified the duration in days instead
of minutes.
invite_asintegeroptional
Theorganization-level roleof the user that is
created when the invitation is accepted.
Possible values are:
- 100 = Organization owner
- 200 = Organization administrator
- 300 = Organization moderator
- 400 = Member
- 600 = Guest
Users can only create invitation links forroles with equal or stricter restrictionsas their own. For example, a moderator cannot invite someone to be an owner
or administrator, but they can invite them to be a moderator or member.
Changes: In Zulip 4.0 (feature level 61), added support for inviting
users as moderators.
Must be one of:100,200,300,400,600. 
Defaults to400.
stream_ids(integer)[]optional
A list containing theIDs of the channelsthat the
newly created user will be automatically subscribed to if the invitation
is accepted, in addition to any default channels that the new user may
be subscribed to based on theinclude_realm_default_subscriptionsparameter.
Requested channels must either be default channels for the
organization, or ones the acting user has permission to add
subscribers to.
This list must be empty if the current user has the unlikely
configuration of being able to create reusable invitation links while
lacking permission tosubscribe other users to
channels.
Changes: Prior to Zulip 10.0 (feature level 342), default channels
that the acting user did not directly have permission to add
subscribers to would be rejected.
Defaults to[].
group_ids(integer)[]optional
A list containing theIDs of the user groupsthat
the newly created user will be automatically added to if the invitation
is accepted. If the list is empty, then the new user will not be
added to any user groups. The acting user must have permission to add users
to the groups listed in this request.
Changes: New in Zulip 10.0 (feature level 322).
Defaults to[].
include_realm_default_subscriptionsbooleanoptional
Boolean indicating whether the newly created user should be subscribed
to thedefault channelsfor the organization.
Note that this parameter can betrueeven if the current user does
not generally have permission tosubscribe other users to
channels.
Changes: New in Zulip 9.0 (feature level 261). Previous versions
of Zulip behaved as though this parameter was alwaysfalse; clients
needed to include the organization's default channels in thestream_idsparameter for a newly created user to be automatically
subscribed to them.
Defaults tofalse.
welcome_message_custom_textstring | nulloptional

```
"Welcome to Zulip! We're excited to have you on board."
```
Custom message text, in Zulip Markdown format, to be sent by the
Welcome Bot to new users that join the organization via this
invitation.
Maximum length is 8000 Unicode code points.
Only organization administrators can use this feature; for other
users, the value is alwaysnull.
- null: the organization's defaultwelcome_message_custom_textis used.
- Empty string: no Welcome Bot custom message is sent.
- Otherwise, the provided string is the custom message.
Changes: New in Zulip 11.0 (feature level 416).

## Response

#### Return values
- invite_link:stringThe URL of thereusable invitation linkthat was created by this request.

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"invite_link":"https://example.zulipchat.com/join/yddhtzk4jgl7rsmazc5fyyyy/","msg":"","result":"success"}
```

```
{"invite_link":"https://example.zulipchat.com/join/yddhtzk4jgl7rsmazc5fyyyy/","msg":"","result":"success"}
```
An example JSON error response for when the user doesn't have permission
to send invitations.

```
{"code":"BAD_REQUEST","msg":"Insufficient permission","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"Insufficient permission","result":"error"}
```
An example JSON error response for when any of the specified channels
does not exist or the user does not have permission to access one of
the targeted channels.

```
{"code":"BAD_REQUEST","msg":"Invalid channel ID 11. No invites were sent.","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"Invalid channel ID 11. No invites were sent.","result":"error"}
```
An example JSON error response for when the user doesn't have permission
to subscribe other users to channels andstream_idsis not empty.

```
{"code":"BAD_REQUEST","msg":"You do not have permission to subscribe other users to channels.","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"You do not have permission to subscribe other users to channels.","result":"error"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.