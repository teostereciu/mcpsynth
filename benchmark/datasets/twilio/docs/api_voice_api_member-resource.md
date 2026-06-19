# Members subresource

*Source: https://www.twilio.com/docs/voice/api/member-resource*

---

# Members subresource

Positive FeedbackNegative Feedback

* * *

Members is a subresource of [Queues](/docs/voice/api/queue-resource "Queues") and represents a single call in a call queue.

All members in a call queue can be identified by their unique `CallSid`, and the member at the front of the queue can be identified by the `Front` sid.

* * *

## Member Properties

member-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

callSidSID<CA>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Call](/docs/voice/api/call-resource "Call") the Member resource is associated with.

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

dateEnqueuedstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date that the member was enqueued, given in RFC 2822 format.

* * *

positioninteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

This member's current position in the queue.

Default: `0`

* * *

uristring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URI of the resource, relative to `https://api.twilio.com`.

* * *

waitTimeinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The number of seconds the member has been in the queue.

Default: `0`

* * *

queueSidSID<QU>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Queue the member is in.

Pattern: `^QU[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

## Retrieve a Member

retrieve-a-member page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Queues/{QueueSid}/Members/{CallSid}.json`

You can address the member to fetch by its unique `CallSid` or by the `Front` sid to fetch the member at the front of the queue.

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Member resource(s) to fetch.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

queueSidSID<QU>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Queue in which to find the members to fetch.

Pattern: `^QU[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

callSidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The [Call](/docs/voice/api/call-resource "Call") SID of the resource(s) to fetch.

Retrieve a MemberLink to code sample: Retrieve a Member

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

    async function fetchMember() {


    11

      const member = await client


    12

        .queues("QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .members("CallSid")


    14

        .fetch();


    15




    16

      console.log(member.callSid);


    17

    }


    18




    19

    fetchMember();

### Response

Note about this response

Copy response


    1

    {


    2

      "queue_sid": "QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "call_sid": "CallSid",


    4

      "date_enqueued": "Tue, 07 Aug 2012 22:57:41 +0000",


    5

      "position": 1,


    6

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    7

      "wait_time": 143


    8

    }

Retrieve a Member at the front of the queueLink to code sample: Retrieve a Member at the front of the queue

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

    async function fetchMember() {


    11

      const member = await client


    12

        .queues("QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .members("Front")


    14

        .fetch();


    15




    16

      console.log(member.callSid);


    17

    }


    18




    19

    fetchMember();

### Response

Note about this response

Copy response


    1

    {


    2

      "queue_sid": "QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "call_sid": "Front",


    4

      "date_enqueued": "Tue, 07 Aug 2012 22:57:41 +0000",


    5

      "position": 1,


    6

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    7

      "wait_time": 143


    8

    }

* * *

## Retrieve a list of Members

retrieve-a-list-of-members page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Queues/{QueueSid}/Members.json`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Member resource(s) to read.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

queueSidSID<QU>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Queue in which to find the members

Pattern: `^QU[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

pageSizeinteger<int64>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

How many resources to return in each list page. The default is 50, and the maximum is 1000.

Minimum: `1`Maximum: `1000`

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

Retrieve a list of MembersLink to code sample: Retrieve a list of Members

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

    async function listMember() {


    11

      const members = await client


    12

        .queues("QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .members.list({ limit: 20 });


    14




    15

      members.forEach((m) => console.log(m.callSid));


    16

    }


    17




    18

    listMember();

### Response

Note about this response

Copy response


    1

    {


    2

      "end": 0,


    3

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members.json?PageSize=50&Page=0",


    4

      "next_page_uri": null,


    5

      "page": 0,


    6

      "page_size": 50,


    7

      "previous_page_uri": null,


    8

      "queue_members": [


    9

        {


    10

          "queue_sid": "QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    11

          "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    12

          "date_enqueued": "Mon, 17 Dec 2018 18:36:39 +0000",


    13

          "position": 1,


    14

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    15

          "wait_time": 124


    16

        }


    17

      ],


    18

      "start": 0,


    19

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members.json?PageSize=50&Page=0"


    20

    }

* * *

## Update a Member

update-a-member page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Queues/{QueueSid}/Members/{CallSid}.json`

Updating a Member subresource dequeues the member to begin executing the TwiML document at that URL.

You can address the member to dequeue by its unique `CallSid` or by the `Front` sid.

If you successfully dequeue a member by its unique `CallSid`, it will no longer be queued so a second update action on that same member will fail.

When dequeueing a member by using the `Front` SID, that member will be dequeued and the next member in the queue will take its place.

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Member resource(s) to update.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

queueSidSID<QU>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Queue in which to find the members to update.

Pattern: `^QU[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

callSidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The [Call](/docs/voice/api/call-resource "Call") SID of the resource(s) to update.

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

urlstring<uri>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The absolute URL of the Queue resource.

* * *

methodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

How to pass the update request data. Can be `GET` or `POST` and the default is `POST`. `POST` sends the data as encoded form data and `GET` sends the data as query parameters.

Possible values:

`GET``POST`

Select from available examples

Copy code block


    {


      "Method": "GET",


      "Url": "https://example.com"


    }

Update a MemberLink to code sample: Update a Member

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

    async function updateMember() {


    11

      const member = await client


    12

        .queues("QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .members("CallSid")


    14

        .update({ url: "https://www.example.com" });


    15




    16

      console.log(member.callSid);


    17

    }


    18




    19

    updateMember();

### Response

Note about this response

Copy response


    1

    {


    2

      "queue_sid": "QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "call_sid": "CallSid",


    4

      "date_enqueued": "Thu, 06 Dec 2018 18:42:47 +0000",


    5

      "position": 1,


    6

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    7

      "wait_time": 143


    8

    }

Update a Member at the front of the queueLink to code sample: Update a Member at the front of the queue

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

    async function updateMember() {


    11

      const member = await client


    12

        .queues("QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .members("Front")


    14

        .update({ url: "https://www.example.com" });


    15




    16

      console.log(member.callSid);


    17

    }


    18




    19

    updateMember();

### Response

Note about this response

Copy response


    1

    {


    2

      "queue_sid": "QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "call_sid": "Front",


    4

      "date_enqueued": "Thu, 06 Dec 2018 18:42:47 +0000",


    5

      "position": 1,


    6

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    7

      "wait_time": 143


    8

    }