# Configuration Resource

*Source: https://www.twilio.com/docs/conversations/api/configuration-resource*

---

# Configuration Resource

Positive FeedbackNegative Feedback

* * *

The Twilio Conversations' Configuration resource represents settings applied at the account level, across all [Conversation Services](/docs/conversations/api/service-resource "Conversation Services").

* * *

## Configuration Properties

configuration-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") responsible for this configuration.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

defaultChatServiceSidSID<IS>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the default [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") used when creating a conversation.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

defaultMessagingServiceSidSID<MG>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the default [Messaging Service](/docs/messaging/api/service-resource "Messaging Service") used when creating a conversation.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

defaultInactiveTimerstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Default ISO8601 duration when conversation will be switched to `inactive` state. Minimum value for this timer is 1 minute.

* * *

defaultClosedTimerstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Default ISO8601 duration when conversation will be switched to `closed` state. Minimum value for this timer is 10 minutes.

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An absolute API resource URL for this global configuration.

* * *

linksobject<uri-map>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Contains absolute API resource URLs to access the webhook and default service configurations.

* * *

## Fetch a Configuration resource

fetch-a-configuration-resource page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Configuration`

Fetch a ConfigurationLink to code sample: Fetch a Configuration

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

    async function fetchConfiguration() {


    11

      const configuration = await client.conversations.v1.configuration().fetch();


    12




    13

      console.log(configuration.accountSid);


    14

    }


    15




    16

    fetchConfiguration();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "default_chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "default_messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "default_inactive_timer": "PT1M",


    6

      "default_closed_timer": "PT10M",


    7

      "url": "https://conversations.twilio.com/v1/Configuration",


    8

      "links": {


    9

        "service": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Configuration",


    10

        "webhooks": "https://conversations.twilio.com/v1/Configuration/Webhooks"


    11

      }


    12

    }

* * *

## Update a Configuration resource

update-a-configuration-resource page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Configuration`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

defaultChatServiceSidSID<IS>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the default [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") to use when creating a conversation.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

defaultMessagingServiceSidSID<MG>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the default [Messaging Service](/docs/messaging/api/service-resource "Messaging Service") to use when creating a conversation.

Pattern: `^MG[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

defaultInactiveTimerstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Default ISO8601 duration when conversation will be switched to `inactive` state. Minimum value for this timer is 1 minute.

* * *

defaultClosedTimerstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Default ISO8601 duration when conversation will be switched to `closed` state. Minimum value for this timer is 10 minutes.

Copy code block


    {


      "DefaultChatServiceSid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "DefaultMessagingServiceSid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "DefaultInactiveTimer": "PT1M",


      "DefaultClosedTimer": "PT10M"


    }

Update a ConfigurationLink to code sample: Update a Configuration

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

    async function updateConfiguration() {


    11

      const configuration = await client.conversations.v1


    12

        .configuration()


    13

        .update({ defaultChatServiceSid: "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" });


    14




    15

      console.log(configuration.accountSid);


    16

    }


    17




    18

    updateConfiguration();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "default_chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "default_messaging_service_sid": "MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "default_inactive_timer": "PT1M",


    6

      "default_closed_timer": "PT10M",


    7

      "url": "https://conversations.twilio.com/v1/Configuration",


    8

      "links": {


    9

        "service": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Configuration",


    10

        "webhooks": "https://conversations.twilio.com/v1/Configuration/Webhooks"


    11

      }


    12

    }