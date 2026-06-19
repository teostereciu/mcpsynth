# Notification/6/post/ACCOUNT_HOLDER_UPCOMING_DEADLINE

*Source: https://docs.adyen.com/api-explorer/Notification/6/post/ACCOUNT_HOLDER_UPCOMING_DEADLINE*

---

# Upcoming deadline
Adyen sends this notification when an account holder's deadline to fulfill the requirements of a specific event is coming up.
The details of the upcoming event.
The code of the account holder whom the event refers to.
The event name that will be trigger if no action is taken.
The execution date scheduled for the event.
The reason that leads to scheduling of the event.
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