# Upload a file | Zulip API documentation

*Source: https://zulip.com/api/upload-file*

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

# Upload a file
POST https://your-org.zulipchat.com/api/v1/user_uploads
Uploada single file and get the corresponding URL.
Initially, only you will be able to access the link. To share the
uploaded file, you'll need tosend a messagecontaining the resulting link. Users who can already access the link
can reshare it with other users by sending additional Zulip messages
containing the link.
The maximum allowed file size is available in themax_file_upload_size_mibfield in thePOST /registerresponse. Note that
large files (25MB+) may fail to upload using this API endpoint due to
network-layer timeouts, depending on the quality of your connection to the
Zulip server.

```
POST /register
```
For uploading larger files,/api/v1/tusis an endpoint implementing thetusresumable upload protocol,
which supports uploading arbitrarily large files limited only by the server'smax_file_upload_size_mib(Configured viaMAX_FILE_UPLOAD_SIZEin/etc/zulip/settings.py). Clients which send authenticated credentials
(either via browser-based cookies, or API key viaAuthorizationheader) may
use this endpoint to upload files.
Changes: Theapi/v1/tusendpoint supporting resumable uploads was
introduced in Zulip 10.0 (feature level 296). Previously,max_file_upload_size_mibwas typically 25MB.

## Usage examples
Pythoncurl
- Python
- curl

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Upload a file.withopen(path_to_file,"rb")asfp:result=client.upload_file(fp)# Share the file by including it in a message.client.send_message({"type":"stream","to":"Denmark","topic":"Castle","content":"Check out [this picture]({}) of my castle!".format(result["url"]),})print(result)
```

```
#!/usr/bin/env python3importzulip# Pass the path to your zuliprc file here.client=zulip.Client(config_file="~/zuliprc")# Upload a file.withopen(path_to_file,"rb")asfp:result=client.upload_file(fp)# Share the file by including it in a message.client.send_message({"type":"stream","to":"Denmark","topic":"Castle","content":"Check out [this picture]({}) of my castle!".format(result["url"]),})print(result)
```
The-ulineimplements HTTPBasicauthentication.
See theAuthorizationheaderdocumentation for how
to get those credentials for Zulip users and bots.

```
Authorization
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/user_uploads \
    -u EMAIL_ADDRESS:API_KEY \
    -F filename=@/path/to/file
```

```
curl -sSX POST https://your-org.zulipchat.com/api/v1/user_uploads \
    -u EMAIL_ADDRESS:API_KEY \
    -F filename=@/path/to/file
```

## Parameters
As described above, the file to upload must be provided in the
request's body.

## Response

#### Return values
- uri:stringThe URL of the uploaded file. Alias ofurl.Changes: Deprecated in Zulip 9.0 (feature level 272). The term
"URI" is deprecated inweb standards.
- url:stringThe URL of the uploaded file.Changes: New in Zulip 9.0 (feature level 272). Previously,
this property was only available under the legacyuriname.
- filename:stringThe filename that Zulip stored the upload as. This usually
differs from the basename of the URL when HTML escaping is
required to generate a valid URL.Clients generating a Markdown link to a newly uploaded file
should do so by combining theurlandfilenamefields in the
response as follows:[{filename}]({url}), with care taken to
cleanfilenameof[and]characters that might break
Markdown rendering.Changes: New in Zulip 10.0 (feature level 285).

#### Example response(s)
Changes: As of Zulip 7.0 (feature level 167), if any
parameters sent in the request are not supported by this
endpoint, a successful JSON response will include anignored_parameters_unsupportedarray.

```
ignored_parameters_unsupported
```
A typical successful JSON response may look like:

```
{"filename":"zulip.txt","msg":"","result":"success","uri":"/user_uploads/1/4e/m2A3MSqFnWRLUf9SaPzQ0Up_/zulip.txt","url":"/user_uploads/1/4e/m2A3MSqFnWRLUf9SaPzQ0Up_/zulip.txt"}
```

```
{"filename":"zulip.txt","msg":"","result":"success","uri":"/user_uploads/1/4e/m2A3MSqFnWRLUf9SaPzQ0Up_/zulip.txt","url":"/user_uploads/1/4e/m2A3MSqFnWRLUf9SaPzQ0Up_/zulip.txt"}
```
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.