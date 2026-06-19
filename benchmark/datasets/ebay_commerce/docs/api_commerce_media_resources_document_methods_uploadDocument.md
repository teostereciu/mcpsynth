# commerce/media/resources/document/methods/uploadDocument

*Source: https://developer.ebay.com/api-docs/commerce/media/resources/document/methods/uploadDocument*

---

## Input

### Resource URI

### URI parameters

### HTTP request headers

### OAuth scope

### Request payload

### Request fields

## Output

### HTTP response headers

### Response payload

### Response fields

### HTTP status codes

## Error codes

## Warnings

## Samples

### Sample 1: Upload a document

#### Thank you for helping us to improve the eBay developer program.
POST/document/{document_id}/upload
This method associates the specified file with the specified document ID and uploads the input file. After the file has been uploaded, the processing of the file begins. Supported file types include .PDF, .JPEG/.JPG, and .PNG, with a maximum file size of 10 MB (10485760 bytes).Note:Animated and multi-page PNG files are not currently supported.Note:The document ID value returned in the response of thecreateDocumentmethod is a required input path parameter for this method. This value is also returned in thelocationheader of thecreateDocumentresponse payload.A successful upload returns the HTTP Status Code200 OK.SeeManaging documentsfor additional information.Note:You must use aContent-Typeheader with its value set tomultipart/form-data.
SeeManaging documentsfor additional information.
Important!All POST methods in the Media API, including this method, are subject to short-duration rate limits at the user level: 50 requests per 5 seconds.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Required
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
This request requires an access token created with theauthorization code grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope/sell.inventory
SeeOAuth access tokensfor more information.
This call does not use a JSON request payload, but uploads files using multipart form data with information about the form data in the key-value pairs. SeeUpload the filefor more information.
This call has no payload.
This call has no field definitions.
This call has no response headers.
The unique ID of the document.Occurrence:Always
Occurrence:Always
This container provides the name, size, and type of the specified file.Occurrence:Conditional
Occurrence:Conditional
The name of the file including its extension (for example,drone_user_warranty.pdf).Occurrence:Conditional
The size, in bytes, of the document content.Occurrence:Conditional
The type of the file uploaded. Supported file types include the following:pdf,jpeg,jpg, andpng.Occurrence:Conditional
The status of the document resource.Once a document has been uploaded using theuploadDocumentmethod, thedocumentStatuswill beSUBMITTED. The document will then either be accepted or rejected. Only documents with the status ofACCEPTEDare available to be added to a listing.Occurrence:Always
The type of the document uploaded. For example,USER_GUIDE_OR_MANUAL.Occurrence:Always
This array shows the language(s) used in the document.Occurrence:Always
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample uploads a document file using a created document ID.
The input is thedocument ID1*******-**********d5as a URI parameter. Although there is no JSON request payload, information about the form data is sent as key-value pairs. Onlyfileis required. SeeUpload the document filefor more information.
POSThttps://api.ebay.com/commerce/media/v1_beta/document/1*******-**********d5/upload
A successful call will show an HTTP status of 200 and the following payload. The response payload includes the document ID, type, status, and document metadata. If the call is successful, the document will be uploaded.
Related topics
If you need help, contactDeveloper Technical Support.

```
file: @"/C:/Users/.../drone_user_warranty.pdf"
```
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
document_id | string | The unique identifier of the document to be uploaded.This value is returned in the response of thecreateDocumentmethod.Occurrence:Required
[/TABLE]

[TABLE]
Header | Type | Description
Content-Type | string | This header indicates the format of the request body provided by the client. Its value should be set tomultipart/form-data.For more information, refer toHTTP request headers.Occurrence:Required
[/TABLE]

[TABLE]
Output container/field | Type | Description
documentId | string | The unique ID of the document.Occurrence:Always
documentMetadata | DocumentMetadata | This container provides the name, size, and type of the specified file.Occurrence:Conditional
documentMetadata.fileName | string | The name of the file including its extension (for example,drone_user_warranty.pdf).Occurrence:Conditional
documentMetadata.fileSize | string | The size, in bytes, of the document content.Occurrence:Conditional
documentMetadata.fileType | string | The type of the file uploaded. Supported file types include the following:pdf,jpeg,jpg, andpng.Occurrence:Conditional
documentStatus | DocumentStatusEnum | The status of the document resource.Once a document has been uploaded using theuploadDocumentmethod, thedocumentStatuswill beSUBMITTED. The document will then either be accepted or rejected. Only documents with the status ofACCEPTEDare available to be added to a listing.Occurrence:Always
documentType | DocumentTypeEnum | The type of the document uploaded. For example,USER_GUIDE_OR_MANUAL.Occurrence:Always
languages | array ofLanguageEnum | This array shows the language(s) used in the document.Occurrence:Always
[/TABLE]

[TABLE]
200 | Uploaded
400 | Bad Request
404 | Document Not Found
500 | Internal Server Error
[/TABLE]

[TABLE]
190052 | API_MEDIA | REQUEST | No document found with id {document_id}.
[/TABLE]