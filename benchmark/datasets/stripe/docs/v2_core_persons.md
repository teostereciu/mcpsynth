# v2/core/persons

*Source: https://docs.stripe.com/api/v2/core/persons*

---

# Personsv2
A Person represents an individual associated with an Account’s identity (for example, an owner, director, executive, or representative). Use Persons to provide and update identity information for verification and compliance.

# The Person objectv2

### Attributes
- idstringUnique identifier for the Person.
- objectstring, value is "v2.core.account_person"String representing the object’s type. Objects of the same type share the same value of the object field.
- accountstringThe account ID which the individual belongs to.
- additional_addressesnullablearray of objectsAdditional addresses associated with the person.Show child attributes
- additional_namesnullablearray of objectsAdditional names (e.g. aliases) associated with the person.Show child attributes
- additional_terms_of_servicenullableobjectAttestations of accepted terms of service agreements.Show child attributes
- addressnullableobjectThe person’s residential address.Show child attributes
- createdtimestampTime at which the object was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
- date_of_birthnullableobjectThe person’s date of birth.Show child attributes
- documentsnullableobjectDocuments that may be submitted to satisfy various informational requests.Show child attributes
- emailnullablestringThe person’s email address.
- given_namenullablestringThe person’s first name.
- id_numbersnullablearray of objectsThe identification numbers (e.g., SSN) associated with the person.Show child attributes
- legal_gendernullableenumThe person’s gender (International regulations require either “male” or “female”).Possible enum valuesfemaleFemale gender person.maleMale gender person.
- livemodebooleanHas the valuetrueif the object exists in live mode or the valuefalseif the object exists in test mode.
- metadatanullablemapSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- nationalitiesnullablearray of enumsThe countries where the person is a national. Two-letter country code (ISO 3166-1 alpha-2).
- phonenullablestringThe person’s phone number.
- political_exposurenullableenumThe person’s political exposure.Possible enum valuesexistingThe person has disclosed that they do have political exposure.noneThe person has disclosed that they have no political exposure.
- relationshipnullableobjectThe relationship that this person has with the Account’s business or legal entity.Show child attributes
- script_addressesnullableobjectThe script addresses (e.g., non-Latin characters) associated with the person.Show child attributes
- script_namesnullableobjectThe script names (e.g. non-Latin characters) associated with the person.Show child attributes
- surnamenullablestringThe person’s last name.
- updatedtimestampTime at which the object was last updated. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

#### idstring

#### objectstring, value is "v2.core.account_person"

#### accountstring

#### additional_addressesnullablearray of objects

#### additional_namesnullablearray of objects

#### additional_terms_of_servicenullableobject

#### addressnullableobject

#### createdtimestamp

#### date_of_birthnullableobject

#### documentsnullableobject

#### emailnullablestring

#### given_namenullablestring

#### id_numbersnullablearray of objects

#### legal_gendernullableenum

[TABLE]
femaleFemale gender person.
maleMale gender person.
[/TABLE]

#### livemodeboolean

#### metadatanullablemap

#### nationalitiesnullablearray of enums

#### phonenullablestring

#### political_exposurenullableenum

[TABLE]
existingThe person has disclosed that they do have political exposure.
noneThe person has disclosed that they have no political exposure.
[/TABLE]

#### relationshipnullableobject

#### script_addressesnullableobject

#### script_namesnullableobject

#### surnamenullablestring

#### updatedtimestamp

```
{"id":"person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY","object":"v2.core.account_person","account":"acct_1Nv0FGQ9RKHgCVdK","additional_addresses":[],"additional_names":[],"address":{"city":"Brothers","country":"us","line1":"27 Fredrick Ave","postal_code":"97712","state":"OR"},"created":"2024-11-26T17:10:07.000Z","email":"jenny.rosen@example.com","given_name":"Jenny","id_numbers":[{"type":"us_ssn_last_4"}],"metadata":{},"nationalities":[],"relationship":{"owner":true,"percent_ownership":"0.8","representative":true,"title":"CEO"},"surname":"Rosen","updated":"2024-11-26T17:10:07.000Z"}
```

```
{"id":"person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY","object":"v2.core.account_person","account":"acct_1Nv0FGQ9RKHgCVdK","additional_addresses":[],"additional_names":[],"address":{"city":"Brothers","country":"us","line1":"27 Fredrick Ave","postal_code":"97712","state":"OR"},"created":"2024-11-26T17:10:07.000Z","email":"jenny.rosen@example.com","given_name":"Jenny","id_numbers":[{"type":"us_ssn_last_4"}],"metadata":{},"nationalities":[],"relationship":{"owner":true,"percent_ownership":"0.8","representative":true,"title":"CEO"},"surname":"Rosen","updated":"2024-11-26T17:10:07.000Z"}
```

