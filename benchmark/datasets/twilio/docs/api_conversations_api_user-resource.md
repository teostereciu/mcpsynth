# Conversations User Resource

*Source: https://www.twilio.com/docs/conversations/api/user-resource*

---

# Conversations User Resource

Positive FeedbackNegative Feedback

* * *

In Conversations, Users are Participants with privileges such as the ability to edit and delete [Messages](/docs/conversations/api/conversation-message-resource "Messages").

Every [Conversation Participant](/docs/conversations/api/conversation-participant-resource "Conversation Participant") who connects with a Chat SDK (browser or mobile) is backed by a User. Participants over SMS or other non-chat channel, in contrast, do not have a corresponding User. Attached to the User is:

  * **the Role assigned to the User** , which determines their permissions in your application
  * **a JSON blob of arbitrary Attributes** , which you can use to store profile information for display in your application
  * **Online/Offline status** , determined by whether the User is presently connected through a frontend SDK
  * **the Identity string** , which uniquely identifies a user in each Conversation Service.


_We recommend following the standard URI specification and avoid the following reserved characters_ `! * ' ( ) ; : @ & = + $ , / ? % # [ ]` _for values such as identity and friendly name._

* * *

## API Base URL

api-base-url page anchor

Positive FeedbackNegative Feedback

All URLs in the reference documentation use the following base URL:

Copy code block


    1

    https://conversations.twilio.com/v1


    2

### Using the shortened base URL

using-the-shortened-base-url page anchor

Positive FeedbackNegative Feedback

Using the REST API, you can interact with User resources in the **default Conversation Service** instance via a "shortened" URL that does not include the Conversation Service instance SID ("ISXXX..."). If you are only using one Conversation Service (the default), you do not need to include the Conversation Service SID in your URL, e.g.

Copy code block


    1

    GET /v1/Users/


    2

For Conversations applications that build on more than one Conversation Service instance, you will need to specify the Conversation Service SID in the REST API call:

Copy code block


    GET /v1/Services/<Service SID, ISXXX...>/Users/

* * *

## User Properties

user-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

sidSID<US>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string that we created to identify the User resource.

Pattern: `^US[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the User resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

chatServiceSidSID<IS>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service") the User resource is associated with.

Pattern: `^IS[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

roleSidSID<RL>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of a service-level [Role](/docs/conversations/api/role-resource "Role") assigned to the user.

Pattern: `^RL[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

identitystring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The application-defined string that uniquely identifies the resource's User within the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service"). This value is often a username or an email address, and is case-sensitive.

* * *

friendlyNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The string that you assigned to describe the resource.

* * *

attributesstring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.

* * *

isOnlineboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether the User is actively connected to this Conversations Service and online. This value is only returned by Fetch actions that return a single resource and `null` is always returned by a Read action. This value is `null` if the Service's `reachability_enabled` is `false`, if the User has never been online for this Conversations Service, even if the Service's `reachability_enabled` is `true`.

* * *

isNotifiableboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether the User has a potentially valid Push Notification registration (APN or GCM) for this Conversations Service. If at least one registration exists, `true`; otherwise `false`. This value is only returned by Fetch actions that return a single resource and `null` is always returned by a Read action. This value is `null` if the Service's `reachability_enabled` is `false`, and if the User has never had a notification registration, even if the Service's `reachability_enabled` is `true`.

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

An absolute API resource URL for this user.

* * *

linksobject<uri-map>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

## Create a Conversations User

create-a-conversations-user page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Users`

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

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

identitystring

required

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The application-defined string that uniquely identifies the resource's User within the [Conversation Service](/docs/conversations/api/service-resource "Conversation Service"). This value is often a username or an email address, and is case-sensitive.

* * *

friendlyNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The string that you assigned to describe the resource.

* * *

attributesstring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.

* * *

roleSidSID<RL>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of a service-level [Role](/docs/conversations/api/role-resource "Role") to assign to the user.

Pattern: `^RL[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Copy code block


    {


      "Identity": "admin",


      "FriendlyName": "name",


      "Attributes": "{ \"duty\": \"tech\" }",


      "RoleSid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    }

Create a UserLink to code sample: Create a User

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

    async function createUser() {


    11

      const user = await client.conversations.v1.users.create({


    12

        identity: "RedgrenGrumbholdt",


    13

      });


    14




    15

      console.log(user.sid);


    16

    }


    17




    18

    createUser();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

      "identity": "RedgrenGrumbholdt",


    7

      "friendly_name": "name",


    8

      "attributes": "{ \"duty\": \"tech\" }",


    9

      "is_online": true,


    10

      "is_notifiable": null,


    11

      "date_created": "2019-12-16T22:18:37Z",


    12

      "date_updated": "2019-12-16T22:18:38Z",


    13

      "url": "https://conversations.twilio.com/v1/Users/USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

      "links": {


    15

        "user_conversations": "https://conversations.twilio.com/v1/Users/USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations"


    16

      }


    17

    }

* * *

## Fetch a specific User Resource

fetch-a-specific-user-resource page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Users/{Sid}`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the User resource to fetch. This value can be either the `sid` or the `identity` of the User resource to fetch.

Fetch an UserLink to code sample: Fetch an User

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

    async function fetchUser() {


    11

      const user = await client.conversations.v1.users("Sid").fetch();


    12




    13

      console.log(user.sid);


    14

    }


    15




    16

    fetchUser();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "Sid",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    6

      "identity": "admin",


    7

      "friendly_name": "name",


    8

      "attributes": "{ \"duty\": \"tech\" }",


    9

      "is_online": true,


    10

      "is_notifiable": null,


    11

      "date_created": "2019-12-16T22:18:37Z",


    12

      "date_updated": "2019-12-16T22:18:38Z",


    13

      "url": "https://conversations.twilio.com/v1/Users/USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

      "links": {


    15

        "user_conversations": "https://conversations.twilio.com/v1/Users/USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations"


    16

      }


    17

    }

