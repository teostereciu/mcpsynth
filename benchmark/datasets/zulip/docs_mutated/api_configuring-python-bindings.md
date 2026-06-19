# Configuring the Python bindings | Zulip API documentation

*Source: https://zulip.com/api/configuring-python-bindings*

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

# Configuring the Python bindings
Zulip provides a set of tools that allows interacting with its API more
easily, called thePython bindings.
One of the most notable use cases for these bindings are bots developed
using Zulip'sbot framework.
In order to use them, you need to configure them with your identity
(account, API key, and Zulip server URL). There are a few ways to
achieve that:
- Using azuliprcfile, referenced via the--config-fileoption or
  theconfig_fileoption to thezulip.Clientconstructor
  (recommended for bots).
- Using azuliprcfile in your home directory at~/.zuliprc(recommended for your own API key).
- Using theenvironment
  variablesdocumented below.
- Using the--api-key,--email, and--sitevariables as command
  line parameters.
- Using theapi_key,email, andsiteparameters to thezulip.Clientconstructor.

## Download azuliprcfile
For a botFor yourself
- For a bot
- For yourself
1. Click on thegear() icon in the upper
   right corner of the web or desktop app.
2. SelectPersonal settings.
3. On the left, clickBots.
4. In theActionscolumn, click themanage bot() icon,
   and scroll down toZuliprc configuration.
5. Click thedownload() icon
   to download the bot'szuliprcfile, or thecopy() icon to
   copy the file's content to your clipboard.
Anyone with a bot's API key can impersonate the bot, so be careful with it!
1. Click on thegear() icon in the upper
   right corner of the web or desktop app.
2. SelectPersonal settings.
3. On the left, clickAccount & privacy.
4. UnderAPI key, clickManage your API key.
5. Enter your password, and clickGet API key. If you don't know your
   password, clickreset itand follow the
   instructions from there.
6. ClickDownload zuliprcto download yourzuliprcfile.
7. (optional) If you'd like your credentials to be used by default
   when using the Zulip API on your computer, move thezuliprcfile
   to~/.zuliprcin your home directory.
Anyone with your API key can impersonate you, so be doubly careful with it.

## Configuration keys and environment variables
zuliprcis a configuration file written in theINI file format,
which contains key-value pairs as shown in the following example:

```
[api]
key=<API key from the web interface>
email=<your email address>
site=<your Zulip server's URI>
...
```

```
[api]
key=<API key from the web interface>
email=<your email address>
site=<your Zulip server's URI>
...
```
The keys you can use in this file (and their equivalent environment variables)
can be found in the following table:

[TABLE]
zuliprckey | Environment variable | Required | Description
key | ZULIP_API_KEY | Yes | API key, which you can get through
            Zulip's web interface.
email | ZULIP_EMAIL | Yes | The email address of the user who owns the API key mentioned
            above.
site | ZULIP_SITE | No | URL where your Zulip server is located.
client_cert_key | ZULIP_CERT_KEY | No | Path to the SSL/TLS private key that the binding should use to
            connect to the server.
client_cert | ZULIP_CERT | No* | The public counterpart ofclient_cert_key/ZULIP_CERT_KEY.This setting is required if a cert
            key has been set.
client_bundle | ZULIP_CERT_BUNDLE | No | Path where the server's PEM-encoded certificate is located. CA
            certificates are also accepted, in case those CA's have issued the
            server's certificate. Defaults to the built-in CA bundle trusted
            by Python.
insecure | ZULIP_ALLOW_INSECURE | No | Allows connecting to Zulip servers with an invalid SSL/TLS
            certificate. Please note that enabling this will make the HTTPS
            connection insecure. Defaults tofalse.
[/TABLE]

```
ZULIP_API_KEY
```

```
ZULIP_EMAIL
```

```
client_cert_key
```

```
ZULIP_CERT_KEY
```

```
client_cert
```

```
client_cert_key
```

```
ZULIP_CERT_KEY
```

```
client_bundle
```

```
ZULIP_CERT_BUNDLE
```

```
ZULIP_ALLOW_INSECURE
```

## Related articles
- Installation instructions
- API keys
- Running bots
- Deploying bots
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.