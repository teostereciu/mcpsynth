# balanceplatform-webhooks/2/overview

*Source: https://docs.adyen.com/api-explorer/balanceplatform-webhooks/2/overview*

---

# Configuration webhooks
Adyen sends webhooks to inform your system about events that occur in your platform. These events include, for example, when an account holder's capabilities are updated, or when a sweep configuration is created or updated.
When an event occurs, Adyen makes an HTTP POST request to a URL on your server and includes the details of the event in the request body.
You can use these webhooks to build your implementation. For example, you can use this information to update internal statuses when the status of a capability is changed.