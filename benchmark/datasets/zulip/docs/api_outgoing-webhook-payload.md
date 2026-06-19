# Outgoing webhook payloads | Zulip API documentation

*Source: https://zulip.com/api/outgoing-webhook-payload*

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

# Outgoing webhook payloads
Zulip supportsoutgoing webhooksin a clean,
nativeZulip format, as well as in aSlack-compatible
format.

## Zulip format
This is an example of the JSON payload that the Zulip server willPOSTto your server:

```
{"bot_email":"outgoing-bot@localhost","bot_full_name":"Outgoing webhook test","data":"@**Outgoing webhook test** Zulip is the world\u2019s most productive group chat!","message":{"avatar_url":"https://secure.gravatar.com/avatar/1f4f1575bf002ae562fea8fc4b861b09?d=identicon&version=1","client":"website","content":"@**Outgoing webhook test** Zulip is the world\u2019s most productive group chat!","display_recipient":"Verona","id":112,"is_me_message":false,"reactions":[],"recipient_id":20,"rendered_content":"<p><span class=\"user-mention\" data-user-id=\"25\">@Outgoing webhook test</span> Zulip is the world\u2019s most productive group chat!</p>","sender_email":"iago@zulip.com","sender_full_name":"Iago","sender_id":5,"sender_realm_str":"zulip","stream_id":5,"subject":"Verona2","submessages":[],"timestamp":1527876931,"topic_links":[],"type":"stream"},"token":"xvOzfurIutdRRVLzpXrIIHXJvNfaJLJ0","trigger":"mention"}
```

```
{"bot_email":"outgoing-bot@localhost","bot_full_name":"Outgoing webhook test","data":"@**Outgoing webhook test** Zulip is the world\u2019s most productive group chat!","message":{"avatar_url":"https://secure.gravatar.com/avatar/1f4f1575bf002ae562fea8fc4b861b09?d=identicon&version=1","client":"website","content":"@**Outgoing webhook test** Zulip is the world\u2019s most productive group chat!","display_recipient":"Verona","id":112,"is_me_message":false,"reactions":[],"recipient_id":20,"rendered_content":"<p><span class=\"user-mention\" data-user-id=\"25\">@Outgoing webhook test</span> Zulip is the world\u2019s most productive group chat!</p>","sender_email":"iago@zulip.com","sender_full_name":"Iago","sender_id":5,"sender_realm_str":"zulip","stream_id":5,"subject":"Verona2","submessages":[],"timestamp":1527876931,"topic_links":[],"type":"stream"},"token":"xvOzfurIutdRRVLzpXrIIHXJvNfaJLJ0","trigger":"mention"}
```

### Fields documentation

