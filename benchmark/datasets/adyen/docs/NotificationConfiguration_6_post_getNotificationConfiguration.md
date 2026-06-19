# NotificationConfiguration/6/post/getNotificationConfiguration

*Source: https://docs.adyen.com/api-explorer/NotificationConfiguration/6/post/getNotificationConfiguration*

---

# Get a notification subscription configuration
Returns the details of the configuration of a notification subscription.
The ID of the notification subscription configuration whose details are to be retrieved.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessconfigurationDetailsobjectDetails of the notification subscription configuration.Show childrenHide childrenactivebooleanIndicates whether the notification subscription is active.apiVersionintegerThe version of the notification to which you are subscribing. To make sure that your integration can properly process the notification, subscribe to the same version as the API that you're using.descriptionstringA description of the notification subscription configuration.eventConfigsarray[object]Contains objects that define event types and their subscription settings.Show childrenHide childreneventTypestringThe type of event.Possible values:ACCOUNT_CLOSED,ACCOUNT_CREATED,ACCOUNT_FUNDS_BELOW_THRESHOLD,ACCOUNT_HOLDER_CREATED,ACCOUNT_HOLDER_LIMIT_REACHED,ACCOUNT_HOLDER_PAYOUT,ACCOUNT_HOLDER_STATUS_CHANGE,ACCOUNT_HOLDER_STORE_STATUS_CHANGE,ACCOUNT_HOLDER_UPCOMING_DEADLINE,ACCOUNT_HOLDER_UPDATED,ACCOUNT_HOLDER_VERIFICATION,ACCOUNT_UPDATED,BENEFICIARY_SETUP,COMPENSATE_NEGATIVE_BALANCE,DIRECT_DEBIT_INITIATED,PAYMENT_FAILURE,REFUND_FUNDS_TRANSFER,REPORT_AVAILABLE,SCHEDULED_REFUNDS,TRANSFER_FUNDS.includeModestringIndicates whether the specifiedeventTypeis sent to your webhook endpoint.
Possible values:INCLUDE: Send the specifiedeventType.EXCLUDE: Send all event types except the specifiedeventTypeand other event types with theincludeModeset toEXCLUDE.hmacSignatureKeystringA string with which to salt the notification(s) before hashing. If this field is provided, a hash value will be included under the notification headerHmacSignatureand the hash protocol will be included under the notification headerProtocol. A notification body along with itshmacSignatureKeyandProtocolcan be used to calculate a hash value; matching this hash value with theHmacSignaturewill ensure that the notification body has not been tampered with or corrupted.Must be a 32-byte hex-encoded string (i.e. a string containing 64 hexadecimal characters; e.g. "b0ea55c2fe60d4d1d605e9c385e0e7f7e6cafbb939ce07010f31a327a0871f27").The omission of this field will preclude the provision of theHmacSignatureandProtocolheaders in notification(s).notificationIdintegerAdyen-generated ID for the entry, returned in the response when you create a notification configuration. Required when updating an existing configuration using/updateNotificationConfiguration.notifyPasswordstringThe password to use when accessing the notifyURL with the specified username.notifyURLstringThe URL to which the notifications are to be sent.notifyUsernamestringThe username to use when accessing the notifyURL.sslProtocolstringThe SSL protocol employed by the endpoint.Permitted values:TLSv12,TLSv13.invalidFieldsarray[object]Contains field validation errors that would prevent requests from being processed.Show childrenHide childrenerrorCodeintegerThe validation error code.errorDescriptionstringA description of the validation error.fieldTypeobjectThe type of error field.Show childrenHide childrenfieldstringThe full name of the property.fieldNamestringThe type of the field.shareholderCodestringThe code of the shareholder that the field belongs to. If empty, the field belongs to an account holder.pspReferencestringThe reference of a request. Can be used to uniquely identify the request.resultCodestringThe result code.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK
- INCLUDE: Send the specifiedeventType.
- EXCLUDE: Send all event types except the specifiedeventTypeand other event types with theincludeModeset toEXCLUDE.

```
/updateNotificationConfiguration
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error