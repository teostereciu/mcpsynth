# ManagementNotification/3/post/terminalAssignment.completed

*Source: https://docs.adyen.com/api-explorer/ManagementNotification/3/post/terminalAssignment.completed*

---

# Terminal assignment completed
A request toreassign a terminalwas completed.
The unique identifier of the merchant/company account to which the terminal is assigned.
The store that the terminal is assigned to, identified by the store reference (also known as store code).
The unique identifier of the store to which the terminal is assigned.
The date and time when an event has been completed.
The PSP reference of the request from which the notification originates.
The unique identifier of the terminal.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringRespond with any2xxHTTP status code toaccept the webhook.

#### 200 - OK