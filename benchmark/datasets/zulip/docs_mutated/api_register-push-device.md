# Register E2EE push device | Zulip API documentation

*Source: https://zulip.com/api/register-push-device*

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

# Register E2EE push device
POST https://your-org.zulipchat.com/api/v1/mobile_push/register
Register a device to receive end-to-end encrypted mobile push notifications,
or update such a registration.
To perform an initial registration, clients must provide both the
push key fields (push_keyandpush_key_id) and the token fields
(token_kind,token_id,bouncer_public_key, andencrypted_push_registration).
Once registered, clients should use this endpoint to rotatepush_keyor
FCM/APNs provided token:
- Rotate push key: Provide only the push key fields.
- Rotate token: Provide only the token fields.
Changes: In Zulip 12.0 (feature level 468), the endpoint
was significantly redesigned to support rotation ofpush_keyand
token provided by FCM/APNs.
New in Zulip 11.0 (feature level 406).

## Usage examples
Pythoncurl
- Python
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Register a device for push notifications.request={"device_id":device_id,"token_kind":"fcm","push_key":"MTaUDJDMWypQ1WufZ1NRTHSSvgYtXh1qVNSjN3aBiEFt","push_key_id":2408,"bouncer_public_key":"bouncer-public-key","encrypted_push_registration":"encrypted-push-registration-data","token_id":"hGsEWGmyyfI=",}result=client.call_endpoint(url="/mobile_push/register",method="POST",request=request)print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Register a device for push notifications.request={"device_id":device_id,"token_kind":"fcm","push_key":"MTaUDJDMWypQ1WufZ1NRTHSSvgYtXh1qVNSjN3aBiEFt","push_key_id":2408,"bouncer_public_key":"bouncer-public-key","encrypted_push_registration":"encrypted-push-registration-data","token_id":"hGsEWGmyyfI=",}result=client.call_endpoint(url="/mobile_push/register",method="POST",request=request)print(result)
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/mobile_push/register \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode device_id=1 \
    --data-urlencode push_key_id=2408 \
    --data-urlencode push_key=MTaUDJDMWypQ1WufZ1NRTHSSvgYtXh1qVNSjN3aBiEFt \
    --data-urlencode token_kind=fcm \
    --data-urlencode token_id=hGsEWGmyyfI= \
    --data-urlencode bouncer_public_key=bouncer-public-key \
    --data-urlencode encrypted_push_registration=encrypted-push-registration-data
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/mobile_push/register \
    -u EMAIL_ADDRESS:API_KEY \
    --data-urlencode device_id=1 \
    --data-urlencode push_key_id=2408 \
    --data-urlencode push_key=MTaUDJDMWypQ1WufZ1NRTHSSvgYtXh1qVNSjN3aBiEFt \
    --data-urlencode token_kind=fcm \
    --data-urlencode token_id=hGsEWGmyyfI= \
    --data-urlencode bouncer_public_key=bouncer-public-key \
    --data-urlencode encrypted_push_registration=encrypted-push-registration-data
```

## Parameters
device_idintegerrequired
The ID of the device to configure for push notifications.
SeePOST /register_client_devicefor how to obtain a device ID.

```
POST /register_client_device
```
push_key_idintegeroptional
A random unsigned 32-bit integer generated by the client as an identifier
forpush_key. It will be included in mobile push notifications
along with encrypted payloads to identify thepush_keyto decrypt.
push_keystringoptional

```
"MTaUDJDMWypQ1WufZ1NRTHSSvgYtXh1qVNSjN3aBiEFt"
```
Key that the client would like the server to use to encrypt notifications,
encoded with Base64.
The key is a byte sequence beginning with a single byte that encodes which
cryptosystem to use, followed by the key to use for that cryptosystem.
This byte sequence is encoded using standard Base64 encoding as defined in RFC 4648.
The client should avoid sharing the key anywhere else: in particular it should
generate a fresh key for each server, and to the extent possible keep the key
out of any backups of the client's data.
Supported cryptosystems are:
- 0x31: LibSodium'sSecretBoxsymmetric key encryption
  system. Keys are 32 bytes, which the server will use with libsodium'scrypto_secretbox_easy. See theNaCl documentation, which
  details how this system usesXSalsa20andPoly1305to provide authenticated
  encryption.
Changes: New in Zulip 12.0 (feature level 432). This replaced thepush_public_keyparameter which had a prototype asymmetric cryptosystem, and
did not have a natural way to support multiple cryptosystems.
token_kindstringoptional
Whether the token was generated by FCM or APNs.
Must be one of:"fcm","apns".
token_idstringoptional

```
"hGsEWGmyyfI="
```
Identifier for the FCM/APNs provided token to the device,
produced by taking the first 8 bytes of the SHA-256 hash of
the token, then encoding those bytes using standard Base64 encoding
as defined in RFC 4648.
bouncer_public_keystringoptional

```
"bouncer-public-key"
```
Which of the bouncer's public keys the client used to encrypt thePushRegistrationdictionary.
When the bouncer rotates the key, a new asymmetric key pair is created,
and the new public key is baked into a new client release. Because
the bouncer routinely rotates key, this field clarifies which
public key the client is using.
The public key is encoded using standard Base64 encoding as defined
in RFC 4648.
encrypted_push_registrationstringoptional

```
"encrypted-push-registration-data"
```
Ciphertext generated by encrypting aPushRegistrationdictionary
using thebouncer_public_key, encoded using a RFC 4648 standard
base64 encoder.
ThePushRegistrationdictionary contains the fieldstoken,token_kind,timestamp, and (for iOS devices)ios_app_id.
The dictionary is JSON-encoded before encryption.

## Response

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"msg":"","result":"success"}
```

```
{"msg":"","result":"success"}
```
Error when the server is not configured to use push notification service:

```
{"code":"PUSH_SERVICE_NOT_CONFIGURED","msg":"Server is not configured to use push notification service.","result":"error"}
```

```
{"code":"PUSH_SERVICE_NOT_CONFIGURED","msg":"Server is not configured to use push notification service.","result":"error"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.