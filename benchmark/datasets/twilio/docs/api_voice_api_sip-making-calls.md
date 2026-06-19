# Making SIP Calls

*Source: https://www.twilio.com/docs/voice/api/sip-making-calls*

---

# Making SIP Calls

Positive FeedbackNegative Feedback

* * *

Use Twilio's REST API to connect to your SIP-enabled endpoints. With this feature, you can set up a VoIP session using SIP. If you are unfamiliar with SIP, or want more information on how Twilio works with your SIP endpoint, please see the [SIP overview](/docs/voice/api/sip-interface "SIP overview").

* * *

## HTTP POST to Calls

http-post-to-calls page anchor

Positive FeedbackNegative Feedback

Initiate SIP sessions via the REST API by `POST`ing to the same calls resource used to [make outbound phone calls](/docs/voice/tutorials/how-to-make-outbound-phone-calls "make outbound phone calls"). Once the call is connected, Twilio will then fetch the TwiML you specify for the call. For example, make a SIP call by `POST`ing to your account's [calls list resource](/docs/voice/api/call-resource "calls list resource") URI:

Copy code block


     /2010-04-01/Accounts/{AccountSid}/Calls

### POST Parameters

post-parameters page anchor

Positive FeedbackNegative Feedback

All outgoing call features and parameters are supported — the only difference is that you pass different values in the "To" and "From" parameters. In the "To" parameter, put the SIP URI you are trying to connect to. In the "From" parameter, specify the user you want to show up in the From header in the SIP request.

#### Required Parameters

required-parameters page anchor

You must `POST` the following parameters:

Parameter| Description
---|---
To| The SIP URI to which you want to connect

The 'To' parameter specifies a SIP address for Twilio to connect to. The body of the URI element should be a valid SIP URI under 255 characters. For example:

Copy code block


    sip:michael@example.com

#### Headers

headers page anchor

Pass headers in the `To` parameter by appending them to the end of the SIP URI. For certain sdks, `&` will need encoding as `%26`. The total characters passed in a header must be under 1024. For example:

Copy code block


    sip:michael@example.com?mycustomheader=foo&myotherheader=bar

#### Transport

transport page anchor

Set a parameter on your SIP URI to specify what transport protocol you want to use. You may use `UDP`, `TCP` or `TLS`. By default, Twilio sends your SIP INVITE over `UDP`. Change this by using the transport parameter:

Copy code block


    sip:jack@example.com;transport=tcp

Also, when using `transport=tls`, this will only encrypt SIP signaling messages and not `RTP`. To use `SRTP` and to encrypt SIP signaling, please add a parameter `secure=true` to your SIP URI:

Copy code block


    sip:jack@example.com;secure=true

#### Optional Parameters

optional-parameters page anchor

You may `POST` the following parameters:

Parameter| Description
---|---
From| This value is used to populate the username portion of the From header that is passed to the SIP endpoint. This may be any alphanumeric character, as well as the plus, minus, underscore, and period characters (+-_.). No spaces or other characters are allowed.
SipAuthUsername| Your authentication username.
SipAuthPassword| The password for the user.

#### Create a SIP Dial

create-a-sip-dial page anchor

Basic SIP dial using the REST API.

Create Basic SIP DialLink to code sample: Create Basic SIP Dial

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

    async function createCall() {


    11

      const call = await client.calls.create({


    12

        from: "Jack",


    13

        to: "sip:kate@example.com",


    14

        url: "http://www.example.com/sipdial.xml",


    15

      });


    16




    17

      console.log(call.sid);


    18

    }


    19




    20

    createCall();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "answered_by": null,


    4

      "api_version": "2010-04-01",


    5

      "caller_name": null,


    6

      "date_created": "Tue, 31 Aug 2010 20:36:28 +0000",


    7

      "date_updated": "Tue, 31 Aug 2010 20:36:44 +0000",


    8

      "direction": "inbound",


    9

      "duration": "15",


    10

      "end_time": "Tue, 31 Aug 2010 20:36:44 +0000",


    11

      "forwarded_from": "+141586753093",


    12

      "from": "Jack",


    13

      "from_formatted": "(415) 867-5308",


    14

      "group_sid": null,


    15

      "parent_call_sid": null,


    16

      "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

      "price": "-0.03000",


    18

      "price_unit": "USD",


    19

      "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    20

      "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",


    21

      "status": "completed",


    22

      "subresource_uris": {


    23

        "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",


    24

        "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",


    25

        "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments.json",


    26

        "events": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Events.json",


    27

        "siprec": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Siprec.json",


    28

        "streams": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Streams.json",


    29

        "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json",


    30

        "twiml_sessions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TwimlSessions.json",


    31

        "user_defined_message_subscriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessageSubscriptions.json",


    32

        "user_defined_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessages.json"


    33

      },


    34

      "to": "sip:kate@example.com",


    35

      "to_formatted": "(415) 867-5309",


    36

      "trunk_sid": null,


    37

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    38

      "queue_time": "1000"


    39

    }

