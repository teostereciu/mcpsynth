# issuing/authorizations

*Source: https://docs.stripe.com/api/issuing/authorizations*

---

# Authorizations
When anissued cardis used to make a purchase, an IssuingAuthorizationobject is created.Authorizationsmust be approved for thepurchase to be completed successfully.
Related guide:Issued card authorizations

# The Authorization object

### Attributes
- idstringUnique identifier for the object.
- amountintegerThe total amount that was authorized or rejected. This amount is incurrencyand in thesmallest currency unit.amountshould be the same asmerchant_amount, unlesscurrencyandmerchant_currencyare different.
- approvedbooleanWhether the authorization has been approved.
- cardobjectCard associated with this authorization.Show child attributes
- cardholdernullablestringExpandableThe cardholder to whom this authorization belongs.
- currencyenumThe currency of the cardholder. This currency can be different from the currency presented at authorization and themerchant_currencyfield on this authorization. Three-letterISO currency code, in lowercase. Must be asupported currency.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- statusenumThe current status of the authorization in its lifecycle.Possible enum valuesclosedThe authorization was declined orcapturedthrough one or moretransactions.expiredThe authorization was expired without capture.pendingThe authorization was created and is awaiting approval or was approved and is awaitingcapture.reversedThe authorization was reversed by the merchant.

#### idstring

#### amountinteger

#### approvedboolean

#### cardobject

#### cardholdernullablestringExpandable

#### currencyenum

#### metadataobject

#### statusenum

[TABLE]
closedThe authorization was declined orcapturedthrough one or moretransactions.
expiredThe authorization was expired without capture.
pendingThe authorization was created and is awaiting approval or was approved and is awaitingcapture.
reversedThe authorization was reversed by the merchant.
[/TABLE]

### More attributesExpand all
- objectstring
- amount_detailsnullableobject
- authorization_methodenum
- balance_transactionsarray of objects
- createdtimestamp
- fleetnullableobject
- fraud_challengesnullablearray of objectsExpandable
- fuelnullableobject
- livemodeboolean
- merchant_amountinteger
- merchant_currencyenum
- merchant_dataobject
- network_datanullableobject
- pending_requestnullableobject
- request_historyarray of objects
- tokennullablestringPreview featureExpandable
- transactionsarray of objects
- verification_dataobject
- verified_by_fraud_challengenullableboolean
- walletnullablestring

#### objectstring

#### amount_detailsnullableobject

#### authorization_methodenum

#### balance_transactionsarray of objects

#### createdtimestamp

#### fleetnullableobject

#### fraud_challengesnullablearray of objectsExpandable

#### fuelnullableobject

#### livemodeboolean

#### merchant_amountinteger

#### merchant_currencyenum

#### merchant_dataobject

#### network_datanullableobject

#### pending_requestnullableobject

#### request_historyarray of objects

#### tokennullablestringPreview featureExpandable

#### transactionsarray of objects

#### verification_dataobject

#### verified_by_fraud_challengenullableboolean

#### walletnullablestring

```
{"id":"iauth_1JVXl82eZvKYlo2CPIiWlzrn","object":"issuing.authorization","amount":382,"amount_details":{"atm_fee":null},"approved":false,"authorization_method":"online","balance_transactions":[],"card":{"id":"ic_1JDmgz2eZvKYlo2CRXlTsXj6","object":"issuing.card","brand":"Visa","cancellation_reason":null,"cardholder":{"id":"ich_1JDmfb2eZvKYlo2CwHUgaAxU","object":"issuing.cardholder","billing":{"address":{"city":"San Francisco","country":"US","line1":"123 Main Street","line2":null,"postal_code":"94111","state":"CA"}},"company":null,"created":1626425119,"email":"jenny.rosen@example.com","individual":null,"livemode":false,"metadata":{},"name":"Jenny Rosen","phone_number":"+18008675309","redaction":null,"requirements":{"disabled_reason":null,"past_due":[]},"spending_controls":{"allowed_categories":[],"blocked_categories":[],"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"individual"},"created":1626425206,"currency":"usd","exp_month":6,"exp_year":2024,"last4":"8693","livemode":false,"metadata":{},"redaction":null,"replaced_by":null,"replacement_for":null,"replacement_reason":null,"shipping":null,"spending_controls":{"allowed_categories":null,"blocked_categories":null,"spending_limits":[{"amount":50000,"categories":[],"interval":"daily"}],"spending_limits_currency":"usd"},"status":"active","type":"virtual","wallets":{"apple_pay":{"eligible":true,"ineligible_reason":null},"google_pay":{"eligible":true,"ineligible_reason":null},"primary_account_identifier":null}},"cardholder":"ich_1JDmfb2eZvKYlo2CwHUgaAxU","created":1630657706,"currency":"usd","livemode":false,"merchant_amount":382,"merchant_currency":"usd","merchant_data":{"category":"computer_software_stores","category_code":"5734","city":"SAN FRANCISCO","country":"US","name":"STRIPE","network_id":"1234567890","postal_code":"94103","state":"CA"},"metadata":{"order_id":"6735"},"network_data":null,"pending_request":null,"redaction":null,"request_history":[{"amount":382,"amount_details":{"atm_fee":null},"approved":false,"created":1630657706,"currency":"usd","merchant_amount":382,"merchant_currency":"usd","reason":"verification_failed","reason_message":null}],"status":"closed","transactions":[],"verification_data":{"address_line1_check":"not_provided","address_postal_code_check":"not_provided","cvc_check":"mismatch","expiry_check":"match"},"wallet":null}
```

