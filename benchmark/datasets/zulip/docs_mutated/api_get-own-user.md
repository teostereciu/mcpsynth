# Get own user | Zulip API documentation

*Source: https://zulip.com/api/get-own-user*

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

# Get own user
GET https://your-org.zulipchat.com/api/v1/users/me
Get basic data about the user/bot that requests this endpoint.
Changes: Removedis_billing_adminfield in Zulip 10.0 (feature level 363), as it was
replaced by thecan_manage_billing_grouprealm setting.

## Usage examples
PythonJavaScriptcurl
- Python
- JavaScript
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Get the profile of the user/bot that requests this endpoint,# which is `client` in this case.result=client.get_profile()print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Get the profile of the user/bot that requests this endpoint,# which is `client` in this case.result=client.get_profile()print(result)
```
More examples and documentation can be foundhere.

```
constzulipInit=require("zulip-js");// Pass the path to your zuliprc file here.constconfig={zuliprc:"zuliprc"};(async()=>{constclient=awaitzulipInit(config);// Get the profile of the user/bot that requests this endpoint,// which is `client` in this case:console.log(awaitclient.users.me.getProfile());})();
```

```
constzulipInit=require("zulip-js");// Pass the path to your zuliprc file here.constconfig={zuliprc:"zuliprc"};(async()=>{constclient=awaitzulipInit(config);// Get the profile of the user/bot that requests this endpoint,// which is `client` in this case:console.log(awaitclient.users.me.getProfile());})();
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/users/me \
    -u EMAIL_ADDRESS:API_KEY
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/users/me \
    -u EMAIL_ADDRESS:API_KEY
```

## Parameters
This endpoint does not accept any parameters.

## Response

#### Return values
- avatar_url:stringURL for the requesting user's avatar.Changes: New in Zulip 2.1.0.
- avatar_version:integerVersion for the requesting user's avatar. Used for cache-busting requests
for the user's avatar. Clients generally shouldn't need to use this;
most avatar URLs sent by Zulip will already end with?v={avatar_version}.Changes: New in Zulip 3.0 (feature level 10).
- email:stringZulip API email of the requesting user.
- full_name:stringFull name of the requesting user.
- is_admin:booleanA boolean indicating if the requesting user is an admin.
- is_owner:booleanA boolean indicating if the requesting user is
an organization owner.Changes: New in Zulip 3.0 (feature level 8).
- role:integerOrganization-level roleof
the requesting user.
Possible values are:100 = Organization owner200 = Organization administrator300 = Organization moderator400 = Member600 = GuestChanges: New in Zulip 4.0 (feature level 59).
- is_guest:booleanA boolean indicating if the requesting user is a guest.Changes: New in Zulip 3.0 (feature level 10).
- is_bot:booleanA boolean indicating if the requesting user is a bot.
- is_active:booleanA boolean specifying whether the requesting user account
has been deactivated.Changes: New in Zulip 3.0 (feature level 10).
- timezone:stringThe IANA identifier of the requesting user'sprofile time zone,
which is used primarily to display the user's local time to other users.Changes: New in Zulip 3.0 (feature level 10).
- date_joined:stringThe time when the user joined. For users imported from other
applications and users created via the API, this is set to the
account creation time until the user logs in for the first time,
after which it is updated to that login time.For imported users, clients can use theis_imported_stubflag
to determine how to display this field: whenis_imported_stubistrue, the user has not yet logged in and this value is the
account creation time during import; whenis_imported_stubisfalse, this value reflects when the user first logged in.Changes: Starting with Zulip 12.0 (feature level 475),
this field is updated when an imported stub user or a user created
via the API logs in for the first time.New in Zulip 3.0 (feature level 10).
- max_message_id:integerThe integer ID of the last message received by the requesting
user's account.Deprecated. We plan to remove this in favor of recommending
usingGET /messageswith"start_message_id": "newest".
- user_id:integerThe user's ID.
- delivery_email:stringThe requesting user's real email address.Changes: Prior to Zulip 7.0 (feature level 163), this field was
present only whenemail_address_visibilitywas restricted and the
requesting user had permission to access realm users' emails. As of
this feature level, this field is always present.
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
{"avatar_url":"https://secure.gravatar.com/avatar/af4f06322c177ef4e1e9b2c424986b54?d=identicon&version=1","avatar_version":1,"date_joined":"2019-10-20T07:50:53.728864+00:00","delivery_email":"iago@zulip.com","email":"iago@zulip.com","full_name":"Iago","is_active":true,"is_admin":true,"is_bot":false,"is_guest":false,"is_imported_stub":false,"is_owner":false,"max_message_id":30,"msg":"","profile_data":{"1":{"rendered_value":"<p>+1-234-567-8901</p>","value":"+1-234-567-8901"},"2":{"rendered_value":"<p>Betrayer of Othello.</p>","value":"Betrayer of Othello."},"3":{"rendered_value":"<p>Apples</p>","value":"Apples"},"4":{"value":"emacs"},"5":{"value":"2000-01-01"},"6":{"value":"https://zulip.readthedocs.io/en/latest/"},"7":{"value":"[10]"},"8":{"value":"zulip"}},"result":"success","role":200,"timezone":"","user_id":5}
```

```
{"avatar_url":"https://secure.gravatar.com/avatar/af4f06322c177ef4e1e9b2c424986b54?d=identicon&version=1","avatar_version":1,"date_joined":"2019-10-20T07:50:53.728864+00:00","delivery_email":"iago@zulip.com","email":"iago@zulip.com","full_name":"Iago","is_active":true,"is_admin":true,"is_bot":false,"is_guest":false,"is_imported_stub":false,"is_owner":false,"max_message_id":30,"msg":"","profile_data":{"1":{"rendered_value":"<p>+1-234-567-8901</p>","value":"+1-234-567-8901"},"2":{"rendered_value":"<p>Betrayer of Othello.</p>","value":"Betrayer of Othello."},"3":{"rendered_value":"<p>Apples</p>","value":"Apples"},"4":{"value":"emacs"},"5":{"value":"2000-01-01"},"6":{"value":"https://zulip.readthedocs.io/en/latest/"},"7":{"value":"[10]"},"8":{"value":"zulip"}},"result":"success","role":200,"timezone":"","user_id":5}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.