# Service-Scoped Conversation Message Resource

*Source: https://www.twilio.com/docs/conversations/api/service-conversation-message-resource*

---

# Service-Scoped Conversation Message Resource

Positive FeedbackNegative Feedback

* * *

Use the Service-scoped Conversation Message resource to interact with messages in Conversations that belong to a **non-default,** [service-scoped Conversation](/docs/conversations/api/service-conversation-resource "service-scoped Conversation") resource.

Please see the [Conversation Message Resource API Reference page](/docs/conversations/api/conversation-message-resource "Conversation Message Resource API Reference page") for Messages that belong to Conversations in the default [Conversation Service](/docs/conversations/api/service-resource "Conversation Service").

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

## Service-Scoped Conversation Message Properties

service-scoped-conversation-message-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Account](/docs/iam/api/account "Account") responsible for this message.

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

The unique ID of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for this message.

Pattern: `^CH[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<IM>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource.

Pattern: `^IM[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

indexinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The index of the message within the [Conversation](/docs/conversations/api/conversation-resource "Conversation").

Default: `0`

* * *

authorstring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The channel specific identifier of the message's author. Defaults to `system`.

* * *

bodystring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The content of the message, can be up to 1,600 characters long.

* * *

mediaarray

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

An array of objects that describe the Message's media, if the message contains media. Each object contains these fields: `content_type` with the MIME type of the media, `filename` with the name of the media, `sid` with the SID of the Media resource, and `size` with the media object's file size in bytes. If the Message has no media, this value is `null`.

* * *

attributesstring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned.

* * *

participantSidSID<MB>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of messages's author participant. Null in case of `system` sent message.

Pattern: `^MB[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

dateCreatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that this resource was created.

* * *

dateUpdatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that this resource was last updated. `null` if the message has not been edited.

* * *

delivery

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An object that contains the summary of delivery statuses for the message to non-chat participants.

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An absolute API resource URL for this message.

* * *

linksobject<uri-map>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Contains an absolute API resource URL to access the delivery & read receipts of this message.

* * *

contentSidSID<HX>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the multi-channel [Rich Content](/docs/content "Rich Content") template.

Pattern: `^HX[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

## Create a Service-Scoped Conversation Message resource

create-a-service-scoped-conversation-message-resource page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages`

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

The SID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") the Participant resource is associated with.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

conversationSidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for this message.

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

authorstring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The channel specific identifier of the message's author. Defaults to `system`.

* * *

bodystring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The content of the message, can be up to 1,600 characters long.

* * *

dateCreatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that this resource was created.

* * *

dateUpdatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that this resource was last updated. `null` if the message has not been edited.

* * *

attributesstring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned.

* * *

mediaSidSID<ME>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Media SID to be attached to the new Message.

Pattern: `^ME[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

contentSidSID<HX>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the multi-channel [Rich Content](/docs/content "Rich Content") template, required for template-generated messages. **Note** that if this field is set, `Body` and `MediaSid` parameters are ignored.

Pattern: `^HX[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

contentVariablesstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A structurally valid JSON string that contains values to resolve Rich Content template variables.

* * *

subjectstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The subject of the message, can be up to 256 characters long.

Select from available examples

Copy code block


    {


      "Body": "Hello",


      "Author": "message author",


      "Attributes": "{ \"importance\": \"high\" }",


      "DateCreated": "2015-12-16T22:18:37Z",


      "DateUpdated": "2015-12-16T22:18:38Z"


    }

Create a MessageLink to code sample: Create a Message

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

    async function createServiceConversationMessage() {


    11

      const message = await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .conversations("ConversationSid")


    14

        .messages.create();


    15




    16

      console.log(message.accountSid);


    17

    }


    18




    19

    createServiceConversationMessage();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "conversation_sid": "ConversationSid",


    6

      "body": "Hello",


    7

      "media": null,


    8

      "author": "message author",


    9

      "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    10

      "attributes": "{ \"importance\": \"high\" }",


    11

      "date_created": "2015-12-16T22:18:37Z",


    12

      "date_updated": "2015-12-16T22:18:38Z",


    13

      "index": 0,


    14

      "delivery": {


    15

        "total": 2,


    16

        "sent": "all",


    17

        "delivered": "some",


    18

        "read": "some",


    19

        "failed": "none",


    20

        "undelivered": "none"


    21

      },


    22

      "content_sid": null,


    23

      "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    24

      "links": {


    25

        "delivery_receipts": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts",


    26

        "channel_metadata": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelMetadata"


    27

      }


    28

    }

* * *

## Fetch a Service-Scoped Conversation Message resource

fetch-a-service-scoped-conversation-message-resource page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages/{Sid}`

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

The unique ID of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for this message.

* * *

sidSID<IM>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource.

Pattern: `^IM[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Fetch a MessageLink to code sample: Fetch a Message

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

    async function fetchServiceConversationMessage() {


    11

      const message = await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .conversations("ConversationSid")


    14

        .messages("IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    15

        .fetch();


    16




    17

      console.log(message.accountSid);


    18

    }


    19




    20

    fetchServiceConversationMessage();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "conversation_sid": "ConversationSid",


    6

      "body": "Welcome!",


    7

      "media": null,


    8

      "author": "system",


    9

      "participant_sid": null,


    10

      "attributes": "{ \"importance\": \"high\" }",


    11

      "date_created": "2016-03-24T20:37:57Z",


    12

      "date_updated": "2016-03-24T20:37:57Z",


    13

      "index": 0,


    14

      "delivery": {


    15

        "total": 2,


    16

        "sent": "all",


    17

        "delivered": "some",


    18

        "read": "some",


    19

        "failed": "none",


    20

        "undelivered": "none"


    21

      },


    22

      "content_sid": null,


    23

      "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    24

      "links": {


    25

        "delivery_receipts": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts",


    26

        "channel_metadata": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelMetadata"


    27

      }


    28

    }

* * *

## Read all Service-Scoped Conversation Message resources

read-all-service-scoped-conversation-message-resources page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages`

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

The unique ID of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for messages.

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

orderenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The sort order of the returned messages. Can be: `asc` (ascending) or `desc` (descending), with `asc` as the default.

Possible values:

`asc``desc`

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

List multiple MessagesLink to code sample: List multiple Messages

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

    async function listServiceConversationMessage() {


    11

      const messages = await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .conversations("ConversationSid")


    14

        .messages.list({ limit: 20 });


    15




    16

      messages.forEach((m) => console.log(m.accountSid));


    17

    }


    18




    19

    listServiceConversationMessage();

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

        "first_page_url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages?PageSize=50&Page=0",


    6

        "previous_page_url": null,


    7

        "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages?PageSize=50&Page=0",


    8

        "next_page_url": null,


    9

        "key": "messages"


    10

      },


    11

      "messages": [


    12

        {


    13

          "sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    15

          "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    16

          "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

          "body": "I like pie.",


    18

          "media": null,


    19

          "author": "pie_preferrer",


    20

          "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    21

          "attributes": "{ \"importance\": \"high\" }",


    22

          "date_created": "2016-03-24T20:37:57Z",


    23

          "date_updated": "2016-03-24T20:37:57Z",


    24

          "index": 0,


    25

          "delivery": {


    26

            "total": 2,


    27

            "sent": "all",


    28

            "delivered": "some",


    29

            "read": "some",


    30

            "failed": "none",


    31

            "undelivered": "none"


    32

          },


    33

          "content_sid": null,


    34

          "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    35

          "links": {


    36

            "delivery_receipts": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts",


    37

            "channel_metadata": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelMetadata"


    38

          }


    39

        },


    40

        {


    41

          "sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    42

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    43

          "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    44

          "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    45

          "body": "Cake is my favorite!",


    46

          "media": null,


    47

          "author": "cake_lover",


    48

          "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    49

          "attributes": "{ \"importance\": \"high\" }",


    50

          "date_created": "2016-03-24T20:38:21Z",


    51

          "date_updated": "2016-03-24T20:38:21Z",


    52

          "index": 0,


    53

          "delivery": {


    54

            "total": 2,


    55

            "sent": "all",


    56

            "delivered": "some",


    57

            "read": "some",


    58

            "failed": "none",


    59

            "undelivered": "none"


    60

          },


    61

          "content_sid": null,


    62

          "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    63

          "links": {


    64

            "delivery_receipts": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts",


    65

            "channel_metadata": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelMetadata"


    66

          }


    67

        },


    68

        {


    69

          "sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    70

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    71

          "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    72

          "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    73

          "body": null,


    74

          "media": [


    75

            {


    76

              "sid": "MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    77

              "size": 42056,


    78

              "content_type": "image/jpeg",


    79

              "filename": "car.jpg"


    80

            }


    81

          ],


    82

          "author": "cake_lover",


    83

          "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    84

          "attributes": "{ \"importance\": \"high\" }",


    85

          "date_created": "2016-03-24T20:38:21Z",


    86

          "date_updated": "2016-03-24T20:38:21Z",


    87

          "index": 0,


    88

          "delivery": {


    89

            "total": 2,


    90

            "sent": "all",


    91

            "delivered": "some",


    92

            "read": "some",


    93

            "failed": "none",


    94

            "undelivered": "none"


    95

          },


    96

          "content_sid": null,


    97

          "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    98

          "links": {


    99

            "delivery_receipts": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts",


    100

            "channel_metadata": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelMetadata"


    101

          }


    102

        }


    103

      ]


    104

    }

* * *

## Update a Service-Scoped Conversation Message resource

update-a-service-scoped-conversation-message-resource page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages/{Sid}`

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

The SID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") the Participant resource is associated with.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

conversationSidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for this message.

* * *

sidSID<IM>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource.

Pattern: `^IM[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters-1 page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

authorstring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The channel specific identifier of the message's author. Defaults to `system`.

* * *

bodystring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The content of the message, can be up to 1,600 characters long.

* * *

dateCreatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that this resource was created.

* * *

dateUpdatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that this resource was last updated. `null` if the message has not been edited.

* * *

attributesstring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned.

* * *

subjectstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The subject of the message, can be up to 256 characters long.

Copy code block


    {


      "Body": "Hello",


      "Author": "message author",


      "Attributes": "{ \"importance\": \"high\" }",


      "DateCreated": "2015-12-16T22:18:37Z",


      "DateUpdated": "2015-12-16T22:18:38Z"


    }

Update a MessageLink to code sample: Update a Message

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

    async function updateServiceConversationMessage() {


    11

      const message = await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .conversations("ConversationSid")


    14

        .messages("IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    15

        .update({ author: "Author" });


    16




    17

      console.log(message.accountSid);


    18

    }


    19




    20

    updateServiceConversationMessage();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "conversation_sid": "ConversationSid",


    6

      "body": "Hello",


    7

      "media": null,


    8

      "author": "Author",


    9

      "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    10

      "attributes": "{ \"importance\": \"high\" }",


    11

      "date_created": "2015-12-16T22:18:37Z",


    12

      "date_updated": "2015-12-16T22:18:38Z",


    13

      "index": 0,


    14

      "delivery": {


    15

        "total": 2,


    16

        "sent": "all",


    17

        "delivered": "some",


    18

        "read": "some",


    19

        "failed": "none",


    20

        "undelivered": "none"


    21

      },


    22

      "content_sid": null,


    23

      "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    24

      "links": {


    25

        "delivery_receipts": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts",


    26

        "channel_metadata": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelMetadata"


    27

      }


    28

    }

* * *

## Delete a Service-Scoped Conversation Message resource

delete-a-service-scoped-conversation-message-resource page anchor

Positive FeedbackNegative Feedback

`DELETE https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Messages/{Sid}`

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

The SID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") the Participant resource is associated with.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

conversationSidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for this message.

* * *

sidSID<IM>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource.

Pattern: `^IM[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Delete a MessageLink to code sample: Delete a Message

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

    async function deleteServiceConversationMessage() {


    11

      await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .conversations("ConversationSid")


    14

        .messages("IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    15

        .remove();


    16

    }


    17




    18

    deleteServiceConversationMessage();