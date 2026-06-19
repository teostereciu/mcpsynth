# Get server settings | Zulip API documentation

*Source: https://zulip.com/api/get-server-settings*

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

# Get server settings
GET https://your-org.zulipchat.com/api/v1/server_settings
Fetch global settings for a Zulip server.
Note:this endpoint does not require any authentication at all, and you can use it to check:
- If this is a Zulip server, and if so, what version of Zulip it's running.
- What a Zulip client (e.g. a mobile app orzulip-terminal) needs to
  know in order to display a login prompt for the server (e.g. what
  authentication methods are available).

## Usage examples
Pythoncurl
- Python
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Fetch the settings for this server.result=client.get_server_settings()print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Fetch the settings for this server.result=client.get_server_settings()print(result)
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/server_settings \
    -u EMAIL_ADDRESS:API_KEY
```

```
curl -sSX GET -G https://your-org.zulipchat.com/api/v1/server_settings \
    -u EMAIL_ADDRESS:API_KEY
```

## Parameters
This endpoint does not accept any parameters.

## Response

#### Return values
- authentication_methods:objectEach key-value pair in the object indicates whether the authentication
method is enabled on this server.Changes: Deprecated in Zulip 2.1.0, in favor of the more expressiveexternal_authentication_methods.password:booleanWhether the user can authenticate using password.dev:booleanWhether the user can authenticate using development API key.email:booleanWhether the user can authenticate using email.ldap:booleanWhether the user can authenticate using LDAP.remoteuser:booleanWhether the user can authenticate using REMOTE_USER.github:booleanWhether the user can authenticate using their GitHub account.azuread:booleanWhether the user can authenticate using their Microsoft Entra ID account.gitlab:booleanWhether the user can authenticate using their GitLab account.Changes: New in Zulip 3.0 (feature level 1).apple:booleanWhether the user can authenticate using their Apple account.google:booleanWhether the user can authenticate using their Google account.saml:booleanWhether the user can authenticate using SAML.openid connect:booleanWhether the user can authenticate using OpenID Connect.
- external_authentication_methods:(object)[]A list of dictionaries describing the available external
authentication methods (E.g. Google, GitHub, or SAML)
enabled for this organization.The list is sorted in the order in which these
authentication methods should be displayed.Changes: New in Zulip 2.1.0.name:stringA unique, table, machine-readable name for the authentication method,
intended to be used by clients with special behavior for specific
authentication methods to correctly identify the method.display_name:stringDisplay name of the authentication method, to be used in all buttons
for the authentication method.display_icon:string | nullURL for an image to be displayed as an icon in all buttons for
the external authentication method. This URL should be resolved
relative to the server's base URL.Whennull, no icon should be displayed.login_url:stringURL to be used to initiate authentication using this method.signup_url:stringURL to be used to initiate account registration using this method.
- zulip_feature_level:integerAn integer indicating what features are
available on the server. The feature level increases monotonically;
a value of N means the server supports all API features introduced
before feature level N. This is designed to provide a simple way
for client apps to decide whether the server supports a given
feature or API change. See thechangelogfor
details on what each feature level means.Changes: New in Zulip 3.0 (feature level 1). We recommend using an
implied value of 0 for Zulip servers that do not send this field.
- zulip_version:stringThe server's version number. This is often a release version number,
like2.1.7. But for a server running aversion from Git,
it will be a Git reference to the commit, like5.0-dev-1650-gc3fd37755f.
- zulip_merge_base:stringThegit merge-basebetweenzulip_versionand official branches
in the publicZulip server and web app repository,
in the same format aszulip_version. This will equalzulip_versionif the server is not running a fork of the Zulip server.This will be""if unavailable.Changes: New in Zulip 5.0 (feature level 88).
- push_notifications_enabled:booleanWhether mobile/push notifications are configured.
- is_incompatible:booleanWhether the Zulip client that has sent a request to this endpoint is
deemed incompatible with the server.
- email_auth_enabled:booleanSetting for allowing users authenticate with an email-password
combination.
- require_email_format_usernames:booleanWhether all valid usernames for authentication to this
organization will be email addresses. This is important
for clients to know whether to do client side validation
of email address format in a login prompt.This value will be false if the server hasLDAP
authenticationenabled with a username and
password combination.
- realm_uri:stringThe organization's canonical URL. Alias ofrealm_url.Changes: Deprecated in Zulip 9.0 (feature level 257). The term
"URI" is deprecated inweb standards.
- realm_url:stringThe organization's canonical URL.Changes: New in Zulip 9.0 (feature level 257), replacing the
deprecatedrealm_uri.
- realm_name:stringThe organization's name (for display purposes).
- realm_icon:stringThe URL for the organization's logo formatted as a square image,
used for identifying the organization in small locations in the
mobile and desktop apps.
- realm_description:stringHTML description of the organization, as configured by theorganization
profile.
- realm_web_public_access_enabled:booleanWhether the organization has enabled the creation ofweb-public channelsand
at least one web-public channel on the server currently
exists. Clients that support viewing content
in web-public channels without an account can
use this to determine whether to offer that
feature on the login page for an organization.Changes: New in Zulip 5.0 (feature level 116).
- password:booleanWhether the user can authenticate using password.
- dev:booleanWhether the user can authenticate using development API key.
- email:booleanWhether the user can authenticate using email.
- ldap:booleanWhether the user can authenticate using LDAP.
- remoteuser:booleanWhether the user can authenticate using REMOTE_USER.
- github:booleanWhether the user can authenticate using their GitHub account.
- azuread:booleanWhether the user can authenticate using their Microsoft Entra ID account.
- gitlab:booleanWhether the user can authenticate using their GitLab account.Changes: New in Zulip 3.0 (feature level 1).
- apple:booleanWhether the user can authenticate using their Apple account.
- google:booleanWhether the user can authenticate using their Google account.
- saml:booleanWhether the user can authenticate using SAML.
- openid connect:booleanWhether the user can authenticate using OpenID Connect.
- name:stringA unique, table, machine-readable name for the authentication method,
intended to be used by clients with special behavior for specific
authentication methods to correctly identify the method.
- display_name:stringDisplay name of the authentication method, to be used in all buttons
for the authentication method.
- display_icon:string | nullURL for an image to be displayed as an icon in all buttons for
the external authentication method. This URL should be resolved
relative to the server's base URL.Whennull, no icon should be displayed.
- login_url:stringURL to be used to initiate authentication using this method.
- signup_url:stringURL to be used to initiate account registration using this method.
Please note that not all of these attributes are guaranteed to appear in a
response, for two reasons:
- This endpoint has evolved over time, so responses from older Zulip servers
  might be missing some keys (in which case a client should assume the
  appropriate default).
- If a/server_settingsrequest is made to the root domain of a
  multi-subdomain server, like the root domain of zulip.com, the settings
  that are realm-specific are not known and thus not provided.

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"authentication_methods":{"azuread":false,"dev":true,"email":true,"github":true,"google":true,"ldap":false,"password":true,"remoteuser":false,"saml":true},"email_auth_enabled":true,"external_authentication_methods":[{"display_icon":null,"display_name":"SAML","login_url":"/accounts/login/social/saml/idp_name","name":"saml:idp_name","signup_url":"/accounts/register/social/saml/idp_name"},{"display_icon":"/static/images/authentication_backends/googl_e-icon.png","display_name":"Google","login_url":"/accounts/login/social/google","name":"google","signup_url":"/accounts/register/social/google"},{"display_icon":"/static/images/authentication_backends/github-icon.png","display_name":"GitHub","login_url":"/accounts/login/social/github","name":"github","signup_url":"/accounts/register/social/github"}],"is_incompatible":false,"msg":"","push_notifications_enabled":false,"realm_description":"<p>The Zulip development environment default organization.  It's great for testing!</p>","realm_icon":"https://secure.gravatar.com/avatar/62429d594b6ffc712f54aee976a18b44?d=identicon","realm_name":"Zulip Dev","realm_uri":"http://localhost:9991","realm_url":"http://localhost:9991","realm_web_public_access_enabled":false,"require_email_format_usernames":true,"result":"success","zulip_merge_base":"5.0-dev-1646-gea6b21cd8c","zulip_version":"5.0-dev-1650-gc3fd37755f"}
```

