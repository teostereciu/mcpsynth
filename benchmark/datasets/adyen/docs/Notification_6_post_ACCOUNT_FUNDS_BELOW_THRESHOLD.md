# Notification/6/post/ACCOUNT_FUNDS_BELOW_THRESHOLD

*Source: https://docs.adyen.com/api-explorer/Notification/6/post/ACCOUNT_FUNDS_BELOW_THRESHOLD*

---

# Liable account's funds are below configured threshold
Adyen sends this notification when the current funds of your liable account are below the configured threshold.
Details of the liable account with funds under threshold.
The code of the account with funds under threshold
The date of the funds were found to be below threshold.
The current funds in the liable account.
The three-characterISO currency code.
The amount of the transaction, inminor units.
The configured fund threshold for the liable account
The three-characterISO currency code.
The amount of the transaction, inminor units.
The code of the merchant account.
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