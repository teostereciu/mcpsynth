# Fetch an API key (JWT) | Zulip API documentation

*Source: https://zulip.com/api/jwt-fetch-api-key*

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

# Fetch an API key (JWT)
POST https://your-org.zulipchat.com/api/v1/jwt/fetch_api_key
This API endpoint is used by clients to implement JSON Web Token
(JWT) authentication. Given a JWT identifying a Zulip user, it
returns a Zulip API key that the client can use to make requests
as the user.
Note:This endpoint is only useful for Zulip servers/organizations
withJSON web token authenticationenabled.
See theAPI keysdocumentation for more details
on how to manage API keys manually.
Changes: New in Zulip 7.0 (feature level 160).

## Usage examples
curl
- curl

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/jwt/fetch_api_key \
    --data-urlencode token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImhhbWxldEB6dWxpcC5jb20ifQ.EsHxSVt54zPR-ywgPH54TB1FYmrGKsfq7hsQEhp_9w0 \
    --data-urlencode include_profile=false
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/jwt/fetch_api_key \
    --data-urlencode token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImhhbWxldEB6dWxpcC5jb20ifQ.EsHxSVt54zPR-ywgPH54TB1FYmrGKsfq7hsQEhp_9w0 \
    --data-urlencode include_profile=false
