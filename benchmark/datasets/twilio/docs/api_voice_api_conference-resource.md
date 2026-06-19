# Conferences resource

*Source: https://www.twilio.com/docs/voice/api/conference-resource*

---

# Conferences resource

Positive FeedbackNegative Feedback

* * *

The Conferences resource allows you to query and manage the state of [conferences](/docs/voice/conference "conferences") on your Twilio account.

(information)

## Info

Conference rooms are not directly created from the Programmable Voice API.

In order to create a new conference, you must use [TwiML's <Dial> verb](/docs/voice/twiml/dial "TwiML's <Dial> verb") with the [<Conference> noun,](/docs/voice/twiml/conference "<Conference> noun,") or by [creating a conference participant using the /Participants API](/docs/voice/api/conference-participant-resource "creating a conference participant using the /Participants API"). After a **Conference** instance has been created, you can access it by using the REST API.

For step-by-step instructions on how to write this TwiML and programmatically handle the conference, check out our guides on [how to create conference calls using Twilio's supported SDKs](/docs/voice/tutorials/how-to-create-conference-calls "how to create conference calls using Twilio's supported SDKs").

* * *

## Conferences properties

conferences-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created this Conference resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

dateCreatedstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in UTC that this resource was created specified in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.

* * *

dateUpdatedstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in UTC that this resource was last updated, specified in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.

* * *

apiVersionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The API version used to create this conference.

* * *

friendlyNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A string that you assigned to describe this conference room. Maximum length is 128 characters.

* * *

regionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A string that represents the Twilio Region where the conference audio was mixed. May be `us1`, `us2`, `ie1`, `de1`, `sg1`, `br1`, `au1`, and `jp1`. Basic conference audio will always be mixed in `us1`. Global Conference audio will be mixed nearest to the majority of participants.

* * *

sidSID<CF>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique, Twilio-provided string used to identify this Conference resource.

Pattern: `^CF[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

statusenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The status of this conference. Can be: `init`, `in-progress`, or `completed`.

Possible values:

`init``in-progress``completed`

* * *

uristring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URI of this resource, relative to `https://api.twilio.com`.

* * *

subresourceUrisobject<uri-map>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A list of related resources identified by their URIs relative to `https://api.twilio.com`.

* * *

reasonConferenceEndedenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The reason why a conference ended. When a conference is in progress, will be `null`. When conference is completed, can be: `conference-ended-via-api`, `participant-with-end-conference-on-exit-left`, `participant-with-end-conference-on-exit-kicked`, `last-participant-kicked`, or `last-participant-left`.

Possible values:

`conference-ended-via-api``participant-with-end-conference-on-exit-left``participant-with-end-conference-on-exit-kicked``last-participant-kicked``last-participant-left`

* * *

callSidEndingConferenceSID<CA>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The call SID that caused the conference to end.

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

(warning)

## Warning

You may have many conference instances that share the same `friendly_name`. Only **one** of these distinct conferences may be in-progress at any given time. For instance, if you have two separate conferences with the `friendly_name` of `"my-conference"` you cannot add participants to one instance while the other is in progress.

* * *

## Retrieve a Conference

retrieve-a-conference page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Conferences/{Sid}.json`

(information)

## Info

The recommended way to monitor the state of a Conference and its participants is to use the Conference [statusCallback](/docs/voice/twiml/conference#attributes-statusCallback "statusCallback"). This webhook callback will be fired when the state of the Conference or a participant changes.

At any time you can use the REST API to query the Conferences resource and [Participants](/docs/voice/api/conference-participant-resource "Participants") subresource, however continuously polling these resources is **not** recommended.

When fetching conferences after the conference has ended, associated Participants will not be returned. For retrieving conference participants after a conference has ended, see the [Conferences resource](/docs/voice/voice-insights/api/conference/conference-summary-resource "Conferences resource") of the Voice Insights API.

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Conference resource(s) to fetch.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<CF>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the Conference resource to fetch

Pattern: `^CF[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Retrieve a ConferenceLink to code sample: Retrieve a Conference

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

    async function fetchConference() {


    11

      const conference = await client


    12

        .conferences("CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .fetch();


    14




    15

      console.log(conference.accountSid);


    16

    }


    17




    18

    fetchConference();

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

      "date_created": "Fri, 18 Feb 2011 19:26:50 +0000",


    5

      "date_updated": "Fri, 18 Feb 2011 19:27:33 +0000",


    6

      "friendly_name": "AHH YEAH",


    7

      "sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    8

      "region": "us1",


    9

      "status": "completed",


    10

      "subresource_uris": {


    11

        "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json",


    12

        "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json"


    13

      },


    14

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    15

      "reason_conference_ended": "last-participant-left",


    16

      "call_sid_ending_conference": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    17

    }

* * *

## Retrieve a list of Conferences

retrieve-a-list-of-conferences page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Conferences.json`

Read all the conferences within your account.

The list of conferences that we return includes [paging information](/docs/usage/twilios-response#pagination "paging information").

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Conference resource(s) to read.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

dateCreatedstring<date>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Only include conferences that were created on this date. Specify a date as `YYYY-MM-DD` in UTC, for example: `2009-07-06`, to read only conferences that were created on this date. You can also specify an inequality, such as `DateCreated<=YYYY-MM-DD`, to read conferences that were created on or before midnight of this date, and `DateCreated>=YYYY-MM-DD` to read conferences that were created on or after midnight of this date.

* * *

dateCreatedBeforestring<date>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Only include conferences that were created on this date. Specify a date as `YYYY-MM-DD` in UTC, for example: `2009-07-06`, to read only conferences that were created on this date. You can also specify an inequality, such as `DateCreated<=YYYY-MM-DD`, to read conferences that were created on or before midnight of this date, and `DateCreated>=YYYY-MM-DD` to read conferences that were created on or after midnight of this date.

* * *

dateCreatedAfterstring<date>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Only include conferences that were created on this date. Specify a date as `YYYY-MM-DD` in UTC, for example: `2009-07-06`, to read only conferences that were created on this date. You can also specify an inequality, such as `DateCreated<=YYYY-MM-DD`, to read conferences that were created on or before midnight of this date, and `DateCreated>=YYYY-MM-DD` to read conferences that were created on or after midnight of this date.

* * *

dateUpdatedstring<date>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Only include conferences that were last updated on this date. Specify a date as `YYYY-MM-DD` in UTC, for example: `2009-07-06`, to read only conferences that were last updated on this date. You can also specify an inequality, such as `DateUpdated<=YYYY-MM-DD`, to read conferences that were last updated on or before midnight of this date, and `DateUpdated>=YYYY-MM-DD` to read conferences that were last updated on or after midnight of this date.

* * *

dateUpdatedBeforestring<date>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Only include conferences that were last updated on this date. Specify a date as `YYYY-MM-DD` in UTC, for example: `2009-07-06`, to read only conferences that were last updated on this date. You can also specify an inequality, such as `DateUpdated<=YYYY-MM-DD`, to read conferences that were last updated on or before midnight of this date, and `DateUpdated>=YYYY-MM-DD` to read conferences that were last updated on or after midnight of this date.

* * *

dateUpdatedAfterstring<date>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Only include conferences that were last updated on this date. Specify a date as `YYYY-MM-DD` in UTC, for example: `2009-07-06`, to read only conferences that were last updated on this date. You can also specify an inequality, such as `DateUpdated<=YYYY-MM-DD`, to read conferences that were last updated on or before midnight of this date, and `DateUpdated>=YYYY-MM-DD` to read conferences that were last updated on or after midnight of this date.

* * *

friendlyNamestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The string that identifies the Conference resources to read.

* * *

statusenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The status of the resources to read. Can be: `init`, `in-progress`, or `completed`.

Possible values:

`init``in-progress``completed`

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

Retrieve a list of ConferencesLink to code sample: Retrieve a list of Conferences

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

    async function listConference() {


    11

      const conferences = await client.conferences.list({ limit: 20 });


    12




    13

      conferences.forEach((c) => console.log(c.accountSid));


    14

    }


    15




    16

    listConference();

### Response

Note about this response

Copy response


    1

    {


    2

      "conferences": [


    3

        {


    4

          "status": "in-progress",


    5

          "region": "jp1",


    6

          "sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    7

          "date_updated": "Fri, 03 Jul 2020 11:23:45 +0000",


    8

          "date_created": "Fri, 03 Jul 2020 11:23:45 +0000",


    9

          "subresource_uris": {


    10

            "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json",


    11

            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json"


    12

          },


    13

          "friendly_name": "friendly_name",


    14

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    15

          "api_version": "2010-04-01",


    16

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

          "reason_conference_ended": null,


    18

          "call_sid_ending_conference": null


    19

        },


    20

        {


    21

          "status": "in-progress",


    22

          "region": "de1",


    23

          "sid": "CFbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",


    24

          "date_updated": "Thu, 02 Jul 2020 11:23:45 +0000",


    25

          "date_created": "Thu, 02 Jul 2020 11:23:45 +0000",


    26

          "subresource_uris": {


    27

            "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/Participants.json",


    28

            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/Recordings.json"


    29

          },


    30

          "friendly_name": "MyRoom",


    31

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.json",


    32

          "api_version": "2010-04-01",


    33

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    34

          "reason_conference_ended": null,


    35

          "call_sid_ending_conference": null


    36

        },


    37

        {


    38

          "status": "completed",


    39

          "region": "br1",


    40

          "sid": "CFcccccccccccccccccccccccccccccccc",


    41

          "date_updated": "Wed, 01 Jul 2020 11:23:45 +0000",


    42

          "date_created": "Wed, 01 Jul 2020 11:23:45 +0000",


    43

          "subresource_uris": {


    44

            "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFcccccccccccccccccccccccccccccccc/Participants.json",


    45

            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFcccccccccccccccccccccccccccccccc/Recordings.json"


    46

          },


    47

          "friendly_name": "FRIEND",


    48

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFcccccccccccccccccccccccccccccccc.json",


    49

          "api_version": "2010-04-01",


    50

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    51

          "reason_conference_ended": "participant-with-end-conference-on-exit-left",


    52

          "call_sid_ending_conference": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    53

        }


    54

      ],


    55

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?PageSize=3&Page=0",


    56

      "next_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?PageSize=3&Page=1&PageToken=PACFcccccccccccccccccccccccccccccccc",


    57

      "previous_page_uri": null,


    58

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?PageSize=3&Page=0",


    59

      "page": 0,


    60

      "page_size": 3,


    61

      "start": 0,


    62

      "end": 2


    63

    }

Retrieve a list of Conferences that started on a specific dateLink to code sample: Retrieve a list of Conferences that started on a specific date

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

    async function listConference() {


    11

      const conferences = await client.conferences.list({


    12

        dateCreated: "2020-07-07",


    13

        limit: 20,


    14

      });


    15




    16

      conferences.forEach((c) => console.log(c.accountSid));


    17

    }


    18




    19

    listConference();

### Response

Note about this response

Copy response


    1

    {


    2

      "conferences": [


    3

        {


    4

          "status": "in-progress",


    5

          "region": "jp1",


    6

          "sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    7

          "date_updated": "Tue, 07 Jul 2020 11:23:45 +0000",


    8

          "date_created": "Tue, 07 Jul 2020 11:23:45 +0000",


    9

          "subresource_uris": {


    10

            "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json",


    11

            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json"


    12

          },


    13

          "friendly_name": "friendly_name",


    14

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    15

          "api_version": "2010-04-01",


    16

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

          "reason_conference_ended": null,


    18

          "call_sid_ending_conference": null


    19

        },


    20

        {


    21

          "status": "in-progress",


    22

          "region": "de1",


    23

          "sid": "CFbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",


    24

          "date_updated": "Tue, 07 Jul 2020 11:23:45 +0000",


    25

          "date_created": "Tue, 07 Jul 2020 11:23:45 +0000",


    26

          "subresource_uris": {


    27

            "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/Participants.json",


    28

            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/Recordings.json"


    29

          },


    30

          "friendly_name": "MyRoom",


    31

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.json",


    32

          "api_version": "2010-04-01",


    33

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    34

          "reason_conference_ended": null,


    35

          "call_sid_ending_conference": null


    36

        },


    37

        {


    38

          "status": "completed",


    39

          "region": "br1",


    40

          "sid": "CFcccccccccccccccccccccccccccccccc",


    41

          "date_updated": "Tue, 07 Jul 2020 11:23:45 +0000",


    42

          "date_created": "Tue, 07 Jul 2020 11:23:45 +0000",


    43

          "subresource_uris": {


    44

            "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFcccccccccccccccccccccccccccccccc/Participants.json",


    45

            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFcccccccccccccccccccccccccccccccc/Recordings.json"


    46

          },


    47

          "friendly_name": "FRIEND",


    48

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFcccccccccccccccccccccccccccccccc.json",


    49

          "api_version": "2010-04-01",


    50

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    51

          "reason_conference_ended": "participant-with-end-conference-on-exit-left",


    52

          "call_sid_ending_conference": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    53

        }


    54

      ],


    55

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?DateCreated=2020-07-07&PageSize=3&Page=0",


    56

      "next_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?DateCreated=2020-07-07&PageSize=3&Page=1&PageToken=PACFcccccccccccccccccccccccccccccccc",


    57

      "previous_page_uri": null,


    58

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?DateCreated=2020-07-07&PageSize=3&Page=0",


    59

      "page": 0,


    60

      "page_size": 3,


    61

      "start": 0,


    62

      "end": 2


    63

    }

Retrieve a list of in-progress Conferences that were created on or after a specific dateLink to code sample: Retrieve a list of in-progress Conferences that were created on or after a specific date

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

    async function listConference() {


    11

      const conferences = await client.conferences.list({


    12

        dateCreated: "2021-01-01",


    13

        status: "in-progress",


    14

        limit: 20,


    15

      });


    16




    17

      conferences.forEach((c) => console.log(c.accountSid));


    18

    }


    19




    20

    listConference();

### Response

Note about this response

Copy response


    1

    {


    2

      "conferences": [


    3

        {


    4

          "status": "in-progress",


    5

          "region": "jp1",


    6

          "sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    7

          "date_updated": "Fri, 01 Jan 2021 11:23:45 +0000",


    8

          "date_created": "Fri, 01 Jan 2021 11:23:45 +0000",


    9

          "subresource_uris": {


    10

            "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json",


    11

            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json"


    12

          },


    13

          "friendly_name": "friendly_name",


    14

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    15

          "api_version": "2010-04-01",


    16

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

          "reason_conference_ended": null,


    18

          "call_sid_ending_conference": null


    19

        },


    20

        {


    21

          "status": "in-progress",


    22

          "region": "de1",


    23

          "sid": "CFbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",


    24

          "date_updated": "Fri, 01 Jan 2021 11:23:45 +0000",


    25

          "date_created": "Fri, 01 Jan 2021 11:23:45 +0000",


    26

          "subresource_uris": {


    27

            "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/Participants.json",


    28

            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/Recordings.json"


    29

          },


    30

          "friendly_name": "MyRoom",


    31

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.json",


    32

          "api_version": "2010-04-01",


    33

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    34

          "reason_conference_ended": null,


    35

          "call_sid_ending_conference": null


    36

        },


    37

        {


    38

          "status": "in-progress",


    39

          "region": "br1",


    40

          "sid": "CFcccccccccccccccccccccccccccccccc",


    41

          "date_updated": "Fri, 01 Jan 2021 11:23:45 +0000",


    42

          "date_created": "Fri, 01 Jan 2021 11:23:45 +0000",


    43

          "subresource_uris": {


    44

            "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFcccccccccccccccccccccccccccccccc/Participants.json",


    45

            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFcccccccccccccccccccccccccccccccc/Recordings.json"


    46

          },


    47

          "friendly_name": "FRIEND",


    48

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFcccccccccccccccccccccccccccccccc.json",


    49

          "api_version": "2010-04-01",


    50

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    51

          "reason_conference_ended": null,


    52

          "call_sid_ending_conference": null


    53

        }


    54

      ],


    55

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?Status=in-progress&DateCreated%3E=2021-01-01&PageSize=20&Page=0",


    56

      "next_page_uri": null,


    57

      "previous_page_uri": null,


    58

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?Status=in-progress&DateCreated%3E=2021-01-01&PageSize=20&Page=0",


    59

      "page": 0,


    60

      "page_size": 20,


    61

      "start": 0,


    62

      "end": 2


    63

    }

Retrieve a list of Conferences named 'MyRoom'Link to code sample: Retrieve a list of Conferences named 'MyRoom'

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

    async function listConference() {


    11

      const conferences = await client.conferences.list({


    12

        friendlyName: "MyRoom",


    13

        limit: 20,


    14

      });


    15




    16

      conferences.forEach((c) => console.log(c.accountSid));


    17

    }


    18




    19

    listConference();

### Response

Note about this response

Copy response


    1

    {


    2

      "conferences": [


    3

        {


    4

          "status": "in-progress",


    5

          "region": "jp1",


    6

          "sid": "CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    7

          "date_updated": "Sun, 03 Jan 2021 11:23:45 +0000",


    8

          "date_created": "Sun, 03 Jan 2021 11:23:45 +0000",


    9

          "subresource_uris": {


    10

            "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json",


    11

            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json"


    12

          },


    13

          "friendly_name": "MyRoom",


    14

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    15

          "api_version": "2010-04-01",


    16

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

          "reason_conference_ended": null,


    18

          "call_sid_ending_conference": null


    19

        },


    20

        {


    21

          "status": "completed",


    22

          "region": "us1",


    23

          "sid": "CFbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",


    24

          "date_updated": "Sat, 02 Jan 2021 11:23:45 +0000",


    25

          "date_created": "Sat, 02 Jan 2021 11:23:45 +0000",


    26

          "subresource_uris": {


    27

            "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/Participants.json",


    28

            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb/Recordings.json"


    29

          },


    30

          "friendly_name": "MyRoom",


    31

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.json",


    32

          "api_version": "2010-04-01",


    33

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    34

          "reason_conference_ended": "last-participant-left",


    35

          "call_sid_ending_conference": "CAbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"


    36

        },


    37

        {


    38

          "status": "completed",


    39

          "region": "ie1",


    40

          "sid": "CFcccccccccccccccccccccccccccccccc",


    41

          "date_updated": "Fri, 01 Jan 2021 11:23:45 +0000",


    42

          "date_created": "Fri, 01 Jan 2021 11:23:45 +0000",


    43

          "subresource_uris": {


    44

            "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFcccccccccccccccccccccccccccccccc/Participants.json",


    45

            "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFcccccccccccccccccccccccccccccccc/Recordings.json"


    46

          },


    47

          "friendly_name": "MyRoom",


    48

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFcccccccccccccccccccccccccccccccc.json",


    49

          "api_version": "2010-04-01",


    50

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    51

          "reason_conference_ended": "last-participant-left",


    52

          "call_sid_ending_conference": "CAcccccccccccccccccccccccccccccccc"


    53

        }


    54

      ],


    55

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?FriendlyName=MyRoom&PageSize=20&Page=0",


    56

      "next_page_uri": null,


    57

      "previous_page_uri": null,


    58

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences.json?FriendlyName=MyRoom&PageSize=20&Page=0",


    59

      "page": 0,


    60

      "page_size": 20,


    61

      "start": 0,


    62

      "end": 2


    63

    }

* * *

## Update a Conference

update-a-conference page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Conferences/{Sid}.json`

You can use the update action to change the conference's properties as well as to end the conference.

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Conference resource(s) to update.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidstring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the Conference resource to update

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

statusenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Possible values:

`completed`

* * *

announceUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we should call to announce something into the conference. The URL may return an MP3 file, a WAV file, or a TwiML document that contains `<Play>`, `<Say>`, `<Pause>`, or `<Redirect>` verbs.

* * *

announceMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method used to call `announce_url`. Can be: `GET` or `POST` and the default is `POST`

Possible values:

`GET``POST`

Select from available examples

Copy code block


    {


      "Status": "completed"


    }

Update a Conference: End the conferenceLink to code sample: Update a Conference: End the conference

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

    async function updateConference() {


    11

      const conference = await client


    12

        .conferences("Sid")


    13

        .update({ status: "completed" });


    14




    15

      console.log(conference.accountSid);


    16

    }


    17




    18

    updateConference();

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

      "date_created": "Mon, 22 Aug 2011 20:58:45 +0000",


    5

      "date_updated": "Mon, 22 Aug 2011 20:58:46 +0000",


    6

      "friendly_name": null,


    7

      "region": "us1",


    8

      "sid": "Sid",


    9

      "status": "completed",


    10

      "subresource_uris": {


    11

        "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json",


    12

        "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json"


    13

      },


    14

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    15

      "reason_conference_ended": "conference-ended-via-api",


    16

      "call_sid_ending_conference": null


    17

    }

Update a Conference: Announce to the ConferenceLink to code sample: Update a Conference: Announce to the Conference

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

    async function updateConference() {


    11

      const conference = await client


    12

        .conferences("Sid")


    13

        .update({ announceUrl: "http://www.myapp.com/announce" });


    14




    15

      console.log(conference.accountSid);


    16

    }


    17




    18

    updateConference();

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

      "date_created": "Mon, 08 Feb 2021 20:58:45 +0000",


    5

      "date_updated": "Mon, 08 Feb 2021 20:58:46 +0000",


    6

      "friendly_name": "MyRoom",


    7

      "region": "us1",


    8

      "sid": "Sid",


    9

      "status": "in-progress",


    10

      "subresource_uris": {


    11

        "participants": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants.json",


    12

        "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json"


    13

      },


    14

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conferences/CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    15

      "reason_conference_ended": null,


    16

      "call_sid_ending_conference": null


    17

    }

* * *

## Manage conference participants

manage-conference-participants page anchor

Positive FeedbackNegative Feedback

Each Conference resource has a Participant subresource. Participants represent the set of people currently connected to a running conference.

You can retrieve a list of Participants from a given Conference by requesting the following:

Copy code block


    GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants.json

Learn more about [Participants subresource](/docs/voice/api/conference-participant-resource "Participants subresource") and how to manage them.

* * *

## Conference recordings

conference-recordings page anchor

Positive FeedbackNegative Feedback

You can access the Recordings subresource on any given Conference resource.

The following will return a list of all of the recordings generated for a given conference, identified by its `ConferenceSid`. (Note that recordings associated with an individual call leg of the conference will not be returned.)

Copy code block


    GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings.json

Learn more about [Recordings](/docs/voice/api/recording "Recordings").

* * *

## Conference Log Retention

conference-log-retention page anchor

Positive FeedbackNegative Feedback

Starting on February 5, 2021 you will be able to retrieve resources via `GET` to the /Conferences and /Participants endpoints for thirteen months after the resource is created. This represents a significant change as these logs are currently stored indefinitely by Twilio and retrievable via Console and API.

It's important to note that we are not deleting your logs, just changing _where_ they will be available to you. We provide a Bulk Export utility in Console for [Conferences(link takes you to an external page)](https://www.twilio.com/console/voice/settings/conferences-archives "Conferences") and [Participant(link takes you to an external page)](https://www.twilio.com/console/voice/settings/participants-archives "Participant") resources, as well as an [API](/docs/usage/bulkexport "API"). Bulk Export will generate S3 files containing one day of data per file and deliver the download link via webhook, email, or Console. Records older than thirteen months will only be able to be retrieved via Bulk Export.

If you perform log extraction via API on a rolling basis, it is important to verify that you are pulling the logs at a frequency that will remain unaffected by this change.

* * *

## Tips and best practices

tips-and-best-practices page anchor

Positive FeedbackNegative Feedback

  * Long audio files for conference announcements delay playback. For example, a 25-minute file can take about 13–15 seconds to begin after you send the API request.
  * Conference announcements that are 30 minutes or longer can trigger a request timeout and cause the announcement to fail. When this happens, the conference and all calls stay connected, but participants hear "An application error has occurred." The 30-minute limit is approximate. Factors such as file size, HTTP method, and your server's processing or response time can also cause timeouts.
  * For announcements longer than 30 minutes, divide the audio into shorter segments and play them sequentially.


* * *

## What's next?

whats-next page anchor

Positive FeedbackNegative Feedback

Explore [Voice Insights](/docs/voice/voice-insights "Voice Insights") with its [Conference Insights Event Stream](/docs/voice/voice-insights/event-streams/conference-insights-event "Conference Insights Event Stream") and [Conference Insights REST API](/docs/voice/voice-insights/api/conference "Conference Insights REST API") which allow you to see conference parameters, investigate participant event timelines, and understand detected quality issues.