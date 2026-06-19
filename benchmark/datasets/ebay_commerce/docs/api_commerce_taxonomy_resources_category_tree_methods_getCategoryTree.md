# commerce/taxonomy/resources/category_tree/methods/getCategoryTree

*Source: https://developer.ebay.com/api-docs/commerce/taxonomy/resources/category_tree/methods/getCategoryTree*

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

### Sample 1: Get a complete category tree

#### Thank you for helping us to improve the eBay developer program.
GET/category_tree/{category_tree_id}
This method retrieves the complete category tree that is identified by thecategory_tree_idparameter. The value ofcategory_tree_idwas returned by thegetDefaultCategoryTreeIdmethod in thecategoryTreeIdfield. The response contains details of all nodes of the specified eBay category tree, as well as the eBay marketplaces that use this category tree.Note:This method can return a very large payload, so gzip compression is supported. To enable gzip compression, include theAccept-Encodingheader and set its value togzipas shown below:Accept-Encoding: gzip
This method is supported in Sandbox environment. To access the endpoint, just replace theapi.ebay.comroot URI withapi.sandbox.ebay.com
Occurrence:Required
All requests made to eBay REST operations require you to provide theAuthorizationHTTP header for authentication authorization.
The table below shows additional HTTP request headers that are either required, conditionally required, or strongly recommended for this method. Other standardHTTP request headers- opens rest request components page(not in this table) can also be used, but they are optional.
Occurrence:Optional
This request requires an access token created with theclient credentials grantflow, using one or more scopes from the following list (please check your Application Keys page for a list of OAuth scopes available to your application):
https://api.ebay.com/oauth/api_scope
SeeOAuth access tokensfor more information.
This call has no payload.
This call has no field definitions.
This call has no response headers.
A list of one or more identifiers of the eBay marketplaces that use this category tree.Occurrence:Always
Occurrence:Always
The unique identifier of this eBay category tree.Occurrence:Always
The version of this category tree. It's a good idea to cache this value for comparison so you can determine if this category tree has been modified in subsequent calls.Occurrence:Always
Contains details of all nodes of the category tree hierarchy, starting with the root node and down to the leaf nodes. This is a recursive structure.Note:The root node of a full default category tree includes thecategoryIdfield, but its value should not be relied upon. It provides no useful information for application development.Occurrence:Always
Contains details about the current category tree node.Occurrence:Always
The unique identifier of the eBay category within its category tree.Note:The root node of a full default category tree includes thecategoryIdfield, but its value should not be relied upon. It provides no useful information for application development.Occurrence:Always
The name of the category identified bycategoryId.Occurrence:Always
The absolute level of the current category tree node in the hierarchy of its category tree.Note:The root node of any full category tree is always at level0.Occurrence:Always
An array of one or more category tree nodes that are the immediate children of the current category tree node, as well as their children, recursively down to the leaf nodes.Returned only ifthe current category tree node is not a leaf node (the value ofleafCategoryTreeNodeisfalse).Occurrence:Conditional
Occurrence:Conditional
A value oftrueindicates that the current category tree node is a leaf node (it has no child nodes). A value offalseindicates that the current node has one or more child nodes, which are identified by thechildCategoryTreeNodesarray.Returned only ifthe value of this field istrue.Occurrence:Conditional
The href portion of thegetCategorySubtreecall that retrieves the subtree below the parent of this category tree node.Not returned ifthe current category tree node is the root node of its tree.Occurrence:Conditional
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample retrieves the complete content of the specified category tree.
Use thecategory_tree_idpath parameter to specify the category tree to retrieve. It is not necessary to specify an eBay marketplace.
GEThttps://api.ebay.com/commerce/taxonomy/v1/category_tree/0
A successful call returns the complete category tree specified, from the root node to all leaf nodes of the tree. In this sample, the returned category tree contains almost 20,000 categories, so the response shown here has most of the nodes removed for easier viewing.
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
category_tree_id | string | The unique identifier of the eBay category tree. The category tree ID for an eBay marketplace can be retrieved using thegetDefaultCategoryTreeIdmethod.Occurrence:Required
[/TABLE]

[TABLE]
Header | Type | Description
Accept-Encoding | string | This header indicates the compression-encoding algorithms the client accepts for the response. This value should be set togzip.For more information, refer toHTTP request headers.Occurrence:Optional
[/TABLE]

