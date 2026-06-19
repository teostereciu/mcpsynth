# Payments subresource

*Source: https://www.twilio.com/docs/voice/api/payment-resource*

---

# Payments subresource

Positive FeedbackNegative Feedback

* * *

Payments is a subresource of [Calls](/docs/voice/api/call-resource "Calls").

* * *

## Agent-assisted payments

agent-assisted-payments page anchor

Positive FeedbackNegative Feedback

Agent-assisted payments allow agents to collect customer payment information in a PCI-compliant manner on Twilio voice calls in the contact center. With agent-assisted payments, the agent stays on the phone and guides the customer through the payment flow, requesting the various required pieces of payment information one item at a time.

The agent can control the payment flow asking for payment information in the order they see best for the customer and even re-request information as needed. When the customer is entering their payment information, the agent will not be able to hear the DTMF (Dual-Tone Multi-Frequency) tones, ensuring PCI DSS (Payment Card Industry Data Security Standard) compliance of the payment information and the security of the customer payment information.

Once the agent has progressed through all the steps to gather the payment information from the customer, they complete the capture via Twilio. Twilio sends the payment information directly to the payment connector for processing, ensuring no card information is ever divulged to the agent.

(information)

## Support for Twilio Regions

[<Pay>](/docs/voice/twiml/pay "<Pay>") and the [Payment resource](/docs/voice/api/payment-resource "Payment resource") are now available in the Ireland (IE1) and Australia (AU1) Regions for the following Pay Connectors: Base Commerce, Braintree, CardConnect, Chase Paymentech, [Generic Pay Connector](/docs/voice/twiml/pay/generic-pay-connector "Generic Pay Connector"), and Shuttle.

  * For outbound calls, [follow the guide for outbound calls in non-US Regions](/docs/global-infrastructure/create-an-outbound-call-via-rest-api-in-a-non-us-twilio-region "follow the guide for outbound calls in non-US Regions").
  * For inbound calls, [follow the guide for inbound call processing in non-US Regions](/docs/global-infrastructure/inbound-call-processing "follow the guide for inbound call processing in non-US Regions").
  * For more info on Twilio Regions, [visit the Global Infrastructure docs](/docs/global-infrastructure "visit the Global Infrastructure docs").


### Workflow

workflow page anchor

