# accounts

*Source: https://docs.stripe.com/api/accounts*

---

# Accounts
For new integrations, we recommend using theAccounts v2 API, in place of /v1/accounts and /v1/customers to represent a user.
This is an object representing a Stripe account. You can retrieve it to seeproperties on the account like its current requirements or if the account isenabled to make live charges or receive payouts.
For accounts wherecontroller.requirement_collectionisapplication, which includes Custom accounts, the properties below are alwaysreturned.
For accounts wherecontroller.requirement_collectionisstripe, which includes Standard and Express accounts, some properties are only returneduntil you create anAccount LinkorAccount Sessionto start Connect Onboarding. Learn about thedifferences between accounts.

# The Account object

### Attributes
- idstringUnique identifier for the object.
- business_typenullableenumThe business type.Possible enum valuescompanygovernment_entityUS onlyindividualnon_profit
- capabilitiesnullableobjectA hash containing the set of capabilities that was requested for this account and their associated states. Keys are names of capabilities. You can see the full listhere. Values may beactive,inactive, orpending.Show child attributes
- companynullableobjectInformation about the company or business. This property is available for anybusiness_type. After you create anAccount LinkorAccount Session, only a subset of this property is returned for accounts wherecontroller.requirement_collectionisstripe, which includes Standard and Express accounts.Show child attributes
- countrystringThe account’s country.
- emailnullablestringAn email address associated with the account. It’s not used for authentication and Stripe doesn’t market to this field without explicit approval from the platform.
- individualnullableobjectInformation about the person represented by the account. This property is null unlessbusiness_typeis set toindividual. After you create anAccount LinkorAccount Session, only a subset of this property is returned for accounts wherecontroller.requirement_collectionisstripe, which includes Standard and Express accounts.Show child attributes
- metadatanullableobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- requirementsnullableobjectDetails about the requirements for the account, including what information needs to be collected, verified, or reviewed, and by when. After a requirement is collected, verified, or reviewed, it is considered resolved. Most requirements can be addressed programmatically, however, some must be completed through a form or challenge using the Stripe Interface.Learn more about handling requirements.Show child attributes
- tos_acceptanceobjectDetails on theacceptance of the Stripe Services Agreementby the account representative.Show child attributes
- typeenumThe Stripe account type. Can bestandard,express,custom, ornone.Possible enum valuescustomexpressnoneIndicates that the account was created withcontrollerattributes that don’t map to a type ofstandard,express, orcustom.standard

#### idstring

#### business_typenullableenum

[TABLE]
company
government_entityUS only
individual
non_profit
[/TABLE]

```
government_entity
```

#### capabilitiesnullableobject

#### companynullableobject

#### countrystring

#### emailnullablestring

#### individualnullableobject

#### metadatanullableobject

#### requirementsnullableobject

#### tos_acceptanceobject

#### typeenum

[TABLE]
custom
express
noneIndicates that the account was created withcontrollerattributes that don’t map to a type ofstandard,express, orcustom.
standard
[/TABLE]

### More attributesExpand all
- objectstring
- business_profilenullableobject
- charges_enabledboolean
- controllernullableobject
- createdtimestamp
- default_currencystring
- details_submittedboolean
- external_accountsobject
- future_requirementsnullableobject
- groupsnullableobjectPreview featureExpandable
- payouts_enabledboolean
- settingsnullableobject

#### objectstring

#### business_profilenullableobject

#### charges_enabledboolean

#### controllernullableobject

#### createdtimestamp

#### default_currencystring

#### details_submittedboolean

#### external_accountsobject

#### future_requirementsnullableobject

#### groupsnullableobjectPreview featureExpandable

#### payouts_enabledboolean

#### settingsnullableobject