# Create a personv2
Create a Person. Adds an individual to an Account’s identity. You can set relationship attributes and identity information at creation.

### Parameters
- account_idstringRequiredAccount the Person should be associated with.
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
- person_tokenstringThe person token generated by the person token api.
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

#### person_tokenstring

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
- idstringUnique identifier for the Person.
- objectstring, value is "v2.core.account_person"String representing the object’s type. Objects of the same type share the same value of the object field.
- accountstringThe account ID which the individual belongs to.
- additional_addressesnullablearray of objectsAdditional addresses associated with the person.Show child attributes
- additional_namesnullablearray of objectsAdditional names (e.g. aliases) associated with the person.Show child attributes
- additional_terms_of_servicenullableobjectAttestations of accepted terms of service agreements.Show child attributes
- addressnullableobjectThe person’s residential address.Show child attributes
- createdtimestampTime at which the object was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
- date_of_birthnullableobjectThe person’s date of birth.Show child attributes
- documentsnullableobjectDocuments that may be submitted to satisfy various informational requests.Show child attributes
- emailnullablestringThe person’s email address.
- given_namenullablestringThe person’s first name.
- id_numbersnullablearray of objectsThe identification numbers (e.g., SSN) associated with the person.Show child attributes
- legal_gendernullableenumThe person’s gender (International regulations require either “male” or “female”).Possible enum valuesfemaleFemale gender person.maleMale gender person.
- livemodebooleanHas the valuetrueif the object exists in live mode or the valuefalseif the object exists in test mode.
- metadatanullablemapSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- nationalitiesnullablearray of enumsThe countries where the person is a national. Two-letter country code (ISO 3166-1 alpha-2).
- phonenullablestringThe person’s phone number.
- political_exposurenullableenumThe person’s political exposure.Possible enum valuesexistingThe person has disclosed that they do have political exposure.noneThe person has disclosed that they have no political exposure.
- relationshipnullableobjectThe relationship that this person has with the Account’s business or legal entity.Show child attributes
- script_addressesnullableobjectThe script addresses (e.g., non-Latin characters) associated with the person.Show child attributes
- script_namesnullableobjectThe script names (e.g. non-Latin characters) associated with the person.Show child attributes
- surnamenullablestringThe person’s last name.
- updatedtimestampTime at which the object was last updated. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

#### idstring

#### objectstring, value is "v2.core.account_person"

#### accountstring

#### additional_addressesnullablearray of objects

#### additional_namesnullablearray of objects

#### additional_terms_of_servicenullableobject

#### addressnullableobject

#### createdtimestamp

#### date_of_birthnullableobject

#### documentsnullableobject

#### emailnullablestring

#### given_namenullablestring

#### id_numbersnullablearray of objects

#### legal_gendernullableenum

[TABLE]
femaleFemale gender person.
maleMale gender person.
[/TABLE]

#### livemodeboolean

#### metadatanullablemap

#### nationalitiesnullablearray of enums

#### phonenullablestring

#### political_exposurenullableenum

[TABLE]
existingThe person has disclosed that they do have political exposure.
noneThe person has disclosed that they have no political exposure.
[/TABLE]

#### relationshipnullableobject

#### script_addressesnullableobject

#### script_namesnullableobject

#### surnamenullablestring

