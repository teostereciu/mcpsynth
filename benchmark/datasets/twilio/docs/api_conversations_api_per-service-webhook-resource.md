# Per-Service Webhook Resource

*Source: https://www.twilio.com/docs/conversations/api/per-service-webhook-resource*

---

# Per-Service Webhook Resource

Positive FeedbackNegative Feedback

* * *

The Per-Service Webhook resource allows you to control the effects of webhooks in a particular [Conversation Service](/docs/conversations/api/service-resource "Conversation Service"). The webhooks will only fire for activity at the service-level.

Services allow you to:

  * Create multiple, distinct environments (such as dev, stage, and prod) under a single Twilio account
  * Scope access to resources through both the REST and client APIs
  * Configure different service instances with specific behaviors


Every service can have unique webhook targets. This means you can include different metadata in the URLs or even trigger different behavior for different services.

Webhook targets for the Service Instance (the URL that Twilio will invoke) are configured in the Twilio Console.

If configured, service-scoped webhooks will override your global webhook settings such that only the service-scoped hooks will fire. This applies only to the services where service-level hooks are configured. See [Conversations Webhooks](/docs/conversations/conversations-webhooks "Conversations Webhooks")for more information.

* * *

## Webhook Properties

webhook-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Account](/docs/iam/api/account "Account") responsible for this service.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

chatServiceSidSID<IS>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") this conversation belongs to.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

preWebhookUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute url the pre-event webhook request should be sent to.

* * *

postWebhookUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute url the post-event webhook request should be sent to.

* * *

filtersarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The list of events that your configured webhook targets will receive. Events not configured here will not fire. Possible values are `onParticipantAdd`, `onParticipantAdded`, `onDeliveryUpdated`, `onConversationUpdated`, `onConversationRemove`, `onParticipantRemove`, `onConversationUpdate`, `onMessageAdd`, `onMessageRemoved`, `onParticipantUpdated`, `onConversationAdded`, `onMessageAdded`, `onConversationAdd`, `onConversationRemoved`, `onParticipantUpdate`, `onMessageRemove`, `onMessageUpdated`, `onParticipantRemoved`, `onMessageUpdate` or `onConversationStateUpdated`.

* * *

methodenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method to be used when sending a webhook request. One of `GET` or `POST`.

Possible values:

`GET``POST`

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An absolute API resource URL for this webhook.

* * *

## Fetch a ServiceWebhookConfiguration resource

fetch-a-servicewebhookconfiguration-resource page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Configuration/Webhooks`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

chatServiceSidSID<IS>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") this conversation belongs to.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Fetch a Service WebhookLink to code sample: Fetch a Service Webhook

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

    async function fetchServiceWebhookConfiguration() {


    11

      const webhook = await client.conversations.v1


    12

        .services("ISXXXXXXXXXXXXXXXXXXXXXX")


    13

        .configuration.webhooks()


    14

        .fetch();


    15




    16

      console.log(webhook.accountSid);


    17

    }


    18




    19

    fetchServiceWebhookConfiguration();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "chat_service_sid": "ISXXXXXXXXXXXXXXXXXXXXXX",


    4

      "pre_webhook_url": "https://www.example.com/pre",


    5

      "post_webhook_url": "https://www.example.com/post",


    6

      "filters": [


    7

        "onMessageRemove",


    8

        "onParticipantAdd"


    9

      ],


    10

      "method": "POST",


    11

      "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Configuration/Webhooks"


    12

    }

* * *

## Update a ServiceWebhookConfiguration resource

update-a-servicewebhookconfiguration-resource page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Configuration/Webhooks`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

chatServiceSidSID<IS>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") this conversation belongs to.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

preWebhookUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute url the pre-event webhook request should be sent to.

* * *

postWebhookUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute url the post-event webhook request should be sent to.

* * *

filtersarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The list of events that your configured webhook targets will receive. Events not configured here will not fire. Possible values are `onParticipantAdd`, `onParticipantAdded`, `onDeliveryUpdated`, `onConversationUpdated`, `onConversationRemove`, `onParticipantRemove`, `onConversationUpdate`, `onMessageAdd`, `onMessageRemoved`, `onParticipantUpdated`, `onConversationAdded`, `onMessageAdded`, `onConversationAdd`, `onConversationRemoved`, `onParticipantUpdate`, `onMessageRemove`, `onMessageUpdated`, `onParticipantRemoved`, `onMessageUpdate` or `onConversationStateUpdated`.

* * *

methodstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method to be used when sending a webhook request. One of `GET` or `POST`.

Copy code block


    {


      "PreWebhookUrl": "https://www.example.com/pre",


      "PostWebhookUrl": "https://www.example.com/post",


      "Filters": [


        "onMessageRemoved",


        "onParticipantAdded"


      ],


      "Method": "GET"


    }

Update a Service WebhookLink to code sample: Update a Service Webhook

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

    async function updateServiceWebhookConfiguration() {


    11

      const webhook = await client.conversations.v1


    12

        .services("ISXXXXXXXXXXXXXXXXXXXXXX")


    13

        .configuration.webhooks()


    14

        .update({


    15

          filters: ["onConversationUpdated", "onMessageRemoved"],


    16

          method: "POST",


    17

          postWebhookUrl: "https://example.com/archive-every-action",


    18

          preWebhookUrl: "https://example.com/filtering-and-permissions",


    19

        });


    20




    21

      console.log(webhook.accountSid);


    22

    }


    23




    24

    updateServiceWebhookConfiguration();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "chat_service_sid": "ISXXXXXXXXXXXXXXXXXXXXXX",


    4

      "pre_webhook_url": "https://example.com/filtering-and-permissions",


    5

      "post_webhook_url": "https://example.com/archive-every-action",


    6

      "filters": [


    7

        "onConversationUpdated",


    8

        "onMessageRemoved"


    9

      ],


    10

      "method": "POST",


    11

      "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Configuration/Webhooks"


    12

    }