# ManagementNotification/3/post/paymentMethod.created

*Source: https://docs.adyen.com/api-explorer/ManagementNotification/3/post/paymentMethod.created*

---

# Payment method created
A request toadd a payment methodwas completed.
Timestamp for when the webhook was created.
Contains event details.
Indicates whether receiving payments is allowed. This value is set totrueby Adyen after screening your merchant account.
Indicates whether the payment method is enabled (true) or disabled (false).
The unique identifier of the resource.
The unique identifier of the merchant account.
Your reference for the payment method.
The status of the request to add a payment method. Possible values:
- success: the payment method was added.
- failure: the request failed.
- capabilityPending: thereceivePaymentscapability is not allowed.
The unique identifier of thestore, if any.
Payment methodvariant.
Payment method status. Possible values:
- valid
- pending
- invalid
- rejected
The environment from which the webhook originated.
Possible values:test,live.
Type of notification.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringRespond with any2xxHTTP status code toaccept the webhook.

#### 200 - OK