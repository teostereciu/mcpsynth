# Recurring/68/post/notifyShopper

*Source: https://docs.adyen.com/api-explorer/Recurring/68/post/notifyShopper*

---

# Ask issuer to notify the shopper
Sends a request to the issuer so they can inform the shopper about the upcoming recurring payment. This endpoint is used only for local acquiring in India. For more information, refer toRecurring card payments in India.
The amount of the upcoming payment.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
Date on which the subscription amount will be debited from the shopper. In YYYY-MM-DD format
Sequence of the debit. Depends on Frequency and Billing Attempts Rule.
Reference of Pre-debit notification that is displayed to the shopper. Optional field. Maps to reference if missing
The merchant account identifier with which you want to process the transaction.
This is therecurringDetailReferencereturned in the response when you created the token.
Pre-debit notification reference sent by the merchant. This is a mandatory field
The ID that uniquely identifies the shopper.
ThisshopperReferencemust be the same as theshopperReferenceused in the initial payment.
This is therecurringDetailReferencereturned in the response when you created the token.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessdisplayedReferencestringReference of Pre-debit notification that is displayed to the shoppermessagestringA simple description of theresultCode.pspReferencestringThe unique reference that is associated with the request.referencestringReference of Pre-debit notification sent in my the merchantresultCodestringThe code indicating the status of notification.shopperNotificationReferencestringThe unique reference for the request sent downstream.storedPaymentMethodIdstringThis is the recurringDetailReference returned in the response when token was created
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessadditionalDataobjectContains additional information about the payment. Some data fields are included only if you select them first. Go toCustomer Area>Developers>Additional data.errorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error