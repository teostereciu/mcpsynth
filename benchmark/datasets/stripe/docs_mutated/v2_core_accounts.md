# v2/core/accounts

*Source: https://docs.stripe.com/api/v2/core/accounts*

---

# Accountsv2
An Account v2 object represents a company, individual, or other entity that interacts with a platform on Stripe. It contains both identifying information and properties that control its behavior and functionality. An Account can have one or more configurations that enable sets of related features, such as allowing it to act as a merchant or customer_id.The Accounts v2 API supports both the Global Payouts preview feature and the Connect-Billing integration preview feature. However, a particular Account can only access one of them.The Connect-Billing integration preview feature allows an Account v2 to pay subscription fees to a platform. An Account v1 required a separate Customer object to pay subscription fees.

# The Account objectv2

### Attributes
- idstringUnique identifier for the Account.
- objectstring, value is "v2.core.account"String representing the object’s type. Objects of the same type share the same value of the object field.
- applied_configurationsarray of enumsThe configurations that have been applied to this account.Possible enum valuescustomerThe Account can be used as a customer_id.merchantThe Account can be used as a merchant.recipientThe Account can be used as a recipient.
- closednullablebooleanIndicates whether the account has been closed.
- configurationnullableobjectAn Account represents a company, individual, or other entity that a user interacts with. Accounts store identity information and one or more configurations that enable product-specific capabilities. You can assign configurations at creation or add them later.Show child attributes
- contact_emailnullablestringThe default contact email address for the Account. Required when configuring the account as a merchant or recipient.
- contact_phonenullablestringThe default contact phone for the Account.
- createdtimestampTime at which the object was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
- dashboardnullableenumA value indicating the Stripe dashboard this Account has access to. This will depend on which configurations are enabled for this account.Possible enum valuesexpressThe Account has access to the Express hosted dashboard.fullThe Account has access to the full Stripe hosted dashboard.noneThe Account does not have access to any Stripe hosted dashboard.
- defaultsnullableobjectDefault values for settings shared across Account configurations.Show child attributes
- display_namenullablestringA descriptive name for the Account. This name will be surfaced in the Stripe Dashboard and on any invoices sent to the Account.
- future_requirementsnullableobjectInformation about the future requirements for the Account that will eventually come into effect, including what information needs to be collected, and by when.Show child attributes
- identitynullableobjectInformation about the company, individual, and business represented by the Account.Show child attributes
- livemodebooleanHas the valuetrueif the object exists in live mode or the valuefalseif the object exists in test mode.
- metadatanullablemapSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- requirementsnullableobjectInformation about the active requirements for the Account, including what information needs to be collected, and by when.Show child attributes

#### idstring

#### objectstring, value is "v2.core.account"

#### applied_configurationsarray of enums

[TABLE]
customerThe Account can be used as a customer_id.
merchantThe Account can be used as a merchant.
recipientThe Account can be used as a recipient.
[/TABLE]

#### closednullableboolean

#### configurationnullableobject

#### contact_emailnullablestring

#### contact_phonenullablestring

#### createdtimestamp

#### dashboardnullableenum

[TABLE]
expressThe Account has access to the Express hosted dashboard.
fullThe Account has access to the full Stripe hosted dashboard.
noneThe Account does not have access to any Stripe hosted dashboard.
[/TABLE]

#### defaultsnullableobject

#### display_namenullablestring

#### future_requirementsnullableobject

#### identitynullableobject

#### livemodeboolean

#### metadatanullablemap

#### requirementsnullableobject

```
{"id":"acct_1Nv0FGQ9RKHgCVdK","object":"v2.core.account","applied_configurations":["customer_id","merchant"],"configuration":{"customer_id":{"automatic_indirect_tax":{"exempt":"none","location":{"country":"US","state":"NY"},"location_source":"identity_address"},"billing":{"invoice":{"next_sequence":1,"prefix":"5626C87C","custom_fields":[]}},"capabilities":{"automatic_indirect_tax":{"status":"active","status_details":[]}}},"merchant":{"card_payments":{"decline_on":{"avs_failure":false,"cvc_failure":false}},"capabilities":{"card_payments":{"status":"active","status_details":[]},"stripe_balance":{"payouts":{"status":"active","status_details":[]}}}}},"contact_email":"furever@example.com","created":"2025-03-28T19:59:16.000Z","dashboard":"full","identity":{"business_details":{"registered_name":"Furever","address":{"country":"US","postal_code":"10001"}},"country":"US","entity_type":"company"},"defaults":{"currency_code":"usd","responsibilities":{"fees_collector":"stripe","losses_collector":"stripe","requirements_collector":"stripe"}},"display_name":"Furever"}
```

