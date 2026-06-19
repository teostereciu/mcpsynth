# Management/3/post/companies/(companyId)/webhooks/(webhookId)/test

*Source: https://docs.adyen.com/api-explorer/Management/3/post/companies/(companyId)/webhooks/(webhookId)/test*

---

# Test a webhook
Sends sample notifications to test if the webhook is set up correctly.
We send sample notifications for maximum 20 of the merchant accounts that the webhook is configured for. If the webhook is configured for more than 20 merchant accounts, use themerchantIdsarray to specify a subset of the merchant accounts for which to send test notifications.
We send four test notifications for each event code you choose. They cover success and failure scenarios for the hard-coded currencies EUR and GBP, regardless of the currencies configured in the merchant accounts. For custom notifications, we only send the specified custom notification.
The response describes the result of the test. Thestatusfield tells you if the test was successful or not. You can use the other response fields to troubleshoot unsuccessful tests.
To make this request, your API credential must have the followingroles:
- Management API—Webhooks read and write
Unique identifier of the webhook configuration.
The unique identifier of the company account.
List ofmerchantIdvalues for which test webhooks will be sent. The list can have a maximum of 20merchantIdvalues.
If not specified, we send sample notifications to all the merchant accounts that the webhook is configured for. If this is more than 20 merchant accounts, use this list to specify a subset of the merchant accounts for which to send test notifications.
Custom test notification object. Required when thetypeslist containsCUSTOM.
The amount of the payment that the notification is about. Set the value inminor units.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The event that caused the notification to be sent.Currently supported values:
- AUTHORISATION
- CANCELLATION
- REFUND
- CAPTURE
- REPORT_AVAILABLE
- CHARGEBACK
- REQUEST_FOR_INFORMATION
- NOTIFICATION_OF_CHARGEBACK
- NOTIFICATIONTEST
- ORDER_OPENED
- ORDER_CLOSED
- CHARGEBACK_REVERSED
- REFUNDED_REVERSED
- REFUND_WITH_DATA
The time of the event. Format:ISO 8601, YYYY-MM-DDThh:mm:ssTZD.
Your reference for the custom test notification.
The payment method for the payment that the notification is about. Possible values:
- amex
- visa
- mc
- maestro
- bcmc
- paypal
- sms
- bankTransfer_NL
- bankTransfer_DE
- bankTransfer_BE
- ideal
- elv
- sepadirectdebit
A description of what caused the notification.
The outcome of the event which the notification is about. Set to eithertrueorfalse.
List of event codes for which to send test notifications. Only the webhook types below are supported.
Possible values if webhooktype:standard:
- AUTHORISATION
- CHARGEBACK_REVERSED
- ORDER_CLOSED
- ORDER_OPENED
- PAIDOUT_REVERSED
- PAYOUT_THIRDPARTY
- REFUNDED_REVERSED
- REFUND_WITH_DATA
- REPORT_AVAILABLE
- CUSTOM- set your custom notification fields in thenotificationobject.

```
notification
```
Possible values if webhooktype:banktransfer-notification:
- PENDING
Possible values if webhooktype:report-notification:
- REPORT_AVAILABLE
Possible values if webhooktype:ideal-notification:
- AUTHORISATION
Possible values if webhooktype:pending-notification:
- PENDING
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessdataarray[object]List with test results. Each test webhook we send has a list element with the result.Show childrenHide childrenmerchantIdstringUnique identifier of the merchant account that the notification is about.outputstringA short, human-readable explanation of the test result.Your server must respond with *HTTP 2xxfor the test webhook to be successful (data.status:success). Find out more aboutaccepting notificationsYou can use the value of this field together with theresponseCodevalue to troubleshoot unsuccessful test webhooks.requestSentstringThebody of the notification webhookthat was sent to your server.responseCodestringThe HTTP response code for your server's response to the test webhook.You can use the value of this field together with the theoutputfield value to troubleshoot failed test webhooks.responseTimestringThe time between sending the test webhook and receiving the response from your server. You can use it as an indication of how long your server takes to process a webhook notification. Measured in milliseconds, for example304 ms.statusstringThe status of the test request. Possible values are:success,data.responseCode:2xx.failed, in all other cases.You can use the value of theoutputfield together with theresponseCodevalue to troubleshoot failed test webhooks.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 401 - UnauthorizedAuthentication required.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.

#### 200 - OK

```
responseCode
```
- success,data.responseCode:2xx.
- failed, in all other cases.

```
responseCode
```

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error