# commerce/taxonomy/resources/category_tree/methods/getCategorySubtree

*Source: https://developer.ebay.com/api-docs/commerce/taxonomy/resources/category_tree/methods/getCategorySubtree*

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

### Sample 1: Get a subtree of a category tree

#### Thank you for helping us to improve the eBay developer program.
GET/category_tree/{category_tree_id}/get_category_subtree
This call retrieves the details of all nodes of the category tree hierarchy (the subtree) below a specified category of a category tree. You identify the tree using thecategory_tree_idparameter, which was returned by thegetDefaultCategoryTreeIdcall in thecategoryTreeIdfield.Note:This method can return a very large payload, so gzip compression is supported. To enable gzip compression, include theAccept-Encodingheader and set its value togzipas shown below:Accept-Encoding: gzip
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
Contains details of all nodes of the category subtree hierarchy below a specified node. This is a recursive structure.Occurrence:Always
Occurrence:Always
Contains details about the current category tree node.Occurrence:Always
The unique identifier of the eBay category within its category tree.Note:The root node of a full default category tree includes thecategoryIdfield, but its value should not be relied upon. It provides no useful information for application development.Occurrence:Always
The name of the category identified bycategoryId.Occurrence:Always
The absolute level of the current category tree node in the hierarchy of its category tree.Note:The root node of any full category tree is always at level0.Occurrence:Always
An array of one or more category tree nodes that are the immediate children of the current category tree node, as well as their children, recursively down to the leaf nodes.Returned only ifthe current category tree node is not a leaf node (the value ofleafCategoryTreeNodeisfalse).Occurrence:Conditional
Occurrence:Conditional
A value oftrueindicates that the current category tree node is a leaf node (it has no child nodes). A value offalseindicates that the current node has one or more child nodes, which are identified by thechildCategoryTreeNodesarray.Returned only ifthe value of this field istrue.Occurrence:Conditional
The href portion of thegetCategorySubtreecall that retrieves the subtree below the parent of this category tree node.Not returned ifthe current category tree node is the root node of its tree.Occurrence:Conditional
The unique identifier of the eBay category tree to which this subtree belongs.Occurrence:Always
The version of the category tree identified bycategoryTreeId. It's a good idea to cache this value for comparison so you can determine if this category tree has been modified in subsequent calls.Occurrence:Always
This call can return one of the following HTTP status codes. For an overview of the status codes, seeHTTP status codesinUsing eBay RESTful APIs.
For more on errors, plus the codes of other common errors, seeHandling errors.
This call has no warnings.
New to making API calls? Please seeMaking a Call.
Note:Identifiers, such as order IDs or user IDs, and personal data in these samples might be anonymized or may no longer be active on eBay. If necessary, substitute current, relevant eBay data in your requests.
This sample retrieves the complete content of a subtree of an eBay category tree, using the category tree node that contains the specified category as the root of the desired subtree.
Use thecategory_tree_idpath parameter to specify the category tree, and use thecategory_idquery parameter to specify the category in the category node at the top of the subtree being requested.
GEThttps://api.ebay.com/commerce/taxonomy/v1/category_tree/0/get_category_subtree?category_id=11450
A successful call returns the complete category subtree specified, from the specified category node to all leaf nodes of the subtree. In this sample, the returned category subtree contains almost 600 categories, so the response shown here has most of the nodes removed for easier viewing.
Related topics
If you need help, contactDeveloper Technical Support.
- API DocumentationCatalog APICharity APIIdentity APIMedia APINotification APITaxonomy APITranslation API Beta
- GuidesBuying Integration GuideSelling Integration GuideTaxonomy Migration Guide
- Related DocsUsing eBay RESTful APIsBuy APIsSell APIsDeveloper APIs

[TABLE]
Parameter | Type | Description
category_tree_id | string | The unique identifier of the eBay category tree. The category tree ID for an eBay marketplace can be retrieved using thegetDefaultCategoryTreeIdmethod.Occurrence:Required
category_id | string | The unique identifier of the category at the top of the subtree being requested. Metadata on this category and all its descendant categories are retrieved.Note:If thecategory_idsubmitted identifies a leaf node of the tree, the call response will contain information about only that leaf node, which is a valid subtree.Occurrence:Required
[/TABLE]

[TABLE]
Header | Type | Description
Accept-Encoding | string | This header indicates the compression-encoding algorithms the client accepts for the response. This value should be set togzip.For more information, refer toHTTP request headers.Occurrence:Optional
[/TABLE]

