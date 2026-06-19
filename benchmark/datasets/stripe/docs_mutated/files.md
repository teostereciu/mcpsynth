# files

*Source: https://docs.stripe.com/api/files*

---

# Files
This object represents files hosted on Stripe’s servers. You can uploadfiles with thecreate filerequest(for example, when uploading dispute evidence). Stripe alsocreates files independently (for example, the results of aSigma scheduledquery).
Related guide:File upload guide

# The File object

### Attributes
- idstringUnique identifier for the object.
- purposeenumThepurposeof the uploaded file.Possible enum valuesaccount_requirementAdditional documentation requirements that can be requested for an account.additional_verificationAdditional verification for custom accounts.business_iconA business icon.business_logoA business logo.customer_signatureCustomer signature image.dispute_evidenceEvidence to submit with a dispute response.finance_report_runUser-accessible copies of query results from the Reporting dataset.financial_account_statementFinancial account statements.identity_documentA document to verify the identity of an account owner during account provisioning.identity_document_downloadableImage of a document collected by Stripe Identity.Show 10 more
- typenullablestringThe returned file type (for example,csv,pdf,jpg, orpng).

#### idstring

#### purposeenum

[TABLE]
account_requirementAdditional documentation requirements that can be requested for an account.
additional_verificationAdditional verification for custom accounts.
business_iconA business icon.
business_logoA business logo.
customer_signatureCustomer signature image.
dispute_evidenceEvidence to submit with a dispute response.
finance_report_runUser-accessible copies of query results from the Reporting dataset.
financial_account_statementFinancial account statements.
identity_documentA document to verify the identity of an account owner during account provisioning.
identity_document_downloadableImage of a document collected by Stripe Identity.
Show 10 more
[/TABLE]

```
account_requirement
```

```
additional_verification
```

```
business_icon
```

```
business_logo
```

```
customer_signature
```

```
dispute_evidence
```

```
finance_report_run
```

```
financial_account_statement
```

```
identity_document
```

```
identity_document_downloadable
```

#### typenullablestring

### More attributesExpand all
- objectstring
- createdtimestamp
- expires_atnullabletimestamp
- filenamenullablestring
- linksnullableobject
- sizeinteger
- titlenullablestring
- urlnullablestring

#### objectstring

#### createdtimestamp

#### expires_atnullabletimestamp

#### filenamenullablestring

#### linksnullableobject

#### sizeinteger

#### titlenullablestring

#### urlnullablestring

```
{"id":"file_1Mr4LDLkdIwHu7ixFCz0dZiH","object":"file","created":1680116847,"expires_at":1703444847,"filename":"file.png","links":{"object":"list","data":[],"has_more":false,"url":"/v1/file_links?file=file_1Mr4LDLkdIwHu7ixFCz0dZiH"},"purpose":"dispute_evidence","size":8429,"title":null,"type":"png","url":"https://files.stripe.com/v1/files/file_1Mr4LDLkdIwHu7ixFCz0dZiH/contents"}
```

```
{"id":"file_1Mr4LDLkdIwHu7ixFCz0dZiH","object":"file","created":1680116847,"expires_at":1703444847,"filename":"file.png","links":{"object":"list","data":[],"has_more":false,"url":"/v1/file_links?file=file_1Mr4LDLkdIwHu7ixFCz0dZiH"},"purpose":"dispute_evidence","size":8429,"title":null,"type":"png","url":"https://files.stripe.com/v1/files/file_1Mr4LDLkdIwHu7ixFCz0dZiH/contents"}
```

# Create a file
To upload a file to Stripe, you need to send a request of typemultipart/form-data. Include the file you want to upload in the request, and the parameters for creating a file.
All of Stripe’s officially supported Client libraries support sendingmultipart/form-data.

### Parameters
- fileobjectRequiredA file to upload. Make sure that the specifications follow RFC 2388, which defines file transfers for themultipart/form-dataprotocol.
- purposeenumRequiredThepurposeof the uploaded file.Possible enum valuesaccount_requirementAdditional documentation requirements that can be requested for an account.additional_verificationAdditional verification for custom accounts.business_iconA business icon.business_logoA business logo.customer_signatureCustomer signature image.dispute_evidenceEvidence to submit with a dispute response.identity_documentA document to verify the identity of an account owner during account provisioning.issuing_regulatory_reportingAdditional regulatory reporting requirements for Issuing.pci_documentA self-assessment PCI questionnaire.platform_terms_of_serviceA copy of the platform’s Terms of Service.Show 5 more

#### fileobjectRequired

#### purposeenumRequired

[TABLE]
account_requirementAdditional documentation requirements that can be requested for an account.
additional_verificationAdditional verification for custom accounts.
business_iconA business icon.
business_logoA business logo.
customer_signatureCustomer signature image.
dispute_evidenceEvidence to submit with a dispute response.
identity_documentA document to verify the identity of an account owner during account provisioning.
issuing_regulatory_reportingAdditional regulatory reporting requirements for Issuing.
pci_documentA self-assessment PCI questionnaire.
platform_terms_of_serviceA copy of the platform’s Terms of Service.
Show 5 more
[/TABLE]

```
account_requirement
```

```
additional_verification
```

```
business_icon
```

