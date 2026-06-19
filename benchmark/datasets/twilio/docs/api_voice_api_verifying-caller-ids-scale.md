# Verifying Caller IDs at Scale

*Source: https://www.twilio.com/docs/voice/api/verifying-caller-ids-scale*

---

# Verifying Caller IDs at Scale

Positive FeedbackNegative Feedback

* * *

What if you need to make calls in a subaccount using a Twilio phone number provisioned in your Master account? You'll need to verify those outgoing caller IDs with the Twilio account or subaccount you are using.

This guide will be helpful if you have a large number of phone numbers that you need to verify programmatically. If you need to verify a mobile phone or landline number, it may be easier to do so through the Twilio console.

* * *

## What this guide covers

what-this-guide-covers page anchor

Positive FeedbackNegative Feedback

This guide covers the process you would use to programmatically verify many phone numbers with Twilio. The specifics of the implementation are going to be different, based on the API provider you are using for the phone numbers.

In general, you will start with a list of phone numbers to verify. Make a call to the Twilio API with each phone number to start the verification process. Twilio will respond with a unique six digit verification code for each number.

Twilio will then make a phone call to the phone number from another provider, and that phone number should respond with the six digit verification code. After Twilio either receives or doesn't receive the correct code, a separate status callback request is made to a web URL of your choosing that contains the verification result for that phone number - either success or failure.

