# balanceplatform-webhooks/2/post/balancePlatform.networkToken.updated

*Source: https://docs.adyen.com/api-explorer/balanceplatform-webhooks/2/post/balancePlatform.networkToken.updated*

---

# Network token updated
Adyen sends this webhook when there is an internal status update for the network token during the provisioning process.
Contains event details.
Contains information about the authentication process triggered during token provisioning.
The method used to complete the authentication process.
Possible values:sms_OTP,email_OTP.
The result of the authentication process.
Specifies whether the authentication process was triggered during token provisioning.
The unique identifier of the balance platform.
The decision about the network token provisioning.
Possible values:approved,declined,requiresAuthentication.
The unique identifier of the network token.
The unique identifier of the payment instrument to which the network token is associated.
The confidence score of scheme, indicating the degree of risk associated with a token.
A high score indicates a high level of risk. A low score indicates a low level of risk.
Possible values for visa :00to99, a value of 00 signifies no score was provided by visa
The status of the network token.
The last four digits of the network token. Use this value to help your user to identify their network token.
Contains information about the entity or organization that is requesting the network token.
The unique identifier of the network token requestor.
The name of the network token requestor.
Contains the results of the evaluation of the transaction rules that apply to network token creation.
The advice given by the Risk analysis.
Indicates whether the transaction passed all rules withoutcomeTypehardBlock.
The score of the Risk analysis.
Contains a list of all triggered transaction rules and the corresponding data.
Explains why the transaction rule failed.
Contains information about the transaction rule.
The description of the transaction rule.
The unique identifier of the transaction rule.
The outcome type of the transaction rule.
The reference for the transaction rule.
The transaction score determined by the rule.
Contains information about the resource to which the transaction rule applies.
The unique identifier of the resource to which the transaction rule applies.
Indicates the type of resource for which the transaction rule is defined.
Possible values:
- PaymentInstrumentGroup
- PaymentInstrument
- BalancePlatform
- EntityUsageConfiguration
- PlatformRule: The transaction rule is a platform-wide rule imposed by Adyen.
The type of network token.
Possible values:wallet,cof.
The rules used to validate the request for provisioning the network token.
The reason for theresultof the validations.
This field is only sent forvalidationFacts.typewalletValidation, whenvalidationFacts.resultisinvalid.
The evaluation result of the validation facts.
Possible values:valid,invalid,notValidated,notApplicable.
The type of the validation fact.
Contains information about the wallet for which the network token is provisioned.
Returned only whentypeiswallet.
The confidence score of the wallet account, calculated by the wallet provider.
A high score means that account is considered trustworthy. A low score means that the account is considered suspicious.
Possible values:1to5.
Contains information about the device used for provisioning the network token.
The unique identifier of the device used for provisioning the network token.
The type of the device used for provisioning the network token.
For example,phone,mobile_phone,watch,mobilephone_or_tablet, etc
The operating system of the device used for provisioning the network token.
The confidence score of the device, calculated by the wallet provider.
A high score means that device is considered trustworthy. A low score means that the device is considered suspicious.
Possible values:1to5.
The method used for provisioning the network token.
Possible values:push,manual,cof,unknown.
A list of risk indicators triggered at the time of provisioning the network token.
Some example values of risk indicators are:
- accountTooNewSinceLaunch
- tooManyRecentAttempts
- lowDeviceScore
- lowAccountScore
Use name of thetokenRequestorinstead.
The type of wallet that the network token is associated with.
Possible values:applePay,googlePay,garminPay.
The environment from which the webhook originated.
Possible values:test,live.
When the event was queued.
The type of webhook.
When you receive a webhook, you must respond with an HTTP status code.

### HTTP Responses
- 200 - OKThe request has succeeded.Show moreShow lessnotificationResponsestringRespond with any2xxHTTP status code toaccept the webhook.

#### 200 - OK