# treasury/financial_accounts

*Source: https://docs.stripe.com/api/treasury/financial_accounts*

---

# Financial Accounts
Stripe Treasury provides users with a container for money called a FinancialAccount that is separate from their Payments balance.FinancialAccounts serve as the source and destination of Treasury’s money movement APIs.

# The FinancialAccount object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- active_featuresarray of enumsThe array of paths to active Features in the Features hash.
- balanceobjectThe single multi-currency_code balance of the FinancialAccount. Positive values represent money that belongs to the user while negative values represent funds the user owes. Currently, FinancialAccounts can only carry balances in USD.Show child attributes
- countrystringTwo-letter country code (ISO 3166-1 alpha-2).
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- featuresnullableobjectExpandableThe features and their statuses for this FinancialAccount.Show child attributes
- financial_addressesarray of objectsThe set of credentials that resolve to a FinancialAccount.Show child attributes
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- metadatanullableobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- nicknamenullablestringPreview featureThe nickname for the FinancialAccount.
- pending_featuresarray of enumsThe array of paths to pending Features in the Features hash.
- platform_restrictionsnullableobjectThe set of functionalities that the platform can restrict on the FinancialAccount.Show child attributes
- restricted_featuresarray of enumsThe array of paths to restricted Features in the Features hash.
- statusenumStatus of this FinancialAccount.Possible enum valuesclosedThe FinancialAccount is closed.openThe FinancialAccount is open.
- status_detailsobjectDetails related to the status of this FinancialAccount.Show child attributes
- supported_currenciesarray of enumsThe currencies the FinancialAccount can hold a balance in. Three-letterISO currency_code code, in lowercase.

#### idstring

#### objectstring

#### active_featuresarray of enums

#### balanceobject

#### countrystring

#### createdtimestamp

#### featuresnullableobjectExpandable

#### financial_addressesarray of objects

#### livemodeboolean

#### metadatanullableobject

#### nicknamenullablestringPreview feature

#### pending_featuresarray of enums

#### platform_restrictionsnullableobject

#### restricted_featuresarray of enums

#### statusenum

[TABLE]
closedThe FinancialAccount is closed.
openThe FinancialAccount is open.
[/TABLE]

#### status_detailsobject

#### supported_currenciesarray of enums

```
{"id":"fa_1MtZmL2eZvKYlo2Cer6cdwEC","object":"treasury.financial_account","active_features":["financial_addresses.aba","outbound_payments.ach","outbound_payments.us_domestic_wire"],"balance":{"cash":{"usd":0},"inbound_pending":{"usd":0},"outbound_pending":{"usd":0}},"country":"US","created":1680714349,"financial_addresses":[{"aba":{"account_holder_name":"Jenny Rosen","account_number_last4":"7890","bank_name":"STRIPE TEST BANK","routing_number":"0000000001"},"supported_networks":["ach","us_domestic_wire"],"type":"aba"}],"livemode":true,"custom_fields":null,"pending_features":[],"restricted_features":[],"status":"open","status_details":{"closed":null},"supported_currencies":["usd"],"features":{}}
```

```
{"id":"fa_1MtZmL2eZvKYlo2Cer6cdwEC","object":"treasury.financial_account","active_features":["financial_addresses.aba","outbound_payments.ach","outbound_payments.us_domestic_wire"],"balance":{"cash":{"usd":0},"inbound_pending":{"usd":0},"outbound_pending":{"usd":0}},"country":"US","created":1680714349,"financial_addresses":[{"aba":{"account_holder_name":"Jenny Rosen","account_number_last4":"7890","bank_name":"STRIPE TEST BANK","routing_number":"0000000001"},"supported_networks":["ach","us_domestic_wire"],"type":"aba"}],"livemode":true,"custom_fields":null,"pending_features":[],"restricted_features":[],"status":"open","status_details":{"closed":null},"supported_currencies":["usd"],"features":{}}
```

# Create a FinancialAccount
Creates a new FinancialAccount. Each connected account can have up to three FinancialAccounts by default.

### Parameters
- supported_currenciesarray of stringsRequiredThe currencies the FinancialAccount can hold a balance in.
- featuresobjectEncodes whether a FinancialAccount has access to a particular feature. Stripe or the platform can control features via the requested field.Show child parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- nicknamestringThe nickname for the FinancialAccount.
- platform_restrictionsobjectThe set of functionalities that the platform can restrict on the FinancialAccount.Show child parameters

#### supported_currenciesarray of stringsRequired

#### featuresobject

#### metadataobject

#### nicknamestring

#### platform_restrictionsobject

### Returns
Returns a FinancialAccount object.

```
curlhttps://api.stripe.com/v1/treasury/financial_accounts \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"supported_currencies[]"=usd
```

```
curlhttps://api.stripe.com/v1/treasury/financial_accounts \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"supported_currencies[]"=usd
```

```
{"id":"fa_1MtZmL2eZvKYlo2Cer6cdwEC","object":"treasury.financial_account","active_features":["financial_addresses.aba","outbound_payments.ach","outbound_payments.us_domestic_wire"],"balance":{"cash":{"usd":0},"inbound_pending":{"usd":0},"outbound_pending":{"usd":0}},"country":"US","created":1680714349,"financial_addresses":[{"aba":{"account_holder_name":"Jenny Rosen","account_number_last4":"7890","bank_name":"STRIPE TEST BANK","routing_number":"0000000001"},"supported_networks":["ach","us_domestic_wire"],"type":"aba"}],"livemode":true,"custom_fields":null,"pending_features":[],"restricted_features":[],"status":"open","status_details":{"closed":null},"supported_currencies":["usd"],"features":{}}
```

