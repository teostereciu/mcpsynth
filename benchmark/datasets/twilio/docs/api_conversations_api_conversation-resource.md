# Conversation Resource

*Source: https://www.twilio.com/docs/conversations/api/conversation-resource*

---

# Conversation Resource

Positive FeedbackNegative Feedback

* * *

A **Conversation** is a unique message thread that contains Participants and the Messages they have sent.

(error)

## Don't use Personally Identifiable Information (PII) for the friendlyName field

Avoid using a person's name, home address, email address, phone number, or other PII in the `friendlyName` field. Instead, use a pseudonymized identifier.

You can learn more about how we process your data in our [privacy policy(link takes you to an external page)](https://www.twilio.com/legal/privacy "privacy policy").

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

Using the REST API, you can interact with Conversation resources in the **default Conversation Service** instance via a "shortened" URL that doesn't include the Conversation Service instance SID ("ISXXX..."). If you are only using one Conversation Service (the default), you don't need to include the Conversation Service SID in your URL, e.g.

Copy code block


    1

    GET /v1/Conversations


    2

For Conversations applications that build on more than one Conversation Service instance, you will need to specify the Conversation Service SID in the REST API call:

Copy code block


    GET /v1/Services/ISxx/Conversations

* * *

## Conversation Properties

conversation-properties page anchor

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

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An absolute API resource URL for this conversation.

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

## Create a Conversation resource

create-a-conversation-resource page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Conversations`

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

Create ConversationLink to code sample: Create Conversation

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

    async function createConversation() {


    11

      const conversation = await client.conversations.v1.conversations.create({


    12

        friendlyName: "Friendly Conversation",


    13

      });


    14




    15

      console.log(conversation.sid);


    16

    }


    17




    18

    createConversation();

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

      "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    18

      "links": {


    19

        "participants": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",


    20

        "messages": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages",


    21

        "webhooks": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks",


    22

        "export": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Export"


    23

      }


    24

    }

* * *

## Fetch a Conversation resource

fetch-a-conversation-resource page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Conversations/{Sid}`

You can fetch a Conversation by providing your account credentials and the conversation SID (provided when the Conversation is created).

The most valuable part of the Conversation resource itself is the `attributes` key, which includes metadata attached to the conversation from the moment of its creation.

The other relevant parts of a Conversation include its Participants (the entities who are currently conversing) and the Messages they've sent. Both of these are linked directly from the top-level `url` key.

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource. Can also be the `unique_name` of the Conversation.

Fetch ConversationLink to code sample: Fetch Conversation

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

    async function fetchConversation() {


    11

      const conversation = await client.conversations.v1


    12

        .conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .fetch();


    14




    15

      console.log(conversation.accountSid);


    16

    }


    17




    18

    fetchConversation();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

      "friendly_name": "My First Conversation",


    7

      "unique_name": "first_conversation",


    8

      "attributes": "{ \"topic\": \"feedback\" }",


    9

      "date_created": "2015-12-16T22:18:37Z",


    10

      "date_updated": "2015-12-16T22:18:38Z",


    11

      "state": "active",


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

      "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    18

      "links": {


    19

        "participants": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",


    20

        "messages": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages",


    21

        "webhooks": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks",


    22

        "export": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Export"


    23

      }


    24

    }

* * *

## Read multiple Conversation resources

