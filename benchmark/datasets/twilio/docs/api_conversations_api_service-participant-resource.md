# Service-Scoped Conversation Participant Resource

*Source: https://www.twilio.com/docs/conversations/api/service-participant-resource*

---

# Service-Scoped Conversation Participant Resource

Positive FeedbackNegative Feedback

* * *

Each service-scoped **Participant** in a Conversation represents one real (probably human) participant in a non-default, service-scoped [Conversation](/docs/conversations/api/service-conversation-resource "Conversation").

* * *

## API Base URL

api-base-url page anchor

Positive FeedbackNegative Feedback

All URLs in the reference documentation use the following base URL:

Copy code block


    1

    https://conversations.twilio.com/v1


    2

For Conversations applications that build on more than one Conversation Service instance, you will need to specify the Conversation Service SID (`ISxx`) and the Conversation SID (`CHxx`) in the REST API call:

Copy code block


    1

    GET /v1/Services/ISxx/Conversations/CHxx/Messages


    2

* * *

## Service-Scoped Conversation Participant Properties

service-scoped-conversation-participant-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Account](/docs/iam/api/account "Account") responsible for this participant.

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

A unique string identifier for the conversation participant as [Conversation User](/docs/conversations/api/user-resource "Conversation User"). This parameter is non-null if (and only if) the participant is using the [Conversation SDK](/docs/conversations/sdk-overview "Conversation SDK") to communicate. Limited to 256 characters.

* * *

attributesstring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified. **Note** that if the attributes are not set `{}` will be returned.

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

The date on which this resource was created.

* * *

dateUpdatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date on which this resource was last updated.

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

## Create a Service-Scoped Participant resource

create-a-service-scoped-participant-resource page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants`

Creating a Participant joins them to the Conversation, and the connected person will receive all subsequent messages.

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

A unique string identifier for the conversation participant as [Conversation User](/docs/conversations/api/user-resource "Conversation User"). This parameter is non-null if (and only if) the participant is using the [Conversation SDK](/docs/conversations/sdk-overview "Conversation SDK") to communicate. Limited to 256 characters.

* * *

messagingBinding.addressstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The address of the participant's device, e.g. a phone or WhatsApp number. Together with the Proxy address, this determines a participant uniquely. This field (with `proxy_address`) is only null when the participant is interacting from an SDK endpoint (see the `identity` field).

* * *

messagingBinding.proxyAddressstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The address of the Twilio phone number (or WhatsApp number) that the participant is in contact with. This field, together with participant address, is only null when the participant is interacting from an SDK endpoint (see the `identity` field).

* * *

dateCreatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date on which this resource was created.

* * *

dateUpdatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date on which this resource was last updated.

* * *

attributesstring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified. **Note** that if the attributes are not set `{}` will be returned.

* * *

messagingBinding.projectedAddressstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The address of the Twilio phone number that is used in Group MMS.

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

Create a ParticipantLink to code sample: Create a Participant

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

    async function createServiceConversationParticipant() {


    11

      const participant = await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .conversations("ConversationSid")


    14

        .participants.create();


    15




    16

      console.log(participant.accountSid);


    17

    }


    18




    19

    createServiceConversationParticipant();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "conversation_sid": "ConversationSid",


    5

      "sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

      "identity": "null",


    7

      "attributes": "{ \"role\": \"driver\" }",


    8

      "messaging_binding": {


    9

        "type": "sms",


    10

        "address": "+15558675310",


    11

        "proxy_address": "+15017122661"


    12

      },


    13

      "role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

      "date_created": "2015-12-16T22:18:37Z",


    15

      "date_updated": "2015-12-16T22:18:38Z",


    16

      "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

      "last_read_message_index": null,


    18

      "last_read_timestamp": null


    19

    }

* * *

## Fetch a Service-Scoped Participant resource

fetch-a-service-scoped-participant-resource page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants/{Sid}`

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

The unique ID of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for this participant.

* * *

sidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource. Alternatively, you can pass a Participant's `identity` rather than the SID.

Fetch a Service-Scoped Participant resource by SIDLink to code sample: Fetch a Service-Scoped Participant resource by SID

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

    async function fetchServiceConversationParticipant() {


    11

      const participant = await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .conversations("ConversationSid")


    14

        .participants("Sid")


    15

        .fetch();


    16




    17

      console.log(participant.accountSid);


    18

    }


    19




    20

    fetchServiceConversationParticipant();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "conversation_sid": "ConversationSid",


    5

      "sid": "Sid",


    6

      "identity": null,


    7

      "attributes": "{ \"role\": \"driver\" }",


    8

      "messaging_binding": {


    9

        "type": "sms",


    10

        "address": "+15558675310",


    11

        "proxy_address": "+15017122661"


    12

      },


    13

      "role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

      "date_created": "2016-03-24T21:05:50Z",


    15

      "date_updated": "2016-03-24T21:05:50Z",


    16

      "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

      "last_read_message_index": null,


    18

      "last_read_timestamp": null


    19

    }

You can also fetch a Service-Scoped Conversation Participant by their `identity`. Pass their `identity` as the value for the `sid` argument.