[TABLE]
Output container/field | Type | Description
categorySubtreeNode | CategoryTreeNode | Contains details of all nodes of the category subtree hierarchy below a specified node. This is a recursive structure.Occurrence:Always
categorySubtreeNode.category | Category | Contains details about the current category tree node.Occurrence:Always
categorySubtreeNode.category.categoryId | string | The unique identifier of the eBay category within its category tree.Note:The root node of a full default category tree includes thecategoryIdfield, but its value should not be relied upon. It provides no useful information for application development.Occurrence:Always
categorySubtreeNode.category.categoryName | string | The name of the category identified bycategoryId.Occurrence:Always
categorySubtreeNode.categoryTreeNodeLevel | integer | The absolute level of the current category tree node in the hierarchy of its category tree.Note:The root node of any full category tree is always at level0.Occurrence:Always
categorySubtreeNode.childCategoryTreeNodes | array ofCategoryTreeNode | An array of one or more category tree nodes that are the immediate children of the current category tree node, as well as their children, recursively down to the leaf nodes.Returned only ifthe current category tree node is not a leaf node (the value ofleafCategoryTreeNodeisfalse).Occurrence:Conditional
categorySubtreeNode.childCategoryTreeNodes.category | Category | Contains details about the current category tree node.Occurrence:Always
categorySubtreeNode.childCategoryTreeNodes.category.categoryId | string | The unique identifier of the eBay category within its category tree.Note:The root node of a full default category tree includes thecategoryIdfield, but its value should not be relied upon. It provides no useful information for application development.Occurrence:Always
categorySubtreeNode.childCategoryTreeNodes.category.categoryName | string | The name of the category identified bycategoryId.Occurrence:Always
categorySubtreeNode.childCategoryTreeNodes.categoryTreeNodeLevel | integer | The absolute level of the current category tree node in the hierarchy of its category tree.Note:The root node of any full category tree is always at level0.Occurrence:Always
categorySubtreeNode.childCategoryTreeNodes.childCategoryTreeNodes | array ofCategoryTreeNode | An array of one or more category tree nodes that are the immediate children of the current category tree node, as well as their children, recursively down to the leaf nodes.Returned only ifthe current category tree node is not a leaf node (the value ofleafCategoryTreeNodeisfalse).Occurrence:Conditional
categorySubtreeNode.childCategoryTreeNodes.childCategoryTreeNodes.category | Category | Contains details about the current category tree node.Occurrence:Always
categorySubtreeNode.childCategoryTreeNodes.childCategoryTreeNodes.category.categoryId | string | The unique identifier of the eBay category within its category tree.Note:The root node of a full default category tree includes thecategoryIdfield, but its value should not be relied upon. It provides no useful information for application development.Occurrence:Always
categorySubtreeNode.childCategoryTreeNodes.childCategoryTreeNodes.category.categoryName | string | The name of the category identified bycategoryId.Occurrence:Always
categorySubtreeNode.childCategoryTreeNodes.childCategoryTreeNodes.categoryTreeNodeLevel | integer | The absolute level of the current category tree node in the hierarchy of its category tree.Note:The root node of any full category tree is always at level0.Occurrence:Always
categorySubtreeNode.childCategoryTreeNodes.childCategoryTreeNodes.childCategoryTreeNodes | array ofCategoryTreeNode | An array of one or more category tree nodes that are the immediate children of the current category tree node, as well as their children, recursively down to the leaf nodes.Returned only ifthe current category tree node is not a leaf node (the value ofleafCategoryTreeNodeisfalse).Occurrence:Conditional
categorySubtreeNode.childCategoryTreeNodes.childCategoryTreeNodes.leafCategoryTreeNode | boolean | A value oftrueindicates that the current category tree node is a leaf node (it has no child nodes). A value offalseindicates that the current node has one or more child nodes, which are identified by thechildCategoryTreeNodesarray.Returned only ifthe value of this field istrue.Occurrence:Conditional
categorySubtreeNode.childCategoryTreeNodes.childCategoryTreeNodes.parentCategoryTreeNodeHref | string | The href portion of thegetCategorySubtreecall that retrieves the subtree below the parent of this category tree node.Not returned ifthe current category tree node is the root node of its tree.Occurrence:Conditional
categorySubtreeNode.childCategoryTreeNodes.leafCategoryTreeNode | boolean | A value oftrueindicates that the current category tree node is a leaf node (it has no child nodes). A value offalseindicates that the current node has one or more child nodes, which are identified by thechildCategoryTreeNodesarray.Returned only ifthe value of this field istrue.Occurrence:Conditional
categorySubtreeNode.childCategoryTreeNodes.parentCategoryTreeNodeHref | string | The href portion of thegetCategorySubtreecall that retrieves the subtree below the parent of this category tree node.Not returned ifthe current category tree node is the root node of its tree.Occurrence:Conditional
categorySubtreeNode.leafCategoryTreeNode | boolean | A value oftrueindicates that the current category tree node is a leaf node (it has no child nodes). A value offalseindicates that the current node has one or more child nodes, which are identified by thechildCategoryTreeNodesarray.Returned only ifthe value of this field istrue.Occurrence:Conditional
categorySubtreeNode.parentCategoryTreeNodeHref | string | The href portion of thegetCategorySubtreecall that retrieves the subtree below the parent of this category tree node.Not returned ifthe current category tree node is the root node of its tree.Occurrence:Conditional
categoryTreeId | string | The unique identifier of the eBay category tree to which this subtree belongs.Occurrence:Always
categoryTreeVersion | string | The version of the category tree identified bycategoryTreeId. It's a good idea to cache this value for comparison so you can determine if this category tree has been modified in subsequent calls.Occurrence:Always
[/TABLE]

[TABLE]
200 | Success
400 | Bad Request
404 | Not Found
500 | Internal Server Error
[/TABLE]

[TABLE]
62000 | API_TAXONOMY | APPLICATION | There was a problem with an eBay internal system or process. Contact eBay developer support for assistance.
62004 | API_TAXONOMY | REQUEST | The specified category tree ID was not found.
62005 | API_TAXONOMY | REQUEST | The specified category ID does not belong to the specified category tree.
62006 | API_TAXONOMY | REQUEST | Missing category ID.
62008 | API_TAXONOMY | REQUEST | The specified category ID is the root for the category tree. Please use{categoryTreeHref}to retrieve the entire tree.
[/TABLE]