```
{"id":"acct_1Nv0FGQ9RKHgCVdK","object":"account","business_profile":{"annual_revenue":null,"estimated_worker_count":null,"mcc":null,"name":null,"product_description":null,"support_address":null,"support_email":null,"support_phone":null,"support_url":null,"url":null},"business_type":null,"capabilities":{},"charges_enabled":false,"controller":{"fees":{"payer":"application"},"is_controller":true,"losses":{"payments":"application"},"requirement_collection":"stripe","stripe_dashboard":{"type":"express"},"type":"application"},"country":"US","created":1695830751,"default_currency":"usd","details_submitted":false,"email":"jenny.rosen@example.com","external_accounts":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/accounts/acct_1Nv0FGQ9RKHgCVdK/external_accounts"},"future_requirements":{"alternatives":[],"current_deadline":null,"currently_due":[],"disabled_reason":null,"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"login_links":{"object":"list","total_count":0,"has_more":false,"url":"/v1/accounts/acct_1Nv0FGQ9RKHgCVdK/login_links","data":[]},"metadata":{},"payouts_enabled":false,"requirements":{"alternatives":[],"current_deadline":null,"currently_due":["business_profile.mcc","business_profile.url","business_type","external_account","representative.first_name","representative.last_name","tos_acceptance.date","tos_acceptance.ip"],"disabled_reason":"requirements.past_due","errors":[],"eventually_due":["business_profile.mcc","business_profile.url","business_type","external_account","representative.first_name","representative.last_name","tos_acceptance.date","tos_acceptance.ip"],"past_due":["business_profile.mcc","business_profile.url","business_type","external_account","representative.first_name","representative.last_name","tos_acceptance.date","tos_acceptance.ip"],"pending_verification":[]},"settings":{"bacs_debit_payments":{"display_name":null,"service_user_number":null},"branding":{"icon":null,"logo":null,"primary_color":null,"secondary_color":null},"card_issuing":{"tos_acceptance":{"date":null,"ip":null}},"card_payments":{"decline_on":{"avs_failure":false,"cvc_failure":false},"statement_descriptor_prefix":null,"statement_descriptor_prefix_kanji":null,"statement_descriptor_prefix_kana":null},"dashboard":{"display_name":null,"timezone":"Etc/UTC"},"invoices":{"default_account_tax_ids":null},"payments":{"statement_descriptor":null,"statement_descriptor_kana":null,"statement_descriptor_kanji":null},"payouts":{"debit_negative_balances":true,"schedule":{"delay_days":2,"interval":"daily"},"statement_descriptor":null},"sepa_debit_payments":{}},"tos_acceptance":{"date":null,"ip":null,"user_agent":null},"type":"none"}
```

```
{"id":"acct_1Nv0FGQ9RKHgCVdK","object":"account","business_profile":{"annual_revenue":null,"estimated_worker_count":null,"mcc":null,"name":null,"product_description":null,"support_address":null,"support_email":null,"support_phone":null,"support_url":null,"url":null},"business_type":null,"capabilities":{},"charges_enabled":false,"controller":{"fees":{"payer":"application"},"is_controller":true,"losses":{"payments":"application"},"requirement_collection":"stripe","stripe_dashboard":{"type":"express"},"type":"application"},"country":"US","created":1695830751,"default_currency":"usd","details_submitted":false,"email":"jenny.rosen@example.com","external_accounts":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/accounts/acct_1Nv0FGQ9RKHgCVdK/external_accounts"},"future_requirements":{"alternatives":[],"current_deadline":null,"currently_due":[],"disabled_reason":null,"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"login_links":{"object":"list","total_count":0,"has_more":false,"url":"/v1/accounts/acct_1Nv0FGQ9RKHgCVdK/login_links","data":[]},"metadata":{},"payouts_enabled":false,"requirements":{"alternatives":[],"current_deadline":null,"currently_due":["business_profile.mcc","business_profile.url","business_type","external_account","representative.first_name","representative.last_name","tos_acceptance.date","tos_acceptance.ip"],"disabled_reason":"requirements.past_due","errors":[],"eventually_due":["business_profile.mcc","business_profile.url","business_type","external_account","representative.first_name","representative.last_name","tos_acceptance.date","tos_acceptance.ip"],"past_due":["business_profile.mcc","business_profile.url","business_type","external_account","representative.first_name","representative.last_name","tos_acceptance.date","tos_acceptance.ip"],"pending_verification":[]},"settings":{"bacs_debit_payments":{"display_name":null,"service_user_number":null},"branding":{"icon":null,"logo":null,"primary_color":null,"secondary_color":null},"card_issuing":{"tos_acceptance":{"date":null,"ip":null}},"card_payments":{"decline_on":{"avs_failure":false,"cvc_failure":false},"statement_descriptor_prefix":null,"statement_descriptor_prefix_kanji":null,"statement_descriptor_prefix_kana":null},"dashboard":{"display_name":null,"timezone":"Etc/UTC"},"invoices":{"default_account_tax_ids":null},"payments":{"statement_descriptor":null,"statement_descriptor_kana":null,"statement_descriptor_kanji":null},"payouts":{"debit_negative_balances":true,"schedule":{"delay_days":2,"interval":"daily"},"statement_descriptor":null},"sepa_debit_payments":{}},"tos_acceptance":{"date":null,"ip":null,"user_agent":null},"type":"none"}
```

