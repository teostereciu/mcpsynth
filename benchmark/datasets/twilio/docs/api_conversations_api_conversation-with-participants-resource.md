# Conversation with Participants Resource

*Source: https://www.twilio.com/docs/conversations/api/conversation-with-participants-resource*

---

# Conversation with Participants Resource

Positive FeedbackNegative Feedback

* * *

The **ConversationWithParticipants** resource accepts all the details for a conversation and allows up to 10 participants in one request. It is especially helpful for situations where you want to send group texts. It helps prevent issues that might occur with existing conversations when you add participants individually.

* * *

## API Base URL

api-base-url page anchor

Positive FeedbackNegative Feedback

All URLs in the reference documentation use the following base URL:

Copy code block


    https://conversations.twilio.com/v1

### Using the shortened base URL

using-the-shortened-base-url page anchor

Positive FeedbackNegative Feedback

Using the REST API, you can create Conversation with Participants in the **default Conversation Service** instance via a "shortened" URL that doesn't include the Conversation Service instance SID (`ISXXX...`). If you are only using one Conversation Service (the default), you don't need to include the Conversation Service SID in your URL, e.g.

Copy code block


    POST /v1/ConversationWithParticipants

For Conversations applications that build on more than one [Conversation Service instance](/docs/conversations/api/service-resource "Conversation Service instance"), you will need to specify the Conversation Service SID in the REST API call:

Copy code block


    POST /v1/Services/ISxx/ConversationWithParticipants

* * *

## ConversationWithParticipant Properties

conversationwithparticipant-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Account](/docs/iam/api/account "Account") responsible for this conversation.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

chatServiceSidSID<IS>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") this conversation belongs to.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

messagingServiceSidSID<MG>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Messaging Service](/docs/messaging/api/service-resource "Messaging Service") this conversation belongs to.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<CH>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource.

Pattern: `^CH[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

friendlyNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The human-readable name of this conversation, limited to 256 characters. Optional.

* * *

uniqueNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL.

* * *

attributesstring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned.

* * *

stateenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Current state of this conversation. Can be either `initializing`, `active`, `inactive` or `closed` and defaults to `active`

Possible values:

`initializing``inactive``active``closed`

* * *

dateCreatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that this resource was created.

* * *

dateUpdatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that this resource was last updated.

* * *

timers

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Timer date values representing state update for this conversation.

* * *

linksobject<uri-map>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Contains absolute URLs to access the [participants](/docs/conversations/api/conversation-participant-resource "participants"), [messages](/docs/conversations/api/conversation-message-resource "messages") and [webhooks](/docs/conversations/api/conversation-scoped-webhook-resource "webhooks") of this conversation.

* * *

bindingsnull

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An absolute API resource URL for this conversation.

* * *

## Create a Conversation with Participants resource

create-a-conversation-with-participants-resource page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/ConversationWithParticipants`

This resource behaves differently than most other Conversations API resources. Here's how it works:

  1. **Parameter validation** : It validates all conversation and participant parameters and returns various possible conversations errors.
  2. **Conversations are created synchronously** : If the request is valid, a conversation will be created and returned in the response. This conversation will be in the state `initializing` while the participants are added. In this state, the conversation cannot be updated.
  3. **Participants are added to the conversation asynchronously** : Once all participants are added, the conversation state will be set to `active` and the conversation can be used. Listening to the `onConversationStateUpdated` webhook event or polling the conversations `GET` endpoint are both acceptable ways to check if the conversation is ready to be used.
  4. **System Errors** : If any unexpected errors happen while adding the participants, the conversation state will be set to `closed`. You can view the error logs in the [Twilio Console(link takes you to an external page)](https://console.twilio.com/us1/monitor/logs/conversations?frameUrl=%2Fconsole%2Fconversations%2Fdefault%3Fx-target-region%3Dus1 "Twilio Console"), and in your webhook notifications if you subscribe to them.


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

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

friendlyNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The human-readable name of this conversation, limited to 256 characters. Optional.

* * *

uniqueNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL.

* * *

dateCreatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that this resource was created.

* * *

dateUpdatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that this resource was last updated.

* * *

messagingServiceSidSID<MG>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Messaging Service](/docs/messaging/api/service-resource "Messaging Service") this conversation belongs to.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

