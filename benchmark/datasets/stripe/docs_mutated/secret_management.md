# secret_management

*Source: https://docs.stripe.com/api/secret_management*

---

# Secrets
Secret Store is an API that allows Stripe Apps developers to securely persist secrets for use by UI Extensions and app backends.
The primary resource in Secret Store is asecret. Other apps can’t view secrets created by an app. Additionally, secrets are scoped to provide further permission control.
All Dashboard users and the app backend shareaccountscoped secrets. Use theaccountscope for secrets that don’t change per-user, like a third-party API key.
Auserscoped secret is accessible by the app backend and one specific Dashboard user. Use theuserscope for per-user secrets like per-user OAuth tokens, where different users might have different permissions.
Related guide:Store data between page reloads

# The Secret object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- deletednullablebooleanIf true, indicates that this secret has been deleted
- expires_atnullabletimestampThe Unix timestamp for the expiry time of the secret, after which the secret deletes.
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- namestringA name for the secret that’s unique within the scope.
- payloadnullablestringExpandableThe plaintext secret value to be stored.
- scopeobjectSpecifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.Show child attributes

#### idstring

#### objectstring

#### createdtimestamp

#### deletednullableboolean

#### expires_atnullabletimestamp

#### livemodeboolean

#### namestring

#### payloadnullablestringExpandable

#### scopeobject

```
{"id":"appsecret_5110hHS1707T6fjBnah1LkdIwHu7ix","object":"apps.secret","created":1680209063,"expires_at":null,"livemode":false,"name":"my-api-key","scope":{"type":"account"}}
```

```
{"id":"appsecret_5110hHS1707T6fjBnah1LkdIwHu7ix","object":"apps.secret","created":1680209063,"expires_at":null,"livemode":false,"name":"my-api-key","scope":{"type":"account"}}
```

# List secrets
List all secrets stored on the given scope.

### Parameters
- scopeobjectRequiredSpecifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.Show child parameters

#### scopeobjectRequired

### More parametersExpand all
- ending_beforestring
- limitinteger
- starting_afterstring

#### ending_beforestring

#### limitinteger

#### starting_afterstring

### Returns
Adictionarywith adataproperty that contains an array of up tolimitSecrets, starting after Secretstarting_after. Each entry in the array is a separate Secret object. If no more Secrets are available, the resulting array will be empty.

```
curl-G https://api.stripe.com/v1/apps/secrets \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"scope[type]"=account
```

```
curl-G https://api.stripe.com/v1/apps/secrets \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"scope[type]"=account
```

```
{"object":"list","url":"/v1/apps/secrets","has_more":false,"data":[{"id":"appsecret_5110hHS1707T6fjBnah1LkdIwHu7ix","object":"apps.secret","created":1680209063,"expires_at":null,"livemode":false,"name":"my-api-key","scope":{"type":"account"}}]}
```

```
{"object":"list","url":"/v1/apps/secrets","has_more":false,"data":[{"id":"appsecret_5110hHS1707T6fjBnah1LkdIwHu7ix","object":"apps.secret","created":1680209063,"expires_at":null,"livemode":false,"name":"my-api-key","scope":{"type":"account"}}]}
```

# Delete a Secret
Deletes a secret from the secret store by name and scope.

### Parameters
- namestringRequiredA name for the secret that’s unique within the scope.
- scopeobjectRequiredSpecifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.Show child parameters

#### namestringRequired

#### scopeobjectRequired

### Returns
Returns the deleted secret object.

```
curlhttps://api.stripe.com/v1/apps/secrets/delete \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d name=my-api-key \-d"scope[type]"=account
```

```
curlhttps://api.stripe.com/v1/apps/secrets/delete \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d name=my-api-key \-d"scope[type]"=account
```

```
{"id":"appsecret_5110hHS1707T6fjBnah1LkdIwHu7ix","object":"apps.secret","deleted":true}
```

```
{"id":"appsecret_5110hHS1707T6fjBnah1LkdIwHu7ix","object":"apps.secret","deleted":true}
```

# Find a Secret
Finds a secret in the secret store by name and scope.

### Parameters
- namestringRequiredA name for the secret that’s unique within the scope.
- scopeobjectRequiredSpecifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.Show child parameters

#### namestringRequired

#### scopeobjectRequired

### Returns
Returns a secret object.

```
curl-G https://api.stripe.com/v1/apps/secrets/find \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d name=my-api-key \-d"scope[type]"=account
```

```
curl-G https://api.stripe.com/v1/apps/secrets/find \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d name=my-api-key \-d"scope[type]"=account
```

```
{"id":"appsecret_5110hHS1707T6fjBnah1LkdIwHu7ix","object":"apps.secret","created":1680209063,"expires_at":null,"livemode":false,"name":"my-api-key","scope":{"type":"account"}}
```

```
{"id":"appsecret_5110hHS1707T6fjBnah1LkdIwHu7ix","object":"apps.secret","created":1680209063,"expires_at":null,"livemode":false,"name":"my-api-key","scope":{"type":"account"}}
```