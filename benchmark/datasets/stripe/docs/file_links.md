# file_links

*Source: https://docs.stripe.com/api/file_links*

---

# File Links
To share the contents of aFileobject with non-Stripe users, you cancreate aFileLink.FileLinks contain a URL that you can use toretrieve the contents of the file without authentication.

# The File Link object

### Attributes
- idstringUnique identifier for the object.
- expires_atnullabletimestampTime that the link expires.
- filestringExpandableThe file object this link points to.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.
- urlnullablestringThe publicly accessible URL to download the file.

#### idstring

#### expires_atnullabletimestamp

#### filestringExpandable

#### metadataobject

#### urlnullablestring

### More attributesExpand all
- objectstring
- createdtimestamp
- expiredboolean
- livemodeboolean

#### objectstring

#### createdtimestamp

#### expiredboolean

#### livemodeboolean

```
{"id":"link_1Mr23jLkdIwHu7ix65betcoo","object":"file_link","created":1680108075,"expired":false,"expires_at":null,"file":"file_1Mr23iLkdIwHu7ixQkCV3CBR","livemode":false,"metadata":{},"url":"https://files.stripe.com/links/MDB8YWNjdF8xTTJKVGtMa2RJd0h1N2l4fGZsX3Rlc3RfaXVoY2hrUnJPMzlBR3dPb01XMmFkSTVq00yUPLFf3h"}
```

```
{"id":"link_1Mr23jLkdIwHu7ix65betcoo","object":"file_link","created":1680108075,"expired":false,"expires_at":null,"file":"file_1Mr23iLkdIwHu7ixQkCV3CBR","livemode":false,"metadata":{},"url":"https://files.stripe.com/links/MDB8YWNjdF8xTTJKVGtMa2RJd0h1N2l4fGZsX3Rlc3RfaXVoY2hrUnJPMzlBR3dPb01XMmFkSTVq00yUPLFf3h"}
```

# Create a file link
Creates a new file link object.

### Parameters
- filestringRequiredThe ID of the file. The file’spurposemust be one of the following:business_icon,business_logo,customer_signature,dispute_evidence,finance_report_run,financial_account_statement,identity_document_downloadable,issuing_regulatory_reporting,pci_document,selfie,sigma_scheduled_query,tax_document_user_upload,terminal_android_apk, orterminal_reader_splashscreen.
- expires_attimestampThe link isn’t usable after this future timestamp.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### filestringRequired

#### expires_attimestamp

#### metadataobject

### Returns
Returns the file link object if successful andraisesan errorotherwise.

```
curlhttps://api.stripe.com/v1/file_links \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d file=file_1Mr23iLkdIwHu7ixQkCV3CBR
```

```
curlhttps://api.stripe.com/v1/file_links \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d file=file_1Mr23iLkdIwHu7ixQkCV3CBR
```

```
{"id":"link_1Mr23jLkdIwHu7ix65betcoo","object":"file_link","created":1680108075,"expired":false,"expires_at":null,"file":"file_1Mr23iLkdIwHu7ixQkCV3CBR","livemode":false,"metadata":{},"url":"https://files.stripe.com/links/MDB8YWNjdF8xTTJKVGtMa2RJd0h1N2l4fGZsX3Rlc3RfaXVoY2hrUnJPMzlBR3dPb01XMmFkSTVq00yUPLFf3h"}
```

```
{"id":"link_1Mr23jLkdIwHu7ix65betcoo","object":"file_link","created":1680108075,"expired":false,"expires_at":null,"file":"file_1Mr23iLkdIwHu7ixQkCV3CBR","livemode":false,"metadata":{},"url":"https://files.stripe.com/links/MDB8YWNjdF8xTTJKVGtMa2RJd0h1N2l4fGZsX3Rlc3RfaXVoY2hrUnJPMzlBR3dPb01XMmFkSTVq00yUPLFf3h"}
```

# Update a file link
Updates an existing file link object. Expired links can no longer be updated.

### Parameters
- expires_atstring | timestampA future timestamp after which the link will no longer be usable, ornowto expire the link immediately.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### expires_atstring | timestamp

#### metadataobject

### Returns
Returns the file link object if successful, andraisesan errorotherwise.

```
curlhttps://api.stripe.com/v1/file_links/link_1Mr23jLkdIwHu7ix65betcoo \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
curlhttps://api.stripe.com/v1/file_links/link_1Mr23jLkdIwHu7ix65betcoo \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d"metadata[order_id]"=6735
```

```
{"id":"link_1Mr23jLkdIwHu7ix65betcoo","object":"file_link","created":1680108075,"expired":false,"expires_at":null,"file":"file_1Mr23iLkdIwHu7ixQkCV3CBR","livemode":false,"metadata":{"order_id":"6735"},"url":"https://files.stripe.com/links/MDB8YWNjdF8xTTJKVGtMa2RJd0h1N2l4fGZsX3Rlc3RfaXVoY2hrUnJPMzlBR3dPb01XMmFkSTVq00yUPLFf3h"}
```

```
{"id":"link_1Mr23jLkdIwHu7ix65betcoo","object":"file_link","created":1680108075,"expired":false,"expires_at":null,"file":"file_1Mr23iLkdIwHu7ixQkCV3CBR","livemode":false,"metadata":{"order_id":"6735"},"url":"https://files.stripe.com/links/MDB8YWNjdF8xTTJKVGtMa2RJd0h1N2l4fGZsX3Rlc3RfaXVoY2hrUnJPMzlBR3dPb01XMmFkSTVq00yUPLFf3h"}
```

# Retrieve a file link
Retrieves the file link with the given ID.

### Parameters
Noparameters.

### Returns
If the identifier you provide is valid, a file link object returns. If not, Striperaisesan error.

```
curlhttps://api.stripe.com/v1/file_links/link_1Mr23jLkdIwHu7ix65betcoo \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/file_links/link_1Mr23jLkdIwHu7ix65betcoo \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"link_1Mr23jLkdIwHu7ix65betcoo","object":"file_link","created":1680108075,"expired":false,"expires_at":null,"file":"file_1Mr23iLkdIwHu7ixQkCV3CBR","livemode":false,"metadata":{},"url":"https://files.stripe.com/links/MDB8YWNjdF8xTTJKVGtMa2RJd0h1N2l4fGZsX3Rlc3RfaXVoY2hrUnJPMzlBR3dPb01XMmFkSTVq00yUPLFf3h"}
```

```
{"id":"link_1Mr23jLkdIwHu7ix65betcoo","object":"file_link","created":1680108075,"expired":false,"expires_at":null,"file":"file_1Mr23iLkdIwHu7ixQkCV3CBR","livemode":false,"metadata":{},"url":"https://files.stripe.com/links/MDB8YWNjdF8xTTJKVGtMa2RJd0h1N2l4fGZsX3Rlc3RfaXVoY2hrUnJPMzlBR3dPb01XMmFkSTVq00yUPLFf3h"}
```