```
{"id":"acct_1Nv0FGQ9RKHgCVdK","object":"v2.core.account","applied_configurations":["customer_id","merchant"],"configuration":{"customer_id":{"automatic_indirect_tax":{"exempt":"none","location":{"country":"US","state":"NY"},"location_source":"identity_address"},"billing":{"invoice":{"next_sequence":1,"prefix":"5626C87C","custom_fields":[]}},"capabilities":{"automatic_indirect_tax":{"status":"active","status_details":[]}}},"merchant":{"card_payments":{"decline_on":{"avs_failure":false,"cvc_failure":false}},"capabilities":{"card_payments":{"status":"active","status_details":[]},"stripe_balance":{"payouts":{"status":"active","status_details":[]}}}}},"contact_email":"furever@example.com","created":"2025-03-28T19:59:16.000Z","dashboard":"full","identity":{"business_details":{"registered_name":"Furever","address":{"country":"US","postal_code":"10001"}},"country":"US","entity_type":"company"},"defaults":{"currency_code":"usd","responsibilities":{"fees_collector":"stripe","losses_collector":"stripe","requirements_collector":"stripe"}},"display_name":"Furever"}
```

# Create an Accountv2
An Account is a representation of a company, individual or other entity that a user interacts with. Accounts contain identifying information about the entity, and configurations that store the features an account has access to. An account can be configured as any or all of the following configurations: Customer, Merchant and/or Recipient.

### Parameters
- account_tokenstringThe account token generated by the account token api.
- configurationobjectAn Account Configuration which allows the Account to take on a key persona across Stripe products.Show child parameters
- contact_emailstringThe default contact email address for the Account. Required when configuring the account as a merchant or recipient.
- contact_phonestringThe default contact phone for the Account.
- dashboardenumA value indicating the Stripe dashboard this Account has access to. This will depend on which configurations are enabled for this account.Possible enum valuesexpressThe Account has access to the Express hosted dashboard.fullThe Account has access to the full Stripe hosted dashboard.noneThe Account does not have access to any Stripe hosted dashboard.
- defaultsobjectDefault values to be used on Account Configurations.Show child parameters
- display_namestringA descriptive name for the Account. This name will be surfaced in the Stripe Dashboard and on any invoices sent to the Account.
- identityobjectInformation about the company, individual, and business represented by the Account.Show child parameters
- includearray of enumsAdditional fields to include in the response.Possible enum valuesconfiguration.customerInclude parameter to exposeconfiguration.customeron an Account.configuration.merchantInclude parameter to exposeconfiguration.merchanton an Account.configuration.recipientInclude parameter to exposeconfiguration.recipienton an Account.defaultsInclude parameter to exposedefaultson an Account.future_requirementsInclude parameter to exposefuture_requirementson an Account.identityInclude parameter to exposeidentityon an Account.requirementsInclude parameter to exposerequirementson an Account.
- metadatamapSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

#### account_tokenstring

#### configurationobject

#### contact_emailstring

#### contact_phonestring

#### dashboardenum

[TABLE]
expressThe Account has access to the Express hosted dashboard.
fullThe Account has access to the full Stripe hosted dashboard.
noneThe Account does not have access to any Stripe hosted dashboard.
[/TABLE]

#### defaultsobject

#### display_namestring

#### identityobject

#### includearray of enums

[TABLE]
configuration.customerInclude parameter to exposeconfiguration.customeron an Account.
configuration.merchantInclude parameter to exposeconfiguration.merchanton an Account.
configuration.recipientInclude parameter to exposeconfiguration.recipienton an Account.
defaultsInclude parameter to exposedefaultson an Account.
future_requirementsInclude parameter to exposefuture_requirementson an Account.
identityInclude parameter to exposeidentityon an Account.
requirementsInclude parameter to exposerequirementson an Account.
[/TABLE]

```
configuration.customer_id
```

```
configuration.merchant
```

```
configuration.recipient
```

```
future_requirements
```

```
requirements
```

#### metadatamap

### Returns

### Response attributes
- idstringUnique identifier for the Account.
- objectstring, value is "v2.core.account"String representing the object’s type. Objects of the same type share the same value of the object field.
- applied_configurationsarray of enumsThe configurations that have been applied to this account.Possible enum valuescustomerThe Account can be used as a customer_id.merchantThe Account can be used as a merchant.recipientThe Account can be used as a recipient.
- closednullablebooleanIndicates whether the account has been closed.
- configurationnullableobjectAn Account represents a company, individual, or other entity that a user interacts with. Accounts store identity information and one or more configurations that enable product-specific capabilities. You can assign configurations at creation or add them later.Show child attributes
- contact_emailnullablestringThe default contact email address for the Account. Required when configuring the account as a merchant or recipient.
- contact_phonenullablestringThe default contact phone for the Account.
- createdtimestampTime at which the object was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
- dashboardnullableenumA value indicating the Stripe dashboard this Account has access to. This will depend on which configurations are enabled for this account.Possible enum valuesexpressThe Account has access to the Express hosted dashboard.fullThe Account has access to the full Stripe hosted dashboard.noneThe Account does not have access to any Stripe hosted dashboard.
- defaultsnullableobjectDefault values for settings shared across Account configurations.Show child attributes
- display_namenullablestringA descriptive name for the Account. This name will be surfaced in the Stripe Dashboard and on any invoices sent to the Account.
- future_requirementsnullableobjectInformation about the future requirements for the Account that will eventually come into effect, including what information needs to be collected, and by when.Show child attributes
- identitynullableobjectInformation about the company, individual, and business represented by the Account.Show child attributes
- livemodebooleanHas the valuetrueif the object exists in live mode or the valuefalseif the object exists in test mode.
- metadatanullablemapSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- requirementsnullableobjectInformation about the active requirements for the Account, including what information needs to be collected, and by when.Show child attributes

