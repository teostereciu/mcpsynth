# Conversation Message Resource

*Source: https://www.twilio.com/docs/conversations/api/conversation-message-resource*

---

# Conversation Message Resource

Positive FeedbackNegative Feedback

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

Using the REST API, you can interact with Conversation Message resources in the **default Conversation Service** instance via a "shortened" URL that does not include the Conversation Service instance SID ("ISXXX..."). If you are only using one Conversation Service (the default), you do not need to include the Conversation Service SID in your URL, e.g.

Copy code block


    1

    GET /v1/Conversations/CHxx/Messages


    2

For Conversations applications that build on more than one Conversation Service instance, you will need to specify the Conversation Service SID in the REST API call:

Copy code block


    GET /v1/Services/ISxx/Conversations/CHxx/Messages

* * *

## Message Properties

message-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Account](/docs/iam/api/account "Account") responsible for this message.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

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

The index of the message within the [Conversation](/docs/conversations/api/conversation-resource "Conversation"). Indices may skip numbers, but will always be in order of when the message was received.

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

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An absolute API resource API URL for this message.

* * *

delivery

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An object that contains the summary of delivery statuses for the message to non-chat participants.

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

## Create a ConversationMessage resource

create-a-conversationmessage-resource page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Conversations/{ConversationSid}/Messages`

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

Create a Conversation MessageLink to code sample: Create a Conversation Message

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

    async function createConversationMessage() {


    11

      const message = await client.conversations.v1


    12

        .conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .messages.create({


    14

          author: "smee",


    15

          body: "Ahoy there!",


    16

        });


    17




    18

      console.log(message.sid);


    19

    }


    20




    21

    createConversationMessage();

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

      "conversation_sid": "CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    5

      "body": "Ahoy there!",


    6

      "media": null,


    7

      "author": "smee",


    8

      "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    9

      "attributes": "{ \"importance\": \"high\" }",


    10

      "date_created": "2015-12-16T22:18:37Z",


    11

      "date_updated": "2015-12-16T22:18:38Z",


    12

      "index": 0,


    13

      "delivery": {


    14

        "total": 2,


    15

        "sent": "all",


    16

        "delivered": "some",


    17

        "read": "some",


    18

        "failed": "none",


    19

        "undelivered": "none"


    20

      },


    21

      "content_sid": null,


    22

      "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    23

      "links": {


    24

        "delivery_receipts": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts",


    25

        "channel_metadata": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelMetadata"


    26

      }


    27

    }

* * *

## Fetch a ConversationMessage resource

fetch-a-conversationmessage-resource page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Conversations/{ConversationSid}/Messages/{Sid}`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

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

Fetch a Conversation MessageLink to code sample: Fetch a Conversation Message

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

    async function fetchConversationMessage() {


    11

      const message = await client.conversations.v1


    12

        .conversations("ConversationSid")


    13

        .messages("IMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    14

        .fetch();


    15




    16

      console.log(message.accountSid);


    17

    }


    18




    19

    fetchConversationMessage();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "IMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "conversation_sid": "ConversationSid",


    5

      "body": "Welcome!",


    6

      "media": null,


    7

      "author": "system",


    8

      "participant_sid": null,


    9

      "attributes": "{ \"importance\": \"high\" }",


    10

      "date_created": "2016-03-24T20:37:57Z",


    11

      "date_updated": "2016-03-24T20:37:57Z",


    12

      "index": 0,


    13

      "delivery": {


    14

        "total": 2,


    15

        "sent": "all",


    16

        "delivered": "some",


    17

        "read": "some",


    18

        "failed": "none",


    19

        "undelivered": "none"


    20

      },


    21

      "content_sid": null,


    22

      "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    23

      "links": {


    24

        "delivery_receipts": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts",


    25

        "channel_metadata": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelMetadata"


    26

      }


    27

    }

* * *

## List all Conversation Message(s)

