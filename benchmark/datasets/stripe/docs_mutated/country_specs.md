# country_specs

*Source: https://docs.stripe.com/api/country_specs*

---

# Country Specs
Stripe needs to collect certain pieces of information about each accountcreated. These requirements can differ depending on the account’s country. TheCountry Specs API makes these rules available to your integration.
You can also view the information from this API call asan onlineguide.

# The Country Spec object

### Attributes
- idstringUnique identifier for the object. Represented as the ISO country code for this country.
- default_currencystringThe default currency_code for this country. This applies to both payment methods and bank accounts.
- supported_bank_account_currenciesobjectCurrencies that can be accepted in the specific country (for transfers).
- supported_payment_currenciesarray of stringsCurrencies that can be accepted in the specified country (for payments).
- supported_payment_methodsarray of stringsPayment methods available in the specified country. You may need to enable some payment methods (e.g.,ACH) on your account before they appear in this list. Thestripepayment method refers tocharging through your platform.
- supported_transfer_countriesarray of stringsCountries that can accept transfers from the specified country.

#### idstring

#### default_currencystring

#### supported_bank_account_currenciesobject

#### supported_payment_currenciesarray of strings

#### supported_payment_methodsarray of strings

#### supported_transfer_countriesarray of strings

### More attributesExpand all
- objectstring
- verification_fieldsobject

#### objectstring

#### verification_fieldsobject

```
{"id":"US","object":"country_spec","default_currency":"usd","supported_bank_account_currencies":{"usd":["US"]},"supported_payment_currencies":["usd","aed","afn","..."],"supported_payment_methods":["ach","card","stripe"],"supported_transfer_countries":["US","AE","AG","AL","AM","AR","AT","AU","BA","BE","BG","BH","BO","CA","CH","CI","CL","CO","CR","CY","CZ","DE","DK","DO","EC","EE","EG","ES","ET","FI","FR","GB","GH","GM","GR","GT","GY","HK","HR","HU","ID","IE","IL","IS","IT","JM","JO","JP","KE","KH","KR","KW","LC","LI","LK","LT","LU","LV","MA","MD","MG","MK","MN","MO","MT","MU","MX","MY","NA","NG","NL","NO","NZ","OM","PA","PE","PH","PL","PT","PY","QA","RO","RS","RW","SA","SE","SG","SI","SK","SN","SV","TH","TN","TR","TT","TZ","UY","UZ","VN","ZA","BD","BJ","MC","NE","SM","AZ","BN","BT","AO","DZ","TW","BS","BW","GA","LA","MZ","KZ","PK"],"verification_fields":{"company":{"additional":[],"minimum":["business_profile.mcc","business_profile.url","business_type","company.address.city","company.address.line1","company.address.postal_code","company.address.state","company.name","company.owners_provided","company.phone","company.tax_id","external_account","owners.address.city","owners.address.line1","owners.address.postal_code","owners.address.state","owners.dob.day","owners.dob.month","owners.dob.year","owners.email","owners.first_name","owners.id_number","owners.last_name","owners.phone","owners.ssn_last_4","owners.verification.document","representative.address.city","representative.address.line1","representative.address.postal_code","representative.address.state","representative.dob.day","representative.dob.month","representative.dob.year","representative.email","representative.first_name","representative.id_number","representative.last_name","representative.phone","representative.relationship.executive","representative.relationship.title","representative.ssn_last_4","representative.verification.document","tos_acceptance.date","tos_acceptance.ip"]},"individual":{"additional":[],"minimum":["business_profile.mcc","business_profile.url","business_type","external_account","individual.address.city","individual.address.line1","individual.address.postal_code","individual.address.state","individual.dob.day","individual.dob.month","individual.dob.year","individual.email","individual.first_name","individual.id_number","individual.last_name","individual.phone","individual.ssn_last_4","individual.verification.document","tos_acceptance.date","tos_acceptance.ip"]}}}
```

