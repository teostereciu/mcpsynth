# Service Rate Limits

*Source: https://www.twilio.com/docs/verify/api/service-rate-limits*

---

# Service Rate Limits

Positive FeedbackNegative Feedback

* * *

Service Rate Limits makes it easy to use Twilio's battle-tested rate-limiting services to protect your Verify deployment. With Service Rate Limits, you can define the keys to meter and limits to enforce when starting user verifications. Together with Verify's built-in platform protections Service Rate Limits gives you turnkey protection with flexibility.

**Prerequisites:**

  1. [Create a Verification Service](/docs/verify/api/service "Create a Verification Service")


(information)

## Info

If you are just getting started with Rate Limits in Verify we recommend checking out our guide on [Using Verify Service Rate Limits to Protect Your Application](/docs/verify/api/programmable-rate-limits "Using Verify Service Rate Limits to Protect Your Application") before diving into the API.

* * *

## Rate Limit Properties

rate-limit-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

sidSID<RK>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A 34 character string that uniquely identifies this Rate Limit.

Pattern: `^RK[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

serviceSidSID<VA>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Service](/docs/verify/api/service "Service") the resource is associated with.

Pattern: `^VA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Rate Limit resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

uniqueNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Provides a unique and addressable name to be assigned to this Rate Limit, assigned by the developer, to be optionally used in addition to SID. **This value should not contain PII.**

* * *

descriptionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Description of this Rate Limit

* * *

dateCreatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT when the resource was created specified in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.

* * *

dateUpdatedstring<date-time>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT when the resource was last updated specified in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.

* * *

urlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL of this resource.

* * *

linksobject<uri-map>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URLs of related resources.

* * *

## Create a Rate Limit

create-a-rate-limit page anchor

Positive FeedbackNegative Feedback

`POST https://verify.twilio.com/v2/Services/{ServiceSid}/RateLimits`

The Rate Limit represents the key that your application will provide when starting a user verification request. For example, you may create a rate limit for an end-user IP address to prevent a malicious bot. See the section on Selecting Rate Limit Keys for information on this topic.

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

serviceSidSID<VA>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Service](/docs/verify/api/service "Service") the resource is associated with.

Pattern: `^VA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

uniqueNamestring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Provides a unique and addressable name to be assigned to this Rate Limit, assigned by the developer, to be optionally used in addition to SID. **This value should not contain PII.**

* * *

descriptionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Description of this Rate Limit

Copy code block


    {


      "UniqueName": "unique.name",


      "Description": "Description"


    }

Create a Rate LimitLink to code sample: Create a Rate Limit

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

    async function createRateLimit() {


    11

      const rateLimit = await client.verify.v2


    12

        .services("VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .rateLimits.create({


    14

          description: "Limit on end user IP Address",


    15

          uniqueName: "end_user_ip_address",


    16

        });


    17




    18

      console.log(rateLimit.sid);


    19

    }


    20




    21

    createRateLimit();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "RKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "unique_name": "end_user_ip_address",


    6

      "description": "Limit on end user IP Address",


    7

      "date_created": "2015-07-30T20:00:00Z",


    8

      "date_updated": "2015-07-30T20:00:00Z",


    9

      "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits/RKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    10

      "links": {


    11

        "buckets": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits/RKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Buckets"


    12

      }


    13

    }

* * *

## Fetch a Rate Limit

fetch-a-rate-limit page anchor

Positive FeedbackNegative Feedback

`GET https://verify.twilio.com/v2/Services/{ServiceSid}/RateLimits/{Sid}`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

serviceSidSID<VA>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Service](/docs/verify/api/service "Service") the resource is associated with.

