# Service-Scoped Conversation-Scoped Webhook Resource

*Source: https://www.twilio.com/docs/conversations/api/service-scoped-conversation-scoped-webhook-resource*

---

# Service-Scoped Conversation-Scoped Webhook Resource

Positive FeedbackNegative Feedback

* * *

**Service-Scoped Conversation-Scoped Webhooks** provide a way to attach a unique monitor, bot, or other integration to each service-scoped Conversation within a **[non-default Conversation Service](/docs/conversations/api/service-resource "non-default Conversation Service").**

Each individual [service-scoped Conversation](/docs/conversations/api/service-conversation-resource "service-scoped Conversation") can have as many as five such webhooks, as needed for your use case.

Please see the API Reference for the [Conversation-Scoped Webhook](/docs/conversations/api/conversation-scoped-webhook-resource "Conversation-Scoped Webhook") resource for creating and managing Conversation-Scoped Webhooks within the default Conversation Service.

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

## Service-Scoped Conversation-Scoped Webhook Properties

service-scoped-conversation-scoped-webhook-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

sidSID<WH>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource.

Pattern: `^WH[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Account](/docs/iam/api/account "Account") responsible for this conversation.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

chatServiceSidSID<IS>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") the Participant resource is associated with.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

conversationSidSID<CH>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for this webhook.

Pattern: `^CH[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

targetstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The target of this webhook: `webhook`, `studio`, `trigger`

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An absolute API resource URL for this webhook.

* * *

configuration

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The configuration of this webhook. Is defined based on target.

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

## Create a Service-Scoped Conversation-Scoped Webhook resource

create-a-service-scoped-conversation-scoped-webhook-resource page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

chatServiceSidSID<IS>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") the Participant resource is associated with.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

conversationSidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for this webhook.

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

targetenum<string>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The target of this webhook: `webhook`, `studio`, `trigger`

Possible values:

`webhook``trigger``studio`

* * *

configuration.urlstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute url the webhook request should be sent to.

* * *

configuration.methodenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Possible values:

`get``post`

* * *

configuration.filtersarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The list of events, firing webhook event for this Conversation.

* * *

configuration.triggersarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The list of keywords, firing webhook event for this Conversation.

* * *

configuration.flowSidSID<FW>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The studio flow SID, where the webhook should be sent to.

Pattern: `^FW[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

configuration.replayAfterinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The message index for which and it's successors the webhook will be replayed. Not set by default

Copy code block


    {


      "Target": "webhook",


      "Configuration.Url": "https://example.com",


      "Configuration.Method": "get",


      "Configuration.Filters": [


        "onMessageSent",


        "onConversationDestroyed"


      ],


      "Configuration.ReplayAfter": 7


    }

Create a WebhookLink to code sample: Create a Webhook

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

    async function createServiceConversationScopedWebhook() {


    11

      const webhook = await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .conversations("ConversationSid")


    14

        .webhooks.create({ target: "webhook" });


    15




    16

      console.log(webhook.sid);


    17

    }


    18




    19

    createServiceConversationScopedWebhook();

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

      "conversation_sid": "ConversationSid",


    5

      "sid": "WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

      "target": "webhook",


    7

      "configuration": {


    8

        "url": "https://example.com",


    9

        "method": "get",


    10

        "filters": [


    11

          "onMessageSent",


    12

          "onConversationDestroyed"


    13

        ]


    14

      },


    15

      "date_created": "2016-03-24T21:05:50Z",


    16

      "date_updated": "2016-03-24T21:05:50Z",


    17

      "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks/WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    18

    }

* * *

## Fetch a Service-Scoped Conversation-Scoped Webhook resource

fetch-a-service-scoped-conversation-scoped-webhook-resource page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks/{Sid}`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

chatServiceSidSID<IS>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") the Participant resource is associated with.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

conversationSidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for this webhook.

* * *

sidSID<WH>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource.

Pattern: `^WH[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Fetch a WebhookLink to code sample: Fetch a Webhook

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

    async function fetchServiceConversationScopedWebhook() {


    11

      const webhook = await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .conversations("ConversationSid")


    14

        .webhooks("WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    15

        .fetch();


    16




    17

      console.log(webhook.sid);


    18

    }


    19




    20

    fetchServiceConversationScopedWebhook();

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

      "conversation_sid": "ConversationSid",


    5

      "sid": "WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

      "target": "studio",


    7

      "configuration": {


    8

        "flow_sid": "FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    9

      },


    10

      "date_created": "2016-03-24T21:05:50Z",


    11

      "date_updated": "2016-03-24T21:05:50Z",


    12

      "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks/WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    13

    }

* * *

## Read multiple Service-Scoped Conversation-Scoped Webhook resources

read-multiple-service-scoped-conversation-scoped-webhook-resources page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks`

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

chatServiceSidSID<IS>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") the Participant resource is associated with.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

conversationSidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for this webhook.

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

pageSizeinteger<int64>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

How many resources to return in each list page. The default is 5, and the maximum is 5.

Minimum: `1`Maximum: `5`

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

List multiple WebhooksLink to code sample: List multiple Webhooks

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

    async function listServiceConversationScopedWebhook() {


    11

      const webhooks = await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .conversations("ConversationSid")


    14

        .webhooks.list({ limit: 5 });


    15




    16

      webhooks.forEach((w) => console.log(w.sid));


    17

    }


    18




    19

    listServiceConversationScopedWebhook();

### Response

Note about this response

Copy response


    1

    {


    2

      "meta": {


    3

        "page": 0,


    4

        "page_size": 5,


    5

        "first_page_url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks?PageSize=5&Page=0",


    6

        "previous_page_url": null,


    7

        "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks?PageSize=5&Page=0",


    8

        "next_page_url": null,


    9

        "key": "webhooks"


    10

      },


    11

      "webhooks": [


    12

        {


    13

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

          "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    15

          "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    16

          "sid": "WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

          "target": "webhook",


    18

          "configuration": {


    19

            "url": "https://example.com",


    20

            "method": "get",


    21

            "filters": [


    22

              "onMessageSent",


    23

              "onConversationDestroyed"


    24

            ]


    25

          },


    26

          "date_created": "2016-03-24T21:05:50Z",


    27

          "date_updated": "2016-03-24T21:05:50Z",


    28

          "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks/WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    29

        },


    30

        {


    31

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    32

          "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    33

          "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    34

          "sid": "WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    35

          "target": "trigger",


    36

          "configuration": {


    37

            "url": "https://example.com",


    38

            "method": "post",


    39

            "filters": [


    40

              "keyword1",


    41

              "keyword2"


    42

            ]


    43

          },


    44

          "date_created": "2016-03-24T21:05:50Z",


    45

          "date_updated": "2016-03-24T21:05:50Z",


    46

          "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks/WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    47

        },


    48

        {


    49

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    50

          "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    51

          "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    52

          "sid": "WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    53

          "target": "studio",


    54

          "configuration": {


    55

            "flow_sid": "FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    56

          },


    57

          "date_created": "2016-03-24T21:05:50Z",


    58

          "date_updated": "2016-03-24T21:05:50Z",


    59

          "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks/WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    60

        }


    61

      ]


    62

    }

* * *

## Update a Service-Scoped Conversation-Scoped Webhook resources

update-a-service-scoped-conversation-scoped-webhook-resources page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks/{Sid}`

### Path parameters

path-parameters-3 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

chatServiceSidSID<IS>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") the Participant resource is associated with.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

conversationSidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for this webhook.

* * *

sidSID<WH>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource.

Pattern: `^WH[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters-1 page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

configuration.urlstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute url the webhook request should be sent to.

* * *

configuration.methodenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Possible values:

`get``post`

* * *

configuration.filtersarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The list of events, firing webhook event for this Conversation.

* * *

configuration.triggersarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The list of keywords, firing webhook event for this Conversation.

* * *

configuration.flowSidSID<FW>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The studio flow SID, where the webhook should be sent to.

Pattern: `^FW[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Copy code block


    {


      "Configuration.Url": "https://example.com",


      "Configuration.Method": "post",


      "Configuration.Triggers": [


        "keyword1",


        "keyword2"


      ]


    }

Update a WebhookLink to code sample: Update a Webhook

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

    async function updateServiceConversationScopedWebhook() {


    11

      const webhook = await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .conversations("ConversationSid")


    14

        .webhooks("WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    15

        .update({ "configuration.url": "Configuration.Url" });


    16




    17

      console.log(webhook.sid);


    18

    }


    19




    20

    updateServiceConversationScopedWebhook();

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

      "conversation_sid": "ConversationSid",


    5

      "sid": "WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

      "target": "trigger",


    7

      "configuration": {


    8

        "url": "https://example.com",


    9

        "method": "post",


    10

        "filters": [


    11

          "keyword1",


    12

          "keyword2"


    13

        ]


    14

      },


    15

      "date_created": "2016-03-24T21:05:50Z",


    16

      "date_updated": "2016-03-24T21:05:51Z",


    17

      "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks/WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    18

    }

* * *

## Delete a Service-Scoped, Conversation-Scoped Webhook resource

delete-a-service-scoped-conversation-scoped-webhook-resource page anchor

Positive FeedbackNegative Feedback

`DELETE https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Webhooks/{Sid}`

### Path parameters

path-parameters-4 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

chatServiceSidSID<IS>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") the Participant resource is associated with.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

conversationSidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for this webhook.

* * *

sidSID<WH>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource.

Pattern: `^WH[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Delete a WebhookLink to code sample: Delete a Webhook

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

    async function deleteServiceConversationScopedWebhook() {


    11

      await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .conversations("ConversationSid")


    14

        .webhooks("WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    15

        .remove();


    16

    }


    17




    18

    deleteServiceConversationScopedWebhook();