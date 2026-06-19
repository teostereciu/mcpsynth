# Mobile notifications | Zulip API documentation

*Source: https://zulip.com/api/mobile-notifications*

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

# Mobile notifications
Zulip Server 11.0+ supports end-to-end encryption (E2EE) for mobile
push notifications. Mobile push notifications sent by all Zulip
servers go through Zulip's mobile push notifications service, which
then delivers the notifications through the appropriate
platform-specific push notification service (Google's FCM or Apple's
APNs). E2EE push notifications ensure that mobile notification message
content and metadata is not visible to intermediaries.
Mobile clients that haveregistered an E2EE push
devicewill receive mobile notifications
end-to-end encrypted by their Zulip server.
This page documents the format of the encrypted JSON-format payloads
that the client will receive through this protocol. The same encrypted
payload formats are used for both Firebase Cloud Messaging (FCM) and
Apple Push Notification service (APNs).

## Payload examples

### New channel message
Sample JSON data that gets encrypted:

```
{"channel_id":10,"channel_name":"Denmark","content":"@test_user_group","mentioned_user_group_id":41,"mentioned_user_group_name":"test_user_group","message_id":45,"realm_name":"Zulip Dev","realm_url":"http://zulip.testserver","recipient_type":"channel","sender_avatar_url":"https://secure.gravatar.com/avatar/818c212b9f8830dfef491b3f7da99a14?d=identicon&version=1","sender_full_name":"aaron","sender_id":6,"time":1754385395,"topic":"test","type":"message","user_id":10}
```

```
{"channel_id":10,"channel_name":"Denmark","content":"@test_user_group","mentioned_user_group_id":41,"mentioned_user_group_name":"test_user_group","message_id":45,"realm_name":"Zulip Dev","realm_url":"http://zulip.testserver","recipient_type":"channel","sender_avatar_url":"https://secure.gravatar.com/avatar/818c212b9f8830dfef491b3f7da99a14?d=identicon&version=1","sender_full_name":"aaron","sender_id":6,"time":1754385395,"topic":"test","type":"message","user_id":10}
```
- Thementioned_user_group_idandmentioned_user_group_namefields
  are only present for messages that mention a group containing the
  current user, and triggered a mobile notification because of that
  group mention. For example, messages that mention both the user
  directly and a group containing the user, these fields will not be
  present in the payload, because the direct mention has precedence.
Changes: New in Zulip 11.0 (feature level 413).

### New direct message
Sample JSON data that gets encrypted:

```
{"content":"test content","message_id":46,"realm_name":"Zulip Dev","realm_url":"http://zulip.testserver","recipient_type":"direct","recipient_user_ids":[6,10,12,15],"sender_avatar_url":"https://secure.gravatar.com/avatar/818c212b9f8830dfef491b3f7da99a14?d=identicon&version=1","sender_full_name":"aaron","sender_id":6,"time":1754385290,"type":"message","user_id":10}
```

```
{"content":"test content","message_id":46,"realm_name":"Zulip Dev","realm_url":"http://zulip.testserver","recipient_type":"direct","recipient_user_ids":[6,10,12,15],"sender_avatar_url":"https://secure.gravatar.com/avatar/818c212b9f8830dfef491b3f7da99a14?d=identicon&version=1","sender_full_name":"aaron","sender_id":6,"time":1754385290,"type":"message","user_id":10}
```
- Therecipient_user_idsfield is a sorted array of all user IDs in
the direct message conversation, including bothuser_idandsender_id.
Changes: In Zulip 12.0 (feature level 429), replaced thepm_usersfield withrecipient_user_ids. The oldpm_usersfield
was only present for group DMs, and was a string containing a
comma-separated list of sorted user IDs.
New in Zulip 11.0 (feature level 413).

### Remove notifications
When a batch of messages that had previously been included in mobile
notifications are marked as read, are deleted, become inaccessible, or
otherwise should no longer be displayed to the user, a removal
notification is sent.
Sample JSON data that gets encrypted:

```
{"message_ids":[31,32],"realm_name":"Zulip Dev","realm_url":"http://zulip.testserver","type":"remove","user_id":10}
```

```
{"message_ids":[31,32],"realm_name":"Zulip Dev","realm_url":"http://zulip.testserver","type":"remove","user_id":10}
```
Changes: New in Zulip 11.0 (feature level 413).

### Test push notification
A user can triggersending an E2EE test push notificationto the user's selected mobile device or all of their mobile devices.
Sample JSON data that gets encrypted:

