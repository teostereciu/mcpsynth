# Service-Scoped Notification Resource

*Source: https://www.twilio.com/docs/conversations/api/service-notification-resource*

---

# Service-Scoped Notification Resource

Positive FeedbackNegative Feedback

* * *

The Twilio Conversations Service Notification resource manages a set of settings to determine [push notification Service Binding](/docs/conversations/api/service-binding-resource "push notification Service Binding") behavior for a specific [Conversation Service](/docs/conversations/api/service-resource "Conversation Service").

* * *

## API Base URL

api-base-url page anchor

Positive FeedbackNegative Feedback

All URLs in the reference documentation use the following base URL:

Copy code block


    1

    https://conversations.twilio.com/v1


    2

For Conversations applications that build on more than one Conversation Service instance, you will need to specify the Conversation Service SID in the REST API call:

Copy code block


    1

    GET /v1/Services/ISxx/Conversations/CHxx/Messages


    2

* * *

## Notification Properties

notification-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Account](/docs/iam/api/account "Account") responsible for this configuration.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

chatServiceSidSID<IS>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") the Configuration applies to.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

newMessage

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Push Notification configuration for New Messages.

* * *

addedToConversation

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Push Notification configuration for being added to a Conversation.

* * *

removedFromConversation

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Push Notification configuration for being removed from a Conversation.

* * *

logEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Weather the notification logging is enabled.

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An absolute API resource URL for this configuration.

* * *

## Fetch a ServiceNotification resource

fetch-a-servicenotification-resource page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Configuration/Notifications`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

chatServiceSidSID<IS>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") the Configuration applies to.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Fetch a NotificationLink to code sample: Fetch a Notification

Report code block

Copy code block


    1

    // Download the helper library from https://www.twilio.com/docs/node/install


    2

    const twilio = require("twilio"); // Or, for ESM: import twilio from "twilio";


    3




    4

    // Find your Account SID and Auth Token at twilio.com/console


    5

    // and set the environment variables. See http://twil.io/secure


    6

    const accountSid = process.env.TWILIO_ACCOUNT_SID;


    7

    const authToken = process.env.TWILIO_AUTH_TOKEN;


    8

    const client = twilio(accountSid, authToken);


    9




    10

    async function fetchServiceNotification() {


    11

      const notification = await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .configuration.notifications()


    14

        .fetch();


    15




    16

      console.log(notification.accountSid);


    17

    }


    18




    19

    fetchServiceNotification();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "log_enabled": false,


    5

      "added_to_conversation": {


    6

        "enabled": true,


    7

        "template": "You have been added to a Conversation: ${CONVERSATION}",


    8

        "sound": "ring"


    9

      },


    10

      "new_message": {


    11

        "enabled": true,


    12

        "template": "You have a new message in ${CONVERSATION} from ${PARTICIPANT}: ${MESSAGE}",


    13

        "badge_count_enabled": false,


    14

        "sound": "ring",


    15

        "with_media": {


    16

          "enabled": false,


    17

          "template": "You have a new message in ${CONVERSATION} with ${MEDIA_COUNT} media files: ${MEDIA}"


    18

        }


    19

      },


    20

      "removed_from_conversation": {


    21

        "enabled": true,


    22

        "template": "You have been removed from a Conversation: ${CONVERSATION}",


    23

        "sound": "ring"


    24

      },


    25

      "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Configuration/Notifications"


    26

    }

* * *

## Update a ServiceNotification resource

update-a-servicenotification-resource page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Configuration/Notifications`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

chatServiceSidSID<IS>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") the Configuration applies to.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

logEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Weather the notification logging is enabled.

* * *

newMessage.enabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to send a notification when a new message is added to a conversation. The default is `false`.

* * *

newMessage.templatestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The template to use to create the notification text displayed when a new message is added to a conversation and `new_message.enabled` is `true`.

* * *

newMessage.soundstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The name of the sound to play when a new message is added to a conversation and `new_message.enabled` is `true`.