[TABLE]
Output container/field | Type | Description
applicableMarketplaceIds | array ofMarketplaceIdEnum | A list of one or more identifiers of the eBay marketplaces that use this category tree.Occurrence:Always
categoryTreeId | string | The unique identifier of this eBay category tree.Occurrence:Always
categoryTreeVersion | string | The version of this category tree. It's a good idea to cache this value for comparison so you can determine if this category tree has been modified in subsequent calls.Occurrence:Always
rootCategoryNode | CategoryTreeNode | Contains details of all nodes of the category tree hierarchy, starting with the root node and down to the leaf nodes. This is a recursive structure.Note:The root node of a full default category tree includes thecategoryIdfield, but its value should not be relied upon. It provides no useful information for application development.Occurrence:Always
rootCategoryNode.category | Category | Contains details about the current category tree node.Occurrence:Always
rootCategoryNode.category.categoryId | string | The unique identifier of the eBay category within its category tree.Note:The root node of a full default category tree includes thecategoryIdfield, but its value should not be relied upon. It provides no useful information for application development.Occurrence:Always
rootCategoryNode.category.categoryName | string | The name of the category identified bycategoryId.Occurrence:Always
rootCategoryNode.categoryTreeNodeLevel | integer | The absolute level of the current category tree node in the hierarchy of its category tree.Note:The root node of any full category tree is always at level0.Occurrence:Always
rootCategoryNode.childCategoryTreeNodes | array ofCategoryTreeNode | An array of one or more category tree nodes that are the immediate children of the current category tree node, as well as their children, recursively down to the leaf nodes.Returned only ifthe current category tree node is not a leaf node (the value ofleafCategoryTreeNodeisfalse).Occurrence:Conditional
rootCategoryNode.childCategoryTreeNodes.category | Category | Contains details about the current category tree node.Occurrence:Always
rootCategoryNode.childCategoryTreeNodes.category.categoryId | string | The unique identifier of the eBay category within its category tree.Note:The root node of a full default category tree includes thecategoryIdfield, but its value should not be relied upon. It provides no useful information for application development.Occurrence:Always
rootCategoryNode.childCategoryTreeNodes.category.categoryName | string | The name of the category identified bycategoryId.Occurrence:Always
rootCategoryNode.childCategoryTreeNodes.categoryTreeNodeLevel | integer | The absolute level of the current category tree node in the hierarchy of its category tree.Note:The root node of any full category tree is always at level0.Occurrence:Always
rootCategoryNode.childCategoryTreeNodes.childCategoryTreeNodes | array ofCategoryTreeNode | An array of one or more category tree nodes that are the immediate children of the current category tree node, as well as their children, recursively down to the leaf nodes.Returned only ifthe current category tree node is not a leaf node (the value ofleafCategoryTreeNodeisfalse).Occurrence:Conditional
rootCategoryNode.childCategoryTreeNodes.childCategoryTreeNodes.category | Category | Contains details about the current category tree node.Occurrence:Always
rootCategoryNode.childCategoryTreeNodes.childCategoryTreeNodes.category.categoryId | string | The unique identifier of the eBay category within its category tree.Note:The root node of a full default category tree includes thecategoryIdfield, but its value should not be relied upon. It provides no useful information for application development.Occurrence:Always
rootCategoryNode.childCategoryTreeNodes.childCategoryTreeNodes.category.categoryName | string | The name of the category identified bycategoryId.Occurrence:Always
rootCategoryNode.childCategoryTreeNodes.childCategoryTreeNodes.categoryTreeNodeLevel | integer | The absolute level of the current category tree node in the hierarchy of its category tree.Note:The root node of any full category tree is always at level0.Occurrence:Always
rootCategoryNode.childCategoryTreeNodes.childCategoryTreeNodes.childCategoryTreeNodes | array ofCategoryTreeNode | An array of one or more category tree nodes that are the immediate children of the current category tree node, as well as their children, recursively down to the leaf nodes.Returned only ifthe current category tree node is not a leaf node (the value ofleafCategoryTreeNodeisfalse).Occurrence:Conditional
rootCategoryNode.childCategoryTreeNodes.childCategoryTreeNodes.leafCategoryTreeNode | boolean | A value oftrueindicates that the current category tree node is a leaf node (it has no child nodes). A value offalseindicates that the current node has one or more child nodes, which are identified by thechildCategoryTreeNodesarray.Returned only ifthe value of this field istrue.Occurrence:Conditional
rootCategoryNode.childCategoryTreeNodes.childCategoryTreeNodes.parentCategoryTreeNodeHref | string | The href portion of thegetCategorySubtreecall that retrieves the subtree below the parent of this category tree node.Not returned ifthe current category tree node is the root node of its tree.Occurrence:Conditional
rootCategoryNode.childCategoryTreeNodes.leafCategoryTreeNode | boolean | A value oftrueindicates that the current category tree node is a leaf node (it has no child nodes). A value offalseindicates that the current node has one or more child nodes, which are identified by thechildCategoryTreeNodesarray.Returned only ifthe value of this field istrue.Occurrence:Conditional
rootCategoryNode.childCategoryTreeNodes.parentCategoryTreeNodeHref | string | The href portion of thegetCategorySubtreecall that retrieves the subtree below the parent of this category tree node.Not returned ifthe current category tree node is the root node of its tree.Occurrence:Conditional
rootCategoryNode.leafCategoryTreeNode | boolean | A value oftrueindicates that the current category tree node is a leaf node (it has no child nodes). A value offalseindicates that the current node has one or more child nodes, which are identified by thechildCategoryTreeNodesarray.Returned only ifthe value of this field istrue.Occurrence:Conditional
rootCategoryNode.parentCategoryTreeNodeHref | string | The href portion of thegetCategorySubtreecall that retrieves the subtree below the parent of this category tree node.Not returned ifthe current category tree node is the root node of its tree.Occurrence:Conditional
[/TABLE]

[TABLE]
200 | Success
404 | Not Found
500 | Internal Server Error
[/TABLE]

[TABLE]
62000 | API_TAXONOMY | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
62004 | API_TAXONOMY | REQUEST | The specified category tree ID was not found.
[/TABLE]