# Create an account
WithConnect, you can create Stripe accounts for your users.To do this, you’ll first need toregister your platform.
If you’ve already collected information for your connected accounts, youcan prefill that informationwhencreating the account. Connect Onboarding won’t ask for the prefilled information during account onboarding.You can prefill any information on the account.

### Parameters
- business_typeenumThe business type. Once you create anAccount LinkorAccount Session, this property can only be updated for accounts wherecontroller.requirement_collectionisapplication, which includes Custom accounts.Possible enum valuescompanygovernment_entityUS onlyindividualnon_profit
- capabilitiesobjectRequired conditionallyEach key of the dictionary represents a capability, and each capabilitymaps to its settings (for example, whether it has been requested or not). Eachcapability is inactive until you have provided its specificrequirements and Stripe has verified them. An account might have someof its requested capabilities be active and some be inactive.Required whenaccount.controller.stripe_dashboard.typeisnone, which includes Custom accounts.Show child parameters
- companyobjectInformation about the company or business. This field is available for anybusiness_type. Once you create anAccount LinkorAccount Session, this property can only be updated for accounts wherecontroller.requirement_collectionisapplication, which includes Custom accounts.Show child parameters
- controllerobjectA hash of configuration describing the account controller’s attributes.Show child parameters
- countrystringdefault is your own countryThe country in which the account holder resides, or in which the business is legally established. This should be an ISO 3166-1 alpha-2 country code. For example, if you are in the United States and the business for which you’re creating an account is legally represented in Canada, you would useCAas the country for the account being created. Available countries includeStripe’s global marketsas well as countries wherecross-border payoutsare supported.
- emailstringThe email address of the account holder. This is only to make the account easier to identify to you. Ifcontroller.requirement_collectionisapplication, which includes Custom accounts, Stripe doesn’t email the account without your consent.The maximum length is 800 characters.
- individualobjectInformation about the person represented by the account. This field is null unlessbusiness_typeis set toindividual. Once you create anAccount LinkorAccount Session, this property can only be updated for accounts wherecontroller.requirement_collectionisapplication, which includes Custom accounts.Show child parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- tos_acceptanceobjectDetails on the account’s acceptance of theStripe Services Agreement. This property can only be updated for accounts wherecontroller.requirement_collectionisapplication, which includes Custom accounts. This property defaults to afullservice agreement when empty.Show child parameters
- typeenumThe type of Stripe account to create. May be one ofcustom,expressorstandard.Possible enum valuescustomexpressstandard

#### business_typeenum

[TABLE]
company
government_entityUS only
individual
non_profit
[/TABLE]

```
government_entity
```

#### capabilitiesobjectRequired conditionally

#### companyobject

#### controllerobject

#### countrystringdefault is your own country

#### emailstring

#### individualobject

#### metadataobject

#### tos_acceptanceobject

#### typeenum

[TABLE]
custom
express
standard
[/TABLE]

### More parametersExpand all
- account_tokenstring
- business_profileobject
- default_currencyenum
- documentsobject
- external_accountstring
- groupsobjectPreview feature
- settingsobject

#### account_tokenstring

#### business_profileobject

#### default_currencyenum

#### documentsobject

#### external_accountstring