#### idstring

#### objectstring, value is "v2.core.account"

#### applied_configurationsarray of enums

[TABLE]
customerThe Account can be used as a customer_id.
merchantThe Account can be used as a merchant.
recipientThe Account can be used as a recipient.
[/TABLE]

#### closednullableboolean

#### configurationnullableobject

#### contact_emailnullablestring

#### contact_phonenullablestring

#### createdtimestamp

#### dashboardnullableenum

[TABLE]
expressThe Account has access to the Express hosted dashboard.
fullThe Account has access to the full Stripe hosted dashboard.
noneThe Account does not have access to any Stripe hosted dashboard.
[/TABLE]

#### defaultsnullableobject

#### display_namenullablestring

#### future_requirementsnullableobject

#### identitynullableobject

#### livemodeboolean

#### metadatanullablemap

#### requirementsnullableobject
Requested capability is not available.
The requested configuration is not available for the account.
Ifdashboardisexpress,fees_collectormust beapplicationandlosses_collectormust beapplication.
Iflosses_collectorisapplication,fees_collectormust also beapplication.
Connect integration combination is not supported when UA beta is enabled.
Connect integration combination is not supported when UA beta is disabled.
Responsibility combinations is not supported in private preview.
Currency is not allowed for the account’s country.
Platform must be activated to create connected accounts.
Account creation is invalid.
Account creation error - liability unacknowledged.
Account creation error - requirement collection and liability unacknowledged.
Account creation error - requirement collection unacknowledged.
Terms of service must be accepted before adding merchant configuration.
Account token required for platforms in mandated countries (e.g., France).
Accounts v2 is not enabled for your platform.
Invalid characters are provided for address fields.
Address country doesn’t match identity country.
Address postal code is invalid.
Address state is invalid.
Address town is invalid.
Creating accounts with the BGN currency_code is no longer supported, as Bulgaria is now using the Euro as of 2026-01-01.
Dormant accounts cannot create accounts where requirements collector is application (this is an account takeover prevention measure).
Platform is in an invalid state and cannot create connected accounts.
Platform is in a rejected state and cannot create connected accounts.
Feature cannot be unrequested due to being a requirement for another feature.
Feature cannot be requested for the dashboard type.
Requested feature is not available for the entity type in your country.
A v2 Account cannot have both the specified capability and Stripe-owned loss liability.
Requested capability is not available in your country.
Feature cannot be requested given the platform’s country.
Requested feature is not available without also requesting a different feature.
Requested feature is not available without also requesting a different feature in your country.
Cannot create an account with an invalid configuration.
Platform is not verified and cannot create connected accounts.
Platform has not completed platform questionnaire and cannot create connected accounts.
Cross-border connected account creation is not allowed for this platform/account country combination.
Custom accounts cannot be created in certain countries.
Representative date of birth does not meet the age limit.
Representative date of birth is provided an invalid date or a future date.
Cannot changedefaults.currencypost account activation.
Default payment method provided for a customer_id does not exist or is otherwise invalid.
Specified payment method exists but its type is not allowed to be the default payment method.
Directorship declaration is not allowed during account creation.
Provided file tokens for documents are invalid, not found, deleted, or belong to a different account.
Provided file tokens for documents are of the wrong purpose.
Email contains unsupported domain.
Incorrect email is provided.
Theidentity.entity_typevalue is not supported in a givenidentity.country.
NONE is combined with another value in the HighRiskActivities list.
Provided ID number is of the wrong format for the given type.
Theidentity.countryvalue is required but not provided.
Incorrect ID number is provided for a country.
The incorrect token type is provided .
ID number is provided that is not permitted for the Identity’s entity type and business structure.
Theidentity.business_details.id_numbers.registrarvalue is an invalid DE registrar.
Konbini Payments Support Hours is Invalid.
Konbini Payments Support Phone Number is Invalid.
Invoice rendering template does not exist or is otherwise invalid.
Invalid IP address is provided.
MCC is invalid forconfiguration.merchant.mcc.
Kana Kanji script addresses must have JP country.
Ownership declaration is not allowed during account creation.
Parameter cannot be passed alongside account_token.
Error returned when relationship.owner is set to true but the ownership percentage is set to 0%.
Phone number is invalid.
Platform has not signed up for Connect and cannot create connected accounts.
Postal code is required for Japanese addresses.
PurposeOfFundsDescription is not empty while PurposeOfFunds is not OTHER.
Registration date must be in the past.
Provided script characters are invalid for the script.
Shipping address is required within the shipping hash.
Shipping name is required within the shipping hash.
Statement descriptor is invalid.
Thebusiness_details.structurevalue is not valid foridentity.countryandidentity.entity_type.
Cannot set a test clock on a livemode customer_id.
Test clock does not exist or is otherwise invalid.
Cannot modify a test clock that is currently advancing.
Cannot add customer_id to a test clock that has already reached its customer_id limit.
The token is re-used with a different idempotency key.
Token has expired.
TOS cannot be accepted on behalf of accounts when requirement collection isstripe.
Cannot set responsibilities on the current configurations.
Cannot set identity fields when the Account is only configured as a customer_id.
Address is in an unsupported postal code.
Address is in an unsupported state.
URL is invalid.
A v1 token ID is passed in v2 APIs.
Invalid account token.
An idempotent retry occurred with different request parameters.
Account cannot exceed a configured concurrency rate limit on updates.

