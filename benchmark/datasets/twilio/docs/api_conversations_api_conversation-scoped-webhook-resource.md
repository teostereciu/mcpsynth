# Conversation Scoped Webhook Resource

*Source: https://www.twilio.com/docs/conversations/api/conversation-scoped-webhook-resource*

---

# Conversation Scoped Webhook Resource

Positive FeedbackNegative Feedback

* * *

**Conversation Scoped Webhooks** provide a way to attach a unique monitor, bot, or other integration to each conversation.

Each individual Conversation can have as many as five such webhooks, as needed for your use case. This is your go-to tool for adding integrations with third-party bots or [Twilio Studio](/docs/studio "Twilio Studio").

For bot integrations, in particular, pay specific attention to the `ReplayAfter` parameter to ensure that you don't miss any messages that arrive while you're configuring the integration.

(information)

## Info

Only post-event webhooks are supported by the Conversation-Scoped Webhooks.

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

Using the REST API, you can interact with Conversation Scoped Webhook resources in the **default Conversation Service** instance via a "shortened" URL that does not include the Conversation Service instance SID ("ISXXX..."). If you are only using one Conversation Service (the default), you do not need to include the Conversation Service SID in your URL, e.g.

Copy code block


    1

    GET /v1/Conversations/CHxxx/Webhooks


    2

For Conversations applications that build on more than one Conversation Service instance, you will need to specify the Conversation Service SID in the REST API call:

Copy code block


    GET /v1/Services/ISxx/Conversations/CHxx/Webhooks

* * *

## Webhook Properties

webhook-properties page anchor

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

## Create a ConversationScopedWebhook resource

create-a-conversationscopedwebhook-resource page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Conversations/{ConversationSid}/Webhooks`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

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

CREATE: Attach a new Conversation Scoped WebhookLink to code sample: CREATE: Attach a new Conversation Scoped Webhook

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

    async function createConversationScopedWebhook() {


    11

      const webhook = await client.conversations.v1


    12

        .conversations("ConversationSid")


    13

        .webhooks.create({


    14

          "configuration.filters": ["onMessageAdded", "onConversationRemoved"],


    15

          "configuration.method": "get",


    16

          "configuration.url": "https://example.com",


    17

          target: "webhook",


    18

        });


    19




    20

      console.log(webhook.sid);


    21

    }


    22




    23

    createConversationScopedWebhook();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "conversation_sid": "ConversationSid",


    4

      "sid": "WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "target": "webhook",


    6

      "configuration": {


    7

        "url": "https://example.com",


    8

        "method": "get",


    9

        "filters": [


    10

          "onMessageSent",


    11

          "onConversationDestroyed"


    12

        ]


    13

      },


    14

      "date_created": "2016-03-24T21:05:50Z",


    15

      "date_updated": "2016-03-24T21:05:50Z",


    16

      "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks/WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    17

    }

* * *

## Fetch a ConversationScopedWebhook resource

fetch-a-conversationscopedwebhook-resource page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Conversations/{ConversationSid}/Webhooks/{Sid}`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

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

FETCH: Retrieve a Conversation Scoped WebhookLink to code sample: FETCH: Retrieve a Conversation Scoped Webhook

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

    async function fetchConversationScopedWebhook() {


    11

      const webhook = await client.conversations.v1


    12

        .conversations("ConversationSid")


    13

        .webhooks("WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    14

        .fetch();


    15




    16

      console.log(webhook.sid);


    17

    }


    18




    19

    fetchConversationScopedWebhook();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "conversation_sid": "ConversationSid",


    4

      "sid": "WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "target": "studio",


    6

      "configuration": {


    7

        "flow_sid": "FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    8

      },


    9

      "date_created": "2016-03-24T21:05:50Z",


    10

      "date_updated": "2016-03-24T21:05:50Z",


    11

      "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks/WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    12

    }

* * *

## Read multiple ConversationScopedWebhook resources

