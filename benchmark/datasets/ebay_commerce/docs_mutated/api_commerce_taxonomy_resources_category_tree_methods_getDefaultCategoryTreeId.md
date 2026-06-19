# commerce/taxonomy/resources/category_tree/methods/getDefaultCategoryTreeId

*Source: https://developer.ebay.com/api-docs/commerce/taxonomy/resources/category_tree/methods/getDefaultCategoryTreeId*

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

### Sample 1: Get a default category tree ID

#### Thank you for helping us to improve the eBay developer program.
GET/get_default_category_tree_id
A given eBay marketplace might use multiple category trees, but one of those trees is considered to be the default for that marketplace. This call retrieves a reference to the default category tree associated with the specified eBay marketplace ID. The response includes only the tree's unique identifier and version, which you can use to retrieve more details about the tree, its structure, and its individual category nodes.
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Required
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
All other standard RESTful request headers are optional. For more information on standard RESTful request headers, see theHTTP request headers- opens rest request components pagetable.
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope
SeeOAuth access tokensfor more information.
This call has no payload.
This call has no field definitions.
This call has no response headers.
The unique identifier of the eBay category tree for the specified marketplace.Occurrence:Always
Occurrence:Always
The version of the category tree identified bycategoryTreeId. It's a good idea to cache this value for comparison so you can determine if this category tree has been modified in subsequent calls.Occurrence:Always
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample identifies the eBay category tree that is used by default by a given eBay marketplace.
Use themarketplace_idquery parameter to specify the eBay marketplace for which to retrieve the category tree ID. For a list of supported marketplaces and their IDs, seeMarketplaces with Default Category Trees.
GEThttps://api.ebay.com/commerce/taxonomy/v1/get_default_category_tree_id?marketplace_id=EBAY_AT
A successful call returns the category tree's ID and version.
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
marketplace_id | string | The unique identifier of the eBay marketplace for which the category tree ID is requested. For a list of supported marketplace IDs, seeMarketplaces with Default Category Trees.Occurrence:Required
[/TABLE]

[TABLE]
Output container/field | Type | Description
categoryTreeId | string | The unique identifier of the eBay category tree for the specified marketplace.Occurrence:Always
categoryTreeVersion | string | The version of the category tree identified bycategoryTreeId. It's a good idea to cache this value for comparison so you can determine if this category tree has been modified in subsequent calls.Occurrence:Always
[/TABLE]

[TABLE]
200 | Success
204 | No content
400 | Bad Request
500 | Internal Server Error
[/TABLE]

[TABLE]
62000 | API_TAXONOMY | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
62002 | API_TAXONOMY | REQUEST | Missing marketplace ID.
62003 | API_TAXONOMY | REQUEST | The specified marketplace ID was not found.
[/TABLE]