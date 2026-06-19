# identity/verification_sessions

*Source: https://docs.stripe.com/api/identity/verification_sessions*

---

# Verification Session
A VerificationSession guides you through the process of collecting and verifying the identitiesof your users. It contains details about the type of verification, such as whatverificationcheckto perform. Only create one VerificationSession foreach verification in your system.
A VerificationSession transitions throughmultiplestatusesthroughout its lifetime as it progresses throughthe verification flow. The VerificationSession contains the user’s verified data afterverification checks are complete.
Related guide:The Verification Sessions API

# The VerificationSession object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- client_reference_idnullablestringA string to reference this user. This can be a customer_id ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.
- client_secretnullablestringThe short-lived client secret used by Stripe.js toshow a verification modalinside your app. This client secret expires after 24 hours and can only be used once. Don’t store it, log it, embed it in a URL, or expose it to anyone other than the user. Make sure that you have TLS enabled on any page that includes the client secret. Refer to our docs onpassing the client secret to the frontendto learn more.
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- last_errornullableobjectIf present, this property tells you the last error encountered when processing the verification.Show child attributes
- last_verification_reportnullablestringExpandableID of the most recent VerificationReport.Learn more about accessing detailed verification results.
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- optionsnullableobjectA set of options for the session’s verification checks.Show child attributes
- provided_detailsnullableobjectExpandableDetails provided about the user being verified. These details may be shown to the user.Show child attributes
- redactionnullableobjectRedaction status of this VerificationSession. If the VerificationSession is not redacted, this field will be null.Show child attributes
- related_customernullablestringCustomer ID
- related_customer_accountnullablestringThe ID of the Account representing a customer_id.
- related_personnullableobjectTokens referencing the related Person resource and it’s associated account.Show child attributes
- statusenumStatus of this VerificationSession.Learn more about the lifecycle of sessions.Possible enum valuescanceledThe VerificationSession has been invalidated for future submission attempts.processingThe session has been submitted and is being processed. Mostverification checksare processed in less than 1 minute.requires_inputRequires user input before processing can continue.verifiedProcessing of all the verification checks are complete and successfully verified.
- typeenumThe type ofverification checkto be performed.Possible enum valuesdocumentDocument check.id_numberID number check.verification_flowConfiguration provided by verification flow
- urlnullablestringThe short-lived URL that you use to redirect a user to Stripe to submit their identity information. This URL expires after 48 hours and can only be used once. Don’t store it, log it, send it in emails or expose it to anyone other than the user. Refer to our docs onverifying identity documentsto learn how to redirect users to Stripe.
- verification_flownullablestringThe configuration token of a verification flow from the dashboard.
- verified_outputsnullableobjectExpandableThe user’s verified data.Show child attributes

#### idstring

#### objectstring

#### client_reference_idnullablestring

#### client_secretnullablestring

#### createdtimestamp

#### last_errornullableobject

#### last_verification_reportnullablestringExpandable

#### livemodeboolean

#### metadataobject

#### optionsnullableobject

#### provided_detailsnullableobjectExpandable

#### redactionnullableobject

#### related_customernullablestring

#### related_customer_accountnullablestring

#### related_personnullableobject

#### statusenum

[TABLE]
canceledThe VerificationSession has been invalidated for future submission attempts.
processingThe session has been submitted and is being processed. Mostverification checksare processed in less than 1 minute.
requires_inputRequires user input before processing can continue.
verifiedProcessing of all the verification checks are complete and successfully verified.
[/TABLE]

```
requires_input
```

#### typeenum

[TABLE]
documentDocument check.
id_numberID number check.
verification_flowConfiguration provided by verification flow
[/TABLE]

```
verification_flow
```

#### urlnullablestring

#### verification_flownullablestring

#### verified_outputsnullableobjectExpandable

```
{"id":"vs_1NuNAILkdIwHu7ixh7OtGMLw","object":"identity.verification_session","client_secret":"...","created":1695680526,"last_error":null,"last_verification_report":null,"livemode":false,"custom_fields":{},"options":{"document":{"require_matching_selfie":true}},"redaction":null,"status":"requires_input","type":"document","url":"..."}
```

```
{"id":"vs_1NuNAILkdIwHu7ixh7OtGMLw","object":"identity.verification_session","client_secret":"...","created":1695680526,"last_error":null,"last_verification_report":null,"livemode":false,"custom_fields":{},"options":{"document":{"require_matching_selfie":true}},"redaction":null,"status":"requires_input","type":"document","url":"..."}
```

# Create a VerificationSession
Creates a VerificationSession object.
After the VerificationSession is created, display a verification modal using the sessionclient_secretor send your users to the session’surl.
If your API key is in test mode, verification checks won’t actually process, though everything else will occur as if in live mode.
Related guide:Verify your users’ identity documents

