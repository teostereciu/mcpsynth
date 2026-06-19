# Get all invitations | Zulip API documentation

*Source: https://zulip.com/api/get-invites*

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

# Get all invitations
GET https://your-org.zulipchat.com/api/v1/invites
Fetch all unexpiredinvitations(i.e. email
invitations and reusable invitation links) that can be managed by the user.
Note that administrators can manage invitations that were created by other users.
Changes: Prior to Zulip 8.0 (feature level 209), non-admin users could
only create email invitations, and therefore the response would never include
reusable invitation links for these users.

## Usage examples
Pythoncurl
- Python
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Get all invitations.result=client.call_endpoint(url="/invites",method="GET")print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Get all invitations.result=client.call_endpoint(url="/invites",method="GET")print(result)
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/invites \
    -u EMAIL_ADDRESS:API_KEY
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/invites \
    -u EMAIL_ADDRESS:API_KEY
```

## Parameters
This endpoint does not accept any parameters.

## Response

#### Return values
- invites:(object)[]An array of objects, each representing a single unexpiredinvitation.id:integerThe ID of the invitation.Note that email invitations and reusable invitation links are stored
in different database tables on the server, so each ID is guaranteed
to be unique in combination with the boolean value ofis_multiuse,
e.g. there can only be one invitation withid: 1andis_multiuse:
true.invited_by_user_id:integerTheuser IDof the user who created the invitation.Changes: New in Zulip 3.0 (feature level 22), replacing thereffield which contained the Zulip display email address of the user who
created the invitation.invited:integerThe UNIX timestamp for when the invitation was created, in UTC seconds.expiry_date:integer | nullThe UNIX timestamp for when the invitation will expire, in UTC seconds.
Ifnull, the invitation never expires.invited_as:integerTheorganization-level roleof the user that
is created when the invitation is accepted.
Possible values are:100 = Organization owner200 = Organization administrator300 = Organization moderator400 = Member600 = Guestemail:stringThe email address the invitation was sent to. This will not be present whenis_multiuseistrue(i.e. the invitation is a reusable invitation link).notify_referrer_on_join:booleanA boolean indicating whether the referrer has opted to receive a direct
message fromnotification botwhen a user
account is created using this invitation.Changes: New in Zulip 9.0 (feature level 267). Previously,
referrers always received such direct messages.link_url:stringThe URL of the reusable invitation link. This will not be present whenis_multiuseisfalse(i.e. the invitation is an email invitation).is_multiuse:booleanA boolean specifying whether theinvitationis a
reusable invitation link or an email invitation.
- id:integerThe ID of the invitation.Note that email invitations and reusable invitation links are stored
in different database tables on the server, so each ID is guaranteed
to be unique in combination with the boolean value ofis_multiuse,
e.g. there can only be one invitation withid: 1andis_multiuse:
true.
- invited_by_user_id:integerTheuser IDof the user who created the invitation.Changes: New in Zulip 3.0 (feature level 22), replacing thereffield which contained the Zulip display email address of the user who
created the invitation.
- invited:integerThe UNIX timestamp for when the invitation was created, in UTC seconds.
- expiry_date:integer | nullThe UNIX timestamp for when the invitation will expire, in UTC seconds.
Ifnull, the invitation never expires.
- invited_as:integerTheorganization-level roleof the user that
is created when the invitation is accepted.
Possible values are:100 = Organization owner200 = Organization administrator300 = Organization moderator400 = Member600 = Guest
- email:stringThe email address the invitation was sent to. This will not be present whenis_multiuseistrue(i.e. the invitation is a reusable invitation link).
- notify_referrer_on_join:booleanA boolean indicating whether the referrer has opted to receive a direct
message fromnotification botwhen a user
account is created using this invitation.Changes: New in Zulip 9.0 (feature level 267). Previously,
referrers always received such direct messages.
- link_url:stringThe URL of the reusable invitation link. This will not be present whenis_multiuseisfalse(i.e. the invitation is an email invitation).
- is_multiuse:booleanA boolean specifying whether theinvitationis a
reusable invitation link or an email invitation.
- 100 = Organization owner
- 200 = Organization administrator
- 300 = Organization moderator
- 400 = Member
- 600 = Guest

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"invites":[{"email":"example@zulip.com","expiry_date":null,"id":1,"invited":1710606654,"invited_as":200,"invited_by_user_id":9,"is_multiuse":false,"notify_referrer_on_join":true},{"expiry_date":1711463862,"id":1,"invited":1710599862,"invited_as":400,"invited_by_user_id":9,"is_multiuse":true,"link_url":"https://example.zulipchat.com/join/yddhtzk4jgl7rsmazc5fyyyy/","notify_referrer_on_join":true}],"msg":"","result":"success"}
```

```
{"invites":[{"email":"example@zulip.com","expiry_date":null,"id":1,"invited":1710606654,"invited_as":200,"invited_by_user_id":9,"is_multiuse":false,"notify_referrer_on_join":true},{"expiry_date":1711463862,"id":1,"invited":1710599862,"invited_as":400,"invited_by_user_id":9,"is_multiuse":true,"link_url":"https://example.zulipchat.com/join/yddhtzk4jgl7rsmazc5fyyyy/","notify_referrer_on_join":true}],"msg":"","result":"success"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.