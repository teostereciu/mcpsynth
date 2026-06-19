# Notification/6/post/PAYMENT_FAILURE

*Source: https://docs.adyen.com/api-explorer/Notification/6/post/PAYMENT_FAILURE*

---

# Booking for a capture or refund failed
Adyen sends this notification when asplit paymentbooking for a capture or refund fails. When a booking fails due to an invalid account status or an unknownaccountCode, the funds are credited or debited to or fromyour platform's liable account instead of the account specified in the split data.
The details of the payment failure.
Missing or invalid fields that caused the payment error.
The validation error code.
A description of the validation error.
The type of error field.
The full name of the property.
The type of the field.
The code of the shareholder that the field belongs to. If empty, the field belongs to an account holder.
The error message.
The message code.
The message text.
Thereferenceof the capture or refund.
ThepspReferenceof the capture or refund.
Thereferenceof the payment.
ThepspReferenceof the payment.
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