```
{"id":"iauth_1JVXl82eZvKYlo2CPIiWlzrn","object":"issuing.authorization","amount":382,"amount_details":{"atm_fee":null},"approved":false,"authorization_method":"online","balance_transactions":[],"card":{"id":"ic_1JDmgz2eZvKYlo2CRXlTsXj6","object":"issuing.card","brand":"Visa","cancellation_reason":null,"cardholder":{"id":"ich_1JDmfb2eZvKYlo2CwHUgaAxU","object":"issuing.cardholder","billing":{"address":{"city":"San Francisco","country":"US","line1":"123 Main Street","line2":null,"postal_code":"94111","state":"CA"}},"company":null,"created":1626425119,"email":"jenny.rosen@example.com","individual":null,"livemode":false,"metadata":{},"name":"Jenny Rosen","phone_number":"+18008675309","redaction":null,"requirements":{"disabled_reason":null,"past_due":[]},"spending_controls":{"allowed_categories":[],"blocked_categories":[],"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"individual"},"created":1626425206,"currency":"usd","exp_month":6,"exp_year":2024,"last4":"8693","livemode":false,"metadata":{},"redaction":null,"replaced_by":null,"replacement_for":null,"replacement_reason":null,"shipping":null,"spending_controls":{"allowed_categories":null,"blocked_categories":null,"spending_limits":[{"amount":50000,"categories":[],"interval":"daily"}],"spending_limits_currency":"usd"},"status":"active","type":"virtual","wallets":{"apple_pay":{"eligible":true,"ineligible_reason":null},"google_pay":{"eligible":true,"ineligible_reason":null},"primary_account_identifier":null}},"cardholder":"ich_1JDmfb2eZvKYlo2CwHUgaAxU","created":1630657706,"currency":"usd","livemode":false,"merchant_amount":382,"merchant_currency":"usd","merchant_data":{"category":"computer_software_stores","category_code":"5734","city":"SAN FRANCISCO","country":"US","name":"STRIPE","network_id":"1234567890","postal_code":"94103","state":"CA"},"metadata":{"order_id":"6735"},"network_data":null,"pending_request":null,"redaction":null,"request_history":[{"amount":382,"amount_details":{"atm_fee":null},"approved":false,"created":1630657706,"currency":"usd","merchant_amount":382,"merchant_currency":"usd","reason":"verification_failed","reason_message":null}],"status":"closed","transactions":[],"verification_data":{"address_line1_check":"not_provided","address_postal_code_check":"not_provided","cvc_check":"mismatch","expiry_check":"match"},"wallet":null}
```

# Update an authorization
Updates the specified IssuingAuthorizationobject by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

### Parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### metadataobject

### Returns
Returns an updated IssuingAuthorizationobject if a valid identifier was provided.

