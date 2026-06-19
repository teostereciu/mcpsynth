# Notification/6/post/ACCOUNT_CLOSED

*Source: https://docs.adyen.com/api-explorer/Notification/6/post/ACCOUNT_CLOSED*

---

# Account closed
Adyen sends this webhook whenan account is closed.
The details of the Account update.
The account code of the account that is closed.
Contains field validation errors that would prevent requests from being processed.
The validation error code.
A description of the validation error.
The type of error field.
The full name of the property.
The type of the field.
The code of the shareholder that the field belongs to. If empty, the field belongs to an account holder.
The reference of a request. Can be used to uniquely identify the request.
The result code.
The new status of the account.
Permitted values:Active,Inactive,Suspended,Closed.
Error information of failed request. No value provided here if no error occurred on processing.
The Adyen code that is mapped to the error message.
A short explanation of the issue.
The date and time when an event has been completed.
The event type of the notification.
The user or process that has triggered the notification.
Indicates whether the notification originated from the live environment or the test environment. If true, the notification originated from the live environment. If false, the notification originated from the test environment.
The PSP reference of the request from which the notification originates.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringSet this parameter to[accepted]to acknowledge that you received a notification from Adyen.

#### 200 - OK