```
{"authentication_methods":{"azuread":false,"dev":true,"email":true,"github":true,"google":true,"ldap":false,"password":true,"remoteuser":false,"saml":true},"email_auth_enabled":true,"external_authentication_methods":[{"display_icon":null,"display_name":"SAML","login_url":"/accounts/login/social/saml/idp_name","name":"saml:idp_name","signup_url":"/accounts/register/social/saml/idp_name"},{"display_icon":"/static/images/authentication_backends/googl_e-icon.png","display_name":"Google","login_url":"/accounts/login/social/google","name":"google","signup_url":"/accounts/register/social/google"},{"display_icon":"/static/images/authentication_backends/github-icon.png","display_name":"GitHub","login_url":"/accounts/login/social/github","name":"github","signup_url":"/accounts/register/social/github"}],"is_incompatible":false,"msg":"","push_notifications_enabled":false,"realm_description":"<p>The Zulip development environment default organization.  It's great for testing!</p>","realm_icon":"https://secure.gravatar.com/avatar/62429d594b6ffc712f54aee976a18b44?d=identicon","realm_name":"Zulip Dev","realm_uri":"http://localhost:9991","realm_url":"http://localhost:9991","realm_web_public_access_enabled":false,"require_email_format_usernames":true,"result":"success","zulip_merge_base":"5.0-dev-1646-gea6b21cd8c","zulip_version":"5.0-dev-1650-gc3fd37755f"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.