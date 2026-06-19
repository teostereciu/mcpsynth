# v2/core/account-tokens

*Source: https://docs.stripe.com/api/v2/core/account-tokens*

---

# Account Tokensv2
Account tokens are single-use tokens which tokenize company/individual/business information, and are used for creating or updating an Account.

# The Account Token objectv2

### Attributes
- idstringUnique identifier for the token.
- objectstring, value is "v2.core.account_token"String representing the object’s type. Objects of the same type share the same value of the object field.
- createdtimestampTime at which the token was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
- expires_attimestampTime at which the token will expire.
- livemodebooleanHas the valuetrueif the token exists in live mode or the valuefalseif the object exists in test mode.
- usedbooleanDetermines if the token has already been used (tokens can only be used once).

#### idstring

#### objectstring, value is "v2.core.account_token"

#### createdtimestamp

#### expires_attimestamp

#### livemodeboolean

#### usedboolean

```
{"id":"accttok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY","object":"v2.core.account_token","created":"2025-11-17T14:00:00.000Z","expires_at":"2025-11-17T14:10:00.000Z","livemode":true,"used":false}
```

```
{"id":"accttok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY","object":"v2.core.account_token","created":"2025-11-17T14:00:00.000Z","expires_at":"2025-11-17T14:10:00.000Z","livemode":true,"used":false}
```

# Create an Account Tokenv2
Creates an Account Token.

### Parameters
- contact_emailstringThe default contact email address for the Account. Required when configuring the account as a merchant or recipient.
- contact_phonestringThe default contact phone for the Account.
- display_namestringA descriptive name for the Account. This name will be surfaced in the Stripe Dashboard and on any invoices sent to the Account.
- identityobjectInformation about the company, individual, and business represented by the Account.Show child parameters

#### contact_emailstring

#### contact_phonestring

#### display_namestring

#### identityobject

### Returns

### Response attributes
- idstringUnique identifier for the token.
- objectstring, value is "v2.core.account_token"String representing the object’s type. Objects of the same type share the same value of the object field.
- createdtimestampTime at which the token was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
- expires_attimestampTime at which the token will expire.
- livemodebooleanHas the valuetrueif the token exists in live mode or the valuefalseif the object exists in test mode.
- usedbooleanDetermines if the token has already been used (tokens can only be used once).

#### idstring

#### objectstring, value is "v2.core.account_token"

#### createdtimestamp

#### expires_attimestamp

#### livemodeboolean

#### usedboolean
Token must be created with publishable key.
Account cannot exceed a configured concurrency rate limit on updates.

```
curl-X POST https://api.stripe.com/v2/core/account_tokens \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\--json'{"contact_email": "furever@example.com","display_name": "Furever","identity": {"attestations": {"terms_of_service": {"account": {"shown_and_accepted": true}}},"entity_type": "company","business_details": {"registered_name": "Furever"}}}'
```

```
curl-X POST https://api.stripe.com/v2/core/account_tokens \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\--json'{"contact_email": "furever@example.com","display_name": "Furever","identity": {"attestations": {"terms_of_service": {"account": {"shown_and_accepted": true}}},"entity_type": "company","business_details": {"registered_name": "Furever"}}}'
```

```
{"id":"accttok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY","object":"v2.core.account_token","created":"2025-11-17T14:00:00.000Z","expires_at":"2025-11-17T14:10:00.000Z","livemode":true,"used":false}
```

```
{"id":"accttok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY","object":"v2.core.account_token","created":"2025-11-17T14:00:00.000Z","expires_at":"2025-11-17T14:10:00.000Z","livemode":true,"used":false}
```

# Retrieve an Account Tokenv2
Retrieves an Account Token.

### Parameters
- idstringRequiredThe ID of the Account Token to retrieve.

#### idstringRequired

### Returns

### Response attributes
- idstringUnique identifier for the token.
- objectstring, value is "v2.core.account_token"String representing the object’s type. Objects of the same type share the same value of the object field.
- createdtimestampTime at which the token was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
- expires_attimestampTime at which the token will expire.
- livemodebooleanHas the valuetrueif the token exists in live mode or the valuefalseif the object exists in test mode.
- usedbooleanDetermines if the token has already been used (tokens can only be used once).

#### idstring

#### objectstring, value is "v2.core.account_token"

#### createdtimestamp

#### expires_attimestamp

#### livemodeboolean

#### usedboolean
The resource wasn’t found.
Account cannot exceed a configured concurrency rate limit on updates.

```
curlhttps://api.stripe.com/v2/core/account_tokens/accttok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"
```

```
curlhttps://api.stripe.com/v2/core/account_tokens/accttok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"
```

```
{"id":"accttok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY","object":"v2.core.account_token","created":"2025-11-17T14:00:00.000Z","expires_at":"2025-11-17T14:10:00.000Z","livemode":true,"used":true}
```

```
{"id":"accttok_61RS0CgWt1xBt8M1Q16RS0Cg0WSQO5ZXUVpZxZ9tAIbY","object":"v2.core.account_token","created":"2025-11-17T14:00:00.000Z","expires_at":"2025-11-17T14:10:00.000Z","livemode":true,"used":true}
```