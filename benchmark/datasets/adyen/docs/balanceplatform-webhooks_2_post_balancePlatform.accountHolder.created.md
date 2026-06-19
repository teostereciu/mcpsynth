# balanceplatform-webhooks/2/post/balancePlatform.accountHolder.created

*Source: https://docs.adyen.com/api-explorer/balanceplatform-webhooks/2/post/balancePlatform.accountHolder.created*

---

# Account holder created
Adyen sends this webhook when you successfullycreate an account holder.
Contains event details.
Contains information about the account holder resource that triggered the event.
The unique identifier of thebalance platformto which the account holder belongs. Required in the request if your API credentials can be used for multiple balance platforms.
Contains key-value pairs that specify the actions that an account holder can do in your platform. The key is a capability required for your integration. For example,issueCardfor Issuing. The value is an object containing the settings for the capability.
Indicates whether the capability is allowed. Adyen sets this totrueif the verification is successful and the account holder is permitted to use the capability.
The capability level that is allowed for the account holder.
Possible values:notApplicable,low,medium,high.
A JSON object containing the settings that are allowed for the account holder.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
Indicates whether the capability is enabled. Iffalse, the capability is temporarily disabled for the account holder.
Contains verification errors and the actions that you can take to resolve them.
Contains the type of the entity and the corresponding ID.
List of document IDs to which the verification errors related to the capabilities correspond to.
The ID of the entity.
Contains details about the owner of the entity that has an error.
List of document IDs to which the verification errors related to the capabilities correspond to.
The ID of the entity.
Type of entity.
Possible values:LegalEntity,BankAccount,Document.
Type of entity.
Possible values:LegalEntity,BankAccount,Document.
Contains information about the verification error.
Contains the capabilities that the verification error applies to.
The verification error code.
A description of the error.
Contains the actions that you can take to resolve the verification error.
The remediating action code.
A description of how you can resolve the verification error.
Contains more granular information about the verification error.
Contains the capabilities that the verification error applies to.
The verification error code.
A description of the error.
The type of error.
Possible values:
- invalidInput
- dataMissing
- pendingStatus
- dataReview
Contains the actions that you can take to resolve the verification error.
The remediating action code.
A description of how you can resolve the verification error.
The type of error.
Possible values:
- invalidInput
- dataMissing
- pendingStatus
- dataReview
Indicates whether the capability is requested. To check whether the account holder is permitted to use the capability, refer to theallowedfield.
The requested level of the capability. Some capabilities, such as those used incard issuing, have different levels. Levels increase the capability, but also require additional checks and increased monitoring.
Possible values:notApplicable,low,medium,high.
A JSON object containing the settings that were requested for the account holder.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
The three-characterISO currency codeof the amount.
The numeric value of the amount, inminor units.
Contains the status of the transfer instruments associated with this capability.
Indicates whether the supporting entity capability is allowed. Adyen sets this totrueif the verification is successful and the account holder is permitted to use the capability.
The capability level that is allowed for the account holder.
Possible values:notApplicable,low,medium,high.
Indicates whether the capability is enabled. Iffalse, the capability is temporarily disabled for the account holder.
The ID of the supporting entity.
Indicates whether the capability is requested. To check whether the account holder is permitted to use the capability, refer to theallowedfield.
The requested level of the capability. Some capabilities, such as those used incard issuing, have different levels. Levels increase the capability, but also require additional checks and increased monitoring.
Possible values:notApplicable,low,medium,high.
The status of the verification checks for the supporting entity capability.
Possible values:
- pending: Adyen is running the verification.
- invalid: The verification failed. Check if theerrorsarray contains more information.
- valid: The verification has been successfully completed.
- rejected: Adyen has verified the information, but found reasons to not allow the capability.
The status of the verification checks for the capability.
Possible values:
- pending: Adyen is running the verification.
- invalid: The verification failed. Check if theerrorsarray contains more information.
- valid: The verification has been successfully completed.
- rejected: Adyen has verified the information, but found reasons to not allow the capability.
Contact details of the account holder.
The address of the account holder.
The name of the city. Maximum length: 3000 characters.
The two-character ISO-3166-1 alpha-2 country code. For example,US.
If you don't know the country or are not collecting the country from the shopper, providecountryasZZ.
The number or name of the house. Maximum length: 3000 characters.
A maximum of five digits for an address in the US, or a maximum of ten characters for an address in all other countries.
The two-character ISO 3166-2 state or province code. For example,CAin the US orONin Canada.
Required for the US and Canada.
The name of the street. Maximum length: 3000 characters.
The house number should not be included in this field; it should be separately provided viahouseNumberOrName.
The email address of the account holder.
The phone number of the account holder.
The full phone number provided as a single string.
For example,"0031 6 11 22 33 44","+316/1122-3344",
or"(0031) 611223344".
Type of phone number.
Possible values:Landline,Mobile.
The URL of the account holder's website.
Your description for the account holder.
The unique identifier of the account holder.
The unique identifier of thelegal entityassociated with the account holder. Adyen performs a verification process against the legal entity of the account holder.
A set of key and value pairs for general use.
The keys do not have specific names and may be used for storing miscellaneous data as desired.
Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of those key-value pairs.
The unique identifier of the migrated account holder in the classic integration.
The ID of the account holder's primary balance account. By default, this is set to the first balance account that you create for the account holder. To assign a different balance account, send a PATCH request.
Your reference for the account holder.
The status of the account holder.
Possible values:
- active: The account holder is active and allowed to use its capabilities. This is the initial status for account holders and balance accounts. You can change this status tosuspendedorclosed.
- suspended: The account holder is temporarily disabled and payouts are blocked. You can change this status toactiveorclosed.
- closed: The account holder and all of its capabilities are permanently disabled. This is a final status and cannot be changed.
The time zone of the account holder. For example,Europe/Amsterdam.
Defaults to the time zone of the balance platform if no time zone is set. For possible values, see thelist of time zone codes.
List of verification deadlines and the capabilities that will be disallowed if verification errors are not resolved.
The names of the capabilities to be disallowed.
The unique identifiers of the bank account(s) that the deadline applies to
The date that verification is due by before capabilities are disallowed.
The unique identifier of the balance platform.
The environment from which the webhook originated.
Possible values:test,live.
When the event was queued.
Type of webhook.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringRespond with any2xxHTTP status code toaccept the webhook.

#### 200 - OK