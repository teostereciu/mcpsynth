# Conversation Service Resource

*Source: https://www.twilio.com/docs/conversations/api/service-resource*

---

# Conversation Service Resource

Positive FeedbackNegative Feedback

* * *

A Conversation Service is the top-level container for other resources in the Twilio Conversations REST API. All other Twilio Conversations resources, such as [Conversations](/docs/conversations/api/conversation-message-resource "Conversations"), [Users](/docs/conversations/api/user-resource "Users"), [Messages](/docs/conversations/api/conversation-message-resource "Messages"), [Bindings](/docs/conversations/api/service-binding-resource "Bindings"), and [Credentials](/docs/conversations/api/credential-resource "Credentials") belong to a specific Service.

Services allow you to:

  * Create multiple, distinct environments (such as _dev, stage,_ and _prod_) under a single Twilio account
  * Scope access to resources through both the REST and client APIs
  * Configure different Service instances with specific behaviors


A Service can also send [HTTPS requests](/docs/glossary/what-is-a-webhook "HTTPS requests") (webhooks) to URLs that you define to let you know of specific events. See what events you can subscribe to in our [webhook reference(link takes you to an external page)](https://www.twilio.com/console/conversations/configuration/webhooks "webhook reference").

(error)

## Do not use Personally Identifiable Information (PII) for the friendlyName field

Avoid using a person's name, home address, email, phone number, or other PII in the `friendlyName` field. Use some form of pseudonymized identifier, instead.

You can learn more about how we process your data in our [privacy policy.(link takes you to an external page)](https://www.twilio.com/en-us/legal/privacy "privacy policy.")

* * *

## Service Defaults in the Twilio Console

service-defaults-in-the-twilio-console page anchor

Positive FeedbackNegative Feedback

You can use the REST API to configure your Conversation Service instances. (See the following examples.)

You can also find the default Conversation Service instance under _Defaults_ in the [Conversations Section(link takes you to an external page)](https://twilio.com/console/conversations/configuration/defaults "Conversations Section") of the Twilio Console.

You may have created non-default Conversation Service resources to separate messaging traffic, create development environments, etc. To access any non-default Conversation Service resources, the Service Sid (`ISXXX`) has to be a part of the url, as shown below:

Copy code block


    1

    https://conversations.twilio.com/v1/Services/ISXXX


    2




    3

    https://conversations.twilio.com/v1/Services/ISXXX/Conversations


    4




    5

    https://conversations.twilio.com/v1/Services/ISXXX/Conversations/CHXXX/Participants


    6




    7

    https://conversations.twilio.com/v1/Services/ISXXX/Conversations/CHXXX/Messages

* * *

## Service Properties

service-properties page anchor

Positive FeedbackNegative Feedback

The Service resource contains these properties:

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Account](/docs/iam/api/account "Account") responsible for this service.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<IS>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

friendlyNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The human-readable name of this service, limited to 256 characters. Optional.

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

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An absolute API resource URL for this service.

* * *

linksobject<uri-map>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Contains absolute API resource URLs to access conversations, users, roles, bindings and configuration of this service.

* * *

## Create a Service resource

create-a-service-resource page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Services`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

friendlyNamestring

required

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The human-readable name of this service, limited to 256 characters. Optional.

Copy code block


    {


      "FriendlyName": "friendly_name"


    }

Create a ServiceLink to code sample: Create a Service

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

    async function createService() {


    11

      const service = await client.conversations.v1.services.create({


    12

        friendlyName: "FriendlyName",


    13

      });


    14




    15

      console.log(service.accountSid);


    16

    }


    17




    18

    createService();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "friendly_name": "FriendlyName",


    5

      "date_created": "2015-12-16T22:18:37Z",


    6

      "date_updated": "2015-12-16T22:18:38Z",


    7

      "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    8

      "links": {


    9

        "conversations": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations",


    10

        "users": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Users",


    11

        "roles": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Roles",


    12

        "bindings": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings",


    13

        "configuration": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Configuration",


    14

        "participant_conversations": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ParticipantConversations",


    15

        "conversation_with_participants": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ConversationWithParticipants"


    16

      }


    17

    }

* * *

## Fetch a Service resource

fetch-a-service-resource page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Services/{Sid}`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidSID<IS>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Fetch a ServiceLink to code sample: Fetch a Service

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

    async function fetchService() {


    11

      const service = await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .fetch();


    14




    15

      console.log(service.accountSid);


    16

    }


    17




    18

    fetchService();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "friendly_name": "My First Service",


    5

      "date_created": "2015-12-16T22:18:37Z",


    6

      "date_updated": "2015-12-16T22:18:38Z",


    7

      "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    8

      "links": {


    9

        "conversations": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations",


    10

        "users": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Users",


    11

        "roles": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Roles",


    12

        "bindings": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings",


    13

        "configuration": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Configuration",


    14

        "participant_conversations": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ParticipantConversations",


    15

        "conversation_with_participants": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ConversationWithParticipants"


    16

      }


    17

    }

* * *

## Read multiple Service resources

read-multiple-service-resources page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Services`

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

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

List multiple ServicesLink to code sample: List multiple Services

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

    async function listService() {


    11

      const services = await client.conversations.v1.services.list({ limit: 20 });


    12




    13

      services.forEach((s) => console.log(s.accountSid));


    14

    }


    15




    16

    listService();

### Response

Note about this response

Copy response


    1

    {


    2

      "services": [


    3

        {


    4

          "sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

          "friendly_name": "Home Service",


    7

          "date_created": "2015-12-16T22:18:37Z",


    8

          "date_updated": "2015-12-16T22:18:38Z",


    9

          "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    10

          "links": {


    11

            "conversations": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations",


    12

            "users": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Users",


    13

            "roles": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Roles",


    14

            "bindings": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings",


    15

            "configuration": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Configuration",


    16

            "participant_conversations": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ParticipantConversations",


    17

            "conversation_with_participants": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ConversationWithParticipants"


    18

          }


    19

        }


    20

      ],


    21

      "meta": {


    22

        "page": 0,


    23

        "page_size": 50,


    24

        "first_page_url": "https://conversations.twilio.com/v1/Services?PageSize=50&Page=0",


    25

        "previous_page_url": null,


    26

        "url": "https://conversations.twilio.com/v1/Services?PageSize=50&Page=0",


    27

        "next_page_url": null,


    28

        "key": "services"


    29

      }


    30

    }

* * *

## Delete a Service resource

delete-a-service-resource page anchor

Positive FeedbackNegative Feedback

`DELETE https://conversations.twilio.com/v1/Services/{Sid}`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidSID<IS>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Delete a ServiceLink to code sample: Delete a Service

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

    async function deleteService() {


    11

      await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .remove();


    14

    }


    15




    16

    deleteService();