attributesstring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned.

* * *

stateenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Current state of this conversation. Can be either `initializing`, `active`, `inactive` or `closed` and defaults to `active`

Possible values:

`initializing``inactive``active``closed`

* * *

timers.inactivestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

ISO8601 duration when conversation will be switched to `inactive` state. Minimum value for this timer is 1 minute.

* * *

timers.closedstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

ISO8601 duration when conversation will be switched to `closed` state. Minimum value for this timer is 10 minutes.

* * *

bindings.email.addressstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The default email address that will be used when sending outbound emails in this conversation.

* * *

bindings.email.namestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The default name that will be used when sending outbound emails in this conversation.

* * *

participantarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The participant to be added to the conversation in JSON format. The JSON object attributes are as parameters in [Participant Resource](/docs/conversations/api/conversation-participant-resource "Participant Resource"). The maximum number of participants that can be added in a single request is 10.

Select from available examples

Copy code block


    {


      "FriendlyName": "friendly_name",


      "UniqueName": "unique_name",


      "Attributes": "{ \"topic\": \"feedback\" }",


      "DateCreated": "2015-12-16T22:18:37Z",


      "DateUpdated": "2015-12-16T22:18:38Z",


      "MessagingServiceSid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "State": "inactive",


      "Timers.Inactive": "PT1M",


      "Timers.Closed": "PT10M"


    }

Create Conversation with ParticipantsLink to code sample: Create Conversation with Participants

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

    async function createConversationWithParticipants() {


    11

      const conversationWithParticipant =


    12

        await client.conversations.v1.conversationWithParticipants.create({


    13

          friendlyName: "Friendly Conversation",


    14

          participant: [


    15

            '{"messaging_binding": {"address": "<External Participant Number>", "proxy_address": "<Your Twilio Number>"}}',


    16

            '{"identity": "<Chat User Identity>"}',


    17

          ],


    18

        });


    19




    20

      console.log(conversationWithParticipant.sid);


    21

    }


    22




    23

    createConversationWithParticipants();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

      "friendly_name": "Friendly Conversation",


    7

      "unique_name": "unique_name",


    8

      "attributes": "{ \"topic\": \"feedback\" }",


    9

      "date_created": "2015-12-16T22:18:37Z",


    10

      "date_updated": "2015-12-16T22:18:38Z",


    11

      "state": "inactive",


    12

      "timers": {


    13

        "date_inactive": "2015-12-16T22:19:38Z",


    14

        "date_closed": "2015-12-16T22:28:38Z"


    15

      },


    16

      "bindings": {},


    17

      "links": {


    18

        "participants": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",


    19

        "messages": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages",


    20

        "webhooks": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks"


    21

      },


    22

      "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    23

    }

Create GMMS Conversation with ParticipantsLink to code sample: Create GMMS Conversation with Participants

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

    async function createConversationWithParticipants() {


    11

      const conversationWithParticipant =


    12

        await client.conversations.v1.conversationWithParticipants.create({


    13

          friendlyName: "Friendly Conversation",


    14

          participant: [


    15

            '{"messaging_binding": {"address": "<External Participant Number>"}}',


    16

            '{"messaging_binding": {"address": "<External Participant Number>"}}',


    17

            '{"messaging_binding": {"projected_address": "<Your Twilio Number>"}}',


    18

          ],


    19

        });


    20




    21

      console.log(conversationWithParticipant.sid);


    22

    }


    23




    24

    createConversationWithParticipants();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

      "friendly_name": "Friendly Conversation",


    7

      "unique_name": "unique_name",


    8

      "attributes": "{ \"topic\": \"feedback\" }",


    9

      "date_created": "2015-12-16T22:18:37Z",


    10

      "date_updated": "2015-12-16T22:18:38Z",


    11

      "state": "inactive",


    12

      "timers": {


    13

        "date_inactive": "2015-12-16T22:19:38Z",


    14

        "date_closed": "2015-12-16T22:28:38Z"


    15

      },


    16

      "bindings": {},


    17

      "links": {


    18

        "participants": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",


    19

        "messages": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages",


    20

        "webhooks": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks"


    21

      },


    22

      "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    23

    }