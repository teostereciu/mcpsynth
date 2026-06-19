# commerce/taxonomy/resources/category_tree/methods/getCategorySuggestions

*Source: https://developer.ebay.com/api-docs/commerce/taxonomy/resources/category_tree/methods/getCategorySuggestions*

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

### Sample 1: Get category suggestions for a product

#### Thank you for helping us to improve the eBay developer program.
GET/category_tree/{category_tree_id}/get_category_suggestions
This call returns an array of category tree leaf nodes in the specified category tree that are considered by eBay to most closely correspond to the query stringq. Returned with each suggested node is a localized name for that category (based on theAccept-Languageheader specified for the call), and details about each of the category's ancestor nodes, extending from its immediate parent up to the root of the category tree.You identify the tree using thecategory_tree_idparameter, which was returned by thegetDefaultCategoryTreeIdcall in thecategoryTreeIdfield.Important:This call is not supported in the Sandbox environment. It will return a response payload in which thecategoryNamefields contain random or boilerplate text regardless of the query submitted.
This method is not supported in Sandbox environment.
Occurrence:Required
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
All other standard RESTful request headers are optional. For more information on standard RESTful request headers, see theHTTP request headers- opens rest request components pagetable.
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope
SeeOAuth access tokensfor more information.
This call has no payload.
This call has no field definitions.
This call has no response headers.
Contains details about one or more suggested categories that correspond to the provided keywords. The array of suggested categories is sorted in order of eBay's confidence of the relevance of each category (the first category is the most relevant).Important:This call is not supported in the Sandbox environment. It will return a response payload in which thecategoryNamefields contain random or boilerplate text regardless of the query submitted.Occurrence:Always
Occurrence:Always
Contains details about the suggested category.Occurrence:Always
The unique identifier of the eBay category within its category tree.Note:The root node of a full default category tree includes thecategoryIdfield, but its value should not be relied upon. It provides no useful information for application development.Occurrence:Always
The name of the category identified bycategoryId.Occurrence:Always
An ordered list of category references that describes the location of the suggested category in the specified category tree. The list identifies the category's ancestry as a sequence of parent nodes, from the current node's immediate parent to the root node of the category tree.Note:The root node of a full default category tree includescategoryIdandcategoryNamefields, but their values should not be relied upon. They provide no useful information for application development.Occurrence:Always
The unique identifier of the eBay ancestor category.Note:The root node of a full default category tree includes thecategoryIdfield, but its value should not be relied upon. It provides no useful information for application development.Occurrence:Always
The name of the ancestor category identified bycategoryId.Occurrence:Always
The href portion of thegetCategorySubtreecall that retrieves the subtree below the ancestor category node.Occurrence:Always
The absolute level of the ancestor category node in the hierarchy of its category tree.Note:The root node of any full category tree is always at level0.Occurrence:Always
The absolute level of the category tree node in the hierarchy of its category tree.Note:The root node of any full category tree is always at level0.Occurrence:Always
This field is reserved for internal or future use.Occurrence:NA
Occurrence:NA
The unique identifier of the eBay category tree from which suggestions are returned.Occurrence:Always
The version of the category tree identified bycategoryTreeId. It's a good idea to cache this value for comparison so you can determine if this category tree has been modified in subsequent calls.Occurrence:Always
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample retrieves an array of categories selected from the specified category tree which are considered by eBay to most closely correspond to the query string provided.
Use thecategory_tree_idpath parameter to specify the category tree, and use theqquery parameter to provide a free form string of search terms related to the product for which you want category suggestions.
GEThttps://api.ebay.com/commerce/taxonomy/v1/category_tree/0/get_category_suggestions?q=iphone
A successful call returns an array of categories, each one accompanied by details about each of the category's ancestor nodes, extending from its immediate parent up to the root of the category tree.
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
category_tree_id | string | The unique identifier of the eBay category tree. The category tree ID for an eBay marketplace can be retrieved using thegetDefaultCategoryTreeIdmethod.Occurrence:Required
q | string | A quoted string that describes or characterizes the item being offered for sale. The string format is free form, and can contain any combination of phrases or keywords. eBay will parse the string and return suggested categories for the item.Occurrence:Required
[/TABLE]

[TABLE]
Output container/field | Type | Description
categorySuggestions | array ofCategorySuggestion | Contains details about one or more suggested categories that correspond to the provided keywords. The array of suggested categories is sorted in order of eBay's confidence of the relevance of each category (the first category is the most relevant).Important:This call is not supported in the Sandbox environment. It will return a response payload in which thecategoryNamefields contain random or boilerplate text regardless of the query submitted.Occurrence:Always
categorySuggestions.category | Category | Contains details about the suggested category.Occurrence:Always
categorySuggestions.category.categoryId | string | The unique identifier of the eBay category within its category tree.Note:The root node of a full default category tree includes thecategoryIdfield, but its value should not be relied upon. It provides no useful information for application development.Occurrence:Always
categorySuggestions.category.categoryName | string | The name of the category identified bycategoryId.Occurrence:Always
categorySuggestions.categoryTreeNodeAncestors | array ofAncestorReference | An ordered list of category references that describes the location of the suggested category in the specified category tree. The list identifies the category's ancestry as a sequence of parent nodes, from the current node's immediate parent to the root node of the category tree.Note:The root node of a full default category tree includescategoryIdandcategoryNamefields, but their values should not be relied upon. They provide no useful information for application development.Occurrence:Always
categorySuggestions.categoryTreeNodeAncestors.categoryId | string | The unique identifier of the eBay ancestor category.Note:The root node of a full default category tree includes thecategoryIdfield, but its value should not be relied upon. It provides no useful information for application development.Occurrence:Always
categorySuggestions.categoryTreeNodeAncestors.categoryName | string | The name of the ancestor category identified bycategoryId.Occurrence:Always
categorySuggestions.categoryTreeNodeAncestors.categorySubtreeNodeHref | string | The href portion of thegetCategorySubtreecall that retrieves the subtree below the ancestor category node.Occurrence:Always
categorySuggestions.categoryTreeNodeAncestors.categoryTreeNodeLevel | integer | The absolute level of the ancestor category node in the hierarchy of its category tree.Note:The root node of any full category tree is always at level0.Occurrence:Always
categorySuggestions.categoryTreeNodeLevel | integer | The absolute level of the category tree node in the hierarchy of its category tree.Note:The root node of any full category tree is always at level0.Occurrence:Always
categorySuggestions.relevancy | string | This field is reserved for internal or future use.Occurrence:NA
categoryTreeId | string | The unique identifier of the eBay category tree from which suggestions are returned.Occurrence:Always
categoryTreeVersion | string | The version of the category tree identified bycategoryTreeId. It's a good idea to cache this value for comparison so you can determine if this category tree has been modified in subsequent calls.Occurrence:Always
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
62007 | API_TAXONOMY | REQUEST | Missing keyword 'q'. Please specify a valid set of keywords that best describes your item.
[/TABLE]