# Notification/6/post/BENEFICIARY_SETUP

*Source: https://docs.adyen.com/api-explorer/Notification/6/post/BENEFICIARY_SETUP*

---

# Beneficiary defined
Adyen sends this notification when abenefactor/beneficiary relationship is created.
Details of the beneficiary setup.
The code of the beneficiary account.
The code of the beneficiary Account Holder.
A listing of the invalid fields which have caused the Setup Beneficiary request to fail. If this is empty, the Setup Beneficiary request has succeeded.
The validation error code.
A description of the validation error.
The type of error field.
The full name of the property.
The type of the field.
The code of the shareholder that the field belongs to. If empty, the field belongs to an account holder.
The reference provided by the merchant.
The code of the benefactor account.
The code of the benefactor Account Holder.
The date on which the beneficiary was set up and funds transferred from benefactor to beneficiary.
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