list-all-conversation-messages page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Conversations/{ConversationSid}/Messages`

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

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

List all Conversation MessagesLink to code sample: List all Conversation Messages

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

    async function listConversationMessage() {


    11

      const messages = await client.conversations.v1


    12

        .conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .messages.list({ limit: 20 });


    14




    15

      messages.forEach((m) => console.log(m.accountSid));


    16

    }


    17




    18

    listConversationMessage();

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

        "first_page_url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages?PageSize=50&Page=0",


    6

        "previous_page_url": null,


    7

        "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages?PageSize=50&Page=0",


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

          "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    16

          "body": "I like pie.",


    17

          "media": null,


    18

          "author": "pie_preferrer",


    19

          "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    20

          "attributes": "{ \"importance\": \"high\" }",


    21

          "date_created": "2016-03-24T20:37:57Z",


    22

          "date_updated": "2016-03-24T20:37:57Z",


    23

          "index": 0,


    24

          "delivery": {


    25

            "total": 2,


    26

            "sent": "all",


    27

            "delivered": "some",


    28

            "read": "some",


    29

            "failed": "none",


    30

            "undelivered": "none"


    31

          },


    32

          "content_sid": null,


    33

          "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    34

          "links": {


    35

            "delivery_receipts": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts",


    36

            "channel_metadata": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelMetadata"


    37

          }


    38

        },


    39

        {


    40

          "sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    41

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    42

          "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    43

          "body": "Cake is my favorite!",


    44

          "media": null,


    45

          "author": "cake_lover",


    46

          "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    47

          "attributes": "{ \"importance\": \"high\" }",


    48

          "date_created": "2016-03-24T20:38:21Z",


    49

          "date_updated": "2016-03-24T20:38:21Z",


    50

          "index": 5,


    51

          "delivery": {


    52

            "total": 2,


    53

            "sent": "all",


    54

            "delivered": "some",


    55

            "read": "some",


    56

            "failed": "none",


    57

            "undelivered": "none"


    58

          },


    59

          "content_sid": null,


    60

          "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    61

          "links": {


    62

            "delivery_receipts": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts",


    63

            "channel_metadata": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelMetadata"


    64

          }


    65

        },


    66

        {


    67

          "sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    68

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    69

          "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    70

          "body": null,


    71

          "media": [


    72

            {


    73

              "sid": "MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    74

              "size": 42056,


    75

              "content_type": "image/jpeg",


    76

              "filename": "car.jpg"


    77

            }


    78

          ],


    79

          "author": "cake_lover",


    80

          "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    81

          "attributes": "{ \"importance\": \"high\" }",


    82

          "date_created": "2016-03-24T20:38:21Z",


    83

          "date_updated": "2016-03-24T20:38:21Z",


    84

          "index": 9,


    85

          "delivery": {


    86

            "total": 2,


    87

            "sent": "all",


    88

            "delivered": "some",


    89

            "read": "some",


    90

            "failed": "none",


    91

            "undelivered": "none"


    92

          },


    93

          "content_sid": null,


    94

          "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    95

          "links": {


    96

            "delivery_receipts": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts",


    97

            "channel_metadata": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelMetadata"


    98

          }


    99

        }


    100

      ]


    101

    }

Fetch the latest Conversation MessageLink to code sample: Fetch the latest Conversation Message

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

    async function listConversationMessage() {


    11

      const messages = await client.conversations.v1


    12

        .conversations("ConversationSid")


    13

        .messages.list({


    14

          order: "desc",


    15

          limit: 20,


    16

        });


    17




    18

      messages.forEach((m) => console.log(m.accountSid));


    19

    }


    20




    21

    listConversationMessage();

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

        "page_size": 2,


    5

        "first_page_url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages?Order=desc&PageSize=2&Page=0",


    6

        "previous_page_url": null,


    7

        "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages?Order=desc&PageSize=2&Page=0",


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

          "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    16

          "body": null,


    17

          "media": [


    18

            {


    19

              "sid": "MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    20

              "size": 42056,


    21

              "content_type": "image/jpeg",


    22

              "filename": "car.jpg"


    23

            }


    24

          ],


    25

          "author": "cake_lover",


    26

          "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    27

          "attributes": "{ \"importance\": \"high\" }",


    28

          "date_created": "2016-03-24T20:38:21Z",


    29

          "date_updated": "2016-03-24T20:38:21Z",


    30

          "index": 9,


    31

          "delivery": {


    32

            "total": 2,


    33

            "sent": "all",


    34

            "delivered": "some",


    35

            "read": "some",


    36

            "failed": "none",


    37

            "undelivered": "none"


    38

          },


    39

          "content_sid": null,


    40

          "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    41

          "links": {


    42

            "delivery_receipts": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts",


    43

            "channel_metadata": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelMetadata"


    44

          }


    45

        }


    46

      ]


    47

    }

* * *

## Update a ConversationMessage resource

update-a-conversationmessage-resource page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Conversations/{ConversationSid}/Messages/{Sid}`

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

Update a Conversation MessageLink to code sample: Update a Conversation Message

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

    async function updateConversationMessage() {


    11

      const message = await client.conversations.v1


    12

        .conversations("ConversationSid")


    13

        .messages("IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    14

        .update({


    15

          author: "regretfulUser",


    16

          body: "I take back what I said",


    17

        });


    18




    19

      console.log(message.accountSid);


    20

    }


    21




    22

    updateConversationMessage();

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

      "conversation_sid": "ConversationSid",


    5

      "body": "I take back what I said",


    6

      "media": null,


    7

      "author": "regretfulUser",


    8

      "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    9

      "attributes": "{ \"importance\": \"high\" }",


    10

      "date_created": "2015-12-16T22:18:37Z",


    11

      "date_updated": "2015-12-16T22:18:38Z",


    12

      "index": 0,


    13

      "delivery": {


    14

        "total": 2,


    15

        "sent": "all",


    16

        "delivered": "some",


    17

        "read": "some",


    18

        "failed": "none",


    19

        "undelivered": "none"


    20

      },


    21

      "content_sid": null,


    22

      "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    23

      "links": {


    24

        "delivery_receipts": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts",


    25

        "channel_metadata": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelMetadata"


    26

      }


    27

    }

* * *

## Delete a ConversationMessage resource

delete-a-conversationmessage-resource page anchor

Positive FeedbackNegative Feedback

`DELETE https://conversations.twilio.com/v1/Conversations/{ConversationSid}/Messages/{Sid}`

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

Delete a Conversation MessageLink to code sample: Delete a Conversation Message

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

    async function deleteConversationMessage() {


    11

      await client.conversations.v1


    12

        .conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .messages("IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    14

        .remove();


    15

    }


    16




    17

    deleteConversationMessage();