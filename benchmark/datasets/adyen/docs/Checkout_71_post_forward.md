# Checkout/71/post/forward

*Source: https://docs.adyen.com/api-explorer/Checkout/71/post/forward*

---

# Forward stored payment details
Forwards the payment details you stored with Adyen to a third-party that you specify and returns the response from the third-party. Supports forwarding stored card details ornetwork tokens. For more information, seeForward stored payment details.
A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
The amount of the forwarded payment.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The base URL of the third party API, where Adyen will send the request to forward the payment details.
Your merchant account.
Merchant defined payment reference.
The customizations that can be applied when making a forward request.
Whether to check for a card account update (true) or not (false)
Set totrueto receive a copy of the request Adyen is making to the third party in the response. Any sensitive information will be masked in the response you receive. This functionality is only available in the test environment.
The object that contains the details for forwarding a network token.
Set totrueto enable forwarding network token cryptograms.
Set totrueto forward the network token for a card.
Set in tokenize:true case when forwarding PAN. Addresses to the possible location(s) of networkTxReference in the incoming 3rd party response
Set totrue, the payment details aretokenized.
The card details.
Thecard verification code(1-20 characters). Depending on the card brand, it is also known as:
- CVV2/CVC2 – length: 3 digits
- CID – length: 4 digits
The encrypted card number.
The encrypted expiryMonth
The encrypted card expiry year.
The encrypted security code.
The card expiry month.
Format: 2 digits, zero-padded for single digits. For example:
- 03 = March
- 11 = November
The card expiry year.
The name of the cardholder.
The card number. Only collect raw card data if you are fullyPCI compliant.
Format: Do not use separators.
Default payment method details. Common for scheme payment methods, and for simple payment method details.
Thedetails of the requestthat you want to forward to the third-party.
The request body that you want Adyen to forward to the third party on your behalf, in string format.
Include key value pairs to specify the payment details, and useplaceholdersfor the values. Adyen replaces the placeholders with the payment details when making the request to the third party.
When forwarding a network token, include aconditionthat checks if the network token exists, and informs Adyen of which fields to send depending on the outcome.
Your credentials that are needed to authenticate with the third party.
The request headers that will be included in the request Adyen makes to the third party on your behalf. Supports the{{credentials}}placeholder.
The HTTP method to use for the request Adyen makes on your behalf to the third party.
The suffix that Adyen needs to append to thebaseUrlto construct the destination URL that belongs to the third party. This is usually the endpoint name for the request, for example,/payments.
Your reference to uniquely identify this shopper, for example user ID or account ID. The value is case-sensitive and must be at least three characters.
Your reference must not include personally identifiable information (PII) such as name or email address.
The unique identifier of the token that you want to forward to the third party. This is thestoredPaymentMethodIdyou received in the webhook after you created the token.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessmerchantReferencestringMerchant defined payment reference.pspReferencestringAdyen's 16-character reference associated with the transaction/request. This value is globally unique. Use this reference when you communicate with us about this request.responseobjectThe details of the response Adyen received from the third party.Show childrenHide childrenbodystringThe body of the response Adyen received from the third party, in string format.headersobjectThe HTTP headers of the response Adyen received from the third party.statusintegerThe HTTP status of the response Adyen received from the third party.storedPaymentMethodIdstringThe unique identifier of the token.

#### 200 - OK