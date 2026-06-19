# Checkout/71/delete/storedPaymentMethods/(storedPaymentMethodId)

*Source: https://docs.adyen.com/api-explorer/Checkout/71/delete/storedPaymentMethods/(storedPaymentMethodId)*

---

# Delete a token for stored payment details
Deletes the token identified in the path. The token can no longer be used with payment requests.
Your merchant account.
Your reference to uniquely identify this shopper, for example user ID or account ID. Minimum length: 3 characters.
Your reference must not include personally identifiable information (PII), for example name or email address.
The unique identifier of the token.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 204 - No ContentLook at the actual response code for the status of the request.

#### 204 - No Content