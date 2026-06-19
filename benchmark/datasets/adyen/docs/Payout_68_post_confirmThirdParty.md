# Payout/68/post/confirmThirdParty

*Source: https://docs.adyen.com/api-explorer/Payout/68/post/confirmThirdParty*

---

# Confirm a payout
This endpoint isdeprecatedand no longer supports new integrations. Do one of the following:
- If you are building a new integration, use theTransfers APIinstead.
- If you are already using the Payout API, reach out to your Adyen contact to learn how to migrate to the Transfers API.
With the Transfers API, you can:
- Handle multiple payout use cases with a single API.
- Use new payout functionalities, such as instant payouts to bank accounts.
- Receive webhooks with more details and defined transfer states.
For more information about the payout features of the Transfers API, see ourPayoutsdocumentation.
Confirms a previously submitted payout.
To cancel a payout, use the/declineThirdPartyendpoint.
This field contains additional data, which may be required for a particular payout request.
The merchant account identifier, with which you want to process the transaction.
The PSP reference received in the/submitThirdPartyresponse.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessadditionalDataobjectThis field contains additional data, which may be returned in a particular response.pspReferencestringAdyen's 16-character string reference associated with the transaction. This value is globally unique; quote it when communicating with us about this response.responsestringThe response:In case of success, it is eitherpayout-confirm-receivedorpayout-decline-received.In case of an error, an informational message is returned.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK
- In case of success, it is eitherpayout-confirm-receivedorpayout-decline-received.
- In case of an error, an informational message is returned.

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error