Pattern: `^VA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<RK>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch.

Pattern: `^RK[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Fetch a Rate LimitLink to code sample: Fetch a Rate Limit

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

    async function fetchRateLimit() {


    11

      const rateLimit = await client.verify.v2


    12

        .services("VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .rateLimits("RKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    14

        .fetch();


    15




    16

      console.log(rateLimit.sid);


    17

    }


    18




    19

    fetchRateLimit();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "RKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "unique_name": "unique.name",


    6

      "description": "Description",


    7

      "date_created": "2015-07-30T20:00:00Z",


    8

      "date_updated": "2015-07-30T20:00:00Z",


    9

      "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits/RKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    10

      "links": {


    11

        "buckets": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits/RKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Buckets"


    12

      }


    13

    }

* * *

## List all Rate Limits

list-all-rate-limits page anchor

Positive FeedbackNegative Feedback

`GET https://verify.twilio.com/v2/Services/{ServiceSid}/RateLimits`

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

serviceSidSID<VA>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Service](/docs/verify/api/service "Service") the resource is associated with.

Pattern: `^VA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

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

List all Rate LimitsLink to code sample: List all Rate Limits

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

    async function listRateLimit() {


    11

      const rateLimits = await client.verify.v2


    12

        .services("VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .rateLimits.list({ limit: 20 });


    14




    15

      rateLimits.forEach((r) => console.log(r.sid));


    16

    }


    17




    18

    listRateLimit();

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

        "first_page_url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits?PageSize=50&Page=0",


    6

        "previous_page_url": null,


    7

        "next_page_url": null,


    8

        "key": "rate_limits",


    9

        "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits?PageSize=50&Page=0"


    10

      },


    11

      "rate_limits": [


    12

        {


    13

          "sid": "RKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

          "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    15

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    16

          "unique_name": "unique.name",


    17

          "description": "Description",


    18

          "date_created": "2015-07-30T20:00:00Z",


    19

          "date_updated": "2015-07-30T20:00:00Z",


    20

          "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits/RKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    21

          "links": {


    22

            "buckets": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits/RKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Buckets"


    23

          }


    24

        }


    25

      ]


    26

    }

* * *

## Update a Rate Limit

update-a-rate-limit page anchor

Positive FeedbackNegative Feedback

`POST https://verify.twilio.com/v2/Services/{ServiceSid}/RateLimits/{Sid}`

### Path parameters

path-parameters-3 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

serviceSidSID<VA>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Service](/docs/verify/api/service "Service") the resource is associated with.

Pattern: `^VA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<RK>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch.

Pattern: `^RK[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters-1 page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

descriptionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Description of this Rate Limit

Copy code block


    {


      "Description": "Description"


    }

Update a Rate LimitLink to code sample: Update a Rate Limit

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

    async function updateRateLimit() {


    11

      const rateLimit = await client.verify.v2


    12

        .services("VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .rateLimits("RKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    14

        .update({ description: "A much better description" });


    15




    16

      console.log(rateLimit.sid);


    17

    }


    18




    19

    updateRateLimit();

### Response

Note about this response

Copy response


    1

    {


    2

      "sid": "RKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "unique_name": "unique.name",


    6

      "description": "A much better description",


    7

      "date_created": "2015-07-30T20:00:00Z",


    8

      "date_updated": "2015-07-30T20:00:00Z",


    9

      "url": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits/RKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    10

      "links": {


    11

        "buckets": "https://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/RateLimits/RKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Buckets"


    12

      }


    13

    }

* * *

## Delete a Rate Limit

delete-a-rate-limit page anchor

Positive FeedbackNegative Feedback

`DELETE https://verify.twilio.com/v2/Services/{ServiceSid}/RateLimits/{Sid}`

### Path parameters

path-parameters-4 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

serviceSidSID<VA>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Service](/docs/verify/api/service "Service") the resource is associated with.

Pattern: `^VA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<RK>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch.

Pattern: `^RK[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Delete a Rate LimitLink to code sample: Delete a Rate Limit

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

    async function deleteRateLimit() {


    11

      await client.verify.v2


    12

        .services("VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .rateLimits("RKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    14

        .remove();


    15

    }


    16




    17

    deleteRateLimit();