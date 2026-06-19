# Queues resource

*Source: https://www.twilio.com/docs/voice/api/queue-resource*

---

# Queues resource

Positive FeedbackNegative Feedback

* * *

A Queue resource describes a call queue that contains individual calls, which are described by the queue's [Members subsresource](/docs/voice/api/member-resource "Members subsresource"). Your account can have more than one call queue. Each queue can be retrieved by its `sid` directly using fetch. Alternately, you can read the list of Queues and filter by `friendly_name` or any other property you prefer.

Call queues are created when you add a call to a queue that doesn't exist and when you [create one explicitly](/docs/voice/api/queue-resource#create-a-queue "create one explicitly").

For information about enqueuing calls, see [Queueing Calls](/docs/voice/queue-calls "Queueing Calls").

(warning)

## Warning

Queues persist. To optimize fetch operations, inactive Queues should be deleted.

* * *

## Queues properties

queues-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

dateUpdatedstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT that this resource was last updated, specified in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.

* * *

currentSizeinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The number of calls currently in the queue.

Default: `0`

* * *

friendlyNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A string that you assigned to describe this resource.

* * *

uristring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URI of this resource, relative to `https://api.twilio.com`.

* * *

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created this Queue resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

averageWaitTimeinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The average wait time in seconds of the members in this queue. This is calculated at the time of the request.

Default: `0`

* * *

sidSID<QU>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string that that we created to identify this Queue resource.

Pattern: `^QU[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

dateCreatedstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT that this resource was created specified in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.

* * *

maxSizeinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The maximum number of calls that can be in the queue. The default is 1000 and the maximum is 5000.

Default: `0`

* * *

## Create a Queue

create-a-queue page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Queues.json`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that will create the resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

friendlyNamestring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A descriptive string that you created to describe this resource. It can be up to 64 characters long.

* * *

maxSizeinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The maximum number of calls allowed to be in the queue. The default is 1000. The maximum is 5000.

Copy code block


    {


      "FriendlyName": "friendly_name",


      "MaxSize": 1


    }

Create a QueueLink to code sample: Create a Queue

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

    async function createQueue() {


    11

      const queue = await client.queues.create({ friendlyName: "FriendlyName" });


    12




    13

      console.log(queue.dateUpdated);


    14

    }


    15




    16

    createQueue();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "average_wait_time": 0,


    4

      "current_size": 0,


    5

      "date_created": "Tue, 04 Aug 2015 18:39:09 +0000",


    6

      "date_updated": "Tue, 04 Aug 2015 18:39:09 +0000",


    7

      "friendly_name": "FriendlyName",


    8

      "max_size": 100,


    9

      "sid": "QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    10

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    11

    }

* * *

## Retrieve a Queue

retrieve-a-queue page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Queues/{Sid}.json`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Queue resource to fetch.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<QU>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the Queue resource to fetch

Pattern: `^QU[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Retrieve a QueueLink to code sample: Retrieve a Queue

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

    async function fetchQueue() {


    11

      const queue = await client


    12

        .queues("QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .fetch();


    14




    15

      console.log(queue.dateUpdated);


    16

    }


    17




    18

    fetchQueue();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "average_wait_time": 0,


    4

      "current_size": 0,


    5

      "date_created": "Tue, 04 Aug 2015 18:39:09 +0000",


    6

      "date_updated": "Tue, 04 Aug 2015 18:39:09 +0000",


    7

      "friendly_name": "0.361280134646222",


    8

      "max_size": 100,


    9

      "sid": "QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    10

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    11

    }

* * *

## Retrieve a list of Queues

retrieve-a-list-of-queues page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Queues.json`

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Queue resources to read.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

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

Retrieve a list of QueuesLink to code sample: Retrieve a list of Queues

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

    async function listQueue() {


    11

      const queues = await client.queues.list({ limit: 20 });


    12




    13

      queues.forEach((q) => console.log(q.dateUpdated));


    14

    }


    15




    16

    listQueue();

### Response

Note about this response

Copy response


    1

    {


    2

      "end": 0,


    3

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues.json?PageSize=1&Page=0",


    4

      "next_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues.json?PageSize=1&Page=1&PageToken=PAQUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "page": 0,


    6

      "page_size": 1,


    7

      "previous_page_uri": null,


    8

      "queues": [


    9

        {


    10

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    11

          "average_wait_time": 0,


    12

          "current_size": 0,


    13

          "date_created": "Tue, 04 Aug 2015 18:39:09 +0000",


    14

          "date_updated": "Tue, 04 Aug 2015 18:39:09 +0000",


    15

          "friendly_name": "0.361280134646222",


    16

          "max_size": 100,


    17

          "sid": "QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    18

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    19

        }


    20

      ],


    21

      "start": 0,


    22

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues.json?PageSize=1&Page=0"


    23

    }

* * *

## Update a Queue

update-a-queue page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Queues/{Sid}.json`

### Path parameters

path-parameters-3 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Queue resource to update.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<QU>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the Queue resource to update

Pattern: `^QU[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters-1 page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

friendlyNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A descriptive string that you created to describe this resource. It can be up to 64 characters long.

* * *

maxSizeinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The maximum number of calls allowed to be in the queue. The default is 1000. The maximum is 5000.

Copy code block


    {


      "FriendlyName": "friendly_name",


      "MaxSize": 1


    }

Update a QueueLink to code sample: Update a Queue

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

    async function updateQueue() {


    11

      const queue = await client


    12

        .queues("QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .update({ friendlyName: "FriendlyName" });


    14




    15

      console.log(queue.dateUpdated);


    16

    }


    17




    18

    updateQueue();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "average_wait_time": 0,


    4

      "current_size": 0,


    5

      "date_created": "Tue, 04 Aug 2015 18:39:09 +0000",


    6

      "date_updated": "Tue, 04 Aug 2015 18:39:09 +0000",


    7

      "friendly_name": "FriendlyName",


    8

      "max_size": 100,


    9

      "sid": "QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    10

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Queues/QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    11

    }

* * *

## Delete a Queue

delete-a-queue page anchor

Positive FeedbackNegative Feedback

`DELETE https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Queues/{Sid}.json`

### Path parameters

path-parameters-4 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Queue resource to delete.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<QU>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the Queue resource to delete

Pattern: `^QU[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Delete a QueueLink to code sample: Delete a Queue

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

    async function deleteQueue() {


    11

      await client.queues("QUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").remove();


    12

    }


    13




    14

    deleteQueue();