```
curlhttps://api.stripe.com/v1/issuing/authorizations/iauth_1JVXl82eZvKYlo2CPIiWlzrn \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/issuing/authorizations/iauth_1JVXl82eZvKYlo2CPIiWlzrn \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
{"id":"iauth_1JVXl82eZvKYlo2CPIiWlzrn","object":"issuing.authorization","amount":382,"amount_details":{"atm_fee":null},"approved":false,"authorization_method":"online","balance_transactions":[],"card":{"id":"ic_1JDmgz2eZvKYlo2CRXlTsXj6","object":"issuing.card","brand":"Visa","cancellation_reason":null,"cardholder":{"id":"ich_1JDmfb2eZvKYlo2CwHUgaAxU","object":"issuing.cardholder","billing":{"address":{"city":"San Francisco","country":"US","line1":"123 Main Street","line2":null,"postal_code":"94111","state":"CA"}},"company":null,"created":1626425119,"email":"jenny.rosen@example.com","individual":null,"livemode":false,"metadata":{},"name":"Jenny Rosen","phone_number":"+18008675309","redaction":null,"requirements":{"disabled_reason":null,"past_due":[]},"spending_controls":{"allowed_categories":[],"blocked_categories":[],"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"individual"},"created":1626425206,"currency":"usd","exp_month":6,"exp_year":2024,"last4":"8693","livemode":false,"metadata":{},"redaction":null,"replaced_by":null,"replacement_for":null,"replacement_reason":null,"shipping":null,"spending_controls":{"allowed_categories":null,"blocked_categories":null,"spending_limits":[{"amount":50000,"categories":[],"interval":"daily"}],"spending_limits_currency":"usd"},"status":"active","type":"virtual","wallets":{"apple_pay":{"eligible":true,"ineligible_reason":null},"google_pay":{"eligible":true,"ineligible_reason":null},"primary_account_identifier":null}},"cardholder":"ich_1JDmfb2eZvKYlo2CwHUgaAxU","created":1630657706,"currency":"usd","livemode":false,"merchant_amount":382,"merchant_currency":"usd","merchant_data":{"category":"computer_software_stores","category_code":"5734","city":"SAN FRANCISCO","country":"US","name":"STRIPE","network_id":"1234567890","postal_code":"94103","state":"CA"},"metadata":{"order_id":"6735"},"network_data":null,"pending_request":null,"redaction":null,"request_history":[{"amount":382,"amount_details":{"atm_fee":null},"approved":false,"created":1630657706,"currency":"usd","merchant_amount":382,"merchant_currency":"usd","reason":"verification_failed","reason_message":null}],"status":"closed","transactions":[],"verification_data":{"address_line1_check":"not_provided","address_postal_code_check":"not_provided","cvc_check":"mismatch","expiry_check":"match"},"wallet":null}
```

```
{"id":"iauth_1JVXl82eZvKYlo2CPIiWlzrn","object":"issuing.authorization","amount":382,"amount_details":{"atm_fee":null},"approved":false,"authorization_method":"online","balance_transactions":[],"card":{"id":"ic_1JDmgz2eZvKYlo2CRXlTsXj6","object":"issuing.card","brand":"Visa","cancellation_reason":null,"cardholder":{"id":"ich_1JDmfb2eZvKYlo2CwHUgaAxU","object":"issuing.cardholder","billing":{"address":{"city":"San Francisco","country":"US","line1":"123 Main Street","line2":null,"postal_code":"94111","state":"CA"}},"company":null,"created":1626425119,"email":"jenny.rosen@example.com","individual":null,"livemode":false,"metadata":{},"name":"Jenny Rosen","phone_number":"+18008675309","redaction":null,"requirements":{"disabled_reason":null,"past_due":[]},"spending_controls":{"allowed_categories":[],"blocked_categories":[],"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"individual"},"created":1626425206,"currency":"usd","exp_month":6,"exp_year":2024,"last4":"8693","livemode":false,"metadata":{},"redaction":null,"replaced_by":null,"replacement_for":null,"replacement_reason":null,"shipping":null,"spending_controls":{"allowed_categories":null,"blocked_categories":null,"spending_limits":[{"amount":50000,"categories":[],"interval":"daily"}],"spending_limits_currency":"usd"},"status":"active","type":"virtual","wallets":{"apple_pay":{"eligible":true,"ineligible_reason":null},"google_pay":{"eligible":true,"ineligible_reason":null},"primary_account_identifier":null}},"cardholder":"ich_1JDmfb2eZvKYlo2CwHUgaAxU","created":1630657706,"currency":"usd","livemode":false,"merchant_amount":382,"merchant_currency":"usd","merchant_data":{"category":"computer_software_stores","category_code":"5734","city":"SAN FRANCISCO","country":"US","name":"STRIPE","network_id":"1234567890","postal_code":"94103","state":"CA"},"metadata":{"order_id":"6735"},"network_data":null,"pending_request":null,"redaction":null,"request_history":[{"amount":382,"amount_details":{"atm_fee":null},"approved":false,"created":1630657706,"currency":"usd","merchant_amount":382,"merchant_currency":"usd","reason":"verification_failed","reason_message":null}],"status":"closed","transactions":[],"verification_data":{"address_line1_check":"not_provided","address_postal_code_check":"not_provided","cvc_check":"mismatch","expiry_check":"match"},"wallet":null}
```

