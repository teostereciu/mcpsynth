# v2/core/person-tokens

*Source: https://docs.stripe.com/api/v2/core/person-tokens*

---

# Person Tokensv2
Person Tokens are single-use tokens which tokenize person information, and are used for creating or updating a Person.

# The Person Token objectv2

### Attributes
- idstringUnique identifier for the token.
- objectstring, value is "v2.core.account_person_token"String representing the object’s type. Objects of the same type share the same value of the object field.
- createdtimestampTime at which the token was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
- expires_attimestampTime at which the token will expire.
- livemodebooleanHas the valuetrueif the token exists in live mode or the valuefalseif the object exists in test mode.
- usedbooleanDetermines if the token has already been used (tokens can only be used once).

#### idstring

#### objectstring, value is "v2.core.account_person_token"

#### createdtimestamp

#### expires_attimestamp

#### livemodeboolean

#### usedboolean

```
{"id":"perstok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY","object":"v2.core.account_person_token","created":"2025-11-17T14:00:00.000Z","expires_at":"2025-11-17T14:10:00.000Z","livemode":true,"used":false}
```

```
{"id":"perstok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY","object":"v2.core.account_person_token","created":"2025-11-17T14:00:00.000Z","expires_at":"2025-11-17T14:10:00.000Z","livemode":true,"used":false}
```

# Create a Person Tokenv2
Creates a Person Token associated with an Account.

### Parameters
- account_idstringRequiredThe Account the Person is associated with.
- additional_addressesarray of objectsAdditional addresses associated with the person.Show child parameters
- additional_namesarray of objectsAdditional names (e.g. aliases) associated with the person.Show child parameters
- additional_terms_of_serviceobjectAttestations of accepted terms of service agreements.Show child parameters
- addressobjectThe person’s residential address.Show child parameters
- date_of_birthobjectThe person’s date of birth.Show child parameters
- documentsobjectDocuments that may be submitted to satisfy various informational requests.Show child parameters
- emailstringEmail.
- given_namestringThe person’s first name.
- id_numbersarray of objectsThe identification numbers (e.g., SSN) associated with the person.Show child parameters
- legal_genderenumThe person’s gender (International regulations require either “male” or “female”).Possible enum valuesfemaleFemale gender person.maleMale gender person.
- metadatamapSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- nationalitiesarray of enumsThe nationalities (countries) this person is associated with.
- phonestringThe phone number for this person.
- political_exposureenumThe person’s political exposure.Possible enum valuesexistingThe person has disclosed that they do have political exposure.noneThe person has disclosed that they have no political exposure.
- relationshipobjectThe relationship that this person has with the Account’s business or legal entity.Show child parameters
- script_addressesobjectThe script addresses (e.g., non-Latin characters) associated with the person.Show child parameters
- script_namesobjectThe script names (e.g. non-Latin characters) associated with the person.Show child parameters
- surnamestringThe person’s last name.

#### account_idstringRequired

#### additional_addressesarray of objects

#### additional_namesarray of objects

#### additional_terms_of_serviceobject

#### addressobject

#### date_of_birthobject

#### documentsobject

#### emailstring

#### given_namestring

#### id_numbersarray of objects

#### legal_genderenum

[TABLE]
femaleFemale gender person.
maleMale gender person.
[/TABLE]

#### metadatamap

#### nationalitiesarray of enums

#### phonestring

#### political_exposureenum

[TABLE]
existingThe person has disclosed that they do have political exposure.
noneThe person has disclosed that they have no political exposure.
[/TABLE]

#### relationshipobject

#### script_addressesobject

#### script_namesobject

#### surnamestring

### Returns

### Response attributes
- idstringUnique identifier for the token.
- objectstring, value is "v2.core.account_person_token"String representing the object’s type. Objects of the same type share the same value of the object field.
- createdtimestampTime at which the token was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
- expires_attimestampTime at which the token will expire.
- livemodebooleanHas the valuetrueif the token exists in live mode or the valuefalseif the object exists in test mode.
- usedbooleanDetermines if the token has already been used (tokens can only be used once).

#### idstring

#### objectstring, value is "v2.core.account_person_token"

#### createdtimestamp

#### expires_attimestamp

#### livemodeboolean

#### usedboolean
Token must be created with publishable key.
Account cannot exceed a configured concurrency rate limit on updates.

```
curl-X POST https://api.stripe.com/v2/core/accounts/acct_1Nv0FGQ9RKHgCVdK/person_tokens \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\--json'{"given_name": "Jenny","surname": "Rosen","email": "jenny.rosen@example.com","address": {"line1": "27 Fredrick Ave","city": "Brothers","postal_code": "97712","state": "OR","country": "US"},"id_numbers": [{"type": "us_ssn_last_4","value": "0000"}],"relationship": {"owner": true,"percent_ownership": "0.8","representative": true,"title": "CEO"}}'
```

```
curl-X POST https://api.stripe.com/v2/core/accounts/acct_1Nv0FGQ9RKHgCVdK/person_tokens \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\--json'{"given_name": "Jenny","surname": "Rosen","email": "jenny.rosen@example.com","address": {"line1": "27 Fredrick Ave","city": "Brothers","postal_code": "97712","state": "OR","country": "US"},"id_numbers": [{"type": "us_ssn_last_4","value": "0000"}],"relationship": {"owner": true,"percent_ownership": "0.8","representative": true,"title": "CEO"}}'
```

```
{"id":"perstok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY","object":"v2.core.account_person_token","created":"2025-11-17T14:00:00.000Z","expires_at":"2025-11-17T14:10:00.000Z","livemode":true,"used":false}
```

```
{"id":"perstok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY","object":"v2.core.account_person_token","created":"2025-11-17T14:00:00.000Z","expires_at":"2025-11-17T14:10:00.000Z","livemode":true,"used":false}
```

# Retrieve a Person Tokenv2
Retrieves a Person Token associated with an Account.

### Parameters
- account_idstringRequiredThe Account the Person is associated with.
- idstringRequiredThe ID of the Person Token to retrieve.

#### account_idstringRequired

#### idstringRequired

### Returns

### Response attributes
- idstringUnique identifier for the token.
- objectstring, value is "v2.core.account_person_token"String representing the object’s type. Objects of the same type share the same value of the object field.
- createdtimestampTime at which the token was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
- expires_attimestampTime at which the token will expire.
- livemodebooleanHas the valuetrueif the token exists in live mode or the valuefalseif the object exists in test mode.
- usedbooleanDetermines if the token has already been used (tokens can only be used once).

#### idstring

#### objectstring, value is "v2.core.account_person_token"

#### createdtimestamp

#### expires_attimestamp

#### livemodeboolean

#### usedboolean
The resource wasn’t found.
Account cannot exceed a configured concurrency rate limit on updates.

```
curlhttps://api.stripe.com/v2/core/accounts/acct_1Nv0FGQ9RKHgCVdK/person_tokens/perstok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"
```

```
curlhttps://api.stripe.com/v2/core/accounts/acct_1Nv0FGQ9RKHgCVdK/person_tokens/perstok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"
```

```
{"id":"perstok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY","object":"v2.core.account_person_token","created":"2025-11-17T14:00:00.000Z","expires_at":"2025-11-17T14:10:00.000Z","livemode":true,"used":true}
```

```
{"id":"perstok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY","object":"v2.core.account_person_token","created":"2025-11-17T14:00:00.000Z","expires_at":"2025-11-17T14:10:00.000Z","livemode":true,"used":true}
```