# Notification/6/post/ACCOUNT_HOLDER_STATUS_CHANGE

*Source: https://docs.adyen.com/api-explorer/Notification/6/post/ACCOUNT_HOLDER_STATUS_CHANGE*

---

# Account holder status changed
Adyen sends this webhook whenthe status of an account holder is changed.
The details of the Account Holder status change.
The code of the account holder.
in case the account holder has not been updated, contains account holder fields, that did not pass the validation.
The validation error code.
A description of the validation error.
The type of error field.
The full name of the property.
The type of the field.
The code of the shareholder that the field belongs to. If empty, the field belongs to an account holder.
The new status of the account holder.
A list of events scheduled for the account holder.
The event.
Permitted values:InactivateAccount,RefundNotPaidOutTransfers.
For more information, refer toVerification checks.
The date on which the event will take place.
The reason why this event has been created.
The payout state of the account holder.
Indicates whether payouts are allowed. This field is the overarching payout status, and is the aggregate of multiple conditions (e.g., KYC status, disabled flag, etc). If this field is false, no payouts will be permitted for any of the account holder's accounts. If this field is true, payouts will be permitted for any of the account holder's accounts.
The reason why payouts (to all of the account holder's accounts) have been disabled (by the platform). If thedisabledfield is true, this field can be used to explain why.
Indicates whether payouts have been disabled (by the platform) for all of the account holder's accounts. A platform may enable and disable this field at their discretion. If this field is true,allowPayoutwill be false and no payouts will be permitted for any of the account holder's accounts. If this field is false,allowPayoutmay or may not be enabled, depending on other factors.
The reason why payouts (to all of the account holder's accounts) have been disabled (by Adyen). If payouts have been disabled by Adyen, this field will explain why. If this field is blank, payouts have not been disabled by Adyen.
The maximum amount that payouts are limited to. Only applies if payouts are allowed but limited.
The three-characterISO currency code.
The amount of the transaction, inminor units.
The payout tier that the account holder occupies.
The processing state of the account holder.
The reason why processing has been disabled.
Indicates whether the processing of payments is allowed.
The lower bound of the processing tier (i.e., an account holder must have processed at least this amount of money in order to be placed into this tier).
The three-characterISO currency code.
The amount of the transaction, inminor units.
The upper bound of the processing tier (i.e., an account holder must have processed less than this amount of money in order to be placed into this tier).
The three-characterISO currency code.
The amount of the transaction, inminor units.
The processing tier that the account holder occupies.
The status of the account holder.
Permitted values:Active,Inactive,Suspended,Closed.
The reason why the status was assigned to the account holder.
The former status of the account holder.
A list of events scheduled for the account holder.
The event.
Permitted values:InactivateAccount,RefundNotPaidOutTransfers.
For more information, refer toVerification checks.
The date on which the event will take place.
The reason why this event has been created.
The payout state of the account holder.
Indicates whether payouts are allowed. This field is the overarching payout status, and is the aggregate of multiple conditions (e.g., KYC status, disabled flag, etc). If this field is false, no payouts will be permitted for any of the account holder's accounts. If this field is true, payouts will be permitted for any of the account holder's accounts.
The reason why payouts (to all of the account holder's accounts) have been disabled (by the platform). If thedisabledfield is true, this field can be used to explain why.
Indicates whether payouts have been disabled (by the platform) for all of the account holder's accounts. A platform may enable and disable this field at their discretion. If this field is true,allowPayoutwill be false and no payouts will be permitted for any of the account holder's accounts. If this field is false,allowPayoutmay or may not be enabled, depending on other factors.
The reason why payouts (to all of the account holder's accounts) have been disabled (by Adyen). If payouts have been disabled by Adyen, this field will explain why. If this field is blank, payouts have not been disabled by Adyen.
The maximum amount that payouts are limited to. Only applies if payouts are allowed but limited.
The three-characterISO currency code.
The amount of the transaction, inminor units.
The payout tier that the account holder occupies.
The processing state of the account holder.
The reason why processing has been disabled.
Indicates whether the processing of payments is allowed.
The lower bound of the processing tier (i.e., an account holder must have processed at least this amount of money in order to be placed into this tier).
The three-characterISO currency code.
The amount of the transaction, inminor units.
The upper bound of the processing tier (i.e., an account holder must have processed less than this amount of money in order to be placed into this tier).
The three-characterISO currency code.
The amount of the transaction, inminor units.
The processing tier that the account holder occupies.
The status of the account holder.
Permitted values:Active,Inactive,Suspended,Closed.
The reason why the status was assigned to the account holder.
The reason for the status change.
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