#### groupsobjectPreview feature

#### settingsobject

### Returns
Returns anAccountobject if the call succeeds.

```
curlhttps://api.stripe.com/v1/accounts \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d country=US \--data-urlencode email="jenny.rosen@example.com"\-d"controller[fees][payer]"=application \-d"controller[losses][payments]"=application \-d"controller[stripe_dashboard][type]"=express
```

```
curlhttps://api.stripe.com/v1/accounts \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d country=US \--data-urlencode email="jenny.rosen@example.com"\-d"controller[fees][payer]"=application \-d"controller[losses][payments]"=application \-d"controller[stripe_dashboard][type]"=express
```

```
{"id":"acct_1Nv0FGQ9RKHgCVdK","object":"account","business_profile":{"annual_revenue":null,"estimated_worker_count":null,"mcc":null,"name":null,"product_description":null,"support_address":null,"support_email":null,"support_phone":null,"support_url":null,"url":null},"business_type":null,"capabilities":{},"charges_enabled":false,"controller":{"fees":{"payer":"application"},"is_controller":true,"losses":{"payments":"application"},"requirement_collection":"stripe","stripe_dashboard":{"type":"express"},"type":"application"},"country":"US","created":1695830751,"default_currency":"usd","details_submitted":false,"email":"jenny.rosen@example.com","external_accounts":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/accounts/acct_1Nv0FGQ9RKHgCVdK/external_accounts"},"future_requirements":{"alternatives":[],"current_deadline":null,"currently_due":[],"disabled_reason":null,"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"login_links":{"object":"list","total_count":0,"has_more":false,"url":"/v1/accounts/acct_1Nv0FGQ9RKHgCVdK/login_links","data":[]},"metadata":{},"payouts_enabled":false,"requirements":{"alternatives":[],"current_deadline":null,"currently_due":["business_profile.mcc","business_profile.url","business_type","external_account","representative.first_name","representative.last_name","tos_acceptance.date","tos_acceptance.ip"],"disabled_reason":"requirements.past_due","errors":[],"eventually_due":["business_profile.mcc","business_profile.url","business_type","external_account","representative.first_name","representative.last_name","tos_acceptance.date","tos_acceptance.ip"],"past_due":["business_profile.mcc","business_profile.url","business_type","external_account","representative.first_name","representative.last_name","tos_acceptance.date","tos_acceptance.ip"],"pending_verification":[]},"settings":{"bacs_debit_payments":{"display_name":null,"service_user_number":null},"branding":{"icon":null,"logo":null,"primary_color":null,"secondary_color":null},"card_issuing":{"tos_acceptance":{"date":null,"ip":null}},"card_payments":{"decline_on":{"avs_failure":false,"cvc_failure":false},"statement_descriptor_prefix":null,"statement_descriptor_prefix_kanji":null,"statement_descriptor_prefix_kana":null},"dashboard":{"display_name":null,"timezone":"Etc/UTC"},"invoices":{"default_account_tax_ids":null},"payments":{"statement_descriptor":null,"statement_descriptor_kana":null,"statement_descriptor_kanji":null},"payouts":{"debit_negative_balances":true,"schedule":{"delay_days":2,"interval":"daily"},"statement_descriptor":null},"sepa_debit_payments":{}},"tos_acceptance":{"date":null,"ip":null,"user_agent":null},"type":"none"}
```

