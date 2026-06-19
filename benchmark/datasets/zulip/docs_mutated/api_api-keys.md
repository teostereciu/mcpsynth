# API keys | Zulip API documentation

*Source: https://zulip.com/api/api-keys*

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

# API keys
AnAPI keyis how a bot identifies itself to Zulip. For the official
clients, such as the Python bindings, we recommenddownloading azuliprcfile. This file
contains an API key and other necessary configuration values for using the
Zulip API with a specific account on a Zulip server.

## Get API key
For a botFor yourself
- For a bot
- For yourself
1. Click on thegear() icon in the upper
   right corner of the web or desktop app.
2. SelectPersonal settings.
3. On the left, clickBots.
4. In theActionscolumn, click themanage bot() icon,
   and scroll down toAPI key.
5. Click thecopy() icon to
   copy the bot's API key to your clipboard.
Anyone with a bot's API key can impersonate the bot, so be careful with it!
1. Click on thegear() icon in the upper
   right corner of the web or desktop app.
2. SelectPersonal settings.
3. On the left, clickAccount & privacy.
4. UnderAPI key, clickManage your API key.
5. Enter your password, and clickGet API key. If you don't know your
   password, clickreset itand follow the instructions from there.
6. Copy your API key.
Anyone with your API key can impersonate you, so be doubly careful with it.

## Invalidate an API key
To invalidate an existing API key, you have to generate a new key.
For a botFor yourself
- For a bot
- For yourself
1. Click on thegear() icon in the upper
   right corner of the web or desktop app.
2. SelectPersonal settings.
3. On the left, clickBots.
4. In theActionscolumn, click themanage bot() icon,
   and scroll down toAPI key.
5. Click thegenerate new API key() icon.
1. Click on thegear() icon in the upper
   right corner of the web or desktop app.
2. SelectPersonal settings.
3. On the left, clickAccount & privacy.
4. UnderAPI key, clickManage your API key.
5. Enter your password, and clickGet API key. If you don't know your
   password, clickreset itand follow the instructions from there.
6. ClickGenerate new API key

## Related articles
- Configuring the Python bindings
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.