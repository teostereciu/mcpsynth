# Notification/6/post/REPORT_AVAILABLE

*Source: https://docs.adyen.com/api-explorer/Notification/6/post/REPORT_AVAILABLE*

---

# Report available
Adyen sends this notification when a report has been generated and it is available for download.
Details of the report.
The code of the Account to which the report applies.
The type of Account to which the report applies.
The date of the event to which the report applies.
The URL at which the report can be accessed.
Indicates whether the event resulted in a success.
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