Fetch a Service-Scoped Participant resource by identityLink to code sample: Fetch a Service-Scoped Participant resource by identity

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

    async function fetchServiceConversationParticipant() {


    11

      const participant = await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .conversations("ConversationSid")


    14

        .participants("alice")


    15

        .fetch();


    16




    17

      console.log(participant.accountSid);


    18

    }


    19




    20

    fetchServiceConversationParticipant();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "conversation_sid": "ConversationSid",


    5

      "sid": "alice",


    6

      "identity": "alice",


    7

      "attributes": "{ \"role\": \"driver\" }",


    8

      "messaging_binding": {


    9

        "type": "sms",


    10

        "address": "+15558675310",


    11

        "proxy_address": "+15017122661"


    12

      },


    13

      "role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

      "date_created": "2016-03-24T21:05:50Z",


    15

      "date_updated": "2016-03-24T21:05:50Z",


    16

      "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

      "last_read_message_index": null,


    18

      "last_read_timestamp": null


    19

    }

* * *

## Read multiple Service-Scoped Participant resources

read-multiple-service-scoped-participant-resources page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants`

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

List multiple ParticipantsLink to code sample: List multiple Participants

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

    async function listServiceConversationParticipant() {


    11

      const participants = await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .conversations("ConversationSid")


    14

        .participants.list({ limit: 20 });


    15




    16

      participants.forEach((p) => console.log(p.accountSid));


    17

    }


    18




    19

    listServiceConversationParticipant();

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

        "first_page_url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants?PageSize=50&Page=0",


    6

        "previous_page_url": null,


    7

        "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants?PageSize=50&Page=0",


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

          "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    15

          "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    16

          "sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

          "identity": null,


    18

          "attributes": "{ \"role\": \"driver\" }",


    19

          "messaging_binding": {


    20

            "type": "sms",


    21

            "address": "+15558675310",


    22

            "proxy_address": "+15017122661"


    23

          },


    24

          "role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    25

          "date_created": "2016-03-24T21:05:50Z",


    26

          "date_updated": "2016-03-24T21:05:50Z",


    27

          "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    28

          "last_read_message_index": null,


    29

          "last_read_timestamp": null


    30

        },


    31

        {


    32

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    33

          "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    34

          "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    35

          "sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    36

          "identity": "IDENTITY",


    37

          "attributes": "{ \"role\": \"driver\" }",


    38

          "messaging_binding": null,


    39

          "role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    40

          "date_created": "2016-03-24T21:05:50Z",


    41

          "date_updated": "2016-03-24T21:05:50Z",


    42

          "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    43

          "last_read_message_index": null,


    44

          "last_read_timestamp": null


    45

        }


    46

      ]


    47

    }

* * *

## Update a Service-Scoped Participant resource

update-a-service-scoped-participant-resource page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants/{Sid}`

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

The date on which this resource was created.

* * *

dateUpdatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date on which this resource was last updated.

* * *

identitystring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

A unique string identifier for the conversation participant as [Conversation User](/docs/conversations/api/user-resource "Conversation User"). This parameter is non-null if (and only if) the participant is using the [Conversation SDK](/docs/conversations/sdk-overview "Conversation SDK") to communicate. Limited to 256 characters.

* * *

attributesstring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified. **Note** that if the attributes are not set `{}` will be returned.

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

Update a ParticipantLink to code sample: Update a Participant

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

    async function updateServiceConversationParticipant() {


    11

      const participant = await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .conversations("ConversationSid")


    14

        .participants("Sid")


    15

        .update({ dateCreated: new Date("2009-07-06 20:30:00") });


    16




    17

      console.log(participant.accountSid);


    18

    }


    19




    20

    updateServiceConversationParticipant();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "conversation_sid": "ConversationSid",


    5

      "sid": "Sid",


    6

      "identity": null,


    7

      "attributes": "{ \"role\": \"driver\" }",


    8

      "messaging_binding": {


    9

        "type": "sms",


    10

        "address": "+15558675310",


    11

        "proxy_address": "+15017122661"


    12

      },


    13

      "role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

      "date_created": "2009-07-06T20:30:00Z",


    15

      "date_updated": "2015-12-16T22:18:38Z",


    16

      "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

      "last_read_message_index": null,


    18

      "last_read_timestamp": null


    19

    }

* * *

## Delete a Service-Scoped Conversation Participant resource

delete-a-service-scoped-conversation-participant-resource page anchor

Positive FeedbackNegative Feedback

`DELETE https://conversations.twilio.com/v1/Services/{ChatServiceSid}/Conversations/{ConversationSid}/Participants/{Sid}`

Deleting a participant removes them from the Conversation; they will receive no new messages after that point.

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

The unique ID of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") for this participant.

* * *

sidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this resource.

Delete a ParticipantLink to code sample: Delete a Participant

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

    async function deleteServiceConversationParticipant() {


    11

      await client.conversations.v1


    12

        .services("ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .conversations("ConversationSid")


    14

        .participants("Sid")


    15

        .remove();


    16

    }


    17




    18

    deleteServiceConversationParticipant();