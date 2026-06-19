# Service Binding Resource

*Source: https://www.twilio.com/docs/conversations/api/service-binding-resource*

---

# Service Binding Resource

Positive FeedbackNegative Feedback

* * *

A Binding resource in Twilio Conversations represents a Push notification subscription for a [User](/docs/conversations/api/user-resource "User") within their Service instance. Bindings are unique per Service instance, User identity, device, and notification channel (such as APNS, GCM, FCM).

* * *

## Binding Properties

binding-properties page anchor

Positive FeedbackNegative Feedback

Each Binding resource has the following properties:

Property nameTypeRequiredPIIDescriptionChild properties

sidSID<BS>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource.

Pattern: `^BS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Account](/docs/iam/api/account "Account") responsible for this binding.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

chatServiceSidSID<IS>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") the Binding resource is associated with.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

credentialSidSID<CR>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Credential](/docs/conversations/api/credential-resource "Credential") for the binding. See [push notification configuration](/docs/chat/push-notification-configuration "push notification configuration") for more info.

Pattern: `^CR[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

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

endpointstring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The unique endpoint identifier for the Binding. The format of this value depends on the `binding_type`.

* * *

identitystring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The application-defined string that uniquely identifies the [Conversation User](/docs/conversations/api/user-resource "Conversation User") within the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service"). See [access tokens](/docs/conversations/create-tokens "access tokens") for more info.

* * *

bindingTypeenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The push technology to use for the Binding. Can be: `apn`, `gcm`, `fcm`, or `twilsock`. See [push notification configuration](/docs/chat/push-notification-configuration "push notification configuration") for more info.

Possible values:

`apn``gcm``fcm``twilsock`

* * *

messageTypesarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The [Conversation message types](/docs/chat/push-notification-configuration#push-types "Conversation message types") the binding is subscribed to.

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An absolute API resource URL for this binding.

* * *

## Fetch a ServiceBinding resource

fetch-a-servicebinding-resource page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Bindings/{Sid}`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

chatServiceSidSID<IS>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") the Binding resource is associated with.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<BS>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource.

Pattern: `^BS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Fetch a BindingLink to code sample: Fetch a Binding

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

    async function fetchServiceBinding() {


    11

      const binding = await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .bindings("BSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    14

        .fetch();


    15




    16

      console.log(binding.sid);


    17

    }


    18




    19

    fetchServiceBinding();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "BSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "date_created": "2016-10-21T11:37:03Z",


    6

      "date_updated": "2016-10-21T11:37:03Z",


    7

      "endpoint": "TestUser-endpoint",


    8

      "identity": "TestUser",


    9

      "binding_type": "gcm",


    10

      "credential_sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    11

      "message_types": [


    12

        "removed_from_conversation",


    13

        "new_message",


    14

        "added_to_conversation"


    15

      ],


    16

      "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings/BSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    17

    }

* * *

## Read multiple ServiceBinding resources

read-multiple-servicebinding-resources page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Bindings`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

chatServiceSidSID<IS>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") the Binding resource is associated with.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

bindingTypearray[enum<string>]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The push technology used by the Binding resources to read. Can be: `apn`, `gcm`, `fcm`, or `twilsock`. See [push notification configuration](/docs/chat/push-notification-configuration "push notification configuration") for more info.

Possible values:

`apn``gcm``fcm``twilsock`

* * *

identityarray[string]

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The identity of a [Conversation User](/docs/conversations/api/user-resource "Conversation User") this binding belongs to. See [access tokens](/docs/conversations/create-tokens "access tokens") for more details.

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

List multiple BindingsLink to code sample: List multiple Bindings

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

    async function listServiceBinding() {


    11

      const bindings = await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .bindings.list({ limit: 20 });


    14




    15

      bindings.forEach((b) => console.log(b.sid));


    16

    }


    17




    18

    listServiceBinding();

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

        "page_size": 50,


    5

        "first_page_url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings?PageSize=50&Page=0",


    6

        "previous_page_url": null,


    7

        "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings?PageSize=50&Page=0",


    8

        "next_page_url": null,


    9

        "key": "bindings"


    10

      },


    11

      "bindings": [


    12

        {


    13

          "sid": "BSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    15

          "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    16

          "date_created": "2016-10-21T11:37:03Z",


    17

          "date_updated": "2016-10-21T11:37:03Z",


    18

          "endpoint": "TestUser-endpoint",


    19

          "identity": "TestUser",


    20

          "binding_type": "gcm",


    21

          "credential_sid": "CRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    22

          "message_types": [


    23

            "removed_from_conversation",


    24

            "new_message",


    25

            "added_to_conversation"


    26

          ],


    27

          "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings/BSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    28

        }


    29

      ]


    30

    }

* * *

## Delete a ServiceBinding resource

delete-a-servicebinding-resource page anchor

Positive FeedbackNegative Feedback

`DELETE https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Bindings/{Sid}`

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

chatServiceSidSID<IS>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") to delete the Binding resource from.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<BS>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Binding resource to delete.

Pattern: `^BS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Delete a BindingLink to code sample: Delete a Binding

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

    async function deleteServiceBinding() {


    11

      await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .bindings("BSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    14

        .remove();


    15

    }


    16




    17

    deleteServiceBinding();