# capabilities

*Source: https://docs.stripe.com/api/capabilities*

---

# Capabilities
This is an object representing a capability for a Stripe account.
Related guide:Account capabilities

# The Capability object

### Attributes
- idstringThe identifier for the capability.
- accountstringExpandableThe account for which the capability enables functionality.
- requestedbooleanWhether the capability has been requested.
- requirementsobjectInformation about the requirements for the capability, including what information needs to be collected, and by when.Show child attributes
- statusenumThe status of the capability.Possible enum valuesactiveThe capability is active.inactiveThe capability is inactive.pendingThe capability is inactive with requirements pending verification.unrequestedThe capability is unrequested.

#### idstring

#### accountstringExpandable

#### requestedboolean

#### requirementsobject

#### statusenum

[TABLE]
activeThe capability is active.
inactiveThe capability is inactive.
pendingThe capability is inactive with requirements pending verification.
unrequestedThe capability is unrequested.
[/TABLE]

```
unrequested
```

### More attributesExpand all
- objectstring
- future_requirementsobject
- requested_atnullabletimestamp

#### objectstring

#### future_requirementsobject

#### requested_atnullabletimestamp

```
{"id":"card_payments","object":"capability","account":"acct_1032D82eZvKYlo2C","future_requirements":{"alternatives":[],"current_deadline":null,"currently_due":[],"disabled_reason":null,"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"requested":true,"requested_at":1688491010,"requirements":{"alternatives":[],"current_deadline":null,"currently_due":[],"disabled_reason":null,"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"status":"inactive"}
```

```
{"id":"card_payments","object":"capability","account":"acct_1032D82eZvKYlo2C","future_requirements":{"alternatives":[],"current_deadline":null,"currently_due":[],"disabled_reason":null,"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"requested":true,"requested_at":1688491010,"requirements":{"alternatives":[],"current_deadline":null,"currently_due":[],"disabled_reason":null,"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"status":"inactive"}
```

# Update an Account Capability
Updates an existing Account Capability. Request or remove a capability by updating itsrequestedparameter.

### Parameters
- requestedbooleanTo request a new capability for an account, pass true. There can be a delay before the requested capability becomes active. If the capability has any activation requirements, the response includes them in therequirementsarrays.If a capability isn’t permanent, you can remove it from the account by passing false. Some capabilities are permanent after they’ve been requested. Attempting to remove a permanent capability returns an error.

#### requestedboolean

### More parametersExpand all
- previewbooleanPreview feature

#### previewbooleanPreview feature

### Returns
Returns an Account Capability object.

```
curlhttps://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/capabilities/card_payments \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d requested=true
```

```
curlhttps://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/capabilities/card_payments \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d requested=true
```

```
{"id":"card_payments","object":"capability","account":"acct_1032D82eZvKYlo2C","future_requirements":{"alternatives":[],"current_deadline":null,"currently_due":[],"disabled_reason":null,"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"requested":true,"requested_at":1688491010,"requirements":{"alternatives":[],"current_deadline":null,"currently_due":[],"disabled_reason":null,"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"status":"inactive"}
```

```
{"id":"card_payments","object":"capability","account":"acct_1032D82eZvKYlo2C","future_requirements":{"alternatives":[],"current_deadline":null,"currently_due":[],"disabled_reason":null,"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"requested":true,"requested_at":1688491010,"requirements":{"alternatives":[],"current_deadline":null,"currently_due":[],"disabled_reason":null,"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"status":"inactive"}
```

# Retrieve an Account Capability
Retrieves information about the specified Account Capability.

### Parameters
Noparameters.

### Returns
Returns an Account Capability object.

```
curlhttps://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/capabilities/card_payments \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/capabilities/card_payments \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"card_payments","object":"capability","account":"acct_1032D82eZvKYlo2C","future_requirements":{"alternatives":[],"current_deadline":null,"currently_due":[],"disabled_reason":null,"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"requested":true,"requested_at":1688491010,"requirements":{"alternatives":[],"current_deadline":null,"currently_due":[],"disabled_reason":null,"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"status":"inactive"}
```

```
{"id":"card_payments","object":"capability","account":"acct_1032D82eZvKYlo2C","future_requirements":{"alternatives":[],"current_deadline":null,"currently_due":[],"disabled_reason":null,"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"requested":true,"requested_at":1688491010,"requirements":{"alternatives":[],"current_deadline":null,"currently_due":[],"disabled_reason":null,"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"status":"inactive"}
```

# List all account capabilities
Returns a list of capabilities associated with the account. The capabilities are returned sorted by creation date, with the most recent capability appearing first.

### Parameters
Noparameters.

### Returns
Adictionarywith adataproperty that contains an array of the capabilities of this account. Each entry in the array is a separate capability object.

```
curlhttps://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/capabilities \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/capabilities \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"object":"list","url":"/v1/accounts/acct_1032D82eZvKYlo2C/capabilities","has_more":false,"data":[{"id":"card_payments","object":"capability","account":"acct_1032D82eZvKYlo2C","future_requirements":{"alternatives":[],"current_deadline":null,"currently_due":[],"disabled_reason":null,"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"requested":true,"requested_at":1693951912,"requirements":{"alternatives":[],"current_deadline":null,"currently_due":[],"disabled_reason":null,"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"status":"inactive"}]}
```

```
{"object":"list","url":"/v1/accounts/acct_1032D82eZvKYlo2C/capabilities","has_more":false,"data":[{"id":"card_payments","object":"capability","account":"acct_1032D82eZvKYlo2C","future_requirements":{"alternatives":[],"current_deadline":null,"currently_due":[],"disabled_reason":null,"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"requested":true,"requested_at":1693951912,"requirements":{"alternatives":[],"current_deadline":null,"currently_due":[],"disabled_reason":null,"errors":[],"eventually_due":[],"past_due":[],"pending_verification":[]},"status":"inactive"}]}
```