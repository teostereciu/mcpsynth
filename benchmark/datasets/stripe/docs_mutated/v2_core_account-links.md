# v2/core/account-links

*Source: https://docs.stripe.com/api/v2/core/account-links*

---

# Account Linksv2
Account Links let a platform create a temporary, single-use URL that an account can use to access a Stripe-hosted flow for collecting or updating required information.

# The Account Link objectv2

### Attributes
- objectstring, value is "v2.core.account_link"String representing the object’s type. Objects of the same type share the same value of the object field.
- accountstringThe ID of the connected account this Account Link applies to.
- createdtimestampThe timestamp at which this Account Link was created.
- expires_attimestampThe timestamp at which this Account Link will expire.
- livemodebooleanHas the valuetrueif the object exists in live mode or the valuefalseif the object exists in test mode.
- urlstringThe URL at which the account can access the Stripe-hosted flow.
- use_caseobjectHash containing usage options.Show child attributes

#### objectstring, value is "v2.core.account_link"

#### accountstring

#### createdtimestamp

#### expires_attimestamp

#### livemodeboolean

#### urlstring

#### use_caseobject

```
{"object":"v2.core.account_link","account":"acct_1Nv0FGQ9RKHgCVdK","created":"2025-03-27T17:15:18.000Z","expires_at":"2025-03-27T17:25:18.000Z","url":"https://accounts.stripe.com/r/acct_1Nv0FGQ9RKHgCVdK#alu_test_61SGhyomRuz7xsw5216SGhyj0ASQdCLwMKdRUF3mi3H6","use_case":{"account_onboarding":{"configurations":["recipient"],"refresh_url":"https://example.com/reauth","return_url":"https://example.com/return"},"type":"account_onboarding"}}
```

```
{"object":"v2.core.account_link","account":"acct_1Nv0FGQ9RKHgCVdK","created":"2025-03-27T17:15:18.000Z","expires_at":"2025-03-27T17:25:18.000Z","url":"https://accounts.stripe.com/r/acct_1Nv0FGQ9RKHgCVdK#alu_test_61SGhyomRuz7xsw5216SGhyj0ASQdCLwMKdRUF3mi3H6","use_case":{"account_onboarding":{"configurations":["recipient"],"refresh_url":"https://example.com/reauth","return_url":"https://example.com/return"},"type":"account_onboarding"}}
```

# Create an Account Linkv2
Creates an AccountLink object that includes a single-use URL that an account can use to access a Stripe-hosted flow for collecting or updating required information.

### Parameters
- accountstringRequiredThe ID of the Account to create link for.
- use_caseobjectRequiredThe use case of the AccountLink.Show child parameters

#### accountstringRequired

#### use_caseobjectRequired

### Returns

### Response attributes
- objectstring, value is "v2.core.account_link"String representing the object’s type. Objects of the same type share the same value of the object field.
- accountstringThe ID of the connected account this Account Link applies to.
- createdtimestampThe timestamp at which this Account Link was created.
- expires_attimestampThe timestamp at which this Account Link will expire.
- livemodebooleanHas the valuetrueif the object exists in live mode or the valuefalseif the object exists in test mode.
- urlstringThe URL at which the account can access the Stripe-hosted flow.
- use_caseobjectHash containing usage options.Show child attributes

#### objectstring, value is "v2.core.account_link"

#### accountstring

#### createdtimestamp

#### expires_attimestamp

#### livemodeboolean

#### urlstring

#### use_caseobject
Accounts v2 is not enabled for your platform.
Account cannot be onboard via v2/core/account_links without specifying the right configurations.
The resource wasn’t found.
Account cannot exceed a configured concurrency rate limit on updates.

```
curl-X POST https://api.stripe.com/v2/core/account_links \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\--json'{"account": "acct_1Nv0FGQ9RKHgCVdK","use_case": {"type": "account_onboarding","account_onboarding": {"configurations": ["recipient"],"return_url": "https://example.com/return","refresh_url": "https://example.com/reauth"}}}'
```

```
curl-X POST https://api.stripe.com/v2/core/account_links \-H"Authorization: Bearersk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz"\-H"Stripe-Version: 2026-02-25.preview"\--json'{"account": "acct_1Nv0FGQ9RKHgCVdK","use_case": {"type": "account_onboarding","account_onboarding": {"configurations": ["recipient"],"return_url": "https://example.com/return","refresh_url": "https://example.com/reauth"}}}'
```

```
{"object":"v2.core.account_link","account":"acct_1Nv0FGQ9RKHgCVdK","created":"2025-03-27T17:15:18.000Z","expires_at":"2025-03-27T17:25:18.000Z","livemode":true,"url":"https://accounts.stripe.com/r/acct_1Nv0FGQ9RKHgCVdK#alu_test_61SGhyomRuz7xsw5216SGhyj0ASQdCLwMKdRUF3mi3H6","use_case":{"account_onboarding":{"configurations":["recipient"],"refresh_url":"https://example.com/reauth","return_url":"https://example.com/return"},"type":"account_onboarding"}}
```

```
{"object":"v2.core.account_link","account":"acct_1Nv0FGQ9RKHgCVdK","created":"2025-03-27T17:15:18.000Z","expires_at":"2025-03-27T17:25:18.000Z","livemode":true,"url":"https://accounts.stripe.com/r/acct_1Nv0FGQ9RKHgCVdK#alu_test_61SGhyomRuz7xsw5216SGhyj0ASQdCLwMKdRUF3mi3H6","use_case":{"account_onboarding":{"configurations":["recipient"],"refresh_url":"https://example.com/reauth","return_url":"https://example.com/return"},"type":"account_onboarding"}}
```