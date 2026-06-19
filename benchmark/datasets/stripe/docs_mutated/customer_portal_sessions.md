# customer_portal/sessions

*Source: https://docs.stripe.com/api/customer_portal/sessions*

---

# Customer Portal Session
The Billing customer_id portal is a Stripe-hosted UI for subscription andbilling management.
A portal configuration describes the functionality and features that youwant to provide to your customers through the portal.
A portal session describes the instantiation of the customer_id portal fora particular customer_id. By visiting the session’s URL, the customercan manage their subscriptions and billing details. For security reasons,sessions are short-lived and will expire if the customer_id does not visit the URL.Create sessions on-demand when customers intend to manage their subscriptionsand billing details.
Related guide:Customer management

# The Customer Portal Session object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- configurationstringExpandableThe configuration used by this session, describing the features available.
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- customerstringThe ID of the customer_id for this session.
- customer_accountnullablestringThe ID of the account for this session.
- flownullableobjectInformation about a specific flow for the customer_id to go through. See thedocsto learn more about using customer_id portal deep links and flows.Show child attributes
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- localenullableenumThe IETF language tag of the locale Customer Portal is displayed in. If blank or auto, the customer_id’spreferred_localesor browser’s locale is used.
- on_behalf_ofnullablestringConnect onlyThe account for which the session was created on behalf of. When specified, only subscriptions and invoices with thison_behalf_ofaccount appear in the portal. For more information, see thedocs. Use theAccounts APIto modify theon_behalf_ofaccount’s branding settings, which the portal displays.
- return_urlnullablestringThe URL to redirect customers to when they click on the portal’s link to return to your website.
- urlstringThe short-lived URL of the session that gives customers access to the customer_id portal.

#### idstring

#### objectstring

#### configurationstringExpandable

#### createdtimestamp

#### customerstring

#### customer_accountnullablestring

#### flownullableobject

#### livemodeboolean

#### localenullableenum

#### on_behalf_ofnullablestringConnect only

#### return_urlnullablestring

#### urlstring

```
{"id":"bps_1MrSjzLkdIwHu7ixex0IvU9b","object":"billing_portal.session","configuration":"bpc_1MAhNDLkdIwHu7ixckACO1Jq","created":1680210639,"customer_id":"cus_NciAYcXfLnqBoz","flow":null,"livemode":false,"locale":null,"on_behalf_of":null,"return_url":"https://example.com/account","url":"https://billing.stripe.com/p/session/test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LF9OY2lBYjJXcHY4a2NPck96UjBEbFVYRnU5bjlwVUF50100BUtQs3bl"}
```

```
{"id":"bps_1MrSjzLkdIwHu7ixex0IvU9b","object":"billing_portal.session","configuration":"bpc_1MAhNDLkdIwHu7ixckACO1Jq","created":1680210639,"customer_id":"cus_NciAYcXfLnqBoz","flow":null,"livemode":false,"locale":null,"on_behalf_of":null,"return_url":"https://example.com/account","url":"https://billing.stripe.com/p/session/test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LF9OY2lBYjJXcHY4a2NPck96UjBEbFVYRnU5bjlwVUF50100BUtQs3bl"}
```

# Create a portal session
Creates a session of the customer_id portal.

### Parameters
- configurationstringThe ID of an existingconfigurationto use for this session, describing its functionality and features. If not specified, the session uses the default configuration.
- customerstringThe ID of an existing customer_id.
- customer_accountstringThe ID of an existing account.
- flow_dataobjectInformation about a specific flow for the customer_id to go through. See thedocsto learn more about using customer_id portal deep links and flows.Show child parameters
- localeenumThe IETF language tag of the locale customer_id portal is displayed in. If blank or auto, the customer_id’spreferred_localesor browser’s locale is used.
- on_behalf_ofstringConnect onlyTheon_behalf_ofaccount to use for this session. When specified, only subscriptions and invoices with thison_behalf_ofaccount appear in the portal. For more information, see thedocs. Use theAccounts APIto modify theon_behalf_ofaccount’s branding settings, which the portal displays.
- return_urlstringThe default URL to redirect customers to when they click on the portal’s link to return to your website.

#### configurationstring

#### customerstring

#### customer_accountstring

#### flow_dataobject

#### localeenum

#### on_behalf_ofstringConnect only

#### return_urlstring

### Returns
Returns a portal session object.

```
curlhttps://api.stripe.com/v1/billing_portal/sessions \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d customer_id=cus_NciAYcXfLnqBoz \--data-urlencode return_url="https://example.com/account"
```

```
curlhttps://api.stripe.com/v1/billing_portal/sessions \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d customer_id=cus_NciAYcXfLnqBoz \--data-urlencode return_url="https://example.com/account"
```

```
{"id":"bps_1MrSjzLkdIwHu7ixex0IvU9b","object":"billing_portal.session","configuration":"bpc_1MAhNDLkdIwHu7ixckACO1Jq","created":1680210639,"customer_id":"cus_NciAYcXfLnqBoz","flow":null,"livemode":false,"locale":null,"on_behalf_of":null,"return_url":"https://example.com/account","url":"https://billing.stripe.com/p/session/test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LF9OY2lBYjJXcHY4a2NPck96UjBEbFVYRnU5bjlwVUF50100BUtQs3bl"}
```

```
{"id":"bps_1MrSjzLkdIwHu7ixex0IvU9b","object":"billing_portal.session","configuration":"bpc_1MAhNDLkdIwHu7ixckACO1Jq","created":1680210639,"customer_id":"cus_NciAYcXfLnqBoz","flow":null,"livemode":false,"locale":null,"on_behalf_of":null,"return_url":"https://example.com/account","url":"https://billing.stripe.com/p/session/test_YWNjdF8xTTJKVGtMa2RJd0h1N2l4LF9OY2lBYjJXcHY4a2NPck96UjBEbFVYRnU5bjlwVUF50100BUtQs3bl"}
```