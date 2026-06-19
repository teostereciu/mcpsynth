# Notification/6/post/TRANSFER_FUNDS

*Source: https://docs.adyen.com/api-explorer/Notification/6/post/TRANSFER_FUNDS*

---

# Funds transferred between accounts
Adyen sends this notification whenfunds are transferred between accounts.
Details of the fund transfer.
The amount transferred.
The three-characterISO currency code.
The amount of the transaction, inminor units.
The code of the Account to which funds were credited.
Invalid fields list.
The validation error code.
A description of the validation error.
The type of error field.
The full name of the property.
The type of the field.
The code of the shareholder that the field belongs to. If empty, the field belongs to an account holder.
The reference provided by the merchant.
The code of the Account from which funds were debited.
The status of the fund transfer.
The message regarding the operation status.
The message code.
The message text.
The status code.
The transfer code.
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