# Retrieve an authorization
Retrieves an IssuingAuthorizationobject.

### Parameters
Noparameters.

### Returns
Returns an IssuingAuthorizationobject if a valid identifier was provided.

```
curlhttps://api.stripe.com/v1/issuing/authorizations/iauth_1JVXl82eZvKYlo2CPIiWlzrn \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/issuing/authorizations/iauth_1JVXl82eZvKYlo2CPIiWlzrn \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"iauth_1JVXl82eZvKYlo2CPIiWlzrn","object":"issuing.authorization","amount":382,"amount_details":{"atm_fee":null},"approved":false,"authorization_method":"online","balance_transactions":[],"card":{"id":"ic_1JDmgz2eZvKYlo2CRXlTsXj6","object":"issuing.card","brand":"Visa","cancellation_reason":null,"cardholder":{"id":"ich_1JDmfb2eZvKYlo2CwHUgaAxU","object":"issuing.cardholder","billing":{"address":{"city":"San Francisco","country":"US","line1":"123 Main Street","line2":null,"postal_code":"94111","state":"CA"}},"company":null,"created":1626425119,"email":"jenny.rosen@example.com","individual":null,"livemode":false,"metadata":{},"name":"Jenny Rosen","phone_number":"+18008675309","redaction":null,"requirements":{"disabled_reason":null,"past_due":[]},"spending_controls":{"allowed_categories":[],"blocked_categories":[],"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"individual"},"created":1626425206,"currency":"usd","exp_month":6,"exp_year":2024,"last4":"8693","livemode":false,"metadata":{},"redaction":null,"replaced_by":null,"replacement_for":null,"replacement_reason":null,"shipping":null,"spending_controls":{"allowed_categories":null,"blocked_categories":null,"spending_limits":[{"amount":50000,"categories":[],"interval":"daily"}],"spending_limits_currency":"usd"},"status":"active","type":"virtual","wallets":{"apple_pay":{"eligible":true,"ineligible_reason":null},"google_pay":{"eligible":true,"ineligible_reason":null},"primary_account_identifier":null}},"cardholder":"ich_1JDmfb2eZvKYlo2CwHUgaAxU","created":1630657706,"currency":"usd","livemode":false,"merchant_amount":382,"merchant_currency":"usd","merchant_data":{"category":"computer_software_stores","category_code":"5734","city":"SAN FRANCISCO","country":"US","name":"STRIPE","network_id":"1234567890","postal_code":"94103","state":"CA"},"metadata":{"order_id":"6735"},"network_data":null,"pending_request":null,"redaction":null,"request_history":[{"amount":382,"amount_details":{"atm_fee":null},"approved":false,"created":1630657706,"currency":"usd","merchant_amount":382,"merchant_currency":"usd","reason":"verification_failed","reason_message":null}],"status":"closed","transactions":[],"verification_data":{"address_line1_check":"not_provided","address_postal_code_check":"not_provided","cvc_check":"mismatch","expiry_check":"match"},"wallet":null}
```

