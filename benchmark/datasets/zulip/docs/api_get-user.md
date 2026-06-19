# Get a user | Zulip API documentation

*Source: https://zulip.com/api/get-user*

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

# Get a user
GET https://your-org.zulipchat.com/api/v1/users/{user_id}
Fetch details for a single user in the organization.
You can also fetch details onall users in the organizationorby a user's Zulip API email.
Changes: In Zulip 12.0 (feature level 437), fixed a bug
dating to feature level 232, which caused guest users to
receive fake backwards-compatibility users in the format
intended for clients usingPOST /registerwithout theuser_list_incompleteclient capability.
New in Zulip 3.0 (feature level 1).

## Usage examples
Pythoncurl
- Python
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Fetch details on a user given a user ID.result=client.get_user_by_id(user_id)# If you'd like data on custom profile fields, you can request them as follows:result=client.get_user_by_id(user_id,include_custom_profile_fields=True)print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Fetch details on a user given a user ID.result=client.get_user_by_id(user_id)# If you'd like data on custom profile fields, you can request them as follows:result=client.get_user_by_id(user_id,include_custom_profile_fields=True)print(result)
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/users/12 \
    -u EMAIL_ADDRESS:API_KEY
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/users/12 \
    -u EMAIL_ADDRESS:API_KEY
```
You may pass theclient_gravatarorinclude_custom_profile_fieldsquery parameter as follows:
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/users/12 \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode client_gravatar=false \
    --data-urlencode include_custom_profile_fields=true
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/users/12 \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode client_gravatar=false \
    --data-urlencode include_custom_profile_fields=true
```

## Parameters
user_idintegerrequired in path
The target user's ID.
client_gravatarbooleanoptional
Whether the client supports computing gravatars URLs. If
enabled,avatar_urlwill be included in the response only
if there is a Zulip avatar, and will benullfor users who
are using gravatar as their avatar. This option
significantly reduces the compressed size of user data,
since gravatar URLs are long, random strings and thus do not
compress well. Theclient_gravatarfield is set totrueif
clients can compute their own gravatars.
Changes: The default value of this parameter wasfalseprior to Zulip 5.0 (feature level 92).
Defaults totrue.
include_custom_profile_fieldsbooleanoptional
Whether the client wantscustom profile fielddata to be included in the response.
Changes: New in Zulip 2.1.0. Previous versions do not offer these
data via the API.
Defaults tofalse.

## Response

#### Return values
- user:objectA dictionary containing basic data on a given Zulip user.Changes: Removedis_billing_adminfield in Zulip 10.0 (feature level 363), as it was
replaced by thecan_manage_billing_grouprealm setting.user_id:integerThe unique ID of the user.delivery_email:string | nullThe user's real email address. This value will benullif you cannot
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
user's message history.Changes: New in Zulip 12.0 (feature level 433).profile_data:objectOnly present ifis_botis false; bots can't have custom profile fields.A dictionary containing custom profile field data for the user. Each entry
maps the integer ID of a custom profile field in the organization to a
dictionary containing the user's data for that field. Generally the data
includes just a singlevaluekey; for those custom profile fields
supporting Markdown, arendered_valuekey will also be present.{id}:objectObject with data about what value the user filled in the custom
profile field with that ID.value:stringUser's personal value for this custom profile field.rendered_value:stringThevaluerendered in HTML. Will only be present for
custom profile field types that support Markdown rendering.This user-generated HTML content should be rendered
using the same CSS and client-side security protections
as are used for message content.SeeMarkdown message formattingfor details on Zulip's HTML format.
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
- profile_data:objectOnly present ifis_botis false; bots can't have custom profile fields.A dictionary containing custom profile field data for the user. Each entry
maps the integer ID of a custom profile field in the organization to a
dictionary containing the user's data for that field. Generally the data
includes just a singlevaluekey; for those custom profile fields
supporting Markdown, arendered_valuekey will also be present.{id}:objectObject with data about what value the user filled in the custom
profile field with that ID.value:stringUser's personal value for this custom profile field.rendered_value:stringThevaluerendered in HTML. Will only be present for
custom profile field types that support Markdown rendering.This user-generated HTML content should be rendered
using the same CSS and client-side security protections
as are used for message content.SeeMarkdown message formattingfor details on Zulip's HTML format.
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
- {id}:objectObject with data about what value the user filled in the custom
profile field with that ID.value:stringUser's personal value for this custom profile field.rendered_value:stringThevaluerendered in HTML. Will only be present for
custom profile field types that support Markdown rendering.This user-generated HTML content should be rendered
using the same CSS and client-side security protections
as are used for message content.SeeMarkdown message formattingfor details on Zulip's HTML format.
- value:stringUser's personal value for this custom profile field.
- rendered_value:stringThevaluerendered in HTML. Will only be present for
custom profile field types that support Markdown rendering.This user-generated HTML content should be rendered
using the same CSS and client-side security protections
as are used for message content.SeeMarkdown message formattingfor details on Zulip's HTML format.

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"msg":"","result":"success","user":{"avatar_url":"https://secure.gravatar.com/avatar/6d8cad0fd00256e7b40691d27ddfd466?d=identicon&version=1","bot_type":null,"date_joined":"2019-10-20T07:50:53.729659+00:00","delivery_email":null,"email":"hamlet@zulip.com","full_name":"King Hamlet","is_active":true,"is_admin":false,"is_bot":false,"is_guest":false,"is_imported_stub":false,"is_owner":false,"profile_data":{"1":{"rendered_value":"<p>+0-11-23-456-7890</p>","value":"+0-11-23-456-7890"},"2":{"rendered_value":"<p>I am:</p>\n<ul>\n<li>The prince of Denmark</li>\n<li>Nephew to the usurping Claudius</li>\n</ul>","value":"I am:\n* The prince of Denmark\n* Nephew to the usurping Claudius"},"3":{"rendered_value":"<p>Dark chocolate</p>","value":"Dark chocolate"},"4":{"value":"0"},"5":{"value":"1900-01-01"},"6":{"value":"https://blog.zulig.org"},"7":{"value":"[11]"},"8":{"value":"zulipbot"}},"role":400,"timezone":"","user_id":10}}
```

```
{"msg":"","result":"success","user":{"avatar_url":"https://secure.gravatar.com/avatar/6d8cad0fd00256e7b40691d27ddfd466?d=identicon&version=1","bot_type":null,"date_joined":"2019-10-20T07:50:53.729659+00:00","delivery_email":null,"email":"hamlet@zulip.com","full_name":"King Hamlet","is_active":true,"is_admin":false,"is_bot":false,"is_guest":false,"is_imported_stub":false,"is_owner":false,"profile_data":{"1":{"rendered_value":"<p>+0-11-23-456-7890</p>","value":"+0-11-23-456-7890"},"2":{"rendered_value":"<p>I am:</p>\n<ul>\n<li>The prince of Denmark</li>\n<li>Nephew to the usurping Claudius</li>\n</ul>","value":"I am:\n* The prince of Denmark\n* Nephew to the usurping Claudius"},"3":{"rendered_value":"<p>Dark chocolate</p>","value":"Dark chocolate"},"4":{"value":"0"},"5":{"value":"1900-01-01"},"6":{"value":"https://blog.zulig.org"},"7":{"value":"[11]"},"8":{"value":"zulipbot"}},"role":400,"timezone":"","user_id":10}}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.