This guide uses Twilio Sync to share state between different systems - but you may use another data store, such as Redis or a database. It also uses a Twilio Function to store verification status in Twilio Sync.

  * [Verifying outgoing caller IDs with Twilio](/docs/voice/api/verifying-caller-ids-scale#verifying-outgoing-caller-ids-with-twilio "Verifying outgoing caller IDs with Twilio")
  * [Using Twilio Sync to store validation information](/docs/voice/api/verifying-caller-ids-scale#using-twilio-sync-to-store-validation-information "Using Twilio Sync to store validation information")
  * [Responding to the Twilio Verification phone call](/docs/voice/api/verifying-caller-ids-scale#responding-to-the-twilio-verification-phone-call "Responding to the Twilio Verification phone call")
  * [Receiving verification status in a callback](/docs/voice/api/verifying-caller-ids-scale#retrieving-verification-status-from-twilio-sync "Receiving verification status in a callback")
  * [Recording verification status with Twilio Sync](/docs/voice/api/verifying-caller-ids-scale#recording-verification-status-with-twilio-sync "Recording verification status with Twilio Sync")
  * [Retrieving verification status from Twilio Sync](/docs/voice/api/verifying-caller-ids-scale#retrieving-verification-status-from-twilio-sync "Retrieving verification status from Twilio Sync")
  * [Next Steps](/docs/voice/api/verifying-caller-ids-scale#next-steps "Next Steps")


* * *

## Verifying outgoing caller IDs with Twilio

verifying-outgoing-caller-ids-with-twilio page anchor

Positive FeedbackNegative Feedback

Using the [Outgoing Caller IDs Resource](/docs/voice/api/outgoing-caller-ids "Outgoing Caller IDs Resource"), you can create a validation request for a phone number. Twilio will return a six digit verification code to you in the response to the create request (synchronously). Twilio will then call that phone number on the [PSTN](/docs/glossary/what-is-pstn "PSTN"), with a caller ID of +14157234000.

(information)

## Info

The verification call is in English. Other languages aren't supported.

We also set the status callback, so that we can get the verification status for each phone number.

Verify an Outgoing Caller IDLink to code sample: Verify an Outgoing Caller ID

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

    async function createValidationRequest() {


    11

      const validationRequest = await client.validationRequests.create({


    12

        friendlyName: "Third Party VOIP Number",


    13

        phoneNumber: "+14158675310",


    14

        statusCallback:


    15

          "https://somefunction.twil.io/caller-id-validation-callback",


    16

      });


    17




    18

      console.log(validationRequest.accountSid);


    19

    }


    20




    21

    createValidationRequest();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    4

      "friendly_name": "Third Party VOIP Number",


    5

      "phone_number": "+14158675310",


    6

      "validation_code": "111111"


    7

    }

From your non-Twilio phone number (or from a Twilio number not associated with the current account), you will need to answer the incoming call from Twilio. This typically involves configuring a webhook with the third party, however you may be using an incoming voice call webhook on that phone number already. If that's the case, you can either add some logic to the webhook to respond to the inbound Twilio phone number (+14157234000), or temporarily replace the webhook with one that replies back to the Twilio validation request phone call.

When you send the validation request, you will get a six digit verification code in the response. You will have to get that verification code to the webhook that responds to the Twilio incoming phone call. One way to do this would be to use a key/value store like Redis. Another way would be to use [Twilio Sync](/docs/sync "Twilio Sync") to store the validation code.

* * *

## Using Twilio Sync to store validation information

using-twilio-sync-to-store-validation-information page anchor

Positive FeedbackNegative Feedback

Twilio Sync provides shared state in the cloud, so you can store the verification codes in Sync after calling the Verify Outgoing Callers API, and then access those access codes from your phone number's webhook (which probably isn't running on the same system as a script that verifies caller ids). There are two steps - the first is to set up a sync map to store information by phone number. For now, we are only going to store the verification code. Later, we will store verification information, once we retrieve it from the status callback.

When you work with Twilio Sync, you can either use a client SDK (for the web browser with JavaScript, iOS, or Android), or the Twilio REST API. The Twilio REST API has [SDKs](/docs/libraries "SDKs") for Java, C#, Python, Ruby, PHP, and Node.js/JavaScript. You will want to use the REST API or the related SDKs for most of this project, but if you were to build a web application dashboard to show results, you may want to look into the [client-side JavaScript library for Sync](/docs/sync/quickstart/js "client-side JavaScript library for Sync").

We can use the default Sync service - if you are using Sync already, you can also create a new Sync Service from the console or API, and use that. When we create the Sync Map, we give it a unique name, "OutgoingCallerIds" - this can also be whatever you would like to use.

Create a sync map for verifying caller idsLink to code sample: Create a sync map for verifying caller ids

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

    async function createSyncMap() {


    11

      const syncMap = await client.sync.v1


    12

        .services("ServiceSid")


    13

        .syncMaps.create({ uniqueName: "OutgoingCallerIds" });


    14




    15

      console.log(syncMap.sid);


    16

    }


    17




    18

    createSyncMap();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "created_by": "created_by",


    4

      "date_expires": "2015-07-30T21:00:00Z",


    5

      "date_created": "2015-07-30T20:00:00Z",


    6

      "date_updated": "2015-07-30T20:00:00Z",


    7

      "links": {


    8

        "items": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items",


    9

        "permissions": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Permissions"


    10

      },


    11

      "revision": "revision",


    12

      "service_sid": "ServiceSid",


    13

      "sid": "MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    14

      "unique_name": "OutgoingCallerIds",


    15

      "url": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    16

    }

After creating a Sync Map with the REST API (you will only need to do this once), the next step will be to store the verification code from Twilio into that Sync Map. Sync Maps store Map Items, which consist of a data object accessed by a key. The key is a string, and should be unique - the phone number works perfectly as a key. The data can be up to 16 kilobytes in size, and should be structured as key value pairs. We can store the verification code with the key `verification_code`. and store the six digit verification code as the value.

Store a verification code with Twilio SyncLink to code sample: Store a verification code with Twilio Sync

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

    async function createSyncMapItem() {


    11

      const syncMapItem = await client.sync.v1


    12

        .services("ServiceSid")


    13

        .syncMaps("MapSid")


    14

        .syncMapItems.create({


    15

          data: {


    16

            verification_code: "123456",


    17

          },


    18

          key: "+14158675310",


    19

        });


    20




    21

      console.log(syncMapItem.key);


    22

    }


    23




    24

    createSyncMapItem();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "created_by": "created_by",


    4

      "data": {


    5

        "verification_code": "123456"


    6

      },


    7

      "date_expires": "2015-07-30T21:00:00Z",


    8

      "date_created": "2015-07-30T20:00:00Z",


    9

      "date_updated": "2015-07-30T20:00:00Z",


    10

      "key": "+14158675310",


    11

      "map_sid": "MapSid",


    12

      "revision": "revision",


    13

      "service_sid": "ServiceSid",


    14

      "url": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items/key"


    15

    }

* * *

## Responding to the Twilio Verification Phone Call

responding-to-the-twilio-verification-phone-call page anchor

Positive FeedbackNegative Feedback

Depending on your third-party provider, how you respond to an incoming phone call will differ. For instance, your provider may offer a webhook solution that calls a web URL of your choosing with an `HTTP POST` or `GET` request.

Your response should be based on the incoming phone number - +14157234000 is the phone number that Twilio will be using to verify your phone number, so you can play back the proper six digit validation code with DTMF.

When your phone number receives the validation request, your program will need to look up that verification code. For instance, if you were using Redis as the data storage, the phone number would likely be the key. If you use Twilio Sync, you can fetch a Map Item from a Sync Map, based on the phone number as the key.

Retrieving the Verification Code from Twilio Sync.Link to code sample: Retrieving the Verification Code from Twilio Sync.

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

    async function fetchSyncMapItem() {


    11

      const syncMapItem = await client.sync.v1


    12

        .services("ServiceSid")


    13

        .syncMaps("MapSid")


    14

        .syncMapItems("+14158675310")


    15

        .fetch();


    16




    17

      console.log(syncMapItem.key);


    18

    }


    19




    20

    fetchSyncMapItem();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "created_by": "created_by",


    4

      "data": {},


    5

      "date_expires": "2015-07-30T21:00:00Z",


    6

      "date_created": "2015-07-30T20:00:00Z",


    7

      "date_updated": "2015-07-30T20:00:00Z",


    8

      "key": "+14158675310",


    9

      "map_sid": "MapSid",


    10

      "revision": "revision",


    11

      "service_sid": "ServiceSid",


    12

      "url": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items/key"


    13

    }

The map item will contain the verification code in the data object. Read that verification code, and then play it back to Twilio, and your phone number will be verified!

* * *

## Receiving verification status in a callback

receiving-verification-status-in-a-callback page anchor

Positive FeedbackNegative Feedback

After your phone number gets a verification call from Twilio, you can receive a status callback from Twilio to record the verification status for that phone number. This webhook will contain two parameters we are interested in - `VerificationStatus` and `To` (the number being verified), as well as the other parameters included in a [TwiML Voice Request](/docs/voice/twiml#request-parameters "TwiML Voice Request").

Because you may be verifying many numbers, there may be some cases where the verification status fails, and you have to retry those numbers. For those cases, it's helpful to have a record of which verifications were successful, and which were not.

If possible, record the verification status in logs, but also into a key/value store or database, to get a list of failed verifications back. Again, we can use Twilio Sync for this.

* * *

## Recording verification status with Twilio Sync

recording-verification-status-with-twilio-sync page anchor

Positive FeedbackNegative Feedback

We will update the Map Item for our phone number in our `OutgoingCallerIds` Map. You will need the original key used for the map item - this would be the phone number, in the same format as you stored it. Then you can pass in a new data object - in this case, it would look like `{"verification_status":true}`.

If you like, you could also use another Map, with a different unique name, and then create a Map Item in that Map for the verification status.

Recording verification status with Twilio SyncLink to code sample: Recording verification status with Twilio Sync

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

    async function updateSyncMapItem() {


    11

      const syncMapItem = await client.sync.v1


    12

        .services("ServiceSid")


    13

        .syncMaps("MapSid")


    14

        .syncMapItems("+14158675310")


    15

        .update({


    16

          data: {


    17

            verification_status: "true",


    18

          },


    19

        });


    20




    21

      console.log(syncMapItem.key);


    22

    }


    23




    24

    updateSyncMapItem();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "created_by": "created_by",


    4

      "data": {


    5

        "verification_status": "true"


    6

      },


    7

      "date_expires": "2015-07-30T21:00:00Z",


    8

      "date_created": "2015-07-30T20:00:00Z",


    9

      "date_updated": "2015-07-30T20:00:00Z",


    10

      "key": "+14158675310",


    11

      "map_sid": "MapSid",


    12

      "revision": "revision",


    13

      "service_sid": "ServiceSid",


    14

      "url": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items/key"


    15

    }

If you would like, the status callback for the caller id verification could be a [Twilio Function](/docs/serverless/functions-assets/functions "Twilio Function"). Functions is Twilio's serverless environment, where you can run JavaScript code in a Node.js environment. You would need to set the `SYNC_SERVICE_SID` and `VERIFY_CALLER_ID_SYNC_MAP_SID` variables on the [Function Credentials page(link takes you to an external page)](https://www.twilio.com/console/functions/configure "Function Credentials page") in the Twilio Console. Then [create a new Twilio Function in the Runtime Console(link takes you to an external page)](https://www.twilio.com/console/functions/manage "create a new Twilio Function in the Runtime Console") and add the JavaScript source code from the **Twilio Function for storing verification status in Twilio Sync** code sample.

Save the Twilio Function, and then it will automatically deploy. Now just supply that URL as the status callback when you verify the Twilio phone number.

#### Twilio Function for storing verification status in Twilio Sync

twilio-function-for-storing-verification-status-in-twilio-sync page anchor

Copy code block


    1

    exports.handler = function(context, event, callback) {


    2

      console.log('Incoming webhook', event);


    3




    4

     let client = context.getTwilioClient();


    5




    6

      let verificationStatus = event['VerificationStatus'];


    7

      let phoneNumber = event['To'];


    8




    9

      client.sync.services(context.SYNC_SERVICE_SID)


    10

         .syncMaps(context.VERIFY_CALLER_ID_SYNC_MAP_SID)


    11

         .syncMapItems(phoneNumber)


    12

         .update({data: {


    13

            verification_status: verificationStatus


    14

          }})


    15

         .then(sync_map_item => {


    16

              console.log(sync_map_item.data);


    17

              callback(null, 'OK');


    18

          }).catch( error => {


    19

              console.log(error);


    20

              callback(null, error);


    21

          });


    22

    };

* * *

## Retrieving verification status from Twilio Sync

retrieving-verification-status-from-twilio-sync page anchor

Positive FeedbackNegative Feedback

With the verification status stored in Sync, we can make another request to retrieve all of the map items from the Sync Map. With that request, you could then print out the results from a command line, or you could create a web-based dashboard. If you do create a web-based dashboard, you can update the verification status in real time as your script runs with the client side JavaScript SDK for Sync.

The REST API for fetching all Map Items for a Map is paginated - if you have more than 50 numbers to verify, you will need to paginate through the list. For more on working with map items, see the [Map Item Resource](/docs/sync/api/map-item-resource "Map Item Resource") documentation.

Retrieving verification status from Twilio SyncLink to code sample: Retrieving verification status from Twilio Sync

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

    async function listSyncMapItem() {


    11

      const syncMapItems = await client.sync.v1


    12

        .services("ServiceSid")


    13

        .syncMaps("MapSid")


    14

        .syncMapItems.list({ limit: 20 });


    15




    16

      syncMapItems.forEach((s) => console.log(s.key));


    17

    }


    18




    19

    listSyncMapItem();

### Response

Note about this response

Copy response


    1

    {


    2

      "items": [],


    3

      "meta": {


    4

        "first_page_url": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items?From=from&Bounds=inclusive&Order=asc&PageSize=50&Page=0",


    5

        "key": "items",


    6

        "next_page_url": null,


    7

        "page": 0,


    8

        "page_size": 50,


    9

        "previous_page_url": null,


    10

        "url": "https://sync.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items?From=from&Bounds=inclusive&Order=asc&PageSize=50&Page=0"


    11

      }


    12

    }

* * *

## Next Steps

next-steps page anchor

Positive FeedbackNegative Feedback

After verifying your phone numbers with this account, you should be able to make outgoing calls with Twilio using these numbers for the caller ID.

Here are some additional documentation resources that can help you with this project:

  * [Outgoing Caller Ids](/docs/voice/api/outgoing-caller-ids "Outgoing Caller Ids")
  * [Twilio Webhooks](/docs/usage/webhooks/webhooks-overview "Twilio Webhooks")
  * [Sync Map Resource](/docs/sync/api/map-resource "Sync Map Resource")
  * [Sync Map Item Resource](/docs/sync/api/map-item-resource "Sync Map Item Resource")