#### Return values
- bot_email:stringEmail of the bot user.
- bot_full_name:stringThe full name of the bot user.
- data:stringThe message content, in rawZulip-flavored Markdownformat (not rendered to HTML).
- trigger:stringWhat aspect of the message triggered the outgoing webhook notification.
Possible values includedirect_messageandmention.Changes: In Zulip 8.0 (feature level 201), renamed the triggerprivate_messagetodirect_message.
- token:stringA string of alphanumeric characters that can be used to authenticate the
webhook request (each bot user uses a fixed token). You can get the token used by a given outgoing webhook bot
in thezuliprcfile downloaded when creating the bot.
- message:objectA dictionary containing details on the message that triggered the
outgoing webhook, in the format used byGET /messages.avatar_url:string | nullThe URL of the message sender's avatar. Can benullonly if
the current user has access to the sender's real email address
andclient_gravatarwastrue.Ifnull, then the sender has not uploaded an avatar in Zulip,
and the client can compute the gravatar URL by hashing the
sender's email address, which corresponds in this case to their
real email address.Changes: Before Zulip 7.0 (feature level 163), access to a
user's real email address was a realm-level setting. As of this
feature level,email_address_visibilityis a user setting.client:stringA Zulip "client" string, describing what Zulip client
sent the message.content:stringThe content/body of the message.
Whenapply_markdownis set, it will be in HTML format.SeeMarkdown message formattingfor details on Zulip's HTML format.content_type:stringThe HTTPcontent_typefor the message content. This
will betext/htmlortext/x-markdown, depending on
whetherapply_markdownwas set.See the help center article onmessage formattingfor details on Zulip-flavored Markdown.display_recipient:string | (object)[]Data on the recipient of the message;
either the name of a channel or a dictionary containing basic data on
the users who received the message.id:integerID of the user.email:stringZulip API email of the user.full_name:stringFull name of the user.is_mirror_dummy:booleanWhether the user is a mirror dummy.edit_history:(object)[]An array of objects, with each object documenting the
changes in a previous edit made to the message,
ordered chronologically from most recent to least recent
edit.Not present if the message has never been edited or moved,
or ifviewing message edit historyis not allowed in the organization.Every object will containuser_idandtimestamp.The other fields are optional, and will be present or not
depending on whether the channel, topic, and/or message
content were modified in the edit event. For example, if
only the topic was edited, onlyprev_topicandtopicwill be present in addition touser_idandtimestamp.Changes: In Zulip 10.0 (feature level 284), removed theprev_rendered_content_versionfield as it is an internal
server implementation detail not used by any client.prev_content:stringOnly present if message's content was edited.The content of the message immediately prior to this
edit event.prev_rendered_content:stringOnly present if message's content was edited.The rendered HTML representation ofprev_content.SeeMarkdown message formattingfor details on Zulip's HTML format.prev_stream:integerOnly present if message's channel was edited.The channel ID of the message immediately prior to this
edit event.Changes: New in Zulip 3.0 (feature level 1).prev_topic:stringOnly present if message's topic was edited.The topic of the message immediately prior to this
edit event.Changes: New in Zulip 5.0 (feature level 118).
Previously, this field was calledprev_subject;
clients are recommended to renameprev_subjecttoprev_topicif present for compatibility with
older Zulip servers.stream:integerOnly present if message's channel was edited.The ID of the channel containing the message
immediately after this edit event.Changes: New in Zulip 5.0 (feature level 118).timestamp:integerThe UNIX timestamp for the edit.topic:stringOnly present if message's topic was edited.The topic of the message immediately after this edit event.Changes: New in Zulip 5.0 (feature level 118).user_id:integer | nullThe ID of the user that made the edit.Will benullonly for edit history
events predating March 2017.Clients can display edit history events where this
isnullas modified by either the sender (for content
edits) or an unknown user (for topic edits).id:integerThe unique message ID. Messages should always be
displayed sorted by ID.is_me_message:booleanWhether the message is a/me status messagelast_edit_timestamp:integerThe UNIX timestamp for when the message's content was last edited, in
UTC seconds.Not present if the message's content has never been edited.Clients should use this field, rather than parsing theedit_historyarray, to display an indicator that the message has been edited.Changes: Prior to Zulip 10.0 (feature level 365), this was the
time when the message was last edited or moved.last_moved_timestamp:integerThe UNIX timestamp for when the message was last moved to a different
channel or topic, in UTC seconds.Not present if the message has never been moved, or if the only topic
moves for the message areresolving or unresolvingthe message's topic.Clients should use this field, rather than parsing theedit_historyarray, to display an indicator that the message has been moved.Changes: New in Zulip 10.0 (feature level 365). Previously,
parsing theedit_historyarray was required in order to correctly
display moved message indicators.reactions:(object)[]Data on anyreactionsto the message,
ordered chronologically from oldest to newest reaction.Changes: In Zulip 10.0 (feature level 328), the deprecateduserobject was removed from the data for each reaction. It contained the
following information about the user who added the reaction:id,email,full_nameandis_mirror_dummy.emoji_name:stringName of the emoji.emoji_code:stringA unique identifier, defining the specific emoji codepoint requested,
within the namespace of thereaction_type.reaction_type:stringA string indicating the type of emoji. Each emojireaction_typehas an independent namespace for values ofemoji_code.Must be one of the following values:unicode_emoji: In this namespace,emoji_codewill be a
  dash-separated hex encoding of the sequence of Unicode codepoints
  that define this emoji in the Unicode specification.realm_emoji: In this namespace,emoji_codewill be the ID of
  the uploadedcustom emoji.zulip_extra_emoji: These are special emoji included with Zulip.
  In this namespace,emoji_codewill be the name of the emoji (e.g.
  "zulip").user_id:integerThe ID of the user who added the reaction.Changes: New in Zulip 3.0 (feature level 2), which
