# Update your presence | Zulip API documentation

*Source: https://zulip.com/api/update-presence*

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

# Update your presence
POST https://your-org.zulipchat.com/api/v1/users/me/presence
Update the current user'spresenceand fetch presence data
of other users in the organization.
This endpoint is meant to be used by clients for both:
- Reporting the current user's presence status ("active"or"idle")
  to the server.
- Obtaining the presence data of all other users in the organization via
  regular polling.
Accurate user presence is one of the most expensive parts of any
chat application (in terms of bandwidth and other resources). Therefore,
it is important that clients implementing Zulip's user presence system
use the modernlast_update_idprotocol to
minimize fetching duplicate user presence data.

```
last_update_id
```
Client apps implementing presence are recommended to also consumepresenceevents), in order to learn about newly online users
immediately.
The Zulip server is responsible for implementinginvisible mode,
which disables sharing a user's presence data. Nonetheless, clients
should check thepresence_enabledfield in user objects in order to
display the current user as online or offline based on whether they are
sharing their presence information.
Changes: As of Zulip 8.0 (feature level 228), if theCAN_ACCESS_ALL_USERS_GROUP_LIMITS_PRESENCEserver-level setting istrue, then user presence data in the response islimited to users
the current user can see/access.

## Usage examples
Pythoncurl
- Python
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Update your presence.request={"status":"active","ping_only":False,"new_user_input":False,"last_update_id":-1,}result=client.update_presence(request)print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Update your presence.request={"status":"active","ping_only":False,"new_user_input":False,"last_update_id":-1,}result=client.update_presence(request)print(result)
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/users/me/presence \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode last_update_id=5 \
    --data-urlencode history_limit_days=365 \
    --data-urlencode new_user_input=false \
    --data-urlencode ping_only=false \
    --data-urlencode slim_presence=false \
    --data-urlencode status=active
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/users/me/presence \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode last_update_id=5 \
    --data-urlencode history_limit_days=365 \
    --data-urlencode new_user_input=false \
    --data-urlencode ping_only=false \
    --data-urlencode slim_presence=false \
    --data-urlencode status=active