```
{"realm_name":"Zulip Dev","realm_url":"http://zulip.testserver","time":1754577820,"type":"test","user_id":10}
```

```
{"realm_name":"Zulip Dev","realm_url":"http://zulip.testserver","time":1754577820,"type":"test","user_id":10}
```
Changes: New in Zulip 11.0 (feature level 420).

### Data sent to Zulip's push notifications service
Sample JSON data sent by a self-hosted server to the Zulip's push notifications service:

```
{"realm_uuid":"e502dde1-74fc-44b3-9e3a-114c41ed3ea4","push_requests":[{"token_id":"AAAAAAAAAAE=","http_headers":{"apns_priority":10,"apns_push_type":"alert"},"payload":{"push_key_id":10,"encrypted_data":"uOGQ9m8bdnLab/2Qq6WLdJnFUsU/NlX0955rF6GgpiZylQB/HSD+lrHct0KUXdCneu+fnGOuBMAGkYol+SLlbvdsnePn/f6wSvMDbm3iffcgiz2u8TywUlmQL/Q7Ruj5RSpLgEhpFitL/WjwQBtrA31vsqMHycmROju+tOhFlVjmzJmYy3o7ZQDi/YeB2Y+CnA5EuuXjckBYSjL4vi/YaEJXmeHvJ8Pk3T/WwXvo8CFZYlafiqSw0vC/2bkjPTFFAFVo/49nAUI+5Rpa90wJUVChsrkKTclOs4Ih1dNIDYr6+WoIKJTtIR9zgDg3YOkVHBZhlt7Se3i40WAs5JAb1PViMpAp2hbU36z1Qq0g90nmfRjXN9FRdAPaKlbFTT2PkEtS9wVBv9T14ufkhbOwaMLfx5iaHKw3XHoWo7Fe+0IF9ZJ77uhCZoA1kyFKDhl7AZ8K4DOvib8gsfkeAR4XXXnXVmLtAyjBhMrWYNsECo9j4UeE6M90z3xIVR8=","aps":{"mutable-content":1,"alert":{"title":"New notification"}}}},{"token_id":"AAAAAAAAAAI=","fcm_priority":"high","payload":{"push_key_id":20,"encrypted_data":"OzPhtLiyU1U+3ynqyTxkFt83N5GN7t3Uw8/OkCoFKFo/cu3GAzCMMbAAhPghflkrFK37SNOuxpPiL1TzPy5tQJqdSKpQrgu6cp0Y6VVA1aV/zsCDAcSABaWeaOeC5mVL+xFpmFeEbhzUaOLchbRn4kBO4m8gqDU/rAn0cKFY1F7tyCgC+fvvcczP05itDLpkwZMnrADGp3tSHFldr4iGO1pWJxFTXFFhg63UyH1FcMXKFzBPek7hLbpLsqu5OFEQv2TtDbAYdWZr1LXRqnkHTDmMd6NAdkOsVcnk31jHThFPDqaM5zDXb24hGHW79OpBnGAQWydfeChS4pC4yHWCO6ZRDqwvJX9IydS+V7S91KCl0QSToaXvgW7Q3zvHunzu7L/rw0dQQRgPM3qIOHr7gGtptkZpmKuT6icdDGgjRtgP/L0TfxdRKa37fn6nF64+HH60wLPYWOz7vZjgTrA20MrbA3ogMfhFYpwjppidFGVWjrLpk+peQjHB1sY="}}]}
```