```
{"id":"US","object":"country_spec","default_currency":"usd","supported_bank_account_currencies":{"usd":["US"]},"supported_payment_currencies":["usd","aed","afn","..."],"supported_payment_methods":["ach","card","stripe"],"supported_transfer_countries":["US","AE","AG","AL","AM","AR","AT","AU","BA","BE","BG","BH","BO","CA","CH","CI","CL","CO","CR","CY","CZ","DE","DK","DO","EC","EE","EG","ES","ET","FI","FR","GB","GH","GM","GR","GT","GY","HK","HR","HU","ID","IE","IL","IS","IT","JM","JO","JP","KE","KH","KR","KW","LC","LI","LK","LT","LU","LV","MA","MD","MG","MK","MN","MO","MT","MU","MX","MY","NA","NG","NL","NO","NZ","OM","PA","PE","PH","PL","PT","PY","QA","RO","RS","RW","SA","SE","SG","SI","SK","SN","SV","TH","TN","TR","TT","TZ","UY","UZ","VN","ZA","BD","BJ","MC","NE","SM","AZ","BN","BT","AO","DZ","TW","BS","BW","GA","LA","MZ","KZ","PK"],"verification_fields":{"company":{"additional":[],"minimum":["business_profile.mcc","business_profile.url","business_type","company.address.city","company.address.line1","company.address.postal_code","company.address.state","company.name","company.owners_provided","company.phone","company.tax_id","external_account","owners.address.city","owners.address.line1","owners.address.postal_code","owners.address.state","owners.dob.day","owners.dob.month","owners.dob.year","owners.email","owners.first_name","owners.id_number","owners.last_name","owners.phone","owners.ssn_last_4","owners.verification.document","representative.address.city","representative.address.line1","representative.address.postal_code","representative.address.state","representative.dob.day","representative.dob.month","representative.dob.year","representative.email","representative.first_name","representative.id_number","representative.last_name","representative.phone","representative.relationship.executive","representative.relationship.title","representative.ssn_last_4","representative.verification.document","tos_acceptance.date","tos_acceptance.ip"]},"individual":{"additional":[],"minimum":["business_profile.mcc","business_profile.url","business_type","external_account","individual.address.city","individual.address.line1","individual.address.postal_code","individual.address.state","individual.dob.day","individual.dob.month","individual.dob.year","individual.email","individual.first_name","individual.id_number","individual.last_name","individual.phone","individual.ssn_last_4","individual.verification.document","tos_acceptance.date","tos_acceptance.ip"]}}}
```

# Retrieve a Country Spec
Returns a Country Spec for a given Country code.

### Parameters
Noparameters.

### Returns
Returns acountry_specobject if a valid country code is provided, andraisesan errorotherwise.

```
curlhttps://api.stripe.com/v1/country_specs/US \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/country_specs/US \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"US","object":"country_spec","default_currency":"usd","supported_bank_account_currencies":{"usd":["US"]},"supported_payment_currencies":["usd","aed","afn","..."],"supported_payment_methods":["ach","card","stripe"],"supported_transfer_countries":["US","AE","AG","AL","AM","AR","AT","AU","BA","BE","BG","BH","BO","CA","CH","CI","CL","CO","CR","CY","CZ","DE","DK","DO","EC","EE","EG","ES","ET","FI","FR","GB","GH","GM","GR","GT","GY","HK","HR","HU","ID","IE","IL","IS","IT","JM","JO","JP","KE","KH","KR","KW","LC","LI","LK","LT","LU","LV","MA","MD","MG","MK","MN","MO","MT","MU","MX","MY","NA","NG","NL","NO","NZ","OM","PA","PE","PH","PL","PT","PY","QA","RO","RS","RW","SA","SE","SG","SI","SK","SN","SV","TH","TN","TR","TT","TZ","UY","UZ","VN","ZA","BD","BJ","MC","NE","SM","AZ","BN","BT","AO","DZ","TW","BS","BW","GA","LA","MZ","KZ","PK"],"verification_fields":{"company":{"additional":[],"minimum":["business_profile.mcc","business_profile.url","business_type","company.address.city","company.address.line1","company.address.postal_code","company.address.state","company.name","company.owners_provided","company.phone","company.tax_id","external_account","owners.address.city","owners.address.line1","owners.address.postal_code","owners.address.state","owners.dob.day","owners.dob.month","owners.dob.year","owners.email","owners.first_name","owners.id_number","owners.last_name","owners.phone","owners.ssn_last_4","owners.verification.document","representative.address.city","representative.address.line1","representative.address.postal_code","representative.address.state","representative.dob.day","representative.dob.month","representative.dob.year","representative.email","representative.first_name","representative.id_number","representative.last_name","representative.phone","representative.relationship.executive","representative.relationship.title","representative.ssn_last_4","representative.verification.document","tos_acceptance.date","tos_acceptance.ip"]},"individual":{"additional":[],"minimum":["business_profile.mcc","business_profile.url","business_type","external_account","individual.address.city","individual.address.line1","individual.address.postal_code","individual.address.state","individual.dob.day","individual.dob.month","individual.dob.year","individual.email","individual.first_name","individual.id_number","individual.last_name","individual.phone","individual.ssn_last_4","individual.verification.document","tos_acceptance.date","tos_acceptance.ip"]}}}
```