```
curl-X POST https://api.stripe.com/v2/core/accounts \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\--json'{"contact_email": "furever@example.com","display_name": "Furever","identity": {"country": "us","entity_type": "company","business_details": {"registered_name": "Furever"}},"configuration": {"customer_id": {"capabilities": {"automatic_indirect_tax": {"requested": true}}},"merchant": {"capabilities": {"card_payments": {"requested": true}}}},"defaults": {"responsibilities": {"fees_collector": "stripe","losses_collector": "stripe"}},"dashboard": "full","include": ["configuration.merchant","configuration.customer_id","identity","defaults"]}'
```

```
curl-X POST https://api.stripe.com/v2/core/accounts \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\--json'{"contact_email": "furever@example.com","display_name": "Furever","identity": {"country": "us","entity_type": "company","business_details": {"registered_name": "Furever"}},"configuration": {"customer_id": {"capabilities": {"automatic_indirect_tax": {"requested": true}}},"merchant": {"capabilities": {"card_payments": {"requested": true}}}},"defaults": {"responsibilities": {"fees_collector": "stripe","losses_collector": "stripe"}},"dashboard": "full","include": ["configuration.merchant","configuration.customer_id","identity","defaults"]}'
```

```
{"id":"acct_1Nv0FGQ9RKHgCVdK","object":"v2.core.account","applied_configurations":["customer_id","merchant"],"configuration":{"customer_id":{"applied":"2025-03-28T19:59:16.000Z","automatic_indirect_tax":{"exempt":"none","location_source":"identity_address"},"billing":{"invoice":{"next_sequence":1,"prefix":"5626C87C","custom_fields":[]}},"capabilities":{"automatic_indirect_tax":{"status":"active","status_details":[]}}},"merchant":{"applied":"2025-03-28T19:59:16.000Z","card_payments":{"decline_on":{"avs_failure":false,"cvc_failure":false}},"capabilities":{"card_payments":{"status":"active","status_details":[]},"stripe_balance":{"payouts":{"status":"active","status_details":[]}}}}},"contact_email":"furever@example.com","created":"2025-03-28T19:59:16.000Z","dashboard":"full","identity":{"business_details":{"registered_name":"Furever"},"country":"US","entity_type":"company"},"livemode":false,"defaults":{"currency_code":"usd","responsibilities":{"fees_collector":"stripe","losses_collector":"stripe","requirements_collector":"stripe"}},"display_name":"Furever"}
```

```
{"id":"acct_1Nv0FGQ9RKHgCVdK","object":"v2.core.account","applied_configurations":["customer_id","merchant"],"configuration":{"customer_id":{"applied":"2025-03-28T19:59:16.000Z","automatic_indirect_tax":{"exempt":"none","location_source":"identity_address"},"billing":{"invoice":{"next_sequence":1,"prefix":"5626C87C","custom_fields":[]}},"capabilities":{"automatic_indirect_tax":{"status":"active","status_details":[]}}},"merchant":{"applied":"2025-03-28T19:59:16.000Z","card_payments":{"decline_on":{"avs_failure":false,"cvc_failure":false}},"capabilities":{"card_payments":{"status":"active","status_details":[]},"stripe_balance":{"payouts":{"status":"active","status_details":[]}}}}},"contact_email":"furever@example.com","created":"2025-03-28T19:59:16.000Z","dashboard":"full","identity":{"business_details":{"registered_name":"Furever"},"country":"US","entity_type":"company"},"livemode":false,"defaults":{"currency_code":"usd","responsibilities":{"fees_collector":"stripe","losses_collector":"stripe","requirements_collector":"stripe"}},"display_name":"Furever"}
```

# Update an Accountv2
Updates the details of an Account.