Positive FeedbackNegative Feedback

  * Agent requests some information, including payment method, from the customer and [begins a Payment session](/docs/voice/api/payment-resource#create-a-payment-session "begins a Payment session").
  * Agent triggers [API calls](/docs/voice/api/payment-resource#update-a-payment-session "API calls") through their UI to collect specific pieces of payment information from the customer, e.g., credit card number, expiration date, or bank account number.
  * The Caller enters the requested payment information using their phone keypad. Agents are not able to hear any DTMF tones.
  * Once the customer is done, the agent sees the result of the customer's input, e.g., `xxxx xxxx xxxx 4242` or `invalid-card-number`.
  * Agent requests the next piece of required payment information and continues to do so until all the information needed is entered.
    * The agent can re-request a piece of payment information as needed in any order and at any point during the flow.
    * The agent is also able to [cancel the payment](/docs/voice/api/payment-resource#code-update-a-payment-cancel "cancel the payment") at any point during the flow.
  * Once all the information is collected, the agent [completes the Payment session](/docs/voice/api/payment-resource#code-update-a-payment-complete "completes the Payment session") and receives the result of the payment.


### API design and workflow

api-design-and-workflow page anchor

Positive FeedbackNegative Feedback

With Agent assistance the key is to capture customer information while the Agent is on the call with the customer. This means the agent can interact with the customer guiding them through the experience of entering their card details. A typical agent flow is outlined below:

  * The agent collects and enters information like payment method, charge amount or token type, and then [starts the Payment session](/docs/voice/api/payment-resource#create-a-payment-session "starts the Payment session").
  * The agent then makes an [update request](/docs/voice/api/payment-resource#update-a-payment-session "update request") (through their own UI) for each piece of payment information in succession.
  * If customers make a mistake while entering information, the agent makes an [update request](/docs/voice/api/payment-resource#update-a-payment-session "update request") again to re-capture that particular information.
  * Once all the required payment information has been collected, the Agent [completes the Payment session](/docs/voice/api/payment-resource#code-update-a-payment-complete "completes the Payment session") by setting the status to `complete`, which then processes the payment and completes the transaction. The agent can also [cancel the Payment session](/docs/voice/api/payment-resource#code-update-a-payment-cancel "cancel the Payment session"), if required at this stage, by setting the status in the [update request](/docs/voice/api/payment-resource#update-a-payment-session "update request") to `cancel`.
  * Resulting information in each of the calls above will be delivered via [status callbacks](/docs/voice/api/payment-resource#statuscallback "status callbacks"), which can be used to update the agent UI in near real-time.


* * *

## Payments properties

payments-properties page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescriptionChild properties

accountSidSID<AC>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that created the Payments resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

callSidSID<CA>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Call](/docs/voice/api/call-resource "Call") the Payments resource is associated with. This will refer to the call sid that is producing the payment card (credit/ACH) information thru DTMF.

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<PK>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the Payments resource.

Pattern: `^PK[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

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

uristring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The URI of the resource, relative to `https://api.twilio.com`.

* * *

## Create a Payment session

create-a-payment-session page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Payments.json`

### Path parameters

path-parameters page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that will create the resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

callSidSID<CA>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the call that will create the resource. Call leg associated with this sid is expected to provide payment information thru DTMF.

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

idempotencyKeystring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A unique token that will be used to ensure that multiple API calls with the same information do not result in multiple transactions. This should be a unique string value per API call and can be a randomly generated.

* * *

statusCallbackstring<uri>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Provide an absolute or relative URL to receive status updates regarding your Pay session. Read more about the [expected StatusCallback values](/docs/voice/api/payment-resource#statuscallback "expected StatusCallback values")

* * *

bankAccountTypeenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Type of bank account if payment source is ACH. One of `consumer-checking`, `consumer-savings`, or `commercial-checking`. The default value is `consumer-checking`.

Possible values:

`consumer-checking``consumer-savings``commercial-checking`

* * *

chargeAmountnumber

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A positive decimal value less than 1,000,000 to charge against the credit card or bank account. Default currency can be overwritten with `currency` field. Leave blank or set to 0 to tokenize.

* * *

currencystring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The currency of the `charge_amount`, formatted as [ISO 4127(link takes you to an external page)](http://www.iso.org/iso/home/standards/currency_codes.htm "ISO 4127") format. The default value is `USD` and all values allowed from the Pay Connector are accepted.

* * *

descriptionstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The description can be used to provide more details regarding the transaction. This information is submitted along with the payment details to the Payment Connector which are then posted on the transactions.

* * *

inputstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A list of inputs that should be accepted. Currently only `dtmf` is supported. All digits captured during a pay session are redacted from the logs.

* * *

minPostalCodeLengthinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A positive integer that is used to validate the length of the `PostalCode` inputted by the user. User must enter this many digits.

* * *

parameter

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A single-level JSON object used to pass custom parameters to payment processors. (Required for ACH payments). The information that has to be included here depends on the <Pay> Connector. [Read more(link takes you to an external page)](https://www.twilio.com/console/voice/pay-connectors "Read more").

* * *

paymentConnectorstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

This is the unique name corresponding to the Pay Connector installed in the Twilio Add-ons. Learn more about [<Pay> Connectors(link takes you to an external page)](https://www.twilio.com/console/voice/pay-connectors). The default value is `Default`.

* * *

paymentMethodenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Type of payment being captured. One of `credit-card` or `ach-debit`. The default value is `credit-card`.

Possible values:

`credit-card``ach-debit`

* * *

postalCodeboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Indicates whether the credit card postal code (zip code) is a required piece of payment information that must be provided by the caller. The default is `true`.

* * *

securityCodeboolean

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Indicates whether the credit card security code is a required piece of payment information that must be provided by the caller. The default is `true`.

* * *

timeoutinteger

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The number of seconds that <Pay> should wait for the caller to press a digit between each subsequent digit, after the first one, before moving on to validate the digits captured. The default is `5`, maximum is `600`.

* * *

tokenTypeenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Indicates whether the payment method should be tokenized as a `one-time`, `reusable`, or `payment-method` token. The default value is `reusable`. Do not enter a charge amount when tokenizing. If a charge amount is entered, the payment method will be charged and not tokenized.

Possible values:

`one-time``reusable``payment-method`

* * *

validCardTypesstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Credit card types separated by space that Pay should accept. The default value is `visa mastercard amex`

* * *

requireMatchingInputsstring

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A comma-separated list of payment information fields that require the caller to enter the same value twice for confirmation. Supported values are `payment-card-number`, `expiration-date`, `security-code`, and `postal-code`.

* * *

confirmationenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Whether to prompt the caller to confirm their payment information before submitting to the payment gateway. If `true`, the caller will hear the last 4 digits of their card or account number and must press 1 to confirm or 2 to cancel. Default is `false`.

Possible values:

`true``false`

Copy code block


    {


      "ChargeAmount": "12.00",


      "Currency": "USD",


      "Description": "api testing",


      "IdempotencyKey": "abcd",


      "Input": "dtmf",


      "Parameter": "{'name':'foobar'}",


      "PaymentConnector": "stripe_connector",


      "PaymentMethod": "credit-card",


      "PostalCode": true,


      "SecurityCode": true,


      "StatusCallback": "https://myapp.com/payments",


      "ValidCardTypes": "visa amex"


    }

Create a Payment sessionLink to code sample: Create a Payment session

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

    async function createPayments() {


    11

      const payment = await client


    12

        .calls("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .payments.create({


    14

          idempotencyKey: "IdempotencyKey",


    15

          statusCallback: "https://www.example.com",


    16

        });


    17




    18

      console.log(payment.accountSid);


    19

    }


    20




    21

    createPayments();

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

      "date_created": "Wed, 18 Dec 2019 20:02:01 +0000",


    5

      "date_updated": "Wed, 18 Dec 2019 20:02:01 +0000",


    6

      "sid": "PKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    7

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments/PKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    8

    }

### StatusCallback

statuscallback page anchor

Positive FeedbackNegative Feedback

Provide an absolute or relative URL for this parameter. Twilio Pay will make a `POST` request to this URL whenever there is an update to the Parameter being captured. The `POST` request will have the following parameters:

**Parameter**| **Description**
---|---
`AccountSid`| The unique identifier of the Account responsible for this Payment session
`CallSid`| The unique identifier for the call associated with the Payment sessions. `CallSid` will always refer to the parent leg of a two-leg call
`Sid`| The unique identifier of the current Payment session
`DateCreated`| The date when the Payment session was started
`BankAccountType`| If the `ach-debit` PaymentMethod is used, the Bank Account Type provided by the caller and entered by the agent
`ChargeAmount`| If not tokenizing — i.e., the charge amount is specified and greater than zero — the amount to charge the payment method
`PaymentConnector`| The unique name of Payment Connector corresponding to the [Pay Connector](/docs/voice/twiml/pay/pay-connectors "Pay Connector") installed in Twilio Marketplace
`PaymentMethod`| `Ach-debit` or `credit-card`
`TokenType`| One-time or reusable if charge amount not specified

(information)

## Info

All `StatusCallback` requests will contain these fields. Additional `StatusCallback` values can be found during the [`Update`](/docs/voice/api/payment-resource#statuscallback-update-payment-session) and [`Complete/Cancel`](/docs/voice/api/payment-resource#statuscallback-cancelcomplete-payment-session) APIs.

* * *

## Update a Payment session

update-a-payment-session page anchor

Positive FeedbackNegative Feedback

`POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Payments/{Sid}.json`

### Path parameters

path-parameters-1 page anchor

Positive FeedbackNegative Feedback

Property nameTypeRequiredPIIDescription

accountSidSID<AC>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the [Account](/docs/iam/api/account "Account") that will update the resource.

Pattern: `^AC[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

callSidSID<CA>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of the call that will update the resource. This should be the same call sid that was used to create payments resource.

Pattern: `^CA[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

* * *

sidSID<PK>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The SID of Payments session that needs to be updated.

Pattern: `^PK[0-9a-fA-F]{32}$`Min length: `34`Max length: `34`

### Request body parameters

request-body-parameters-1 page anchor

Positive FeedbackNegative Feedback

Encoding type:`application/x-www-form-urlencoded`

SchemaExample

Property nameTypeRequiredPIIDescriptionChild properties

idempotencyKeystring

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

A unique token that will be used to ensure that multiple API calls with the same information do not result in multiple transactions. This should be a unique string value per API call and can be a randomly generated.

* * *

statusCallbackstring<uri>

required

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Provide an absolute or relative URL to receive status updates regarding your Pay session. Read more about the [Update](/docs/voice/api/payment-resource#statuscallback-update "Update") and [Complete/Cancel](/docs/voice/api/payment-resource#statuscallback-cancelcomplete "Complete/Cancel") POST requests.

* * *

captureenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

The piece of payment information that you wish the caller to enter. Must be one of `payment-card-number`, `expiration-date`, `security-code`, `postal-code`, `bank-routing-number`, `bank-account-number`, or their `-matcher` variants for input confirmation when `RequireMatchingInputs` is enabled.

Possible values:

`payment-card-number``expiration-date``security-code``postal-code``bank-routing-number``bank-account-number``payment-card-number-matcher``expiration-date-matcher``security-code-matcher``postal-code-matcher`

* * *

statusenum<string>

Optional

[Not PII](/docs/glossary/what-is-personally-identifiable-information-pii#fields-marked-not-pii)

Indicates whether the current payment session should be cancelled or completed. When `cancel` the payment session is cancelled. When `complete`, Twilio sends the payment information to the selected Pay Connector for processing.

Possible values:

`complete``cancel`

Select from available examples

Copy code block


    {


      "Capture": "payment-card-number",


      "IdempotencyKey": "abcd",


      "StatusCallback": "https://myapp.com/payments"


    }

Update a Payment sessionLink to code sample: Update a Payment session

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

    async function updatePayments() {


    11

      const payment = await client


    12

        .calls("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .payments("PKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    14

        .update({


    15

          capture: "payment-card-number",


    16

          idempotencyKey: "request-4",


    17

          statusCallback: "https://www.example.com",


    18

        });


    19




    20

      console.log(payment.accountSid);


    21

    }


    22




    23

    updatePayments();

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

      "date_created": "Wed, 18 Dec 2019 20:02:01 +0000",


    5

      "date_updated": "Wed, 18 Dec 2019 20:02:01 +0000",


    6

      "sid": "PKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    7

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments/PKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    8

    }

### StatusCallback (Update Payment Session)

statuscallback-update-payment-session page anchor

Positive FeedbackNegative Feedback

Provide an absolute or relative URL for this parameter. Twilio Pay will make a `POST` request to this URL whenever the update request is made and whenever there is an update to the Parameter being captured. The `POST` request will contain all of [common StatusCallback parameters](/docs/voice/api/payment-resource#statuscallback "common StatusCallback parameters") as well as these additional parameters:

**Parameter**| **Description**
---|---
`DateUpdated`| The date when the Payment session was last updated
`BankAccountNumber`| If the `PaymentMethod` is arch-debit the Bank Account Number entered by the caller. Twilio will only return the last two digits. For example, if the Bank Account Number is 508862392, then Pay will return `BankAccountNumber=*******92`
`BankRoutingNumber`| If the `PaymentMethod` is arch-debit the Bank Routing Number provided by the caller. Twilio will return the full routing number entered. For example, if caller enters 121181976 as their Bank Routing Number provided, then Pay will return `BankRoutingNumber=121181976`
`Capture`| The piece of payment information that Pay was expecting
`ChargeAmount`| If not tokenizing — i.e., the charge amount was specified and greater than zero — the amount to charge the payment method
`ErrorType`| The full list of error types is visible [here](/docs/voice/twiml/pay/prompt#errortype "here")
`ExpirationDate`| If the `PaymentMethod` is `credit-card`, the expiration date that is input by the caller. For example, `ExpirationDate=0522`. The expiration date is not PCI data, so it can be clearly visible
`PartialResult`| `true` if DTMF is still being captured and `false` once all the digits of the piece of payment information being captured have been entered
`PaymentCardNumber`| If the `PaymentMethod` is `credit-card`, the card number input by the caller with only the last 4 digits visible. For example, `PaymentCardNumber=xxxx-xxxxxx-x4001`
`PaymentCardPostalCode`| If the `PaymentMethod` is `credit-card`, the postal code input by the caller or by the agent. For example, `PaymentCardPostalCode=94109`. Postal Code is not PCI data, so it can be clearly visible.
`PaymentCardType`| If the `PaymentMethod` is `credit-card`, the type of card input by the caller. For example, `PaymentCardType=amex`. The value provided here will be one of the values provided with the `cardTypes` parameter in the Start API
`Required`| The pieces of payment information that remain to be collected. For example, if postal code and security code are false and credit card number has already been input, then `Required=ExpirationDate`
`SecurityCode`| If the `PaymentMethod` is `credit-card`, the security code input by the caller with all digits redacted, for example, `SecurityCode=xxx`

### Status

status page anchor

Positive FeedbackNegative Feedback

Indicate whether the current payment session should be cancelled or completed when this API request is made. When the status is `cancel`, the payment session will be cancelled. You will have to make a [`POST` request](/docs/voice/api/payment-resource#create-a-payment-session) to start a new payment session. When the status is `complete`, Twilio sends the payment information to the selected Pay connector for processing.

Update a Payment: completeLink to code sample: Update a Payment: complete

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

    async function updatePayments() {


    11

      const payment = await client


    12

        .calls("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .payments("PKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    14

        .update({


    15

          idempotencyKey: "IdempotencyKey",


    16

          status: "complete",


    17

          statusCallback: "https://www.example.com",


    18

        });


    19




    20

      console.log(payment.accountSid);


    21

    }


    22




    23

    updatePayments();

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

      "date_created": "Wed, 18 Dec 2019 20:02:01 +0000",


    5

      "date_updated": "Wed, 18 Dec 2019 20:02:01 +0000",


    6

      "sid": "PKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    7

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments/PKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    8

    }

Update a Payment: cancelLink to code sample: Update a Payment: cancel

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

    async function updatePayments() {


    11

      const payment = await client


    12

        .calls("CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    13

        .payments("PKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


    14

        .update({


    15

          idempotencyKey: "IdempotencyKey",


    16

          status: "cancel",


    17

          statusCallback: "https://www.example.com",


    18

        });


    19




    20

      console.log(payment.accountSid);


    21

    }


    22




    23

    updatePayments();

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

      "date_created": "Wed, 18 Dec 2019 20:02:01 +0000",


    5

      "date_updated": "Wed, 18 Dec 2019 20:02:01 +0000",


    6

      "sid": "PKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",


    7

      "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payments/PKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"


    8

    }

### StatusCallback (Cancel/Complete Payment Session)

statuscallback-cancelcomplete-payment-session page anchor

Positive FeedbackNegative Feedback

Provide an absolute or relative URL for this parameter. Twilio Pay will make a `POST` request to this URL whenever the Cancel/Complete API is called. The `POST` request will contain all of [common StatusCallback parameters](/docs/voice/api/payment-resource#statuscallback "common StatusCallback parameters") as well as these additional parameters:

**Parameter**| **Description**
---|---
`DateUpdated`| The date when the Payment session was last updated
`ConnectorError`| This parameter contains the error code/message received from the underlying payment gateway
`PayErrorCode`| A numerical error code that gives more details about the error. To learn more about the error, please visit the [error page](/docs/api/errors "error page") and search for the error code
`PaymentError`| Payment error for failures. For example, `card is declined`
`PaymentConfirmationCode`| If the payment method provided was charged and not tokenized, this is the confirmation code from the Payment Gateway
`PaymentToken`| The tokenized value of the credit card or ACH payment data. Payment will not be tokenized if a charge amount is provided. Values will vary by connector:
Base Commerce: `BankCard token`
Braintree:`token`
CardConnect: `token`
Chase: `no value`
Stripe: `one-time token`
`ProfileId`| The identifier of the customer object to which the payment is associated. Can be used as a token depending on the Connector. Payment will not be tokenized if a charge amount is provided. Values will vary by connector:
Base Commerce: `no value`
Braintree: `ID of the customer object (cannot be used as a token)`
CardConnect: `profile`
Chase: `customer reference number`
Stripe: `ID of the customer resource`
`Result`| The result of the transaction.
`success`: Twilio successfully captured the payment data and either tokenized or processed the payment
`payment-connector-error`: Twilio Pay experienced an error communicating with Payment Gateway
`caller-interrupted-with-star`: Caller pressed the ***** (star) key to interrupt the Payment session
`caller-hung-up`: The caller hung up the call
`validation-error`: An invalid parameter value, e.g., `chargeAmount="-0.5"`