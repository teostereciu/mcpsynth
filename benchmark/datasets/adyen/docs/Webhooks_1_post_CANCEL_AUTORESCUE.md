# Webhooks/1/post/CANCEL_AUTORESCUE

*Source: https://docs.adyen.com/api-explorer/Webhooks/1/post/CANCEL_AUTORESCUE*

---

# Auto Rescue process canceled
TheAuto Rescue processwas canceled.
Informs about the origin of the notification. The value istruewhen originating from the live environment,falsefor the test environment.
A container object for the details included in the notification.
This object is a generic container that can hold extra fields.
The payment amount. For HTTP POST notifications, currency and value are returned as URL parameters.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The type of event the notification item is for.
The time when the event was generated. Format: ISO 8601; yyyy-MM-DDThh:mm:ssTZD
The merchant account identifier used in the transaction the notification item is for.
Your reference to uniquely identify the payment.
For modifications, this field corresponds to the payment request assigned to the original payment.
The payment method used in the transaction.
Adyen's 16-character unique reference associated with the transaction or request. This value is globally unique. Use it when communicating with us about this request.
Ifsuccess=false, then this includes a short message with an explanation for the refusal.
Informs about the outcome of the event (eventCode) the notification is for.
Iftrue: the event was executed successfully.
Iffalse: the event was not executed successfully.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - No ContentWebhook events are accepted on the basis of the HTTP status code.

#### 200 - No Content