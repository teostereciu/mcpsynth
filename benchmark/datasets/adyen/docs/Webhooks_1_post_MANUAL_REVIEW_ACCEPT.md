# Webhooks/1/post/MANUAL_REVIEW_ACCEPT

*Source: https://docs.adyen.com/api-explorer/Webhooks/1/post/MANUAL_REVIEW_ACCEPT*

---

# Manual review accepted
Themanual reviewwas accepted.
Informs about the origin of the notification. The value istruewhen originating from the live environment,falsefor the test environment.
A container object for the details included in the notification.
A generic container for extra fields.
Reference of the payment account.
The acquirer account code.
The acquirer code.
The acquirer reference.
ACS interface. Related to 3DS.
ACS UI template.
Alias for this card.
Alias type.
Acquirer Reference Number of the dispute.
Authcode of the scheme.
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
BillingAddress: county.
BillingAddress: house number or name.
BillingAddress: postal code.
BillingAddress: state or province
BillingAddress: street
Browser code.
The amount of delay after authorisation.
The merchant reference of the capture.
The PSP reference of the capture.
Card Bank Identification number.
Card issuing bank.
Card issuing country.
Card issuing currency.
Card payment method.
Card scheme enhanced data level.
Card summary
Secure Cardholder Authentication Verification Value.
CAVV algorithm.
Information about the 3DS challenge being canceled.
ID of the Checkout Session.
Card Verification Code result.
Card Verification Code result raw.
Delivery address: city.
Delivery address: country.
Delivery address: house number or name.
Delivery address: postal code.
Delivery address: state or province.
Delivery address: street.
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
International Bank Account Number.
The number of installments that the payment amount should be charged with.
Example: 5
Only relevant for card payments in countries that support installments.
3DS interaction counter.
Card holder name.
Country of the card issuer.
Recurring: Latest card BIN.
Recurring: Latest card expiry date.
Recurring: Latest card summary.
Risk liability shift.
A set of key-value pairs provided in the request, prefixed with 'metadata.'. For example, 'metadata.myField: myValue'
Recurring related.
Recurring related.
Recurring related.
NFC related.
NFC related.
NFC related.
NFC related.
Trans token related to Oracle Opera.
Owner city.
Owner name.
Related to PayU in LATAM.
ID of the Checkout payment link.
Real time Account Update status.
Recurring contract types.
Recurring first PSP reference.
Thetoken for stored payment detailsto make recurring payments.
If the payment is referred, this field is set to true.
This field is unavailable if the payment is referred and is usually not returned with ecommerce transactions.
Example: true
Raw refusal reason received from the acquirer, where available.
Example: AUTHORISED
Indicates if an auto rescue for a payment is scheduled.
Related to Risk.
Related to Risk.
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
For modifications, this field corresponds to the payment request assigned to the original payment.
The payment method used in the transaction.
Adyen's 16-character unique reference associated with the transaction or request. This value is globally unique. Use it when communicating with us about this request.
Ifsuccess=false, then this includes a short message with an explanation for the refusal.
Informs about the outcome of the event (eventCode) the notification is for.
Iftrue: the event was executed successfully.
Iffalse: the event was not executed successfully.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - No ContentWebhook events are accepted on the basis of the HTTP status code.

#### 200 - No Content