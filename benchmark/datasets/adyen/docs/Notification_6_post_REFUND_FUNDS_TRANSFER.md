# Notification/6/post/REFUND_FUNDS_TRANSFER

*Source: https://docs.adyen.com/api-explorer/Notification/6/post/REFUND_FUNDS_TRANSFER*

---

# Funds transfer between accounts refunded
Adyen sends this notification whenfunds transferred between accounts are refunded.
Details of the fund transfer refund.
The amount to be refunded.
The three-characterISO currency code.
The amount of the transaction, inminor units.
Invalid fields list.
The validation error code.
A description of the validation error.
The type of error field.
The full name of the property.
The type of the field.
The code of the shareholder that the field belongs to. If empty, the field belongs to an account holder.
A value that can be supplied at the discretion of the executing user in order to link multiple transactions to one another.
A PSP reference of the original fund transfer.
The status of the fund transfer refund.
The message regarding the operation status.
The message code.
The message text.
The status code.
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