### Parameters
- idstringRequiredThe ID of the Account to update.
- account_tokenstringThe account token generated by the account token api.
- configurationobjectAn Account Configuration which allows the Account to take on a key persona across Stripe products.Show child parameters
- contact_emailstringThe default contact email address for the Account. Required when configuring the account as a merchant or recipient.
- contact_phonestringThe default contact phone for the Account.
- dashboardenumA value indicating the Stripe dashboard this Account has access to. This will depend on which configurations are enabled for this account.Possible enum valuesexpressThe Account has access to the Express hosted dashboard.fullThe Account has access to the full Stripe hosted dashboard.noneThe Account does not have access to any Stripe hosted dashboard.
- defaultsobjectDefault values to be used on Account Configurations.Show child parameters
- display_namestringA descriptive name for the Account. This name will be surfaced in the Stripe Dashboard and on any invoices sent to the Account.
- identityobjectInformation about the company, individual, and business represented by the Account.Show child parameters
- includearray of enumsAdditional fields to include in the response.Possible enum valuesconfiguration.customerInclude parameter to exposeconfiguration.customeron an Account.configuration.merchantInclude parameter to exposeconfiguration.merchanton an Account.configuration.recipientInclude parameter to exposeconfiguration.recipienton an Account.defaultsInclude parameter to exposedefaultson an Account.future_requirementsInclude parameter to exposefuture_requirementson an Account.identityInclude parameter to exposeidentityon an Account.requirementsInclude parameter to exposerequirementson an Account.
- metadatamapSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

#### idstringRequired

#### account_tokenstring

#### configurationobject

#### contact_emailstring

#### contact_phonestring

#### dashboardenum

[TABLE]
expressThe Account has access to the Express hosted dashboard.
fullThe Account has access to the full Stripe hosted dashboard.
noneThe Account does not have access to any Stripe hosted dashboard.
[/TABLE]

#### defaultsobject

#### display_namestring

#### identityobject

#### includearray of enums

[TABLE]
configuration.customerInclude parameter to exposeconfiguration.customeron an Account.
configuration.merchantInclude parameter to exposeconfiguration.merchanton an Account.
configuration.recipientInclude parameter to exposeconfiguration.recipienton an Account.
defaultsInclude parameter to exposedefaultson an Account.
future_requirementsInclude parameter to exposefuture_requirementson an Account.
identityInclude parameter to exposeidentityon an Account.
requirementsInclude parameter to exposerequirementson an Account.
[/TABLE]

```
configuration.customer_id
```

```
configuration.merchant
```

```
configuration.recipient
```

```
future_requirements
```

```
requirements
```

#### metadatamap

### Returns

### Response attributes
- idstringUnique identifier for the Account.
- objectstring, value is "v2.core.account"String representing the object’s type. Objects of the same type share the same value of the object field.
- applied_configurationsarray of enumsThe configurations that have been applied to this account.Possible enum valuescustomerThe Account can be used as a customer_id.merchantThe Account can be used as a merchant.recipientThe Account can be used as a recipient.
- closednullablebooleanIndicates whether the account has been closed.
- configurationnullableobjectAn Account represents a company, individual, or other entity that a user interacts with. Accounts store identity information and one or more configurations that enable product-specific capabilities. You can assign configurations at creation or add them later.Show child attributes
- contact_emailnullablestringThe default contact email address for the Account. Required when configuring the account as a merchant or recipient.
- contact_phonenullablestringThe default contact phone for the Account.
- createdtimestampTime at which the object was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
- dashboardnullableenumA value indicating the Stripe dashboard this Account has access to. This will depend on which configurations are enabled for this account.Possible enum valuesexpressThe Account has access to the Express hosted dashboard.fullThe Account has access to the full Stripe hosted dashboard.noneThe Account does not have access to any Stripe hosted dashboard.
- defaultsnullableobjectDefault values for settings shared across Account configurations.Show child attributes
- display_namenullablestringA descriptive name for the Account. This name will be surfaced in the Stripe Dashboard and on any invoices sent to the Account.
- future_requirementsnullableobjectInformation about the future requirements for the Account that will eventually come into effect, including what information needs to be collected, and by when.Show child attributes
- identitynullableobjectInformation about the company, individual, and business represented by the Account.Show child attributes
- livemodebooleanHas the valuetrueif the object exists in live mode or the valuefalseif the object exists in test mode.
- metadatanullablemapSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- requirementsnullableobjectInformation about the active requirements for the Account, including what information needs to be collected, and by when.Show child attributes

#### idstring

#### objectstring, value is "v2.core.account"

#### applied_configurationsarray of enums

[TABLE]
customerThe Account can be used as a customer_id.
merchantThe Account can be used as a merchant.
recipientThe Account can be used as a recipient.
[/TABLE]

#### closednullableboolean

#### configurationnullableobject

#### contact_emailnullablestring

#### contact_phonenullablestring

#### createdtimestamp

#### dashboardnullableenum