```
business_logo
```

```
customer_signature
```

```
dispute_evidence
```

```
identity_document
```

```
issuing_regulatory_reporting
```

```
pci_document
```

```
platform_terms_of_service
```

### More parametersExpand all
- file_link_dataobject

#### file_link_dataobject

### Returns
Returns the file object.

```
curlhttps://files.stripe.com/v1/files \-usk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \-F purpose=dispute_evidence \-F file="@/path/to/a/file.jpg"
```

```
curlhttps://files.stripe.com/v1/files \-usk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz: \-F purpose=dispute_evidence \-F file="@/path/to/a/file.jpg"
```

```
{"id":"file_1Mr4LDLkdIwHu7ixFCz0dZiH","object":"file","created":1680116847,"expires_at":1703444847,"filename":"file.png","links":{"object":"list","data":[],"has_more":false,"url":"/v1/file_links?file=file_1Mr4LDLkdIwHu7ixFCz0dZiH"},"purpose":"dispute_evidence","size":8429,"title":null,"type":"png","url":"https://files.stripe.com/v1/files/file_1Mr4LDLkdIwHu7ixFCz0dZiH/contents"}
```

```
{"id":"file_1Mr4LDLkdIwHu7ixFCz0dZiH","object":"file","created":1680116847,"expires_at":1703444847,"filename":"file.png","links":{"object":"list","data":[],"has_more":false,"url":"/v1/file_links?file=file_1Mr4LDLkdIwHu7ixFCz0dZiH"},"purpose":"dispute_evidence","size":8429,"title":null,"type":"png","url":"https://files.stripe.com/v1/files/file_1Mr4LDLkdIwHu7ixFCz0dZiH/contents"}
```

# Retrieve a file
Retrieves the details of an existing file object. After you supply a unique file ID, Stripe returns the corresponding file object. Learn how toaccess file contents.

### Parameters
Noparameters.

### Returns
If the identifier you provide is valid, a file object returns. If not, Striperaisesan error.

```
curlhttps://api.stripe.com/v1/files/file_1Mr4LDLkdIwHu7ixFCz0dZiH \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/files/file_1Mr4LDLkdIwHu7ixFCz0dZiH \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"file_1Mr4LDLkdIwHu7ixFCz0dZiH","object":"file","created":1680116847,"expires_at":1703444847,"filename":"file.png","links":{"object":"list","data":[],"has_more":false,"url":"/v1/file_links?file=file_1Mr4LDLkdIwHu7ixFCz0dZiH"},"purpose":"dispute_evidence","size":8429,"title":null,"type":"png","url":"https://files.stripe.com/v1/files/file_1Mr4LDLkdIwHu7ixFCz0dZiH/contents"}
```

```
{"id":"file_1Mr4LDLkdIwHu7ixFCz0dZiH","object":"file","created":1680116847,"expires_at":1703444847,"filename":"file.png","links":{"object":"list","data":[],"has_more":false,"url":"/v1/file_links?file=file_1Mr4LDLkdIwHu7ixFCz0dZiH"},"purpose":"dispute_evidence","size":8429,"title":null,"type":"png","url":"https://files.stripe.com/v1/files/file_1Mr4LDLkdIwHu7ixFCz0dZiH/contents"}
```

# List all files
Returns a list of the files that your account has access to. Stripe sorts and returns the files by their creation dates, placing the most recently created files at the top.

### Parameters
- purposestringFilter queries by the file purpose. If you don’t provide a purpose, the queries return unfiltered files.

#### purposestring

### More parametersExpand all
- createdobject
- ending_beforestring
- limitinteger
- starting_afterstring

#### createdobject

#### ending_beforestring

#### limitinteger

#### starting_afterstring

### Returns
Adictionarywith adataproperty that contains an array of up tolimitfiles, starting after thestarting_afterfile. Each entry in the array is a separate file object. If there aren’t additional available files, the resulting array is empty.

```
curl-G https://api.stripe.com/v1/files \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
curl-G https://api.stripe.com/v1/files \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d limit=3
```

```
{"object":"list","url":"/v1/files","has_more":false,"data":[{"id":"file_1Mr4LDLkdIwHu7ixFCz0dZiH","object":"file","created":1680116847,"expires_at":1703444847,"filename":"file.png","links":{"object":"list","data":[],"has_more":false,"url":"/v1/file_links?file=file_1Mr4LDLkdIwHu7ixFCz0dZiH"},"purpose":"dispute_evidence","size":8429,"title":null,"type":"png","url":"https://files.stripe.com/v1/files/file_1Mr4LDLkdIwHu7ixFCz0dZiH/contents"}]}
```

```
{"object":"list","url":"/v1/files","has_more":false,"data":[{"id":"file_1Mr4LDLkdIwHu7ixFCz0dZiH","object":"file","created":1680116847,"expires_at":1703444847,"filename":"file.png","links":{"object":"list","data":[],"has_more":false,"url":"/v1/file_links?file=file_1Mr4LDLkdIwHu7ixFCz0dZiH"},"purpose":"dispute_evidence","size":8429,"title":null,"type":"png","url":"https://files.stripe.com/v1/files/file_1Mr4LDLkdIwHu7ixFCz0dZiH/contents"}]}
```