### Parameters
- client_reference_idstringA string to reference this user. This can be a customer_id ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- optionsobjectA set of options for the session’s verification checks.Show child parameters
- provided_detailsobjectDetails provided about the user being verified. These details may be shown to the user.Show child parameters
- related_customerstringCustomer ID
- related_customer_accountstringThe ID of the Account representing a customer_id.
- related_personobjectTokens referencing a Person resource and it’s associated account.Show child parameters
- return_urlstringThe URL that the user will be redirected to upon completing the verification flow.
- typeenumThe type ofverification checkto be performed. You must provide atypeif not passingverification_flow.Possible enum valuesdocumentDocument check.id_numberID number check.
- verification_flowstringThe ID of a verification flow from the Dashboard. See https://docs.stripe.com/identity/verification-flows.

#### client_reference_idstring

#### metadataobject

#### optionsobject

#### provided_detailsobject

#### related_customerstring

#### related_customer_accountstring

#### related_personobject

#### return_urlstring

#### typeenum

[TABLE]
documentDocument check.
id_numberID number check.
[/TABLE]

#### verification_flowstring

### Returns
Returns the created VerificationSession object

```
curlhttps://api.stripe.com/v1/identity/verification_sessions \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d type=document
```

```
curlhttps://api.stripe.com/v1/identity/verification_sessions \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d type=document
```

```
{"id":"vs_1NuN4zLkdIwHu7ixleE6HvkI","object":"identity.verification_session","client_secret":"...","created":1695680197,"last_error":null,"last_verification_report":null,"livemode":false,"custom_fields":{},"options":{},"redaction":null,"status":"requires_input","type":"document","url":"..."}
```

```
{"id":"vs_1NuN4zLkdIwHu7ixleE6HvkI","object":"identity.verification_session","client_secret":"...","created":1695680197,"last_error":null,"last_verification_report":null,"livemode":false,"custom_fields":{},"options":{},"redaction":null,"status":"requires_input","type":"document","url":"..."}
```

# Update a VerificationSession
Updates a VerificationSession object.
When the session status isrequires_input, you can use this method to update theverification check and options.

### Parameters
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.
- optionsobjectA set of options for the session’s verification checks.Show child parameters
- provided_detailsobjectDetails provided about the user being verified. These details may be shown to the user.Show child parameters
- typeenumThe type ofverification checkto be performed.Possible enum valuesdocumentDocument check.id_numberID number check.

#### metadataobject

#### optionsobject

#### provided_detailsobject

#### typeenum

[TABLE]
documentDocument check.
id_numberID number check.
[/TABLE]

### Returns
Returns the updated VerificationSession object

```
curlhttps://api.stripe.com/v1/identity/verification_sessions/vs_1NuN9WLkdIwHu7ix597AR9uz \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d type=id_number
```

```
curlhttps://api.stripe.com/v1/identity/verification_sessions/vs_1NuN9WLkdIwHu7ix597AR9uz \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d type=id_number
```

```
{"id":"vs_1NuN9WLkdIwHu7ix597AR9uz","object":"identity.verification_session","client_secret":"...","created":1695680478,"last_error":null,"last_verification_report":null,"livemode":false,"custom_fields":{},"options":{},"redaction":null,"status":"requires_input","type":"id_number","url":"..."}
```

```
{"id":"vs_1NuN9WLkdIwHu7ix597AR9uz","object":"identity.verification_session","client_secret":"...","created":1695680478,"last_error":null,"last_verification_report":null,"livemode":false,"custom_fields":{},"options":{},"redaction":null,"status":"requires_input","type":"id_number","url":"..."}
```

# Retrieve a VerificationSession
Retrieves the details of a VerificationSession that was previously created.
When the session status isrequires_input, you can use this method to retrieve a validclient_secretorurlto allow re-submission.

### Parameters
Noparameters.

### Returns
Returns a VerificationSession object

```
curlhttps://api.stripe.com/v1/identity/verification_sessions/vs_1NuNAILkdIwHu7ixh7OtGMLw \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/identity/verification_sessions/vs_1NuNAILkdIwHu7ixh7OtGMLw \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"vs_1NuNAILkdIwHu7ixh7OtGMLw","object":"identity.verification_session","client_secret":"...","created":1695680526,"last_error":null,"last_verification_report":null,"livemode":false,"custom_fields":{},"options":{"document":{"require_matching_selfie":true}},"redaction":null,"status":"requires_input","type":"document","url":"..."}
```

```
{"id":"vs_1NuNAILkdIwHu7ixh7OtGMLw","object":"identity.verification_session","client_secret":"...","created":1695680526,"last_error":null,"last_verification_report":null,"livemode":false,"custom_fields":{},"options":{"document":{"require_matching_selfie":true}},"redaction":null,"status":"requires_input","type":"document","url":"..."}
```