* * *

## Read multiple ConversationUser resources

read-multiple-conversationuser-resources page anchor

Positive FeedbackNegative Feedback

`GET https://conversations.twilio.com/v1/Users`

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

List multiple UsersLink to code sample: List multiple Users

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

    async function listUser() {


    11

      const users = await client.conversations.v1.users.list({ limit: 20 });


    12




    13

      users.forEach((u) => console.log(u.sid));


    14

    }


    15




    16

    listUser();

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

        "first_page_url": "https://conversations.twilio.com/v1/Users?PageSize=50&Page=0",


    6

        "previous_page_url": null,


    7

        "url": "https://conversations.twilio.com/v1/Users?PageSize=50&Page=0",


    8

        "next_page_url": null,


    9

        "key": "users"


    10

      },


    11

      "users": [


    12

        {


    13

          "sid": "USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    15

          "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    16

          "role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

          "identity": "admin",


    18

          "friendly_name": "name",


    19

          "attributes": "{ \"duty\": \"tech\" }",


    20

          "is_online": true,


    21

          "is_notifiable": null,


    22

          "date_created": "2019-12-16T22:18:37Z",


    23

          "date_updated": "2019-12-16T22:18:38Z",


    24

          "url": "https://conversations.twilio.com/v1/Users/USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    25

          "links": {


    26

            "user_conversations": "https://conversations.twilio.com/v1/Users/USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations"


    27

          }


    28

        },


    29

        {


    30

          "sid": "USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    31

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    32

          "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    33

          "role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    34

          "identity": "agent0034",


    35

          "friendly_name": "John from customs",


    36

          "attributes": "{ \"duty\": \"agent\" }",


    37

          "is_online": false,


    38

          "is_notifiable": null,


    39

          "date_created": "2020-03-24T20:38:21Z",


    40

          "date_updated": "2020-03-24T20:38:21Z",


    41

          "url": "https://conversations.twilio.com/v1/Users/USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    42

          "links": {


    43

            "user_conversations": "https://conversations.twilio.com/v1/Users/USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations"


    44

          }


    45

        }


    46

      ]


    47

    }

* * *

## Update a ConversationUser resource

update-a-conversationuser-resource page anchor

Positive FeedbackNegative Feedback

`POST https://conversations.twilio.com/v1/Users/{Sid}`

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

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.

### Request body parameters

request-body-parameters-1 page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

friendlyNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The string that you assigned to describe the resource.

* * *

attributesstring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.

* * *

roleSidSID<RL>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of a service-level [Role](/docs/conversations/api/role-resource "Role") to assign to the user.

Pattern: `^RL[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Copy code block


    {


      "FriendlyName": "new name",


      "Attributes": "{ \"duty\": \"tech\", \"team\": \"internals\" }",


      "RoleSid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    }

Update a UserLink to code sample: Update a User

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

    async function updateUser() {


    11

      const user = await client.conversations.v1.users("Sid").update({


    12

        friendlyName: "new name",


    13

        roleSid: "RLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    14

      });


    15




    16

      console.log(user.sid);


    17

    }


    18




    19

    updateUser();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "Sid",


    3

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "role_sid": "RLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    6

      "identity": "admin",


    7

      "friendly_name": "new name",


    8

      "attributes": "{ \"duty\": \"tech\", \"team\": \"internals\" }",


    9

      "is_online": true,


    10

      "is_notifiable": null,


    11

      "date_created": "2019-12-16T22:18:37Z",


    12

      "date_updated": "2019-12-16T22:18:38Z",


    13

      "url": "https://conversations.twilio.com/v1/Users/USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

      "links": {


    15

        "user_conversations": "https://conversations.twilio.com/v1/Users/USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations"


    16

      }


    17

    }

* * *

## Delete a User resource

delete-a-user-resource page anchor

Positive FeedbackNegative Feedback

`DELETE https://conversations.twilio.com/v1/Users/{Sid}`

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

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

sidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the User resource to delete. This value can be either the `sid` or the `identity` of the User resource to delete.

Delete an UserLink to code sample: Delete an User

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

    async function deleteUser() {


    11

      await client.conversations.v1.users("Sid").remove();


    12

    }


    13




    14

    deleteUser();