deprecated theuserobject.recipient_id:integerA unique ID for the set of users receiving the
message (either a channel or group of users). Useful primarily
for hashing.Changes: Before Zulip 10.0 (feature level 327),recipient_idwas the same across all incoming 1:1 direct messages. Now, each
incoming message uniquely shares arecipient_idwith outgoing
messages in the same conversation.sender_email:stringThe Zulip API email address of the message's sender.sender_full_name:stringThe full name of the message's sender.sender_id:integerThe user ID of the message's sender.sender_realm_str:stringA string identifier for the realm the sender is in. Unique only within
the context of a given Zulip server.E.g. onexample.zulip.com, this will beexample.stream_id:integerOnly present for channel messages; the ID of the channel.subject:stringThetopicof the message. Currently always""for direct messages,
though this could change if Zulip adds support for topics in direct
message conversations.The field name is a legacy holdover from when topics were
called "subjects" and will eventually change.For clients that don't support theempty_topic_nameclient capability,
the empty string value is replaced with the value ofrealm_empty_topic_display_namefound in thePOST /registerresponse, for channel messages.Changes: Before Zulip 10.0 (feature level 334),empty_topic_nameclient capability didn't exist and empty string as the topic name for
channel messages wasn't allowed.submessages:(object)[]Data used for certain experimental Zulip integrations.msg_type:stringThe type of the message.content:stringThe new content of the submessage.message_id:integerThe ID of the message to which the submessage has been added.sender_id:integerThe ID of the user who sent the message.id:integerThe ID of the submessage.timestamp:integerThe UNIX timestamp for when the message was sent,
in UTC seconds.topic_links:(object)[]Data on any links to be included in thetopicline (these are generated bycustom linkification
filtersthat match content in the
message's topic.)Changes: This field contained a list of urls before
Zulip 4.0 (feature level 46).New in Zulip 3.0 (feature level 1). Previously, this field was calledsubject_links; clients are recommended to renamesubject_linkstotopic_linksif present for compatibility with older Zulip servers.text:stringThe original link text present in the topic.url:stringThe expanded target url which the link points to.type:stringThe type of the message:"stream"or"private".rendered_content:stringThe content/body of the message rendered in HTML.SeeMarkdown message formattingfor details on Zulip's HTML format.

```
GET /messages
```
- avatar_url:string | nullThe URL of the message sender's avatar. Can benullonly if
the current user has access to the sender's real email address
andclient_gravatarwastrue.Ifnull, then the sender has not uploaded an avatar in Zulip,
and the client can compute the gravatar URL by hashing the
sender's email address, which corresponds in this case to their
real email address.Changes: Before Zulip 7.0 (feature level 163), access to a
user's real email address was a realm-level setting. As of this
feature level,email_address_visibilityis a user setting.
- client:stringA Zulip "client" string, describing what Zulip client
sent the message.
- content:stringThe content/body of the message.
Whenapply_markdownis set, it will be in HTML format.SeeMarkdown message formattingfor details on Zulip's HTML format.
- content_type:stringThe HTTPcontent_typefor the message content. This
will betext/htmlortext/x-markdown, depending on
whetherapply_markdownwas set.See the help center article onmessage formattingfor details on Zulip-flavored Markdown.
- display_recipient:string | (object)[]Data on the recipient of the message;
either the name of a channel or a dictionary containing basic data on
the users who received the message.id:integerID of the user.email:stringZulip API email of the user.full_name:stringFull name of the user.is_mirror_dummy:booleanWhether the user is a mirror dummy.
- edit_history:(object)[]An array of objects, with each object documenting the
changes in a previous edit made to the message,
ordered chronologically from most recent to least recent
edit.Not present if the message has never been edited or moved,
or ifviewing message edit historyis not allowed in the organization.Every object will containuser_idandtimestamp.The other fields are optional, and will be present or not
depending on whether the channel, topic, and/or message
content were modified in the edit event. For example, if
only the topic was edited, onlyprev_topicandtopicwill be present in addition touser_idandtimestamp.Changes: In Zulip 10.0 (feature level 284), removed theprev_rendered_content_versionfield as it is an internal
server implementation detail not used by any client.prev_content:stringOnly present if message's content was edited.The content of the message immediately prior to this
edit event.prev_rendered_content:stringOnly present if message's content was edited.The rendered HTML representation ofprev_content.SeeMarkdown message formattingfor details on Zulip's HTML format.prev_stream:integerOnly present if message's channel was edited.The channel ID of the message immediately prior to this
edit event.Changes: New in Zulip 3.0 (feature level 1).prev_topic:stringOnly present if message's topic was edited.The topic of the message immediately prior to this
edit event.Changes: New in Zulip 5.0 (feature level 118).
Previously, this field was calledprev_subject;
clients are recommended to renameprev_subjecttoprev_topicif present for compatibility with
older Zulip servers.stream:integerOnly present if message's channel was edited.The ID of the channel containing the message
immediately after this edit event.Changes: New in Zulip 5.0 (feature level 118).timestamp:integerThe UNIX timestamp for the edit.topic:stringOnly present if message's topic was edited.The topic of the message immediately after this edit event.Changes: New in Zulip 5.0 (feature level 118).user_id:integer | nullThe ID of the user that made the edit.Will benullonly for edit history
events predating March 2017.Clients can display edit history events where this
isnullas modified by either the sender (for content
edits) or an unknown user (for topic edits).
- id:integerThe unique message ID. Messages should always be
displayed sorted by ID.
- is_me_message:booleanWhether the message is a/me status message
- last_edit_timestamp:integerThe UNIX timestamp for when the message's content was last edited, in
UTC seconds.Not present if the message's content has never been edited.Clients should use this field, rather than parsing theedit_historyarray, to display an indicator that the message has been edited.Changes: Prior to Zulip 10.0 (feature level 365), this was the
time when the message was last edited or moved.
- last_moved_timestamp:integerThe UNIX timestamp for when the message was last moved to a different
channel or topic, in UTC seconds.Not present if the message has never been moved, or if the only topic
moves for the message areresolving or unresolvingthe message's topic.Clients should use this field, rather than parsing theedit_historyarray, to display an indicator that the message has been moved.Changes: New in Zulip 10.0 (feature level 365). Previously,
parsing theedit_historyarray was required in order to correctly
display moved message indicators.
- reactions:(object)[]Data on anyreactionsto the message,
ordered chronologically from oldest to newest reaction.Changes: In Zulip 10.0 (feature level 328), the deprecateduserobject was removed from the data for each reaction. It contained the
following information about the user who added the reaction:id,email,full_nameandis_mirror_dummy.emoji_name:stringName of the emoji.emoji_code:stringA unique identifier, defining the specific emoji codepoint requested,
within the namespace of thereaction_type.reaction_type:stringA string indicating the type of emoji. Each emojireaction_typehas an independent namespace for values ofemoji_code.Must be one of the following values:unicode_emoji: In this namespace,emoji_codewill be a
  dash-separated hex encoding of the sequence of Unicode codepoints
  that define this emoji in the Unicode specification.realm_emoji: In this namespace,emoji_codewill be the ID of
  the uploadedcustom emoji.zulip_extra_emoji: These are special emoji included with Zulip.
  In this namespace,emoji_codewill be the name of the emoji (e.g.
  "zulip").user_id:integerThe ID of the user who added the reaction.Changes: New in Zulip 3.0 (feature level 2), which
deprecated theuserobject.
- recipient_id:integerA unique ID for the set of users receiving the
message (either a channel or group of users). Useful primarily
for hashing.Changes: Before Zulip 10.0 (feature level 327),recipient_idwas the same across all incoming 1:1 direct messages. Now, each
incoming message uniquely shares arecipient_idwith outgoing
messages in the same conversation.
- sender_email:stringThe Zulip API email address of the message's sender.
- sender_full_name:stringThe full name of the message's sender.
- sender_id:integerThe user ID of the message's sender.
- sender_realm_str:stringA string identifier for the realm the sender is in. Unique only within
the context of a given Zulip server.E.g. onexample.zulip.com, this will beexample.
- stream_id:integerOnly present for channel messages; the ID of the channel.
- subject:stringThetopicof the message. Currently always""for direct messages,
though this could change if Zulip adds support for topics in direct
message conversations.The field name is a legacy holdover from when topics were
called "subjects" and will eventually change.For clients that don't support theempty_topic_nameclient capability,
the empty string value is replaced with the value ofrealm_empty_topic_display_namefound in thePOST /registerresponse, for channel messages.Changes: Before Zulip 10.0 (feature level 334),empty_topic_nameclient capability didn't exist and empty string as the topic name for
channel messages wasn't allowed.
- submessages:(object)[]Data used for certain experimental Zulip integrations.msg_type:stringThe type of the message.content:stringThe new content of the submessage.message_id:integerThe ID of the message to which the submessage has been added.sender_id:integerThe ID of the user who sent the message.id:integerThe ID of the submessage.
- timestamp:integerThe UNIX timestamp for when the message was sent,
in UTC seconds.
- topic_links:(object)[]Data on any links to be included in thetopicline (these are generated bycustom linkification
filtersthat match content in the
message's topic.)Changes: This field contained a list of urls before
Zulip 4.0 (feature level 46).New in Zulip 3.0 (feature level 1). Previously, this field was calledsubject_links; clients are recommended to renamesubject_linkstotopic_linksif present for compatibility with older Zulip servers.text:stringThe original link text present in the topic.url:stringThe expanded target url which the link points to.
- type:stringThe type of the message:"stream"or"private".
- rendered_content:stringThe content/body of the message rendered in HTML.SeeMarkdown message formattingfor details on Zulip's HTML format.
- id:integerID of the user.
- email:stringZulip API email of the user.
- full_name:stringFull name of the user.
- is_mirror_dummy:booleanWhether the user is a mirror dummy.
- prev_content:stringOnly present if message's content was edited.The content of the message immediately prior to this
edit event.
- prev_rendered_content:stringOnly present if message's content was edited.The rendered HTML representation ofprev_content.SeeMarkdown message formattingfor details on Zulip's HTML format.
- prev_stream:integerOnly present if message's channel was edited.The channel ID of the message immediately prior to this
edit event.Changes: New in Zulip 3.0 (feature level 1).
- prev_topic:stringOnly present if message's topic was edited.The topic of the message immediately prior to this
edit event.Changes: New in Zulip 5.0 (feature level 118).
Previously, this field was calledprev_subject;
clients are recommended to renameprev_subjecttoprev_topicif present for compatibility with
older Zulip servers.
- stream:integerOnly present if message's channel was edited.The ID of the channel containing the message
immediately after this edit event.Changes: New in Zulip 5.0 (feature level 118).
- timestamp:integerThe UNIX timestamp for the edit.
- topic:stringOnly present if message's topic was edited.The topic of the message immediately after this edit event.Changes: New in Zulip 5.0 (feature level 118).
- user_id:integer | nullThe ID of the user that made the edit.Will benullonly for edit history
events predating March 2017.Clients can display edit history events where this
isnullas modified by either the sender (for content
edits) or an unknown user (for topic edits).
- emoji_name:stringName of the emoji.
- emoji_code:stringA unique identifier, defining the specific emoji codepoint requested,
within the namespace of thereaction_type.
- reaction_type:stringA string indicating the type of emoji. Each emojireaction_typehas an independent namespace for values ofemoji_code.Must be one of the following values:unicode_emoji: In this namespace,emoji_codewill be a
  dash-separated hex encoding of the sequence of Unicode codepoints
  that define this emoji in the Unicode specification.realm_emoji: In this namespace,emoji_codewill be the ID of
  the uploadedcustom emoji.zulip_extra_emoji: These are special emoji included with Zulip.
  In this namespace,emoji_codewill be the name of the emoji (e.g.
  "zulip").
- user_id:integerThe ID of the user who added the reaction.Changes: New in Zulip 3.0 (feature level 2), which
deprecated theuserobject.
- unicode_emoji: In this namespace,emoji_codewill be a
  dash-separated hex encoding of the sequence of Unicode codepoints
  that define this emoji in the Unicode specification.
- realm_emoji: In this namespace,emoji_codewill be the ID of
  the uploadedcustom emoji.
- zulip_extra_emoji: These are special emoji included with Zulip.
  In this namespace,emoji_codewill be the name of the emoji (e.g.
  "zulip").
- msg_type:stringThe type of the message.
- content:stringThe new content of the submessage.
- message_id:integerThe ID of the message to which the submessage has been added.
- sender_id:integerThe ID of the user who sent the message.
- id:integerThe ID of the submessage.
- text:stringThe original link text present in the topic.
- url:stringThe expanded target url which the link points to.

## Slack-compatible format
This webhook format is compatible withSlack's outgoing webhook
API,
which can help with porting an existing Slack integration to work with
Zulip, and allows immediate integration with many third-party systems
that already support Slack outgoing webhooks.
The following table details how the Zulip server translates a Zulip
message into the Slack-compatible webhook format.

[TABLE]
Name | Description
token | A string of alphanumeric characters you can use to
            authenticate the webhook request (each bot user uses a fixed token)
team_id | ID of the Zulip organization prefixed by "T".
team_domain | Hostname of the Zulip organization
channel_id | Channel ID prefixed by "C"
channel_name | Channel name
thread_ts | Timestamp for when message was sent
timestamp | Timestamp for when message was sent
user_id | ID of the user who sent the message prefixed by "U"
user_name | Full name of sender
text | The content of the message (in Markdown)
trigger_word | Trigger method
service_id | ID of the bot user
[/TABLE]

```
team_domain
```

```
channel_name
```

```
trigger_word
```
The above data is posted as list of tuples (not JSON), here's an example:

```
[('token', 'v9fpCdldZIej2bco3uoUvGp06PowKFOf'),
 ('team_id', 'T1512'),
 ('team_domain', 'zulip.example.com'),
 ('channel_id', 'C123'),
 ('channel_name', 'integrations'),
 ('thread_ts', 1532078950),
 ('timestamp', 1532078950),
 ('user_id', 'U21'),
 ('user_name', 'Full Name'),
 ('text', '@**test**'),
 ('trigger_word', 'mention'),
 ('service_id', 27)]
```

```
[('token', 'v9fpCdldZIej2bco3uoUvGp06PowKFOf'),
 ('team_id', 'T1512'),
 ('team_domain', 'zulip.example.com'),
 ('channel_id', 'C123'),
 ('channel_name', 'integrations'),
 ('thread_ts', 1532078950),
 ('timestamp', 1532078950),
 ('user_id', 'U21'),
 ('user_name', 'Full Name'),
 ('text', '@**test**'),
 ('trigger_word', 'mention'),
 ('service_id', 27)]
```
- For successful requests, if data is returned, it returns that data,
  else it returns a blank response.
- For failed requests, it returns the reason of failure, as returned by
  the server, or the exception message.
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.