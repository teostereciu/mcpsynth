# identity/verification_reports

*Source: https://docs.stripe.com/api/identity/verification_reports*

---

# Verification Report
A VerificationReport is the result of an attempt to collect and verify data from a user.The collection of verification checks performed is determined from thetypeandoptionsparameters used. You can find the result of each verification check performed in theappropriate sub-resource:document,id_number,selfie.
Each VerificationReport contains a copy of any data collected by the user as well asreference IDs which can be used to access collected images through theFileUploadAPI. To configure and create VerificationReports, use theVerificationSessionAPI.
Related guide:Accessing verification results.

# The VerificationReport object

### Attributes
- idstringUnique identifier for the object.
- objectstringString representing the object’s type. Objects of the same type share the same value.
- client_reference_idnullablestringA string to reference this user. This can be a customer_id ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.
- createdtimestampTime at which the object was created. Measured in seconds since the Unix epoch.
- documentnullableobjectResult of the document check for this report.Show child attributes
- emailnullableobjectResult of the email check for this report.Show child attributes
- id_numbernullableobjectResult of the id number check for this report.Show child attributes
- livemodebooleanIf the object exists in live mode, the value istrue. If the object exists in test mode, the value isfalse.
- optionsnullableobjectConfiguration options for this report.Show child attributes
- phonenullableobjectResult of the phone check for this report.Show child attributes
- selfienullableobjectResult of the selfie check for this report.Show child attributes
- typeenumType of report.Possible enum valuesdocumentPerform a document check.id_numberPerform an ID number check.verification_flowConfiguration provided by verification flow
- verification_flownullablestringThe configuration token of a verification flow from the dashboard.
- verification_sessionnullablestringID of the VerificationSession that created this report.

#### idstring

#### objectstring

#### client_reference_idnullablestring

#### createdtimestamp

#### documentnullableobject

#### emailnullableobject

#### id_numbernullableobject

#### livemodeboolean

#### optionsnullableobject

#### phonenullableobject

#### selfienullableobject

#### typeenum

[TABLE]
documentPerform a document check.
id_numberPerform an ID number check.
verification_flowConfiguration provided by verification flow
[/TABLE]

```
verification_flow
```

#### verification_flownullablestring

#### verification_sessionnullablestring

```
{"id":"vr_1MwBlH2eZvKYlo2C91hOpFMf","object":"identity.verification_report","created":1681337011,"livemode":false,"options":{"document":{}},"type":"document","verification_session":"vs_NhaxYCqOE27AqaUTxbIZOnHw","document":{"status":"verified","error":null,"first_name":"Jenny","last_name":"Rosen","address":{"line1":"1234 Main St.","city":"San Francisco","state":"CA","zip":"94111","country":"US"},"type":"driving_license","files":["file_NhaxRCXT8Iuu8apSuci00UC4","file_NhaxDeWKGAOTc8Uec7UY9Ljj"],"expiration_date":{"month":12,"day":1,"year":2025},"issued_date":{"month":12,"day":1,"year":2020},"issuing_country":"US"}}
```

```
{"id":"vr_1MwBlH2eZvKYlo2C91hOpFMf","object":"identity.verification_report","created":1681337011,"livemode":false,"options":{"document":{}},"type":"document","verification_session":"vs_NhaxYCqOE27AqaUTxbIZOnHw","document":{"status":"verified","error":null,"first_name":"Jenny","last_name":"Rosen","address":{"line1":"1234 Main St.","city":"San Francisco","state":"CA","zip":"94111","country":"US"},"type":"driving_license","files":["file_NhaxRCXT8Iuu8apSuci00UC4","file_NhaxDeWKGAOTc8Uec7UY9Ljj"],"expiration_date":{"month":12,"day":1,"year":2025},"issued_date":{"month":12,"day":1,"year":2020},"issuing_country":"US"}}
```

# Retrieve a VerificationReport
Retrieves an existing VerificationReport

### Parameters
Noparameters.

### Returns
Returns a VerificationReport object

