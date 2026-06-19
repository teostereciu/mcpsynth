# NotificationConfiguration/6/post/testNotificationConfiguration

*Source: https://docs.adyen.com/api-explorer/NotificationConfiguration/6/post/testNotificationConfiguration*

---

# Test a notification configuration
Tests an existing notification subscription configuration. For each event type specified, a test notification will be generated and sent to the URL configured in the subscription specified.
The event types to test.  If left blank, then all of the configured event types will be tested.
Permitted values:ACCOUNT_HOLDER_CREATED,ACCOUNT_CREATED,ACCOUNT_UPDATED,ACCOUNT_HOLDER_UPDATED,ACCOUNT_HOLDER_STATUS_CHANGE,ACCOUNT_HOLDER_STORE_STATUS_CHANGEACCOUNT_HOLDER_VERIFICATION,ACCOUNT_HOLDER_LIMIT_REACHED,ACCOUNT_HOLDER_PAYOUT,PAYMENT_FAILURE,SCHEDULED_REFUNDS,REPORT_AVAILABLE,TRANSFER_FUNDS,BENEFICIARY_SETUP,COMPENSATE_NEGATIVE_BALANCE.
The ID of the notification subscription configuration to be tested.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lesserrorMessagesarray[string]Any error messages encountered.eventTypesarray[string]The event types that were tested.Permitted values:ACCOUNT_HOLDER_CREATED,ACCOUNT_CREATED,ACCOUNT_UPDATED,ACCOUNT_HOLDER_UPDATED,ACCOUNT_HOLDER_STATUS_CHANGE,ACCOUNT_HOLDER_STORE_STATUS_CHANGEACCOUNT_HOLDER_VERIFICATION,ACCOUNT_HOLDER_LIMIT_REACHED,ACCOUNT_HOLDER_PAYOUT,PAYMENT_FAILURE,SCHEDULED_REFUNDS,REPORT_AVAILABLE,TRANSFER_FUNDS,BENEFICIARY_SETUP,COMPENSATE_NEGATIVE_BALANCE.exchangeMessagesarray[object]The notification message and related response messages.Show childrenHide childrenmessageCodestringmessageDescriptionstringinvalidFieldsarray[object]Contains field validation errors that would prevent requests from being processed.Show childrenHide childrenerrorCodeintegerThe validation error code.errorDescriptionstringA description of the validation error.fieldTypeobjectThe type of error field.Show childrenHide childrenfieldstringThe full name of the property.fieldNamestringThe type of the field.shareholderCodestringThe code of the shareholder that the field belongs to. If empty, the field belongs to an account holder.notificationIdintegerThe ID of the notification subscription configuration.okMessagesarray[string]A list of messages describing the testing steps.pspReferencestringThe reference of a request. Can be used to uniquely identify the request.resultCodestringThe result code.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error