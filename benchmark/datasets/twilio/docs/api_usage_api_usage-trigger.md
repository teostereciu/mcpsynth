# REST API: UsageTrigger

*Source: https://www.twilio.com/docs/usage/api/usage-trigger*

---

# REST API: UsageTrigger

Positive FeedbackNegative Feedback

* * *

A **UsageTrigger** is a webhook that notifies your application of usage thresholds.

(information)

## Info

Twilio can send your web application an HTTP request when certain events happen, such as an incoming text message to one of your Twilio phone numbers. These requests are called _webhooks_ , or _status callbacks_. For more, check out our guide to [Getting Started with Twilio Webhooks](/docs/usage/webhooks/getting-started-twilio-webhooks "Getting Started with Twilio Webhooks"). Find other webhook pages, such as a [security guide](/docs/usage/webhooks/webhooks-security "security guide") and an [FAQ](/docs/usage/webhooks/webhooks-faq "FAQ") in the [Webhooks](/docs/usage/webhooks "Webhooks") section of the docs.

(warning)

## Warning

It can take some amount of time for the data used by usage triggers to be reflected in the UsageTriggers evaluations.

Using this resource, you can make or update a new UsageTrigger, fetch information about an existing UsageTrigger or multiple UsageTriggers, or delete an existing UsageTrigger.

You can configure UsageTriggers to recur daily, monthly, or yearly. UsageTriggers are evaluated frequently — about once a minute — to provide timely information to your application.

You can also set UsageTriggers for any usage category. For example, you can create a single UsageTrigger to track daily usage. In this case, a UsageTrigger notifies your application when your cost exceeds a set daily amount. If used together with Subaccounts created for each end-user, then a UsageTrigger would notify your application that a specific user has exceeded an allocated monthly usage.

(information)

## Info

