# A2P 10DLC - Brand 2FA Verification Resource

*Source: https://www.twilio.com/docs/messaging/api/brand-2fa-verify*

---

# A2P 10DLC - Brand 2FA Verification Resource

Positive FeedbackNegative Feedback

* * *

(warning)

## Warning

This API reference supplements the [A2P 10DLC brand registration guide](/docs/messaging/compliance/a2p-10dlc/collect-business-info "A2P 10DLC brand registration guide"). Review that guide before you use this API.

The 2FA Verification resource provides the ability to retrigger a 2FA email for Authentication+ association with the [BrandRegistration resource](/docs/messaging/api/brand-registration-resource "BrandRegistration resource").

The 2FA Verification resource is a subresource of the BrandRegistration resource.

* * *

## Base URL

base-url page anchor

Positive FeedbackNegative Feedback

All URLs referenced in the API documentation have the following base:

`https://messaging.twilio.com/v1/a2p/BrandRegistrations`

* * *

## Create a 2FA Verification resource

create-a-2fa-verification-resource page anchor

Positive FeedbackNegative Feedback

**Resource URL** : `https://messaging.twilio.com/v1/a2p/BrandRegistrations/{BrandSid}/2fa`

To initiate a 2FA Verification for the Brand, make a `POST` request to this resource.

See the following code sample for a complete curl request.

Copy code block


    1

    curl --location --request POST 'https://messaging.twilio.com/v1/a2p/BrandRegistrations/BNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/2fa' \


    2

    -u "Account_SID:Auth_Token" \


    3

    --header 'Content-Type: application/json' \

(warning)

## Warning

Don't create a [UsAppToPerson resource](/docs/messaging/api/usapptoperson-resource "UsAppToPerson resource") until the Brandregistration resource's `vetting_status` is `FAILED`.

You can check the `vetting_status` through fetching the BrandVetting resource.

Once the BrandVetting status is `FAILED` and the 2FA Verification is initiated, a new email will be sent and this will incur a new Authentication+ fee.