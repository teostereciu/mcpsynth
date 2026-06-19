# Service Configuration Resource

*Source: https://www.twilio.com/docs/conversations/api/service-configuration-resource*

---

# Service Configuration Resource

Positive FeedbackNegative Feedback

* * *

The Configuration Resource represents all of the configuration settings for a Conversation Service, such as the default roles assigned to [Users](/docs/conversations/api/user-resource "Users").

* * *

## Configuration Properties

configuration-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

chatServiceSidSID<IS>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string that we created to identify the Service configuration resource.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

defaultConversationCreatorRoleSidSID<RL>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The conversation-level role assigned to a conversation creator when they join a new conversation. See [Conversation Role](/docs/conversations/api/role-resource "Conversation Role") for more info about roles.

Pattern: `^RL[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

defaultConversationRoleSidSID<RL>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The conversation-level role assigned to users when they are added to a conversation. See [Conversation Role](/docs/conversations/api/role-resource "Conversation Role") for more info about roles.

Pattern: `^RL[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

defaultChatServiceRoleSidSID<RL>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The service-level role assigned to users when they are added to the service. See [Conversation Role](/docs/conversations/api/role-resource "Conversation Role") for more info about roles.

Pattern: `^RL[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An absolute API resource URL for this service configuration.

* * *

linksobject<uri-map>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Contains an absolute API resource URL to access the push notifications configuration of this service.

* * *

reachabilityEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether the [Reachability Indicator](/docs/conversations/reachability "Reachability Indicator") is enabled for this Conversations Service. The default is `false`.

* * *

## Fetch a ServiceConfiguration resource

fetch-a-serviceconfiguration-resource page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Configuration`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

chatServiceSidSID<IS>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Service configuration resource to fetch.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

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

    async function fetchServiceConfiguration() {


    11

      const configuration = await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .configuration()


    14

        .fetch();


    15




    16

      console.log(configuration.chatServiceSid);


    17

    }


    18




    19

    fetchServiceConfiguration();

### Response

Note about this response

Copy response


    1

    {


    2

      "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "default_conversation_creator_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "default_conversation_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "default_chat_service_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

      "reachability_enabled": false,


    7

      "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Configuration",


    8

      "links": {


    9

        "notifications": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Configuration/Notifications",


    10

        "webhooks": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Configuration/Webhooks"


    11

      }


    12

    }

* * *

## Update a ServiceConfiguration resource

update-a-serviceconfiguration-resource page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Configuration`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

chatServiceSidSID<IS>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Service configuration resource to update.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

defaultConversationCreatorRoleSidSID<RL>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The conversation-level role assigned to a conversation creator when they join a new conversation. See [Conversation Role](/docs/conversations/api/role-resource "Conversation Role") for more info about roles.

Pattern: `^RL[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

defaultConversationRoleSidSID<RL>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The conversation-level role assigned to users when they are added to a conversation. See [Conversation Role](/docs/conversations/api/role-resource "Conversation Role") for more info about roles.

Pattern: `^RL[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

defaultChatServiceRoleSidSID<RL>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The service-level role assigned to users when they are added to the service. See [Conversation Role](/docs/conversations/api/role-resource "Conversation Role") for more info about roles.

Pattern: `^RL[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

reachabilityEnabledboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether the [Reachability Indicator](/docs/conversations/reachability "Reachability Indicator") is enabled for this Conversations Service. The default is `false`.

Copy code block


    {


      "DefaultConversationCreatorRoleSid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "DefaultConversationRoleSid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "DefaultChatServiceRoleSid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "ReachabilityEnabled": false


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

    async function updateServiceConfiguration() {


    11

      const configuration = await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .configuration()


    14

        .update({


    15

          defaultConversationCreatorRoleSid: "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    16

        });


    17




    18

      console.log(configuration.chatServiceSid);


    19

    }


    20




    21

    updateServiceConfiguration();

### Response

Note about this response

Copy response


    1

    {


    2

      "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "default_conversation_creator_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "default_conversation_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "default_chat_service_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

      "reachability_enabled": false,


    7

      "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Configuration",


    8

      "links": {


    9

        "notifications": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Configuration/Notifications",


    10

        "webhooks": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Configuration/Webhooks"


    11

      }


    12

    }