[TABLE]
expressThe Account has access to the Express hosted dashboard.
fullThe Account has access to the full Stripe hosted dashboard.
noneThe Account does not have access to any Stripe hosted dashboard.
[/TABLE]

#### defaultsnullableobject

#### display_namenullablestring

#### future_requirementsnullableobject

#### identitynullableobject

#### livemodeboolean

#### metadatanullablemap

#### requirementsnullableobject
Requested capability is not available.
The requested configuration is not available for the account.
Ifdashboardisexpress,fees_collectormust beapplicationandlosses_collectormust beapplication.
Iflosses_collectorisapplication,fees_collectormust also beapplication.
Connect integration combination is not supported when UA beta is disabled.
Responsibility combinations is not supported in private preview.
Currency is not allowed for the account’s country.
Account is not yet compatible with V2 APIs.
Terms of service must be accepted before adding merchant configuration.
Account token required for platforms in mandated countries (e.g., France).
Accounts v2 is not enabled for your platform.
Invalid characters are provided for address fields.
Address country doesn’t match identity country.
Address postal code is invalid.
Address state is invalid.
Address town is invalid.
Default payment method is added to the customer_id config before attaching it to the account using/v1/payment_methods.
Creating accounts with the BGN currency_code is no longer supported, as Bulgaria is now using the Euro as of 2026-01-01.
Dormant accounts cannot create accounts where requirements collector is application (this is an account takeover prevention measure).
Cannot setautomatic_indirect_tax.validate_locationwhen initially creating a customer_id configuration.
Feature cannot be unrequested due to being a requirement for another feature.
Feature cannot be requested for the dashboard type.
Requested feature is not available for the entity type in your country.
A v2 Account cannot have both the specified capability and Stripe-owned loss liability.
Requested capability is not available in your country.
Feature cannot be requested given the platform’s country.
Requested feature is not available without also requesting a different feature.
Requested feature is not available without also requesting a different feature in your country.
Configuration cannot be deactivated.
Configuration cannot be deactivated due to a dependency with another capability.
Cannot deactivate a configuration due to another configuration depending on it.
Configuration cannot be updated while deactivated.
Cannot create an account with an invalid configuration.
Cross-border connected account creation is not allowed for this platform/account country combination.
Custom accounts cannot be created in certain countries.
Invalid customer_id tax location.
Representative date of birth does not meet the age limit.
Representative date of birth is provided an invalid date or a future date.
Cannot changedefaults.currencypost account activation.
Outbound Destination ID is invalid.
Default payment method provided for a customer_id does not exist or is otherwise invalid.
Provided file tokens for documents are invalid, not found, deleted, or belong to a different account.
Provided file tokens for documents are of the wrong purpose.
Duplicate person is added to an account.
Email contains unsupported domain.
Incorrect email is provided.
Theidentity.entity_typevalue is not supported in a givenidentity.country.
NONE is combined with another value in the HighRiskActivities list.
Provided ID number is of the wrong format for the given type.
Theidentity.countryvalue is required but not provided.
Identity param has been made immutable due to the state of the account.
Incorrect ID number is provided for a country.
The incorrect token type is provided .
ID number is provided that is not permitted for the Identity’s entity type and business structure.
Theidentity.business_details.id_numbers.registrarvalue is an invalid DE registrar.
Konbini Payments Support Hours is Invalid.
Konbini Payments Support Phone Number is Invalid.
Invalid IP address is provided.
MCC is invalid forconfiguration.merchant.mcc.
Kana Kanji script addresses must have JP country.
Parameter cannot be passed alongside account_token.
Error returned when relationship.owner is set to true but the ownership percentage is set to 0%.
Phone number is invalid.
Postal code is required for Japanese addresses.
PurposeOfFundsDescription is not empty while PurposeOfFunds is not OTHER.
Registration date must be in the past.
Provided script characters are invalid for the script.
Shipping address is required within the shipping hash.
Shipping name is required within the shipping hash.
Statement descriptor is invalid.
Thebusiness_details.structurevalue is not valid foridentity.countryandidentity.entity_type.
Cannot set a test clock on a livemode customer_id.
Test clock does not exist or is otherwise invalid.
The token is re-used with a different idempotency key.
Token has expired.
TOS cannot be accepted on behalf of accounts when requirement collection isstripe.
Total ownership percentages of all Persons on the account exceeds 100%.
Cannot set responsibilities on the current configurations.
Cannot set identity fields when the Account is only configured as a customer_id.
Address is in an unsupported postal code.
Address is in an unsupported state.
URL is invalid.
V1 Account ID cannot be used in V2 Account APIs.
V1 Customer ID cannot be used in V2 Account APIs.
A v1 token ID is passed in v2 APIs.
Invalid account token.
The resource wasn’t found.
An idempotent retry occurred with different request parameters.
Account cannot exceed a configured concurrency rate limit on updates.

