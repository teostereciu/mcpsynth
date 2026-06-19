# Role Resource

*Source: https://www.twilio.com/docs/conversations/api/role-resource*

---

# Role Resource

Positive FeedbackNegative Feedback

* * *

In Twilio Conversations, the Role Resource represents what a User can do within the Service and individual Conversations. Roles are scoped to either a Service or a [Conversation](/docs/conversations/api/conversation-resource "Conversation").

[Users](/docs/conversations/api/user-resource "Users") are assigned a Role at the Service level. This determines what they can do within the chat Service instance, such as create and destroy Conversations within the Service.

[Participants](/docs/conversations/api/conversation-participant-resource "Participants") are assigned a Role at the Conversation level. This determines what they are able to do within a particular Conversation, such as invite Participants to be members of the Conversation, post Messages, and remove other Participants from the Conversation.

See [Permission Values](/docs/conversations/api/role-resource#permission-values "Permission Values") for information about the permissions that can be assigned in each scope.

(error)

## Do not use Personally Identifiable Information (PII) for the friendlyName field

Avoid using a person's name, home address, email, phone number, or other PII in the `friendlyName` field. Use some form of pseudonymized identifier, instead.

You can learn more about how we process your data in our [privacy policy.(link takes you to an external page)](https://www.twilio.com/en-us/legal/privacy "privacy policy.")

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

Using the REST API, you can interact with Role resources in the **default Conversation Service** instance via a "shortened" URL that does not include the Conversation Service instance SID ("ISXXX..."). If you are only using one Conversation Service (the default), you do not need to include the Conversation Service SID in your URL, e.g.

Copy code block


    GET /v1/Roles/

For Conversations applications that build on more than one Conversation Service instance, you will need to specify the Conversation Service SID in the REST API call.

Copy code block


    1

    GET /v1/Services/<Service SID, ISXXX...>/Roles/


    2

* * *

## Role Properties

role-properties page anchor

Positive FeedbackNegative Feedback

Each Role resource contains these properties.

Property nameTypeRequiredPIIDescriptionChild properties

sidSID<RL>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string that we created to identify the Role resource.

Pattern: `^RL[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Role resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

chatServiceSidSID<IS>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") the Role resource is associated with.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

friendlyNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The string that you assigned to describe the resource.

* * *

typeenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The type of role. Can be: `conversation` for [Conversation](/docs/conversations/api/conversation-resource "Conversation") roles or `service` for [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") roles.

Possible values:

`conversation``service`

* * *

permissionsarray[string]

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An array of the permissions the role has been granted.

* * *

dateCreatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT when the resource was created specified in [ISO 8601(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601") format.

* * *

dateUpdatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT when the resource was last updated specified in [ISO 8601(link takes you to an external page)](https://en.wikipedia.org/wiki/ISO_8601 "ISO 8601") format.

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

An absolute API resource URL for this user role.

* * *

## Create a Role resource

create-a-role-resource page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Roles`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

friendlyNamestring

required

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

A descriptive string that you create to describe the new resource. It can be up to 64 characters long.

* * *

typeenum<string>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The type of role. Can be: `conversation` for [Conversation](/docs/conversations/api/conversation-resource "Conversation") roles or `service` for [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") roles.

Possible values:

`conversation``service`

* * *

permissionarray[string]

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A permission that you grant to the new role. Only one permission can be granted per parameter. To assign more than one permission, repeat this parameter for each permission value. The values for this parameter depend on the role's `type`.

Copy code block


    {


      "FriendlyName": "Conversation Role",


      "Type": "conversation",


      "Permission": "sendMessage"


    }

Create a RoleLink to code sample: Create a Role

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

    async function createRole() {


    11

      const role = await client.conversations.v1.roles.create({


    12

        friendlyName: "FriendlyName",


    13

        permission: ["addParticipant"],


    14

        type: "conversation",


    15

      });


    16




    17

      console.log(role.sid);


    18

    }


    19




    20

    createRole();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "friendly_name": "FriendlyName",


    6

      "type": "conversation",


    7

      "permissions": [


    8

        "sendMessage",


    9

        "leaveConversation",


    10

        "editOwnMessage",


    11

        "deleteOwnMessage"


    12

      ],


    13

      "date_created": "2016-03-03T19:47:15Z",


    14

      "date_updated": "2016-03-03T19:47:15Z",


    15

      "url": "https://conversations.twilio.com/v1/Roles/RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    16

    }

* * *

## Fetch a Role resource

fetch-a-role-resource page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Roles/{Sid}`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidSID<RL>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Role resource to fetch.

Pattern: `^RL[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Fetch a RoleLink to code sample: Fetch a Role

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

    async function fetchRole() {


    11

      const role = await client.conversations.v1


    12

        .roles("RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .fetch();


    14




    15

      console.log(role.sid);


    16

    }


    17




    18

    fetchRole();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "friendly_name": "Conversation Role",


    6

      "type": "conversation",


    7

      "permissions": [


    8

        "sendMessage",


    9

        "leaveConversation",


    10

        "editOwnMessage",


    11

        "deleteOwnMessage"


    12

      ],


    13

      "date_created": "2016-03-03T19:47:15Z",


    14

      "date_updated": "2016-03-03T19:47:15Z",


    15

      "url": "https://conversations.twilio.com/v1/Roles/RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    16

    }

* * *

## Read multiple Role resources

read-multiple-role-resources page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Roles`

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

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

List multiple RolesLink to code sample: List multiple Roles

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

    async function listRole() {


    11

      const roles = await client.conversations.v1.roles.list({ limit: 20 });


    12




    13

      roles.forEach((r) => console.log(r.sid));


    14

    }


    15




    16

    listRole();

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

        "first_page_url": "https://conversations.twilio.com/v1/Roles?PageSize=50&Page=0",


    6

        "previous_page_url": null,


    7

        "url": "https://conversations.twilio.com/v1/Roles?PageSize=50&Page=0",


    8

        "next_page_url": null,


    9

        "key": "roles"


    10

      },


    11

      "roles": [


    12

        {


    13

          "sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    15

          "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    16

          "friendly_name": "Conversation Role",


    17

          "type": "conversation",


    18

          "permissions": [


    19

            "sendMessage",


    20

            "leaveConversation",


    21

            "editOwnMessage",


    22

            "deleteOwnMessage"


    23

          ],


    24

          "date_created": "2016-03-03T19:47:15Z",


    25

          "date_updated": "2016-03-03T19:47:15Z",


    26

          "url": "https://conversations.twilio.com/v1/Roles/RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    27

        }


    28

      ]


    29

    }

* * *

## Update a Role resource

update-a-role-resource page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Roles/{Sid}`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidSID<RL>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Role resource to update.

Pattern: `^RL[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters-1 page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

permissionarray[string]

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A permission that you grant to the role. Only one permission can be granted per parameter. To assign more than one permission, repeat this parameter for each permission value. Note that the update action replaces all previously assigned permissions with those defined in the update action. To remove a permission, do not include it in the subsequent update action. The values for this parameter depend on the role's `type`.

Copy code block


    {


      "Permission": "sendMessage"


    }

Update a Conversation RoleLink to code sample: Update a Conversation Role

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

    async function updateRole() {


    11

      const role = await client.conversations.v1


    12

        .roles("New_Chat_Service_SID")


    13

        .update({ permission: ["Permission"] });


    14




    15

      console.log(role.sid);


    16

    }


    17




    18

    updateRole();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "New_Chat_Service_SID",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "friendly_name": "Conversation Role",


    6

      "type": "conversation",


    7

      "permissions": [


    8

        "sendMessage",


    9

        "leaveConversation",


    10

        "editOwnMessage",


    11

        "deleteOwnMessage"


    12

      ],


    13

      "date_created": "2016-03-03T19:47:15Z",


    14

      "date_updated": "2016-03-03T19:47:15Z",


    15

      "url": "https://conversations.twilio.com/v1/Roles/RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    16

    }

* * *

## Delete a Role resource

delete-a-role-resource page anchor

Positive FeedbackNegative Feedback

`DELETE https://conversations.twilio.com/v1/Roles/{Sid}`

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidSID<RL>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Role resource to delete.

Pattern: `^RL[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Delete a RoleLink to code sample: Delete a Role

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

    async function deleteRole() {


    11

      await client.conversations.v1


    12

        .roles("RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .remove();


    14

    }


    15




    16

    deleteRole();

* * *

## Permission Values

permission-values page anchor

Positive FeedbackNegative Feedback

### Service-scope permissions

service-scope-permissions page anchor

Positive FeedbackNegative Feedback

These are the available `permissions` entries for roles where `type` = **service**.

Permission| Enables User to:
---|---
`addParticipant`| Add other users as Participants of a Conversation
`createConversation`| Create new Conversations
`deleteAnyMessage`| Delete any Message in the Service
`deleteConversation`| Delete Conversations
`editAnyMessage`| Edit any Message in the Service
`editAnyMessageAttributes`| Edit any Message attributes in the Service
`editAnyUserInfo`| Edit other User's User Info properties
`editConversationAttributes`| Update the optional `attributes` metadata field on a Conversation
`editConversationName`| Change the name of a Conversation
`editOwnMessage`| Edit their own Messages in the Service
`editOwnMessageAttributes`| Edit the own Message attributes in the Service
`editOwnUserInfo`| Edit their own User Info properties
`joinConversation`| Join Conversations
`removeParticipant`| Remove Participants from a Conversation

### Conversation-scope permissions

conversation-scope-permissions page anchor

Positive FeedbackNegative Feedback

These are the available `permissions` entries for roles where `type` = **conversation**.

Permission| Enables User to:
---|---
`addParticipant`| Add other users as Participants of a Conversation
`deleteAnyMessage`| Delete any Message in the Service
`deleteOwnMessage`| Delete their own Messages in the Service
`deleteConversation`| Delete Conversations
`editAnyMessage`| Edit any Message in the Service
`editAnyMessageAttributes`| Edit any Message attributes in the Service
`editAnyUserInfo`| Edit other User's User Info properties
`editConversationAttributes`| Update the optional `attributes` metadata field on a Conversation
`editConversationName`| Change the name of a Conversation
`editOwnMessage`| Edit their own Messages in the Service
`editOwnMessageAttributes`| Edit the own Message attributes in the Service
`editOwnUserInfo`| Edit their own User Info properties
`leaveConversation`| Leave a Conversation
`removeParticipant`| Remove Participants from a Conversation
`sendMediaMessage`| Send media Messages to Conversations
`sendMessage`| Send Messages to Conversations