```
{"id":"acct_1Nv0FGQ9RKHgCVdK","object":"account","business_profile":{"annual_revenue":null,"estimated_worker_count":null,"mcc":null,"name":null,"product_description":null,"support_address":null,"support_email":null,"support_phone":null,"support_url":null,"url":null},"business_type":null,"capabilities":{},"charges_enabled":false,"controller":{"fees":{"payer":"application"},"is_controller":true,"losses":{"payments":"application"},"requirement_collection":"stripe","stripe_dashboard":{"type":"express"},"type":"application"},"country":"US","created":1695830751,"default_currency":"usd","details_submitted":false,"email":"jenny.rosen@example.com","external_accounts":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/accounts/acct_1Nv0FGQ9RKHgCVdK/external_accounts"},"future_requirements":{"alternatives":[],"current_deadline":null,"currently_due":[],"disabled_reason":null,"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"login_links":{"object":"list","total_count":0,"has_more":false,"url":"/v1/accounts/acct_1Nv0FGQ9RKHgCVdK/login_links","data":[]},"metadata":{},"payouts_enabled":false,"requirements":{"alternatives":[],"current_deadline":null,"currently_due":["business_profile.mcc","business_profile.url","business_type","external_account","representative.first_name","representative.last_name","tos_acceptance.date","tos_acceptance.ip"],"disabled_reason":"requirements.past_due","errors":[],"eventually_due":["business_profile.mcc","business_profile.url","business_type","external_account","representative.first_name","representative.last_name","tos_acceptance.date","tos_acceptance.ip"],"past_due":["business_profile.mcc","business_profile.url","business_type","external_account","representative.first_name","representative.last_name","tos_acceptance.date","tos_acceptance.ip"],"pending_verification":[]},"settings":{"bacs_debit_payments":{"display_name":null,"service_user_number":null},"branding":{"icon":null,"logo":null,"primary_color":null,"secondary_color":null},"card_issuing":{"tos_acceptance":{"date":null,"ip":null}},"card_payments":{"decline_on":{"avs_failure":false,"cvc_failure":false},"statement_descriptor_prefix":null,"statement_descriptor_prefix_kanji":null,"statement_descriptor_prefix_kana":null},"dashboard":{"display_name":null,"timezone":"Etc/UTC"},"invoices":{"default_account_tax_ids":null},"payments":{"statement_descriptor":null,"statement_descriptor_kana":null,"statement_descriptor_kanji":null},"payouts":{"debit_negative_balances":true,"schedule":{"delay_days":2,"interval":"daily"},"statement_descriptor":null},"sepa_debit_payments":{}},"tos_acceptance":{"date":null,"ip":null,"user_agent":null},"type":"none"}
```

# Update an account
Updates aconnected accountby setting the values of the parameters passed. Any parameters not provided areleft unchanged.
For accounts wherecontroller.requirement_collectionisapplication, which includes Custom accounts, you can update any information on the account.
For accounts wherecontroller.requirement_collectionisstripe, which includes Standard and Express accounts, you can update all information until you createanAccount LinkorAccount Sessionto start Connect onboarding,after which some properties can no longer be updated.
To update your own account, use theDashboard. Refer to ourConnectdocumentation to learn more about updating accounts.

### Parameters
- business_typeenumThe business type. Once you create anAccount LinkorAccount Session, this property can only be updated for accounts wherecontroller.requirement_collectionisapplication, which includes Custom accounts.Possible enum valuescompanygovernment_entityUS onlyindividualnon_profit
- capabilitiesobjectEach key of the dictionary represents a capability, and each capabilitymaps to its settings (for example, whether it has been requested or not). Eachcapability is inactive until you have provided its specificrequirements and Stripe has verified them. An account might have someof its requested capabilities be active and some be inactive.Required whenaccount.controller.stripe_dashboard.typeisnone, which includes Custom accounts.Show child parameters
- companyobjectInformation about the company or business. This field is available for anybusiness_type. Once you create anAccount LinkorAccount Session, this property can only be updated for accounts wherecontroller.requirement_collectionisapplication, which includes Custom accounts.Show child parameters
- emailstringThe email address of the account holder. This is only to make the account easier to identify to you. Ifcontroller.requirement_collectionisapplication, which includes Custom accounts, Stripe doesn’t email the account without your consent.The maximum length is 800 characters.
- individualobjectInformation about the person represented by the account. This field is null unlessbusiness_typeis set toindividual. Once you create anAccount LinkorAccount Session, this property can only be updated for accounts wherecontroller.requirement_collectionisapplication, which includes Custom accounts.Show child parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- tos_acceptanceobjectDetails on the account’s acceptance of theStripe Services Agreement. This property can only be updated for accounts wherecontroller.requirement_collectionisapplication, which includes Custom accounts. This property defaults to afullservice agreement when empty.Show child parameters