For more information, see [Usage categories](/docs/usage/api/usage-record#usage-categories "Usage categories") in _Usage Records_ as well as [Subaccounts](/docs/iam/api/subaccounts "Subaccounts").

* * *

## Trigger Properties

trigger-properties page anchor

Positive FeedbackNegative Feedback

A UsageTrigger is represented by the following properties:

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that the trigger monitors.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

apiVersionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The API version used to create the resource.

* * *

callbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we use to call `callback_url`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

* * *

callbackUrlstring<uri>

Optional

[PII MTL: 60 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The URL we call using the `callback_method` when the trigger fires.

* * *

currentValuestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The current value of the field the trigger is watching.

* * *

dateCreatedstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT that the resource was created specified in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.

* * *

dateFiredstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT that the trigger was last fired specified in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.

* * *

dateUpdatedstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT that the resource was last updated specified in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.

* * *

friendlyNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The string that you assigned to describe the trigger.

* * *

recurringenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The frequency of a recurring UsageTrigger. Can be: `daily`, `monthly`, or `yearly` for recurring triggers or empty for non-recurring triggers. A trigger will only fire once during each period. Recurring times are in GMT.

Possible values:

`daily``monthly``yearly``alltime`

* * *

sidSID<UT>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string that that we created to identify the UsageTrigger resource.

Pattern: `^UT[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

triggerByenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The field in the [UsageRecord](/docs/usage/api/usage-record "UsageRecord") resource that fires the trigger. Can be: `count`, `usage`, or `price`, as described in the [UsageRecords documentation](/docs/usage/api/usage-record#usage-count-price "UsageRecords documentation").

Possible values:

`count``usage``price`

* * *

triggerValuestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The value at which the trigger will fire. Must be a positive, numeric value.

* * *

uristring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URI of the resource, relative to `https://api.twilio.com`.

* * *

usageCategorystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The usage category the trigger watches. Must be one of the supported [usage categories](/docs/usage/api/usage-record#usage-categories "usage categories").

* * *

usageRecordUristring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URI of the [UsageRecord](/docs/usage/api/usage-record "UsageRecord") resource this trigger watches, relative to `https://api.twilio.com`.

* * *

## CallbackUrl requests

callbackurl-requests page anchor

Positive FeedbackNegative Feedback

When an account's usage category crosses a UsageTrigger's `TriggerValue` during the specified interval, then Twilio makes a request to the `CallbackUrl` using the HTTP method `CallbackMethod` with the `CallbackUrl` Request parameters.

Twilio guarantees that a UsageTrigger will fire once (at most) during its recurring interval and will quickly retry the callback URL three times after a 5xx error.

(information)

## Info

For more information, see [CallbackUrl Request Parameters](/docs/usage/api/usage-trigger#usagetrigger-callbacks "CallbackUrl Request Parameters") below.

* * *

## Create a UsageTrigger Resource

create-a-usagetrigger-resource page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Usage/Triggers.json`

Each account can create up to 1,000 UsageTriggers. If UsageTrigger creation is successful, Twilio will respond with a representation of the new trigger.

(warning)

## Warning

Inactive UsageTriggers will _not_ be deleted automatically.

You need to delete triggers you no longer need. For more information, see [Delete a UsageTrigger resource](/docs/usage/api/usage-trigger#delete-a-usagetrigger-resource "Delete a UsageTrigger resource") below.

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

callbackUrlstring<uri>

required

[PII MTL: 60 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The URL we should call using `callback_method` when the trigger fires.

* * *

triggerValuestring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The usage value at which the trigger should fire. For convenience, you can use an offset value such as `+30` to specify a trigger_value that is 30 units more than the current usage value. Be sure to urlencode a `+` as `%2B`.

* * *

usageCategorystring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The usage category that the trigger should watch. Use one of the supported [usage categories](/docs/usage/api/usage-record#usage-categories "usage categories") for this value.

* * *

callbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is `POST`.

Possible values:

`GET``POST`

* * *

friendlyNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A descriptive string that you create to describe the resource. It can be up to 64 characters long.

* * *

recurringenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The frequency of a recurring UsageTrigger. Can be: `daily`, `monthly`, or `yearly` for recurring triggers or empty for non-recurring triggers. A trigger will only fire once during each period. Recurring times are in GMT.

Possible values:

`daily``monthly``yearly``alltime`

* * *

triggerByenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The field in the [UsageRecord](/docs/usage/api/usage-record "UsageRecord") resource that fires the trigger. Can be: `count`, `usage`, or `price`, as described in the [UsageRecords documentation](/docs/usage/api/usage-record#usage-count-price "UsageRecords documentation").

Possible values:

`count``usage``price`

Copy code block


    {


      "CallbackMethod": "GET",


      "CallbackUrl": "https://example.com",


      "FriendlyName": "friendly_name",


      "Recurring": "daily",


      "TriggerBy": "count",


      "TriggerValue": "trigger_value",


      "UsageCategory": "calleridlookups"


    }

Create a new UsageTrigger with parametersLink to code sample: Create a new UsageTrigger with parameters

Report code block

Copy code block


    1

    // Download the Node helper library from twilio.com/docs/node/install


    2

    // These consts are your accountSid and authToken from https://www.twilio.com/console


    3

    // To set up environmental variables, see http://twil.io/secure


    4

    const accountSid = process.env.TWILIO_ACCOUNT_SID;


    5

    const authToken = process.env.TWILIO_AUTH_TOKEN;


    6

    const client = require('twilio')(accountSid, authToken);


    7




    8

    client.usage.triggers


    9

      .create({


    10

        triggerValue: '1000',


    11

        usageCategory: 'sms',


    12

        callbackUrl: 'http://www.example.com/',


    13

      })


    14

      .then(trigger => process.stdout.write(trigger.sid));

### Output

Copy output


    1

    {


    2

       "usage_record_uri": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Usage/Records.json?Category=sms",


    3

       "date_updated": "Sat, 13 Oct 2012 21:32:30 +0000",


    4

       "date_fired": null,


    5

       "friendly_name": "Trigger for sms at usage of 1000",


    6

       "uri": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Usage/Triggers/UTc142bed7b38c4f8186ef41a309814fd2.json",


    7

       "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    8

       "callback_method": "POST",


    9

       "trigger_by": "usage",


    10

       "sid": "UTc142bed7b38c4f8186ef41a309814fd2",


    11

       "current_value": "57",


    12

       "date_created": "Sat, 13 Oct 2012 21:32:30 +0000",


    13

       "callback_url": "http://www.example.com",


    14

       "recurring": null,


    15

       "usage_category": "sms",


    16

       "trigger_value": "1000.000000"


    17

    }

Create a TriggerLink to code sample: Create a Trigger

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

    async function createUsageTrigger() {


    11

      const trigger = await client.usage.triggers.create({


    12

        callbackUrl: "https://www.example.com",


    13

        triggerValue: "TriggerValue",


    14

        usageCategory: "UsageCategory",


    15

      });


    16




    17

      console.log(trigger.accountSid);


    18

    }


    19




    20

    createUsageTrigger();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "api_version": "2010-04-01",


    4

      "callback_method": "GET",


    5

      "callback_url": "https://www.example.com",


    6

      "current_value": "0",


    7

      "date_created": "Sun, 06 Sep 2015 12:58:45 +0000",


    8

      "date_fired": null,


    9

      "date_updated": "Sun, 06 Sep 2015 12:58:45 +0000",


    10

      "friendly_name": "raphael-cluster-1441544325.86",


    11

      "recurring": "yearly",


    12

      "sid": "UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    13

      "trigger_by": "price",


    14

      "trigger_value": "TriggerValue",


    15

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers/UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    16

      "usage_category": "UsageCategory",


    17

      "usage_record_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records.json?Category=totalprice"


    18

    }

* * *

## Fetch a UsageTrigger resource

fetch-a-usagetrigger-resource page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Usage/Triggers/{Sid}.json`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the UsageTrigger resource to fetch.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<UT>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the UsageTrigger resource to fetch.

Pattern: `^UT[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Fetch a UsageTrigger resourceLink to code sample: Fetch a UsageTrigger resource

Report code block

Copy code block


    1

    // Download the Node helper library from twilio.com/docs/node/install


    2

    // These consts are your accountSid and authToken from https://www.twilio.com/console


    3

    // To set up environmental variables, see http://twil.io/secure


    4

    const accountSid = process.env.TWILIO_ACCOUNT_SID;


    5

    const authToken = process.env.TWILIO_AUTH_TOKEN;


    6

    const client = require('twilio')(accountSid, authToken);


    7




    8

    client.usage


    9

      .triggers('UT33c6aeeba34e48f38d6899ea5b765ad4')


    10

      .fetch()


    11

      .then(trigger => trigger.currentValue);

### Output

Copy output


    1

    {


    2

       "usage_record_uri": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Usage/Records.json?Category=calls",


    3

       "date_updated": "Sat, 29 Sep 2012 19:47:54 +0000",


    4

       "date_fired": null,


    5

       "friendly_name": "Trigger for calls at usage of 500",


    6

       "uri": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Usage/Triggers/UT33c6aeeba34e48f38d6899ea5b765ad4.json",


    7

       "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    8

       "callback_method": "POST",


    9

       "trigger_by": "usage",


    10

       "sid": "UT33c6aeeba34e48f38d6899ea5b765ad4",


    11

       "current_value": "21",


    12

       "date_created": "Sat, 29 Sep 2012 19:45:43 +0000",


    13

       "callback_url": "http://www.example.com/",


    14

       "recurring": null,


    15

       "usage_category": "calls",


    16

       "trigger_value": "500.000000"


    17

    }

Fetch a TriggerLink to code sample: Fetch a Trigger

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

    async function fetchUsageTrigger() {


    11

      const trigger = await client.usage


    12

        .triggers("UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .fetch();


    14




    15

      console.log(trigger.accountSid);


    16

    }


    17




    18

    fetchUsageTrigger();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "api_version": "2010-04-01",


    4

      "callback_method": "GET",


    5

      "callback_url": "http://cap.com/streetfight",


    6

      "current_value": "0",


    7

      "date_created": "Sun, 06 Sep 2015 12:58:45 +0000",


    8

      "date_fired": null,


    9

      "date_updated": "Sun, 06 Sep 2015 12:58:45 +0000",


    10

      "friendly_name": "raphael-cluster-1441544325.86",


    11

      "recurring": "yearly",


    12

      "sid": "UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    13

      "trigger_by": "price",


    14

      "trigger_value": "50",


    15

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers/UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    16

      "usage_category": "totalprice",


    17

      "usage_record_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records.json?Category=totalprice"


    18

    }

* * *

## Read multiple UsageTrigger resources

read-multiple-usagetrigger-resources page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Usage/Triggers.json`

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the UsageTrigger resources to read.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

recurringenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The frequency of recurring UsageTriggers to read. Can be: `daily`, `monthly`, or `yearly` to read recurring UsageTriggers. An empty value or a value of `alltime` reads non-recurring UsageTriggers.

Possible values:

`daily``monthly``yearly``alltime`

* * *

triggerByenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The trigger field of the UsageTriggers to read. Can be: `count`, `usage`, or `price` as described in the [UsageRecords documentation](/docs/usage/api/usage-record#usage-count-price "UsageRecords documentation").

Possible values:

`count``usage``price`

* * *

usageCategorystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The usage category of the UsageTriggers to read. Must be a supported [usage categories](/docs/usage/api/usage-record#usage-categories "usage categories").

* * *

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

Read multiple UsageTrigger resourcesLink to code sample: Read multiple UsageTrigger resources

Report code block

Copy code block


    1

    // Download the Node helper library from twilio.com/docs/node/install


    2

    // These consts are your accountSid and authToken from https://www.twilio.com/console


    3

    // To set up environmental variables, see http://twil.io/secure


    4

    const accountSid = process.env.TWILIO_ACCOUNT_SID;


    5

    const authToken = process.env.TWILIO_AUTH_TOKEN;


    6

    const client = require('twilio')(accountSid, authToken);


    7




    8

    const filterOpts = {


    9

      recurring: 'daily',


    10

      usageCategory: 'calls',


    11

    };


    12




    13

    client.usage.triggers.each(filterOpts, trigger =>


    14

      console.log(trigger.currentValue)


    15

    );

### Output

Copy output


    1

    {


    2

       "first_page_uri": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Usage/Triggers/.json?UsageCategory=calls&Recurring=daily&Page=0&PageSize=50",


    3

       "previous_page_uri": null,


    4

       "usage_triggers": [


    5

          {


    6

             "usage_record_uri": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Usage/Records/Today.json?Category=calls",


    7

             "date_updated": "Sat, 29 Sep 2012 19:42:57 +0000",


    8

             "date_fired": null,


    9

             "friendly_name": "a trigger",


    10

             "uri": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Usage/Triggers//UTc2db285b0cbf4c60a2f1a8db237a5fba.json",


    11

             "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    12

             "callback_method": "POST",


    13

             "trigger_by": "count",


    14

             "sid": "UTc2db285b0cbf4c60a2f1a8db237a5fba",


    15

             "current_value": "0",


    16

             "date_created": "Sun, 23 Sep 2012 23:07:29 +0000",


    17

             "callback_url": "http://www.google.com",


    18

             "recurring": "daily",


    19

             "usage_category": "calls",


    20

             "trigger_value": "0.000000"


    21

          }


    22

       ],


    23

       "uri": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Usage/Triggers.json?UsageCategory=calls&Recurring=daily",


    24

       "page_size": 50,


    25

       "next_page_uri": null,


    26

       "page": 0


    27

    }

List multiple TriggersLink to code sample: List multiple Triggers

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

    async function listUsageTrigger() {


    11

      const triggers = await client.usage.triggers.list({ limit: 20 });


    12




    13

      triggers.forEach((t) => console.log(t.accountSid));


    14

    }


    15




    16

    listUsageTrigger();

### Response

Note about this response

Copy response


    1

    {


    2

      "end": 0,


    3

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers.json?UsageCategory=calleridlookups&TriggerBy=count&Recurring=daily&PageSize=1&Page=0",


    4

      "next_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers.json?UsageCategory=calleridlookups&TriggerBy=count&Recurring=daily&PageSize=1&Page=1&PageToken=APMQ%3D%3D",


    5

      "page": 0,


    6

      "page_size": 1,


    7

      "previous_page_uri": null,


    8

      "start": 0,


    9

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers.json?UsageCategory=calleridlookups&TriggerBy=count&Recurring=daily&PageSize=1&Page=0",


    10

      "usage_triggers": [


    11

        {


    12

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    13

          "api_version": "2010-04-01",


    14

          "callback_method": "GET",


    15

          "callback_url": "http://cap.com/streetfight",


    16

          "current_value": "0",


    17

          "date_created": "Sun, 06 Sep 2015 12:58:45 +0000",


    18

          "date_fired": null,


    19

          "date_updated": "Sun, 06 Sep 2015 12:58:45 +0000",


    20

          "friendly_name": "raphael-cluster-1441544325.86",


    21

          "recurring": "yearly",


    22

          "sid": "UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    23

          "trigger_by": "price",


    24

          "trigger_value": "50",


    25

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers/UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    26

          "usage_category": "totalprice",


    27

          "usage_record_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records.json?Category=totalprice"


    28

        }


    29

      ]


    30

    }

* * *

## Update a UsageTrigger Resource

update-a-usagetrigger-resource page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Usage/Triggers/{Sid}.json`

Attempts a UsageTrigger's properties update and, if successful, returns the updated resource representation.

The returned response is identical to the returned response of a `GET` request.

### Path parameters

path-parameters-3 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the UsageTrigger resources to update.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<UT>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the UsageTrigger resource to update.

Pattern: `^UT[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters-1 page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

callbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is `POST`.

Possible values:

`GET``POST`

* * *

callbackUrlstring<uri>

Optional

[PII MTL: 60 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The URL we should call using `callback_method` when the trigger fires.

* * *

friendlyNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A descriptive string that you create to describe the resource. It can be up to 64 characters long.

Copy code block


    {


      "CallbackMethod": "GET",


      "CallbackUrl": "https://example.com",


      "FriendlyName": "friendly_name"


    }

Update a UsageTrigger ResourceLink to code sample: Update a UsageTrigger Resource

Report code block

Copy code block


    1

    // Download the Node helper library from twilio.com/docs/node/install


    2

    // These consts are your accountSid and authToken from https://www.twilio.com/console


    3

    // To set up environmental variables, see http://twil.io/secure


    4

    const accountSid = process.env.TWILIO_ACCOUNT_SID;


    5

    const authToken = process.env.TWILIO_AUTH_TOKEN;


    6

    const client = require('twilio')(accountSid, authToken);


    7




    8

    client.usage


    9

      .triggers('UT33c6aeeba34e48f38d6899ea5b765ad4')


    10

      .update({


    11

        friendlyName: 'Monthly Maximum Call Usage',


    12

        callbackUrl: 'https://www.example.com/monthly-usage-trigger',


    13

      })


    14

      .then(trigger => console.log(trigger.dateFired));

### Output

Copy output


    1

    {


    2

       "usage_record_uri": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Usage/Records.json?Category=calls",


    3

       "date_updated": "Sat, 13 Oct 2012 21:24:35 +0000",


    4

       "date_fired": null,


    5

       "friendly_name": "Monthly Maximum Call Usage",


    6

       "uri": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Usage/Triggers/UT33c6aeeba34e48f38d6899ea5b765ad4.json",


    7

       "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    8

       "callback_method": "POST",


    9

       "trigger_by": "usage",


    10

       "sid": "UT33c6aeeba34e48f38d6899ea5b765ad4",


    11

       "current_value": "21",


    12

       "date_created": "Sat, 29 Sep 2012 19:45:43 +0000",


    13

       "callback_url": "https://www.example.com/monthly-usage-trigger",


    14

       "recurring": null,


    15

       "usage_category": "calls",


    16

       "trigger_value": "500.000000"


    17

    }

(warning)

## Warning

Currently, you cannot update the category or value of an existing UsageTrigger. Instead, use `POST` to [create a new UsageTrigger](/docs/usage/api/usage-trigger#create-a-usagetrigger-resource "create a new UsageTrigger") and use `DELETE` to [remove an old UsageTrigger](/docs/usage/api/usage-trigger#delete-a-usagetrigger-resource "remove an old UsageTrigger").

Update a TriggerLink to code sample: Update a Trigger

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

    async function updateUsageTrigger() {


    11

      const trigger = await client.usage


    12

        .triggers("UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .update({ callbackMethod: "GET" });


    14




    15

      console.log(trigger.accountSid);


    16

    }


    17




    18

    updateUsageTrigger();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "api_version": "2010-04-01",


    4

      "callback_method": "GET",


    5

      "callback_url": "http://cap.com/streetfight",


    6

      "current_value": "0",


    7

      "date_created": "Sun, 06 Sep 2015 12:58:45 +0000",


    8

      "date_fired": null,


    9

      "date_updated": "Sun, 06 Sep 2015 12:58:45 +0000",


    10

      "friendly_name": "raphael-cluster-1441544325.86",


    11

      "recurring": "yearly",


    12

      "sid": "UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    13

      "trigger_by": "price",


    14

      "trigger_value": "50",


    15

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Triggers/UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    16

      "usage_category": "totalprice",


    17

      "usage_record_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records.json?Category=totalprice"


    18

    }

* * *

## Delete a UsageTrigger resource

delete-a-usagetrigger-resource page anchor

Positive FeedbackNegative Feedback

`DELETE https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Usage/Triggers/{Sid}.json`

### Path parameters

path-parameters-4 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the UsageTrigger resources to delete.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<UT>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the UsageTrigger resource to delete.

Pattern: `^UT[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Delete a TriggerLink to code sample: Delete a Trigger

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

    async function deleteUsageTrigger() {


    11

      await client.usage.triggers("UTaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").remove();


    12

    }


    13




    14

    deleteUsageTrigger();

### UsageTrigger Callbacks

usagetrigger-callbacks page anchor

Positive FeedbackNegative Feedback

As soon as the usage value of a UsageTrigger exceeds the `TriggerValue`, the trigger will fire and Twilio will make an asynchronous HTTP request to the UsageTrigger's `CallbackUrl`. This request will typically take place within a minute of exceeding the usage threshold.

#### CallbackUrl request parameters

callbackurl-request-parameters page anchor

Twilio will pass the following parameters to the UsageTrigger's `CallbackUrl`:

**Parameter**| **Description**
---|---
AccountSid| Your Twilio account id. It is 34 characters long and always starts with the letters `AC`
UsageTriggerSid| Unique identifier of the fired UsageTrigger.
DateFired| Date when the UsageTrigger fired, in GMT.
Recurring| How the fired UsageTrigger recurs. For non-recurring UsageTriggers: leave empty. For recurring UsageTriggers: choose `daily`, `monthly`, or `yearly`.
UsageCategory| Usage category watched by the UsageTrigger: choose from supported usage categories.
TriggerBy| UsageRecord field that fires the UsageTrigger: choose from `count`, `usage`, or `price`.
TriggerValue| Value at which the UsageTrigger fired.
CurrentValue| The current value of the usage watched by the UsageTrigger.
UsageRecordUri| URI of the UsageRecord that this UsageTrigger watched when it fired.
IdempotencyToken| A random token generated by Twilio and guaranteed to be unique for this particular firing of this UsageTrigger.

#### Best practices with UsageTrigger callbacks

best-practices-with-usagetrigger-callbacks page anchor

When implementing a handler for UsageTrigger's `CallbackUrl`, your handler may receive HTTP requests more than once. Services that handle duplicate requests and return the same response are called Idempotence.

We give you an `IdempotencyToken` that is unique for each Usage Trigger callback.

(information)

## Info

For more information about Idempotence, [see this wiki page(link takes you to an external page)](https://en.wikipedia.org/wiki/Idempotence "see this wiki page").

#### Example: daily recurring UsageTrigger's idempotency token

example-daily-recurring-usagetriggers-idempotency-token page anchor

Copy code block


    1

    ACed70abd024d3f57a4027b5dc2ca88d5b-FIRES-UTc142bed7b38c4f8186ef41a309814fd2-2012-10-04


    2

You can keep track of your `IdempotencyToken` to properly handle requests to your service and prevent a request from performing the same operation twice.

For example, your callback service may send billing notifications via email. For the best possible customer experience, you would want your customers only to receive the billing notification email once.

You can follow the test-and-set (external link) pattern to implement idempotent services. In short, you would test for the existence of the `IdempotencyToken` before processing your application's logic. This allows your application to handle existing tokens and choose the next appropriate step.

In the email example, you would have already sent the email to your customer then you would skip sending the email, instead replying with an HTTP status code of 200.

(information)

## Info

For more information on test-and-set, [see this wiki page(link takes you to an external page)](https://en.wikipedia.org/wiki/Test-and-set "see this wiki page").