# Account/6/post/createAccount

*Source: https://docs.adyen.com/api-explorer/Account/6/post/createAccount*

---

# Create an account
Creates an account under an account holder. An account holder can havemultiple accounts.
The code of Account Holder under which to create the account.
The bankAccountUUID of the bank account held by the account holder to couple the account with. Scheduled payouts in currencies matching the currency of this bank account will be sent to this bank account. Payouts in different currencies will be sent to a matching bank account of the account holder.
A description of the account, maximum 256 characters. You can use alphanumeric characters (A-Z, a-z, 0-9), white spaces, and underscores_.
A set of key and value pairs for general use by the merchant.
The keys do not have specific names and may be used for storing miscellaneous data as desired.
Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of those key-value pairs.
The payout method code held by the account holder to couple the account with. Scheduled card payouts will be sent using this payout method code.
The payout schedule for the account.
Possible values:DEFAULT,DAILY,DAILY_US,DAILY_EU,DAILY_AU,DAILY_SG,WEEKLY,WEEKLY_ON_TUE_FRI_MIDNIGHT,BIWEEKLY_ON_1ST_AND_15TH_AT_MIDNIGHT,MONTHLY,HOLD.
HOLDprevents scheduled payouts, but you can still initiate payouts manually.
The reason for the payout schedule choice.
This field is required when thepayoutScheduleparameter is set toHOLD.
Speed at which payouts for this account are processed.
Possible values:STANDARD(default),SAME_DAY.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessaccountCodestringThe code of the new account.accountHolderCodestringThe code of the account holder.bankAccountUUIDstringThe bankAccountUUID of the bank account held by the account holder to couple the account with. Scheduled payouts in currencies matching the currency of this bank account will be sent to this bank account. Payouts in different currencies will be sent to a matching bank account of the account holder.descriptionstringThe description of the account.invalidFieldsarray[object]A list of fields that caused the/createAccountrequest to fail.Show childrenHide childrenerrorCodeintegerThe validation error code.errorDescriptionstringA description of the validation error.fieldTypeobjectThe type of error field.Show childrenHide childrenfieldstringThe full name of the property.fieldNamestringThe type of the field.shareholderCodestringThe code of the shareholder that the field belongs to. If empty, the field belongs to an account holder.metadataobjectA set of key and value pairs containing metadata.payoutMethodCodestringThe payout method code held by the account holder to couple the account with. Scheduled card payouts will be sent using this payout method code.payoutScheduleobjectThe details of the payout schedule added to the account.Show childrenHide childrennextScheduledPayoutstringThe date of the next scheduled payout.schedulestringThe payout schedule for the account.Possible values:DEFAULT,DAILY,DAILY_US,DAILY_EU,DAILY_AU,DAILY_SG,WEEKLY,WEEKLY_ON_TUE_FRI_MIDNIGHT,BIWEEKLY_ON_1ST_AND_15TH_AT_MIDNIGHT,MONTHLY,HOLD.HOLDprevents scheduled payouts, but you can still initiate payouts manually.payoutSpeedstringSpeed with which payouts for this account are processed. Permitted values:STANDARD,SAME_DAY.pspReferencestringThe reference of a request. Can be used to uniquely identify the request.resultCodestringThe result code.statusstringThe status of the account.Permitted values:Active.
- 202 - AcceptedThe request has been accepted for processing, but the processing has not been completed.Show moreShow lessaccountCodestringThe code of the new account.accountHolderCodestringThe code of the account holder.bankAccountUUIDstringThe bankAccountUUID of the bank account held by the account holder to couple the account with. Scheduled payouts in currencies matching the currency of this bank account will be sent to this bank account. Payouts in different currencies will be sent to a matching bank account of the account holder.descriptionstringThe description of the account.invalidFieldsarray[object]A list of fields that caused the/createAccountrequest to fail.Show childrenHide childrenerrorCodeintegerThe validation error code.errorDescriptionstringA description of the validation error.fieldTypeobjectThe type of error field.Show childrenHide childrenfieldstringThe full name of the property.fieldNamestringThe type of the field.shareholderCodestringThe code of the shareholder that the field belongs to. If empty, the field belongs to an account holder.metadataobjectA set of key and value pairs containing metadata.payoutMethodCodestringThe payout method code held by the account holder to couple the account with. Scheduled card payouts will be sent using this payout method code.payoutScheduleobjectThe details of the payout schedule added to the account.Show childrenHide childrennextScheduledPayoutstringThe date of the next scheduled payout.schedulestringThe payout schedule for the account.Possible values:DEFAULT,DAILY,DAILY_US,DAILY_EU,DAILY_AU,DAILY_SG,WEEKLY,WEEKLY_ON_TUE_FRI_MIDNIGHT,BIWEEKLY_ON_1ST_AND_15TH_AT_MIDNIGHT,MONTHLY,HOLD.HOLDprevents scheduled payouts, but you can still initiate payouts manually.payoutSpeedstringSpeed with which payouts for this account are processed. Permitted values:STANDARD,SAME_DAY.pspReferencestringThe reference of a request. Can be used to uniquely identify the request.resultCodestringThe result code.statusstringThe status of the account.Permitted values:Active.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 401 - UnauthorizedAuthentication required.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 422 - Unprocessable EntityA request validation error.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lesserrorCodestringThe error code mapped to the error message.errorTypestringThe category of the error.messagestringA short explanation of the issue.pspReferencestringThe PSP reference of the payment.statusintegerThe HTTP response status.

#### 200 - OK

#### 202 - Accepted

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error