# Webhooks/1/post/ACH_NOTIFICATION_OF_CHANGE

*Source: https://docs.adyen.com/api-explorer/Webhooks/1/post/ACH_NOTIFICATION_OF_CHANGE*

---

# ACH Notification of Change
An ACH Notification of Change was processed regarding changed bank account details.
Timestamp for when the webhook was created.
Contains details of the update.
The Notification of Change information.
New bank account number.
New bank account type.
Possible values:
- Savings
- Checking
New branch code.
Notification of Change reason code.
Possible values:
- C01: Incorrect bank account number.
- C02: Incorrect transit/routing number.
- C03: Incorrect transit/routing number and bank account number.
- C04: Bank account name change.
- C05: Incorrect payment code.
- C06: Incorrect bank account number and transit code.
- C07: Incorrect transit/routing number, bank account number and payment code.
- C09: Incorrect individual ID number.
- C10: Incorrect company name.
- C11: Incorrect company identification.
- C12: Incorrect company name and company ID.
PSP Reference.
Shopper reference.
The environment from which the webhook originated.
Possible values:test,live.
Type of notification.
The version of this webhook type.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - No ContentWebhook events are accepted on the basis of the HTTP status code.

#### 200 - No Content