```
{"realm_uuid":"e502dde1-74fc-44b3-9e3a-114c41ed3ea4","push_requests":[{"token_id":"AAAAAAAAAAE=","http_headers":{"apns_priority":10,"apns_push_type":"alert"},"payload":{"push_key_id":10,"encrypted_data":"uOGQ9m8bdnLab/2Qq6WLdJnFUsU/NlX0955rF6GgpiZylQB/HSD+lrHct0KUXdCneu+fnGOuBMAGkYol+SLlbvdsnePn/f6wSvMDbm3iffcgiz2u8TywUlmQL/Q7Ruj5RSpLgEhpFitL/WjwQBtrA31vsqMHycmROju+tOhFlVjmzJmYy3o7ZQDi/YeB2Y+CnA5EuuXjckBYSjL4vi/YaEJXmeHvJ8Pk3T/WwXvo8CFZYlafiqSw0vC/2bkjPTFFAFVo/49nAUI+5Rpa90wJUVChsrkKTclOs4Ih1dNIDYr6+WoIKJTtIR9zgDg3YOkVHBZhlt7Se3i40WAs5JAb1PViMpAp2hbU36z1Qq0g90nmfRjXN9FRdAPaKlbFTT2PkEtS9wVBv9T14ufkhbOwaMLfx5iaHKw3XHoWo7Fe+0IF9ZJ77uhCZoA1kyFKDhl7AZ8K4DOvib8gsfkeAR4XXXnXVmLtAyjBhMrWYNsECo9j4UeE6M90z3xIVR8=","aps":{"mutable-content":1,"alert":{"title":"New notification"}}}},{"token_id":"AAAAAAAAAAI=","fcm_priority":"high","payload":{"push_key_id":20,"encrypted_data":"OzPhtLiyU1U+3ynqyTxkFt83N5GN7t3Uw8/OkCoFKFo/cu3GAzCMMbAAhPghflkrFK37SNOuxpPiL1TzPy5tQJqdSKpQrgu6cp0Y6VVA1aV/zsCDAcSABaWeaOeC5mVL+xFpmFeEbhzUaOLchbRn4kBO4m8gqDU/rAn0cKFY1F7tyCgC+fvvcczP05itDLpkwZMnrADGp3tSHFldr4iGO1pWJxFTXFFhg63UyH1FcMXKFzBPek7hLbpLsqu5OFEQv2TtDbAYdWZr1LXRqnkHTDmMd6NAdkOsVcnk31jHThFPDqaM5zDXb24hGHW79OpBnGAQWydfeChS4pC4yHWCO6ZRDqwvJX9IydS+V7S91KCl0QSToaXvgW7Q3zvHunzu7L/rw0dQQRgPM3qIOHr7gGtptkZpmKuT6icdDGgjRtgP/L0TfxdRKa37fn6nF64+HH60wLPYWOz7vZjgTrA20MrbA3ogMfhFYpwjppidFGVWjrLpk+peQjHB1sY="}}]}
```
Changes: In Zulip 12.0 (feature level 468), thedevice_idandpush_account_idfields were replaced withtoken_idandpush_key_idto support the rotation of tokens provided by FCM/APNs and keys used
to encrypt push notifications.
New in Zulip 11.0 (feature level 413).

### Data sent to FCM
Zulip's push notifications service usesFirebase Admin Python SDKto access FCM.
A samplemessagesargument, which is internally used by the SDK to prepare payload for FCM,
passed tofirebase_admin.messaging.send_each:

```
firebase_admin.messaging.send_each
```

```
[firebase_admin.messaging.Message(data={'push_key_id':'20','encrypted_data':'OzPhtLiyU1U+3ynqyTxkFt83N5GN7t3Uw8/OkCoFKFo/cu3GAzCMMbAAhPghflkrFK37SNOuxpPiL1TzPy5tQJqdSKpQrgu6cp0Y6VVA1aV/zsCDAcSABaWeaOeC5mVL+xFpmFeEbhzUaOLchbRn4kBO4m8gqDU/rAn0cKFY1F7tyCgC+fvvcczP05itDLpkwZMnrADGp3tSHFldr4iGO1pWJxFTXFFhg63UyH1FcMXKFzBPek7hLbpLsqu5OFEQv2TtDbAYdWZr1LXRqnkHTDmMd6NAdkOsVcnk31jHThFPDqaM5zDXb24hGHW79OpBnGAQWydfeChS4pC4yHWCO6ZRDqwvJX9IydS+V7S91KCl0QSToaXvgW7Q3zvHunzu7L/rw0dQQRgPM3qIOHr7gGtptkZpmKuT6icdDGgjRtgP/L0TfxdRKa37fn6nF64+HH60wLPYWOz7vZjgTrA20MrbA3ogMfhFYpwjppidFGVWjrLpk+peQjHB1sY=',},token='push-device-token-3',android=firebase_admin.messaging.AndroidConfig(priority='high'),),]
```

