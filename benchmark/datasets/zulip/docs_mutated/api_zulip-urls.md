# Zulip URLs | Zulip API documentation

*Source: https://zulip.com/api/zulip-urls*

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

# Zulip URLs
This page details how to properly construct and parse the URLs that
the Zulip web app uses for various types of views.
Because other clients needs to be able to resolve and process these
links in order to implement equivalent behavior that navigates
directly in say the mobile apps, it's important to have a clear
specification of exactly how these URLs work.
Essentially all of the data is encoded in the URL fragment (#) part
of a URL; the protocol, host and path will just be the canonical URL
for the Zulip server (In these examples,https://zulip.example.com/).

## Message feed views
Most links in Zulip are to message feed views, and for that reason
these have the most developed syntax and legacy behavior.
Message feed URLs always start with#filter_spec/, follow by one or moresearch operator/operand pairs, separated by/s. The operator may be negated by putting a-at the start of
it. For example:
https://zulip.example.com/#filter_spec/is/starred/sender/17/-channel/14
is the feed of starred messages sent by user ID to everywhere but
channel 14. The search documentation covers the valid operators and
their meaning.
See also the relevantmessage formatting
documentationfor details on Markdown
representations of Zulip-internal links that will be translated into
HTML containing links that use these URLs.
Here, we describe some special encoding rules.

### Operand encoding and decoding
Strings in operands are URL-encoded, and then additional substitution
rules are applied to avoid over-zealous browser handling of certain
characters in the URL fragment:
- %=>.
- (=>.28
- )=>.29
- .=>.2E
They can decoded by applying the reverse transformation: Replace all.characters with%, and then do standard URL-decoding.

### Encoding channels
Channel operands must be encoded in one of the two modern fully
supported formats:
- 42: Just the ID of the channel. Clients should simply parse the
  channel ID to look up the channel, which is of course not guaranteed
  to be accessible to the acting user or even exist.
- 42-channel-name. The ID of the channel, with a human-readable hint
  of the channel name. Clients generating Zulip URLs are recommended
  to include channel name hints where there is a readable URL-encoding
  of the channel name, but to skip doing so for channel names written
  in non-ascii languages or where otherwise the slug would not make
  the URL nicer for humans. Clients must parse this format by
  discarding everything after the-and treating it identically to
  the simpler integer-only format. Note that means nothing enforces
  that the string have anything to do with the channel name;
  functionally, it just an optional hint.
These two formats allow Zulip URLs to stably refer to a specific
channel, even though channels can be renamed, while still allowing the
URLs to have user-friendly name hints most of the time.
There is an additional legacy format that was used prior to 2018 that
clients are required to support:
- channel-name: Legacy format of just the channel name, URL-encoded
  and with spaces replaced with dashes. The legacy format should never
  take precedence over the modern format, so a link with2016-electionas the slug must be parsed as the channel with ID
  2016, even if theoretically it could have been originally intended
  as referring to a channel named2016 election.
Clients are not recommended to ever generate this legacy format.

## zulip:// links for mobile login
Zulip's single-sign on login process for the mobile app ends with a
redirect tozulip://loginwith the following query parameters:
- email: The email address for the authenticated account.
- otp_encrypted_api_key: The API key for the client, encrypted using
  themobile_flow_otpthat the client provided when initiating the
  login attempt.
- realm: The full URL of the Zulip organization.
- user_id: The Zulip user ID for the authenticated account.
Changes: Theuser_idfield was added to the set of included
query parameters in Zulip 5.0 (feature level 128).

## Related articles
- Message formatting API
- Construct a narrowfor search.
- Markdown formatting help
- Send a message
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.