read-multiple-conversationscopedwebhook-resources page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Conversations/{ConversationSid}/Webhooks`

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

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

READ: List all Conversation Scoped WebhooksLink to code sample: READ: List all Conversation Scoped Webhooks

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

    async function listConversationScopedWebhook() {


    11

      const webhooks = await client.conversations.v1


    12

        .conversations("ConversationSid")


    13

        .webhooks.list({ limit: 5 });


    14




    15

      webhooks.forEach((w) => console.log(w.sid));


    16

    }


    17




    18

    listConversationScopedWebhook();

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

        "first_page_url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks?PageSize=5&Page=0",


    6

        "previous_page_url": null,


    7

        "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks?PageSize=5&Page=0",


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

          "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    15

          "sid": "WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    16

          "target": "webhook",


    17

          "configuration": {


    18

            "url": "https://example.com",


    19

            "method": "get",


    20

            "filters": [


    21

              "onMessageSent",


    22

              "onConversationDestroyed"


    23

            ]


    24

          },


    25

          "date_created": "2016-03-24T21:05:50Z",


    26

          "date_updated": "2016-03-24T21:05:50Z",


    27

          "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks/WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    28

        },


    29

        {


    30

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    31

          "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    32

          "sid": "WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    33

          "target": "trigger",


    34

          "configuration": {


    35

            "url": "https://example.com",


    36

            "method": "post",


    37

            "filters": [


    38

              "keyword1",


    39

              "keyword2"


    40

            ]


    41

          },


    42

          "date_created": "2016-03-24T21:05:50Z",


    43

          "date_updated": "2016-03-24T21:05:50Z",


    44

          "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks/WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    45

        },


    46

        {


    47

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    48

          "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    49

          "sid": "WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    50

          "target": "studio",


    51

          "configuration": {


    52

            "flow_sid": "FWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    53

          },


    54

          "date_created": "2016-03-24T21:05:50Z",


    55

          "date_updated": "2016-03-24T21:05:50Z",


    56

          "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks/WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    57

        }


    58

      ]


    59

    }

* * *

## Update a ConversationScopedWebhook resource

update-a-conversationscopedwebhook-resource page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Conversations/{ConversationSid}/Webhooks/{Sid}`

### Path parameters

path-parameters-3 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

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

UPDATE: Configure a Conversation Scoped WebhookLink to code sample: UPDATE: Configure a Conversation Scoped Webhook

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

    async function updateConversationScopedWebhook() {


    11

      const webhook = await client.conversations.v1


    12

        .conversations("ConversationSid")


    13

        .webhooks("WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    14

        .update({ "configuration.filters": ["keyword1", "keyword2"] });


    15




    16

      console.log(webhook.configuration);


    17

    }


    18




    19

    updateConversationScopedWebhook();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "conversation_sid": "ConversationSid",


    4

      "sid": "WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "target": "trigger",


    6

      "configuration": {


    7

        "url": "https://example.com",


    8

        "method": "post",


    9

        "filters": [


    10

          "keyword1",


    11

          "keyword2"


    12

        ]


    13

      },


    14

      "date_created": "2016-03-24T21:05:50Z",


    15

      "date_updated": "2016-03-24T21:05:51Z",


    16

      "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Webhooks/WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    17

    }

* * *

## Delete a ConversationScopedWebhook resource

delete-a-conversationscopedwebhook-resource page anchor

Positive FeedbackNegative Feedback

`DELETE https://conversations.twilio.com/v1/Conversations/{ConversationSid}/Webhooks/{Sid}`

### Path parameters

path-parameters-4 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

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

DELETE: Detach a Conversation Scoped WebhookLink to code sample: DELETE: Detach a Conversation Scoped Webhook

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

    async function deleteConversationScopedWebhook() {


    11

      await client.conversations.v1


    12

        .conversations("ConversationSid")


    13

        .webhooks("WHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    14

        .remove();


    15

    }


    16




    17

    deleteConversationScopedWebhook();