#### updatedtimestamp
Account is not yet compatible with V2 APIs.
Accounts v2 is not enabled for your platform.
More than one legal guardian is added to an account.
More than one representative is added to an account.
Additional terms of service are signed by someone other than the legal guardian.
Invalid characters are provided for address fields.
Address country doesn’t match identity country.
Registered/script address country doesn’t match residential address country.
Address country is required but not provided.
Address postal code is invalid.
Address state is invalid.
Address town is invalid.
There can only be one authorizer.
An authorizer cannot be a representative.
Representative date of birth does not meet the age limit.
Representative date of birth is provided an invalid date or a future date.
Provided file tokens for documents are invalid, not found, deleted, or belong to a different account.
Provided file tokens for documents are of the wrong purpose.
Duplicate person is added to an account.
Email contains unsupported domain.
Incorrect email is provided.
Provided ID number is of the wrong format for the given type.
Theidentity.countryvalue is required but not provided.
A person token is created with one account but used on a different account.
Incorrect ID number is provided for a country.
The incorrect token type is provided .
Additional person is added for an individual business type.
Some relationships are specific to type, structure, and country.
Invalid IP address is provided.
Person is designated as both legal guardian and representative.
A legal guardian may not be added to the account without an existing representative.
Kana Kanji script addresses must have JP country.
Parameter cannot be passed alongside person_token.
Error returned when relationship.owner is set to true but the ownership percentage is set to 0%.
Person token required for platforms in mandated countries (e.g., France).
Phone number is invalid.
Postal code is required for Japanese addresses.
Provided script characters are invalid for the script.
The token is re-used with a different idempotency key.
Token has expired.
Total ownership percentages of all Persons on the account exceeds 100%.
Address is in an unsupported postal code.
Address is in an unsupported state.
V1 Account ID cannot be used in V2 Account APIs.
V1 Customer ID cannot be used in V2 Account APIs.
A v1 token ID is passed in v2 APIs.
Invalid person token.
Account cannot exceed a configured concurrency rate limit on updates.

```
curl-X POST https://api.stripe.com/v2/core/accounts/acct_1Nv0FGQ9RKHgCVdK/persons \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\--json'{"given_name": "Jenny","surname": "Rosen","email": "jenny.rosen@example.com","address": {"line1": "27 Fredrick Ave","city": "Brothers","postal_code": "97712","state": "OR","country": "us"},"id_numbers": [{"type": "us_ssn_last_4","value": "0000"}],"relationship": {"owner": true,"percent_ownership": "0.8","representative": true,"title": "CEO"}}'
```

```
curl-X POST https://api.stripe.com/v2/core/accounts/acct_1Nv0FGQ9RKHgCVdK/persons \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\--json'{"given_name": "Jenny","surname": "Rosen","email": "jenny.rosen@example.com","address": {"line1": "27 Fredrick Ave","city": "Brothers","postal_code": "97712","state": "OR","country": "us"},"id_numbers": [{"type": "us_ssn_last_4","value": "0000"}],"relationship": {"owner": true,"percent_ownership": "0.8","representative": true,"title": "CEO"}}'
```

```
{"id":"person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY","object":"v2.core.account_person","account":"acct_1Nv0FGQ9RKHgCVdK","additional_addresses":[],"additional_names":[],"address":{"city":"Brothers","country":"us","line1":"27 Fredrick Ave","postal_code":"97712","state":"OR"},"created":"2024-11-26T17:10:07.000Z","email":"jenny.rosen@example.com","given_name":"Jenny","id_numbers":[{"type":"us_ssn_last_4"}],"livemode":true,"metadata":{},"nationalities":[],"relationship":{"owner":true,"percent_ownership":"0.8","representative":true,"title":"CEO"},"surname":"Rosen","updated":"2024-11-26T17:10:07.000Z"}
```

```
{"id":"person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY","object":"v2.core.account_person","account":"acct_1Nv0FGQ9RKHgCVdK","additional_addresses":[],"additional_names":[],"address":{"city":"Brothers","country":"us","line1":"27 Fredrick Ave","postal_code":"97712","state":"OR"},"created":"2024-11-26T17:10:07.000Z","email":"jenny.rosen@example.com","given_name":"Jenny","id_numbers":[{"type":"us_ssn_last_4"}],"livemode":true,"metadata":{},"nationalities":[],"relationship":{"owner":true,"percent_ownership":"0.8","representative":true,"title":"CEO"},"surname":"Rosen","updated":"2024-11-26T17:10:07.000Z"}
```

# Update a personv2
Updates a Person associated with an Account.

