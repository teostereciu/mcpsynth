# Webhooks/1/post/AUTHORISATION

*Source: https://docs.adyen.com/api-explorer/Webhooks/1/post/AUTHORISATION*

---

# Result of authorisation request
The result of theauthorisation request.
Informs about the origin of the notification. The value istruewhen originating from the live environment,falsefor the test environment.
A container object for the details included in the notification.
This object is a generic container that can hold extra fields.
A GoPay shopper's wallet ID. Used by merchant for Risk and Fraud checks.
The acquirer account code.
The acquirer code.
The acquirer reference.
Information related to airlines.
Alias for this card.
Alias type.
Shopper device application info in a dynamic format.
Acquirer Reference Number of the dispute.
3DS authentication type
Authorisation MID of the acquirer.
The currency authorised for a dynamic zero auth request.
The amount authorised for a dynamic zero auth request.
Address Verification Service result.
Address Verification Service result raw.
The bank account number.
The bank location.
The bank location ID.
The bank name.
The bank verification result.
The bank verification result raw.
Business Identifier Code.
Browser code.
The amount of delay after authorisation.
The merchant reference of the capture.
The PSP reference of the capture.
Card Bank Identification number.
Card issuing bank.
Card issuing country.
Card issuing currency.
Card payment method.
The card product identifier for the card used in the transaction.
Card scheme enhanced data level.
Card summary
Secure Cardholder Authentication Verification Value.
CAVV algorithm.
Information about the 3DS challenge being canceled.
Card Verification Code result.
Card Verification Code result raw.
Delivery address: postal code.
Type of device the request was made from.
Direct debit GB: date of signature.
Direct debit GB: mandate ID.
Direct debit GB: sequence type.
Direct debit GB: service user name.
Direct debit GB: service user number.
3DS: Electronic Commerce Indicator.
Expiry date of the card.
Additional cost used inBIN or card verification.
Related additional cost value.
Gratuity related additional cost value.
Surcharge related additional cost value.
Information on the fraud check in a dynamic format.
Indicates if the risk check was done manually.
The fraud offset.
Result type of the fraud check.
The risk level of the transaction as classified by themachine learningfraud risk rule. The risk level indicates the likelihood that a transaction will result in a fraudulent dispute. Possible values:
- veryLow
- low
- medium
- high
- veryHigh
Funding source.
Chargeback gross currency.
Chargeback gross value.
Only included for iDeal payments.
Only included for iDeal payments.
Only included for iDeal payments.
Only included for iDeal payments.
Only included for iDeal payments.
Only included for iDeal payments.
Only included for iDeal payments.
International Bank Account Number.
3DS interaction counter.
Indicates if the card is used for business purposes only.
Card holder name.
Country of the card issuer.
Risk liability shift.
A set of key-value pairs provided in the request, prefixed with 'metadata.'. For example, 'metadata.myField: myValue'
NFC related.
NFC related.
NFC related.
NFC related.
The transaction token to be used in your Oracle Opera integration.
Owner city.
Owner name.
Related to PayU in LATAM.
ID of the Checkout payment link.
Related to PayPal.
Related to PayPal.
The buyer's PayPal account email address.
Example: paypaltest@adyen.com
Related to PayPal.
Related to PayPal.
Related to PayPal.
The buyer's PayPal ID.
Example: LF5HCWWBRV2KL
The buyer's country of residence.
Example: NL
The status of the buyer's PayPal account.
Example: unverified
Related to PayPal.
The eligibility for PayPal Seller Protection for this payment.
Example: Ineligible
Related to PayPal.
Real time Account Update status.
The new tokenization.storedPaymentMethodId field replaces this field.
TherecurringDetailReferencereturned in the/paymentsresponse when you stored the shopper's payment details.
The new tokenization.shopperReferencefield replaces this field.
The shopper reference you set when you made the request to store the shopper's payment details.
The recurring processing model the request was flagged with.
If the payment is referred, this field is set to true.
This field is unavailable if the payment is referred and is usually not returned with ecommerce transactions.
Example: true
Raw refusal reason received from the acquirer, where available.
Example: AUTHORISED
Indicates if an auto rescue for a payment is scheduled.
Related to Risk.
Related to Risk.
Risk data in a dynamic format.
Country of the shopper.
Email of the shopper.
IP of the shopper.
The shopper interaction type of the payment request.
Example: Ecommerce
The locale of the shopper.
The social security number of the shopper.
The text to be shown on the shopper's bank statement.
The telephone number of the shopper.
Identifier of the store processing the transaction.
A Swish shopper's telephone number.
Tender reference. For point-of-sale integrations only.
Terminal ID. For point-of-sale integrations only.
A Boolean value indicating whether 3DS authentication was completed on this payment.
Example: true
The raw 3DS authentication result from the card issuer.
Example: N
A Boolean value indicating whether 3DS was offered for this payment.
Example: true
The raw enrollment result from the 3DS directory services of the card schemes.
Example: Y
The 3D Secure 2 version.
Payment method variant of the token/wallet payment method.
The reference for the shopper that you sent when tokenizing the payment details.
The operation performed on the token. Possible values:
- created: the token has been created.
- updated: the existing token has been updated.
- alreadyExisting: the details have already been stored.
The reference that uniquely identifies tokenized payment details.
Total fraud score from risk.
Card summary without tokenization.
The 3DS transaction ID of the 3DS session sent in notifications. The value is Base64-encoded and is returned for transactions with directoryResponse 'N' or 'Y'.
Example: ODgxNDc2MDg2MDExODk5MAAAAAA=
The payment amount. For HTTP POST notifications, currency and value are returned as URL parameters.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The type of event the notification item is for.
The time when the event was generated. Format: ISO 8601; yyyy-MM-DDThh:mm:ssTZD
The merchant account identifier used in the transaction the notification item is for.
Your reference to uniquely identify the payment.
The operations indicate the supported follow-up actions concerning the payment.
This is anexperimental field. Do not base your code on this field. Not all specific cases are covered yet. It's possible that the field is empty or contains generic information.
The payment method used in the transaction.
Adyen's 16-character unique reference associated with the transaction or request. This value is globally unique. Use it when communicating with us about this request.
Ifsuccess=trueandpaymentMethod=visa,mc, oramexthen this field contains the following details:
Authorisation code, last 4 digits of the card, card expiry date.
In case of failure, this contains information about the authorisation failure
Iftrue: The payment request was successful.
Iffalse: The payment request failed.
Check thereasonfield for failure information.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - No ContentWebhook events are accepted on the basis of the HTTP status code.

#### 200 - No Content