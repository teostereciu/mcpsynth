# Fetch a single message | Zulip API documentation

*Source: https://zulip.com/api/get-message*

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

# Fetch a single message
GET https://your-org.zulipchat.com/api/v1/messages/{message_id}
Given a message ID, return the message object.
Additionally, araw_contentfield is included. This field is
useful for clients that primarily work with HTML-rendered
messages but might need to occasionally fetch the message's
rawZulip-flavored Markdown(e.g. forview
sourceor
prefilling a message edit textarea).
Changes: Before Zulip 5.0 (feature level 120), this
endpoint only returned theraw_contentfield.

## Usage examples
Pythoncurl
- Python
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Get the raw content of a message given the message's ID.result=client.get_raw_message(message_id)print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Get the raw content of a message given the message's ID.result=client.get_raw_message(message_id)print(result)
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/messages/43 \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode apply_markdown=false \
    --data-urlencode allow_empty_topic_name=true
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/messages/43 \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode apply_markdown=false \
    --data-urlencode allow_empty_topic_name=true
```

## Parameters
message_idintegerrequired in path
The target message's ID.
apply_markdownbooleanoptional
Iftrue, message content is returned in the rendered HTML
format. Iffalse, message content is returned in the rawZulip-flavored Markdown formattext that user entered.
Changes: New in Zulip 5.0 (feature level 120).
Defaults totrue.
allow_empty_topic_namebooleanoptional
Whether the client supports processing the empty string as a topic in the
topic name fields in the returned data, including in returned edit_history data.
Iffalse, the server will use the value ofrealm_empty_topic_display_namefound in thePOST /registerresponse instead of empty string
to represent the empty string topic in its response.

```
POST /register
```
Changes: New in Zulip 10.0 (feature level 334). Previously, the empty string
was not a valid topic.
Defaults tofalse.

## Response

#### Return values
- raw_content:stringThe raw Markdown content of the message.See the help center article onmessage formattingfor details on Zulip-flavored Markdown.Deprecatedand to be removed once no longer required for
legacy clients. Modern clients should prefer passing"apply_markdown": falseto request raw message content.
- message:objectAn object containing details of the message.Changes: New in Zulip 5.0 (feature level 120).avatar_url:string | nullThe URL of the message sender's avatar. Can benullonly if
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
Zulip 4.0 (feature level 46).New in Zulip 3.0 (feature level 1). Previously, this field was calledsubject_links; clients are recommended to renamesubject_linkstotopic_linksif present for compatibility with older Zulip servers.text:stringThe original link text present in the topic.url:stringThe expanded target url which the link points to.type:stringThe type of the message:"stream"or"private".flags:(string)[]The user'smessage flagsfor the message.Changes: In Zulip 8.0 (feature level 224), thewildcard_mentionedflag was deprecated in favor of thestream_wildcard_mentionedandtopic_wildcard_mentionedflags. Thewildcard_mentionedflag exists
for backwards compatibility with older clients and equalsstream_wildcard_mentioned || topic_wildcard_mentioned. Clients
supporting older server versions should treat this field as a previous
name for thestream_wildcard_mentionedflag as topic wildcard mentions
were not available prior to this feature level.
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
- flags:(string)[]The user'smessage flagsfor the message.Changes: In Zulip 8.0 (feature level 224), thewildcard_mentionedflag was deprecated in favor of thestream_wildcard_mentionedandtopic_wildcard_mentionedflags. Thewildcard_mentionedflag exists
for backwards compatibility with older clients and equalsstream_wildcard_mentioned || topic_wildcard_mentioned. Clients
supporting older server versions should treat this field as a previous
name for thestream_wildcard_mentionedflag as topic wildcard mentions
were not available prior to this feature level.
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

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"message":{"avatar_url":"https://secure.gravatar.com/avatar/6d8cad0fd00256e7b40691d27ddfd466?d=identicon&version=1","client":"ZulipDataImport","content":"<p>Security experts agree that relational algorithms are an interesting new topic in the field of networking, and scholars concur.</p>","content_type":"text/html","display_recipient":[{"email":"hamlet@zulip.com","full_name":"King Hamlet","id":4,"is_mirror_dummy":false},{"email":"iago@zulip.com","full_name":"Iago","id":5,"is_mirror_dummy":false},{"email":"prospero@zulip.com","full_name":"Prospero from The Tempest","id":8,"is_mirror_dummy":false}],"flags":["read"],"id":16,"is_me_message":false,"reactions":[],"recipient_id":27,"sender_email":"hamlet@zulip.com","sender_full_name":"King Hamlet","sender_id":4,"sender_realm_str":"zulip","subject":"","submessages":[],"timestamp":1527921326,"topic_links":[],"type":"private"},"msg":"","raw_content":"**Don't** forget your towel!","result":"success"}
```

```
{"message":{"avatar_url":"https://secure.gravatar.com/avatar/6d8cad0fd00256e7b40691d27ddfd466?d=identicon&version=1","client":"ZulipDataImport","content":"<p>Security experts agree that relational algorithms are an interesting new topic in the field of networking, and scholars concur.</p>","content_type":"text/html","display_recipient":[{"email":"hamlet@zulip.com","full_name":"King Hamlet","id":4,"is_mirror_dummy":false},{"email":"iago@zulip.com","full_name":"Iago","id":5,"is_mirror_dummy":false},{"email":"prospero@zulip.com","full_name":"Prospero from The Tempest","id":8,"is_mirror_dummy":false}],"flags":["read"],"id":16,"is_me_message":false,"reactions":[],"recipient_id":27,"sender_email":"hamlet@zulip.com","sender_full_name":"King Hamlet","sender_id":4,"sender_realm_str":"zulip","subject":"","submessages":[],"timestamp":1527921326,"topic_links":[],"type":"private"},"msg":"","raw_content":"**Don't** forget your towel!","result":"success"}
```
An example JSON response for when the specified message does not exist or it
is not visible to the user making the query (e.g. it was a direct message
between two other users):

```
{"code":"BAD_REQUEST","msg":"Invalid message(s)","result":"error"}
```

```
{"code":"BAD_REQUEST","msg":"Invalid message(s)","result":"error"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.