# acs-webhook/1/post/balancePlatform.authentication.created

*Source: https://docs.adyen.com/api-explorer/acs-webhook/1/post/balancePlatform.authentication.created*

---

# Cardholder authenticated
Adyen sends this webhook when the process of cardholder authentication is finalized, whether it is completed successfully, fails, or expires.
Contains event details.
Contains information about the authentication.
Universally unique transaction identifier assigned by the Access Control Server (ACS) to identify a single transaction.
Information about Strong Customer Authentication (SCA). Returned whentypeischallenge.
Indicator informing the Access Control Server (ACS) and the Directory Server (DS) that the authentication has been cancelled. Possible values:
- 00: Data element is absent or value has been sent back with the keychallengeCancel.
- 01: Cardholder selectedCancel.
- 02: 3DS Requestor cancelled Authentication.
- 03: Transaction abandoned.
- 04: Transaction timed out at ACS — other timeouts.
- 05: Transaction timed out at ACS — first CReq not received by ACS.
- 06: Transaction error.
- 07: Unknown.
- 08: Transaction time out at SDK.
The flow used in the challenge. Possible values:
- PWD_OTP_PHONE_FL: one-time password (OTP) flow via SMS
- PWD_OTP_EMAIL_FL: one-time password (OTP) flow via email
- OOB_TRIGGER_FL: out-of-band (OOB) flow
The last time of interaction with the challenge.
The last four digits of the phone number used in the challenge.
The number of times the one-time password (OTP) was resent during the challenge.
The number of retries used in the challenge.
Specifies a preference for receiving a challenge. Possible values:
- 01: No preference
- 02: No challenge requested
- 03: Challenge requested (preference)
- 04: Challenge requested (mandate)
- 05: No challenge requested (transactional risk analysis is already performed)
- 07: No challenge requested (SCA is already performed)
- 08: No challenge requested (trusted beneficiaries exemption of no challenge required)
- 09: Challenge requested (trusted beneficiaries prompt requested if challenge required)
- 80: No challenge requested (secure corporate payment with Mastercard)
- 82: No challenge requested (secure corporate payment with Visa)
Date and time in UTC of the cardholder authentication.
ISO 8601format: YYYY-MM-DDThh:mm:ss+TZD, for example,2020-12-18T10:15:30+01:00.
Indicates the type of channel interface being used to initiate the transaction. Possible values:
- app
- browser
- 3DSRequestorInitiated(initiated by a merchant when the cardholder is not available)
Universally unique transaction identifier assigned by the DS (card scheme) to identify a single transaction.
Indicates the exemption type that was applied to the authentication by the issuer, if exemption applied. Possible values:
- lowValue
- secureCorporate
- trustedBeneficiary
- transactionRiskAnalysis
- acquirerExemption
- noExemptionApplied
- visaDAFExemption
Indicates if the purchase was in the PSD2 scope.
Identifies the category of the message for a specific use case. Possible values:
- payment
- nonPayment
ThemessageVersionvalue as defined in the 3D Secure 2 specification.
Risk score calculated from the transaction rules.
ThethreeDSServerTransIDvalue as defined in the 3D Secure 2 specification.
ThetransStatusvalue as defined in the 3D Secure 2 specification. Possible values:
- Y: Authentication / Account verification successful.
- N: Not Authenticated / Account not verified. Transaction denied.
- U: Authentication / Account verification could not be performed.
- I: Informational Only / 3D Secure Requestor challenge preference acknowledged.
- R: Authentication / Account verification rejected by the Issuer.
Provides information on why thetransStatusfield has the specified value. For possible values, refer toour docs.
The type of authentication performed. Possible values:
- frictionless
- challenge
The unique identifier of the balance platform.
The unique identifier of the authentication.
The unique identifier of the payment instrument that was used for the authentication.
Contains information about the purchase.
The date of the purchase.
The name of the business that the cardholder purchased from.
The amount of the purchase.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
Outcome of the authentication.
Allowed values:
- authenticated
- rejected
- error
The environment from which the webhook originated.
Possible values:test,live.
When the event was queued.
Type of notification.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringRespond with any2xxHTTP status code toaccept the webhook.

#### 200 - OK