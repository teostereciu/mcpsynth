# commerce/media/resources/document/methods/createDocument

*Source: https://developer.ebay.com/api-docs/commerce/media/resources/document/methods/createDocument*

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

### Sample 1: 
	Create a document ID

#### Thank you for helping us to improve the eBay developer program.
POST/document
This method stages a document to be uploaded, and requires the type of document to be uploaded, and the language(s) that the document contains. A successful call returns adocumentIdvalue that is then used as a path parameter in anuploadDocumentcall.When a document is successfully created, the method returns the HTTP Status Code201 Created.The method returnsdocumentIdin the response payload, which you can use to retrieve the document resource. This ID is also returned in thelocationheader, for convenience.Important!Make sure to capture the document ID value returned in the response payload. This value is required to use the other methods in thedocumentresource, and also needed to associate a document to a listing using the Trading and Inventory APIs.To upload a created document, use the document ID returned from this method's response with theuploadDocumentmethod. SeeManaging documentsfor information on creating, uploading, and adding documents to listings.Important!All POST methods in the Media API, including this method, are subject to short-duration rate limits at the user level: 50 requests per 5 seconds.
When a document is successfully created, the method returns the HTTP Status Code201 Created.The method returnsdocumentIdin the response payload, which you can use to retrieve the document resource. This ID is also returned in thelocationheader, for convenience.
Important!Make sure to capture the document ID value returned in the response payload. This value is required to use the other methods in thedocumentresource, and also needed to associate a document to a listing using the Trading and Inventory APIs.
To upload a created document, use the document ID returned from this method's response with theuploadDocumentmethod. SeeManaging documentsfor information on creating, uploading, and adding documents to listings.
Important!All POST methods in the Media API, including this method, are subject to short-duration rate limits at the user level: 50 requests per 5 seconds.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
This method has no URI parameters.
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
Occurrence:Required
This request requires an access token created with theauthorization code grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope/sell.inventory
SeeOAuth access tokensfor more information.
The type of the document being uploaded. For example, aUSER_GUIDE_OR_MANUALor aSAFETY_DATA_SHEET.Occurrence:Required
This array shows the language(s) used in the document.Occurrence:Required
SeeHTTP response headersfor details.
The unique identifier of the document to be uploaded.This value is returned in the response andlocationheader of thecreateDocumentandcreateDocumentFromUrlmethods. This ID can be used with thegetDocumentanduploadDocumentmethods, and to add an uploaded document to a listing. SeeAdding documents to listingsfor more information.Occurrence:Always
Occurrence:Always
The status of the document resource.For example, the valuePENDING_UPLOADis the initial state when the reference to the document has been created using thecreateDocumentmethod. When creating a document using thecreateDocumentFromUrlmethod, the initial state will beSUBMITTED.Occurrence:Always
The type of the document uploaded. For example,USER_GUIDE_OR_MANUAL.Occurrence:Always
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample creates a document ID using provided metadata to be used when uploading a document. Metadata includesdocumentTypeandlanguages.
The inputs are thedocumentTypeandlanguagesarray.
POSThttps://api.ebay.com/commerce/media/v1_beta/document
A successful call will show an HTTP status of 201 Created and the following payload. If the call is successful, the document will be created and the document ID is returned in the response payload as well as theLocationheader. The response payload includes the document ID, status, type, and language(s).
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Header | Type | Description
Content-Type | string | This header indicates the format of the request body provided by the client. Its value should be set toapplication/json.For more information, refer toHTTP request headers.Occurrence:Required
[/TABLE]

[TABLE]
Input container/field | Type | Description
documentType | DocumentTypeEnum | The type of the document being uploaded. For example, aUSER_GUIDE_OR_MANUALor aSAFETY_DATA_SHEET.Occurrence:Required
languages | array ofLanguageEnum | This array shows the language(s) used in the document.Occurrence:Required
[/TABLE]

[TABLE]
Location | Thelocationresponse header returns thegetDocumentURI.
[/TABLE]

[TABLE]
Output container/field | Type | Description
documentId | string | The unique identifier of the document to be uploaded.This value is returned in the response andlocationheader of thecreateDocumentandcreateDocumentFromUrlmethods. This ID can be used with thegetDocumentanduploadDocumentmethods, and to add an uploaded document to a listing. SeeAdding documents to listingsfor more information.Occurrence:Always
documentStatus | DocumentStatusEnum | The status of the document resource.For example, the valuePENDING_UPLOADis the initial state when the reference to the document has been created using thecreateDocumentmethod. When creating a document using thecreateDocumentFromUrlmethod, the initial state will beSUBMITTED.Occurrence:Always
documentType | DocumentTypeEnum | The type of the document uploaded. For example,USER_GUIDE_OR_MANUAL.Occurrence:Always
languages | array ofLanguageEnum | This array shows the language(s) used in the document.Occurrence:Always
[/TABLE]

[TABLE]
201 | Created
400 | Bad Request
500 | Internal Server Error
[/TABLE]

[TABLE]
190050 | API_MEDIA | REQUEST | Missing or invalid 'languages' value(s).
190051 | API_MEDIA | REQUEST | Missing or invalid 'documentType' value.
[/TABLE]