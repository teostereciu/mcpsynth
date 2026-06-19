# Conversation Participant Resource

*Source: https://www.twilio.com/docs/conversations/api/conversation-participant-resource*

---

# Conversation Participant Resource

Positive FeedbackNegative Feedback

* * *

Each **Participant** in a Conversation represents one real (probably human) participant in a [Conversation](/docs/conversations/api/conversation-resource "Conversation").

[Creating a Participant](/docs/conversations/api/conversation-participant-resource#add-a-conversation-participant-sms "Creating a Participant") joins them with the conversation, and the connected person will receive all subsequent [messages](/docs/conversations/api/conversation-message-resource "messages").

[Deleting a participant](/docs/conversations/api/conversation-participant-resource#delete-a-conversationparticipant-resource "Deleting a participant") removes them from the conversation. They will receive no new messages after that point, but their previous messages will remain in the conversation.

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

Using the REST API, you can interact with Conversation Participant resources in the **default Conversation Service** instance via a "shortened" URL that does not include the Conversation Service instance SID ("ISXXX..."). If you are only using one Conversation Service (the default), you do not need to include the Conversation Service SID in your URL, e.g.

Copy code block


    1

    GET /v1/Conversations/CHxx/Participants


    2

For Conversations applications that build on more than one Conversation Service instance, you will need to specify the Conversation Service SID in the REST API call:

Copy code block


    GET /v1/Services/ISxx/Conversations/CHxx/Participants

* * *

## Participant Properties

participant-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Account](/docs/iam/api/account "Account") responsible for this participant.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

conversationSidSID<CH>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for this participant.

Pattern: `^CH[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<MB>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource.

Pattern: `^MB[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

identitystring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

A unique string identifier for the conversation participant as [Conversation User](/docs/conversations/api/user-resource "Conversation User"). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.

* * *

attributesstring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned.

* * *

messagingBinding

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

Information about how this participant exchanges messages with the conversation. A JSON parameter consisting of type and address fields of the participant.

* * *

roleSidSID<RL>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of a conversation-level [Role](/docs/conversations/api/role-resource "Role") to assign to the participant.

Pattern: `^RL[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

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

An absolute API resource URL for this participant.

* * *

lastReadMessageIndexinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Index of last “read” message in the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for the Participant.

* * *

lastReadTimestampstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Timestamp of last “read” message in the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for the Participant.

* * *

## Add a Conversation Participant (SMS)

add-a-conversation-participant-sms page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Conversations/{ConversationSid}/Participants`

Adding a new participant to an ongoing conversation immediately allows them to see all subsequent communications. The same person (i.e., a single personal phone number) can be part of any number of conversations concurrently, as long as the address they are in contact with (the `ProxyAddress`) is unique.

To create a Conversation Participant by SMS, you must enter:

  1. Their phone number as the `messagingbinding.address`
  2. Your Twilio number as the `messagingbinding.proxyaddress`.


To create a Conversation Participant by Chat, you must enter the Chat User Identity as the `identity` parameter.
_We recommend following the standard URI specification and avoid the following reserved characters_ `! * ' ( ) ; : @ & = + $ , / ? % # [ ]` _for values such as identity and friendly name._

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

The unique ID of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for this participant.

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

identitystring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

A unique string identifier for the conversation participant as [Conversation User](/docs/conversations/api/user-resource "Conversation User"). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.

* * *

messagingBinding.addressstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The address of the participant's device, e.g. a phone or WhatsApp number. Together with the Proxy address, this determines a participant uniquely. This field (with proxy_address) is only null when the participant is interacting from an SDK endpoint (see the 'identity' field).

* * *

messagingBinding.proxyAddressstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The address of the Twilio phone number (or WhatsApp number) that the participant is in contact with. This field, together with participant address, is only null when the participant is interacting from an SDK endpoint (see the 'identity' field).

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

attributesstring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned.

* * *

messagingBinding.projectedAddressstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The address of the Twilio phone number that is used in Group MMS. Communication mask for the Conversation participant with Identity.

* * *

roleSidSID<RL>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of a conversation-level [Role](/docs/conversations/api/role-resource "Role") to assign to the participant.

Pattern: `^RL[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Select from available examples

Copy code block


    {


      "Attributes": "{ \"role\": \"driver\" }",


      "MessagingBinding.Address": "+15558675310",


      "MessagingBinding.ProxyAddress": "+15017122661",


      "RoleSid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "DateCreated": "2015-12-16T22:18:37Z",


      "DateUpdated": "2015-12-16T22:18:38Z"


    }

Create Conversation Participant (SMS)Link to code sample: Create Conversation Participant (SMS)

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

    async function createConversationParticipant() {


    11

      const participant = await client.conversations.v1


    12

        .conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .participants.create({


    14

          "messagingBinding.address": "+15558675310",


    15

          "messagingBinding.proxyAddress": "<Your Twilio Number>",


    16

        });


    17




    18

      console.log(participant.sid);


    19

    }


    20




    21

    createConversationParticipant();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "conversation_sid": "CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    4

      "sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "identity": null,


    6

      "attributes": "{ \"role\": \"driver\" }",


    7

      "messaging_binding": {


    8

        "type": "sms",


    9

        "address": "+15558675310",


    10

        "proxy_address": "+15017122661"


    11

      },


    12

      "role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    13

      "date_created": "2015-12-16T22:18:37Z",


    14

      "date_updated": "2015-12-16T22:18:38Z",


    15

      "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    16

      "last_read_message_index": null,


    17

      "last_read_timestamp": null


    18

    }

Create Conversation Participant (Chat)Link to code sample: Create Conversation Participant (Chat)

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

    async function createConversationParticipant() {


    11

      const participant = await client.conversations.v1


    12

        .conversations("ConversationSid")


    13

        .participants.create({ identity: "<Chat User Identity>" });


    14




    15

      console.log(participant.sid);


    16

    }


    17




    18

    createConversationParticipant();

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

      "sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "identity": "<Chat User Identity>",


    6

      "attributes": "{ \"role\": \"driver\" }",


    7

      "messaging_binding": null,


    8

      "role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    9

      "date_created": "2015-12-16T22:18:37Z",


    10

      "date_updated": "2015-12-16T22:18:38Z",


    11

      "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    12

      "last_read_message_index": null,


    13

      "last_read_timestamp": null


    14

    }

* * *

## Fetch a ConversationParticipant resource

fetch-a-conversationparticipant-resource page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Conversations/{ConversationSid}/Participants/{Sid}`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

conversationSidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for this participant.

* * *

sidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource. Alternatively, you can pass a Participant's `identity` rather than the SID.

Fetch Conversation Participant by SIDLink to code sample: Fetch Conversation Participant by SID

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

    async function fetchConversationParticipant() {


    11

      const participant = await client.conversations.v1


    12

        .conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .participants("MBXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    14

        .fetch();


    15




    16

      console.log(participant.accountSid);


    17

    }


    18




    19

    fetchConversationParticipant();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "conversation_sid": "CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    4

      "sid": "MBXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    5

      "identity": null,


    6

      "attributes": "{ \"role\": \"driver\" }",


    7

      "messaging_binding": {


    8

        "type": "sms",


    9

        "address": "+15558675310",


    10

        "proxy_address": "+15017122661"


    11

      },


    12

      "role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    13

      "date_created": "2016-03-24T21:05:50Z",


    14

      "date_updated": "2016-03-24T21:05:50Z",


    15

      "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    16

      "last_read_message_index": null,


    17

      "last_read_timestamp": null


    18

    }

You can also fetch a Conversation Participant by their `identity`. Pass their `identity` as the value for the `sid` argument.

Fetch Conversation Participant by identityLink to code sample: Fetch Conversation Participant by identity

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

    async function fetchConversationParticipant() {


    11

      const participant = await client.conversations.v1


    12

        .conversations("ConversationSid")


    13

        .participants("alice")


    14

        .fetch();


    15




    16

      console.log(participant.accountSid);


    17

    }


    18




    19

    fetchConversationParticipant();

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

      "sid": "alice",


    5

      "identity": "alice",


    6

      "attributes": "{ \"role\": \"driver\" }",


    7

      "messaging_binding": {


    8

        "type": "sms",


    9

        "address": "+15558675310",


    10

        "proxy_address": "+15017122661"


    11

      },


    12

      "role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    13

      "date_created": "2016-03-24T21:05:50Z",


    14

      "date_updated": "2016-03-24T21:05:50Z",


    15

      "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    16

      "last_read_message_index": null,


    17

      "last_read_timestamp": null


    18

    }

* * *

## Read multiple ConversationParticipant resources

read-multiple-conversationparticipant-resources page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Conversations/{ConversationSid}/Participants`

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

conversationSidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for participants.

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

List Conversation Participant(s)Link to code sample: List Conversation Participant(s)

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

    async function listConversationParticipant() {


    11

      const participants = await client.conversations.v1


    12

        .conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .participants.list({ limit: 20 });


    14




    15

      participants.forEach((p) => console.log(p.accountSid));


    16

    }


    17




    18

    listConversationParticipant();

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

        "first_page_url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants?PageSize=50&Page=0",


    6

        "previous_page_url": null,


    7

        "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants?PageSize=50&Page=0",


    8

        "next_page_url": null,


    9

        "key": "participants"


    10

      },


    11

      "participants": [


    12

        {


    13

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

          "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    15

          "sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    16

          "identity": null,


    17

          "attributes": "{ \"role\": \"driver\" }",


    18

          "messaging_binding": {


    19

            "type": "sms",


    20

            "address": "+15558675310",


    21

            "proxy_address": "+15017122661"


    22

          },


    23

          "role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    24

          "date_created": "2016-03-24T21:05:50Z",


    25

          "date_updated": "2016-03-24T21:05:50Z",


    26

          "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    27

          "last_read_message_index": null,


    28

          "last_read_timestamp": null


    29

        },


    30

        {


    31

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    32

          "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    33

          "sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    34

          "identity": "IDENTITY",


    35

          "attributes": "{ \"role\": \"driver\" }",


    36

          "messaging_binding": null,


    37

          "role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    38

          "date_created": "2016-03-24T21:05:50Z",


    39

          "date_updated": "2016-03-24T21:05:50Z",


    40

          "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    41

          "last_read_message_index": null,


    42

          "last_read_timestamp": null


    43

        }


    44

      ]


    45

    }

* * *

## Update a ConversationParticipant resource

update-a-conversationparticipant-resource page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Conversations/{ConversationSid}/Participants/{Sid}`

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

The unique ID of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for this participant.

* * *

sidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource.

### Request body parameters

request-body-parameters-1 page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

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

attributesstring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned.

* * *

roleSidSID<RL>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of a conversation-level [Role](/docs/conversations/api/role-resource "Role") to assign to the participant.

Pattern: `^RL[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

messagingBinding.proxyAddressstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The address of the Twilio phone number that the participant is in contact with. 'null' value will remove it.

* * *

messagingBinding.projectedAddressstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The address of the Twilio phone number that is used in Group MMS. 'null' value will remove it.

* * *

identitystring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

A unique string identifier for the conversation participant as [Conversation User](/docs/conversations/api/user-resource "Conversation User"). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.

* * *

lastReadMessageIndexinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Index of last “read” message in the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for the Participant.

* * *

lastReadTimestampstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Timestamp of last “read” message in the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for the Participant.

Select from available examples

Copy code block


    {


      "Attributes": "{ \"role\": \"driver\" }",


      "RoleSid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "DateCreated": "2015-12-16T22:18:37Z",


      "DateUpdated": "2015-12-16T22:18:38Z"


    }

Update Conversation ParticipantLink to code sample: Update Conversation Participant

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

    async function updateConversationParticipant() {


    11

      const participant = await client.conversations.v1


    12

        .conversations("ConversationSid")


    13

        .participants("Sid")


    14

        .update({ dateUpdated: new Date("2019-05-15 13:37:35") });


    15




    16

      console.log(participant.accountSid);


    17

    }


    18




    19

    updateConversationParticipant();

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

      "sid": "Sid",


    5

      "identity": null,


    6

      "attributes": "{ \"role\": \"driver\" }",


    7

      "messaging_binding": {


    8

        "type": "sms",


    9

        "address": "+15558675310",


    10

        "proxy_address": "+15017122661"


    11

      },


    12

      "role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    13

      "date_created": "2015-12-16T22:18:37Z",


    14

      "date_updated": "2019-05-15T13:37:35Z",


    15

      "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    16

      "last_read_message_index": null,


    17

      "last_read_timestamp": null


    18

    }

Update attributes for a Conversation ParticipantLink to code sample: Update attributes for a Conversation Participant

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

    async function updateConversationParticipant() {


    11

      const participant = await client.conversations.v1


    12

        .conversations("ConversationSid")


    13

        .participants("Sid")


    14

        .update({ attributes: JSON.stringify({ role: "driver" }) });


    15




    16

      console.log(participant.accountSid);


    17

    }


    18




    19

    updateConversationParticipant();

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

      "sid": "Sid",


    5

      "identity": null,


    6

      "attributes": "{\"role\": \"driver\"}",


    7

      "messaging_binding": {


    8

        "type": "sms",


    9

        "address": "+15558675310",


    10

        "proxy_address": "+15017122661"


    11

      },


    12

      "role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    13

      "date_created": "2015-12-16T22:18:37Z",


    14

      "date_updated": "2015-12-16T22:18:38Z",


    15

      "url": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    16

      "last_read_message_index": null,


    17

      "last_read_timestamp": null


    18

    }

* * *

## Delete a ConversationParticipant resource

delete-a-conversationparticipant-resource page anchor

Positive FeedbackNegative Feedback

`DELETE https://conversations.twilio.com/v1/Conversations/{ConversationSid}/Participants/{Sid}`

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

The unique ID of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for this participant.

* * *

sidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource.

Delete Conversation ParticipantLink to code sample: Delete Conversation Participant

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

    async function deleteConversationParticipant() {


    11

      await client.conversations.v1


    12

        .conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    13

        .participants("MBXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


    14

        .remove();


    15

    }


    16




    17

    deleteConversationParticipant();