```

## Parameters
last_update_idintegeroptional
The identifier that specifies what presence data the client already
has received, which allows the server to only return more recent
user presence data.
This should be set to-1during initialization of the client in
order to fetch all user presence data, unless the client is obtaining
initial user presence metadata from thePOST /registerendpoint.

```
POST /register
```
In subsequent queries to this endpoint, this value should be set to the
most recent value ofpresence_last_update_idreturned by the server
in this endpoint's response, which implements incremental fetching
of user presence data.
When this parameter is passed, the user presence data in the response
will always be in the modern format.
Changes: New in Zulip 9.0 (feature level 263). Previously, the
server sent user presence data for all users who had been active in the
last two weeks unconditionally.
history_limit_daysintegeroptional
Limits how far back in time to fetch user presence data. If not specified,
defaults to 14 days. A value of N means that the oldest presence data
fetched will be from at most N days ago.
Note that this is only useful during the initial user presence data fetch,
as subsequent fetches should use thelast_update_idparameter, which
will act as the limit on how much presence data is returned.history_limit_daysis ignored iflast_update_idis passed with a value greater than0,
indicating that the client already has some presence data.
Changes: New in Zulip 10.0 (feature level 288).
new_user_inputbooleanoptional
Whether the user has interacted with the client (e.g. moved the mouse,
used the keyboard, etc.) since the previous presence request from this
client.
The server uses data from this parameter to implement certainusage
statistics.
User interface clients that might run in the background, without the
user ever interacting with them, should be careful to only passtrueif the user has actually interacted with the client in order to avoid
corrupting usage statistics graphs.
Defaults tofalse.
ping_onlybooleanoptional
Whether the client is sending a ping-only request, meaning it only
wants to update the user's presencestatuson the server.
Otherwise, also requests the server return user presence data for all
users in the organization, which is further specified by thelast_update_idparameter.

```
last_update_id
```
Defaults tofalse.
statusstringrequired
The status of the user on this client.
Clients should report the user as"active"on this device if the client
knows that the user is presently using the device (and thus would
potentially see a notification immediately), even if the user
has not directly interacted with the Zulip client.
Otherwise, it should report the user as"idle".
See the relatednew_user_inputparameter
for how a client should report whether the user is actively using the
Zulip client.

```
new_user_input
```
Must be one of:"idle","active".
slim_presencebooleanoptionalDeprecated
Legacy parameter for configuring the format (modern or legacy) in
which the server will return user presence data for the organization.
Modern clients should uselast_update_id, which guarantees that
user presence data will be returned in the modern format, and
should not pass this parameter astrueunless interacting with an
older server.

```
last_update_id
```
Legacy clients that do not yet supportlast_update_idmay use the
value oftrueto request the modern format for user presence data.
Note: The legacy format for user presence data will be removed
entirely in a future release.
Changes:Deprecatedin Zulip 9.0 (feature level 263). Using
the modernlast_update_idparameter is the recommended way to
request the modern format for user presence data.
New in Zulip 3.0 (no feature level as it was an unstable API at that
point).
Defaults tofalse.

## Response

#### Return values
- presence_last_update_id:integerThe identifier for the latest user presence data returned in
thepresencesdata of the response.If a value was passed forlast_update_id, then this is
guaranteed to be equal to or greater than that value. If it
is the same value, then that indicates to the client that
there were no updates to previously received user presence
data.The client should then pass this value as thelast_update_idparameter when it next queries this endpoint, in order to only
receive new user presence data and avoid redundantly fetching
already known information.This will be-1if no value was passed forlast_update_idand no user
presence data was returned by the server. This can happen, for
example, if an organization has disabled presence.Changes: New in Zulip 9.0 (feature level 263).
- server_timestamp:numberOnly present ifping_onlyisfalse.The time when the server fetched thepresencesdata included
in the response.
- presences:objectOnly present ifping_onlyisfalse.A dictionary where each entry describes the presence details
of a user in the Zulip organization. Entries can be in either
the modern presence format or the legacy presence format.These entries will be the modern presence format when thelast_updated_idparameter is passed, or when the deprecatedslim_presenceparameter istrue.If the deprecatedslim_presenceparameter isfalseand thelast_updated_idparameter is omitted, the entries will be in
the legacy presence API format.Note: The legacy presence format should only be used when
interacting with old servers. It will be removed as soon as
doing so is practical.Will be one of these two formats (modern or legacy) for user
    presence data:{user_id}:objectPresence data (modern format) for the user with
the specified ID.active_timestamp:integerThe UNIX timestamp of the last time a client connected
to Zulip reported that the user was actually present
(e.g. via focusing a browser window or interacting
with a computer running the desktop app).Clients should display users with a currentactive_timestampas fully present.idle_timestamp:integerThe UNIX timestamp of the last time the user had a
client connected to Zulip, including idle clients
where the user hasn't interacted with the system
recently.The Zulip server has no way of distinguishing whether
an idle web app user is at their computer, but hasn't
interacted with the Zulip tab recently, or simply left
their desktop computer on when they left.Thus, clients should display users with a currentidle_timestampbut no currentactive_timestampas
potentially present.{user_email}:objectPresence data (legacy format) for the user with
the specified Zulip API email.{client_name}or"aggregated":objectObject containing the details of the user's
presence.Changes: Starting with Zulip 7.0 (feature level 178), this will always
contain two keys,"website"and"aggregated", with identical data. The
server no longer stores which client submitted presence updates.Previously, the{client_name}keys for these objects were the names of the
different clients where the user was logged in, for examplewebsiteorZulipDesktop.client:stringThe client's platform name.Changes: Starting with Zulip 7.0 (feature level 178), this will
always be"website"as the server no longer stores which client
submitted presence data.status:stringThe status of the user on this client. Will be either"idle"or"active".timestamp:integerThe UNIX timestamp of when this client sent the user's presence
to the server with the precision of a second.pushable:booleanWhether the client is capable of showing mobile/push notifications
to the user.Not present in objects with the"aggregated"key.Changes: Starting with Zulip 7.0 (feature level 178), alwaysfalsewhen present as the server no longer stores which client
submitted presence data.

```
last_update_id
```
- Will be one of these two formats (modern or legacy) for user
    presence data:{user_id}:objectPresence data (modern format) for the user with
the specified ID.active_timestamp:integerThe UNIX timestamp of the last time a client connected
to Zulip reported that the user was actually present
(e.g. via focusing a browser window or interacting
with a computer running the desktop app).Clients should display users with a currentactive_timestampas fully present.idle_timestamp:integerThe UNIX timestamp of the last time the user had a
client connected to Zulip, including idle clients
where the user hasn't interacted with the system
recently.The Zulip server has no way of distinguishing whether
an idle web app user is at their computer, but hasn't
interacted with the Zulip tab recently, or simply left
their desktop computer on when they left.Thus, clients should display users with a currentidle_timestampbut no currentactive_timestampas
potentially present.{user_email}:objectPresence data (legacy format) for the user with
the specified Zulip API email.{client_name}or"aggregated":objectObject containing the details of the user's
presence.Changes: Starting with Zulip 7.0 (feature level 178), this will always
contain two keys,"website"and"aggregated", with identical data. The
server no longer stores which client submitted presence updates.Previously, the{client_name}keys for these objects were the names of the
different clients where the user was logged in, for examplewebsiteorZulipDesktop.client:stringThe client's platform name.Changes: Starting with Zulip 7.0 (feature level 178), this will
always be"website"as the server no longer stores which client
submitted presence data.status:stringThe status of the user on this client. Will be either"idle"or"active".timestamp:integerThe UNIX timestamp of when this client sent the user's presence
to the server with the precision of a second.pushable:booleanWhether the client is capable of showing mobile/push notifications
to the user.Not present in objects with the"aggregated"key.Changes: Starting with Zulip 7.0 (feature level 178), alwaysfalsewhen present as the server no longer stores which client
submitted presence data.
- {user_id}:objectPresence data (modern format) for the user with
the specified ID.active_timestamp:integerThe UNIX timestamp of the last time a client connected
to Zulip reported that the user was actually present
(e.g. via focusing a browser window or interacting
with a computer running the desktop app).Clients should display users with a currentactive_timestampas fully present.idle_timestamp:integerThe UNIX timestamp of the last time the user had a
client connected to Zulip, including idle clients
where the user hasn't interacted with the system
recently.The Zulip server has no way of distinguishing whether
an idle web app user is at their computer, but hasn't
interacted with the Zulip tab recently, or simply left
their desktop computer on when they left.Thus, clients should display users with a currentidle_timestampbut no currentactive_timestampas
potentially present.
- {user_email}:objectPresence data (legacy format) for the user with
the specified Zulip API email.{client_name}or"aggregated":objectObject containing the details of the user's
presence.Changes: Starting with Zulip 7.0 (feature level 178), this will always
contain two keys,"website"and"aggregated", with identical data. The
server no longer stores which client submitted presence updates.Previously, the{client_name}keys for these objects were the names of the
different clients where the user was logged in, for examplewebsiteorZulipDesktop.client:stringThe client's platform name.Changes: Starting with Zulip 7.0 (feature level 178), this will
always be"website"as the server no longer stores which client
submitted presence data.status:stringThe status of the user on this client. Will be either"idle"or"active".timestamp:integerThe UNIX timestamp of when this client sent the user's presence
to the server with the precision of a second.pushable:booleanWhether the client is capable of showing mobile/push notifications
to the user.Not present in objects with the"aggregated"key.Changes: Starting with Zulip 7.0 (feature level 178), alwaysfalsewhen present as the server no longer stores which client
submitted presence data.
- active_timestamp:integerThe UNIX timestamp of the last time a client connected
to Zulip reported that the user was actually present
(e.g. via focusing a browser window or interacting
with a computer running the desktop app).Clients should display users with a currentactive_timestampas fully present.
- idle_timestamp:integerThe UNIX timestamp of the last time the user had a
client connected to Zulip, including idle clients
where the user hasn't interacted with the system
recently.The Zulip server has no way of distinguishing whether
an idle web app user is at their computer, but hasn't
interacted with the Zulip tab recently, or simply left
their desktop computer on when they left.Thus, clients should display users with a currentidle_timestampbut no currentactive_timestampas
potentially present.
- {client_name}or"aggregated":objectObject containing the details of the user's
presence.Changes: Starting with Zulip 7.0 (feature level 178), this will always
contain two keys,"website"and"aggregated", with identical data. The
server no longer stores which client submitted presence updates.Previously, the{client_name}keys for these objects were the names of the
different clients where the user was logged in, for examplewebsiteorZulipDesktop.client:stringThe client's platform name.Changes: Starting with Zulip 7.0 (feature level 178), this will
always be"website"as the server no longer stores which client
submitted presence data.status:stringThe status of the user on this client. Will be either"idle"or"active".timestamp:integerThe UNIX timestamp of when this client sent the user's presence
to the server with the precision of a second.pushable:booleanWhether the client is capable of showing mobile/push notifications
to the user.Not present in objects with the"aggregated"key.Changes: Starting with Zulip 7.0 (feature level 178), alwaysfalsewhen present as the server no longer stores which client
submitted presence data.
- client:stringThe client's platform name.Changes: Starting with Zulip 7.0 (feature level 178), this will
always be"website"as the server no longer stores which client
submitted presence data.
- status:stringThe status of the user on this client. Will be either"idle"or"active".
- timestamp:integerThe UNIX timestamp of when this client sent the user's presence
to the server with the precision of a second.
- pushable:booleanWhether the client is capable of showing mobile/push notifications
to the user.Not present in objects with the"aggregated"key.Changes: Starting with Zulip 7.0 (feature level 178), alwaysfalsewhen present as the server no longer stores which client
submitted presence data.

#### Example response(s)
Modern presence format:

```
{"msg":"","presence_last_update_id":1000,"presences":{"10":{"active_timestamp":1656958520,"idle_timestamp":1656958530}},"result":"success","server_timestamp":1656958539.6287155}
```

```
{"msg":"","presence_last_update_id":1000,"presences":{"10":{"active_timestamp":1656958520,"idle_timestamp":1656958530}},"result":"success","server_timestamp":1656958539.6287155}
```
Legacy presence format:

```
{"msg":"","presence_last_update_id":1000,"presences":{"user@example.com":{"aggregated":{"client":"website","status":"idle","timestamp":1594825445},"website":{"client":"website","pushable":false,"status":"idle","timestamp":1594825445}}},"result":"success","server_timestamp":1656958539.6287155}
```

```
{"msg":"","presence_last_update_id":1000,"presences":{"user@example.com":{"aggregated":{"client":"website","status":"idle","timestamp":1594825445},"website":{"client":"website","pushable":false,"status":"idle","timestamp":1594825445}}},"result":"success","server_timestamp":1656958539.6287155}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.