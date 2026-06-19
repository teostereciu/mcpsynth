# IncomingPhoneNumber resource

*Source: https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource*

---

# IncomingPhoneNumber resource

Positive FeedbackNegative Feedback

* * *

An **IncomingPhoneNumber** instance resource represents a phone number that you provision, port, or host with Twilio.

The IncomingPhoneNumbers list resource represents an account's Twilio phone numbers. You can `POST` to the list resource to [provision a new Twilio number](/docs/phone-numbers/api/incomingphonenumber-resource "provision a new Twilio number"). To find a number to provision, use the subresources of the [AvailablePhoneNumbers](/docs/phone-numbers/api/availablephonenumber-resource "AvailablePhoneNumbers") resource.

You can transfer phone numbers between two Twilio accounts if you're using [subaccounts](/docs/iam/api/subaccounts "subaccounts"). For details, see [Exchanging Numbers Between Subaccounts](/docs/iam/api/subaccounts#exchanging-numbers "Exchanging Numbers Between Subaccounts").

(information)

## Info

Provisioning a phone number is a two-step process:

  1. Find an available phone number to provision by making a [`GET` request to the subresources of the AvailablePhoneNumbers resource](/docs/phone-numbers/api/availablephonenumber-resource).
  2. Make a [`POST` request to the IncomingPhoneNumbers resource](/docs/phone-numbers/api/incomingphonenumber-resource#create-an-incomingphonenumber-resource).


(warning)

## Warning

The order of columns in the CSV can change as we add fields to the API response. Design your application to handle column-order changes.

The following properties are available for the IncomingPhoneNumber resource:

* * *

## IncomingPhoneNumber Properties

incomingphonenumber-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created this IncomingPhoneNumber resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

addressSidSID<AD>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Address resource associated with the phone number.

Pattern: `^AD[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

addressRequirementsenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether the phone number requires an [Address](/docs/usage/api/address "Address") registered with Twilio. Can be: `none`, `any`, `local`, or `foreign`.

Possible values:

`none``any``local``foreign`

* * *

apiVersionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The API version used to start a new TwiML session.

* * *

betaboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether the phone number is new to the Twilio platform. Can be: `true` or `false`.

* * *

capabilitiesobject<phone-number-capabilities>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The set of Boolean properties that indicate whether a phone number can receive calls or messages. Capabilities are `Voice`, `SMS`, and `MMS` and each capability can be: `true` or `false`.

Show capabilities properties

Property nameTypeRequiredPIIDescriptionChild properties

mmsboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

smsboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

voiceboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

faxboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

dateCreatedstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT that the resource was created specified in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.

* * *

dateUpdatedstring<date-time-rfc-2822>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The date and time in GMT that the resource was last updated specified in [RFC 2822(link takes you to an external page)](https://www.ietf.org/rfc/rfc2822.txt "RFC 2822") format.

* * *

friendlyNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

The string that you assigned to describe the resource.

* * *

identitySidSID<RI>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Identity resource that we associate with the phone number. Some regions require an Identity to meet local regulations.

Pattern: `^RI[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

phoneNumberstring<phone-number>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The phone number in [E.164](/docs/glossary/what-e164 "E.164") format, which consists of a + followed by the country code and subscriber number.

* * *

originstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The phone number's origin. `twilio` identifies Twilio-owned phone numbers and `hosted` identifies hosted phone numbers.

* * *

sidSID<PN>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The unique string that that we created to identify this IncomingPhoneNumber resource.

Pattern: `^PN[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

smsApplicationSidSID<AP>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the application that handles SMS messages sent to the phone number. If an `sms_application_sid` is present, we ignore all `sms_*_url` values and use those of the application.

Pattern: `^AP[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

smsFallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we use to call `sms_fallback_url`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

* * *

smsFallbackUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that we call when an error occurs while retrieving or executing the TwiML from `sms_url`.

* * *

smsMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we use to call `sms_url`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

* * *

smsUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we call when the phone number receives an incoming SMS message.

* * *

statusCallbackstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we call using the `status_callback_method` to send status information to your application.

* * *

statusCallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we use to call `status_callback`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

* * *

trunkSidSID<TK>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Trunk that handles calls to the phone number. If a `trunk_sid` is present, we ignore all of the voice urls and voice applications and use those set on the Trunk. Setting a `trunk_sid` will automatically delete your `voice_application_sid` and vice versa.

Pattern: `^TK[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

uristring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URI of the resource, relative to `https://api.twilio.com`.

* * *

voiceReceiveModeenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Possible values:

`voice``fax`

* * *

voiceApplicationSidSID<AP>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the application that handles calls to the phone number. If a `voice_application_sid` is present, we ignore all of the voice urls and use those set on the application. Setting a `voice_application_sid` will automatically delete your `trunk_sid` and vice versa.

Pattern: `^AP[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

voiceCallerIdLookupboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether we look up the caller's caller-ID name from the CNAM database ($0.01 per look up). Can be: `true` or `false`.

* * *

voiceFallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we use to call `voice_fallback_url`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

* * *

voiceFallbackUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that we call when an error occurs retrieving or executing the TwiML requested by `url`.

* * *

voiceMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we use to call `voice_url`. Can be: `GET` or `POST`.

Possible values:

`GET``POST`

* * *

voiceUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we call when the phone number receives a call. The `voice_url` will not be used if a `voice_application_sid` or a `trunk_sid` is set.

* * *

emergencyStatusenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The parameter displays if emergency calling is enabled for this number. Active numbers may place emergency calls by dialing valid emergency numbers for the country.

Possible values:

`Active``Inactive`

* * *

emergencyAddressSidSID<AD>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the emergency address configuration that we use for emergency calling from this phone number.

Pattern: `^AD[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

emergencyAddressStatusenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The status of address registration with emergency services. A registered emergency address will be used during handling of emergency calls from this number.

Possible values:

`registered``unregistered``pending-registration``registration-failure``pending-unregistration``unregistration-failure`

* * *

bundleSidSID<BU>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations.

Pattern: `^BU[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

statusstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

* * *

typestring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The phone number type.

* * *

## Create an IncomingPhoneNumber resource

create-an-incomingphonenumber-resource page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers.json`

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

apiVersionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The API version to use for incoming calls made to the new phone number. The default is `2010-04-01`.

* * *

friendlyNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

A descriptive string that you created to describe the new phone number. It can be up to 64 characters long. By default, this is a formatted version of the new phone number.

* * *

smsApplicationSidSID<AP>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the application that should handle SMS messages sent to the new phone number. If an `sms_application_sid` is present, we ignore all of the `sms_*_url` urls and use those set on the application.

Pattern: `^AP[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

smsFallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method that we should use to call `sms_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`.

Possible values:

`GET``POST`

* * *

smsFallbackUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that we should call when an error occurs while requesting or executing the TwiML defined by `sms_url`.

* * *

smsMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method that we should use to call `sms_url`. Can be: `GET` or `POST` and defaults to `POST`.

Possible values:

`GET``POST`

* * *

smsUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we should call when the new phone number receives an incoming SMS message.

* * *

statusCallbackstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we should call using the `status_callback_method` to send status information to your application.

* * *

statusCallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST` and defaults to `POST`.

Possible values:

`GET``POST`

* * *

voiceApplicationSidSID<AP>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the application we should use to handle calls to the new phone number. If a `voice_application_sid` is present, we ignore all of the voice urls and use only those set on the application. Setting a `voice_application_sid` will automatically delete your `trunk_sid` and vice versa.

Pattern: `^AP[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

voiceCallerIdLookupboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to lookup the caller's name from the CNAM database and post it to your app. Can be: `true` or `false` and defaults to `false`.

* * *

voiceFallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method that we should use to call `voice_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`.

Possible values:

`GET``POST`

* * *

voiceFallbackUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that we should call when an error occurs retrieving or executing the TwiML requested by `url`.

* * *

voiceMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method that we should use to call `voice_url`. Can be: `GET` or `POST` and defaults to `POST`.

Possible values:

`GET``POST`

* * *

voiceUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that we should call to answer a call to the new phone number. The `voice_url` will not be called if a `voice_application_sid` or a `trunk_sid` is set.

* * *

emergencyStatusenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The parameter displays if emergency calling is enabled for this number. Active numbers may place emergency calls by dialing valid emergency numbers for the country.

Possible values:

`Active``Inactive`

* * *

emergencyAddressSidSID<AD>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the emergency address configuration to use for emergency calling from the new phone number.

Pattern: `^AD[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

trunkSidSID<TK>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Trunk we should use to handle calls to the new phone number. If a `trunk_sid` is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a `trunk_sid` will automatically delete your `voice_application_sid` and vice versa.

Pattern: `^TK[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

identitySidSID<RI>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Identity resource that we should associate with the new phone number. Some regions require an identity to meet local regulations.

Pattern: `^RI[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

addressSidSID<AD>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Address resource we should associate with the new phone number. Some regions require addresses to meet local regulations.

Pattern: `^AD[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

voiceReceiveModeenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Possible values:

`voice``fax`

* * *

bundleSidSID<BU>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations.

Pattern: `^BU[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

phoneNumberstring<phone-number>

required if AreaCode is not passed

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The phone number to purchase specified in [E.164](/docs/glossary/what-e164 "E.164") format. E.164 phone numbers consist of a + followed by the country code and subscriber number without punctuation characters. For example, +14155551234.

* * *

areaCodestring

required if PhoneNumber is not passed

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The desired area code for your new incoming phone number. Can be any three-digit, US or Canada area code. We will provision an available phone number within this area code for you. **You must provide an`area_code` or a `phone_number`.** (US and Canada only).

Copy code block


    {


      "AddressSid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "ApiVersion": "api_version",


      "AreaCode": "area_code",


      "EmergencyStatus": "Active",


      "EmergencyAddressSid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "IdentitySid": "RIaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "FriendlyName": "friendly_name",


      "PhoneNumber": "+18089255327",


      "SmsApplicationSid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "SmsFallbackMethod": "GET",


      "SmsFallbackUrl": "https://example.com",


      "SmsMethod": "GET",


      "SmsUrl": "https://example.com",


      "StatusCallback": "https://example.com",


      "StatusCallbackMethod": "GET",


      "VoiceApplicationSid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "VoiceCallerIdLookup": "true",


      "VoiceFallbackMethod": "GET",


      "VoiceFallbackUrl": "https://example.com",


      "VoiceMethod": "GET",


      "VoiceUrl": "https://example.com",


      "BundleSid": "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    }

The following examples demonstrate how to provision phone numbers with various configurations:

Provision a Phone NumberLink to code sample: Provision a Phone Number

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

    async function createIncomingPhoneNumber() {


    11

      const incomingPhoneNumber = await client.incomingPhoneNumbers.create({


    12

        phoneNumber: "+14155552344",


    13

      });


    14




    15

      console.log(incomingPhoneNumber.accountSid);


    16

    }


    17




    18

    createIncomingPhoneNumber();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "address_requirements": "none",


    4

      "address_sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "api_version": "2010-04-01",


    6

      "beta": false,


    7

      "capabilities": {


    8

        "voice": true,


    9

        "sms": false,


    10

        "mms": true,


    11

        "fax": false


    12

      },


    13

      "date_created": "Thu, 30 Jul 2015 23:19:04 +0000",


    14

      "date_updated": "Thu, 30 Jul 2015 23:19:04 +0000",


    15

      "emergency_status": "Active",


    16

      "emergency_address_sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

      "emergency_address_status": "registered",


    18

      "friendly_name": "friendly_name",


    19

      "identity_sid": "RIaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    20

      "origin": "origin",


    21

      "phone_number": "+14155552344",


    22

      "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    23

      "sms_application_sid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    24

      "sms_fallback_method": "GET",


    25

      "sms_fallback_url": "https://example.com",


    26

      "sms_method": "GET",


    27

      "sms_url": "https://example.com",


    28

      "status_callback": "https://example.com",


    29

      "status_callback_method": "GET",


    30

      "trunk_sid": null,


    31

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    32

      "voice_application_sid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    33

      "voice_caller_id_lookup": false,


    34

      "voice_fallback_method": "GET",


    35

      "voice_fallback_url": "https://example.com",


    36

      "voice_method": "GET",


    37

      "voice_url": "https://example.com",


    38

      "bundle_sid": "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    39

      "voice_receive_mode": "voice",


    40

      "status": "in-use",


    41

      "type": "local"


    42

    }

Provision a Phone Number with an AddressSid and a BundleSidLink to code sample: Provision a Phone Number with an AddressSid and a BundleSid

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

    async function createIncomingPhoneNumber() {


    11

      const incomingPhoneNumber = await client.incomingPhoneNumbers.create({


    12

        addressSid: "ADXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    13

        bundleSid: "BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    14

        phoneNumber: "+14155552344",


    15

      });


    16




    17

      console.log(incomingPhoneNumber.accountSid);


    18

    }


    19




    20

    createIncomingPhoneNumber();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "address_requirements": "none",


    4

      "address_sid": "ADXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    5

      "api_version": "2010-04-01",


    6

      "beta": false,


    7

      "capabilities": {


    8

        "voice": true,


    9

        "sms": false,


    10

        "mms": true,


    11

        "fax": false


    12

      },


    13

      "date_created": "Thu, 30 Jul 2015 23:19:04 +0000",


    14

      "date_updated": "Thu, 30 Jul 2015 23:19:04 +0000",


    15

      "emergency_status": "Active",


    16

      "emergency_address_sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

      "emergency_address_status": "registered",


    18

      "friendly_name": "friendly_name",


    19

      "identity_sid": "RIaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    20

      "origin": "origin",


    21

      "phone_number": "+14155552344",


    22

      "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    23

      "sms_application_sid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    24

      "sms_fallback_method": "GET",


    25

      "sms_fallback_url": "https://example.com",


    26

      "sms_method": "GET",


    27

      "sms_url": "https://example.com",


    28

      "status_callback": "https://example.com",


    29

      "status_callback_method": "GET",


    30

      "trunk_sid": null,


    31

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    32

      "voice_application_sid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    33

      "voice_caller_id_lookup": false,


    34

      "voice_fallback_method": "GET",


    35

      "voice_fallback_url": "https://example.com",


    36

      "voice_method": "GET",


    37

      "voice_url": "https://example.com",


    38

      "bundle_sid": "BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    39

      "voice_receive_mode": "voice",


    40

      "status": "in-use",


    41

      "type": "local"


    42

    }

Provision a Phone Number with a Voice URLLink to code sample: Provision a Phone Number with a Voice URL

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

    async function createIncomingPhoneNumber() {


    11

      const incomingPhoneNumber = await client.incomingPhoneNumbers.create({


    12

        phoneNumber: "+14155552344",


    13

        voiceUrl: "https://www.your-voice-url.com/example",


    14

      });


    15




    16

      console.log(incomingPhoneNumber.accountSid);


    17

    }


    18




    19

    createIncomingPhoneNumber();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "address_requirements": "none",


    4

      "address_sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "api_version": "2010-04-01",


    6

      "beta": false,


    7

      "capabilities": {


    8

        "voice": true,


    9

        "sms": false,


    10

        "mms": true,


    11

        "fax": false


    12

      },


    13

      "date_created": "Thu, 30 Jul 2015 23:19:04 +0000",


    14

      "date_updated": "Thu, 30 Jul 2015 23:19:04 +0000",


    15

      "emergency_status": "Active",


    16

      "emergency_address_sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

      "emergency_address_status": "registered",


    18

      "friendly_name": "friendly_name",


    19

      "identity_sid": "RIaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    20

      "origin": "origin",


    21

      "phone_number": "+14155552344",


    22

      "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    23

      "sms_application_sid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    24

      "sms_fallback_method": "GET",


    25

      "sms_fallback_url": "https://example.com",


    26

      "sms_method": "GET",


    27

      "sms_url": "https://example.com",


    28

      "status_callback": "https://example.com",


    29

      "status_callback_method": "GET",


    30

      "trunk_sid": null,


    31

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    32

      "voice_application_sid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    33

      "voice_caller_id_lookup": false,


    34

      "voice_fallback_method": "GET",


    35

      "voice_fallback_url": "https://example.com",


    36

      "voice_method": "GET",


    37

      "voice_url": "https://www.your-voice-url.com/example",


    38

      "bundle_sid": "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    39

      "voice_receive_mode": "voice",


    40

      "status": "in-use",


    41

      "type": "local"


    42

    }

Provision a Phone Number with an SMS URLLink to code sample: Provision a Phone Number with an SMS URL

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

    async function createIncomingPhoneNumber() {


    11

      const incomingPhoneNumber = await client.incomingPhoneNumbers.create({


    12

        phoneNumber: "+14155552344",


    13

        smsUrl: "https://www.your-sms-url.com/example",


    14

      });


    15




    16

      console.log(incomingPhoneNumber.accountSid);


    17

    }


    18




    19

    createIncomingPhoneNumber();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "address_requirements": "none",


    4

      "address_sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "api_version": "2010-04-01",


    6

      "beta": false,


    7

      "capabilities": {


    8

        "voice": true,


    9

        "sms": false,


    10

        "mms": true,


    11

        "fax": false


    12

      },


    13

      "date_created": "Thu, 30 Jul 2015 23:19:04 +0000",


    14

      "date_updated": "Thu, 30 Jul 2015 23:19:04 +0000",


    15

      "emergency_status": "Active",


    16

      "emergency_address_sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

      "emergency_address_status": "registered",


    18

      "friendly_name": "friendly_name",


    19

      "identity_sid": "RIaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    20

      "origin": "origin",


    21

      "phone_number": "+14155552344",


    22

      "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    23

      "sms_application_sid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    24

      "sms_fallback_method": "GET",


    25

      "sms_fallback_url": "https://example.com",


    26

      "sms_method": "GET",


    27

      "sms_url": "https://www.your-sms-url.com/example",


    28

      "status_callback": "https://example.com",


    29

      "status_callback_method": "GET",


    30

      "trunk_sid": null,


    31

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    32

      "voice_application_sid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    33

      "voice_caller_id_lookup": false,


    34

      "voice_fallback_method": "GET",


    35

      "voice_fallback_url": "https://example.com",


    36

      "voice_method": "GET",


    37

      "voice_url": "https://example.com",


    38

      "bundle_sid": "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    39

      "voice_receive_mode": "voice",


    40

      "status": "in-use",


    41

      "type": "local"


    42

    }

* * *

## Fetch an IncomingPhoneNumber resource

fetch-an-incomingphonenumber-resource page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{Sid}.json`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the IncomingPhoneNumber resource to fetch.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<PN>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to fetch.

Pattern: `^PN[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Fetch an IncomingPhoneNumberLink to code sample: Fetch an IncomingPhoneNumber

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

    async function fetchIncomingPhoneNumber() {


    11

      const incomingPhoneNumber = await client


    12

        .incomingPhoneNumbers("PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .fetch();


    14




    15

      console.log(incomingPhoneNumber.accountSid);


    16

    }


    17




    18

    fetchIncomingPhoneNumber();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "address_requirements": "none",


    4

      "address_sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "api_version": "2010-04-01",


    6

      "beta": false,


    7

      "capabilities": {


    8

        "voice": true,


    9

        "sms": false,


    10

        "mms": true,


    11

        "fax": false


    12

      },


    13

      "date_created": "Thu, 30 Jul 2015 23:19:04 +0000",


    14

      "date_updated": "Thu, 30 Jul 2015 23:19:04 +0000",


    15

      "emergency_status": "Active",


    16

      "emergency_address_sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

      "emergency_address_status": "registered",


    18

      "friendly_name": "(808) 925-5327",


    19

      "identity_sid": "RIaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    20

      "origin": "origin",


    21

      "phone_number": "+18089255327",


    22

      "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    23

      "sms_application_sid": "",


    24

      "sms_fallback_method": "POST",


    25

      "sms_fallback_url": "",


    26

      "sms_method": "POST",


    27

      "sms_url": "",


    28

      "status_callback": "",


    29

      "status_callback_method": "POST",


    30

      "trunk_sid": null,


    31

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    32

      "voice_application_sid": "",


    33

      "voice_caller_id_lookup": false,


    34

      "voice_fallback_method": "POST",


    35

      "voice_fallback_url": null,


    36

      "voice_method": "POST",


    37

      "voice_url": null,


    38

      "voice_receive_mode": "voice",


    39

      "status": "in-use",


    40

      "bundle_sid": "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    41

      "type": "local"


    42

    }

* * *

## Read multiple IncomingPhoneNumber resources

read-multiple-incomingphonenumber-resources page anchor

Positive FeedbackNegative Feedback

`GET https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers.json`

### Path parameters

path-parameters-2 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the IncomingPhoneNumber resources to read.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Query parameters

query-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

betaboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to include phone numbers new to the Twilio platform. Can be: `true` or `false` and the default is `true`.

* * *

friendlyNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

A string that identifies the IncomingPhoneNumber resources to read.

* * *

phoneNumberstring<phone-number>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial numbers and use '*' as a wildcard for any digit.

* * *

originstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to include phone numbers based on their origin. Can be: `twilio` or `hosted`. By default, phone numbers of all origin are included.

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

The following examples demonstrate how to list and filter IncomingPhoneNumber resources:

List all IncomingPhoneNumber resources for your accountLink to code sample: List all IncomingPhoneNumber resources for your account

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

    async function listIncomingPhoneNumber() {


    11

      const incomingPhoneNumbers = await client.incomingPhoneNumbers.list({


    12

        limit: 20,


    13

      });


    14




    15

      incomingPhoneNumbers.forEach((i) => console.log(i.accountSid));


    16

    }


    17




    18

    listIncomingPhoneNumber();

### Response

Note about this response

Copy response


    1

    {


    2

      "end": 0,


    3

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers.json?FriendlyName=friendly_name&Beta=true&PhoneNumber=%2B19876543210&PageSize=50&Page=0",


    4

      "incoming_phone_numbers": [


    5

        {


    6

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    7

          "address_requirements": "none",


    8

          "address_sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    9

          "api_version": "2010-04-01",


    10

          "beta": null,


    11

          "capabilities": {


    12

            "voice": true,


    13

            "sms": false,


    14

            "mms": true,


    15

            "fax": false


    16

          },


    17

          "date_created": "Thu, 30 Jul 2015 23:19:04 +0000",


    18

          "date_updated": "Thu, 30 Jul 2015 23:19:04 +0000",


    19

          "emergency_status": "Active",


    20

          "emergency_address_sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    21

          "emergency_address_status": "registered",


    22

          "friendly_name": "(808) 925-5327",


    23

          "identity_sid": "RIaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    24

          "origin": "origin",


    25

          "phone_number": "+18089255327",


    26

          "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    27

          "sms_application_sid": "",


    28

          "sms_fallback_method": "POST",


    29

          "sms_fallback_url": "",


    30

          "sms_method": "POST",


    31

          "sms_url": "",


    32

          "status_callback": "",


    33

          "status_callback_method": "POST",


    34

          "trunk_sid": null,


    35

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    36

          "voice_application_sid": "",


    37

          "voice_caller_id_lookup": false,


    38

          "voice_fallback_method": "POST",


    39

          "voice_fallback_url": null,


    40

          "voice_method": "POST",


    41

          "voice_url": null,


    42

          "bundle_sid": "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    43

          "voice_receive_mode": "voice",


    44

          "status": "in-use",


    45

          "type": "local"


    46

        }


    47

      ],


    48

      "next_page_uri": null,


    49

      "page": 0,


    50

      "page_size": 50,


    51

      "previous_page_uri": null,


    52

      "start": 0,


    53

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers.json?FriendlyName=friendly_name&Beta=true&PhoneNumber=%2B19876543210&PageSize=50&Page=0"


    54

    }

Filter IncomingPhoneNumbers with exact matchLink to code sample: Filter IncomingPhoneNumbers with exact match

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

    async function listIncomingPhoneNumber() {


    11

      const incomingPhoneNumbers = await client.incomingPhoneNumbers.list({


    12

        phoneNumber: "+14158675310",


    13

        limit: 20,


    14

      });


    15




    16

      incomingPhoneNumbers.forEach((i) => console.log(i.accountSid));


    17

    }


    18




    19

    listIncomingPhoneNumber();

### Response

Note about this response

Copy response


    1

    {


    2

      "end": 0,


    3

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers.json?FriendlyName=friendly_name&Beta=true&PhoneNumber=%2B19876543210&PageSize=50&Page=0",


    4

      "incoming_phone_numbers": [


    5

        {


    6

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    7

          "address_requirements": "none",


    8

          "address_sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    9

          "api_version": "2010-04-01",


    10

          "beta": null,


    11

          "capabilities": {


    12

            "voice": true,


    13

            "sms": false,


    14

            "mms": true,


    15

            "fax": false


    16

          },


    17

          "date_created": "Thu, 30 Jul 2015 23:19:04 +0000",


    18

          "date_updated": "Thu, 30 Jul 2015 23:19:04 +0000",


    19

          "emergency_status": "Active",


    20

          "emergency_address_sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    21

          "emergency_address_status": "registered",


    22

          "friendly_name": "(808) 925-5327",


    23

          "identity_sid": "RIaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    24

          "origin": "origin",


    25

          "phone_number": "+18089255327",


    26

          "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    27

          "sms_application_sid": "",


    28

          "sms_fallback_method": "POST",


    29

          "sms_fallback_url": "",


    30

          "sms_method": "POST",


    31

          "sms_url": "",


    32

          "status_callback": "",


    33

          "status_callback_method": "POST",


    34

          "trunk_sid": null,


    35

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    36

          "voice_application_sid": "",


    37

          "voice_caller_id_lookup": false,


    38

          "voice_fallback_method": "POST",


    39

          "voice_fallback_url": null,


    40

          "voice_method": "POST",


    41

          "voice_url": null,


    42

          "bundle_sid": "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    43

          "voice_receive_mode": "voice",


    44

          "status": "in-use",


    45

          "type": "local"


    46

        }


    47

      ],


    48

      "next_page_uri": null,


    49

      "page": 0,


    50

      "page_size": 50,


    51

      "previous_page_uri": null,


    52

      "start": 0,


    53

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers.json?FriendlyName=friendly_name&Beta=true&PhoneNumber=%2B19876543210&PageSize=50&Page=0"


    54

    }

Filter IncomingPhoneNumbers with partial matchLink to code sample: Filter IncomingPhoneNumbers with partial match

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

    async function listIncomingPhoneNumber() {


    11

      const incomingPhoneNumbers = await client.incomingPhoneNumbers.list({


    12

        phoneNumber: "867",


    13

        limit: 20,


    14

      });


    15




    16

      incomingPhoneNumbers.forEach((i) => console.log(i.accountSid));


    17

    }


    18




    19

    listIncomingPhoneNumber();

### Response

Note about this response

Copy response


    1

    {


    2

      "end": 0,


    3

      "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers.json?FriendlyName=friendly_name&Beta=true&PhoneNumber=%2B19876543210&PageSize=50&Page=0",


    4

      "incoming_phone_numbers": [


    5

        {


    6

          "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    7

          "address_requirements": "none",


    8

          "address_sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    9

          "api_version": "2010-04-01",


    10

          "beta": null,


    11

          "capabilities": {


    12

            "voice": true,


    13

            "sms": false,


    14

            "mms": true,


    15

            "fax": false


    16

          },


    17

          "date_created": "Thu, 30 Jul 2015 23:19:04 +0000",


    18

          "date_updated": "Thu, 30 Jul 2015 23:19:04 +0000",


    19

          "emergency_status": "Active",


    20

          "emergency_address_sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    21

          "emergency_address_status": "registered",


    22

          "friendly_name": "(808) 925-5327",


    23

          "identity_sid": "RIaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    24

          "origin": "origin",


    25

          "phone_number": "+18089255327",


    26

          "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    27

          "sms_application_sid": "",


    28

          "sms_fallback_method": "POST",


    29

          "sms_fallback_url": "",


    30

          "sms_method": "POST",


    31

          "sms_url": "",


    32

          "status_callback": "",


    33

          "status_callback_method": "POST",


    34

          "trunk_sid": null,


    35

          "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    36

          "voice_application_sid": "",


    37

          "voice_caller_id_lookup": false,


    38

          "voice_fallback_method": "POST",


    39

          "voice_fallback_url": null,


    40

          "voice_method": "POST",


    41

          "voice_url": null,


    42

          "bundle_sid": "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    43

          "voice_receive_mode": "voice",


    44

          "status": "in-use",


    45

          "type": "local"


    46

        }


    47

      ],


    48

      "next_page_uri": null,


    49

      "page": 0,


    50

      "page_size": 50,


    51

      "previous_page_uri": null,


    52

      "start": 0,


    53

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers.json?FriendlyName=friendly_name&Beta=true&PhoneNumber=%2B19876543210&PageSize=50&Page=0"


    54

    }

* * *

## Update an IncomingPhoneNumber resource

update-an-incomingphonenumber-resource page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{Sid}.json`

### Path parameters

path-parameters-3 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the IncomingPhoneNumber resource to update. For more information, see [Exchanging Numbers Between Subaccounts](/docs/iam/api/subaccounts#exchanging-numbers "Exchanging Numbers Between Subaccounts").

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<PN>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to update.

Pattern: `^PN[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters-1 page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the IncomingPhoneNumber resource to update. For more information, see [Exchanging Numbers Between Subaccounts](/docs/iam/api/subaccounts#exchanging-numbers "Exchanging Numbers Between Subaccounts").

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

apiVersionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The API version to use for incoming calls made to the phone number. The default is `2010-04-01`.

* * *

friendlyNamestring

Optional

[PII MTL: 30 days](/docs/glossary/what-is-personally-identifiable-information-pii#pii-fields)

A descriptive string that you created to describe this phone number. It can be up to 64 characters long. By default, this is a formatted version of the phone number.

* * *

smsApplicationSidSID<AP>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the application that should handle SMS messages sent to the number. If an `sms_application_sid` is present, we ignore all of the `sms_*_url` urls and use those set on the application.

Pattern: `^AP[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

smsFallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method that we should use to call `sms_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`.

Possible values:

`GET``POST`

* * *

smsFallbackUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that we should call when an error occurs while requesting or executing the TwiML defined by `sms_url`.

* * *

smsMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method that we should use to call `sms_url`. Can be: `GET` or `POST` and defaults to `POST`.

Possible values:

`GET``POST`

* * *

smsUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we should call when the phone number receives an incoming SMS message.

* * *

statusCallbackstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL we should call using the `status_callback_method` to send status information to your application.

* * *

statusCallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST` and defaults to `POST`.

Possible values:

`GET``POST`

* * *

voiceApplicationSidSID<AP>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the application we should use to handle phone calls to the phone number. If a `voice_application_sid` is present, we ignore all of the voice urls and use only those set on the application. Setting a `voice_application_sid` will automatically delete your `trunk_sid` and vice versa.

Pattern: `^AP[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

voiceCallerIdLookupboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to lookup the caller's name from the CNAM database and post it to your app. Can be: `true` or `false` and defaults to `false`.

* * *

voiceFallbackMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method that we should use to call `voice_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`.

Possible values:

`GET``POST`

* * *

voiceFallbackUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that we should call when an error occurs retrieving or executing the TwiML requested by `url`.

* * *

voiceMethodenum<http-method>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The HTTP method that we should use to call `voice_url`. Can be: `GET` or `POST` and defaults to `POST`.

Possible values:

`GET``POST`

* * *

voiceUrlstring<uri>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URL that we should call to answer a call to the phone number. The `voice_url` will not be called if a `voice_application_sid` or a `trunk_sid` is set.

* * *

emergencyStatusenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The parameter displays if emergency calling is enabled for this number. Active numbers may place emergency calls by dialing valid emergency numbers for the country.

Possible values:

`Active``Inactive`

* * *

emergencyAddressSidSID<AD>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the emergency address configuration to use for emergency calling from this phone number.

Pattern: `^AD[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

trunkSidSID<TK>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Trunk we should use to handle phone calls to the phone number. If a `trunk_sid` is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a `trunk_sid` will automatically delete your `voice_application_sid` and vice versa.

Pattern: `^TK[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

voiceReceiveModeenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Possible values:

`voice``fax`

* * *

identitySidSID<RI>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Identity resource that we should associate with the phone number. Some regions require an identity to meet local regulations.

Pattern: `^RI[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

addressSidSID<AD>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Address resource we should associate with the phone number. Some regions require addresses to meet local regulations.

Pattern: `^AD[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

bundleSidSID<BU>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations.

Pattern: `^BU[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Copy code block


    {


      "AccountSid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "AddressSid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "ApiVersion": "api_version",


      "EmergencyStatus": "Inactive",


      "EmergencyAddressSid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "FriendlyName": "friendly_name",


      "IdentitySid": "RIaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "SmsApplicationSid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "SmsFallbackMethod": "GET",


      "SmsFallbackUrl": "https://example.com",


      "SmsMethod": "GET",


      "SmsUrl": "https://example.com",


      "StatusCallback": "https://example.com",


      "StatusCallbackMethod": "GET",


      "VoiceApplicationSid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


      "VoiceCallerIdLookup": "true",


      "VoiceFallbackMethod": "GET",


      "VoiceFallbackUrl": "https://example.com",


      "VoiceMethod": "GET",


      "VoiceUrl": "https://example.com",


      "VoiceReceiveMode": "voice",


      "BundleSid": "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


    }

The following examples demonstrate how to update IncomingPhoneNumber resources with different configurations:

Update IncomingPhoneNumber to include an AddressSid and a BundleSidLink to code sample: Update IncomingPhoneNumber to include an AddressSid and a BundleSid

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

    async function updateIncomingPhoneNumber() {


    11

      const incomingPhoneNumber = await client


    12

        .incomingPhoneNumbers("PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .update({


    14

          addressSid: "ADXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    15

          bundleSid: "BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    16

        });


    17




    18

      console.log(incomingPhoneNumber.accountSid);


    19

    }


    20




    21

    updateIncomingPhoneNumber();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "address_requirements": "none",


    4

      "address_sid": "ADXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    5

      "api_version": "2010-04-01",


    6

      "beta": false,


    7

      "capabilities": {


    8

        "voice": true,


    9

        "sms": false,


    10

        "mms": true,


    11

        "fax": false


    12

      },


    13

      "date_created": "Thu, 30 Jul 2015 23:19:04 +0000",


    14

      "date_updated": "Thu, 30 Jul 2015 23:19:04 +0000",


    15

      "emergency_status": "Inactive",


    16

      "emergency_address_sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

      "emergency_address_status": "registered",


    18

      "friendly_name": "(808) 925-5327",


    19

      "identity_sid": "RIaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    20

      "origin": "origin",


    21

      "phone_number": "+18089255327",


    22

      "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    23

      "sms_application_sid": "",


    24

      "sms_fallback_method": "POST",


    25

      "sms_fallback_url": "",


    26

      "sms_method": "POST",


    27

      "sms_url": "",


    28

      "status_callback": "",


    29

      "status_callback_method": "POST",


    30

      "trunk_sid": null,


    31

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    32

      "voice_application_sid": "",


    33

      "voice_caller_id_lookup": true,


    34

      "voice_fallback_method": "POST",


    35

      "voice_fallback_url": null,


    36

      "voice_method": "POST",


    37

      "voice_url": null,


    38

      "voice_receive_mode": "voice",


    39

      "status": "in-use",


    40

      "bundle_sid": "BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",


    41

      "type": "local"


    42

    }

Update IncomingPhoneNumber to use a new Voice URLLink to code sample: Update IncomingPhoneNumber to use a new Voice URL

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

    async function updateIncomingPhoneNumber() {


    11

      const incomingPhoneNumber = await client


    12

        .incomingPhoneNumbers("PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .update({ voiceUrl: "https://www.your-new-voice-url.com/example" });


    14




    15

      console.log(incomingPhoneNumber.accountSid);


    16

    }


    17




    18

    updateIncomingPhoneNumber();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "address_requirements": "none",


    4

      "address_sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "api_version": "2010-04-01",


    6

      "beta": false,


    7

      "capabilities": {


    8

        "voice": true,


    9

        "sms": false,


    10

        "mms": true,


    11

        "fax": false


    12

      },


    13

      "date_created": "Thu, 30 Jul 2015 23:19:04 +0000",


    14

      "date_updated": "Thu, 30 Jul 2015 23:19:04 +0000",


    15

      "emergency_status": "Inactive",


    16

      "emergency_address_sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

      "emergency_address_status": "registered",


    18

      "friendly_name": "(808) 925-5327",


    19

      "identity_sid": "RIaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    20

      "origin": "origin",


    21

      "phone_number": "+18089255327",


    22

      "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    23

      "sms_application_sid": "",


    24

      "sms_fallback_method": "POST",


    25

      "sms_fallback_url": "",


    26

      "sms_method": "POST",


    27

      "sms_url": "",


    28

      "status_callback": "",


    29

      "status_callback_method": "POST",


    30

      "trunk_sid": null,


    31

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    32

      "voice_application_sid": "",


    33

      "voice_caller_id_lookup": true,


    34

      "voice_fallback_method": "POST",


    35

      "voice_fallback_url": null,


    36

      "voice_method": "POST",


    37

      "voice_url": "https://www.your-new-voice-url.com/example",


    38

      "voice_receive_mode": "voice",


    39

      "status": "in-use",


    40

      "bundle_sid": "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    41

      "type": "local"


    42

    }

Update IncomingPhoneNumber to use a new SMS URLLink to code sample: Update IncomingPhoneNumber to use a new SMS URL

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

    async function updateIncomingPhoneNumber() {


    11

      const incomingPhoneNumber = await client


    12

        .incomingPhoneNumbers("PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .update({ smsUrl: "https://www.your-new-sms-url.com/example" });


    14




    15

      console.log(incomingPhoneNumber.accountSid);


    16

    }


    17




    18

    updateIncomingPhoneNumber();

### Response

Note about this response

Copy response


    1

    {


    2

      "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    3

      "address_requirements": "none",


    4

      "address_sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    5

      "api_version": "2010-04-01",


    6

      "beta": false,


    7

      "capabilities": {


    8

        "voice": true,


    9

        "sms": false,


    10

        "mms": true,


    11

        "fax": false


    12

      },


    13

      "date_created": "Thu, 30 Jul 2015 23:19:04 +0000",


    14

      "date_updated": "Thu, 30 Jul 2015 23:19:04 +0000",


    15

      "emergency_status": "Inactive",


    16

      "emergency_address_sid": "ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    17

      "emergency_address_status": "registered",


    18

      "friendly_name": "(808) 925-5327",


    19

      "identity_sid": "RIaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    20

      "origin": "origin",


    21

      "phone_number": "+18089255327",


    22

      "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    23

      "sms_application_sid": "",


    24

      "sms_fallback_method": "POST",


    25

      "sms_fallback_url": "",


    26

      "sms_method": "POST",


    27

      "sms_url": "https://www.your-new-sms-url.com/example",


    28

      "status_callback": "",


    29

      "status_callback_method": "POST",


    30

      "trunk_sid": null,


    31

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",


    32

      "voice_application_sid": "",


    33

      "voice_caller_id_lookup": true,


    34

      "voice_fallback_method": "POST",


    35

      "voice_fallback_url": null,


    36

      "voice_method": "POST",


    37

      "voice_url": null,


    38

      "voice_receive_mode": "voice",


    39

      "status": "in-use",


    40

      "bundle_sid": "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    41

      "type": "local"


    42

    }

* * *

## Delete an IncomingPhoneNumber resource

delete-an-incomingphonenumber-resource page anchor

Positive FeedbackNegative Feedback

`DELETE https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{Sid}.json`

Deleting an IncomingPhoneNumber releases it from your account. Twilio will no longer answer calls to this number and will stop charging the monthly fee.

Twilio might reclaim and assign the number to another customer, so delete numbers with caution. If you make a mistake, contact [Twilio Support(link takes you to an external page)](https://help.twilio.com/ "Twilio Support"). We might be able to give you the number back.

### Path parameters

path-parameters-4 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the IncomingPhoneNumber resources to delete.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<PN>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The Twilio-provided string that uniquely identifies the IncomingPhoneNumber resource to delete.

Pattern: `^PN[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

Delete an IncomingPhoneNumberLink to code sample: Delete an IncomingPhoneNumber

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

    async function deleteIncomingPhoneNumber() {


    11

      await client


    12

        .incomingPhoneNumbers("PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .remove();


    14

    }


    15




    16

    deleteIncomingPhoneNumber();