# Notification/6/post/ACCOUNT_CREATED

*Source: https://docs.adyen.com/api-explorer/Notification/6/post/ACCOUNT_CREATED*

---

# Account created
Adyen sends this webhook whenan account is created.
The details of the account creation.
The code of the new account.
The code of the account holder.
The bankAccountUUID of the bank account held by the account holder to couple the account with. Scheduled payouts in currencies matching the currency of this bank account will be sent to this bank account. Payouts in different currencies will be sent to a matching bank account of the account holder.
The description of the account.
A list of fields that caused the/createAccountrequest to fail.
The validation error code.
A description of the validation error.
The type of error field.
The full name of the property.
The type of the field.
The code of the shareholder that the field belongs to. If empty, the field belongs to an account holder.
A set of key and value pairs containing metadata.
The payout method code held by the account holder to couple the account with. Scheduled card payouts will be sent using this payout method code.
The details of the payout schedule added to the account.
The date of the next scheduled payout.
The payout schedule for the account.
Possible values:DEFAULT,DAILY,DAILY_US,DAILY_EU,DAILY_AU,DAILY_SG,WEEKLY,WEEKLY_ON_TUE_FRI_MIDNIGHT,BIWEEKLY_ON_1ST_AND_15TH_AT_MIDNIGHT,MONTHLY,HOLD.
HOLDprevents scheduled payouts, but you can still initiate payouts manually.
Speed with which payouts for this account are processed. Permitted values:STANDARD,SAME_DAY.
The reference of a request. Can be used to uniquely identify the request.
The result code.
The status of the account.
Permitted values:Active.
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