```
{"id":"US","object":"country_spec","default_currency":"usd","supported_bank_account_currencies":{"usd":["US"]},"supported_payment_currencies":["usd","aed","afn","..."],"supported_payment_methods":["ach","card","stripe"],"supported_transfer_countries":["US","AE","AG","AL","AM","AR","AT","AU","BA","BE","BG","BH","BO","CA","CH","CI","CL","CO","CR","CY","CZ","DE","DK","DO","EC","EE","EG","ES","ET","FI","FR","GB","GH","GM","GR","GT","GY","HK","HR","HU","ID","IE","IL","IS","IT","JM","JO","JP","KE","KH","KR","KW","LC","LI","LK","LT","LU","LV","MA","MD","MG","MK","MN","MO","MT","MU","MX","MY","NA","NG","NL","NO","NZ","OM","PA","PE","PH","PL","PT","PY","QA","RO","RS","RW","SA","SE","SG","SI","SK","SN","SV","TH","TN","TR","TT","TZ","UY","UZ","VN","ZA","BD","BJ","MC","NE","SM","AZ","BN","BT","AO","DZ","TW","BS","BW","GA","LA","MZ","KZ","PK"],"verification_fields":{"company":{"additional":[],"minimum":["business_profile.mcc","business_profile.url","business_type","company.address.city","company.address.line1","company.address.postal_code","company.address.state","company.name","company.owners_provided","company.phone","company.tax_id","external_account","owners.address.city","owners.address.line1","owners.address.postal_code","owners.address.state","owners.dob.day","owners.dob.month","owners.dob.year","owners.email","owners.first_name","owners.id_number","owners.last_name","owners.phone","owners.ssn_last_4","owners.verification.document","representative.address.city","representative.address.line1","representative.address.postal_code","representative.address.state","representative.dob.day","representative.dob.month","representative.dob.year","representative.email","representative.first_name","representative.id_number","representative.last_name","representative.phone","representative.relationship.executive","representative.relationship.title","representative.ssn_last_4","representative.verification.document","tos_acceptance.date","tos_acceptance.ip"]},"individual":{"additional":[],"minimum":["business_profile.mcc","business_profile.url","business_type","external_account","individual.address.city","individual.address.line1","individual.address.postal_code","individual.address.state","individual.dob.day","individual.dob.month","individual.dob.year","individual.email","individual.first_name","individual.id_number","individual.last_name","individual.phone","individual.ssn_last_4","individual.verification.document","tos_acceptance.date","tos_acceptance.ip"]}}}
```

# List Country Specs
Lists all Country Spec objects available in the API.

### Parameters
Noparameters.

### More parametersExpand all
- ending_beforestring
- limitinteger
- starting_afterstring

#### ending_beforestring

#### limitinteger

#### starting_afterstring

### Returns
Returns a list of country_spec objects.

