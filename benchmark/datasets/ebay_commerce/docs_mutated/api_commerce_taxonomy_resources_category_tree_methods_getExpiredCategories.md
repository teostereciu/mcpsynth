# commerce/taxonomy/resources/category_tree/methods/getExpiredCategories

*Source: https://developer.ebay.com/api-docs/commerce/taxonomy/resources/category_tree/methods/getExpiredCategories*

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

### Sample 1: Retrieve category mappings for expired categories

#### Thank you for helping us to improve the eBay developer program.
GET/category_tree/{category_tree_id}/get_expired_categories
This method retrieves the mappings of expired leaf categories in the specified category tree to their corresponding active leaf categories. Note that in some cases, several expired categories are mapped to a single active category.Note:This method only returns information about categories that have been mapped (i.e., combined categories and split categories). It does not return information about expired categories that have no corresponding active categories. When a category expires in this manner, any completed items that were listed in the expired category can still be found, but new listings cannot be created in the category.
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
An array of expired category ID(s) for the requested category tree, and the currently active category ID(s) that have replaced them.Occurrence:Always
Occurrence:Always
The unique identifier of the expired eBay leaf category.Occurrence:Always
The unique identifier of the currently active eBay leaf category that has replaced the expired leaf category.Note:More than onefromCategoryIDvalue may map into the sametoCategoryIDvalue, as multiple eBay categories may be consolidated into one new, expanded category.Occurrence:Always
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample retrieves an array of expired category IDs for the specified category tree and the corresponding active eBay leaf categories that have replaced them.
Use thecategory_tree_idpath parameter to specify the category tree for which to retrieve expired leaf categories and their associated active leaf categories.
GEThttps://api.ebay.com/commerce/taxonomy/v1/category_tree/0/get_expired_categories
A successful call returns an array of expired leaf categories (fromCategoryId), each one accompanied by the corresponding active leaf category (toCategoryId). Note that the response shown is only a sample of a much larger response.
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
category_tree_id | string | The unique identifier of the eBay category tree.The category tree ID for an eBay marketplace can be retrieved using thegetDefaultCategoryTreeIdmethod.Occurrence:Required
[/TABLE]

[TABLE]
Output container/field | Type | Description
expiredCategories | array ofExpiredCategory | An array of expired category ID(s) for the requested category tree, and the currently active category ID(s) that have replaced them.Occurrence:Always
expiredCategories.fromCategoryId | string | The unique identifier of the expired eBay leaf category.Occurrence:Always
expiredCategories.toCategoryId | string | The unique identifier of the currently active eBay leaf category that has replaced the expired leaf category.Note:More than onefromCategoryIDvalue may map into the sametoCategoryIDvalue, as multiple eBay categories may be consolidated into one new, expanded category.Occurrence:Always
[/TABLE]

[TABLE]
200 | Success
204 | No content
400 | Bad Request
404 | Not found
500 | Internal Server Error
[/TABLE]

[TABLE]
62000 | API_TAXONOMY | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
62004 | API_TAXONOMY | REQUEST | The specified category tree ID was not found.
62103 | API_TAXONOMY | REQUEST | The CategoryTreeId is not supported.
[/TABLE]