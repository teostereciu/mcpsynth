# account_links

*Source: https://docs.stripe.com/api/account_links*

---

# Account Links
Account Links are the means by which a Connect platform grants a connected account permission to accessStripe-hosted applications, such as Connect Onboarding.
Related guide:Connect Onboarding

# The Account Link object

### Attributes
- expires_attimestampThe timestamp at which this account link will expire.
- urlstringThe URL for the account link.

#### expires_attimestamp

#### urlstring

### More attributesExpand all
- objectstring
- createdtimestamp

#### objectstring

#### createdtimestamp

```
{"object":"account_link","created":1680577733,"expires_at":1680578033,"url":"https://connect.stripe.com/setup/c/acct_1Mt0CORHFI4mz9Rw/TqckGNUHg2mG"}
```

```
{"object":"account_link","created":1680577733,"expires_at":1680578033,"url":"https://connect.stripe.com/setup/c/acct_1Mt0CORHFI4mz9Rw/TqckGNUHg2mG"}
```

# Create an account link
Creates an AccountLink object that includes a single-use Stripe URL that the platform can redirect their user to in order to take them through the Connect Onboarding flow.

### Parameters
- accountstringRequiredThe identifier of the account to create an account link for.
- typeenumRequiredThe type of account link the user is requesting.You can create Account Links of typeaccount_updateonly for connected accounts where your platform is responsible for collecting requirements, including Custom accounts. You can’t create them for accounts that have access to a Stripe-hosted Dashboard. If you useConnect embedded components, you can include components that allow your connected accounts to update their own information. For an account without Stripe-hosted Dashboard access where Stripe is liable for negative balances, you must use embedded components.Possible enum valuesaccount_onboardingProvides a form for inputting outstanding requirements. Send the user to the form in this mode to just collect the new information you need.account_updateDisplays the fields that are already populated on the account object, and allows your user to edit previously provided information. Consider framing this as “edit my profile” or “update my verification information”.
- refresh_urlstringRequiredThe URL the user will be redirected to if the account link is expired, has been previously-visited, or is otherwise invalid. The URL you specify should attempt to generate a new account link with the same parameters used to create the original account link, then redirect the user to the new account link’s URL so they can continue with Connect Onboarding. If a new account link cannot be generated or the redirect fails you should display a useful error to the user.
- return_urlstringRequiredThe URL that the user will be redirected to upon leaving or completing the linked flow.

#### accountstringRequired

#### typeenumRequired

[TABLE]
account_onboardingProvides a form for inputting outstanding requirements. Send the user to the form in this mode to just collect the new information you need.
account_updateDisplays the fields that are already populated on the account object, and allows your user to edit previously provided information. Consider framing this as “edit my profile” or “update my verification information”.
[/TABLE]

```
account_onboarding
```

```
account_update
```

#### refresh_urlstringRequired

#### return_urlstringRequired

### More parametersExpand all
- collectenumDeprecated
- collection_optionsobject

#### collectenumDeprecated

#### collection_optionsobject

### Returns
Returns an account link object if the call succeeded.

```
curlhttps://api.stripe.com/v1/account_links \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d account=acct_1Mt0CORHFI4mz9Rw \--data-urlencode refresh_url="https://example.com/reauth"\--data-urlencode return_url="https://example.com/return"\-d type=account_onboarding
```

```
curlhttps://api.stripe.com/v1/account_links \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d account=acct_1Mt0CORHFI4mz9Rw \--data-urlencode refresh_url="https://example.com/reauth"\--data-urlencode return_url="https://example.com/return"\-d type=account_onboarding
```

```
{"object":"account_link","created":1680577733,"expires_at":1680578033,"url":"https://connect.stripe.com/setup/c/acct_1Mt0CORHFI4mz9Rw/TqckGNUHg2mG"}
```

```
{"object":"account_link","created":1680577733,"expires_at":1680578033,"url":"https://connect.stripe.com/setup/c/acct_1Mt0CORHFI4mz9Rw/TqckGNUHg2mG"}
```