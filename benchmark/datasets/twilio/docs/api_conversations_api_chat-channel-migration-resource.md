# Chat Channel Migration Resource

*Source: https://www.twilio.com/docs/conversations/api/chat-channel-migration-resource*

---

# Chat Channel Migration Resource

Positive FeedbackNegative Feedback

* * *

A **Channel** is a Programmable Chat object that is equivalent to a **Conversation** in the Conversations API.

Please see the [Conversation Resource](/docs/conversations/api/conversation-resource "Conversation Resource") for Conversations that are already available to your Conversations application.

Only 'private' type **Channels** are automatically migrated to Conversations. For 'public' type **Channels** , please use this API to migrate them to 'private' type.

* * *

## API Base URL

api-base-url page anchor

Positive FeedbackNegative Feedback

Copy code block


    1

    https://chat.twilio.com/v3


    2

There is only one API endpoint on the v3 Chat API:

Copy code block


    1

    POST /Services/ISxx/Channels/CHxx


    2

* * *

## Channel Properties

channel-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

sidSID<CH>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string that we created to identify the Channel resource.

Pattern: `^CH[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Channel resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

serviceSidSID<IS>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Service](/docs/chat/rest/service-resource "Service") the Channel resource is associated with.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

friendlyNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The string that you assigned to describe the resource.

* * *

uniqueNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL.

* * *

attributesstring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The JSON string that stores application-specific data. If attributes have not been set, `{}` is returned.

* * *

typeenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The visibility of the channel. Can be: `public` or `private`.

Possible values:

`public``private`

* * *

dateCreatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT when the resource was created specified in [ISO 8601(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601") format.

* * *

dateUpdatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT when the resource was last updated specified in [ISO 8601(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601") format.

* * *

createdBystring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The `identity` of the User that created the channel. If the Channel was created by using the API, the value is `system`.

* * *

membersCountinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The number of Members in the Channel.

Default: `0`

* * *

messagesCountinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The number of Messages that have been passed in the Channel.

Default: `0`

* * *

messagingServiceSidSID<MG>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Messaging Service](/docs/messaging/api/service-resource "Messaging Service") this channel belongs to.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute URL of the Channel resource.

* * *

## Update Channel Type

update-channel-type page anchor

Positive FeedbackNegative Feedback

`POST https://chat.twilio.com/v3/Services/{ServiceSid}/Channels/{Sid}`

Use this API to change a Channel's type from `public` to `private`. This makes it available in Conversations.

(information)

## Info

Read [here](/docs/conversations/migrating-chat-conversations#conversations-is-multichannel "here") to determine if you need to include a Messaging Service SID in your request.

### Headers

headers page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

x-Twilio-Webhook-Enabledenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The X-Twilio-Webhook-Enabled HTTP request header

Possible values:

`true``false`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

serviceSidSID<IS>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique SID identifier of the Service.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this Channel.

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

typeenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The visibility of the channel. Can be: `public` or `private`.

Possible values:

`public``private`

* * *

messagingServiceSidSID<MG>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Messaging Service](/docs/messaging/api/service-resource "Messaging Service") this channel belongs to.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Copy code block


    {


      "Type": "private",


      "MessagingServiceSid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    }

Migrate public Channel to ConversationsLink to code sample: Migrate public Channel to Conversations

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

    async function updateChannel() {


    11

      const channel = await client.chat.v3


    12

        .channels("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "Sid")


    13

        .update({


    14

          messagingServiceSid: "MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    15

          type: "private",


    16

        });


    17




    18

      console.log(channel.sid);


    19

    }


    20




    21

    updateChannel();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "Sid",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "messaging_service_sid": "MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    6

      "friendly_name": "friendly_name",


    7

      "unique_name": "unique_name",


    8

      "attributes": "{ \"foo\": \"bar\" }",


    9

      "type": "private",


    10

      "date_created": "2015-12-16T22:18:37Z",


    11

      "date_updated": "2015-12-16T22:18:38Z",


    12

      "created_by": "username",


    13

      "members_count": 0,


    14

      "messages_count": 0,


    15

      "url": "https://chat.twilio.com/v3/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    16

    }