```
[firebase_admin.messaging.Message(data={'push_key_id':'20','encrypted_data':'OzPhtLiyU1U+3ynqyTxkFt83N5GN7t3Uw8/OkCoFKFo/cu3GAzCMMbAAhPghflkrFK37SNOuxpPiL1TzPy5tQJqdSKpQrgu6cp0Y6VVA1aV/zsCDAcSABaWeaOeC5mVL+xFpmFeEbhzUaOLchbRn4kBO4m8gqDU/rAn0cKFY1F7tyCgC+fvvcczP05itDLpkwZMnrADGp3tSHFldr4iGO1pWJxFTXFFhg63UyH1FcMXKFzBPek7hLbpLsqu5OFEQv2TtDbAYdWZr1LXRqnkHTDmMd6NAdkOsVcnk31jHThFPDqaM5zDXb24hGHW79OpBnGAQWydfeChS4pC4yHWCO6ZRDqwvJX9IydS+V7S91KCl0QSToaXvgW7Q3zvHunzu7L/rw0dQQRgPM3qIOHr7gGtptkZpmKuT6icdDGgjRtgP/L0TfxdRKa37fn6nF64+HH60wLPYWOz7vZjgTrA20MrbA3ogMfhFYpwjppidFGVWjrLpk+peQjHB1sY=',},token='push-device-token-3',android=firebase_admin.messaging.AndroidConfig(priority='high'),),]
```
Changes: In Zulip 12.0 (feature level 468), thepush_account_idfield was replaced withpush_key_idto support the rotation of
keys used to encrypt push notifications.
New in Zulip 11.0 (feature level 413).

### Data sent to APNs
Zulip's push notifications service usesaioapnsto access APNs.
A samplerequestargument, which is internally used by the library to prepare payload for APNs,
passed toaioapns.APNs.send_notification:

```
aioapns.APNs.send_notification
```

```
aioapns.NotificationRequest(apns_topic='remote_push_device_ios_app_id',device_token='push-device-token-1',message={'push_key_id':10,'encrypted_data':'rUNqoWOB+EQmjThJyXhDptmUrHyzSx4DPlvShzrM7XGdRVMG5qNuH0dnGQDVza9frnWNVOF3vFcuYvDnUnYRBf1j+/n1ML1K2CBnsThCGl3KJNWrKcf5fME7Q1dU2xtJ3+RAKuLtZ9y2gq6DWamui7WfQ75m1eJpYRDbbHIQEiSIZpo7X2Lie3aHkQBgE8SN5MJ6N3VM33DM6i1xGpIeWiFy+hqNloGyEI2qf6xV0SjvvkN+HbGticben4atBkAuAIKi0gIYMPyMihH26T1sEhOH3IDyO3KvaHe1NIdj0naT9RoFkN5UgdxIchXQ7qkVEjivA2E/HefpvZYlhems6TAosfJwgCMB8HuydqdImjixkugRQfugroTTG97p6xQIJSFWCOyrpuBDElI0Ale8XjmzaVo4Dbgqz5kIAhmJWtlwgJw8nt7Orr3EWUVjnIAi0nHCFObAXNShedAbyuLeC1qezqC4FZe/GOLLi4DPWgWSdk8PV5vGw9YC+XcZ38dqQogtpG7dpzMwwsqzLBmlzQ==','aps':{'mutable-content':1,'alert':{'title':'New notification'}}},priority=10,push_type="alert",)
```

```
aioapns.NotificationRequest(apns_topic='remote_push_device_ios_app_id',device_token='push-device-token-1',message={'push_key_id':10,'encrypted_data':'rUNqoWOB+EQmjThJyXhDptmUrHyzSx4DPlvShzrM7XGdRVMG5qNuH0dnGQDVza9frnWNVOF3vFcuYvDnUnYRBf1j+/n1ML1K2CBnsThCGl3KJNWrKcf5fME7Q1dU2xtJ3+RAKuLtZ9y2gq6DWamui7WfQ75m1eJpYRDbbHIQEiSIZpo7X2Lie3aHkQBgE8SN5MJ6N3VM33DM6i1xGpIeWiFy+hqNloGyEI2qf6xV0SjvvkN+HbGticben4atBkAuAIKi0gIYMPyMihH26T1sEhOH3IDyO3KvaHe1NIdj0naT9RoFkN5UgdxIchXQ7qkVEjivA2E/HefpvZYlhems6TAosfJwgCMB8HuydqdImjixkugRQfugroTTG97p6xQIJSFWCOyrpuBDElI0Ale8XjmzaVo4Dbgqz5kIAhmJWtlwgJw8nt7Orr3EWUVjnIAi0nHCFObAXNShedAbyuLeC1qezqC4FZe/GOLLi4DPWgWSdk8PV5vGw9YC+XcZ38dqQogtpG7dpzMwwsqzLBmlzQ==','aps':{'mutable-content':1,'alert':{'title':'New notification'}}},priority=10,push_type="alert",)
```
Changes: In Zulip 12.0 (feature level 468), thepush_account_idfield was replaced withpush_key_idto support the rotation of
keys used to encrypt push notifications.
New in Zulip 11.0 (feature level 413).
Your feedback helps us make Zulip better for everyone! Pleasecontact uswith questions, suggestions, and feature requests.