#### business_typeenum

[TABLE]
company
government_entityUS only
individual
non_profit
[/TABLE]

```
government_entity
```

#### capabilitiesobject

#### companyobject

#### emailstring

#### individualobject

#### metadataobject

#### tos_acceptanceobject

### More parametersExpand all
- account_tokenstring
- business_profileobject
- default_currencyenum
- documentsobject
- external_accountstring
- groupsobjectPreview feature
- settingsobject

#### account_tokenstring

#### business_profileobject

#### default_currencyenum

#### documentsobject

#### external_accountstring

#### groupsobjectPreview feature

#### settingsobject

### Returns
Returns anAccountobject if the call succeeds. If the account ID does not exist or another issue occurs, this callraisesan error. Some validations will not raise an error but will instead populate therequirements.errorsarray.

```
requirements.errors
```

```
curlhttps://api.stripe.com/v1/accounts/acct_1Nv0FGQ9RKHgCVdK \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/accounts/acct_1Nv0FGQ9RKHgCVdK \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
{"id":"acct_1Nv0FGQ9RKHgCVdK","object":"account","business_profile":{"annual_revenue":null,"estimated_worker_count":null,"mcc":null,"name":null,"product_description":null,"support_address":null,"support_email":null,"support_phone":null,"support_url":null,"url":null},"business_type":null,"capabilities":{},"charges_enabled":false,"controller":{"fees":{"payer":"application"},"is_controller":true,"losses":{"payments":"application"},"requirement_collection":"stripe","stripe_dashboard":{"type":"express"},"type":"application"},"country":"US","created":1695830751,"default_currency":"usd","details_submitted":false,"email":"jenny.rosen@example.com","external_accounts":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/accounts/acct_1Nv0FGQ9RKHgCVdK/external_accounts"},"future_requirements":{"alternatives":[],"current_deadline":null,"currently_due":[],"disabled_reason":null,"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"login_links":{"object":"list","total_count":0,"has_more":false,"url":"/v1/accounts/acct_1Nv0FGQ9RKHgCVdK/login_links","data":[]},"metadata":{"order_id":"6735"},"payouts_enabled":false,"requirements":{"alternatives":[],"current_deadline":null,"currently_due":["business_profile.mcc","business_profile.url","business_type","external_account","representative.first_name","representative.last_name","tos_acceptance.date","tos_acceptance.ip"],"disabled_reason":"requirements.past_due","errors":[],"eventually_due":["business_profile.mcc","business_profile.url","business_type","external_account","representative.first_name","representative.last_name","tos_acceptance.date","tos_acceptance.ip"],"past_due":["business_profile.mcc","business_profile.url","business_type","external_account","representative.first_name","representative.last_name","tos_acceptance.date","tos_acceptance.ip"],"pending_verification":[]},"settings":{"bacs_debit_payments":{"display_name":null,"service_user_number":null},"branding":{"icon":null,"logo":null,"primary_color":null,"secondary_color":null},"card_issuing":{"tos_acceptance":{"date":null,"ip":null}},"card_payments":{"decline_on":{"avs_failure":false,"cvc_failure":false},"statement_descriptor_prefix":null,"statement_descriptor_prefix_kanji":null,"statement_descriptor_prefix_kana":null},"dashboard":{"display_name":null,"timezone":"Etc/UTC"},"invoices":{"default_account_tax_ids":null},"payments":{"statement_descriptor":null,"statement_descriptor_kana":null,"statement_descriptor_kanji":null},"payouts":{"debit_negative_balances":true,"schedule":{"delay_days":2,"interval":"daily"},"statement_descriptor":null},"sepa_debit_payments":{}},"tos_acceptance":{"date":null,"ip":null,"user_agent":null},"type":"none"}
```