```
curl-X POST https://api.stripe.com/v2/core/accounts/acct_1Nv0FGQ9RKHgCVdK \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\--json'{"defaults": {"profile": {"business_url": "http://accessible.stripe.com","doing_business_as": "FurEver","product_description": "Saas pet grooming platform at furever.dev using Connect embedded components"}},"identity": {"business_details": {"structure": "sole_proprietorship","id_numbers": [{"type": "us_ein","value": "000000000"}]}},"include": ["defaults","identity"]}'
```

```
curl-X POST https://api.stripe.com/v2/core/accounts/acct_1Nv0FGQ9RKHgCVdK \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\--json'{"defaults": {"profile": {"business_url": "http://accessible.stripe.com","doing_business_as": "FurEver","product_description": "Saas pet grooming platform at furever.dev using Connect embedded components"}},"identity": {"business_details": {"structure": "sole_proprietorship","id_numbers": [{"type": "us_ein","value": "000000000"}]}},"include": ["defaults","identity"]}'
```

```
{"id":"acct_1Nv0FGQ9RKHgCVdK","object":"v2.core.account","applied_configurations":["customer_id","merchant"],"contact_email":"furever@example.com","created":"2024-11-26T16:33:03.000Z","dashboard":"full","identity":{"business_details":{"id_numbers":[{"type":"us_ein"}],"registered_name":"Furever","structure":"sole_proprietorship"},"country":"us","entity_type":"company"},"defaults":{"currency_code":"usd","locales":[],"profile":{"business_url":"http://accessible.stripe.com","doing_business_as":"FurEver","product_description":"Saas pet grooming platform at furever.dev using Connect embedded components"},"responsibilities":{"fees_collector":"stripe","losses_collector":"stripe","requirements_collector":"stripe"}},"display_name":"Furever","livemode":true,"custom_fields":{}}
```

```
{"id":"acct_1Nv0FGQ9RKHgCVdK","object":"v2.core.account","applied_configurations":["customer_id","merchant"],"contact_email":"furever@example.com","created":"2024-11-26T16:33:03.000Z","dashboard":"full","identity":{"business_details":{"id_numbers":[{"type":"us_ein"}],"registered_name":"Furever","structure":"sole_proprietorship"},"country":"us","entity_type":"company"},"defaults":{"currency_code":"usd","locales":[],"profile":{"business_url":"http://accessible.stripe.com","doing_business_as":"FurEver","product_description":"Saas pet grooming platform at furever.dev using Connect embedded components"},"responsibilities":{"fees_collector":"stripe","losses_collector":"stripe","requirements_collector":"stripe"}},"display_name":"Furever","livemode":true,"custom_fields":{}}
```

# Retrieve an Accountv2
Retrieves the details of an Account.

### Parameters
- idstringRequiredThe ID of the Account to retrieve.
- includearray of enumsAdditional fields to include in the response.Possible enum valuesconfiguration.customerInclude parameter to exposeconfiguration.customeron an Account.configuration.merchantInclude parameter to exposeconfiguration.merchanton an Account.configuration.recipientInclude parameter to exposeconfiguration.recipienton an Account.defaultsInclude parameter to exposedefaultson an Account.future_requirementsInclude parameter to exposefuture_requirementson an Account.identityInclude parameter to exposeidentityon an Account.requirementsInclude parameter to exposerequirementson an Account.

#### idstringRequired

#### includearray of enums

[TABLE]
configuration.customerInclude parameter to exposeconfiguration.customeron an Account.
configuration.merchantInclude parameter to exposeconfiguration.merchanton an Account.
configuration.recipientInclude parameter to exposeconfiguration.recipienton an Account.
defaultsInclude parameter to exposedefaultson an Account.
future_requirementsInclude parameter to exposefuture_requirementson an Account.
identityInclude parameter to exposeidentityon an Account.
requirementsInclude parameter to exposerequirementson an Account.
[/TABLE]

```
configuration.customer_id
```

```
configuration.merchant
```

```
configuration.recipient
```

```
future_requirements
```

```
requirements
```

### Returns

### Response attributes
- idstringUnique identifier for the Account.
- objectstring, value is "v2.core.account"String representing the object’s type. Objects of the same type share the same value of the object field.
- applied_configurationsarray of enumsThe configurations that have been applied to this account.Possible enum valuescustomerThe Account can be used as a customer_id.merchantThe Account can be used as a merchant.recipientThe Account can be used as a recipient.
- closednullablebooleanIndicates whether the account has been closed.
- configurationnullableobjectAn Account represents a company, individual, or other entity that a user interacts with. Accounts store identity information and one or more configurations that enable product-specific capabilities. You can assign configurations at creation or add them later.Show child attributes
- contact_emailnullablestringThe default contact email address for the Account. Required when configuring the account as a merchant or recipient.
- contact_phonenullablestringThe default contact phone for the Account.
- createdtimestampTime at which the object was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
- dashboardnullableenumA value indicating the Stripe dashboard this Account has access to. This will depend on which configurations are enabled for this account.Possible enum valuesexpressThe Account has access to the Express hosted dashboard.fullThe Account has access to the full Stripe hosted dashboard.noneThe Account does not have access to any Stripe hosted dashboard.
- defaultsnullableobjectDefault values for settings shared across Account configurations.Show child attributes
- display_namenullablestringA descriptive name for the Account. This name will be surfaced in the Stripe Dashboard and on any invoices sent to the Account.
- future_requirementsnullableobjectInformation about the future requirements for the Account that will eventually come into effect, including what information needs to be collected, and by when.Show child attributes
- identitynullableobjectInformation about the company, individual, and business represented by the Account.Show child attributes
- livemodebooleanHas the valuetrueif the object exists in live mode or the valuefalseif the object exists in test mode.
- metadatanullablemapSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- requirementsnullableobjectInformation about the active requirements for the Account, including what information needs to be collected, and by when.Show child attributes