read-multiple-conversation-resources page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Conversations`

Returns a list of conversations sorted by recent message activity.

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

startDatestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Specifies the beginning of the date range for filtering Conversations based on their creation date. Conversations that were created on or after this date will be included in the results. The date must be in ISO8601 format, specifically starting at the beginning of the specified date (YYYY-MM-DDT00:00:00Z), for precise filtering. This parameter can be combined with other filters. If this filter is used, the returned list is sorted by latest conversation creation date in descending order.

* * *

endDatestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Defines the end of the date range for filtering conversations by their creation date. Only conversations that were created on or before this date will appear in the results. The date must be in ISO8601 format, specifically capturing up to the end of the specified date (YYYY-MM-DDT23:59:59Z), to ensure that conversations from the entire end day are included. This parameter can be combined with other filters. If this filter is used, the returned list is sorted by latest conversation creation date in descending order.

* * *

stateenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

State for sorting and filtering list of Conversations. Can be `active`, `inactive` or `closed`

Possible values:

`initializing``inactive``active``closed`

* * *

pageSizeinteger<int64>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

How many resources to return in each list page. The default is 50, and the maximum is 100.

Minimum: `1`Maximum: `100`

* * *

pageinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The page index. This value is simply for client state.

Minimum: `0`

* * *

pageTokenstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The page token. This is provided by the API.

Read multiple Conversation resourcesLink to code sample: Read multiple Conversation resources

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

    async function listConversation() {


    11

      const conversations = await client.conversations.v1.conversations.list({


    12

        limit: 20,


    13

      });


    14




    15

      conversations.forEach((c) => console.log(c.accountSid));


    16

    }


    17




    18

    listConversation();

### Response

Note about this response

Copy response


    1

    {


    2

      "conversations": [


    3

        {


    4

          "sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

          "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    7

          "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    8

          "friendly_name": "Home Repair Visit",


    9

          "unique_name": null,


    10

          "attributes": "{ \"topic\": \"feedback\" }",


    11

          "date_created": "2015-12-16T22:18:37Z",


    12

          "date_updated": "2015-12-16T22:18:38Z",


    13

          "state": "active",


    14

          "timers": {


    15

            "date_inactive": "2015-12-16T22:19:38Z",


    16

            "date_closed": "2015-12-16T22:28:38Z"


    17

          },


    18

          "bindings": {},


    19

          "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    20

          "links": {


    21

            "participants": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",


    22

            "messages": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages",


    23

            "webhooks": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks",


    24

            "export": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Export"


    25

          }


    26

        }


    27

      ],


    28

      "meta": {


    29

        "page": 0,


    30

        "page_size": 50,


    31

        "first_page_url": "https://conversations.twilio.com/v1/Conversations?PageSize=50&Page=0",


    32

        "previous_page_url": null,


    33

        "url": "https://conversations.twilio.com/v1/Conversations?PageSize=50&Page=0",


    34

        "next_page_url": null,


    35

        "key": "conversations"


    36

      }


    37

    }

* * *

## Update a Conversation resource

update-a-conversation-resource page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Conversations/{Sid}`

The core definition of any Conversation can be modified on the fly. Update a Conversation to attach metadata that you extract on the fly (e.g. "customer-loyalty-status": "gold", or "aml-risk-level": "heightened"), or to correct mistakes.

### Headers

headers-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

x-Twilio-Webhook-Enabledenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The X-Twilio-Webhook-Enabled HTTP request header

Possible values:

`true``false`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource. Can also be the `unique_name` of the Conversation.

### Request body parameters

request-body-parameters-1 page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

friendlyNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The human-readable name of this conversation, limited to 256 characters. Optional.

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

attributesstring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned.

* * *

messagingServiceSidSID<MG>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Messaging Service](/docs/messaging/api/service-resource "Messaging Service") this conversation belongs to.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

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

uniqueNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL.

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

Select from available examples

Copy code block


    {


      "FriendlyName": "friendly_name",


      "UniqueName": "unique_name",


      "Attributes": "{ \"topic\": \"feedback\" }",


      "DateCreated": "2015-12-16T22:18:37Z",


      "DateUpdated": "2015-12-16T22:18:38Z",


      "MessagingServiceSid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",


      "State": "inactive",


      "Timers.Inactive": "PT1M",


      "Timers.Closed": "PT10M"


    }

Update ConversationLink to code sample: Update Conversation

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

    async function updateConversation() {


    11

      const conversation = await client.conversations.v1


    12

        .conversations("Sid")


    13

        .update({ friendlyName: "Important Customer Question" });


    14




    15

      console.log(conversation.friendlyName);


    16

    }


    17




    18

    updateConversation();

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

      "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",


    6

      "friendly_name": "Important Customer Question",


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

      "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    18

      "links": {


    19

        "participants": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",


    20

        "messages": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages",


    21

        "webhooks": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks",


    22

        "export": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Export"


    23

      }


    24

    }

* * *

## Delete a Conversation resource

delete-a-conversation-resource page anchor

Positive FeedbackNegative Feedback

`DELETE https://conversations.twilio.com/v1/Conversations/{Sid}`

### Headers

headers-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

x-Twilio-Webhook-Enabledenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The X-Twilio-Webhook-Enabled HTTP request header

Possible values:

`true``false`

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource. Can also be the `unique_name` of the Conversation.

Delete ConversationLink to code sample: Delete Conversation

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

    async function deleteConversation() {


    11

      await client.conversations.v1


    12

        .conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .remove();


    14

    }


    15




    16

    deleteConversation();