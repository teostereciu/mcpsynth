# Management/3/get/merchants/(merchantId)/webhooks/(webhookId)

*Source: https://docs.adyen.com/api-explorer/Management/3/get/merchants/(merchantId)/webhooks/(webhookId)*

---

# Get a webhook
Returns the configuration for the webhook identified in the path.
To make this request, your API credential must have one of the followingroles:
- Management API—Webhooks read
- Management API—Webhooks read and write
Unique identifier of the webhook configuration.
The unique identifier of the merchant account.
After submitting a call, you receive a response message to inform you that your request was received and processed.
Depending on the HTTP status code of the response message, it is helpful to build some logic to handle any errors that a request or the system may return.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow less_linksobjectReferences to resources connected with this webhook.Show childrenHide childrencompanyobjectThe company account that the webhook is configured for. Only present for company-level webhooks.Show childrenHide childrenhrefstringgenerateHmacobjectGenerate an HMAC key.Show childrenHide childrenhrefstringmerchantobjectThe merchant account that the webhook is configured for. Only present for merchant-level webhooks.Show childrenHide childrenhrefstringselfobjectLink to the resource itself.Show childrenHide childrenhrefstringtestWebhookobjectTest the webhook setup.Show childrenHide childrenhrefstringacceptsExpiredCertificatebooleanIndicates if expired SSL certificates are accepted. Default value:false.acceptsSelfSignedCertificatebooleanIndicates if self-signed SSL certificates are accepted. Default value:false.acceptsUntrustedRootCertificatebooleanIndicates if untrusted SSL certificates are accepted. Default value:false.accountReferencestringReference to the account the webook is set on.activebooleanIndicates if the webhook configuration is active. The field must betruefor you to receive webhooks about events related an account.additionalSettingsobjectAdditional shopper and transaction information to be included in yourstandard webhooks. Find out more about the availableadditional settings.Show childrenHide childrenexcludeEventCodesarray[string]Object containing list of event codes for which the notification will not be sent.includeEventCodesarray[string]Object containing list of event codes for which the notification will be sent.propertiesobjectObject containing boolean key-value pairs. The key can be anystandard webhook additional setting, and the value indicates if the setting is enabled.
For example,includeCaptureDelayHours:truemeans the standard notifications you get will contain the number of hours remaining until the payment will be captured.certificateAliasstringThe alias of our SSL certificate. When you receive a notification from us, the alias from the HMAC signature will match this alias.communicationFormatstringFormat or protocol for receiving webhooks. Possible values:soaphttpjsondescriptionstringYour description for this webhook configuration.encryptionProtocolstringSSL version to access the public webhook URL specified in theurlfield. Possible values:TLSv1.3TLSv1.2HTTP- Only allowed on Test environment.If not specified, the webhook will usesslVersion:TLSv1.2.filterMerchantAccountTypestringShows how merchant accounts are included in company-level webhooks. Possible values:includeAccountsexcludeAccountsallAccounts: Includes all merchant accounts, and does not require specifyingfilterMerchantAccounts.filterMerchantAccountsarray[string]A list of merchant account names that are included or excluded from receiving the webhook. Inclusion or exclusion is based on the value defined forfilterMerchantAccountType.Required iffilterMerchantAccountTypeis either:includeAccountsexcludeAccountsNot needed forfilterMerchantAccountType:allAccounts.hasErrorbooleanIndicates if the webhook configuration has errors that need troubleshooting. If the value istrue, troubleshoot the configuration using thetesting endpoint.hasPasswordbooleanIndicates if the webhook is password protected.hmacKeyCheckValuestringThechecksumof the HMAC key generated for this webhook. You can use this value to uniquely identify the HMAC key configured for this webhook.idstringUnique identifier for this webhook.networkTypestringNetwork type for Terminal API details webhooks.populateSoapActionHeaderbooleanIndicates if the SOAP action header needs to be populated. Default value:false.Only applies ifcommunicationFormat:soap.typestringThe type of webhook. Possible values are:standardaccount-settings-notificationbanktransfer-notificationboletobancario-notificationdirectdebit-notificationach-notification-of-change-notificationdirect-debit-notice-of-change-notificationpending-notificationideal-notificationideal-pending-notificationreport-notificationterminal-api-notificationterminal-settingsterminal-boardingFind out more aboutstandard webhooksandother types of webhooks.urlstringPublic URL where webhooks will be sent, for examplehttps://www.domain.com/webhook-endpoint.usernamestringUsername to access the webhook URL.
- 204 - No ContentThe request has been successfully processed, but there is no additional content.
- 400 - Bad RequestA problem reading or understanding the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 401 - UnauthorizedAuthentication required.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 403 - ForbiddenInsufficient permissions to process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 422 - Unprocessable EntityA request validation error.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.
- 500 - Internal Server ErrorThe server could not process the request.Show moreShow lessdetailstringA human-readable explanation specific to this occurrence of the problem.errorCodestringA code that identifies the problem type.instancestringA unique URI that identifies the specific occurrence of the problem.invalidFieldsarray[object]Detailed explanation of each validation error, when applicable.Show childrenHide childrenmessagestringDescription of the validation error.namestringThe field that has an invalid value.valuestringThe invalid value.requestIdstringA unique reference for the request, essentially the same aspspReference.responseobjectJSON response payload.statusintegerThe HTTP status code.titlestringA short, human-readable summary of the problem type.typestringA URI that identifies the problem type, pointing to human-readable documentation on this problem type.

#### 200 - OK
- soap
- http
- json
- TLSv1.3
- TLSv1.2
- HTTP- Only allowed on Test environment.
- includeAccounts
- excludeAccounts
- allAccounts: Includes all merchant accounts, and does not require specifyingfilterMerchantAccounts.
- includeAccounts
- excludeAccounts
- standard
- account-settings-notification
- banktransfer-notification
- boletobancario-notification
- directdebit-notification
- ach-notification-of-change-notification
- direct-debit-notice-of-change-notification
- pending-notification
- ideal-notification
- ideal-pending-notification
- report-notification
- terminal-api-notification
- terminal-settings
- terminal-boarding

#### 204 - No Content

#### 400 - Bad Request

#### 401 - Unauthorized

#### 403 - Forbidden

#### 422 - Unprocessable Entity

#### 500 - Internal Server Error