```

## Parameters
tokenstringrequired

```
"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImhhbWxldEB6dWxpcC5jb20ifQ.EsHxSVt54zPR-ywgPH54TB1FYmrGKsfq7hsQEhp_9w0"
```
A JSON Web Token for the target user.
The token payload must contain a customemailclaim with the target
user's email address, e.g.,{"email": "<target user email>"}.
include_profilebooleanoptional
Whether to include auserobject containing the target
user's profile details in the response.
Defaults tofalse.

## Response

#### Return values
- api_key:stringThe API key that can be used to authenticate as the requested user.
- email:stringThe email address of the user who owns the API key.
- user:objectOnly present ifinclude_profileparameter was set totrue.A dictionary with data on the target user.user_id:integerThe unique ID of the user.delivery_email:string | nullThe user's real email address. This value will benullif you cannot
access user's real email address. For bot users, this field is always
set to the real email of the bot, because bot users always haveemail_address_visibilityset to everyone.Changes: Prior to Zulip 7.0 (feature level 163), this field was
present only whenemail_address_visibilitywas restricted and you had
access to the user's real email. As of this feature level, this field
is always present, including the case whenemail_address_visibilityis set to everyone (and therefore not restricted).email:stringThe Zulip API email address of the user or bot.If you do not have permission to view the email address of the target user,
this will be a fake email address that is usable for the Zulip API but nothing else.full_name:stringFull name of the user or bot, used for all display purposes.date_joined:stringThe time when the user joined. For users imported from other
applications and users created via the API, this is set to the
account creation time until the user logs in for the first time,
after which it is updated to that login time.For imported users, clients can use theis_imported_stubflag
to determine how to display this field: whenis_imported_stubistrue, the user has not yet logged in and this value is the
account creation time during import; whenis_imported_stubisfalse, this value reflects when the user first logged in.Changes: Starting with Zulip 12.0 (feature level 475),
this field is updated when an imported stub user or a user created
via the API logs in for the first time.is_active:booleanA boolean specifying whether the user account has been deactivated.is_owner:booleanA boolean specifying whether the user is an organization owner.
If true,is_adminwill also be true.Changes: New in Zulip 3.0 (feature level 8).is_admin:booleanA boolean specifying whether the user is an organization administrator.is_guest:booleanA boolean specifying whether the user is a guest user.is_bot:booleanA boolean specifying whether the user is a bot or full account.bot_type:integer | nullAn integer describing the type of bot:nullif the user isn't a bot.1for aGenericbot.2for anIncoming webhookbot.3for anOutgoing webhookbot.4for anEmbeddedbot.bot_owner_id:integer | nullIf the user is a bot (i.e.is_botis true), thenbot_owner_idis the user ID of the bot's owner (usually, whoever created the bot).Will benullfor legacy bots that do not have an owner.Changes: New in Zulip 3.0 (feature level 1). In previous
versions, there was abot_ownerfield containing the email
address of the bot's owner.role:integerOrganization-level roleof the user.
Possible values are:100 = Organization owner200 = Organization administrator300 = Organization moderator400 = Member600 = GuestChanges: New in Zulip 4.0 (feature level 59).timezone:stringThe IANA identifier of the user'sprofile time zone,
which is used primarily to display the user's local time to other users.avatar_url:string | nullURL for the user's avatar.Will benullif theclient_gravatarquery parameter was set totrue, the current user has access to
this user's real email address, and this user's avatar is hosted by
the Gravatar provider (i.e. this user has never uploaded an avatar).Changes: Before Zulip 7.0 (feature level 163), access to a
user's real email address was a realm-level setting. As of this
feature level,email_address_visibilityis a user setting.In Zulip 3.0 (feature level 18), if the client has theuser_avatar_url_field_optionalcapability, this will be missing at
the server's sole discretion.avatar_version:integerVersion for the user's avatar. Used for cache-busting requests
for the user's avatar. Clients generally shouldn't need to use this;
most avatar URLs sent by Zulip will already end with?v={avatar_version}.is_imported_stub:booleanIndicates whether this user object is a stub account imported from
another chat system. Stub accounts are used to represent the senders
for imported messages. Stub accounts can be converted to regular Zulip
accounts when the user starts using Zulip, preserving that imported
user's message history.Changes: New in Zulip 12.0 (feature level 433).
- user_id:integerThe unique ID of the user.
- delivery_email:string | nullThe user's real email address. This value will benullif you cannot
access user's real email address. For bot users, this field is always
set to the real email of the bot, because bot users always haveemail_address_visibilityset to everyone.Changes: Prior to Zulip 7.0 (feature level 163), this field was
present only whenemail_address_visibilitywas restricted and you had
access to the user's real email. As of this feature level, this field
is always present, including the case whenemail_address_visibilityis set to everyone (and therefore not restricted).
- email:stringThe Zulip API email address of the user or bot.If you do not have permission to view the email address of the target user,
this will be a fake email address that is usable for the Zulip API but nothing else.
- full_name:stringFull name of the user or bot, used for all display purposes.
- date_joined:stringThe time when the user joined. For users imported from other
applications and users created via the API, this is set to the
account creation time until the user logs in for the first time,
after which it is updated to that login time.For imported users, clients can use theis_imported_stubflag
to determine how to display this field: whenis_imported_stubistrue, the user has not yet logged in and this value is the
account creation time during import; whenis_imported_stubisfalse, this value reflects when the user first logged in.Changes: Starting with Zulip 12.0 (feature level 475),
this field is updated when an imported stub user or a user created
via the API logs in for the first time.
- is_active:booleanA boolean specifying whether the user account has been deactivated.
- is_owner:booleanA boolean specifying whether the user is an organization owner.
If true,is_adminwill also be true.Changes: New in Zulip 3.0 (feature level 8).
- is_admin:booleanA boolean specifying whether the user is an organization administrator.
- is_guest:booleanA boolean specifying whether the user is a guest user.
- is_bot:booleanA boolean specifying whether the user is a bot or full account.
- bot_type:integer | nullAn integer describing the type of bot:nullif the user isn't a bot.1for aGenericbot.2for anIncoming webhookbot.3for anOutgoing webhookbot.4for anEmbeddedbot.
- bot_owner_id:integer | nullIf the user is a bot (i.e.is_botis true), thenbot_owner_idis the user ID of the bot's owner (usually, whoever created the bot).Will benullfor legacy bots that do not have an owner.Changes: New in Zulip 3.0 (feature level 1). In previous
versions, there was abot_ownerfield containing the email
address of the bot's owner.
- role:integerOrganization-level roleof the user.
Possible values are:100 = Organization owner200 = Organization administrator300 = Organization moderator400 = Member600 = GuestChanges: New in Zulip 4.0 (feature level 59).
- timezone:stringThe IANA identifier of the user'sprofile time zone,
which is used primarily to display the user's local time to other users.
- avatar_url:string | nullURL for the user's avatar.Will benullif theclient_gravatarquery parameter was set totrue, the current user has access to
this user's real email address, and this user's avatar is hosted by
the Gravatar provider (i.e. this user has never uploaded an avatar).Changes: Before Zulip 7.0 (feature level 163), access to a
user's real email address was a realm-level setting. As of this
feature level,email_address_visibilityis a user setting.In Zulip 3.0 (feature level 18), if the client has theuser_avatar_url_field_optionalcapability, this will be missing at
the server's sole discretion.
- avatar_version:integerVersion for the user's avatar. Used for cache-busting requests
for the user's avatar. Clients generally shouldn't need to use this;
most avatar URLs sent by Zulip will already end with?v={avatar_version}.
- is_imported_stub:booleanIndicates whether this user object is a stub account imported from
another chat system. Stub accounts are used to represent the senders
for imported messages. Stub accounts can be converted to regular Zulip
accounts when the user starts using Zulip, preserving that imported
user's message history.Changes: New in Zulip 12.0 (feature level 433).
- nullif the user isn't a bot.
- 1for aGenericbot.
- 2for anIncoming webhookbot.
- 3for anOutgoing webhookbot.
- 4for anEmbeddedbot.
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
{"api_key":"gjA04ZYcqXKalvYMA8OeXSfzUOLrtbZv","email":"hamlet@zulip.com","msg":"","result":"success"}
```

```
{"api_key":"gjA04ZYcqXKalvYMA8OeXSfzUOLrtbZv","email":"hamlet@zulip.com","msg":"","result":"success"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.