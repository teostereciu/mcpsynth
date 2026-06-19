# Unsubscribe from a channel | Zulip API documentation

*Source: https://zulip.com/api/unsubscribe*

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

# Unsubscribe from a channel
DELETE https://your-org.zulipchat.com/api/v1/users/me/subscriptions
Unsubscribe yourself or other users from one or more channels.
In addition to managing the current user's subscriptions, this
endpoint can be used to remove other users from channels. This
is possible in 3 situations:
- Organization administrators can remove any user from any
  channel.
- Users can remove a bot that they own from any channel that
  the usercan access.
- Users can unsubscribe any user from a channel if theyhave
  accessto the channel and are a
  member of theuser groupspecified
  by thecan_remove_subscribers_groupfor the channel.

```
can_remove_subscribers_group
```
Changes: Before Zulip 10.0 (feature level 362),
subscriptions in archived channels could not be modified.
Before Zulip 8.0 (feature level 208), if a user specified by
theprincipalsparameter was a
deactivated user, or did not exist, then an HTTP status code
of 403 was returned withcode: "UNAUTHORIZED_PRINCIPAL"in
the error response. As of this feature level, an HTTP status
code of 400 is returned withcode: "BAD_REQUEST"in the
error response for these cases.
Before Zulip 8.0 (feature level 197),
thecan_remove_subscribers_groupsetting
was namedcan_remove_subscribers_group_id.
Before Zulip 7.0 (feature level 161), thecan_remove_subscribers_group_idfor all channels was always
the system group for organization administrators.
Before Zulip 6.0 (feature level 145), users had no special
privileges for managing bots that they own.

## Usage examples
PythonJavaScriptcurl
- Python
- JavaScript
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Unsubscribe from channel "python-test".result=client.remove_subscriptions(["python-test"],)# Unsubscribe another user from channel "python-test".result=client.remove_subscriptions(["python-test"],principals=["newbie@zulip.com"],)print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Unsubscribe from channel "python-test".result=client.remove_subscriptions(["python-test"],)# Unsubscribe another user from channel "python-test".result=client.remove_subscriptions(["python-test"],principals=["newbie@zulip.com"],)print(result)
```
More examples and documentation can be foundhere.

```
constzulipInit=require("zulip-js");// Pass the path to your zuliprc file here.constconfig={zuliprc:"zuliprc"};(async()=>{constclient=awaitzulipInit(config);// Unsubscribe from the channel "Denmark"constmeParams={subscriptions:JSON.stringify(["Denmark"]),};console.log(awaitclient.users.me.subscriptions.remove(meParams));constuser_id=7;// Unsubscribe Zoe from the channel "Denmark"constzoeParams={subscriptions:JSON.stringify(["Denmark"]),principals:JSON.stringify([user_id]),};console.log(awaitclient.users.me.subscriptions.remove(zoeParams));})();
```

```
constzulipInit=require("zulip-js");// Pass the path to your zuliprc file here.constconfig={zuliprc:"zuliprc"};(async()=>{constclient=awaitzulipInit(config);// Unsubscribe from the channel "Denmark"constmeParams={subscriptions:JSON.stringify(["Denmark"]),};console.log(awaitclient.users.me.subscriptions.remove(meParams));constuser_id=7;// Unsubscribe Zoe from the channel "Denmark"constzoeParams={subscriptions:JSON.stringify(["Denmark"]),principals:JSON.stringify([user_id]),};console.log(awaitclient.users.me.subscriptions.remove(zoeParams));})();
```
Note: Unsubscribing another user from a channel requires
administrative privileges.
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX DELETE https://your-org.zulipchat.com/api/v1/users/me/subscriptions \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'subscriptions=["Verona", "Denmark"]'
```

```
curl -sSX DELETE https://your-org.zulipchat.com/api/v1/users/me/subscriptions \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'subscriptions=["Verona", "Denmark"]'
```
You may specify theprincipalsparameter like so:
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX DELETE https://your-org.zulipchat.com/api/v1/users/me/subscriptions \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'subscriptions=["Verona", "Denmark"]' \
    --data-urlencode 'principals=["ZOE@zulip.com"]'
```

```
curl -sSX DELETE https://your-org.zulipchat.com/api/v1/users/me/subscriptions \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode 'subscriptions=["Verona", "Denmark"]' \
    --data-urlencode 'principals=["ZOE@zulip.com"]'
```

## Parameters
subscriptions(string)[]required

```
["Verona", "Denmark"]
```
A list of channel names to unsubscribe from. This parameter is calledstreamsin our Python API.
principals(string)[] | (integer)[]optional

```
["ZOE@zulip.com"]
```
A list of user IDs (preferred) or Zulip API email
addresses of the users to be subscribed to or unsubscribed
from the channels specified in thesubscriptionsparameter. If
not provided, then the requesting user/bot is subscribed.
Changes: The integer format is new in Zulip 3.0 (feature level 9).

## Response

#### Return values
- not_removed:(string)[]A list of the names of channels that the user is already unsubscribed
from, and hence doesn't need to be unsubscribed.
- removed:(string)[]A list of the names of channels which were unsubscribed from as a result
of the query.

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"msg":"","not_removed":[],"removed":["testing-help"],"result":"success"}
```

```
{"msg":"","not_removed":[],"removed":["testing-help"],"result":"success"}
```
A typical failed JSON response for when the target channel does not exist:

```
{"code":"STREAM_DOES_NOT_EXIST","msg":"Channel 'nonexistent' does not exist","result":"error","channel_name":"nonexistent"}
```

```
{"code":"STREAM_DOES_NOT_EXIST","msg":"Channel 'nonexistent' does not exist","result":"error","channel_name":"nonexistent"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.