```
{"id":"acct_1Nv0FGQ9RKHgCVdK","object":"account","business_profile":{"annual_revenue":null,"estimated_worker_count":null,"mcc":null,"name":null,"product_description":null,"support_address":null,"support_email":null,"support_phone":null,"support_url":null,"url":null},"business_type":null,"capabilities":{},"charges_enabled":false,"controller":{"fees":{"payer":"application"},"is_controller":true,"losses":{"payments":"application"},"requirement_collection":"stripe","stripe_dashboard":{"type":"express"},"type":"application"},"country":"US","created":1695830751,"default_currency":"usd","details_submitted":false,"email":"jenny.rosen@example.com","external_accounts":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/accounts/acct_1Nv0FGQ9RKHgCVdK/external_accounts"},"future_requirements":{"alternatives":[],"current_deadline":null,"currently_due":[],"disabled_reason":null,"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"login_links":{"object":"list","total_count":0,"has_more":false,"url":"/v1/accounts/acct_1Nv0FGQ9RKHgCVdK/login_links","data":[]},"metadata":{"order_id":"6735"},"payouts_enabled":false,"requirements":{"alternatives":[],"current_deadline":null,"currently_due":["business_profile.mcc","business_profile.url","business_type","external_account","representative.first_name","representative.last_name","tos_acceptance.date","tos_acceptance.ip"],"disabled_reason":"requirements.past_due","errors":[],"eventually_due":["business_profile.mcc","business_profile.url","business_type","external_account","representative.first_name","representative.last_name","tos_acceptance.date","tos_acceptance.ip"],"past_due":["business_profile.mcc","business_profile.url","business_type","external_account","representative.first_name","representative.last_name","tos_acceptance.date","tos_acceptance.ip"],"pending_verification":[]},"settings":{"bacs_debit_payments":{"display_name":null,"service_user_number":null},"branding":{"icon":null,"logo":null,"primary_color":null,"secondary_color":null},"card_issuing":{"tos_acceptance":{"date":null,"ip":null}},"card_payments":{"decline_on":{"avs_failure":false,"cvc_failure":false},"statement_descriptor_prefix":null,"statement_descriptor_prefix_kanji":null,"statement_descriptor_prefix_kana":null},"dashboard":{"display_name":null,"timezone":"Etc/UTC"},"invoices":{"default_account_tax_ids":null},"payments":{"statement_descriptor":null,"statement_descriptor_kana":null,"statement_descriptor_kanji":null},"payouts":{"debit_negative_balances":true,"schedule":{"delay_days":2,"interval":"daily"},"statement_descriptor":null},"sepa_debit_payments":{}},"tos_acceptance":{"date":null,"ip":null,"user_agent":null},"type":"none"}
```

# Retrieve account
Retrieves the details of an account.

### Parameters
Noparameters.

### Returns
Returns anAccountobject if the call succeeds. If the account ID does not exist, this callraisesan error.

```
curlhttps://api.stripe.com/v1/accounts/acct_1Nv0FGQ9RKHgCVdK \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/accounts/acct_1Nv0FGQ9RKHgCVdK \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"acct_1Nv0FGQ9RKHgCVdK","object":"account","business_profile":{"annual_revenue":null,"estimated_worker_count":null,"mcc":null,"name":null,"product_description":null,"support_address":null,"support_email":null,"support_phone":null,"support_url":null,"url":null},"business_type":null,"capabilities":{},"charges_enabled":false,"controller":{"fees":{"payer":"application"},"is_controller":true,"losses":{"payments":"application"},"requirement_collection":"stripe","stripe_dashboard":{"type":"express"},"type":"application"},"country":"US","created":1695830751,"default_currency":"usd","details_submitted":false,"email":"jenny.rosen@example.com","external_accounts":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/accounts/acct_1Nv0FGQ9RKHgCVdK/external_accounts"},"future_requirements":{"alternatives":[],"current_deadline":null,"currently_due":[],"disabled_reason":null,"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"login_links":{"object":"list","total_count":0,"has_more":false,"url":"/v1/accounts/acct_1Nv0FGQ9RKHgCVdK/login_links","data":[]},"metadata":{},"payouts_enabled":false,"requirements":{"alternatives":[],"current_deadline":null,"currently_due":["business_profile.mcc","business_profile.url","business_type","external_account","representative.first_name","representative.last_name","tos_acceptance.date","tos_acceptance.ip"],"disabled_reason":"requirements.past_due","errors":[],"eventually_due":["business_profile.mcc","business_profile.url","business_type","external_account","representative.first_name","representative.last_name","tos_acceptance.date","tos_acceptance.ip"],"past_due":["business_profile.mcc","business_profile.url","business_type","external_account","representative.first_name","representative.last_name","tos_acceptance.date","tos_acceptance.ip"],"pending_verification":[]},"settings":{"bacs_debit_payments":{"display_name":null,"service_user_number":null},"branding":{"icon":null,"logo":null,"primary_color":null,"secondary_color":null},"card_issuing":{"tos_acceptance":{"date":null,"ip":null}},"card_payments":{"decline_on":{"avs_failure":false,"cvc_failure":false},"statement_descriptor_prefix":null,"statement_descriptor_prefix_kanji":null,"statement_descriptor_prefix_kana":null},"dashboard":{"display_name":null,"timezone":"Etc/UTC"},"invoices":{"default_account_tax_ids":null},"payments":{"statement_descriptor":null,"statement_descriptor_kana":null,"statement_descriptor_kanji":null},"payouts":{"debit_negative_balances":true,"schedule":{"delay_days":2,"interval":"daily"},"statement_descriptor":null},"sepa_debit_payments":{}},"tos_acceptance":{"date":null,"ip":null,"user_agent":null},"type":"none"}
```

