# REST API: Usage Records

*Source: https://www.twilio.com/docs/usage/api/usage-record*

---

# REST API: Usage Records

Positive FeedbackNegative Feedback

* * *

The UsageRecords resource provides a simple API to retrieve actions made by your Twilio account during any period and by any usage category. This makes it easy to build reporting and analytics tools for your application.

UsageRecords used in combination with [Subaccounts](/docs/iam/api/subaccounts "Subaccounts") created for each of your end-users make it possible to build recurring usage-based billing systems on top of Twilio's API with just a few simple API calls. If rectifying UsageRecords with billing, [see our dedicated article](/docs/voice/resolve-call-log-usage-discrepancies "see our dedicated article").

You can also set up [usage triggers](/docs/usage/api/usage-trigger "usage triggers") to notify your application when a particular category of usage reaches a threshold on a daily, monthly, yearly, or all-time basis. Triggers can help determine if your users have reached a usage cap or if your application has runaway requests.

* * *

## Record Properties

record-properties page anchor

Positive FeedbackNegative Feedback

This resource and its subresources always return a list of UsageRecords. Each UsageRecord is represented by the following properties:

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that accrued the usage.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

apiVersionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The API version used to create the resource.

* * *

asOfstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Usage records up to date as of this timestamp, formatted as YYYY-MM-DDTHH:MM:SS+00:00. All timestamps are in GMT

* * *

categorystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The category of usage. For more information, see [Usage Categories](/docs/usage/api/usage-record#usage-categories "Usage Categories").

* * *

countstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The number of usage events, such as the number of calls.

* * *

countUnitstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The units in which `count` is measured, such as `calls` for calls or `messages` for SMS.

* * *

descriptionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A plain-language description of the usage category.

* * *

endDatestring<date>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The last date for which usage is included in the UsageRecord. The date is specified in GMT and formatted as `YYYY-MM-DD`.

* * *

pricenumber

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The total price of the usage in the currency specified in `price_unit` and associated with the account.

* * *

priceUnitstring<currency>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The currency in which `price` is measured, in [ISO 4127(link takes you to an external page)](https://www.iso.org/iso/home/standards/currency_codes.htm "ISO 4127") format, such as `usd`, `eur`, and `jpy`.

* * *

startDatestring<date>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The first date for which usage is included in this UsageRecord. The date is specified in GMT and formatted as `YYYY-MM-DD`.

* * *

subresourceUrisobject<uri-map>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A list of related resources identified by their URIs. For more information, see [List Subresources](/docs/usage/api/usage-record#list-subresources "List Subresources").

* * *

uristring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URI of the resource, relative to `https://api.twilio.com`.

* * *

usagestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The amount used to bill usage and measured in units described in `usage_unit`.

* * *

usageUnitstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The units in which `usage` is measured, such as `minutes` for calls or `messages` for SMS.

* * *

## Usage, Count, and Price

usage-count-price page anchor

Positive FeedbackNegative Feedback

Each UsageRecord contains three amounts: `Usage`, `Count`, and `Price`. `Usage` is the primary way usage is measured for that category: `minutes` for calls, `messages` for SMS, etc. `Count` is the number of usage events: `calls` for calls, etc. `Price` is the price of the usage in the currency associated with the account.

Each UsageRecord also has fields that show the units in which each amount is measured: `Usage` is measured in units of `UsageUnit`, for instance. These fields make it easy to build usage dashboards. For example, you can always display human-readable strings describing usage with "`$Usage $UsageUnits`", "`$Count $CountUnits`", or "`$Price $PriceUnits`".

* * *

## Usage Categories

usage-categories page anchor

Positive FeedbackNegative Feedback

A UsageRecord's `Category` defines the type of usage it represents. The full list of all categories is [here](/docs/usage/api/usage-record#usage-all-categories "here"), but you'll usually focus on just a few common categories:

Category| Description
---|---
calls| Inbound and outbound voice calls. Does _not_ include SIP or client calls. `Count` is the number of calls and `Usage` is the number of minutes.
sms| All SMS messages. `Count` and `Usage` are both the number of messages sent.
pfax-minutes| Programmable Fax minutes. `Count` is the number of faxes and `Usage` is the number of minutes.
pfax-pages| Programmable Fax pages. `Count` is the number of faxes and `Usage` is the number of pages.
phonenumbers| All phone numbers owned by the account.
recordings| Recordings of voice calls. `Count` is the number of recordings and `Usage` is the number of recorded minutes.
transcriptions| Transcriptions of voice calls. `Count` is the number of transcriptions and `Usage` is the number of transcribed minutes.
pv| All Programmable Video usage including TURN. `Price` accounts for expenses in all Programmable Video products. `Count` and `Usage` should be ignored.
totalprice| Total price of all usage. `Usage` will be the same as `Price`, and `Count` will be empty. Note that because some Twilio costs may not be included in any usage category, the sum of the `Price` of all UsageRecords may not be equal to the `Price` of `TotalPrice`.

* * *

## Read multiple UsageRecord resources

read-multiple-usagerecord-resources page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Usage/Records.json`

By default, the UsageRecords resource will return one UsageRecord for each `Category`, representing all usage accrued all-time for the account. You can filter the usage `Category` or change the date-range over which usage is counted using optional `GET` query parameters. Note that query parameters are case-sensitive:

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the UsageRecord resources to read.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

categorystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The [usage category](/docs/usage/api/usage-record#usage-categories "usage category") of the UsageRecord resources to read. Only UsageRecord resources in the specified category are retrieved.

* * *

startDatestring<date>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`. You can also specify offsets from the current date, such as: `-30days`, which will set the start date to be 30 days before the current date.

* * *

endDatestring<date>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`. You can also specify offsets from the current date, such as: `+30days`, which will set the end date to 30 days from the current date.

* * *

includeSubaccountsboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to include usage from the master account and all its subaccounts. Can be: `true` (the default) to include usage from the master account and all subaccounts or `false` to retrieve usage from only the specified account.

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

Last Month's Usage for All Usage CategoriesLink to code sample: Last Month's Usage for All Usage Categories

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

    async function listUsageRecordLastMonth() {


    11

      const lastMonths = await client.usage.records.lastMonth.list({ limit: 20 });


    12




    13

      lastMonths.forEach((l) => console.log(l.accountSid));


    14

    }


    15




    16

    listUsageRecordLastMonth();

### Response

Note about this response

Copy response


    1

    {


    2

      "end": 0,


    3

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/LastMonth.json?PageSize=50&Page=0",


    4

      "next_page_uri": null,


    5

      "page": 0,


    6

      "page_size": 50,


    7

      "previous_page_uri": null,


    8

      "start": 0,


    9

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/LastMonth.json?PageSize=50&Page=0",


    10

      "usage_records": [


    11

        {


    12

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    13

          "api_version": "2010-04-01",


    14

          "as_of": "2019-06-24T22:32:49+00:00",


    15

          "category": "sms-inbound-shortcode",


    16

          "count": "0",


    17

          "count_unit": "messages",


    18

          "description": "Short Code Inbound SMS",


    19

          "end_date": "2015-09-04",


    20

          "price": "0",


    21

          "price_unit": "usd",


    22

          "start_date": "2011-08-23",


    23

          "subresource_uris": {


    24

            "all_time": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/AllTime.json?Category=sms-inbound-shortcode",


    25

            "daily": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Daily.json?Category=sms-inbound-shortcode",


    26

            "last_month": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/LastMonth.json?Category=sms-inbound-shortcode",


    27

            "monthly": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Monthly.json?Category=sms-inbound-shortcode",


    28

            "this_month": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/ThisMonth.json?Category=sms-inbound-shortcode",


    29

            "today": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Today.json?Category=sms-inbound-shortcode",


    30

            "yearly": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Yearly.json?Category=sms-inbound-shortcode",


    31

            "yesterday": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Yesterday.json?Category=sms-inbound-shortcode"


    32

          },


    33

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/LastMonth.json?Category=sms-inbound-shortcode&StartDate=2011-08-23&EndDate=2015-09-04",


    34

          "usage": "0",


    35

          "usage_unit": "messages"


    36

        }


    37

      ]


    38

    }

Today's CallsLink to code sample: Today's Calls

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

    async function listUsageRecordToday() {


    11

      const todays = await client.usage.records.today.list({


    12

        category: "calls",


    13

        limit: 20,


    14

      });


    15




    16

      todays.forEach((t) => console.log(t.accountSid));


    17

    }


    18




    19

    listUsageRecordToday();

### Response

Note about this response

Copy response


    1

    {


    2

      "end": 0,


    3

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Today.json?PageSize=50&Page=0",


    4

      "next_page_uri": null,


    5

      "page": 0,


    6

      "page_size": 50,


    7

      "previous_page_uri": null,


    8

      "start": 0,


    9

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Today.json?PageSize=50&Page=0",


    10

      "usage_records": [


    11

        {


    12

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    13

          "api_version": "2010-04-01",


    14

          "as_of": "2019-06-24T22:32:49+00:00",


    15

          "category": "sms-inbound-shortcode",


    16

          "count": "0",


    17

          "count_unit": "messages",


    18

          "description": "Short Code Inbound SMS",


    19

          "end_date": "2015-09-04",


    20

          "price": "0",


    21

          "price_unit": "usd",


    22

          "start_date": "2011-08-23",


    23

          "subresource_uris": {


    24

            "all_time": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/AllTime.json?Category=sms-inbound-shortcode",


    25

            "daily": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Daily.json?Category=sms-inbound-shortcode",


    26

            "last_month": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/LastMonth.json?Category=sms-inbound-shortcode",


    27

            "monthly": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Monthly.json?Category=sms-inbound-shortcode",


    28

            "this_month": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/ThisMonth.json?Category=sms-inbound-shortcode",


    29

            "today": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Today.json?Category=sms-inbound-shortcode",


    30

            "yearly": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Yearly.json?Category=sms-inbound-shortcode",


    31

            "yesterday": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Yesterday.json?Category=sms-inbound-shortcode"


    32

          },


    33

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Today.json?Category=sms-inbound-shortcode&StartDate=2011-08-23&EndDate=2015-09-04",


    34

          "usage": "0",


    35

          "usage_unit": "messages"


    36

        }


    37

      ]


    38

    }

One-Month Date-Range, Inbound Calls OnlyLink to code sample: One-Month Date-Range, Inbound Calls Only

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

    async function listUsageRecord() {


    11

      const records = await client.usage.records.list({


    12

        category: "calls-inbound",


    13

        endDate: "2022-06-30",


    14

        startDate: "2022-06-01",


    15

        limit: 20,


    16

      });


    17




    18

      records.forEach((r) => console.log(r.accountSid));


    19

    }


    20




    21

    listUsageRecord();

### Response

Note about this response

Copy response


    1

    {


    2

      "end": 0,


    3

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records.json?Category=calleridlookups&StartDate=2008-01-02&EndDate=2008-01-02&PageSize=1&Page=0",


    4

      "next_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records.json?Category=calleridlookups&StartDate=2008-01-02&EndDate=2008-01-02&PageSize=1&Page=1&PageToken=APMQ%3D%3D",


    5

      "page": 0,


    6

      "page_size": 1,


    7

      "previous_page_uri": null,


    8

      "start": 0,


    9

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records.json?Category=calleridlookups&StartDate=2008-01-02&EndDate=2008-01-02&PageSize=1&Page=0",


    10

      "usage_records": [


    11

        {


    12

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    13

          "api_version": "2010-04-01",


    14

          "as_of": "2019-06-24T22:32:49+00:00",


    15

          "category": "calleridlookups",


    16

          "count": null,


    17

          "count_unit": "",


    18

          "description": "Caller Name Lookups",


    19

          "end_date": "2008-01-02",


    20

          "price": "2192.84855",


    21

          "price_unit": "usd",


    22

          "start_date": "2008-01-02",


    23

          "subresource_uris": {


    24

            "all_time": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/AllTime.json?Category=calleridlookups",


    25

            "daily": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Daily.json?Category=calleridlookups",


    26

            "last_month": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/LastMonth.json?Category=calleridlookups",


    27

            "monthly": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Monthly.json?Category=calleridlookups",


    28

            "this_month": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/ThisMonth.json?Category=calleridlookups",


    29

            "today": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Today.json?Category=calleridlookups",


    30

            "yearly": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Yearly.json?Category=calleridlookups",


    31

            "yesterday": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Yesterday.json?Category=calleridlookups"


    32

          },


    33

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records.json?Category=calleridlookups&StartDate=2008-01-02&EndDate=2008-01-02",


    34

          "usage": "2192.84855",


    35

          "usage_unit": "usd"


    36

        }


    37

      ]


    38

    }

Daily Usage for Inbound Calls Over a One-Month PeriodLink to code sample: Daily Usage for Inbound Calls Over a One-Month Period

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

    async function listUsageRecordDaily() {


    11

      const dailies = await client.usage.records.daily.list({


    12

        category: "calls-inbound",


    13

        endDate: "2022-06-30",


    14

        startDate: "2022-06-01",


    15

        limit: 20,


    16

      });


    17




    18

      dailies.forEach((d) => console.log(d.accountSid));


    19

    }


    20




    21

    listUsageRecordDaily();

### Response

Note about this response

Copy response


    1

    {


    2

      "end": 0,


    3

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Daily.json?PageSize=50&Page=0",


    4

      "next_page_uri": null,


    5

      "page": 0,


    6

      "page_size": 50,


    7

      "previous_page_uri": null,


    8

      "start": 0,


    9

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Daily.json?PageSize=50&Page=0",


    10

      "usage_records": [


    11

        {


    12

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    13

          "api_version": "2010-04-01",


    14

          "as_of": "2019-06-24T22:32:49+00:00",


    15

          "category": "sms-inbound-shortcode",


    16

          "count": "0",


    17

          "count_unit": "messages",


    18

          "description": "Short Code Inbound SMS",


    19

          "end_date": "2015-09-04",


    20

          "price": "0",


    21

          "price_unit": "usd",


    22

          "start_date": "2011-08-23",


    23

          "subresource_uris": {


    24

            "all_time": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/AllTime.json?Category=sms-inbound-shortcode",


    25

            "daily": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Daily.json?Category=sms-inbound-shortcode",


    26

            "last_month": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/LastMonth.json?Category=sms-inbound-shortcode",


    27

            "monthly": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Monthly.json?Category=sms-inbound-shortcode",


    28

            "this_month": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/ThisMonth.json?Category=sms-inbound-shortcode",


    29

            "today": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Today.json?Category=sms-inbound-shortcode",


    30

            "yearly": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Yearly.json?Category=sms-inbound-shortcode",


    31

            "yesterday": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Yesterday.json?Category=sms-inbound-shortcode"


    32

          },


    33

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Daily.json?Category=sms-inbound-shortcode&StartDate=2011-08-23&EndDate=2015-09-04",


    34

          "usage": "0",


    35

          "usage_unit": "messages"


    36

        }


    37

      ]


    38

    }

All-Time Usage, All Usage CategoriesLink to code sample: All-Time Usage, All Usage Categories

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

    async function listUsageRecord() {


    11

      const records = await client.usage.records.list({ limit: 20 });


    12




    13

      records.forEach((r) => console.log(r.accountSid));


    14

    }


    15




    16

    listUsageRecord();

### Response

Note about this response

Copy response


    1

    {


    2

      "end": 0,


    3

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records.json?Category=calleridlookups&StartDate=2008-01-02&EndDate=2008-01-02&PageSize=1&Page=0",


    4

      "next_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records.json?Category=calleridlookups&StartDate=2008-01-02&EndDate=2008-01-02&PageSize=1&Page=1&PageToken=APMQ%3D%3D",


    5

      "page": 0,


    6

      "page_size": 1,


    7

      "previous_page_uri": null,


    8

      "start": 0,


    9

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records.json?Category=calleridlookups&StartDate=2008-01-02&EndDate=2008-01-02&PageSize=1&Page=0",


    10

      "usage_records": [


    11

        {


    12

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    13

          "api_version": "2010-04-01",


    14

          "as_of": "2019-06-24T22:32:49+00:00",


    15

          "category": "calleridlookups",


    16

          "count": null,


    17

          "count_unit": "",


    18

          "description": "Caller Name Lookups",


    19

          "end_date": "2008-01-02",


    20

          "price": "2192.84855",


    21

          "price_unit": "usd",


    22

          "start_date": "2008-01-02",


    23

          "subresource_uris": {


    24

            "all_time": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/AllTime.json?Category=calleridlookups",


    25

            "daily": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Daily.json?Category=calleridlookups",


    26

            "last_month": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/LastMonth.json?Category=calleridlookups",


    27

            "monthly": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Monthly.json?Category=calleridlookups",


    28

            "this_month": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/ThisMonth.json?Category=calleridlookups",


    29

            "today": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Today.json?Category=calleridlookups",


    30

            "yearly": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Yearly.json?Category=calleridlookups",


    31

            "yesterday": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records/Yesterday.json?Category=calleridlookups"


    32

          },


    33

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Usage/Records.json?Category=calleridlookups&StartDate=2008-01-02&EndDate=2008-01-02",


    34

          "usage": "2192.84855",


    35

          "usage_unit": "usd"


    36

        }


    37

      ]


    38

    }

For example, you might request all usage records for the month of April, 2012. In this case, the query string would be `StartDate=2012-04-01&EndDate=2012-04-30`. This would return one UsageRecord for each usage-type summarizing the usage during April. The list includes [paging information](/docs/usage/twilios-response#pagination "paging information").

It's also possible to group usage by day, by month, or by year using the [subresources](/docs/usage/api/usage-record#list-subresources "subresources") described below.

### List Subresources

list-subresources page anchor

Positive FeedbackNegative Feedback

The main UsageRecords list resource supports a variety of convenience subresources. In general, these take the form:

Copy code block


    1

    /2010-04-01/Accounts/{AccountSid}/Usage/Records/{Subresource}


    2

Supported subresources are:

Subresource| Description
---|---
Daily| Return multiple UsageRecords for each usage category, each representing usage over a daily time interval.
Monthly| Return multiple UsageRecords for each usage category, each representing usage over a monthly time interval.
Yearly| Return multiple UsageRecords for each usage category, each representing usage over a yearly time interval.
AllTime| Return a single UsageRecord for each usage category, each representing usage over the date range specified. This is the same as the root /Usage/Records.
Today| Return a single UsageRecord per usage category, for today's usage only.
Yesterday| Return a single UsageRecord per usage category, for yesterday's usage only.
ThisMonth| Return a single UsageRecord per usage category, for this month's usage only.
LastMonth| Return a single UsageRecord per usage category, for last month's usage only.

These convenience subresources can be used to draw a graph of daily calls, display dashboards of monthly usage across all usage categories, or build a simple usage-based billing system based on last month's usage totals.

### Full List of All Usage Categories

usage-all-categories page anchor

Positive FeedbackNegative Feedback

#### Voice

usage-voice page anchor

Category| Description
---|---
agent-conference| Count is the number of agent conferences and Usage is the number of minutes.
answering-machine-detection| All answering machine detection recognitions for outbound calls. Count is the number of recognitions.
amazon-polly| Text-to-Speech generated with Amazon Polly voices.
calls| Inbound and outbound voice calls. Count is the number of calls and Usage is the number of minutes. Does _not_ include client or SIP calls.
calls-inbound| All inbound voice calls, to mobile, toll-free and local numbers.
calls-inbound-local| All inbound voice calls to local numbers.
calls-inbound-mobile| All inbound voice calls to mobile numbers.
calls-inbound-tollfree| All inbound voice calls to toll-free numbers.
calls-outbound| All outbound voice calls.
calls-sip| All SIP calls.
calls-sip-inbound| All inbound SIP calls.
calls-sip-outbound| All outbound SIP calls.
calls-client| All TwilioClient voice calls.
calls-globalconference| All global conference calls.
calls-media-stream-minutes| All Media Stream calls
calls-pay-verb-transactions| `<Pay>` verb transactions. Count is total number of `<Pay>` transactions
call-progess-events| All call progress events.
calls-recordings| Recordings of voice calls. Count is the number of recordings and Usage is the number of recorded minutes.
ivr-virtual-agent-genai| Virtual Agent Generative AI usage in calls. Count is the number of `<VirtualAgent>` invocations that used Generative AI and Usage is the number of minutes.
ivr-virtual-agent-custom-voices| Virtual Agent TTS Custom Voice Model usage in calls. Count is the number of `<VirtualAgent>` invocations that used a [TTS custom voice model(link takes you to an external page)](https://cloud.google.com/text-to-speech/custom-voice/docs "TTS custom voice model") and Usage is the number of minutes.
programmablevoice-platform| All Programmable Voice Platform usage in Flex Projects
programmablevoiceconnectivity| Inbound and outbound voice calls in Flex Projects. Count is the number of calls and Usage is the number of minutes. Includes Client and SIP Calls.
programmablevoiceconn-sip| All SIP Calls in Flex Projects
programmablevoiceconn-sip-inbound| All Inbound SIP Calls in Flex Projects
programmablevoiceconn-sip-outbound| All Outbound SIP Calls in Flex Projects
programmablevoiceconn-clientsdk| All TwilioClient voice calls in Flex Projects
pstnconnectivity| Inbound and outbound voice calls in Flex Projects. Count is the number of calls and Usage is the number of minutes.
pstnconnectivity-inbound| All inbound voice calls, to mobile, toll-free and local numbers in Flex Projects
pstnconnectivity-outbound| All outbound voice calls in Flex Projects
recordings| Recordings of voice and trunking calls. Count is the number of recordings and Usage is the number of recorded minutes.
recordingstorage| Amount of storage used by call recordings stored for the account. Count is the number of stored recordings, Usage is the number of stored recorded minutes, and Price is the price of storing the recordings.
speech-recognition| Speech recognitions in calls. Count is the total number of calls where speech recognition was performed and usage is the total number of recognitions
transcriptions| Transcriptions of voice calls. Count is the number of transcriptions and Usage is the number of transcribed minutes.
tts-google| Text-to-Speech generated with Google Polly voices.
virtual-agent| Virtual Agent usage in calls. Count is the number of `<VirtualAgent>` invocations and Usage is the number of minutes.
voice-intelligence| All Conversational Intelligence transcriptions and language operators minutes
voice-intelligence-transcription| Conversational Intelligence transcriptions minutes
voice-intelligence-operators| Conversational Intelligence language operators minutes
voice-insights| Voice Insights Advanced Features
voice-insights-ptsn-insights-on-demand-minute| Voice Insights Advanced Features for Programmable Voice calls
voice-insights-sip-trunking-insights-on-demand-minute| Voice Insights Advanced Features for Elastic SIP Trunking calls.

#### SMS & MMS

usage-sms-mms page anchor

Category| Description
---|---
a2p-registration-fees| All Messaging A2P Registration Fees
sms| All SMS messages, both inbound and outbound. Count and Usage are both the number of messages sent.
sms-inbound| All inbound SMS messages, to both short-codes and long-codes.
sms-inbound-longcode| All inbound SMS messages to long-codes.
sms-inbound-shortcode| All inbound SMS messages to short-codes.
sms-outbound| All outbound SMS messages, from both short-codes and long-codes.
sms-outbound-longcode| All outbound SMS messages from long-codes.
sms-outbound-shortcode| All outbound SMS messages from short-codes.
sms-messages-carrierfees| All carrier fees for SMS messages.
mms| All MMS messages, both inbound and outbound. Count and Usage are both the number of messages sent.
mms-inbound| All inbound MMS messages, to both short-codes and long-codes.
mms-inbound-longcode| All inbound MMS messages to long-codes.
mms-inbound-shortcode| All inbound MMS messages to short-codes.
mms-outbound| All outbound MMS messages, from both short-codes and long-codes.
mms-outbound-longcode| All outbound MMS messages from long-codes.
mms-outbound-shortcode| All outbound MMS messages from short-codes.
mms-messages-carrierfees| All carrier fees for MMS messages.
mediastorage| Amount of storage used by media stored for the account. Count is the number of stored media files, Usage is the number of megabytes, and Price is the price of storing the media.

#### RCS

usage-rcs page anchor

Category| Description
---|---
Usage-RCS-Messages| All RCS messages.
Usage-RCS-basic-Messages-Outbound| All outbound RCS Basic messages.
Usage-RCS-Single-Messages-Outbound| All outbound RCS Single messages.
Usage-RCS-Messages-Inbound| All inbound RCS messages.
Usage-RCS-Messaging-Carrier-Fees| All RCS message carrier fees.
RCS-Activation-Fee| All RCS sender activation fees.

#### WhatsApp Business API

usage-whatsapp page anchor

Category| Description
---|---
channels-whatsapp-template-authentication| WhatsApp charges Authentication template fees for using Authentication category templates. [See our pricing page for details.(link takes you to an external page)](https://www.twilio.com/en-us/whatsapp/pricing "See our pricing page for details.")
channels-whatsapp-template-marketing| WhatsApp charges Marketing template fees for using Marketing category templates. [See our pricing page for details.(link takes you to an external page)](https://www.twilio.com/en-us/whatsapp/pricing "See our pricing page for details.")
channels-whatsapp-template-utility| WhatsApp charges Utility template fees for using Utility category templates. [See our pricing page for details.(link takes you to an external page)](https://www.twilio.com/en-us/whatsapp/pricing "See our pricing page for details.")
channels-whatsapp-service| WhatsApp does not charge fees for using free-form messages during a customer service window. This billing item is used to track usage. [See our pricing page for details.(link takes you to an external page)](https://www.twilio.com/en-us/whatsapp/pricing "See our pricing page for details.")
channels-whatsapp-conversation-free| WhatsApp waives conversation fees for conversations opened by Click to WhatsApp Ads or for the first 1,000 Service conversations opened by a WhatsApp Business Account each month. [See our pricing page for details.(link takes you to an external page)](https://www.twilio.com/en-us/whatsapp/pricing "See our pricing page for details.")
channels-messaging-inbound| Twilio charges a flat-rate per inbound message platform fee for any country.
channels-messaging-outbound| Twilio charges a flat-rate per outbound message platform fee for any country.

#### Twilio Conversations

usage-prog-chat page anchor

Category| Description
---|---
pchat-users| Active Monthly Users - An active user is defined as someone who creates a user or conversation, edits, or is assigned to a conversation. This includes reading conversations, sending messages in a chat view, or sending and receiving SMS and WhatsApp messages via the Conversations product.
pchat-conv-med-storage| Media Storage - Photos, videos, or other files stored and distributed in Conversations are billed at a monthly rate according to their size, prorated daily. Only stored media (pictures, videos, etc.) incurs a charge; ordinary text-only message bodies are stored at no cost.

#### Phone Numbers

usage-phone-numbers page anchor

Category| Description
---|---
phonenumbers| All phone numbers owned by the account, mobile, toll-free and local.
phonenumbers-local| All local phone numbers owned by the account.
phonenumbers-mobile| All mobile phone numbers owned by the account.
phonenumbers-tollfree| All toll-free phone numbers owned by the account.
phonenumbers-cps| All phone number calls per second (CPS) increases.
phonenumbers-setups| All phone number setups fees.
shortcodes| All short codes owned by the account, of all types.
shortcodes-customerowned| All short codes owned by the account that are leased from another provider.
shortcodes-mms-enablement| All short code MMS enablement fees.
shortcodes-mps| All short code message per second (MPS) increases.
shortcodes-random| All randomly-assigned short codes owned by the account.
shortcodes-uk| All UK short codes owned by the account.
shortcodes-vanity| All vanity short codes owned by the account.

#### Lookup

usage-lookups page anchor

Category| Description
---|---
lookups| All Lookups executed across all categories
carrier-lookups| All Carrier lookups
calleridlookups| All Caller Name lookups
number-format-lookups| All Number Formatting lookups
call-forwarding-lookups| All Call Forwarding lookups
sim-swap-lookups| All SIM Swap lookups
live-activity-lookups| All Live Activity lookups
enhanced-line-type-lookups| All Line Type Intelligence lookups
identity-match| All Identity Match lookups

#### Elastic SIP Trunking

usage-elastic-sip-trunking page anchor

Category| Description
---|---
trunking-origination| All trunking origination (inbound) calls, to mobile, toll-free and local numbers.
trunking-origination-local| All trunking origination (inbound) calls to local numbers.
trunking-origination-mobile| All trunking origination (inbound) calls to mobile numbers.
trunking-origination-tollfree| All trunking origination (inbound) calls to toll-free numbers.
trunking-termination| All trunking termination (outbound) calls.
trunking-recordings| Recordings of trunking calls. Count is the number of recordings and Usage is the number of recorded minutes.
trunking-cps| All trunking calls per second (CPS) increases.
trunking-secure| All secured trunking calls.
voice-insights-sip-trunking-insights-on-demand-minute| Voice Insights Advanced Features for trunking calls

#### Sync

usage-sync page anchor

Category| Description
---|---
sync-actions| All incoming requests from your application that read and write data. It means actions include any read or write from an SDK or the REST API. Resulting webhooks, updates to connected endpoints, and storage are included in the cost of an action.
sync-endpoint-hours| An endpoint-hour is counted once per wall-clock hour for each unique device connected to Sync. Endpoints can be unique devices or browser tabs. Each unique endpoint will incur charges for at most four hours of every calendar day; the remainder are free of charge.
sync-endpoint-hours-above-daily-cap| All hours spent above four hours limit are shown separately. All these hours are free of charge.

#### Task Router

usage-task-router page anchor

Category| Description
---|---
taskrouter-tasks| All tasks created in Task Router.

#### Programmable Video

usage-video page anchor

Category| Description
---|---
pv| All Programmable Video usage including TURN. `Price` accounts for expenses in all Programmable Video products. `Count` and `Usage` should be ignored.
group-rooms| Accounts for all Group Rooms usage. `Count` is the number of rooms. `Usage` should be ignored.
group-rooms-participant-minutes| All participant usage in Group Rooms. `Count` and `Usage` measure the number of participant minutes.
group-rooms-data-track| All Group Room Data Tracks activity. `Count` and `Usage` measure thousands of messages sent.
small-group-rooms| Accounts for all Small Group Rooms usage. `Count` is the number of rooms. `Usage` should be ignored.
small-group-rooms-participant-minutes| All participant usage in Small Group Rooms. `Count` and `Usage` measure the number of participant minutes.
small-group-rooms-data-track| All Small Group Room Data Tracks activity. `Count` and `Usage` measure thousands of messages sent.
pv-rooms| Accounts for all Peer-to-Peer Rooms usage. `Count` is the number of rooms. `Usage` is the number of participant minutes.
peer-to-peer-rooms-participant-minutes| All participant usage in P2P Rooms. `Count` and `Usage` measure the number of participant minutes.
video-recordings| All usage regarding video Recordings and Compositions. `Count` and `Usage` should be ignored.
group-rooms-recorded-minutes| All Recordings generated out of Group Rooms (including Small Group Rooms). `Count` and `Usage` measure the number of recorded participant minutes.
pv-composition-minutes| All Video Recording Compositions. `Count` and `Usage` measure the number of composition minutes.
group-rooms-encrypted-media-recorded| All encrypted media including Group Room Recordings and Compositions. `Count` and `Usage` measure the number of encrypted participant minutes and composition minutes.
group-rooms-media-stored| All media stored in Twilio by Programmable Video Services including Recordings and Compositions. `Count` and `Usage` measure the number of stored GB/day (Gigabytes per day).
group-rooms-media-downloaded| All media downloaded from Twilio regarding Programmable Video Services. This includes Recordings and Compositions. `Count` and `Usage` measure the number of downloaded GB (Gigabytes).
turnmegabytes| All TURN data relayed by Twilio. `Count` and `Usage` measure the relayed traffic in MB (Megabytes)
turnmegabytes-australia| TURN data relayed by Twilio in the Australia AWS region. `Count` and `Usage` measure the relayed traffic in MB (Megabytes)
turnmegabytes-brasil| TURN data relayed by Twilio in the Brazil AWS region. `Count` and `Usage` measure the relayed traffic in MB (Megabytes)
turnmegabytes-india| TURN data relayed by Twilio in the India AWS region. `Count` and `Usage` measure the relayed traffic in MB (Megabytes)
turnmegabytes-ireland| TURN data relayed by Twilio in the Ireland AWS region. `Count` and `Usage` measure the relayed traffic in MB (Megabytes)
turnmegabytes-japan| TURN data relayed by Twilio in the Japan AWS region. `Count` and `Usage` measure the relayed traffic in MB (Megabytes)
turnmegabytes-singapore| TURN data relayed by Twilio in the Singapore AWS region. `Count` and `Usage` measure the relayed traffic in MB (Megabytes)
turnmegabytes-useast| TURN data relayed by Twilio in the US (East) AWS region. `Count` and `Usage` measure the relayed traffic in MB (Megabytes)
turnmegabytes-uswest| TURN data relayed by Twilio in the US (West) AWS region. `Count` and `Usage` measure the relayed traffic in MB (Megabytes)
turnmegabytes-germany| TURN data relayed by Twilio in the Germany AWS region. `Count` and `Usage` measure the relayed traffic in MB (Megabytes)

#### Programmable Chat

usage-prog-chat-1 page anchor

Category| Description
---|---
pchat-users| Active Monthly Users - An active user is defined as someone who creates a user or conversation, or edits, or is assigned to a chat channel. This includes reading conversations or sending messages.
pchat-conv-med-storage| Media Storage - Photos, videos, or other files stored and distributed in chat channels are billed at a monthly rate according to their size, prorated daily. Only stored media (pictures, videos, etc.) incurs a charge; ordinary text-only message bodies are stored at no cost.

#### Verify

usage-verify page anchor

Category| Description
---|---
verify-push| All Verify push verifications. Each verification is defined as a challenge that is updated with a status of `approved` or `denied`.
verify-totp| All Verify TOTP verifications. Each verification is defined as a challenge that is updated with a status of `approved`.
verify-sna| All Verify Silent Network Auth (SNA) verifications.
authy-phone-verifications| All Verify SMS and Voice verifications.
authy-verify-email-verifications| All Verify email verifications.
authy-verify-outbound-email| All Verify one-time tokens requested to be delivered via email.
verify-whatsapp-template-business-initiated| All WhatsApp messages associated with using Verify to send one-time-passcode messages to WhatsApp users.

#### Authy

usage-authy page anchor

Category| Description
---|---
authy-authentications| All Authy authentications.
authy-calls-outbound| All Authy outbound calls. Note that this usage is also included in the Voice categories.
authy-monthly-fees| All Authy monthly fees.
authy-phone-intelligence| All Authy phone intelligence requests.
authy-sms-outbound| All Authy and Verify outbound SMS messages. Note that this usage is also included in the SMS categories.
authy-outbound-email| All Authy one-time tokens requested to be delivered via email.

#### Studio

usage-studio page anchor

Category| Description
---|---
studio-engagements| All Studio Engagements

#### Monitor

usage-monitor page anchor

Category| Description
---|---
monitor-reads| All Monitor events API reads.
monitor-writes| All Monitor events writes.
monitor-storage| All Monitor events storage fees.

#### Event Streams

usage-eventstreams page anchor

Category| Description
---|---
events| All Event Streams events delivered. Usage is in thousands of events.

#### Engagement Suite

usage-engagement-suite page anchor

Category| Description
---|---
engagement-suite-packaged-plans| All Engagement Suite packaged plans enabled on account.
sms-messages-features-engagement-suite| All Engagement Suite-enabled messages. `Count` and `Usage` are both the number of messages sent.

#### Other

usage-other page anchor

Category| Description
---|---
premiumsupport| All premium support fees.
totalprice| Total price of all usage. Usage will be the same as Price, and Count will be empty. Note that because some Twilio costs may not be included in any usage category, the sum of the Price in all UsageRecords may or may not be equal to the Price of TotalPrice.