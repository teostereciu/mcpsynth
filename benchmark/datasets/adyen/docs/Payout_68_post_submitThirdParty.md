# Payout/68/post/submitThirdParty

*Source: https://docs.adyen.com/api-explorer/Payout/68/post/submitThirdParty*

---

# Submit a payout
This endpoint isdeprecatedand no longer supports new integrations. Do one of the following:
- If you are building a new integration, use the POST/transfersendpoint instead.
- If you are already using the Payout API, reach out to your Adyen contact to learn how to migrate to the Transfers API.
With the Transfers API, you can:
- Handle multiple payout use cases with a single API.
- Use new payout functionalities, such as instant payouts to bank accounts.
- Receive webhooks with more details and defined transfer states.
For more information about the payout features of the Transfers API, see ourPayoutsdocumentation.
Submits a payout using the previously stored payment details. To store payment details, use the/storeDetailAPI call.
The submitted payout must be confirmed or declined either by a reviewer or via/confirmThirdPartyor/declineThirdPartycalls.
This field contains additional data, which may be required for a particular request.
A container object for the payable amount information of the transaction.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The date of birth.
Format: ISO-8601; example: YYYY-MM-DD
For Paysafecard it must be the same as used when registering the Paysafecard account.
This field is mandatory for natural persons.
This field is required to update the existingdateOfBirththat is associated with this recurring contract.
The type of the entity the payout is processed for.
Allowed values:
- NaturalPerson
- Company
This field is required to update the existingentityTypethat is associated with this recurring contract.
An integer value that is added to the normal fraud score. The value can be either positive or negative.
The merchant account identifier you want to process the transaction request with.
The shopper's nationality.
A valid value is an ISO 2-character country code (e.g. 'NL').
This field is required to update the existing nationality that is associated with this recurring contract.
A container for the type of recurring contract to be retrieved.
Therecurring.contractmust be set to "PAYOUT".
The type of recurring contract to be used.
Possible values:
- ONECLICK– Payment details can be used to initiate a one-click payment, where the shopper enters thecard security code (CVC/CVV).
- RECURRING– Payment details can be used without the card security code to initiatecard-not-present transactions.
- ONECLICK,RECURRING– Payment details can be used regardless of whether the shopper is on your site or not.
- PAYOUT– Payment details can be used tomake a payout.
- EXTERNAL- Use this when you store payment details and send the raw card number or network token directly in your API request.
A descriptive name for this detail.
Date after which no further authorisations shall be performed. Only for 3D Secure 2.
Minimum number of days between authorisations. Only for 3D Secure 2.
The name of the token service.
The merchant reference for this payout. This reference will be used in all communication to the merchant about the status of the payout. Although it is a good idea to make sure it is unique, this is not a requirement.
This is therecurringDetailReferenceyou want to use for this payout.
You can use the value LATEST to select the most recently used recurring detail.
The shopper's email address.
The shopper's name.
In case theentityTypeisCompany, theshopperName.lastNamemust contain the company name.
This field is required to update the existingshopperNameassociated with a recurring contract.
The first name.
The last name.
The shopper's reference for the payout transaction.
The description of this payout. This description is shown on the bank statement of the shopper (if this is supported by the chosen payment method).
The shopper's social security number.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessadditionalDataobjectThis field contains additional data, which may be returned in a particular response.pspReferencestringA new reference to uniquely identify this request.refusalReasonstringIn case of refusal, an informational message for the reason.resultCodestringThe response:In case of success, it ispayout-submit-received.In case of an error, an informational message is returned.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK
- In case of success, it ispayout-submit-received.
- In case of an error, an informational message is returned.

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error