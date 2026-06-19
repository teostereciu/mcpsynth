# HTTP headers | Zulip API documentation

*Source: https://zulip.com/api/http-headers*

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

# HTTP headers
This page documents the HTTP headers used by the Zulip API.
Full details of the HTTP requests are given in thecurlexample
on each endpoint's documentation page. You can access curl's
documentation atman curl.

## TheAuthorizationheader

```
Authorization
```
Most important is that API clients authenticate to the server using
HTTP Basic authentication. If you're using the officialPython or
JavaScript bindings, this is taken
care of when you configure said bindings.
Otherwise, to authenticate an API request:
- Use HTTPBasicauthentication, which is describedhere.
  This means sending an HTTP header namedAuthorization, with your
  credentialsin a certain format.
- ForBasicauthentication credentials in the Zulip API, a "username"
  takes the form of an email address, and a "password" takes the form of
  an API key. In thecurlexample for each endpoint, this is shown as:-u EMAIL_ADDRESS:API_KEY.
- A bot's credentials can be obtained through the web and desktop apps'bot management UIor bydownloading the bot's
  zuliprc file.
- Seefetch an API key (production)for the
  password-based authentication flow for getting a user's credentials.

## TheUser-Agentheader
Clients are not required to pass aUser-AgentHTTP header, but we
highly recommend doing so when writing an integration. It's easy to do
and it can help save time when debugging issues related to an API
client.
If provided, the Zulip server will parse theUser-AgentHTTP header
in order to identify specific clients and integrations. This
information is used by the server for logging,usage
statistics, and on rare occasions, for
backwards-compatibility logic to preserve support for older versions
of official clients.
Official Zulip clients and integrations use aUser-Agentthat starts
with something likeZulipMobile/20.0.103, encoding the name of the
application and it's version.
Zulip's official API bindings have reasonable defaults forUser-Agent. For example, the official Zulip Python bindings have a
defaultUser-Agentstarting withZulipPython/{version}, whereversionis the version of the library.
You can give your bot/integration its own name by passing theclientparameter when initializing the Python bindings. For example, the
official Zulip Nagios integration is initialized like this:

```
client=zulip.Client(config_file=opts.config,client=f"ZulipNagios/{VERSION}")
```

```
client=zulip.Client(config_file=opts.config,client=f"ZulipNagios/{VERSION}")
```
If you are working on an integration that you plan to share outside
your organization, you can get help picking a good name in#integrationsin theZulip development
community.

## Rate-limiting response headers
To help clients avoid exceeding rate limits, Zulip sets the following
HTTP headers in all API responses:
- X-RateLimit-Remaining: The number of additional requests of this
  type that the client can send before exceeding its limit.
- X-RateLimit-Limit: The limit that would be applicable to a client
  that had not made any recent requests of this type. This is useful
  for designing a client's burst behavior so as to avoid ever reaching
  a rate limit.
- X-RateLimit-Reset: The time at which the client will no longer
  have any rate limits applied to it (and thus could do a burst ofX-RateLimit-Limitrequests).
Zulip's rate limiting rules are configurable,
and can vary by server and over time. The default configuration
currently limits:
- Every user is limited to 200 total API requests per minute.
- Separate, much lower limits for authentication/login attempts.
When the Zulip server has configured multiple rate limits that apply
to a given request, the values returned will be for the strictest
limit.
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.