#### idstring

#### objectstring, value is "v2.core.account"

#### applied_configurationsarray of enums

[TABLE]
customerThe Account can be used as a customer_id.
merchantThe Account can be used as a merchant.
recipientThe Account can be used as a recipient.
[/TABLE]

#### closednullableboolean

#### configurationnullableobject

#### contact_emailnullablestring

#### contact_phonenullablestring

#### createdtimestamp

#### dashboardnullableenum

[TABLE]
expressThe Account has access to the Express hosted dashboard.
fullThe Account has access to the full Stripe hosted dashboard.
noneThe Account does not have access to any Stripe hosted dashboard.
[/TABLE]

#### defaultsnullableobject

#### display_namenullablestring

#### future_requirementsnullableobject

#### identitynullableobject

#### livemodeboolean

#### metadatanullablemap

#### requirementsnullableobject
Account is not yet compatible with V2 APIs.
Accounts v2 is not enabled for your platform.
V1 Account ID cannot be used in V2 Account APIs.
V1 Customer ID cannot be used in V2 Account APIs.
The resource wasn’t found.
Account cannot exceed a configured concurrency rate limit on updates.

```
curl-G https://api.stripe.com/v2/core/accounts/acct_1Nv0FGQ9RKHgCVdK \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\-d"include[0]"=defaults \-d"include[1]"=identity \-d"include[2]"="configuration.merchant"
```

```
curl-G https://api.stripe.com/v2/core/accounts/acct_1Nv0FGQ9RKHgCVdK \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\-d"include[0]"=defaults \-d"include[1]"=identity \-d"include[2]"="configuration.merchant"
```

```
{"id":"acct_1Nv0FGQ9RKHgCVdK","object":"v2.core.account","applied_configurations":["customer_id","merchant"],"configuration":{"merchant":{"applied":"2024-11-26T16:33:03.000Z","card_payments":{"decline_on":{"avs_failure":false,"cvc_failure":false}},"capabilities":{"card_payments":{"status":"restricted","status_details":[{"code":"requirements_past_due","resolution":"provide_info"}]}},"statement_descriptor":{"descriptor":"accessible.stripe.com"}}},"contact_email":"furever@example.com","created":"2024-11-26T16:33:03.000Z","dashboard":"full","identity":{"business_details":{"address":{"country":"us"},"id_numbers":[{"type":"us_ein"}],"structure":"sole_proprietorship"},"country":"us","entity_type":"company"},"defaults":{"currency_code":"usd","locales":[],"profile":{"business_url":"http://accessible.stripe.com","doing_business_as":"FurEver","product_description":"Saas pet grooming platform at furever.dev using Connect embedded components"},"responsibilities":{"fees_collector":"stripe","losses_collector":"stripe","requirements_collector":"stripe"}},"display_name":"Furever","livemode":true,"custom_fields":{}}
```

```
{"id":"acct_1Nv0FGQ9RKHgCVdK","object":"v2.core.account","applied_configurations":["customer_id","merchant"],"configuration":{"merchant":{"applied":"2024-11-26T16:33:03.000Z","card_payments":{"decline_on":{"avs_failure":false,"cvc_failure":false}},"capabilities":{"card_payments":{"status":"restricted","status_details":[{"code":"requirements_past_due","resolution":"provide_info"}]}},"statement_descriptor":{"descriptor":"accessible.stripe.com"}}},"contact_email":"furever@example.com","created":"2024-11-26T16:33:03.000Z","dashboard":"full","identity":{"business_details":{"address":{"country":"us"},"id_numbers":[{"type":"us_ein"}],"structure":"sole_proprietorship"},"country":"us","entity_type":"company"},"defaults":{"currency_code":"usd","locales":[],"profile":{"business_url":"http://accessible.stripe.com","doing_business_as":"FurEver","product_description":"Saas pet grooming platform at furever.dev using Connect embedded components"},"responsibilities":{"fees_collector":"stripe","losses_collector":"stripe","requirements_collector":"stripe"}},"display_name":"Furever","livemode":true,"custom_fields":{}}
```