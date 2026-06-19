# Verify Phone Verification API V1

*Source: https://www.twilio.com/docs/verify/api/v1/verification*

---

# Verify Phone Verification API V1

Positive FeedbackNegative Feedback

* * *

(warning)

## Warning

Verify v1 API has reached End of Sale. It is now closed to new customers and will be fully deprecated in the future.

For new development, we encourage you to use the [Verify v2 API](/docs/verify/api "Verify v2 API"). v2 has an improved developer experience and new features, including:

  * Twilio server-side SDKs in multiple languages
  * [PSD2](/docs/verify/verifying-transactions-psd2 "PSD2") Secure Customer Authentication Support
  * [Improved Visibility and Insights](/docs/verify/migrating-1x-2x#improved-visibility-and-insights "Improved Visibility and Insights")


Existing customers will not be impacted at this time until Verify v1 API has reached End of Life. For more information about migration, see [Migrating from 1.x to 2.x](/docs/verify/migrating-1x-2x "Migrating from 1.x to 2.x").

The Twilio Verify REST API allows you to verify that a user has a claimed device in their possession. The API lets you request a verification code to be sent to the user and to check that a received code is valid.

Phone verification is an important first step in your online relationship with a user. To learn more about best practices and recommended registration flows, please consult [Twilio Verify Best Practices](/docs/verify/developer-best-practices "Twilio Verify Best Practices").

* * *

## Send a Verification Code

send-a-verification-code page anchor

Positive FeedbackNegative Feedback

To verify a user's phone number, you will start by requesting to send a verification code to their device. _**Each verification code is valid for 10 minutes. Subsequent calls to the API before the code has expired will send the same verification code.**_ You cannot modify the amount of time a verification code is valid. You can query the [`status`](/docs/verify/api/v1/verification#get-the-status-of-a-verification-code-sent-to-the-user) endpoint to check if a verification code is still valid.

Note that you may use dashes, periods, spaces or nothing to format a phone number.

Copy code block


    POST https://api.authy.com/protected/{FORMAT}/phones/verification/start

### URL

url page anchor

Positive FeedbackNegative Feedback

Name| Type| Description
---|---|---
FORMAT| String| The format to expect back from the REST API call. `json` or `xml`.

### PARAMETERS

parameters page anchor

Positive FeedbackNegative Feedback

Name| Type| Description
---|---|---
via| String| The method of delivering the code to the user. `sms` or `call`. ([🏢 not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "🏢 not PII") )
country_code| Integer| The phone's country code. ([🏢 not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "🏢 not PII") )
phone_number| String| The phone number to send the verification code. ([📇 PII](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields "📇 PII") )
locale| String (recommended)| The language of the message received by user. If no region is given (or supported) there will be a [default by country](/docs/verify/default-phone-verification-languages "default by country"). Depending on the country, this will either be the official language of the country or English. We highly recommend that you test your region or use the locale parameter to ensure that your desired language is used. See [supported languages](/docs/verify/api/v1/verification#supported-languages-recommended "supported languages") for a list of available options. ([🏢 not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "🏢 not PII") )
code_length| Integer (optional)| Optional value to change the number of verification digits sent. Default value is 4. Allowed values are 4-10. ([🏢 not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "🏢 not PII") )
custom_code| Integer (optional)| Pass in a pre-generated code. Code length can be between 4-10 characters. Contact [Twilio Sales(link takes you to an external page)](https://www.twilio.com/help/sales "Twilio Sales") to have this feature enabled. ([🏢 not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "🏢 not PII") )

Start a phone verification.Link to code sample: Start a phone verification.

Report code block

Copy code block


    1

    // npm install authy


    2

    const authy = require("authy")("YOUR_AUTHY_API_KEY");


    3




    4

    authy


    5

      .phones()


    6

      .verification_start("5551234567", "1", "sms", function(err, res) {


    7

        if (err) {


    8

          console.log(err);


    9

        }


    10




    11

        console.log(res.message);


    12

      });

### Output

Copy output


    1

    {


    2

      "carrier": "AT&T Wireless",


    3

      "is_cellphone": true,


    4

      "message": "Text message sent to +1 987-654-3210.",


    5

      "seconds_to_expire": 599,


    6

      "uuid": "b8ebcd40-1234-5678-3fb5-0e5d6a065904",


    7

      "success": true


    8

    }

(information)

## Info

For some regions, we are unable to return carrier and cellphone data by default. You need to contact our support team to switch on those regions. More information on our [support site.(link takes you to an external page)](https://help.twilio.com/hc/en-us/articles/360004563433 "support
site.")

#### Supported Languages (Recommended)

supported-languages-recommended page anchor

Please reference [Supported Languages](/docs/verify/supported-languages "Supported Languages") for full documentation. We support the format country-region as described in [IETF's BPC 47(link takes you to an external page)](https://www.rfc-editor.org/rfc/bcp/bcp47.txt "IETF's BPC 47"). If no region is given (or supported) there will be a [default by country](/docs/verify/default-phone-verification-languages "default by country"). Supported languages for the `locale` parameter are `af`, `ar`, `ca`, `zh`, `zh-CN`, `zh-HK`, `hr`, `cs`, `da`, `nl`, `en`, `fi`, `fr`, `de`, `el`, `he`, `hi`, `hu`, `id`, `it`, `ja`, `ko`, `ms`, `nb`, `pl`, `pt-BR`, `pt`, `ro`, `ru`, `es`, `sv`, `tl`, `th`, `tr`, `vi`.

For more information, [please reference our full guide to Supported Languages.](/docs/verify/supported-languages "please reference our full guide to Supported Languages.")

#### Custom Verification Codes (Optional)

custom-verification-codes-optional page anchor

If you already have token generation and validation logic and would like to keep those systems in place, you can do so. We have a feature where you can submit your code to us and utilize our pre-screened message templates and localizations for both text and voice.

With this modified setup, you will be charged on each _**attempted**_ customer verification (requests for a verification code). Due to situations like abandoned requests and users who eagerly request multiple codes, we typically see 30% more [/start](/docs/verify/api/v1/verification#send-a-verification-code "/start") verifications than [/check](/docs/verify/api/v1/verification#check-a-verification-code "/check") verifications. **This means that you can expect to pay 30% more for this feature.** Keep this in mind as you are considering your options.

If you're using custom verification codes you must also [provide feedback](/docs/verify/api/v1/feedback "provide feedback") that lets us know whether or not the user verified the code. This allows us to proactively monitor our global routing and stay operational. You can send feedback to our system with the [Verify Feedback API](/docs/verify/api/v1/feedback "Verify Feedback API").

[Contact Twilio Sales(link takes you to an external page)](https://www.twilio.com/help/sales "Contact Twilio Sales") and we'll help you enable this option.

Start a phone verification with custom code.Link to code sample: Start a phone verification with custom code.

Report code block

Copy code block


    1

    curl -X POST 'https://api.authy.com/protected/json/phones/verification/start' \


    2

    -H "X-Authy-API-Key: d57d919d11e6b221c9bf6f7c882028f9" \


    3

    -d via='sms' \


    4

    -d phone_number='987-654-3210' \


    5

    -d country_code=1 \


    6

    -d locale=en \


    7

    -d custom_code=3333

### Output

Copy output


    1

    {


    2

      "carrier": "AT&T Wireless",


    3

      "is_cellphone": true,


    4

      "message": "Text message sent to +1 987-654-3210.",


    5

      "seconds_to_expire": 599,


    6

      "uuid": "b8ebcd40-1234-5678-3fb5-0e5d6a065904",


    7

      "sms_id": "cafd7a60-6d03-1234-5678-0eb34144aeb2", # You'll use this ID to send feedback


    8

      "success": true


    9

    }

Following a request using `custom_code` you will then submit a request to our [Feedback API](/docs/verify/api/v1/feedback "Feedback API"). Head over to the [Feedback API docs](/docs/verify/api/v1/feedback#examples "Feedback API docs") for example requests.

* * *

## Check a Verification Code

check-a-verification-code page anchor

Positive FeedbackNegative Feedback

To check if a verification code is correct, pass the code along with the phone number to the API.

Copy code block


    GET https://api.authy.com/protected/{FORMAT}/phones/verification/check

### URL

url-1 page anchor

Positive FeedbackNegative Feedback

Name| Type| Description
---|---|---
FORMAT| String| The format to expect back from the REST API call. `json`, or `xml`.

### PARAMETERS

parameters-2 page anchor

Positive FeedbackNegative Feedback

Name| Type| Description
---|---|---
country_code| Integer| The phone's country code. ([🏢 not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "🏢 not PII") )
phone_number| String| The phone number to send the verification code. ([📇 PII](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields "📇 PII") )
verification_code| String| The verification code from the user that is being validated. ([🏢 not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "🏢 not PII") )

Check a Verification Code.Link to code sample: Check a Verification Code.

Report code block

Copy code block


    1

    authy.phones().verification_check('111-111-1111', '1', '1234', function (err, res) {


    2

      if (err) {


    3

        // invalid token


    4

        console.log(err);


    5

      }


    6




    7

      console.log(res);


    8

    });

### Output

Copy output


    1

    {


    2

      "message":"Verification code is correct.",


    3

      "success":true


    4

    }

* * *

## Get the Status of a Verification Code Sent to the User

get-the-status-of-a-verification-code-sent-to-the-user page anchor

Positive FeedbackNegative Feedback

Each verification code is valid for 10 minutes. Subsequent calls to the API before the code has expired will send the same verification code. Use this status API to determine how much time remains for an active or pending verification request.

Copy code block


    GET https://api.authy.com/protected/{FORMAT}/phones/verification/status

Name| Type| Description
---|---|---
FORMAT| String| The format to expect back from the REST API call. `json`, or `xml`.

### PARAMETERS

parameters-3 page anchor

Positive FeedbackNegative Feedback

Name| Type| Description
---|---|---
uuid| String| The uuid from the original request. ([🏢 not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "🏢 not PII") )
country_code| Integer (Optional)| The phone's country code. Alternative to `uuid` when combined with `phone_number`. ([🏢 not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "🏢 not PII") )
phone_number| String (Optional)| The phone number to send the verification code. Alternative to `uuid` when combined with `country_code`. ([📇 PII](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields "📇 PII") )

### Response

response page anchor

Positive FeedbackNegative Feedback

Name| Type| Description
---|---|---
status| String| The status of the original request to the user. `expired`, `verified` or `pending`. ([🏢 not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "🏢 not PII") )
seconds_to_expire| Integer| The amount of time in seconds remaining before the verification code expires. ([🏢 not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "🏢 not PII") )
success| Boolean| Returns `true` if the request was successful. ([🏢 not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "🏢 not PII") )
message| String| A message indicating what happened with the request. ([🏢 not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii "🏢 not PII") )

Check Verification Status using Verification UUID.Link to code sample: Check Verification Status using Verification UUID.

Report code block

Copy code block


    1

    curl 'https://api.authy.com/protected/json/phones/verification/status?uuid=b8ebcd40-1234-5678-3fb5-0e5d6a065904' \


    2

    -H "X-Authy-API-Key: d57d919d11e6b221c9bf6f7c882028f9"

### Output

Copy output


    1

    {


    2

      "message": "Phone Verification status.",


    3

      "status": "verified",


    4

      "seconds_to_expire": 474,


    5

      "success": true


    6

    }

This example checks the status of the request using `country_code` and `phone_number`.

Check Verification Status using Phone Number.Link to code sample: Check Verification Status using Phone Number.

Report code block

Copy code block


    1

    curl 'https://api.authy.com/protected/json/phones/verification/status?country_code=1&phone_number=987-654-3210' \


    2

    -H "X-Authy-API-Key: d57d919d11e6b221c9bf6f7c882028f9"

### Output

Copy output


    1

    {


    2

      "message": "Phone Verification status.",


    3

      "status": "pending",


    4

      "seconds_to_expire": 598,


    5

      "success": true


    6

    }