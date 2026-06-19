# Participant Conversation Resource

*Source: https://www.twilio.com/docs/conversations/api/participant-conversation-resource*

---

# Participant Conversation Resource

Positive FeedbackNegative Feedback

* * *

The ParticipantConversation resource lists all the Conversations for a specific participant. It performs the lookup using an exact match to the participant identifier.
This resource supports the lookup of conversations for a specific participant based on two types of query parameters:

  * Identity: for Chat users,
  * Address: for non-Chat members, e.g., SMS or WhatsApp addresses.


Users can provide only one parameter at a time, i.e. either `identity` or `address`. The returned data will be sorted by the `conversationSid` alphabetically.

* * *

## ParticipantConversation Properties

participantconversation-properties page anchor

Positive FeedbackNegative Feedback

Each Participant Conversation resource contains these properties.

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Account](/docs/iam/api/account "Account") responsible for this conversation.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

chatServiceSidSID<IS>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") this conversation belongs to.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

participantSidSID<MB>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Participant](/docs/conversations/api/conversation-participant-resource "Participant").

Pattern: `^MB[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

participantUserSidSID<US>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string that identifies the conversation participant as [Conversation User](/docs/conversations/api/user-resource "Conversation User").

Pattern: `^US[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

participantIdentitystring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

A unique string identifier for the conversation participant as [Conversation User](/docs/conversations/api/user-resource "Conversation User"). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.

* * *

participantMessagingBinding

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

Information about how this participant exchanges messages with the conversation. A JSON parameter consisting of type and address fields of the participant.

* * *

conversationSidSID<CH>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique ID of the [Conversation](/docs/conversations/api/conversation-resource "Conversation") this Participant belongs to.

Pattern: `^CH[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

conversationUniqueNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

An application-defined string that uniquely identifies the Conversation resource.

* * *

conversationFriendlyNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The human-readable name of this conversation, limited to 256 characters. Optional.

* * *

conversationAttributesstring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified. **Note** that if the attributes are not set "{}" will be returned.

* * *

conversationDateCreatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that this conversation was created, given in ISO 8601 format.

* * *

conversationDateUpdatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that this conversation was last updated, given in ISO 8601 format.

* * *

conversationCreatedBystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Identity of the creator of this Conversation.

* * *

conversationStateenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The current state of this User Conversation. One of `inactive`, `active` or `closed`.

Possible values:

`inactive``active``closed`

* * *

conversationTimers

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Timer date values representing state update for this conversation.

* * *

linksobject<uri-map>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Contains absolute URLs to access the [participant](/docs/conversations/api/conversation-participant-resource "participant") and [conversation](/docs/conversations/api/conversation-resource "conversation") of this conversation.

* * *

## List All of a Participant's Conversations

list-all-of-a-participants-conversations page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/ParticipantConversations`

The ParticipantConversation resource also supports pagination via additional parameters like: `PageSize` and `PageToken`.

(information)

## Info

It's expected that you will encode the url for the ParticipantConversations endpoint, for example, if a phone number is passed as an address parameter the `+` character should be encoded as `%2B`.

(warning)

## Warning

In the [Group MMS](/docs/conversations/group-texting#what-is-group-texting "Group MMS") use case, it may happen that the participant might not have an identifier (no `address` and no `identity`). So, this endpoint will not return conversations for this participant. Similarly if the identity of this participant with [Projected Address](/docs/conversations/group-texting#projected-addresses-vs-proxy-addresses "Projected Address") is created later then this endpoint will not return conversations to which this participant was added when it was without identity.

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

identitystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A unique string identifier for the conversation participant as [Conversation User](/docs/conversations/api/user-resource "Conversation User"). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.

* * *

addressstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A unique string identifier for the conversation participant who's not a Conversation User. This parameter could be found in messaging_binding.address field of Participant resource. It should be url-encoded.

* * *

pageSizeinteger<int64>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

How many resources to return in each list page. The default is 50, and the maximum is 50.

Minimum: `1`Maximum: `50`

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

List All of a Participant's ConversationsLink to code sample: List All of a Participant's Conversations

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

    async function listParticipantConversation() {


    11

      const participantConversations =


    12

        await client.conversations.v1.participantConversations.list({


    13

          address: "+375255555555",


    14

          limit: 20,


    15

        });


    16




    17

      participantConversations.forEach((p) => console.log(p.accountSid));


    18

    }


    19




    20

    listParticipantConversation();

### Response

Note about this response

Copy response


    1

    {


    2

      "conversations": [


    3

        {


    4

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

          "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

          "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    7

          "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    8

          "conversation_friendly_name": "friendly_name",


    9

          "conversation_state": "inactive",


    10

          "conversation_timers": {


    11

            "date_inactive": "2015-12-16T22:19:38Z",


    12

            "date_closed": "2015-12-16T22:28:38Z"


    13

          },


    14

          "conversation_attributes": "{}",


    15

          "conversation_date_created": "2015-07-30T20:00:00Z",


    16

          "conversation_date_updated": "2015-07-30T20:00:00Z",


    17

          "conversation_created_by": "created_by",


    18

          "conversation_unique_name": "unique_name",


    19

          "participant_user_sid": null,


    20

          "participant_identity": null,


    21

          "participant_messaging_binding": {


    22

            "address": "+375255555555",


    23

            "proxy_address": "+12345678910",


    24

            "type": "sms",


    25

            "level": null,


    26

            "name": null,


    27

            "projected_address": null


    28

          },


    29

          "links": {


    30

            "participant": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    31

            "conversation": "https://conversations.twilio.com/v1/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    32

          }


    33

        }


    34

      ],


    35

      "meta": {


    36

        "page": 0,


    37

        "page_size": 50,


    38

        "first_page_url": "https://conversations.twilio.com/v1/ParticipantConversations?Address=%2B375255555555&PageSize=50&Page=0",


    39

        "previous_page_url": null,


    40

        "url": "https://conversations.twilio.com/v1/ParticipantConversations?Address=%2B375255555555&PageSize=50&Page=0",


    41

        "next_page_url": null,


    42

        "key": "conversations"


    43

      }


    44

    }