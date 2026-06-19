# Construct a filter_spec | Zulip API documentation

*Source: https://zulip.com/api/construct-filter_spec*

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

# Construct a filter_spec
Anarrowis a set of filters for Zulip messages, that can be based
on many different factors (like sender, channel, message_topic, search
keywords, etc.). Narrows are used in various places in the Zulip
API (most importantly, in the API for fetching messages).
It is simplest to explain the algorithm for encoding a search as a
filter_spec using a single example. Consider the following search query
(written as it would be entered in the Zulip web app's search box).
It filters for messages sent to channelannounce, not sent byiago@zulip.com, and containing the wordscoolandsunglasses:

```
channel:announce -sender:iago@zulip.com cool sunglasses
```

```
channel:announce -sender:iago@zulip.com cool sunglasses
```
This query would be JSON-encoded for use in the Zulip API using JSON
as a list of simple objects, as follows:

```
[{"operator":"channel","operand":"announce"},{"operator":"sender","operand":"iago@zulip.com","negated":true},{"operator":"search","operand":"cool sunglasses"}]
```

```
[{"operator":"channel","operand":"announce"},{"operator":"sender","operand":"iago@zulip.com","negated":true},{"operator":"search","operand":"cool sunglasses"}]
```
The Zulip help center article onsearching for messagesdocuments the majority of the search/filter_spec options supported by the
Zulip API.
Note that many narrows, including all that lack achannelorchannelsoperator, search the current user's personal message history. Seesearching shared historyfor details.
Clients should note that theis:unreadfilter takes advantage of the
fact that there is a database index for unread messages, which can be an
important optimization when fetching messages in certain cases (e.g.,
whenadding thereadflag to a user's personal
messages).
Note: When the value ofrealm_empty_topic_display_namefound in
thePOST /registerresponse is used as an operand
for the"message_topic"operator in the filter_spec, it is interpreted
as an empty string.

## Changes
- In Zulip 12.0 (feature level 446), add thementionsoperator,
  matching messages that contain a direct personal mention of the
  specified user.
- In Zulip 10.0 (feature level 366), support was added for a newis:mutedoperator combination, matching messages in topics and
  channels that the user hasmuted.
- Before Zulip 10.0 (feature level 334), empty string was not a valid
  message_topic name for channel messages.
- In Zulip 9.0 (feature level 271), support was added for a new filter
  operator,with, which uses amessage IDfor its
  operand, and is designed for creating permanent links to topics.
- In Zulip 9.0 (feature level 265), support was added for a newis:followedfilter, matching messages in topics that the current
  user isfollowing.
- In Zulip 9.0 (feature level 250), support was added for two filters
  related to channel_name messages:channelandchannels. Thechanneloperator is an alias for thestreamoperator. Thechannelsoperator is an alias for thestreamsoperator. Bothchannelandchannelsreturn the same exact results asstreamandstreamsrespectively.
- In Zulip 9.0 (feature level 249), support was added for a new filter,has:reaction, which returns messages that have at least oneemoji
  reaction.
- In Zulip 7.0 (feature level 177), support was added for three filters
  related to direct messages:is:dm,dmanddm-including. Thedmoperator replaced and deprecated thepm-withoperator. Theis:dmfilter replaced and deprecated theis:privatefilter. Thedm-includingoperator replaced and deprecated thegroup-pm-withoperator.Thedm-includingandgroup-pm-withoperators return slightly
  different results. For example,dm-including:1234returns all
  direct messages (1-on-1 and group) that include the current user
  and the user with the unique user ID of1234. On the other hand,group-pm-with:1234returned only group direct messages that
  included the current user and the user with the unique user ID of1234.Bothdmandis:dmare aliases ofpm-withandis:privaterespectively, and return the same exact results that the
  deprecated filters did.
- Thedm-includingandgroup-pm-withoperators return slightly
  different results. For example,dm-including:1234returns all
  direct messages (1-on-1 and group) that include the current user
  and the user with the unique user ID of1234. On the other hand,group-pm-with:1234returned only group direct messages that
  included the current user and the user with the unique user ID of1234.
- Bothdmandis:dmare aliases ofpm-withandis:privaterespectively, and return the same exact results that the
  deprecated filters did.

## Narrows that use IDs

### Message IDs
Theidandwithoperators use message IDs for their operands. The
message ID operand for these two operators may be encoded as either a
number or a string.
- id:12345: Search for only the message with ID12345.
- with:12345: Search for the conversation that contains the message
  with ID12345.
Theidoperator returns the message with the specified ID if it exists,
and if it can be accessed by the user.
Thewithoperator is designed to be used for permanent links to
topics, which means they should continue to work when the message_topic ismovedorresolved. If the message with the specified
ID exists, and can be accessed by the user, then it will return
messages with thechannel/message_topic/dmoperators corresponding to
the current conversation containing that message, replacing any such
operators included in the original filter_spec query.
If no such message exists, or the message ID represents a message that
is inaccessible to the user, this operator will be ignored (rather
than throwing an error) if the remaining operators uniquely identify a
conversation (i.e., they containchannelandtopicterms ordmterm). This behavior is intended to provide the best possible
experience for links to private channels with protected history.
Thehelp centeralso
documents thenearoperator for searching for messages by ID, but
this filter_spec operator has no effect on filtering messages when sent to
the server. In practice, when thenearoperator is used to search for
messages, or is part of a URL fragment, the value of its operand should
instead be used for the value of theanchorparameter in endpoints
that also accept anarrowparameter; seeGET /messagesandPOST /messages/flags/filter_spec.
Changes: Prior to Zulip 8.0 (feature level 194), the message ID
operand for theidoperator needed to be encoded as a string.

```
[{"operator":"id","operand":12345}]
```

```
[{"operator":"id","operand":12345}]
```

### Channel and user IDs
There are a few additional filter_spec/search options (new in Zulip 2.1)
that use either channel IDs or user IDs that are not documented in the
help center because they are primarily useful to API clients:
- channel:1234: Search messages sent to the channel with ID1234.
- sender:1234: Search messages sent by user ID1234.
- dm:1234: Search the direct message conversation between
  you and user ID1234.
- dm:1234,5678: Search the direct message conversation between
  you, user ID1234, and user ID5678.
- dm-including:1234: Search all direct messages (1-on-1 and group)
  that include you and user ID1234.
A user ID can be found byviewing a user's profilein the web or desktop apps. A channel ID can be found whenbrowsing
channelsin the web or desktop apps.
The operands for these search options must be encoded either as an
integer ID or a JSON list of integer IDs. For example, to query
messages sent by a user 1234 to a direct message thread with yourself,
user 1234, and user 5678, the correct JSON-encoded query is:

```
[{"operator":"dm","operand":[1234,5678]},{"operator":"sender","operand":1234}]
```

```
[{"operator":"dm","operand":[1234,5678]},{"operator":"sender","operand":1234}]
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.