```
{"id":"iauth_1JVXl82eZvKYlo2CPIiWlzrn","object":"issuing.authorization","amount":382,"amount_details":{"atm_fee":null},"approved":false,"authorization_method":"online","balance_transactions":[],"card":{"id":"ic_1JDmgz2eZvKYlo2CRXlTsXj6","object":"issuing.card","brand":"Visa","cancellation_reason":null,"cardholder":{"id":"ich_1JDmfb2eZvKYlo2CwHUgaAxU","object":"issuing.cardholder","billing":{"address":{"city":"San Francisco","country":"US","line1":"123 Main Street","line2":null,"postal_code":"94111","state":"CA"}},"company":null,"created":1626425119,"email":"jenny.rosen@example.com","individual":null,"livemode":false,"metadata":{},"name":"Jenny Rosen","phone_number":"+18008675309","redaction":null,"requirements":{"disabled_reason":null,"past_due":[]},"spending_controls":{"allowed_categories":[],"blocked_categories":[],"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"individual"},"created":1626425206,"currency":"usd","exp_month":6,"exp_year":2024,"last4":"8693","livemode":false,"metadata":{},"redaction":null,"replaced_by":null,"replacement_for":null,"replacement_reason":null,"shipping":null,"spending_controls":{"allowed_categories":null,"blocked_categories":null,"spending_limits":[{"amount":50000,"categories":[],"interval":"daily"}],"spending_limits_currency":"usd"},"status":"active","type":"virtual","wallets":{"apple_pay":{"eligible":true,"ineligible_reason":null},"google_pay":{"eligible":true,"ineligible_reason":null},"primary_account_identifier":null}},"cardholder":"ich_1JDmfb2eZvKYlo2CwHUgaAxU","created":1630657706,"currency":"usd","livemode":false,"merchant_amount":382,"merchant_currency":"usd","merchant_data":{"category":"computer_software_stores","category_code":"5734","city":"SAN FRANCISCO","country":"US","name":"STRIPE","network_id":"1234567890","postal_code":"94103","state":"CA"},"metadata":{"order_id":"6735"},"network_data":null,"pending_request":null,"redaction":null,"request_history":[{"amount":382,"amount_details":{"atm_fee":null},"approved":false,"created":1630657706,"currency":"usd","merchant_amount":382,"merchant_currency":"usd","reason":"verification_failed","reason_message":null}],"status":"closed","transactions":[],"verification_data":{"address_line1_check":"not_provided","address_postal_code_check":"not_provided","cvc_check":"mismatch","expiry_check":"match"},"wallet":null}
```

# List all authorizations
Returns a list of IssuingAuthorizationobjects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.

### Parameters
- cardstringOnly return authorizations that belong to the given card.
- cardholderstringOnly return authorizations that belong to the given cardholder.
- statusenumOnly return authorizations with the given status. One ofpending,closed, orreversed.Possible enum valuesclosedThe authorization was declined orcapturedthrough one or moretransactions.expiredThe authorization was expired without capture.pendingThe authorization was created and is awaiting approval or was approved and is awaitingcapture.reversedThe authorization was reversed by the merchant.

#### cardstring

#### cardholderstring

#### statusenum

[TABLE]
closedThe authorization was declined orcapturedthrough one or moretransactions.
expiredThe authorization was expired without capture.
pendingThe authorization was created and is awaiting approval or was approved and is awaitingcapture.
reversedThe authorization was reversed by the merchant.
[/TABLE]

### More parametersExpand all
- createdobject
- ending_beforestring
- limitinteger
- starting_afterstring

#### createdobject

#### ending_beforestring

#### limitinteger

#### starting_afterstring

### Returns
Adictionarywith adataproperty that contains an array of up tolimitauthorizations, starting after authorizationstarting_after. Each entry in the array is a separate IssuingAuthorizationobject. If no more authorizations are available, the resulting array will be empty.

