# commerce/media/resources/document/methods/getDocument

*Source: https://developer.ebay.com/api-docs/commerce/media/resources/document/methods/getDocument*

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

### Sample 1: Get Document Details

#### Thank you for helping us to improve the eBay developer program.
GET/document/{document_id}
This method retrieves the currentstatusand metadata of the specified document.Important!The document ID value returned in the response payload of thecreateDocumentmethod is a required input path parameter for this method.SeeManaging documentsfor additional information.
Important!The document ID value returned in the response payload of thecreateDocumentmethod is a required input path parameter for this method.
SeeManaging documentsfor additional information.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Required
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
All other standard RESTful request headers are optional. For more information on standard RESTful request headers, see theHTTP request headers- opens rest request components pagetable.
This request requires an access token created with theauthorization code grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope/sell.inventory
SeeOAuth access tokensfor more information.
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
This sample retrieves the details of a document for the specifieddocumentId1*******-**********d5including thedocumentMetadata,documentStatus,documentType, andlanguages.
The input isdocument_id. There is no payload with this request.
GEThttps://api.ebay.com/commerce/media/v1_beta/document/1*******-**********d5
If the call is successful, details of the document will be retrieved.
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
document_id | string | The unique identifier of the document for which status and metadata is being retrieved.This value is returned in the response of thecreateDocumentmethod.Occurrence:Required
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