# Webhook Configuration Resource

*Source: https://www.twilio.com/docs/conversations/api/webhook-configuration-resource*

---

# Webhook Configuration Resource

Positive FeedbackNegative Feedback

* * *

The **Webhook Configuration** resource allows you to precisely control the effects of **account-scoped** webhooks. Sending a `POST` request to the Webhook Configuration endpoint is equivalent to configuring session webhooks in the [Twilio Console(link takes you to an external page)](https://www.twilio.com/console/conversations/configuration/webhooks "Twilio Console").

Good applications of the configured webhooks in Conversations include:

  * Implementing an archival system for all Conversations
  * Feeding messages into Elasticsearch
  * Implementing a profanity filter across all Conversations


**Note:** You can send pre-hooks and post-hooks to different targets.

Our [guide to Conversations Webhooks](/docs/conversations/conversations-webhooks "guide to Conversations Webhooks") includes the specific pre- and post-event webhooks that fire, as well as the webhook payloads.

* * *

## Webhook Properties

webhook-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Account](/docs/iam/api/account "Account") responsible for this conversation.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

methodenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method to be used when sending a webhook request.

Possible values:

`GET``POST`

* * *

filtersarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The list of webhook event triggers that are enabled for this Service: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onMessageAdd`, `onMessageUpdate`, `onMessageRemove`, `onConversationUpdated`, `onConversationRemoved`, `onConversationAdd`, `onConversationAdded`, `onConversationRemove`, `onConversationUpdate`, `onConversationStateUpdated`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`, `onParticipantAdd`, `onParticipantRemove`, `onParticipantUpdate`, `onDeliveryUpdated`, `onUserAdded`, `onUserUpdate`, `onUserUpdated`

* * *

preWebhookUrlstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute url the pre-event webhook request should be sent to.

* * *

postWebhookUrlstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute url the post-event webhook request should be sent to.

* * *

targetenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The routing target of the webhook. Can be ordinary or route internally to Flex

Possible values:

`webhook``flex`

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An absolute API resource API resource URL for this webhook.

* * *

## Fetch a ConfigurationWebhook resource

fetch-a-configurationwebhook-resource page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Configuration/Webhooks`

FETCH: Retrieve a Webhook Configuration ResourceLink to code sample: FETCH: Retrieve a Webhook Configuration Resource

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

    async function fetchConfigurationWebhook() {


    11

      const webhook = await client.conversations.v1.configuration


    12

        .webhooks()


    13

        .fetch();


    14




    15

      console.log(webhook.accountSid);


    16

    }


    17




    18

    fetchConfigurationWebhook();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "pre_webhook_url": "https://example.com/pre",


    4

      "post_webhook_url": "https://example.com/post",


    5

      "method": "GET",


    6

      "filters": [


    7

        "onMessageSend",


    8

        "onConversationUpdated"


    9

      ],


    10

      "target": "webhook",


    11

      "url": "https://conversations.twilio.com/v1/Configuration/Webhooks"


    12

    }

* * *

## Update a ConfigurationWebhook resource

update-a-configurationwebhook-resource page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Configuration/Webhooks`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

methodstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method to be used when sending a webhook request.

* * *

filtersarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The list of webhook event triggers that are enabled for this Service: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onMessageAdd`, `onMessageUpdate`, `onMessageRemove`, `onConversationUpdated`, `onConversationRemoved`, `onConversationAdd`, `onConversationAdded`, `onConversationRemove`, `onConversationUpdate`, `onConversationStateUpdated`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`, `onParticipantAdd`, `onParticipantRemove`, `onParticipantUpdate`, `onDeliveryUpdated`, `onUserAdded`, `onUserUpdate`, `onUserUpdated`

* * *

preWebhookUrlstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute url the pre-event webhook request should be sent to.

* * *

postWebhookUrlstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute url the post-event webhook request should be sent to.

* * *

targetenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The routing target of the webhook. Can be ordinary or route internally to Flex

Possible values:

`webhook``flex`

Copy code block


    {


      "PreWebhookUrl": "https://example.com/pre",


      "PostWebhookUrl": "https://example.com/post",


      "Method": "GET",


      "Filters": [


        "onConversationUpdated"


      ],


      "Target": "webhook"


    }

UPDATE: Enable all Webhooks with filtersLink to code sample: UPDATE: Enable all Webhooks with filters

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

    async function updateConfigurationWebhook() {


    11

      const webhook = await client.conversations.v1.configuration


    12

        .webhooks()


    13

        .update({


    14

          filters: ["onConversationUpdated", "onMessageRemoved"],


    15

          method: "POST",


    16

          postWebhookUrl: "https://example.com/archive-every-action",


    17

          preWebhookUrl: "https://example.com/filtering-and-permissions",


    18

        });


    19




    20

      console.log(webhook.accountSid);


    21

    }


    22




    23

    updateConfigurationWebhook();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "pre_webhook_url": "https://example.com/filtering-and-permissions",


    4

      "post_webhook_url": "https://example.com/archive-every-action",


    5

      "method": "POST",


    6

      "filters": [


    7

        "onConversationUpdated",


    8

        "onMessageRemoved"


    9

      ],


    10

      "target": "webhook",


    11

      "url": "https://conversations.twilio.com/v1/Configuration/Webhooks"


    12

    }