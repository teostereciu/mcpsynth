# Service-Scoped Conversation Resource

*Source: https://www.twilio.com/docs/conversations/api/service-conversation-resource*

---

# Service-Scoped Conversation Resource

Positive FeedbackNegative Feedback

* * *

A **Service-scoped Conversation** is a unique thread of a conversation that is scoped or limited to a specific, **non-default** [Conversation Service](/docs/conversations/api/service-resource "Conversation Service").

Please see the [Conversation Resource](/docs/conversations/api/conversation-resource "Conversation Resource") for Conversations within the default [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") instance.

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

## Service-Scoped Conversation Properties

service-scoped-conversation-properties page anchor

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

`inactive``active``closed``initializing`

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

## Create a Service-Scoped Conversation

create-a-service-scoped-conversation page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Conversations`

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

chatServiceSidSID<IS>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") the Conversation resource is associated with.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

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

stateenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Current state of this conversation. Can be either `initializing`, `active`, `inactive` or `closed` and defaults to `active`

Possible values:

`inactive``active``closed``initializing`

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

Create a ConversationLink to code sample: Create a Conversation

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

    async function createServiceConversation() {


    11

      const conversation = await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .conversations.create();


    14




    15

      console.log(conversation.accountSid);


    16

    }


    17




    18

    createServiceConversation();

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

      "friendly_name": "friendly_name",


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

      "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    18

      "links": {


    19

        "participants": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",


    20

        "messages": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages",


    21

        "webhooks": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks",


    22

        "export": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Export"


    23

      }


    24

    }

* * *

## Fetch a Service-Scoped Conversation

fetch-a-service-scoped-conversation page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Conversations/{Sid}`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

chatServiceSidSID<IS>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") the Conversation resource is associated with.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource. Can also be the `unique_name` of the Conversation.

Fetch a ConversationLink to code sample: Fetch a Conversation

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

    async function fetchServiceConversation() {


    11

      const conversation = await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .conversations("Sid")


    14

        .fetch();


    15




    16

      console.log(conversation.accountSid);


    17

    }


    18




    19

    fetchServiceConversation();

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

      "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    18

      "links": {


    19

        "participants": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",


    20

        "messages": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages",


    21

        "webhooks": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks",


    22

        "export": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Export"


    23

      }


    24

    }

* * *

## Read multiple Service-Scoped Conversation resources

read-multiple-service-scoped-conversation-resources page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Conversations`

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

chatServiceSidSID<IS>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") the Conversation resource is associated with.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

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

`inactive``active``closed``initializing`

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

List multiple ConversationsLink to code sample: List multiple Conversations

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

    async function listServiceConversation() {


    11

      const conversations = await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .conversations.list({ limit: 20 });


    14




    15

      conversations.forEach((c) => console.log(c.accountSid));


    16

    }


    17




    18

    listServiceConversation();

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

          "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    20

          "links": {


    21

            "participants": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",


    22

            "messages": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages",


    23

            "webhooks": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks",


    24

            "export": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Export"


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

        "first_page_url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations?PageSize=50&Page=0",


    32

        "previous_page_url": null,


    33

        "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations?PageSize=50&Page=0",


    34

        "next_page_url": null,


    35

        "key": "conversations"


    36

      }


    37

    }

* * *

## Update a Service-Scoped Conversation resource

update-a-service-scoped-conversation-resource page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Conversations/{Sid}`

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

path-parameters-3 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

chatServiceSidSID<IS>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") the Conversation resource is associated with.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

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

`inactive``active``closed``initializing`

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

Update a ConversationLink to code sample: Update a Conversation

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

    async function updateServiceConversation() {


    11

      const conversation = await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .conversations("Sid")


    14

        .update({ friendlyName: "FriendlyName" });


    15




    16

      console.log(conversation.accountSid);


    17

    }


    18




    19

    updateServiceConversation();

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

      "friendly_name": "FriendlyName",


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

      "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    18

      "links": {


    19

        "participants": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants",


    20

        "messages": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages",


    21

        "webhooks": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks",


    22

        "export": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Export"


    23

      }


    24

    }

* * *

## Delete a Service-Scoped Conversation

delete-a-service-scoped-conversation page anchor

Positive FeedbackNegative Feedback

`DELETE https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Conversations/{Sid}`

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

path-parameters-4 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

chatServiceSidSID<IS>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") the Conversation resource is associated with.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource. Can also be the `unique_name` of the Conversation.

Delete a ConversationLink to code sample: Delete a Conversation

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

    async function deleteServiceConversation() {


    11

      await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .conversations("Sid")


    14

        .remove();


    15

    }


    16




    17

    deleteServiceConversation();