```
curl-G https://api.stripe.com/v1/issuing/authorizations \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
curl-G https://api.stripe.com/v1/issuing/authorizations \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
{"object":"list","url":"/v1/issuing/authorizations","has_more":false,"data":[{"id":"iauth_1JVXl82eZvKYlo2CPIiWlzrn","object":"issuing.authorization","amount":382,"amount_details":{"atm_fee":null},"approved":false,"authorization_method":"online","balance_transactions":[],"card":{"id":"ic_1JDmgz2eZvKYlo2CRXlTsXj6","object":"issuing.card","brand":"Visa","cancellation_reason":null,"cardholder":{"id":"ich_1JDmfb2eZvKYlo2CwHUgaAxU","object":"issuing.cardholder","billing":{"address":{"city":"San Francisco","country":"US","line1":"123 Main Street","line2":null,"postal_code":"94111","state":"CA"}},"company":null,"created":1626425119,"email":"jenny.rosen@example.com","individual":null,"livemode":false,"metadata":{},"name":"Jenny Rosen","phone_number":"+18008675309","redaction":null,"requirements":{"disabled_reason":null,"past_due":[]},"spending_controls":{"allowed_categories":[],"blocked_categories":[],"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"individual"},"created":1626425206,"currency":"usd","exp_month":6,"exp_year":2024,"last4":"8693","livemode":false,"metadata":{},"redaction":null,"replaced_by":null,"replacement_for":null,"replacement_reason":null,"shipping":null,"spending_controls":{"allowed_categories":null,"blocked_categories":null,"spending_limits":[{"amount":50000,"categories":[],"interval":"daily"}],"spending_limits_currency":"usd"},"status":"active","type":"virtual","wallets":{"apple_pay":{"eligible":true,"ineligible_reason":null},"google_pay":{"eligible":true,"ineligible_reason":null},"primary_account_identifier":null}},"cardholder":"ich_1JDmfb2eZvKYlo2CwHUgaAxU","created":1630657706,"currency":"usd","livemode":false,"merchant_amount":382,"merchant_currency":"usd","merchant_data":{"category":"computer_software_stores","category_code":"5734","city":"SAN FRANCISCO","country":"US","name":"STRIPE","network_id":"1234567890","postal_code":"94103","state":"CA"},"metadata":{"order_id":"6735"},"network_data":null,"pending_request":null,"redaction":null,"request_history":[{"amount":382,"amount_details":{"atm_fee":null},"approved":false,"created":1630657706,"currency":"usd","merchant_amount":382,"merchant_currency":"usd","reason":"verification_failed","reason_message":null}],"status":"closed","transactions":[],"verification_data":{"address_line1_check":"not_provided","address_postal_code_check":"not_provided","cvc_check":"mismatch","expiry_check":"match"},"wallet":null}]}
```

```
{"object":"list","url":"/v1/issuing/authorizations","has_more":false,"data":[{"id":"iauth_1JVXl82eZvKYlo2CPIiWlzrn","object":"issuing.authorization","amount":382,"amount_details":{"atm_fee":null},"approved":false,"authorization_method":"online","balance_transactions":[],"card":{"id":"ic_1JDmgz2eZvKYlo2CRXlTsXj6","object":"issuing.card","brand":"Visa","cancellation_reason":null,"cardholder":{"id":"ich_1JDmfb2eZvKYlo2CwHUgaAxU","object":"issuing.cardholder","billing":{"address":{"city":"San Francisco","country":"US","line1":"123 Main Street","line2":null,"postal_code":"94111","state":"CA"}},"company":null,"created":1626425119,"email":"jenny.rosen@example.com","individual":null,"livemode":false,"metadata":{},"name":"Jenny Rosen","phone_number":"+18008675309","redaction":null,"requirements":{"disabled_reason":null,"past_due":[]},"spending_controls":{"allowed_categories":[],"blocked_categories":[],"spending_limits":[],"spending_limits_currency":null},"status":"active","type":"individual"},"created":1626425206,"currency":"usd","exp_month":6,"exp_year":2024,"last4":"8693","livemode":false,"metadata":{},"redaction":null,"replaced_by":null,"replacement_for":null,"replacement_reason":null,"shipping":null,"spending_controls":{"allowed_categories":null,"blocked_categories":null,"spending_limits":[{"amount":50000,"categories":[],"interval":"daily"}],"spending_limits_currency":"usd"},"status":"active","type":"virtual","wallets":{"apple_pay":{"eligible":true,"ineligible_reason":null},"google_pay":{"eligible":true,"ineligible_reason":null},"primary_account_identifier":null}},"cardholder":"ich_1JDmfb2eZvKYlo2CwHUgaAxU","created":1630657706,"currency":"usd","livemode":false,"merchant_amount":382,"merchant_currency":"usd","merchant_data":{"category":"computer_software_stores","category_code":"5734","city":"SAN FRANCISCO","country":"US","name":"STRIPE","network_id":"1234567890","postal_code":"94103","state":"CA"},"metadata":{"order_id":"6735"},"network_data":null,"pending_request":null,"redaction":null,"request_history":[{"amount":382,"amount_details":{"atm_fee":null},"approved":false,"created":1630657706,"currency":"usd","merchant_amount":382,"merchant_currency":"usd","reason":"verification_failed","reason_message":null}],"status":"closed","transactions":[],"verification_data":{"address_line1_check":"not_provided","address_postal_code_check":"not_provided","cvc_check":"mismatch","expiry_check":"match"},"wallet":null}]}
```