#### Create SIP Dial with Authentication

create-sip-dial-with-authentication page anchor

Pass user and password to your SIP call for authentication.

Create SIP Dial with AuthenticationLink to code sample: Create SIP Dial with Authentication

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

    async function createCall() {


    11

      const call = await client.calls.create({


    12

        from: "Jack",


    13

        sipAuthPassword: "secret",


    14

        sipAuthUsername: "jack",


    15

        to: "sip:kate@example.com",


    16

        url: "http://www.example.com/sipdial.xml",


    17

      });


    18




    19

      console.log(call.sid);


    20

    }


    21




    22

    createCall();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "answered_by": null,


    4

      "api_version": "2010-04-01",


    5

      "caller_name": null,


    6

      "date_created": "Tue, 31 Aug 2010 20:36:28 +0000",


    7

      "date_updated": "Tue, 31 Aug 2010 20:36:44 +0000",


    8

      "direction": "inbound",


    9

      "duration": "15",


    10

      "end_time": "Tue, 31 Aug 2010 20:36:44 +0000",


    11

      "forwarded_from": "+141586753093",


    12

      "from": "Jack",


    13

      "from_formatted": "(415) 867-5308",


    14

      "group_sid": null,


    15

      "parent_call_sid": null,


    16

      "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

      "price": "-0.03000",


    18

      "price_unit": "USD",


    19

      "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    20

      "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",


    21

      "status": "completed",


    22

      "subresource_uris": {


    23

        "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",


    24

        "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",


    25

        "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments.json",


    26

        "events": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Events.json",


    27

        "siprec": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Siprec.json",


    28

        "streams": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Streams.json",


    29

        "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json",


    30

        "twiml_sessions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TwimlSessions.json",


    31

        "user_defined_message_subscriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessageSubscriptions.json",


    32

        "user_defined_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessages.json"


    33

      },


    34

      "to": "sip:kate@example.com",


    35

      "to_formatted": "(415) 867-5309",


    36

      "trunk_sid": null,


    37

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    38

      "queue_time": "1000"


    39

    }

#### Pass Headers in your SIP URI

pass-headers-in-your-sip-uri page anchor

Pass headers to your SIP Dial as part of the SIP URI.

Create SIP Dial using Pass Headers in the SIP URILink to code sample: Create SIP Dial using Pass Headers in the SIP URI

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

    async function createCall() {


    11

      const call = await client.calls.create({


    12

        from: "Jack",


    13

        to: "sip:kate@example.com?X-hatchkey=4815162342",


    14

        url: "http://www.example.com/sipdial.xml",


    15

      });


    16




    17

      console.log(call.sid);


    18

    }


    19




    20

    createCall();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    3

      "answered_by": null,


    4

      "api_version": "2010-04-01",


    5

      "caller_name": null,


    6

      "date_created": "Tue, 31 Aug 2010 20:36:28 +0000",


    7

      "date_updated": "Tue, 31 Aug 2010 20:36:44 +0000",


    8

      "direction": "inbound",


    9

      "duration": "15",


    10

      "end_time": "Tue, 31 Aug 2010 20:36:44 +0000",


    11

      "forwarded_from": "+141586753093",


    12

      "from": "Jack",


    13

      "from_formatted": "(415) 867-5308",


    14

      "group_sid": null,


    15

      "parent_call_sid": null,


    16

      "phone_number_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

      "price": "-0.03000",


    18

      "price_unit": "USD",


    19

      "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    20

      "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",


    21

      "status": "completed",


    22

      "subresource_uris": {


    23

        "notifications": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json",


    24

        "recordings": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings.json",


    25

        "payments": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments.json",


    26

        "events": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Events.json",


    27

        "siprec": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Siprec.json",


    28

        "streams": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Streams.json",


    29

        "transcriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Transcriptions.json",


    30

        "twiml_sessions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TwimlSessions.json",


    31

        "user_defined_message_subscriptions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessageSubscriptions.json",


    32

        "user_defined_messages": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/UserDefinedMessages.json"


    33

      },


    34

      "to": "sip:kate@example.com?X-hatchkey=4815162342",


    35

      "to_formatted": "(415) 867-5309",


    36

      "trunk_sid": null,


    37

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    38

      "queue_time": "1000"


    39

    }