```
curlhttps://api.stripe.com/v1/identity/verification_reports/vr_1MwBlH2eZvKYlo2C91hOpFMf \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/identity/verification_reports/vr_1MwBlH2eZvKYlo2C91hOpFMf \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"vr_1MwBlH2eZvKYlo2C91hOpFMf","object":"identity.verification_report","created":1681337011,"livemode":false,"options":{"document":{}},"type":"document","verification_session":"vs_NhaxYCqOE27AqaUTxbIZOnHw","document":{"status":"verified","error":null,"first_name":"Jenny","last_name":"Rosen","address":{"line1":"1234 Main St.","city":"San Francisco","state":"CA","zip":"94111","country":"US"},"type":"driving_license","files":["file_NhaxRCXT8Iuu8apSuci00UC4","file_NhaxDeWKGAOTc8Uec7UY9Ljj"],"expiration_date":{"month":12,"day":1,"year":2025},"issued_date":{"month":12,"day":1,"year":2020},"issuing_country":"US"}}
```

```
{"id":"vr_1MwBlH2eZvKYlo2C91hOpFMf","object":"identity.verification_report","created":1681337011,"livemode":false,"options":{"document":{}},"type":"document","verification_session":"vs_NhaxYCqOE27AqaUTxbIZOnHw","document":{"status":"verified","error":null,"first_name":"Jenny","last_name":"Rosen","address":{"line1":"1234 Main St.","city":"San Francisco","state":"CA","zip":"94111","country":"US"},"type":"driving_license","files":["file_NhaxRCXT8Iuu8apSuci00UC4","file_NhaxDeWKGAOTc8Uec7UY9Ljj"],"expiration_date":{"month":12,"day":1,"year":2025},"issued_date":{"month":12,"day":1,"year":2020},"issuing_country":"US"}}
```

# List VerificationReports
List all verification reports.

### Parameters
- client_reference_idstringA string to reference this user. This can be a customer_id ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.
- createdobjectOnly return VerificationReports that were created during the given date interval.Show child parameters
- typeenumOnly return VerificationReports of this typePossible enum valuesdocumentPerform a document check.id_numberPerform an ID number check.
- verification_sessionstringOnly return VerificationReports created by this VerificationSession ID. It is allowed to provide a VerificationIntent ID.

#### client_reference_idstring

#### createdobject

#### typeenum

[TABLE]
documentPerform a document check.
id_numberPerform an ID number check.
[/TABLE]

#### verification_sessionstring

### More parametersExpand all
- ending_beforestring
- limitinteger
- starting_afterstring

#### ending_beforestring

#### limitinteger

#### starting_afterstring

### Returns
List of VerificationInent objects that match the provided filter criteria.

```
curl-G https://api.stripe.com/v1/identity/verification_reports \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
curl-G https://api.stripe.com/v1/identity/verification_reports \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
{"object":"list","url":"/v1/identity/verification_reports","has_more":false,"data":[{"id":"vr_1MwBlH2eZvKYlo2C91hOpFMf","object":"identity.verification_report","created":1681337011,"livemode":false,"options":{"document":{}},"type":"document","verification_session":"vs_NhaxYCqOE27AqaUTxbIZOnHw","document":{"status":"verified","error":null,"first_name":"Jenny","last_name":"Rosen","address":{"line1":"1234 Main St.","city":"San Francisco","state":"CA","zip":"94111","country":"US"},"type":"driving_license","files":["file_NhaxRCXT8Iuu8apSuci00UC4","file_NhaxDeWKGAOTc8Uec7UY9Ljj"],"expiration_date":{"month":12,"day":1,"year":2025},"issued_date":{"month":12,"day":1,"year":2020},"issuing_country":"US"}}]}
```

```
{"object":"list","url":"/v1/identity/verification_reports","has_more":false,"data":[{"id":"vr_1MwBlH2eZvKYlo2C91hOpFMf","object":"identity.verification_report","created":1681337011,"livemode":false,"options":{"document":{}},"type":"document","verification_session":"vs_NhaxYCqOE27AqaUTxbIZOnHw","document":{"status":"verified","error":null,"first_name":"Jenny","last_name":"Rosen","address":{"line1":"1234 Main St.","city":"San Francisco","state":"CA","zip":"94111","country":"US"},"type":"driving_license","files":["file_NhaxRCXT8Iuu8apSuci00UC4","file_NhaxDeWKGAOTc8Uec7UY9Ljj"],"expiration_date":{"month":12,"day":1,"year":2025},"issued_date":{"month":12,"day":1,"year":2020},"issuing_country":"US"}}]}
```