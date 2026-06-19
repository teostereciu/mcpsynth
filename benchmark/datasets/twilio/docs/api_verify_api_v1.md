# Verify API V1 Reference

*Source: https://www.twilio.com/docs/verify/api/v1*

---

# Verify API V1 Reference

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

As part of Twilio's Trusted Activation offerings, the Twilio Verify API makes it simple to add phone verification to your web application. It supports codes sent via voice and SMS. To start working with the API, first [create an application in the console(link takes you to an external page)](https://www.twilio.com/console/verify/applications "create an application in the console") and get the API Key.

* * *

## Base URL

base-url page anchor

Positive FeedbackNegative Feedback

All URLs in the reference documentation use the following base URL:

Copy code block


    https://api.authy.com

All requests to the Verify REST API are served over HTTPS. Unencrypted HTTP is not supported.

* * *

## Authentication

authentication page anchor

Positive FeedbackNegative Feedback

All `HTTP` requests to the Verify REST API `/protected` endpoints are protected with an API Secret you pass as an HTTP header `X-Authy-API-Key`, e.g.:

Copy code block


    1

    curl -X POST 'https://api.authy.com/protected/json/phones/verification/start' \


    2

    -H "X-Authy-API-Key: $VERIFY_API_KEY" \


    3

    -d via='sms' \


    4

    -d phone_number='987-654-3210' \


    5

    -d country_code=1

The Verify API Key can be found in the [Verify section of the Twilio Console(link takes you to an external page)](https://www.twilio.com/console/verify/applications "Verify section of the Twilio Console") after clicking through to your application.

Expand image

* * *

## Phone Verification Workflow

phone-verification-workflow page anchor

Positive FeedbackNegative Feedback

  1. Create a [new Verify application in the Twilio Console.](/docs/verify/api/v1/applications#create-new-application "new Verify application in the Twilio Console.")
  2. [Send a Verification Token via SMS or Voice](/docs/verify/api/verification#start-new-verification "Send a Verification Token via SMS or Voice")
  3. [Check the Verification Token](/docs/verify/api/verification "Check the Verification Token")


Need help troubleshooting an error or understanding a response?

  * [Verify Return Codes and Error Codes](/docs/verify/api/v1/return-and-error-codes "Verify Return Codes and Error Codes")