### Parameters
- account_idstringRequiredThe Account the Person is associated with.
- idstringRequiredThe ID of the Person to update.
- additional_addressesarray of objectsAdditional addresses associated with the person.Show child parameters
- additional_namesarray of objectsAdditional names (e.g. aliases) associated with the person.Show child parameters
- additional_terms_of_serviceobjectAttestations of accepted terms of service agreements.Show child parameters
- addressobjectThe primary address associated with the person.Show child parameters
- date_of_birthobjectThe person’s date of birth.Show child parameters
- documentsobjectDocuments that may be submitted to satisfy various informational requests.Show child parameters
- emailstringEmail.
- given_namestringThe person’s first name.
- id_numbersarray of objectsThe identification numbers (e.g., SSN) associated with the person.Show child parameters
- legal_genderenumThe person’s gender (International regulations require either “male” or “female”).Possible enum valuesfemaleFemale gender person.maleMale gender person.
- metadatamapSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- nationalitiesarray of enumsThe nationalities (countries) this person is associated with.
- person_tokenstringThe person token generated by the person token api.
- phonestringThe phone number for this person.
- political_exposureenumThe person’s political exposure.Possible enum valuesexistingThe person has disclosed that they do have political exposure.noneThe person has disclosed that they have no political exposure.
- relationshipobjectThe relationship that this person has with the Account’s business or legal entity.Show child parameters
- script_addressesobjectThe script addresses (e.g., non-Latin characters) associated with the person.Show child parameters
- script_namesobjectThe script names (e.g. non-Latin characters) associated with the person.Show child parameters
- surnamestringThe person’s last name.

#### account_idstringRequired

#### idstringRequired

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

#### person_tokenstring

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
- idstringUnique identifier for the Person.
- objectstring, value is "v2.core.account_person"String representing the object’s type. Objects of the same type share the same value of the object field.
- accountstringThe account ID which the individual belongs to.
- additional_addressesnullablearray of objectsAdditional addresses associated with the person.Show child attributes
- additional_namesnullablearray of objectsAdditional names (e.g. aliases) associated with the person.Show child attributes
- additional_terms_of_servicenullableobjectAttestations of accepted terms of service agreements.Show child attributes
- addressnullableobjectThe person’s residential address.Show child attributes
- createdtimestampTime at which the object was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
- date_of_birthnullableobjectThe person’s date of birth.Show child attributes
- documentsnullableobjectDocuments that may be submitted to satisfy various informational requests.Show child attributes
- emailnullablestringThe person’s email address.
- given_namenullablestringThe person’s first name.
- id_numbersnullablearray of objectsThe identification numbers (e.g., SSN) associated with the person.Show child attributes
- legal_gendernullableenumThe person’s gender (International regulations require either “male” or “female”).Possible enum valuesfemaleFemale gender person.maleMale gender person.
- livemodebooleanHas the valuetrueif the object exists in live mode or the valuefalseif the object exists in test mode.
- metadatanullablemapSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- nationalitiesnullablearray of enumsThe countries where the person is a national. Two-letter country code (ISO 3166-1 alpha-2).
- phonenullablestringThe person’s phone number.
- political_exposurenullableenumThe person’s political exposure.Possible enum valuesexistingThe person has disclosed that they do have political exposure.noneThe person has disclosed that they have no political exposure.
- relationshipnullableobjectThe relationship that this person has with the Account’s business or legal entity.Show child attributes
- script_addressesnullableobjectThe script addresses (e.g., non-Latin characters) associated with the person.Show child attributes
- script_namesnullableobjectThe script names (e.g. non-Latin characters) associated with the person.Show child attributes
- surnamenullablestringThe person’s last name.
- updatedtimestampTime at which the object was last updated. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

#### idstring

#### objectstring, value is "v2.core.account_person"

#### accountstring

#### additional_addressesnullablearray of objects

#### additional_namesnullablearray of objects

#### additional_terms_of_servicenullableobject

#### addressnullableobject

#### createdtimestamp

#### date_of_birthnullableobject

#### documentsnullableobject

#### emailnullablestring

#### given_namenullablestring

#### id_numbersnullablearray of objects

#### legal_gendernullableenum

[TABLE]
femaleFemale gender person.
maleMale gender person.
[/TABLE]

#### livemodeboolean

#### metadatanullablemap

#### nationalitiesnullablearray of enums

#### phonenullablestring

#### political_exposurenullableenum

[TABLE]
existingThe person has disclosed that they do have political exposure.
noneThe person has disclosed that they have no political exposure.
[/TABLE]

#### relationshipnullableobject

#### script_addressesnullableobject

#### script_namesnullableobject

#### surnamenullablestring