```
curl-G https://api.stripe.com/v1/country_specs \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
curl-G https://api.stripe.com/v1/country_specs \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
{"object":"list","url":"/v1/country_specs","has_more":false,"data":[{"id":"US","object":"country_spec","default_currency":"usd","supported_bank_account_currencies":{"usd":["US"]},"supported_payment_currencies":["usd","aed","afn","..."],"supported_payment_methods":["ach","card","stripe"],"supported_transfer_countries":["US","AE","AG","AL","AM","AR","AT","AU","BA","BE","BG","BH","BO","CA","CH","CI","CL","CO","CR","CY","CZ","DE","DK","DO","EC","EE","EG","ES","ET","FI","FR","GB","GH","GM","GR","GT","GY","HK","HR","HU","ID","IE","IL","IS","IT","JM","JO","JP","KE","KH","KR","KW","LC","LI","LK","LT","LU","LV","MA","MD","MG","MK","MN","MO","MT","MU","MX","MY","NA","NG","NL","NO","NZ","OM","PA","PE","PH","PL","PT","PY","QA","RO","RS","RW","SA","SE","SG","SI","SK","SN","SV","TH","TN","TR","TT","TZ","UY","UZ","VN","ZA","BD","BJ","MC","NE","SM","AZ","BN","BT","AO","DZ","TW","BS","BW","GA","LA","MZ","KZ","PK"],"verification_fields":{"company":{"additional":[],"minimum":["business_profile.mcc","business_profile.url","business_type","company.address.city","company.address.line1","company.address.postal_code","company.address.state","company.name","company.owners_provided","company.phone","company.tax_id","external_account","owners.address.city","owners.address.line1","owners.address.postal_code","owners.address.state","owners.dob.day","owners.dob.month","owners.dob.year","owners.email","owners.first_name","owners.id_number","owners.last_name","owners.phone","owners.ssn_last_4","owners.verification.document","representative.address.city","representative.address.line1","representative.address.postal_code","representative.address.state","representative.dob.day","representative.dob.month","representative.dob.year","representative.email","representative.first_name","representative.id_number","representative.last_name","representative.phone","representative.relationship.executive","representative.relationship.title","representative.ssn_last_4","representative.verification.document","tos_acceptance.date","tos_acceptance.ip"]},"individual":{"additional":[],"minimum":["business_profile.mcc","business_profile.url","business_type","external_account","individual.address.city","individual.address.line1","individual.address.postal_code","individual.address.state","individual.dob.day","individual.dob.month","individual.dob.year","individual.email","individual.first_name","individual.id_number","individual.last_name","individual.phone","individual.ssn_last_4","individual.verification.document","tos_acceptance.date","tos_acceptance.ip"]}}}]}
```

```
{"object":"list","url":"/v1/country_specs","has_more":false,"data":[{"id":"US","object":"country_spec","default_currency":"usd","supported_bank_account_currencies":{"usd":["US"]},"supported_payment_currencies":["usd","aed","afn","..."],"supported_payment_methods":["ach","card","stripe"],"supported_transfer_countries":["US","AE","AG","AL","AM","AR","AT","AU","BA","BE","BG","BH","BO","CA","CH","CI","CL","CO","CR","CY","CZ","DE","DK","DO","EC","EE","EG","ES","ET","FI","FR","GB","GH","GM","GR","GT","GY","HK","HR","HU","ID","IE","IL","IS","IT","JM","JO","JP","KE","KH","KR","KW","LC","LI","LK","LT","LU","LV","MA","MD","MG","MK","MN","MO","MT","MU","MX","MY","NA","NG","NL","NO","NZ","OM","PA","PE","PH","PL","PT","PY","QA","RO","RS","RW","SA","SE","SG","SI","SK","SN","SV","TH","TN","TR","TT","TZ","UY","UZ","VN","ZA","BD","BJ","MC","NE","SM","AZ","BN","BT","AO","DZ","TW","BS","BW","GA","LA","MZ","KZ","PK"],"verification_fields":{"company":{"additional":[],"minimum":["business_profile.mcc","business_profile.url","business_type","company.address.city","company.address.line1","company.address.postal_code","company.address.state","company.name","company.owners_provided","company.phone","company.tax_id","external_account","owners.address.city","owners.address.line1","owners.address.postal_code","owners.address.state","owners.dob.day","owners.dob.month","owners.dob.year","owners.email","owners.first_name","owners.id_number","owners.last_name","owners.phone","owners.ssn_last_4","owners.verification.document","representative.address.city","representative.address.line1","representative.address.postal_code","representative.address.state","representative.dob.day","representative.dob.month","representative.dob.year","representative.email","representative.first_name","representative.id_number","representative.last_name","representative.phone","representative.relationship.executive","representative.relationship.title","representative.ssn_last_4","representative.verification.document","tos_acceptance.date","tos_acceptance.ip"]},"individual":{"additional":[],"minimum":["business_profile.mcc","business_profile.url","business_type","external_account","individual.address.city","individual.address.line1","individual.address.postal_code","individual.address.state","individual.dob.day","individual.dob.month","individual.dob.year","individual.email","individual.first_name","individual.id_number","individual.last_name","individual.phone","individual.ssn_last_4","individual.verification.document","tos_acceptance.date","tos_acceptance.ip"]}}}]}
```