```
{"id":"acct_1Nv0FGQ9RKHgCVdK","object":"account","business_profile":{"annual_revenue":null,"estimated_worker_count":null,"mcc":null,"name":null,"product_description":null,"support_address":null,"support_email":null,"support_phone":null,"support_url":null,"url":null},"business_type":null,"capabilities":{},"charges_enabled":false,"controller":{"fees":{"payer":"application"},"is_controller":true,"losses":{"payments":"application"},"requirement_collection":"stripe","stripe_dashboard":{"type":"express"},"type":"application"},"country":"US","created":1695830751,"default_currency":"usd","details_submitted":false,"email":"jenny.rosen@example.com","external_accounts":{"object":"list","data":[],"has_more":false,"total_count":0,"url":"/v1/accounts/acct_1Nv0FGQ9RKHgCVdK/external_accounts"},"future_requirements":{"alternatives":[],"current_deadline":null,"currently_due":[],"disabled_reason":null,"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"login_links":{"object":"list","total_count":0,"has_more":false,"url":"/v1/accounts/acct_1Nv0FGQ9RKHgCVdK/login_links","data":[]},"metadata":{},"payouts_enabled":false,"requirements":{"alternatives":[],"current_deadline":null,"currently_due":["business_profile.mcc","business_profile.url","business_type","external_account","representative.first_name","representative.last_name","tos_acceptance.date","tos_acceptance.ip"],"disabled_reason":"requirements.past_due","errors":[],"eventually_due":["business_profile.mcc","business_profile.url","business_type","external_account","representative.first_name","representative.last_name","tos_acceptance.date","tos_acceptance.ip"],"past_due":["business_profile.mcc","business_profile.url","business_type","external_account","representative.first_name","representative.last_name","tos_acceptance.date","tos_acceptance.ip"],"pending_verification":[]},"settings":{"bacs_debit_payments":{"display_name":null,"service_user_number":null},"branding":{"icon":null,"logo":null,"primary_color":null,"secondary_color":null},"card_issuing":{"tos_acceptance":{"date":null,"ip":null}},"card_payments":{"decline_on":{"avs_failure":false,"cvc_failure":false},"statement_descriptor_prefix":null,"statement_descriptor_prefix_kanji":null,"statement_descriptor_prefix_kana":null},"dashboard":{"display_name":null,"timezone":"Etc/UTC"},"invoices":{"default_account_tax_ids":null},"payments":{"statement_descriptor":null,"statement_descriptor_kana":null,"statement_descriptor_kanji":null},"payouts":{"debit_negative_balances":true,"schedule":{"delay_days":2,"interval":"daily"},"statement_descriptor":null},"sepa_debit_payments":{}},"tos_acceptance":{"date":null,"ip":null,"user_agent":null},"type":"none"}
```