#### updatedtimestamp
Account is not yet compatible with V2 APIs.
Accounts v2 is not enabled for your platform.
More than one legal guardian is added to an account.
More than one representative is added to an account.
Additional terms of service are signed by someone other than the legal guardian.
Invalid characters are provided for address fields.
Address country doesn’t match identity country.
Registered/script address country doesn’t match residential address country.
Address country is required but not provided.
Address postal code is invalid.
Address state is invalid.
Address town is invalid.
Representative date of birth does not meet the age limit.
Representative date of birth is provided an invalid date or a future date.
Provided file tokens for documents are invalid, not found, deleted, or belong to a different account.
Provided file tokens for documents are of the wrong purpose.
Duplicate person is added to an account.
Email contains unsupported domain.
Incorrect email is provided.
Provided ID number is of the wrong format for the given type.
Theidentity.countryvalue is required but not provided.
Identity param has been made immutable due to the state of the account.
A person token is created with one account but used on a different account.
Incorrect ID number is provided for a country.
The incorrect token type is provided .
Invalid IP address is provided.
Person is designated as both legal guardian and representative.
A legal guardian may not be added to the account without an existing representative.
Kana Kanji script addresses must have JP country.
Parameter cannot be passed alongside person_token.
Error returned when relationship.owner is set to true but the ownership percentage is set to 0%.
Person token required for platforms in mandated countries (e.g., France).
Phone number is invalid.
Postal code is required for Japanese addresses.
Provided script characters are invalid for the script.
The token is re-used with a different idempotency key.
Token has expired.
Total ownership percentages of all Persons on the account exceeds 100%.
Address is in an unsupported postal code.
Address is in an unsupported state.
V1 Account ID cannot be used in V2 Account APIs.
V1 Customer ID cannot be used in V2 Account APIs.
A v1 token ID is passed in v2 APIs.
Invalid person token.
The resource wasn’t found.
Account cannot exceed a configured concurrency rate limit on updates.

```
curl-X POST https://api.stripe.com/v2/core/accounts/acct_1Nv0FGQ9RKHgCVdK/persons/person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\--json'{"date_of_birth": {"day": 28,"month": 1,"year": 2000}}'
```

```
curl-X POST https://api.stripe.com/v2/core/accounts/acct_1Nv0FGQ9RKHgCVdK/persons/person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\--json'{"date_of_birth": {"day": 28,"month": 1,"year": 2000}}'
```

```
{"id":"person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY","object":"v2.core.account_person","account":"acct_1Nv0FGQ9RKHgCVdK","additional_addresses":[],"additional_names":[],"address":{"city":"Brothers","country":"us","line1":"27 Fredrick Ave","postal_code":"97712","state":"OR"},"created":"2024-11-26T17:10:07.000Z","date_of_birth":{"day":28,"month":1,"year":2000},"email":"jenny.rosen@example.com","given_name":"Jenny","id_numbers":[{"type":"us_ssn_last_4"}],"livemode":true,"metadata":{},"nationalities":[],"relationship":{"owner":true,"percent_ownership":"0.8","representative":true,"title":"CEO"},"surname":"Rosen","updated":"2024-11-26T17:12:55.000Z"}
```

```
{"id":"person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY","object":"v2.core.account_person","account":"acct_1Nv0FGQ9RKHgCVdK","additional_addresses":[],"additional_names":[],"address":{"city":"Brothers","country":"us","line1":"27 Fredrick Ave","postal_code":"97712","state":"OR"},"created":"2024-11-26T17:10:07.000Z","date_of_birth":{"day":28,"month":1,"year":2000},"email":"jenny.rosen@example.com","given_name":"Jenny","id_numbers":[{"type":"us_ssn_last_4"}],"livemode":true,"metadata":{},"nationalities":[],"relationship":{"owner":true,"percent_ownership":"0.8","representative":true,"title":"CEO"},"surname":"Rosen","updated":"2024-11-26T17:12:55.000Z"}
```

# Retrieve a Personv2
Retrieves a Person associated with an Account.

### Parameters
- account_idstringRequiredThe Account the Person is associated with.
- idstringRequiredThe ID of the Person to retrieve.

#### account_idstringRequired

#### idstringRequired

### Returns