```
{"id":"fa_1MtZmL2eZvKYlo2Cer6cdwEC","object":"treasury.financial_account","active_features":["financial_addresses.aba","outbound_payments.ach","outbound_payments.us_domestic_wire"],"balance":{"cash":{"usd":0},"inbound_pending":{"usd":0},"outbound_pending":{"usd":0}},"country":"US","created":1680714349,"financial_addresses":[{"aba":{"account_holder_name":"Jenny Rosen","account_number_last4":"7890","bank_name":"STRIPE TEST BANK","routing_number":"0000000001"},"supported_networks":["ach","us_domestic_wire"],"type":"aba"}],"livemode":true,"custom_fields":null,"pending_features":[],"restricted_features":[],"status":"open","status_details":{"closed":null},"supported_currencies":["usd"],"features":{}}
```

# Update a FinancialAccount
Updates the details of a FinancialAccount.

### Parameters
- featuresobjectEncodes whether a FinancialAccount has access to a particular feature, with a status enum and associatedstatus_details. Stripe or the platform may control features via the requested field.Show child parameters
- forwarding_settingsobjectA different bank account where funds can be deposited/debited in order to get the closing FA’s balance to $0Show child parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- nicknamestringThe nickname for the FinancialAccount.
- platform_restrictionsobjectThe set of functionalities that the platform can restrict on the FinancialAccount.Show child parameters

#### featuresobject

#### forwarding_settingsobject

#### metadataobject

#### nicknamestring

#### platform_restrictionsobject

### Returns
Returns a FinancialAccount object.

```
curlhttps://api.stripe.com/v1/treasury/financial_accounts/fa_1MtZmL2eZvKYlo2Cer6cdwEC \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/treasury/financial_accounts/fa_1MtZmL2eZvKYlo2Cer6cdwEC \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"custom_fields[order_id]"=6735
```

```
{"id":"fa_1MtZmL2eZvKYlo2Cer6cdwEC","object":"treasury.financial_account","active_features":["financial_addresses.aba","outbound_payments.ach","outbound_payments.us_domestic_wire"],"balance":{"cash":{"usd":0},"inbound_pending":{"usd":0},"outbound_pending":{"usd":0}},"country":"US","created":1680714349,"financial_addresses":[{"aba":{"account_holder_name":"Jenny Rosen","account_number_last4":"7890","bank_name":"STRIPE TEST BANK","routing_number":"0000000001"},"supported_networks":["ach","us_domestic_wire"],"type":"aba"}],"livemode":true,"custom_fields":{"order_id":"6735"},"pending_features":[],"restricted_features":[],"status":"open","status_details":{"closed":null},"supported_currencies":["usd"],"features":{}}
```

```
{"id":"fa_1MtZmL2eZvKYlo2Cer6cdwEC","object":"treasury.financial_account","active_features":["financial_addresses.aba","outbound_payments.ach","outbound_payments.us_domestic_wire"],"balance":{"cash":{"usd":0},"inbound_pending":{"usd":0},"outbound_pending":{"usd":0}},"country":"US","created":1680714349,"financial_addresses":[{"aba":{"account_holder_name":"Jenny Rosen","account_number_last4":"7890","bank_name":"STRIPE TEST BANK","routing_number":"0000000001"},"supported_networks":["ach","us_domestic_wire"],"type":"aba"}],"livemode":true,"custom_fields":{"order_id":"6735"},"pending_features":[],"restricted_features":[],"status":"open","status_details":{"closed":null},"supported_currencies":["usd"],"features":{}}
```

# Retrieve a FinancialAccount
Retrieves the details of a FinancialAccount.

### Parameters
Noparameters.

### Returns
Return a FinancialAccount object.

```
curlhttps://api.stripe.com/v1/treasury/financial_accounts/fa_1MtZmL2eZvKYlo2Cer6cdwEC \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/treasury/financial_accounts/fa_1MtZmL2eZvKYlo2Cer6cdwEC \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"fa_1MtZmL2eZvKYlo2Cer6cdwEC","object":"treasury.financial_account","active_features":["financial_addresses.aba","outbound_payments.ach","outbound_payments.us_domestic_wire"],"balance":{"cash":{"usd":0},"inbound_pending":{"usd":0},"outbound_pending":{"usd":0}},"country":"US","created":1680714349,"financial_addresses":[{"aba":{"account_holder_name":"Jenny Rosen","account_number_last4":"7890","bank_name":"STRIPE TEST BANK","routing_number":"0000000001"},"supported_networks":["ach","us_domestic_wire"],"type":"aba"}],"livemode":true,"custom_fields":null,"pending_features":[],"restricted_features":[],"status":"open","status_details":{"closed":null},"supported_currencies":["usd"],"features":{}}
```

```
{"id":"fa_1MtZmL2eZvKYlo2Cer6cdwEC","object":"treasury.financial_account","active_features":["financial_addresses.aba","outbound_payments.ach","outbound_payments.us_domestic_wire"],"balance":{"cash":{"usd":0},"inbound_pending":{"usd":0},"outbound_pending":{"usd":0}},"country":"US","created":1680714349,"financial_addresses":[{"aba":{"account_holder_name":"Jenny Rosen","account_number_last4":"7890","bank_name":"STRIPE TEST BANK","routing_number":"0000000001"},"supported_networks":["ach","us_domestic_wire"],"type":"aba"}],"livemode":true,"custom_fields":null,"pending_features":[],"restricted_features":[],"status":"open","status_details":{"closed":null},"supported_currencies":["usd"],"features":{}}
```