* * *

newMessage.badgeCountEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether the new message badge is enabled. The default is `false`.

* * *

addedToConversation.enabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to send a notification when a participant is added to a conversation. The default is `false`.

* * *

addedToConversation.templatestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The template to use to create the notification text displayed when a participant is added to a conversation and `added_to_conversation.enabled` is `true`.

* * *

addedToConversation.soundstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The name of the sound to play when a participant is added to a conversation and `added_to_conversation.enabled` is `true`.

* * *

removedFromConversation.enabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to send a notification to a user when they are removed from a conversation. The default is `false`.

* * *

removedFromConversation.templatestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The template to use to create the notification text displayed to a user when they are removed from a conversation and `removed_from_conversation.enabled` is `true`.

* * *

removedFromConversation.soundstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The name of the sound to play to a user when they are removed from a conversation and `removed_from_conversation.enabled` is `true`.

* * *

newMessage.withMedia.enabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to send a notification when a new message with media/file attachments is added to a conversation. The default is `false`.

* * *

newMessage.withMedia.templatestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The template to use to create the notification text displayed when a new message with media/file attachments is added to a conversation and `new_message.attachments.enabled` is `true`.

Copy code block


    {


      "NewMessage.Enabled": false,


      "NewMessage.Template": "You have a new message in ${CONVERSATION} from ${PARTICIPANT}: ${MESSAGE}",


      "NewMessage.Sound": "ring",


      "NewMessage.BadgeCountEnabled": true,


      "NewMessage.WithMedia.Enabled": false,


      "NewMessage.WithMedia.Template": "You have a new message in ${CONVERSATION} with ${MEDIA_COUNT} media files: ${MEDIA}",


      "AddedToConversation.Enabled": false,


      "AddedToConversation.Template": "You have been added to a Conversation: ${CONVERSATION}",


      "AddedToConversation.Sound": "ring",


      "RemovedFromConversation.Enabled": false,


      "RemovedFromConversation.Template": "You have been removed from a Conversation: ${CONVERSATION}",


      "RemovedFromConversation.Sound": "ring",


      "LogEnabled": true


    }

Update a NotificationLink to code sample: Update a Notification

Report code block

Copy code block


    1

    // Download the helper library from https://www.twilio.com/docs/node/install


    2

    const twilio = require("twilio"); // Or, for ESM: import twilio from "twilio";


    3




    4

    // Find your Account SID and Auth Token at twilio.com/console


    5

    // and set the environment variables. See http://twil.io/secure


    6

    const accountSid = process.env.TWILIO_ACCOUNT_SID;


    7

    const authToken = process.env.TWILIO_AUTH_TOKEN;


    8

    const client = twilio(accountSid, authToken);


    9




    10

    async function updateServiceNotification() {


    11

      const notification = await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .configuration.notifications()


    14

        .update({ logEnabled: false });


    15




    16

      console.log(notification.accountSid);


    17

    }


    18




    19

    updateServiceNotification();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "log_enabled": false,


    5

      "added_to_conversation": {


    6

        "enabled": false,


    7

        "template": "You have been added to a Conversation: ${CONVERSATION}",


    8

        "sound": "ring"


    9

      },


    10

      "new_message": {


    11

        "enabled": false,


    12

        "template": "You have a new message in ${CONVERSATION} from ${PARTICIPANT}: ${MESSAGE}",


    13

        "badge_count_enabled": true,


    14

        "sound": "ring",


    15

        "with_media": {


    16

          "enabled": false,


    17

          "template": "You have a new message in ${CONVERSATION} with ${MEDIA_COUNT} media files: ${MEDIA}"


    18

        }


    19

      },


    20

      "removed_from_conversation": {


    21

        "enabled": false,


    22

        "template": "You have been removed from a Conversation: ${CONVERSATION}",


    23

        "sound": "ring"


    24

      },


    25

      "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Configuration/Notifications"


    26

    }