### Response attributes
- idstringUnique identifier for the Person.
- objectstring, value is "v2.core.account_person"String representing the object’s type. Objects of the same type share the same value of the object field.
- accountstringThe account ID which the individual belongs to.
- additional_addressesnullablearray of objectsAdditional addresses associated with the person.Show child attributes
- additional_namesnullablearray of objectsAdditional names (e.g. aliases) associated with the person.Show child attributes
- additional_terms_of_servicenullableobjectAttestations of accepted terms of service agreements.Show child attributes
- addressnullableobjectThe person’s residential address.Show child attributes
- createdtimestampTime at which the object was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
- date_of_birthnullableobjectThe person’s date of birth.Show child attributes
- documentsnullableobjectDocuments that may be submitted to satisfy various informational requests.Show child attributes
- emailnullablestringThe person’s email address.
- given_namenullablestringThe person’s first name.
- id_numbersnullablearray of objectsThe identification numbers (e.g., SSN) associated with the person.Show child attributes
- legal_gendernullableenumThe person’s gender (International regulations require either “male” or “female”).Possible enum valuesfemaleFemale gender person.maleMale gender person.
- livemodebooleanHas the valuetrueif the object exists in live mode or the valuefalseif the object exists in test mode.
- metadatanullablemapSet of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- nationalitiesnullablearray of enumsThe countries where the person is a national. Two-letter country code (ISO 3166-1 alpha-2).
- phonenullablestringThe person’s phone number.
- political_exposurenullableenumThe person’s political exposure.Possible enum valuesexistingThe person has disclosed that they do have political exposure.noneThe person has disclosed that they have no political exposure.
- relationshipnullableobjectThe relationship that this person has with the Account’s business or legal entity.Show child attributes
- script_addressesnullableobjectThe script addresses (e.g., non-Latin characters) associated with the person.Show child attributes
- script_namesnullableobjectThe script names (e.g. non-Latin characters) associated with the person.Show child attributes
- surnamenullablestringThe person’s last name.
- updatedtimestampTime at which the object was last updated. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.

#### idstring

#### objectstring, value is "v2.core.account_person"

#### accountstring

#### additional_addressesnullablearray of objects

#### additional_namesnullablearray of objects

#### additional_terms_of_servicenullableobject

#### addressnullableobject

#### createdtimestamp

#### date_of_birthnullableobject

#### documentsnullableobject

#### emailnullablestring

#### given_namenullablestring

#### id_numbersnullablearray of objects

#### legal_gendernullableenum

[TABLE]
femaleFemale gender person.
maleMale gender person.
[/TABLE]

#### livemodeboolean

#### metadatanullablemap

#### nationalitiesnullablearray of enums

#### phonenullablestring

#### political_exposurenullableenum

[TABLE]
existingThe person has disclosed that they do have political exposure.
noneThe person has disclosed that they have no political exposure.
[/TABLE]

#### relationshipnullableobject

#### script_addressesnullableobject

#### script_namesnullableobject

#### surnamenullablestring

#### updatedtimestamp
Account is not yet compatible with V2 APIs.
Accounts v2 is not enabled for your platform.
V1 Account ID cannot be used in V2 Account APIs.
V1 Customer ID cannot be used in V2 Account APIs.
The resource wasn’t found.
Account cannot exceed a configured concurrency rate limit on updates.

```
curlhttps://api.stripe.com/v2/core/accounts/acct_1Nv0FGQ9RKHgCVdK/persons/person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"
```

```
curlhttps://api.stripe.com/v2/core/accounts/acct_1Nv0FGQ9RKHgCVdK/persons/person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"
```

```
{"id":"person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY","object":"v2.core.account_person","account":"acct_1Nv0FGQ9RKHgCVdK","additional_addresses":[],"additional_names":[],"address":{"city":"Brothers","country":"us","line1":"27 Fredrick Ave","postal_code":"97712","state":"OR"},"created":"2024-11-26T17:10:07.000Z","date_of_birth":{"day":28,"month":1,"year":2000},"email":"jenny.rosen@example.com","given_name":"Jenny","id_numbers":[{"type":"us_ssn_last_4"}],"livemode":true,"metadata":{},"nationalities":[],"relationship":{"owner":true,"percent_ownership":"0.8","representative":true,"title":"CEO"},"surname":"Rosen","updated":"2024-11-26T17:12:55.000Z"}
```

```
{"id":"person_test_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY","object":"v2.core.account_person","account":"acct_1Nv0FGQ9RKHgCVdK","additional_addresses":[],"additional_names":[],"address":{"city":"Brothers","country":"us","line1":"27 Fredrick Ave","postal_code":"97712","state":"OR"},"created":"2024-11-26T17:10:07.000Z","date_of_birth":{"day":28,"month":1,"year":2000},"email":"jenny.rosen@example.com","given_name":"Jenny","id_numbers":[{"type":"us_ssn_last_4"}],"livemode":true,"metadata":{},"nationalities":[],"relationship":{"owner":true,"percent_ownership":"0.8","representative":true,"title":"CEO"},"surname":"Rosen","updated":"2024-11-26T17:12:55.000Z"}
```