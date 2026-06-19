# SmartCollection

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/smartcollection*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# SmartCollection

Ask assistant

Requires `products` access scope.

**Requires `products` access scope.:**

A smart collection is a grouping of products defined by rules that are set by the merchant. Shopify automatically changes the contents of a smart collection based on the rules. Smart collections, like other types of collections, are used to break down the catalog of products into categories and make the shop easier to browse.

By default, a store can have up to 5000 smart collections.

The [Collect](/docs/admin-api/rest/reference/products/collect) resource is used to connect a product to a smart collection. However, these collects can't be added or removed from the API as they're managed by the rules of the smart collection.

You can use the [CustomCollection](/docs/admin-api/rest/reference/products/customcollection) resource to work with collections where each product in the collection is manually chosen by the merchant.

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/smart_collections.json](/docs/api/admin-rest/latest/resources/smartcollection#post-smart-collections)

Creates a smart collection

[collectionCreate](/docs/api/admin-graphql/latest/mutations/collectionCreate)

  * [get/admin/api/latest/smart_collections.json?since_id=482865238](/docs/api/admin-rest/latest/resources/smartcollection#get-smart-collections?since-id=482865238)

Retrieves a list of smart collections

[collections](/docs/api/admin-graphql/latest/queries/collections)

  * [get/admin/api/latest/smart_collections/{smart_collection_id}.json](/docs/api/admin-rest/latest/resources/smartcollection#get-smart-collections-smart-collection-id)

Retrieves a single smart collection

[collection](/docs/api/admin-graphql/latest/queries/collection)

  * [get/admin/api/latest/smart_collections/count.json](/docs/api/admin-rest/latest/resources/smartcollection#get-smart-collections-count)

Retrieves a count of smart collections

[collectionsCount](/docs/api/admin-graphql/latest/queries/collectionsCount?example=retrieves-a-count-of-smart-collections)

  * [put/admin/api/latest/smart_collections/{smart_collection_id}.json](/docs/api/admin-rest/latest/resources/smartcollection#put-smart-collections-smart-collection-id)

Updates an existing smart collection

[collectionUpdate](/docs/api/admin-graphql/latest/mutations/collectionUpdate?example=updates-an-existing-smart-collection)

  * [put/admin/api/latest/smart_collections/{smart_collection_id}/order.json?products[]=921728736&products[]=632910392](/docs/api/admin-rest/latest/resources/smartcollection#put-smart-collections-smart-collection-id-order?products\[\]=921728736&products\[\]=632910392)

Updates the ordering type of products in a smart collection

[collectionUpdate](/docs/api/admin-graphql/latest/mutations/collectionUpdate)

[collectionReorderProducts](/docs/api/admin-graphql/latest/mutations/collectionReorderProducts?example=updates-the-ordering-type-of-products-in-a-smart-collection)

  * [del/admin/api/latest/smart_collections/{smart_collection_id}.json](/docs/api/admin-rest/latest/resources/smartcollection#delete-smart-collections-smart-collection-id)

Removes a smart collection

[collectionDelete](/docs/api/admin-graphql/latest/mutations/collectionDelete?example=removes-a-smart-collection)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/smartcollection#resource-object)

## The SmartCollection resource

[Anchor to ](/docs/api/admin-rest/latest/resources/smartcollection#resource-object-properties)

### Properties

* * *

body_html

->[descriptionHtml](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.descriptionHtml)

The description of the smart collection. Includes HTML markup. Many shop themes display this on the smart collection page.

* * *

handle

->[handle](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.handle)

A human-friendly unique string for the smart collection. Automatically generated from the `title`. Used in shop themes by the Liquid templating language to refer to the smart collection. (maximum: 255 characters)

* * *

id

->[id](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.id)

The ID of the smart collection.

* * *

image

->[image](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.image)

The image associated with the smart collection. Valid values:

Show image properties

  * `attachment`: An image attached to a smart collection returned as Base64-encoded binary data.
  * `src`: A URL that specifies the location of the image.
  * `alt`: Alternative text that describes the collection image.


* * *

published_at

->[publishDate](/docs/api/admin-graphql/latest/objects/ResourcePublication#field-ResourcePublication.fields.publishDate)

The date and time ([ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601)) that the smart collection was published. Returns `null` when the collection is hidden.

* * *

published_scope

->[publishable](/docs/api/admin-graphql/latest/objects/ResourcePublication#field-ResourcePublication.fields.publishable)

Whether the smart collection is published to the Point of Sale channel. Valid values:

Show published_scope properties

  * `web`: The smart collection is published to the Online Store channel but not published to the Point of Sale channel.
  * `global`: The smart collection is published to both the Online Store channel and the Point of Sale channel.


* * *

rules

->[ruleSet](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.ruleSet)

The list of rules that define what products go into the smart collection. Each rule has the following properties:

Show rules properties

  * **column** : The property of a product being used to populate the smart collection.

Valid values for text relations:

    * `title`: The product title.
    * `type`: The product type.
    * `vendor`: The name of the product vendor.
    * `variant_title`: The title of a product variant.

Valid values for number relations:

    * `variant_compare_at_price`: The compare price.
    * `variant_weight`: The weight of the product.
    * `variant_inventory`: The inventory stock. Note: `not_equals` does not work with this property.
    * `variant_price`: product price.

Valid values for an `equals` relation:

    * `tag`: A tag associated with the product.

Valid values for metafield definition relations:

    * `product_metafield_definition`: When the metafield definition rule is powered by a product metafield definition.
    * `variant_metafield_definition`: When the metafield definition rule is powered by a variant metafield definition.
  * **relation** : The relationship between the **column** choice, and the **condition**.

Valid values for number relations:

    * `greater_than` The column value is greater than the condition.
    * `less_than` The column value is less than the condition.
    * `equals` The column value is equal to the condition.
    * `not_equals` The column value is not equal to the condition.

Valid values for text relations:

    * `equals`: Checks if the **column** value is equal to the **condition** value.
    * `not_equals`: Checks if the **column** value is not equal to the **condition** value.
    * `starts_with`: Checks if the **column** value starts with the **condition** value.
    * `ends_with`: Checks if the **column** value ends with the **condition** value.
    * `contains`: Checks if the **column** value contains the **condition** value.
    * `not_contains`: Checks if the **column** value does not contain the **condition** value.

Valid values for metafield relations are based on the corresponding metafield definition type. The following definition types support the listed relations

    * `rating`: `equals`, `greater_than`, `less_than`
    * `boolean`: `equals`
    * `number_integer`: `equals`, `greater_than`, `less_than`
    * `number_decimal`: `equals`, `greater_than`, `less_than`
    * `single_line_text_field`: `equals`
    * `list.single_line_text_field`: `equals`
  * **condition** : Select products for a smart collection using a condition. Values are either strings or numbers, depending on the **relation** value.

  * **condition_object_id** : The object id that points to additional attributes for the collection rule. This is only required when using metafield definition rules.


* * *

disjunctive

->[appliedDisjunctively](/docs/api/admin-graphql/latest/objects/CollectionRuleSet#field-CollectionRuleSet.fields.appliedDisjunctively)

Whether the product must match all the rules to be included in the smart collection. Valid values:

Show disjunctive properties

  * `true`: Products only need to match one or more of the rules to be included in the smart collection.
  * `false`: Products must match all of the rules to be included in the smart collection.


* * *

sort_order

->[sortOrder](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.sortOrder)

The order of the products in the smart collection. Valid values:

Show sort_order properties

  * `alpha-asc`: The products are sorted alphabetically from A to Z.
  * `alpha-des`: The products are sorted alphabetically from Z to A.
  * `best-selling`: The products are sorted by number of sales.
  * `created`: The products are sorted by the date they were created, from oldest to newest.
  * `created-desc`: The products are sorted by the date they were created, from newest to oldest.
  * `manual`: The products are manually sorted by the shop owner.
  * `price-asc`: The products are sorted by price from lowest to highest.
  * `price-desc`: The products are sorted by price from highest to lowest.


* * *

template_suffix

->[templateSuffix](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.templateSuffix)

The suffix of the Liquid template that the shop uses. By default, the original template is called product.liquid, and additional templates are called product.`suffix`.liquid.

* * *

title

->[title](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.title)

The name of the smart collection. Maximum length: 255 characters.

* * *

updated_at

read-only**read-only**

->[updatedAt](/docs/api/admin-graphql/latest/objects/Collection#field-Collection.fields.updatedAt)

The date and time ([ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601)) when the smart collection was last modified.

* * *

Was this section helpful?

YesNo

{}

## The SmartCollection resource

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

{

"body_html": "<p>The best selling ipod ever</p>",

"handle": "smart-ipods",

"id": 482865238,

"image": {

"src": "http://static.shopify.com/collections/ipod.jpg?0",

"alt": "iPods"

},

"published_at": "2008-02-01T19:00:00-05:00",

"published_scope": "global",

"rules": {

"column": "variant_price",

"relation": "less_than",

"condition": "20"

},

"disjunctive": false,

"sort_order": "alpha-asc",

"template_suffix": null,

"title": "Smart iPods",

"updated_at": "2008-02-01T19:00:00-05:00"

}

* * *

##

[Anchor to POST request, Creates a smart collection](/docs/api/admin-rest/latest/resources/smartcollection#post-smart-collections)

post

Creates a smart collection

[collectionCreate](/docs/api/admin-graphql/latest/mutations/collectionCreate)

Creates a new smart collection using the specified rules.

###

[Anchor to Parameters of Creates a smart collection](/docs/api/admin-rest/latest/resources/smartcollection#post-smart-collections-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-smart-collections-examples](/docs/api/admin-rest/latest/resources/smartcollection#post-smart-collections-examples)Examples

Create a new smart collection with a base64 encoded image

Request body

smart_collection

Smart_collection resource**Smart_collection resource**

Show smart_collection properties

smart_collection.title:"Macbooks"

->[title](/docs/api/admin-graphql/latest/input-objects/CollectionInput#fields-title)

The name of the smart collection. Maximum length: 255 characters.

smart_collection.rules:[{"column":"vendor","relation":"equals","condition":"Apple"}]

->[ruleSet](/docs/api/admin-graphql/latest/input-objects/CollectionInput#fields-ruleSet)

The list of rules that define what products go into the smart collection. Each rule has the following properties:

Show rules properties

  * **column** : The property of a product being used to populate the smart collection.

Valid values for text relations:

    * `title`: The product title.
    * `type`: The product type.
    * `vendor`: The name of the product vendor.
    * `variant_title`: The title of a product variant.

Valid values for number relations:

    * `variant_compare_at_price`: The compare price.
    * `variant_weight`: The weight of the product.
    * `variant_inventory`: The inventory stock. Note: `not_equals` does not work with this property.
    * `variant_price`: product price.

Valid values for an `equals` relation:

    * `tag`: A tag associated with the product.

Valid values for metafield definition relations:

    * `product_metafield_definition`: When the metafield definition rule is powered by a product metafield definition.
    * `variant_metafield_definition`: When the metafield definition rule is powered by a variant metafield definition.
  * **relation** : The relationship between the **column** choice, and the **condition**.

Valid values for number relations:

    * `greater_than` The column value is greater than the condition.
    * `less_than` The column value is less than the condition.
    * `equals` The column value is equal to the condition.
    * `not_equals` The column value is not equal to the condition.

Valid values for text relations:

    * `equals`: Checks if the **column** value is equal to the **condition** value.
    * `not_equals`: Checks if the **column** value is not equal to the **condition** value.
    * `starts_with`: Checks if the **column** value starts with the **condition** value.
    * `ends_with`: Checks if the **column** value ends with the **condition** value.
    * `contains`: Checks if the **column** value contains the **condition** value.
    * `not_contains`: Checks if the **column** value does not contain the **condition** value.

Valid values for metafield relations are based on the corresponding metafield definition type. The following definition types support the listed relations

    * `rating`: `equals`, `greater_than`, `less_than`
    * `boolean`: `equals`
    * `number_integer`: `equals`, `greater_than`, `less_than`
    * `number_decimal`: `equals`, `greater_than`, `less_than`
    * `single_line_text_field`: `equals`
    * `list.single_line_text_field`: `equals`
  * **condition** : Select products for a smart collection using a condition. Values are either strings or numbers, depending on the **relation** value.

  * **condition_object_id** : The object id that points to additional attributes for the collection rule. This is only required when using metafield definition rules.


smart_collection.image:{"attachment":"R0lGODlhAQABAIAAAAAAAAAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==\n","alt":"iPod"}

->[image](/docs/api/admin-graphql/latest/input-objects/CollectionInput#fields-image)

The image associated with the smart collection. Valid values:

Show image properties

  * `attachment`: An image attached to a smart collection returned as Base64-encoded binary data.
  * `src`: A URL that specifies the location of the image.
  * `alt`: Alternative text that describes the collection image.


Create a new smart collection with an image that will be downloaded by Shopify

Request body

smart_collection

Smart_collection resource**Smart_collection resource**

Show smart_collection properties

smart_collection.title:"Macbooks"

->[title](/docs/api/admin-graphql/latest/input-objects/CollectionInput#fields-title)

The name of the smart collection. Maximum length: 255 characters.

smart_collection.rules:[{"column":"vendor","relation":"equals","condition":"Apple"}]

->[ruleSet](/docs/api/admin-graphql/latest/input-objects/CollectionInput#fields-ruleSet)

The list of rules that define what products go into the smart collection. Each rule has the following properties:

Show rules properties

  * **column** : The property of a product being used to populate the smart collection.

Valid values for text relations:

    * `title`: The product title.
    * `type`: The product type.
    * `vendor`: The name of the product vendor.
    * `variant_title`: The title of a product variant.

Valid values for number relations:

    * `variant_compare_at_price`: The compare price.
    * `variant_weight`: The weight of the product.
    * `variant_inventory`: The inventory stock. Note: `not_equals` does not work with this property.
    * `variant_price`: product price.

Valid values for an `equals` relation:

    * `tag`: A tag associated with the product.

Valid values for metafield definition relations:

    * `product_metafield_definition`: When the metafield definition rule is powered by a product metafield definition.
    * `variant_metafield_definition`: When the metafield definition rule is powered by a variant metafield definition.
  * **relation** : The relationship between the **column** choice, and the **condition**.

Valid values for number relations:

    * `greater_than` The column value is greater than the condition.
    * `less_than` The column value is less than the condition.
    * `equals` The column value is equal to the condition.
    * `not_equals` The column value is not equal to the condition.

Valid values for text relations:

    * `equals`: Checks if the **column** value is equal to the **condition** value.
    * `not_equals`: Checks if the **column** value is not equal to the **condition** value.
    * `starts_with`: Checks if the **column** value starts with the **condition** value.
    * `ends_with`: Checks if the **column** value ends with the **condition** value.
    * `contains`: Checks if the **column** value contains the **condition** value.
    * `not_contains`: Checks if the **column** value does not contain the **condition** value.

Valid values for metafield relations are based on the corresponding metafield definition type. The following definition types support the listed relations

    * `rating`: `equals`, `greater_than`, `less_than`
    * `boolean`: `equals`
    * `number_integer`: `equals`, `greater_than`, `less_than`
    * `number_decimal`: `equals`, `greater_than`, `less_than`
    * `single_line_text_field`: `equals`
    * `list.single_line_text_field`: `equals`
  * **condition** : Select products for a smart collection using a condition. Values are either strings or numbers, depending on the **relation** value.

  * **condition_object_id** : The object id that points to additional attributes for the collection rule. This is only required when using metafield definition rules.


smart_collection.image:{"src":"http://example.com/rails_logo.gif","alt":"Rails Logo"}

->[image](/docs/api/admin-graphql/latest/input-objects/CollectionInput#fields-image)

The image associated with the smart collection. Valid values:

Show image properties

  * `attachment`: An image attached to a smart collection returned as Base64-encoded binary data.
  * `src`: A URL that specifies the location of the image.
  * `alt`: Alternative text that describes the collection image.


Create a new unpublished smart collection

Request body

smart_collection

Smart_collection resource**Smart_collection resource**

Show smart_collection properties

smart_collection.title:"Macbooks"

->[title](/docs/api/admin-graphql/latest/input-objects/CollectionInput#fields-title)

The name of the smart collection. Maximum length: 255 characters.

smart_collection.rules:[{"column":"vendor","relation":"equals","condition":"Apple"}]

->[ruleSet](/docs/api/admin-graphql/latest/input-objects/CollectionInput#fields-ruleSet)

The list of rules that define what products go into the smart collection. Each rule has the following properties:

Show rules properties

  * **column** : The property of a product being used to populate the smart collection.

Valid values for text relations:

    * `title`: The product title.
    * `type`: The product type.
    * `vendor`: The name of the product vendor.
    * `variant_title`: The title of a product variant.

Valid values for number relations:

    * `variant_compare_at_price`: The compare price.
    * `variant_weight`: The weight of the product.
    * `variant_inventory`: The inventory stock. Note: `not_equals` does not work with this property.
    * `variant_price`: product price.

Valid values for an `equals` relation:

    * `tag`: A tag associated with the product.

Valid values for metafield definition relations:

    * `product_metafield_definition`: When the metafield definition rule is powered by a product metafield definition.
    * `variant_metafield_definition`: When the metafield definition rule is powered by a variant metafield definition.
  * **relation** : The relationship between the **column** choice, and the **condition**.

Valid values for number relations:

    * `greater_than` The column value is greater than the condition.
    * `less_than` The column value is less than the condition.
    * `equals` The column value is equal to the condition.
    * `not_equals` The column value is not equal to the condition.

Valid values for text relations:

    * `equals`: Checks if the **column** value is equal to the **condition** value.
    * `not_equals`: Checks if the **column** value is not equal to the **condition** value.
    * `starts_with`: Checks if the **column** value starts with the **condition** value.
    * `ends_with`: Checks if the **column** value ends with the **condition** value.
    * `contains`: Checks if the **column** value contains the **condition** value.
    * `not_contains`: Checks if the **column** value does not contain the **condition** value.

Valid values for metafield relations are based on the corresponding metafield definition type. The following definition types support the listed relations

    * `rating`: `equals`, `greater_than`, `less_than`
    * `boolean`: `equals`
    * `number_integer`: `equals`, `greater_than`, `less_than`
    * `number_decimal`: `equals`, `greater_than`, `less_than`
    * `single_line_text_field`: `equals`
    * `list.single_line_text_field`: `equals`
  * **condition** : Select products for a smart collection using a condition. Values are either strings or numbers, depending on the **relation** value.

  * **condition_object_id** : The object id that points to additional attributes for the collection rule. This is only required when using metafield definition rules.


Create a smart collection of all products starting with the specified term

Request body

smart_collection

Smart_collection resource**Smart_collection resource**

Show smart_collection properties

smart_collection.title:"IPods"

->[title](/docs/api/admin-graphql/latest/input-objects/CollectionInput#fields-title)

The name of the smart collection. Maximum length: 255 characters.

smart_collection.rules:[{"column":"title","relation":"starts_with","condition":"iPod"}]

->[ruleSet](/docs/api/admin-graphql/latest/input-objects/CollectionInput#fields-ruleSet)

The list of rules that define what products go into the smart collection. Each rule has the following properties:

Show rules properties

  * **column** : The property of a product being used to populate the smart collection.

Valid values for text relations:

    * `title`: The product title.
    * `type`: The product type.
    * `vendor`: The name of the product vendor.
    * `variant_title`: The title of a product variant.

Valid values for number relations:

    * `variant_compare_at_price`: The compare price.
    * `variant_weight`: The weight of the product.
    * `variant_inventory`: The inventory stock. Note: `not_equals` does not work with this property.
    * `variant_price`: product price.

Valid values for an `equals` relation:

    * `tag`: A tag associated with the product.

Valid values for metafield definition relations:

    * `product_metafield_definition`: When the metafield definition rule is powered by a product metafield definition.
    * `variant_metafield_definition`: When the metafield definition rule is powered by a variant metafield definition.
  * **relation** : The relationship between the **column** choice, and the **condition**.

Valid values for number relations:

    * `greater_than` The column value is greater than the condition.
    * `less_than` The column value is less than the condition.
    * `equals` The column value is equal to the condition.
    * `not_equals` The column value is not equal to the condition.

Valid values for text relations:

    * `equals`: Checks if the **column** value is equal to the **condition** value.
    * `not_equals`: Checks if the **column** value is not equal to the **condition** value.
    * `starts_with`: Checks if the **column** value starts with the **condition** value.
    * `ends_with`: Checks if the **column** value ends with the **condition** value.
    * `contains`: Checks if the **column** value contains the **condition** value.
    * `not_contains`: Checks if the **column** value does not contain the **condition** value.

Valid values for metafield relations are based on the corresponding metafield definition type. The following definition types support the listed relations

    * `rating`: `equals`, `greater_than`, `less_than`
    * `boolean`: `equals`
    * `number_integer`: `equals`, `greater_than`, `less_than`
    * `number_decimal`: `equals`, `greater_than`, `less_than`
    * `single_line_text_field`: `equals`
    * `list.single_line_text_field`: `equals`
  * **condition** : Select products for a smart collection using a condition. Values are either strings or numbers, depending on the **relation** value.

  * **condition_object_id** : The object id that points to additional attributes for the collection rule. This is only required when using metafield definition rules.


Create a smart collection with a specified title

Request body

smart_collection

Smart_collection resource**Smart_collection resource**

Show smart_collection properties

smart_collection.title:"Macbooks"

->[title](/docs/api/admin-graphql/latest/input-objects/CollectionInput#fields-title)

The name of the smart collection. Maximum length: 255 characters.

smart_collection.rules:[{"column":"vendor","relation":"equals","condition":"Apple"}]

->[ruleSet](/docs/api/admin-graphql/latest/input-objects/CollectionInput#fields-ruleSet)

The list of rules that define what products go into the smart collection. Each rule has the following properties:

Show rules properties

  * **column** : The property of a product being used to populate the smart collection.

Valid values for text relations:

    * `title`: The product title.
    * `type`: The product type.
    * `vendor`: The name of the product vendor.
    * `variant_title`: The title of a product variant.

Valid values for number relations:

    * `variant_compare_at_price`: The compare price.
    * `variant_weight`: The weight of the product.
    * `variant_inventory`: The inventory stock. Note: `not_equals` does not work with this property.
    * `variant_price`: product price.

Valid values for an `equals` relation:

    * `tag`: A tag associated with the product.

Valid values for metafield definition relations:

    * `product_metafield_definition`: When the metafield definition rule is powered by a product metafield definition.
    * `variant_metafield_definition`: When the metafield definition rule is powered by a variant metafield definition.
  * **relation** : The relationship between the **column** choice, and the **condition**.

Valid values for number relations:

    * `greater_than` The column value is greater than the condition.
    * `less_than` The column value is less than the condition.
    * `equals` The column value is equal to the condition.
    * `not_equals` The column value is not equal to the condition.

Valid values for text relations:

    * `equals`: Checks if the **column** value is equal to the **condition** value.
    * `not_equals`: Checks if the **column** value is not equal to the **condition** value.
    * `starts_with`: Checks if the **column** value starts with the **condition** value.
    * `ends_with`: Checks if the **column** value ends with the **condition** value.
    * `contains`: Checks if the **column** value contains the **condition** value.
    * `not_contains`: Checks if the **column** value does not contain the **condition** value.

Valid values for metafield relations are based on the corresponding metafield definition type. The following definition types support the listed relations

    * `rating`: `equals`, `greater_than`, `less_than`
    * `boolean`: `equals`
    * `number_integer`: `equals`, `greater_than`, `less_than`
    * `number_decimal`: `equals`, `greater_than`, `less_than`
    * `single_line_text_field`: `equals`
    * `list.single_line_text_field`: `equals`
  * **condition** : Select products for a smart collection using a condition. Values are either strings or numbers, depending on the **relation** value.

  * **condition_object_id** : The object id that points to additional attributes for the collection rule. This is only required when using metafield definition rules.


Creating a smart collection without a title will return an error

Request body

smart_collection

Smart_collection resource**Smart_collection resource**

Show smart_collection properties

smart_collection.rules:[{"column":"vendor","relation":"equals","condition":"Apple"}]

->[ruleSet](/docs/api/admin-graphql/latest/input-objects/CollectionInput#fields-ruleSet)

The list of rules that define what products go into the smart collection. Each rule has the following properties:

Show rules properties

  * **column** : The property of a product being used to populate the smart collection.

Valid values for text relations:

    * `title`: The product title.
    * `type`: The product type.
    * `vendor`: The name of the product vendor.
    * `variant_title`: The title of a product variant.

Valid values for number relations:

    * `variant_compare_at_price`: The compare price.
    * `variant_weight`: The weight of the product.
    * `variant_inventory`: The inventory stock. Note: `not_equals` does not work with this property.
    * `variant_price`: product price.

Valid values for an `equals` relation:

    * `tag`: A tag associated with the product.

Valid values for metafield definition relations:

    * `product_metafield_definition`: When the metafield definition rule is powered by a product metafield definition.
    * `variant_metafield_definition`: When the metafield definition rule is powered by a variant metafield definition.
  * **relation** : The relationship between the **column** choice, and the **condition**.

Valid values for number relations:

    * `greater_than` The column value is greater than the condition.
    * `less_than` The column value is less than the condition.
    * `equals` The column value is equal to the condition.
    * `not_equals` The column value is not equal to the condition.

Valid values for text relations:

    * `equals`: Checks if the **column** value is equal to the **condition** value.
    * `not_equals`: Checks if the **column** value is not equal to the **condition** value.
    * `starts_with`: Checks if the **column** value starts with the **condition** value.
    * `ends_with`: Checks if the **column** value ends with the **condition** value.
    * `contains`: Checks if the **column** value contains the **condition** value.
    * `not_contains`: Checks if the **column** value does not contain the **condition** value.

Valid values for metafield relations are based on the corresponding metafield definition type. The following definition types support the listed relations

    * `rating`: `equals`, `greater_than`, `less_than`
    * `boolean`: `equals`
    * `number_integer`: `equals`, `greater_than`, `less_than`
    * `number_decimal`: `equals`, `greater_than`, `less_than`
    * `single_line_text_field`: `equals`
    * `list.single_line_text_field`: `equals`
  * **condition** : Select products for a smart collection using a condition. Values are either strings or numbers, depending on the **relation** value.

  * **condition_object_id** : The object id that points to additional attributes for the collection rule. This is only required when using metafield definition rules.


Was this section helpful?

YesNo

post

## /admin/api/2026-01/smart_collections.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"smart_collection":{"title":"Macbooks","rules":[{"column":"vendor","relation":"equals","condition":"Apple"}],"image":{"attachment":"R0lGODlhAQABAIAAAAAAAAAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==\n","alt":"iPod"}}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections.json" \

-H "X-Shopify-Access-Token: {access_token}" \

-H "Content-Type: application/json"

{}

## Response

JSON

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

HTTP/1.1 201 Created

{

"smart_collection": {

"id": 1063001358,

"handle": "macbooks",

"title": "Macbooks",

"updated_at": "2026-01-09T17:33:55-05:00",

"body_html": null,

"published_at": "2026-01-09T17:33:53-05:00",

"sort_order": "best-selling",

"template_suffix": null,

"disjunctive": false,

"rules": [

{

"column": "vendor",

"relation": "equals",

"condition": "Apple"

}

],

"published_scope": "web",

"admin_graphql_api_id": "gid://shopify/Collection/1063001358",

"image": {

"created_at": "2026-01-09T17:33:55-05:00",

"alt": "iPod",

"width": 1,

"height": 1,

"src": "https://cdn.shopify.com/s/files/1/0005/4838/0009/collections/df3e567d6f16d040326c7a0ea29a4f41.gif?v=1767998035"

}

}

}

### examples

  * #### Create a new smart collection with a base64 encoded image

#####

        curl -d '{"smart_collection":{"title":"Macbooks","rules":[{"column":"vendor","relation":"equals","condition":"Apple"}],"image":{"attachment":"R0lGODlhAQABAIAAAAAAAAAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==\n","alt":"iPod"}}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const smart_collection = new admin.rest.resources.SmartCollection({session: session});

        smart_collection.title = "Macbooks";
        smart_collection.rules = [
          {
            "column": "vendor",
            "relation": "equals",
            "condition": "Apple"
          }
        ];
        smart_collection.image = {
          "attachment": "R0lGODlhAQABAIAAAAAAAAAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==\n",
          "alt": "iPod"
        };
        await smart_collection.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        smart_collection = ShopifyAPI::SmartCollection.new(session: test_session)
        smart_collection.title = "Macbooks"
        smart_collection.rules = [
          {
            "column" => "vendor",
            "relation" => "equals",
            "condition" => "Apple"
          }
        ]
        smart_collection.image = {
          "attachment" => "R0lGODlhAQABAIAAAAAAAAAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==\n",
          "alt" => "iPod"
        }
        smart_collection.save!

#####

        // Session is built by the OAuth process

        const smart_collection = new shopify.rest.SmartCollection({session: session});
        smart_collection.title = "Macbooks";
        smart_collection.rules = [
          {
            "column": "vendor",
            "relation": "equals",
            "condition": "Apple"
          }
        ];
        smart_collection.image = {
          "attachment": "R0lGODlhAQABAIAAAAAAAAAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==\n",
          "alt": "iPod"
        };
        await smart_collection.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"smart_collection":{"id":1063001358,"handle":"macbooks","title":"Macbooks","updated_at":"2026-01-09T17:33:55-05:00","body_html":null,"published_at":"2026-01-09T17:33:53-05:00","sort_order":"best-selling","template_suffix":null,"disjunctive":false,"rules":[{"column":"vendor","relation":"equals","condition":"Apple"}],"published_scope":"web","admin_graphql_api_id":"gid://shopify/Collection/1063001358","image":{"created_at":"2026-01-09T17:33:55-05:00","alt":"iPod","width":1,"height":1,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/collections/df3e567d6f16d040326c7a0ea29a4f41.gif?v=1767998035"}}}

  * #### Create a new smart collection with an image that will be downloaded by Shopify

#####

        curl -d '{"smart_collection":{"title":"Macbooks","rules":[{"column":"vendor","relation":"equals","condition":"Apple"}],"image":{"src":"http://example.com/rails_logo.gif","alt":"Rails Logo"}}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const smart_collection = new admin.rest.resources.SmartCollection({session: session});

        smart_collection.title = "Macbooks";
        smart_collection.rules = [
          {
            "column": "vendor",
            "relation": "equals",
            "condition": "Apple"
          }
        ];
        smart_collection.image = {
          "src": "http://example.com/rails_logo.gif",
          "alt": "Rails Logo"
        };
        await smart_collection.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        smart_collection = ShopifyAPI::SmartCollection.new(session: test_session)
        smart_collection.title = "Macbooks"
        smart_collection.rules = [
          {
            "column" => "vendor",
            "relation" => "equals",
            "condition" => "Apple"
          }
        ]
        smart_collection.image = {
          "src" => "http://example.com/rails_logo.gif",
          "alt" => "Rails Logo"
        }
        smart_collection.save!

#####

        // Session is built by the OAuth process

        const smart_collection = new shopify.rest.SmartCollection({session: session});
        smart_collection.title = "Macbooks";
        smart_collection.rules = [
          {
            "column": "vendor",
            "relation": "equals",
            "condition": "Apple"
          }
        ];
        smart_collection.image = {
          "src": "http://example.com/rails_logo.gif",
          "alt": "Rails Logo"
        };
        await smart_collection.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"smart_collection":{"id":1063001356,"handle":"macbooks","title":"Macbooks","updated_at":"2026-01-09T17:33:44-05:00","body_html":null,"published_at":"2026-01-09T17:33:39-05:00","sort_order":"best-selling","template_suffix":null,"disjunctive":false,"rules":[{"column":"vendor","relation":"equals","condition":"Apple"}],"published_scope":"web","admin_graphql_api_id":"gid://shopify/Collection/1063001356","image":{"created_at":"2026-01-09T17:33:42-05:00","alt":"Rails Logo","width":110,"height":140,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/collections/rails_logo20260109-27647-wkamq1.gif?v=1767998024"}}}

  * #### Create a new unpublished smart collection

#####

        curl -d '{"smart_collection":{"title":"Macbooks","rules":[{"column":"vendor","relation":"equals","condition":"Apple"}],"published":false}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const smart_collection = new admin.rest.resources.SmartCollection({session: session});

        smart_collection.title = "Macbooks";
        smart_collection.rules = [
          {
            "column": "vendor",
            "relation": "equals",
            "condition": "Apple"
          }
        ];
        smart_collection.published = false;
        await smart_collection.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        smart_collection = ShopifyAPI::SmartCollection.new(session: test_session)
        smart_collection.title = "Macbooks"
        smart_collection.rules = [
          {
            "column" => "vendor",
            "relation" => "equals",
            "condition" => "Apple"
          }
        ]
        smart_collection.published = false
        smart_collection.save!

#####

        // Session is built by the OAuth process

        const smart_collection = new shopify.rest.SmartCollection({session: session});
        smart_collection.title = "Macbooks";
        smart_collection.rules = [
          {
            "column": "vendor",
            "relation": "equals",
            "condition": "Apple"
          }
        ];
        smart_collection.published = false;
        await smart_collection.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"smart_collection":{"id":1063001370,"handle":"macbooks","title":"Macbooks","updated_at":"2026-01-09T17:34:26-05:00","body_html":null,"published_at":null,"sort_order":"best-selling","template_suffix":null,"disjunctive":false,"rules":[{"column":"vendor","relation":"equals","condition":"Apple"}],"published_scope":"web","admin_graphql_api_id":"gid://shopify/Collection/1063001370"}}

  * #### Create a smart collection of all products starting with the specified term

#####

        curl -d '{"smart_collection":{"title":"IPods","rules":[{"column":"title","relation":"starts_with","condition":"iPod"}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const smart_collection = new admin.rest.resources.SmartCollection({session: session});

        smart_collection.title = "IPods";
        smart_collection.rules = [
          {
            "column": "title",
            "relation": "starts_with",
            "condition": "iPod"
          }
        ];
        await smart_collection.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        smart_collection = ShopifyAPI::SmartCollection.new(session: test_session)
        smart_collection.title = "IPods"
        smart_collection.rules = [
          {
            "column" => "title",
            "relation" => "starts_with",
            "condition" => "iPod"
          }
        ]
        smart_collection.save!

#####

        // Session is built by the OAuth process

        const smart_collection = new shopify.rest.SmartCollection({session: session});
        smart_collection.title = "IPods";
        smart_collection.rules = [
          {
            "column": "title",
            "relation": "starts_with",
            "condition": "iPod"
          }
        ];
        await smart_collection.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"smart_collection":{"id":1063001366,"handle":"ipods-1","title":"IPods","updated_at":"2026-01-09T17:34:19-05:00","body_html":null,"published_at":"2026-01-09T17:34:19-05:00","sort_order":"best-selling","template_suffix":null,"disjunctive":false,"rules":[{"column":"title","relation":"starts_with","condition":"iPod"}],"published_scope":"web","admin_graphql_api_id":"gid://shopify/Collection/1063001366"}}

  * #### Create a smart collection with a specified title

#####

        curl -d '{"smart_collection":{"title":"Macbooks","rules":[{"column":"vendor","relation":"equals","condition":"Apple"}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const smart_collection = new admin.rest.resources.SmartCollection({session: session});

        smart_collection.title = "Macbooks";
        smart_collection.rules = [
          {
            "column": "vendor",
            "relation": "equals",
            "condition": "Apple"
          }
        ];
        await smart_collection.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        smart_collection = ShopifyAPI::SmartCollection.new(session: test_session)
        smart_collection.title = "Macbooks"
        smart_collection.rules = [
          {
            "column" => "vendor",
            "relation" => "equals",
            "condition" => "Apple"
          }
        ]
        smart_collection.save!

#####

        // Session is built by the OAuth process

        const smart_collection = new shopify.rest.SmartCollection({session: session});
        smart_collection.title = "Macbooks";
        smart_collection.rules = [
          {
            "column": "vendor",
            "relation": "equals",
            "condition": "Apple"
          }
        ];
        await smart_collection.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"smart_collection":{"id":1063001359,"handle":"macbooks","title":"Macbooks","updated_at":"2026-01-09T17:33:59-05:00","body_html":null,"published_at":"2026-01-09T17:33:59-05:00","sort_order":"best-selling","template_suffix":null,"disjunctive":false,"rules":[{"column":"vendor","relation":"equals","condition":"Apple"}],"published_scope":"web","admin_graphql_api_id":"gid://shopify/Collection/1063001359"}}

  * #### Creating a smart collection without a title will return an error

#####

        curl -d '{"smart_collection":{"body":"foobar","rules":[{"column":"vendor","relation":"equals","condition":"Apple"}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const smart_collection = new admin.rest.resources.SmartCollection({session: session});

        smart_collection.body = "foobar";
        smart_collection.rules = [
          {
            "column": "vendor",
            "relation": "equals",
            "condition": "Apple"
          }
        ];
        await smart_collection.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        smart_collection = ShopifyAPI::SmartCollection.new(session: test_session)
        smart_collection.body = "foobar"
        smart_collection.rules = [
          {
            "column" => "vendor",
            "relation" => "equals",
            "condition" => "Apple"
          }
        ]
        smart_collection.save!

#####

        // Session is built by the OAuth process

        const smart_collection = new shopify.rest.SmartCollection({session: session});
        smart_collection.body = "foobar";
        smart_collection.rules = [
          {
            "column": "vendor",
            "relation": "equals",
            "condition": "Apple"
          }
        ];
        await smart_collection.save({
          update: true,
        });

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":{"title":["can't be blank"]}}


* * *

##

[Anchor to GET request, Retrieves a list of smart collections](/docs/api/admin-rest/latest/resources/smartcollection#get-smart-collections?since-id=482865238)

get

Retrieves a list of smart collections

[collections](/docs/api/admin-graphql/latest/queries/collections)

Retrieves a list of smart collections. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

###

[Anchor to Parameters of Retrieves a list of smart collections](/docs/api/admin-rest/latest/resources/smartcollection#get-smart-collections?since-id=482865238-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fields

Show only certain fields, specified by a comma-separated list of field names.

* * *

handle

Filter results by smart collection handle.

* * *

ids

Show only the smart collections specified by a comma-separated list of IDs.

* * *

limit

≤ 250**≤ 250**

default 50**default 50**

The number of results to show.

* * *

product_id

Show smart collections that includes the specified product.

* * *

published_at_max

Show smart collections published before this date. (format: 2014-04-25T16:15:47-04:00)

* * *

published_at_min

Show smart collections published after this date. (format: 2014-04-25T16:15:47-04:00)

* * *

published_status

default any**default any**

Filter results based on the published status of smart collections.

Show published_status properties

  * **published** : Show only published smart collections.

  * **unpublished** : Show only unpublished smart collections.

  * **any** : Show all smart collections.


* * *

since_id

Restrict results to after the specified ID.

* * *

title

Show smart collections with the specified title.

* * *

updated_at_max

Show smart collections last updated before this date. (format: 2014-04-25T16:15:47-04:00)

* * *

updated_at_min

Show smart collections last updated after this date. (format: 2014-04-25T16:15:47-04:00)

* * *

Was this section helpful?

YesNo

###

[Anchor to get-smart-collections?since-id=482865238-examples](/docs/api/admin-rest/latest/resources/smartcollection#get-smart-collections?since-id=482865238-examples)Examples

Retrieve a list all smart collections after a specified ID

Query parameters

since_id=482865238

Restrict results to after the specified ID.

Retrieve a list of all smart collections

Retrieve a list of all smart collections for a certain product_id

Query parameters

product_id=632910392

Show smart collections that includes the specified product.

Retrieve a list of specific smart collections

Query parameters

ids=482865238,1063001362

Show only the smart collections specified by a comma-separated list of IDs.

Was this section helpful?

YesNo

get

## /admin/api/2026-01/smart_collections.json?since_id=482865238

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections.json?since_id=482865238" \

-H "X-Shopify-Access-Token: {access_token}"

{}

## Response

JSON

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

HTTP/1.1 200 OK

{

"smart_collections": [

{

"id": 1063001361,

"handle": "ipods-1",

"title": "IPods",

"updated_at": "2026-01-09T17:34:08-05:00",

"body_html": null,

"published_at": "2026-01-09T17:34:08-05:00",

"sort_order": "best-selling",

"template_suffix": null,

"disjunctive": false,

"rules": [

{

"column": "title",

"relation": "starts_with",

"condition": "iPod"

}

],

"published_scope": "web",

"admin_graphql_api_id": "gid://shopify/Collection/1063001361"

}

]

}

### examples

  * #### Retrieve a list all smart collections after a specified ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections.json?since_id=482865238" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.SmartCollection.all({
          session: session,
          since_id: "482865238",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::SmartCollection.all(
          session: test_session,
          since_id: "482865238",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.SmartCollection.all({
          session: session,
          since_id: "482865238",
        });

#### response

        HTTP/1.1 200 OK{"smart_collections":[{"id":1063001361,"handle":"ipods-1","title":"IPods","updated_at":"2026-01-09T17:34:08-05:00","body_html":null,"published_at":"2026-01-09T17:34:08-05:00","sort_order":"best-selling","template_suffix":null,"disjunctive":false,"rules":[{"column":"title","relation":"starts_with","condition":"iPod"}],"published_scope":"web","admin_graphql_api_id":"gid://shopify/Collection/1063001361"}]}

  * #### Retrieve a list of all smart collections

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.SmartCollection.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::SmartCollection.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.SmartCollection.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"smart_collections":[{"id":482865238,"handle":"smart-ipods","title":"Smart iPods","updated_at":"2008-02-01T19:00:00-05:00","body_html":"<p>The best selling ipod ever</p>","published_at":"2008-02-01T19:00:00-05:00","sort_order":"manual","template_suffix":null,"disjunctive":false,"rules":[{"column":"type","relation":"equals","condition":"Cult Products"}],"published_scope":"web","admin_graphql_api_id":"gid://shopify/Collection/482865238","image":{"created_at":"2026-01-09T17:04:11-05:00","alt":"MP3 Player 8gb","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/collections/ipod_nano_8gb.jpg?v=1767996251"}}]}

  * #### Retrieve a list of all smart collections for a certain product_id

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections.json?product_id=632910392" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.SmartCollection.all({
          session: session,
          product_id: "632910392",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::SmartCollection.all(
          session: test_session,
          product_id: "632910392",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.SmartCollection.all({
          session: session,
          product_id: "632910392",
        });

#### response

        HTTP/1.1 200 OK{"smart_collections":[{"id":482865238,"handle":"smart-ipods","title":"Smart iPods","updated_at":"2008-02-01T19:00:00-05:00","body_html":"<p>The best selling ipod ever</p>","published_at":"2008-02-01T19:00:00-05:00","sort_order":"manual","template_suffix":null,"disjunctive":false,"rules":[{"column":"type","relation":"equals","condition":"Cult Products"}],"published_scope":"web","admin_graphql_api_id":"gid://shopify/Collection/482865238","image":{"created_at":"2026-01-09T17:04:11-05:00","alt":"MP3 Player 8gb","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/collections/ipod_nano_8gb.jpg?v=1767996251"}}]}

  * #### Retrieve a list of specific smart collections

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections.json?ids=482865238%2C1063001362" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.SmartCollection.all({
          session: session,
          ids: "482865238,1063001362",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::SmartCollection.all(
          session: test_session,
          ids: "482865238,1063001362",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.SmartCollection.all({
          session: session,
          ids: "482865238,1063001362",
        });

#### response

        HTTP/1.1 200 OK{"smart_collections":[{"id":1063001362,"handle":"macbooks","title":"Macbooks","updated_at":"2026-01-09T17:34:11-05:00","body_html":null,"published_at":"2026-01-09T17:34:11-05:00","sort_order":"best-selling","template_suffix":null,"disjunctive":false,"rules":[{"column":"vendor","relation":"equals","condition":"Apple"}],"published_scope":"web","admin_graphql_api_id":"gid://shopify/Collection/1063001362"},{"id":482865238,"handle":"smart-ipods","title":"Smart iPods","updated_at":"2008-02-01T19:00:00-05:00","body_html":"<p>The best selling ipod ever</p>","published_at":"2008-02-01T19:00:00-05:00","sort_order":"manual","template_suffix":null,"disjunctive":false,"rules":[{"column":"type","relation":"equals","condition":"Cult Products"}],"published_scope":"web","admin_graphql_api_id":"gid://shopify/Collection/482865238","image":{"created_at":"2026-01-09T17:04:11-05:00","alt":"MP3 Player 8gb","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/collections/ipod_nano_8gb.jpg?v=1767996251"}}]}


* * *

##

[Anchor to GET request, Retrieves a single smart collection](/docs/api/admin-rest/latest/resources/smartcollection#get-smart-collections-smart-collection-id)

get

Retrieves a single smart collection

[collection](/docs/api/admin-graphql/latest/queries/collection)

Retrieves a single smart collection

###

[Anchor to Parameters of Retrieves a single smart collection](/docs/api/admin-rest/latest/resources/smartcollection#get-smart-collections-smart-collection-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

smart_collection_id

string**string**

required**required**

* * *

fields

Show only certain fields, specified by a comma-separated list of field names.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-smart-collections-smart-collection-id-examples](/docs/api/admin-rest/latest/resources/smartcollection#get-smart-collections-smart-collection-id-examples)Examples

Retrieve a specific collection by ID

Path parameters

smart_collection_id=482865238

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/smart_collections/482865238.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections/482865238.json" \

-H "X-Shopify-Access-Token: {access_token}"

{}

## Response

JSON

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

HTTP/1.1 200 OK

{

"smart_collection": {

"id": 482865238,

"handle": "smart-ipods",

"title": "Smart iPods",

"updated_at": "2008-02-01T19:00:00-05:00",

"body_html": "<p>The best selling ipod ever</p>",

"published_at": "2008-02-01T19:00:00-05:00",

"sort_order": "manual",

"template_suffix": null,

"products_count": 2,

"disjunctive": false,

"rules": [

{

"column": "type",

"relation": "equals",

"condition": "Cult Products"

}

],

"published_scope": "web",

"admin_graphql_api_id": "gid://shopify/Collection/482865238",

"image": {

"created_at": "2026-01-09T17:04:11-05:00",

"alt": "MP3 Player 8gb",

"width": 123,

"height": 456,

"src": "https://cdn.shopify.com/s/files/1/0005/4838/0009/collections/ipod_nano_8gb.jpg?v=1767996251"

}

}

}

### examples

  * #### Retrieve a specific collection by ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections/482865238.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.SmartCollection.find({
          session: session,
          id: 482865238,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::SmartCollection.find(
          session: test_session,
          id: 482865238,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.SmartCollection.find({
          session: session,
          id: 482865238,
        });

#### response

        HTTP/1.1 200 OK{"smart_collection":{"id":482865238,"handle":"smart-ipods","title":"Smart iPods","updated_at":"2008-02-01T19:00:00-05:00","body_html":"<p>The best selling ipod ever</p>","published_at":"2008-02-01T19:00:00-05:00","sort_order":"manual","template_suffix":null,"products_count":2,"disjunctive":false,"rules":[{"column":"type","relation":"equals","condition":"Cult Products"}],"published_scope":"web","admin_graphql_api_id":"gid://shopify/Collection/482865238","image":{"created_at":"2026-01-09T17:04:11-05:00","alt":"MP3 Player 8gb","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/collections/ipod_nano_8gb.jpg?v=1767996251"}}}


* * *

##

[Anchor to GET request, Retrieves a count of smart collections](/docs/api/admin-rest/latest/resources/smartcollection#get-smart-collections-count)

get

Retrieves a count of smart collections

[collectionsCount](/docs/api/admin-graphql/latest/queries/collectionsCount?example=retrieves-a-count-of-smart-collections)

Retrieves a count of smart collections

###

[Anchor to Parameters of Retrieves a count of smart collections](/docs/api/admin-rest/latest/resources/smartcollection#get-smart-collections-count-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

product_id

Show smart collections that include the specified product.

* * *

published_at_max

Show smart collections published before this date. (format: 2014-04-25T16:15:47-04:00)

* * *

published_at_min

Show smart collections published after this date. (format: 2014-04-25T16:15:47-04:00)

* * *

published_status

default any**default any**

Filter results based on the published status of smart collections.

Show published_status properties

  * **published** : Show only published smart collections.

  * **unpublished** : Show only unpublished smart collections.

  * **any** : Show all smart collections.


* * *

title

Show smart collections with the specified title.

* * *

updated_at_max

Show smart collections last updated before this date. (format: 2014-04-25T16:15:47-04:00)

* * *

updated_at_min

Show smart collections last updated after this date. (format: 2014-04-25T16:15:47-04:00)

* * *

Was this section helpful?

YesNo

###

[Anchor to get-smart-collections-count-examples](/docs/api/admin-rest/latest/resources/smartcollection#get-smart-collections-count-examples)Examples

Retrieve a count of all smart collections

Retrieve a count of all smart collections for a certain product_id

Query parameters

product_id=632910392

Show smart collections that include the specified product.

Was this section helpful?

YesNo

get

## /admin/api/2026-01/smart_collections/count.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections/count.json" \

-H "X-Shopify-Access-Token: {access_token}"

{}

## Response

JSON

9

1

2

3

4

HTTP/1.1 200 OK

{

"count": 1

}

### examples

  * #### Retrieve a count of all smart collections

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.SmartCollection.count({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::SmartCollection.count(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.SmartCollection.count({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"count":1}

  * #### Retrieve a count of all smart collections for a certain product_id

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections/count.json?product_id=632910392" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.SmartCollection.count({
          session: session,
          product_id: "632910392",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::SmartCollection.count(
          session: test_session,
          product_id: "632910392",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.SmartCollection.count({
          session: session,
          product_id: "632910392",
        });

#### response

        HTTP/1.1 200 OK{"count":1}


* * *

##

[Anchor to PUT request, Updates an existing smart collection](/docs/api/admin-rest/latest/resources/smartcollection#put-smart-collections-smart-collection-id)

put

Updates an existing smart collection

[collectionUpdate](/docs/api/admin-graphql/latest/mutations/collectionUpdate?example=updates-an-existing-smart-collection)

Updates an existing smart collection

###

[Anchor to Parameters of Updates an existing smart collection](/docs/api/admin-rest/latest/resources/smartcollection#put-smart-collections-smart-collection-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

smart_collection_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to put-smart-collections-smart-collection-id-examples](/docs/api/admin-rest/latest/resources/smartcollection#put-smart-collections-smart-collection-id-examples)Examples

Hide a published smart collection

Path parameters

smart_collection_id=482865238

string**string**

required**required**

Request body

smart_collection

Smart_collection resource**Smart_collection resource**

Show smart_collection properties

smart_collection.id:482865238

The ID of the smart collection.

Publish a hidden collection

Path parameters

smart_collection_id=482865238

string**string**

required**required**

Request body

smart_collection

Smart_collection resource**Smart_collection resource**

Show smart_collection properties

smart_collection.id:482865238

The ID of the smart collection.

Update a smart collection by clearing the collection image

Path parameters

smart_collection_id=482865238

string**string**

required**required**

Request body

smart_collection

Smart_collection resource**Smart_collection resource**

Show smart_collection properties

smart_collection.id:482865238

The ID of the smart collection.

smart_collection.image:""

->[image](/docs/api/admin-graphql/latest/input-objects/CollectionInput#fields-image)

The image associated with the smart collection. Valid values:

Show image properties

  * `attachment`: An image attached to a smart collection returned as Base64-encoded binary data.
  * `src`: A URL that specifies the location of the image.
  * `alt`: Alternative text that describes the collection image.


smart_collection.updated_at:"2026-01-09T17:33:49-05:00"

read-only**read-only**

The date and time ([ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601)) when the smart collection was last modified.

smart_collection.handle:"smart-ipods"

->[handle](/docs/api/admin-graphql/latest/input-objects/CollectionInput#fields-handle)

A human-friendly unique string for the smart collection. Automatically generated from the `title`. Used in shop themes by the Liquid templating language to refer to the smart collection. (maximum: 255 characters)

smart_collection.title:"Smart iPods"

->[title](/docs/api/admin-graphql/latest/input-objects/CollectionInput#fields-title)

The name of the smart collection. Maximum length: 255 characters.

smart_collection.body_html:"<p>The best selling ipod ever</p>"

->[descriptionHtml](/docs/api/admin-graphql/latest/input-objects/CollectionInput#fields-descriptionHtml)

The description of the smart collection. Includes HTML markup. Many shop themes display this on the smart collection page.

smart_collection.published_at:"2008-02-01T19:00:00-05:00"

The date and time ([ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601)) that the smart collection was published. Returns `null` when the collection is hidden.

smart_collection.sort_order:"manual"

->[sortOrder](/docs/api/admin-graphql/latest/input-objects/CollectionInput#fields-sortOrder)

The order of the products in the smart collection. Valid values:

Show sort_order properties

  * `alpha-asc`: The products are sorted alphabetically from A to Z.
  * `alpha-des`: The products are sorted alphabetically from Z to A.
  * `best-selling`: The products are sorted by number of sales.
  * `created`: The products are sorted by the date they were created, from oldest to newest.
  * `created-desc`: The products are sorted by the date they were created, from newest to oldest.
  * `manual`: The products are manually sorted by the shop owner.
  * `price-asc`: The products are sorted by price from lowest to highest.
  * `price-desc`: The products are sorted by price from highest to lowest.


smart_collection.template_suffix:null

->[templateSuffix](/docs/api/admin-graphql/latest/input-objects/CollectionInput#fields-templateSuffix)

The suffix of the Liquid template that the shop uses. By default, the original template is called product.liquid, and additional templates are called product.`suffix`.liquid.

smart_collection.disjunctive:false

->[appliedDisjunctively](/docs/api/admin-graphql/latest/input-objects/CollectionRuleSetInput#fields-appliedDisjunctively)

Whether the product must match all the rules to be included in the smart collection. Valid values:

Show disjunctive properties

  * `true`: Products only need to match one or more of the rules to be included in the smart collection.
  * `false`: Products must match all of the rules to be included in the smart collection.


smart_collection.rules:[{"column":"type","relation":"equals","condition":"Cult Products"}]

->[ruleSet](/docs/api/admin-graphql/latest/input-objects/CollectionInput#fields-ruleSet)

The list of rules that define what products go into the smart collection. Each rule has the following properties:

Show rules properties

  * **column** : The property of a product being used to populate the smart collection.

Valid values for text relations:

    * `title`: The product title.
    * `type`: The product type.
    * `vendor`: The name of the product vendor.
    * `variant_title`: The title of a product variant.

Valid values for number relations:

    * `variant_compare_at_price`: The compare price.
    * `variant_weight`: The weight of the product.
    * `variant_inventory`: The inventory stock. Note: `not_equals` does not work with this property.
    * `variant_price`: product price.

Valid values for an `equals` relation:

    * `tag`: A tag associated with the product.

Valid values for metafield definition relations:

    * `product_metafield_definition`: When the metafield definition rule is powered by a product metafield definition.
    * `variant_metafield_definition`: When the metafield definition rule is powered by a variant metafield definition.
  * **relation** : The relationship between the **column** choice, and the **condition**.

Valid values for number relations:

    * `greater_than` The column value is greater than the condition.
    * `less_than` The column value is less than the condition.
    * `equals` The column value is equal to the condition.
    * `not_equals` The column value is not equal to the condition.

Valid values for text relations:

    * `equals`: Checks if the **column** value is equal to the **condition** value.
    * `not_equals`: Checks if the **column** value is not equal to the **condition** value.
    * `starts_with`: Checks if the **column** value starts with the **condition** value.
    * `ends_with`: Checks if the **column** value ends with the **condition** value.
    * `contains`: Checks if the **column** value contains the **condition** value.
    * `not_contains`: Checks if the **column** value does not contain the **condition** value.

Valid values for metafield relations are based on the corresponding metafield definition type. The following definition types support the listed relations

    * `rating`: `equals`, `greater_than`, `less_than`
    * `boolean`: `equals`
    * `number_integer`: `equals`, `greater_than`, `less_than`
    * `number_decimal`: `equals`, `greater_than`, `less_than`
    * `single_line_text_field`: `equals`
    * `list.single_line_text_field`: `equals`
  * **condition** : Select products for a smart collection using a condition. Values are either strings or numbers, depending on the **relation** value.

  * **condition_object_id** : The object id that points to additional attributes for the collection rule. This is only required when using metafield definition rules.


smart_collection.published_scope:"web"

Whether the smart collection is published to the Point of Sale channel. Valid values:

Show published_scope properties

  * `web`: The smart collection is published to the Online Store channel but not published to the Point of Sale channel.
  * `global`: The smart collection is published to both the Online Store channel and the Point of Sale channel.


Update a smart collection by setting a new collection image

Path parameters

smart_collection_id=482865238

string**string**

required**required**

Request body

smart_collection

Smart_collection resource**Smart_collection resource**

Show smart_collection properties

smart_collection.id:482865238

The ID of the smart collection.

smart_collection.image:{"attachment":"R0lGODlhbgCMAPf/APbr48VySrxTO7IgKt2qmKQdJeK8lsFjROG5p/nz7Zg3\nMNmnd7Q1MLNVS9GId71hSJMZIuzTu4UtKbeEeakhKMl8U8WYjfr18YQaIbAf\nKKwhKdKzqpQtLebFortOOejKrOjZ1Mt7aMNpVbAqLLV7bsNqR+3WwMqEWenN\nsZYxL/Ddy/Pm2e7ZxLlUQrIjNPXp3bU5MbhENbEtLtqhj5ZQTfHh0bMxL7Ip\nNsNyUYkZIrZJPcqGdYIUHb5aPKkeJnoUHd2yiJkiLKYiKLRFOsyJXKVDO8up\nosFaS+TBnK4kKti5sNaYg/z49aqYl5kqLrljUtORfMOlo/36+H4ZH8yDYq0f\nKKFYTaU9MrY8MrZBNXwXHpgaIdGVYu/byLZNP9SaZLIyOuXCtHkpJst+Wpcm\nLMyCa8BfP9GMb9KQdPDd1PPk1sd5VP79/L5dQZ0bI9+ymqssK9WcfIoXHdzG\nxdWWfteib79lSr1YP86MYurQxKdcUKdMQr5ZSfPs6YEZH8uhl4oWIenMuurQ\nttmejaqoqsqBVaAcJLlJN5kvMLlZRMNsSL5fRak0LbdQQMVvSPjw6cJnRpkf\nKtmjhvfu5cJtT7IuOMVvWLY/M/37+o0YH9ibhtSYdObErc6HarM9NnYSGNGR\navLi09unje3WyeO8rsVrT7tdRtK3uffu6NWeaL9pTJIjJrM4NPbx8cdyX7M7\nPYYVHu7j4KgoNJAYIKtkV5o9MsOcldicis+RYNutfrhFOZ0hJbqinZ8bI8h5\nUObFuOfItJsfJrJfUOfIqc+PXqQtK8RnSbA4Mcd3Tm0SGbpXQ8aqp7RLNs+s\novHfzpVhV9iggMd1TLtbRKUdKXEQFsd4XrZRPLIgMZUeJ+jKvrAlK6AhJ65A\nMpMpKuC3j5obIsRwS7hAN8l/YtvDvnYXHbAoLI47SIUsOMenorF4gO/m4+fH\npo4vLZ8oKMukqp0cJbhVSMV2UuPR0bAfMLIrLrg/OcJwT8h+Vt+wn8eurLlh\nQrIfKHQOHHQOHf///////yH5BAEAAP8ALAAAAABuAIwAAAj/AP8JHDhQXjpz\n/PopXNiPn0OHDRMmbKhQIsOJFS1SxAhxI8SHFzVeDBnx48iNBAeeOkcxokeX\nFRdOnAlSokaaLXNujJkxo8iYHRkKtWkzZSsaOXkAWsoUECynsHgoqEW1qtVa\n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\nGg4lOnRGDKRZsoS7pMPSA6YXNWLsKJLkSZOVwKhMGSTTrJf9ZNKcomXKTrQY\nevr02cSIvKJxi6aJkaVuXaZMs1ziO5UqPawnuXK9AWEW2Jhja9pMuzMd27YW\nLNga10fuZYUPkdZdqpTv575YbJQbkCHw1sEpb9wQMstwWLFkbfppjJPc/wTI\nhHhJ5r0BBGbMRzfb7ez5MwwbpTMsx5pa9eob2CBM5yETpmzGtTE8hrybN29b\nc1oBn6trc9K7nhmUy6BcOUrn0KHLcr0FQvWYMxdnb3w7t/fvwFMiFvKG0uw8\n4kRLYjkGG0RtMPlWc+GGdyCwbwtYrOsHu7K0a+K/AEO04K0CF8InBvPOg2GE\nKpZTrsHSUotwwgnnmW4LHGGBKbb9bMqhsSly082CW0QMkDLLSvQHFQFiOESX\nLGzQpkUY22swA8Lko9EFLqfBEcdvMhRrwx610OLHtJ5Rc01ahHnCzTeFkXNO\nOfWQkwQ6NNFzTz2X0GQJQAMVdJEYsBhBAyrbK/9tgBcbrCTCG7bkkstvvvwm\nzPzI7JEcNLXDCYICQhXVkAIMMdWQd0x1Y9VdiuHGA1hjhfWQQzyg9dZDYmBg\nyioSVfRKFwfYZ8ZIJ3XhGhe83OLSSwEZU78ea+pUO2wK8MFaUUMl9dReDOll\n1VXbuYIZWWOl1dZDLpGhV3YZXLTR9vZhUMJijUX2mmveYRZcQDLlsCZOp21s\nCx+uLTjbbE/11ttv3diFkSHKRReGcthtN1hgrdxH2Awk5fJefK+ZZ9lvVvXW\n2cT+ZSwHgdHCpmCYDb4WYVNL7baXbsN9FdYYbKDA4otddBdYeffZx9iPjw35\nmmlKNtnUfmXSNNqAW9b/6eWYY8YWYW0V7tYQhxWAwwege61y6OXkbdDoSUFe\nWuR3wP3akKhjUtlHlqklG+YqsjaY620VNgQDMcQQouwrX3zR6KKFZfttyKtw\n+utQnRUL2mjLYjnvtLDpu9e9/ZYZ8FK3maLwwn8OmlF3lWNc7df3gfzteaZZ\n+NTKx5y6RxJ69/333mvBwHOLQ/fhiR2SV34HS47hmnAafJ9gh3AaDMcB7LE/\nIoPY441dhOzDz94VN3DPNmoeM5drAyfK7lWH34baYetVCidBIT6C5UMhB4r2\nn3FheSANRVGCwhBmObtlbgqXyYYNyuYFAMQFCtPwQf3spxAraGBRR+Af91wX\n/zsPoCIuCCAV13yAMsWo7zIOaJHFSHEZHZABdWK4X0JoIAENLIeDCXFA2rgX\nuwG8MC6kKGGoZuaDTEhtd/vBTBoyYLYqeAEzFpihGCagEBqIQQJVGMAOEdLD\n2L0uHJdBAMIOhsTELHExwLnS/i6zAQlIQItWxKIccejGL/4wjPvw4kHSQApA\nBhKQUDCiEWE2C93dTSEW2EMjaWABhbgnA3g8SAj4cElK+kMJWoyjBK6YECtw\nUgKZ7N8ejdZHfzjgGgNY5SpnZsisJXFHikwICTLBskzUECFtxJ/FFKKETmrx\nkwixQiclYAX+mfKUCpnBEZzpzHpkS2Yxm0ViMNcjhf+QABs5uKUuD9KoTOaP\nQb80picxaExk8lCZfIxLNuBhrWnurZpjoiVCbAkBbnrTH2pbTjgZVAVyGnOY\nBylmJ9P5xXWOUS6WEB3ZqgmTazLxMk40WntQub3lbIOc7OjkQP1RUI4e9CCl\nfJ3jjCbEogDAE6KrAiKlVs+4gJF7GUDlDLLnUWCyg6Ps8GgxdyrSVK5zH/WI\noARjZjFEQhSmRCEFg9SGSqIoQadT7alOJcAOoJJUmeFA6VBIETqk+ssPKizK\nDorxwx9CdShSvapOqzpVoO7ApMocgAdcIb74HeSroEOqEn8w1mgVRR0KyEEw\nKqoctTZEquzggFsVooepskP/DwqZAAfmakpGvc4HXSXF54CWVLthALASRYhB\nFpmDd4QxsQxRQmNd61HITnWyCVHC9MTnCsY9U7dH4AM8spGQvVrsiRB4Fg/8\ncFxsJmQDHvUHLQyhWsy01rXs2MFj2ZGC6862KKRgHGY6K9zlEPdyP8AJcteo\n3ClsQCHq0AF0QdkN+HbjlxygL31hO13tMrW7lwkB0BiUoR3x4EfmrYlCNjAF\nCRAoIWmwQexQqQcyxHe+9eXAfVOQAg7k16v7jQsAHGi2Bv0gUzyQQ05Ga+Cy\n0MBEDsZgN8gQ4QnXt7oJ0QOGOZACDTeEu0aTCwC80EKhDcAHMDGHWATMsuMC\nFsVl/9GnP0Jg0kw24MUv/qUTOGDlCj8WETfGsVx2vI+UzsATIFZUaTIRk3QY\n+ZYlFq0Ce5QJHBXgdU+MRCSwEYlVBCHPQZhyn7vhhD9fWdAc2DKhKXxhRCc6\n0Yi4LOPcl6hGVUFqc4gJLGaxufKO1s2VkrOj63znOkciCKMedZ+n7ARUp1rQ\niLAyIlyNYURcONaInrWs9ci4JyJOaFYawDzP8Q+ZwAICLckbgd08i290eh9V\nCIadQw3qO5Oa1H1GNRlSjeorO2HLruZ2rLudAm+Dm9Gxcx/GXmSIMbnjH5W2\nzy2RbOzM+cENBRAWs0N9b3zXWdp8pra1r61tbXdb4N/2Nv8i5gzeIJd5Gjui\nwT+AzQ9YVGrYnNO0Agm27GBkvNnNzje+921qf/+b1QEfuMDFPe5lk/lspUG3\nWKbQCofLBBBuwNEs3C3aikcrB2TTeM81HgmOd3zf/PZ3yFPNaqSXfODF0EDK\nE9e6liZmCvJwOLD7AQhU2efSbG6zm7VgiG1ofBc+//nGgZ7vbYw67aVux4v/\nfXSSK53by/HVrzIwDZTBBANUrzpMeAAIWASeB4P/AQ9+cHjEJx7xWgDE5nLQ\neMdHXvKbg/zkMZ23H/1oFRjYPOc9v3nQ58Aw0xn9LACvO7HQAOZVf/jl0ii1\nHcXe9bPX3euftaPL5R71tIf97nsy7/o0WlP2r4/JOU7B+r5nqva7jz1EdZ97\n4qNe+bonfvCfVXvly1762beOOdLBd+Q7PCAAOw==\n","alt":"Rails logo"}

->[image](/docs/api/admin-graphql/latest/input-objects/CollectionInput#fields-image)

The image associated with the smart collection. Valid values:

Show image properties

  * `attachment`: An image attached to a smart collection returned as Base64-encoded binary data.
  * `src`: A URL that specifies the location of the image.
  * `alt`: Alternative text that describes the collection image.


Update a smart collection by setting a new collection image alternative text

Path parameters

smart_collection_id=482865238

string**string**

required**required**

Request body

smart_collection

Smart_collection resource**Smart_collection resource**

Show smart_collection properties

smart_collection.id:482865238

The ID of the smart collection.

smart_collection.image:{"alt":"Rails logo"}

->[image](/docs/api/admin-graphql/latest/input-objects/CollectionInput#fields-image)

The image associated with the smart collection. Valid values:

Show image properties

  * `attachment`: An image attached to a smart collection returned as Base64-encoded binary data.
  * `src`: A URL that specifies the location of the image.
  * `alt`: Alternative text that describes the collection image.


Update the description of a smart collection

Path parameters

smart_collection_id=482865238

string**string**

required**required**

Request body

smart_collection

Smart_collection resource**Smart_collection resource**

Show smart_collection properties

smart_collection.id:482865238

The ID of the smart collection.

smart_collection.body_html:"<p>5000 songs in your pocket</p>"

->[descriptionHtml](/docs/api/admin-graphql/latest/input-objects/CollectionInput#fields-descriptionHtml)

The description of the smart collection. Includes HTML markup. Many shop themes display this on the smart collection page.

Was this section helpful?

YesNo

put

## /admin/api/2026-01/smart_collections/482865238.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"smart_collection":{"id":482865238,"published":false}}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections/482865238.json" \

-H "X-Shopify-Access-Token: {access_token}" \

-H "Content-Type: application/json"

{}

## Response

JSON

99

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

HTTP/1.1 200 OK

{

"smart_collection": {

"title": "Smart iPods",

"handle": "smart-ipods",

"body_html": "<p>The best selling ipod ever</p>",

"id": 482865238,

"published_at": null,

"updated_at": "2026-01-09T17:34:00-05:00",

"sort_order": "manual",

"template_suffix": null,

"disjunctive": false,

"rules": [

{

"column": "type",

"relation": "equals",

"condition": "Cult Products"

}

],

"published_scope": "web",

"admin_graphql_api_id": "gid://shopify/Collection/482865238",

"image": {

"created_at": "2026-01-09T17:04:11-05:00",

"alt": "MP3 Player 8gb",

"width": 123,

"height": 456,

"src": "https://cdn.shopify.com/s/files/1/0005/4838/0009/collections/ipod_nano_8gb.jpg?v=1767996251"

}

}

}

### examples

  * #### Hide a published smart collection

#####

        curl -d '{"smart_collection":{"id":482865238,"published":false}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections/482865238.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const smart_collection = new admin.rest.resources.SmartCollection({session: session});

        smart_collection.id = 482865238;
        smart_collection.published = false;
        await smart_collection.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        smart_collection = ShopifyAPI::SmartCollection.new(session: test_session)
        smart_collection.id = 482865238
        smart_collection.published = false
        smart_collection.save!

#####

        // Session is built by the OAuth process

        const smart_collection = new shopify.rest.SmartCollection({session: session});
        smart_collection.id = 482865238;
        smart_collection.published = false;
        await smart_collection.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"smart_collection":{"title":"Smart iPods","handle":"smart-ipods","body_html":"<p>The best selling ipod ever</p>","id":482865238,"published_at":null,"updated_at":"2026-01-09T17:34:00-05:00","sort_order":"manual","template_suffix":null,"disjunctive":false,"rules":[{"column":"type","relation":"equals","condition":"Cult Products"}],"published_scope":"web","admin_graphql_api_id":"gid://shopify/Collection/482865238","image":{"created_at":"2026-01-09T17:04:11-05:00","alt":"MP3 Player 8gb","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/collections/ipod_nano_8gb.jpg?v=1767996251"}}}

  * #### Publish a hidden collection

#####

        curl -d '{"smart_collection":{"id":482865238,"published":true}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections/482865238.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const smart_collection = new admin.rest.resources.SmartCollection({session: session});

        smart_collection.id = 482865238;
        smart_collection.published = true;
        await smart_collection.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        smart_collection = ShopifyAPI::SmartCollection.new(session: test_session)
        smart_collection.id = 482865238
        smart_collection.published = true
        smart_collection.save!

#####

        // Session is built by the OAuth process

        const smart_collection = new shopify.rest.SmartCollection({session: session});
        smart_collection.id = 482865238;
        smart_collection.published = true;
        await smart_collection.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"smart_collection":{"title":"Smart iPods","handle":"smart-ipods","body_html":"<p>The best selling ipod ever</p>","id":482865238,"published_at":"2026-01-09T17:34:20-05:00","updated_at":"2026-01-09T17:34:20-05:00","sort_order":"manual","template_suffix":null,"disjunctive":false,"rules":[{"column":"type","relation":"equals","condition":"Cult Products"}],"published_scope":"web","admin_graphql_api_id":"gid://shopify/Collection/482865238","image":{"created_at":"2026-01-09T17:04:11-05:00","alt":"MP3 Player 8gb","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/collections/ipod_nano_8gb.jpg?v=1767996251"}}}

  * #### Update a smart collection by clearing the collection image

#####

        curl -d '{"smart_collection":{"id":482865238,"image":"","updated_at":"2026-01-09T17:33:49-05:00","handle":"smart-ipods","title":"Smart iPods","body_html":"<p>The best selling ipod ever</p>","published_at":"2008-02-01T19:00:00-05:00","sort_order":"manual","template_suffix":null,"disjunctive":false,"rules":[{"column":"type","relation":"equals","condition":"Cult Products"}],"published_scope":"web","admin_graphql_api_id":"gid://shopify/Collection/482865238"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections/482865238.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const smart_collection = new admin.rest.resources.SmartCollection({session: session});

        smart_collection.id = 482865238;
        smart_collection.image = "";
        smart_collection.updated_at = "2026-01-09T17:33:49-05:00";
        smart_collection.handle = "smart-ipods";
        smart_collection.title = "Smart iPods";
        smart_collection.body_html = "<p>The best selling ipod ever</p>";
        smart_collection.published_at = "2008-02-01T19:00:00-05:00";
        smart_collection.sort_order = "manual";
        smart_collection.template_suffix = null;
        smart_collection.disjunctive = false;
        smart_collection.rules = [
          {
            "column": "type",
            "relation": "equals",
            "condition": "Cult Products"
          }
        ];
        smart_collection.published_scope = "web";
        smart_collection.admin_graphql_api_id = "gid://shopify/Collection/482865238";
        await smart_collection.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        smart_collection = ShopifyAPI::SmartCollection.new(session: test_session)
        smart_collection.id = 482865238
        smart_collection.image = ""
        smart_collection.updated_at = "2026-01-09T17:33:49-05:00"
        smart_collection.handle = "smart-ipods"
        smart_collection.title = "Smart iPods"
        smart_collection.body_html = "<p>The best selling ipod ever</p>"
        smart_collection.published_at = "2008-02-01T19:00:00-05:00"
        smart_collection.sort_order = "manual"
        smart_collection.template_suffix = nil
        smart_collection.disjunctive = false
        smart_collection.rules = [
          {
            "column" => "type",
            "relation" => "equals",
            "condition" => "Cult Products"
          }
        ]
        smart_collection.published_scope = "web"
        smart_collection.admin_graphql_api_id = "gid://shopify/Collection/482865238"
        smart_collection.save!

#####

        // Session is built by the OAuth process

        const smart_collection = new shopify.rest.SmartCollection({session: session});
        smart_collection.id = 482865238;
        smart_collection.image = "";
        smart_collection.updated_at = "2026-01-09T17:33:49-05:00";
        smart_collection.handle = "smart-ipods";
        smart_collection.title = "Smart iPods";
        smart_collection.body_html = "<p>The best selling ipod ever</p>";
        smart_collection.published_at = "2008-02-01T19:00:00-05:00";
        smart_collection.sort_order = "manual";
        smart_collection.template_suffix = null;
        smart_collection.disjunctive = false;
        smart_collection.rules = [
          {
            "column": "type",
            "relation": "equals",
            "condition": "Cult Products"
          }
        ];
        smart_collection.published_scope = "web";
        smart_collection.admin_graphql_api_id = "gid://shopify/Collection/482865238";
        await smart_collection.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"smart_collection":{"body_html":"<p>The best selling ipod ever</p>","handle":"smart-ipods","updated_at":"2026-01-09T17:33:50-05:00","id":482865238,"title":"Smart iPods","published_at":"2008-02-01T19:00:00-05:00","sort_order":"manual","template_suffix":null,"disjunctive":false,"rules":[{"column":"type","relation":"equals","condition":"Cult Products"}],"published_scope":"web","admin_graphql_api_id":"gid://shopify/Collection/482865238"}}

  * #### Update a smart collection by setting a new collection image

#####

        curl -d '{"smart_collection":{"id":482865238,"image":{"attachment":"R0lGODlhbgCMAPf/APbr48VySrxTO7IgKt2qmKQdJeK8lsFjROG5p/nz7Zg3\nMNmnd7Q1MLNVS9GId71hSJMZIuzTu4UtKbeEeakhKMl8U8WYjfr18YQaIbAf\nKKwhKdKzqpQtLebFortOOejKrOjZ1Mt7aMNpVbAqLLV7bsNqR+3WwMqEWenN\nsZYxL/Ddy/Pm2e7ZxLlUQrIjNPXp3bU5MbhENbEtLtqhj5ZQTfHh0bMxL7Ip\nNsNyUYkZIrZJPcqGdYIUHb5aPKkeJnoUHd2yiJkiLKYiKLRFOsyJXKVDO8up\nosFaS+TBnK4kKti5sNaYg/z49aqYl5kqLrljUtORfMOlo/36+H4ZH8yDYq0f\nKKFYTaU9MrY8MrZBNXwXHpgaIdGVYu/byLZNP9SaZLIyOuXCtHkpJst+Wpcm\nLMyCa8BfP9GMb9KQdPDd1PPk1sd5VP79/L5dQZ0bI9+ymqssK9WcfIoXHdzG\nxdWWfteib79lSr1YP86MYurQxKdcUKdMQr5ZSfPs6YEZH8uhl4oWIenMuurQ\nttmejaqoqsqBVaAcJLlJN5kvMLlZRMNsSL5fRak0LbdQQMVvSPjw6cJnRpkf\nKtmjhvfu5cJtT7IuOMVvWLY/M/37+o0YH9ibhtSYdObErc6HarM9NnYSGNGR\navLi09unje3WyeO8rsVrT7tdRtK3uffu6NWeaL9pTJIjJrM4NPbx8cdyX7M7\nPYYVHu7j4KgoNJAYIKtkV5o9MsOcldicis+RYNutfrhFOZ0hJbqinZ8bI8h5\nUObFuOfItJsfJrJfUOfIqc+PXqQtK8RnSbA4Mcd3Tm0SGbpXQ8aqp7RLNs+s\novHfzpVhV9iggMd1TLtbRKUdKXEQFsd4XrZRPLIgMZUeJ+jKvrAlK6AhJ65A\nMpMpKuC3j5obIsRwS7hAN8l/YtvDvnYXHbAoLI47SIUsOMenorF4gO/m4+fH\npo4vLZ8oKMukqp0cJbhVSMV2UuPR0bAfMLIrLrg/OcJwT8h+Vt+wn8eurLlh\nQrIfKHQOHHQOHf///////yH5BAEAAP8ALAAAAABuAIwAAAj/AP8JHDhQXjpz\n/PopXNiPn0OHDRMmbKhQIsOJFS1SxAhxI8SHFzVeDBnx48iNBAeeOkcxokeX\nFRdOnAlSokaaLXNujJkxo8iYHRkKtWkzZSsaOXkAWsoUECynsHgoqEW1qtVa\n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\nGg4lOnRGDKRZsoS7pMPSA6YXNWLsKJLkSZOVwKhMGSTTrJf9ZNKcomXKTrQY\nevr02cSIvKJxi6aJkaVuXaZMs1ziO5UqPawnuXK9AWEW2Jhja9pMuzMd27YW\nLNga10fuZYUPkdZdqpTv575YbJQbkCHw1sEpb9wQMstwWLFkbfppjJPc/wTI\nhHhJ5r0BBGbMRzfb7ez5MwwbpTMsx5pa9eob2CBM5yETpmzGtTE8hrybN29b\nc1oBn6trc9K7nhmUy6BcOUrn0KHLcr0FQvWYMxdnb3w7t/fvwFMiFvKG0uw8\n4kRLYjkGG0RtMPlWc+GGdyCwbwtYrOsHu7K0a+K/AEO04K0CF8InBvPOg2GE\nKpZTrsHSUotwwgnnmW4LHGGBKbb9bMqhsSly082CW0QMkDLLSvQHFQFiOESX\nLGzQpkUY22swA8Lko9EFLqfBEcdvMhRrwx610OLHtJ5Rc01ahHnCzTeFkXNO\nOfWQkwQ6NNFzTz2X0GQJQAMVdJEYsBhBAyrbK/9tgBcbrCTCG7bkkstvvvwm\nzPzI7JEcNLXDCYICQhXVkAIMMdWQd0x1Y9VdiuHGA1hjhfWQQzyg9dZDYmBg\nyioSVfRKFwfYZ8ZIJ3XhGhe83OLSSwEZU78ea+pUO2wK8MFaUUMl9dReDOll\n1VXbuYIZWWOl1dZDLpGhV3YZXLTR9vZhUMJijUX2mmveYRZcQDLlsCZOp21s\nCx+uLTjbbE/11ttv3diFkSHKRReGcthtN1hgrdxH2Awk5fJefK+ZZ9lvVvXW\n2cT+ZSwHgdHCpmCYDb4WYVNL7baXbsN9FdYYbKDA4otddBdYeffZx9iPjw35\nmmlKNtnUfmXSNNqAW9b/6eWYY8YWYW0V7tYQhxWAwwege61y6OXkbdDoSUFe\nWuR3wP3akKhjUtlHlqklG+YqsjaY620VNgQDMcQQouwrX3zR6KKFZfttyKtw\n+utQnRUL2mjLYjnvtLDpu9e9/ZYZ8FK3maLwwn8OmlF3lWNc7df3gfzteaZZ\n+NTKx5y6RxJ69/333mvBwHOLQ/fhiR2SV34HS47hmnAafJ9gh3AaDMcB7LE/\nIoPY441dhOzDz94VN3DPNmoeM5drAyfK7lWH34baYetVCidBIT6C5UMhB4r2\nn3FheSANRVGCwhBmObtlbgqXyYYNyuYFAMQFCtPwQf3spxAraGBRR+Af91wX\n/zsPoCIuCCAV13yAMsWo7zIOaJHFSHEZHZABdWK4X0JoIAENLIeDCXFA2rgX\nuwG8MC6kKGGoZuaDTEhtd/vBTBoyYLYqeAEzFpihGCagEBqIQQJVGMAOEdLD\n2L0uHJdBAMIOhsTELHExwLnS/i6zAQlIQItWxKIccejGL/4wjPvw4kHSQApA\nBhKQUDCiEWE2C93dTSEW2EMjaWABhbgnA3g8SAj4cElK+kMJWoyjBK6YECtw\nUgKZ7N8ejdZHfzjgGgNY5SpnZsisJXFHikwICTLBskzUECFtxJ/FFKKETmrx\nkwixQiclYAX+mfKUCpnBEZzpzHpkS2Yxm0ViMNcjhf+QABs5uKUuD9KoTOaP\nQb80picxaExk8lCZfIxLNuBhrWnurZpjoiVCbAkBbnrTH2pbTjgZVAVyGnOY\nBylmJ9P5xXWOUS6WEB3ZqgmTazLxMk40WntQub3lbIOc7OjkQP1RUI4e9CCl\nfJ3jjCbEogDAE6KrAiKlVs+4gJF7GUDlDLLnUWCyg6Ps8GgxdyrSVK5zH/WI\noARjZjFEQhSmRCEFg9SGSqIoQadT7alOJcAOoJJUmeFA6VBIETqk+ssPKizK\nDorxwx9CdShSvapOqzpVoO7ApMocgAdcIb74HeSroEOqEn8w1mgVRR0KyEEw\nKqoctTZEquzggFsVooepskP/DwqZAAfmakpGvc4HXSXF54CWVLthALASRYhB\nFpmDd4QxsQxRQmNd61HITnWyCVHC9MTnCsY9U7dH4AM8spGQvVrsiRB4Fg/8\ncFxsJmQDHvUHLQyhWsy01rXs2MFj2ZGC6862KKRgHGY6K9zlEPdyP8AJcteo\n3ClsQCHq0AF0QdkN+HbjlxygL31hO13tMrW7lwkB0BiUoR3x4EfmrYlCNjAF\nCRAoIWmwQexQqQcyxHe+9eXAfVOQAg7k16v7jQsAHGi2Bv0gUzyQQ05Ga+Cy\n0MBEDsZgN8gQ4QnXt7oJ0QOGOZACDTeEu0aTCwC80EKhDcAHMDGHWATMsuMC\nFsVl/9GnP0Jg0kw24MUv/qUTOGDlCj8WETfGsVx2vI+UzsATIFZUaTIRk3QY\n+ZYlFq0Ce5QJHBXgdU+MRCSwEYlVBCHPQZhyn7vhhD9fWdAc2DKhKXxhRCc6\n0Yi4LOPcl6hGVUFqc4gJLGaxufKO1s2VkrOj63znOkciCKMedZ+n7ARUp1rQ\niLAyIlyNYURcONaInrWs9ci4JyJOaFYawDzP8Q+ZwAICLckbgd08i290eh9V\nCIadQw3qO5Oa1H1GNRlSjeorO2HLruZ2rLudAm+Dm9Gxcx/GXmSIMbnjH5W2\nzy2RbOzM+cENBRAWs0N9b3zXWdp8pra1r61tbXdb4N/2Nv8i5gzeIJd5Gjui\nwT+AzQ9YVGrYnNO0Agm27GBkvNnNzje+921qf/+b1QEfuMDFPe5lk/lspUG3\nWKbQCofLBBBuwNEs3C3aikcrB2TTeM81HgmOd3zf/PZ3yFPNaqSXfODF0EDK\nE9e6liZmCvJwOLD7AQhU2efSbG6zm7VgiG1ofBc+//nGgZ7vbYw67aVux4v/\nfXSSK53by/HVrzIwDZTBBANUrzpMeAAIWASeB4P/AQ9+cHjEJx7xWgDE5nLQ\neMdHXvKbg/zkMZ23H/1oFRjYPOc9v3nQ58Aw0xn9LACvO7HQAOZVf/jl0ii1\nHcXe9bPX3euftaPL5R71tIf97nsy7/o0WlP2r4/JOU7B+r5nqva7jz1EdZ97\n4qNe+bonfvCfVXvly1762beOOdLBd+Q7PCAAOw==\n","alt":"Rails logo"}}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections/482865238.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const smart_collection = new admin.rest.resources.SmartCollection({session: session});

        smart_collection.id = 482865238;
        smart_collection.image = {
          "attachment": "R0lGODlhbgCMAPf/APbr48VySrxTO7IgKt2qmKQdJeK8lsFjROG5p/nz7Zg3\nMNmnd7Q1MLNVS9GId71hSJMZIuzTu4UtKbeEeakhKMl8U8WYjfr18YQaIbAf\nKKwhKdKzqpQtLebFortOOejKrOjZ1Mt7aMNpVbAqLLV7bsNqR+3WwMqEWenN\nsZYxL/Ddy/Pm2e7ZxLlUQrIjNPXp3bU5MbhENbEtLtqhj5ZQTfHh0bMxL7Ip\nNsNyUYkZIrZJPcqGdYIUHb5aPKkeJnoUHd2yiJkiLKYiKLRFOsyJXKVDO8up\nosFaS+TBnK4kKti5sNaYg/z49aqYl5kqLrljUtORfMOlo/36+H4ZH8yDYq0f\nKKFYTaU9MrY8MrZBNXwXHpgaIdGVYu/byLZNP9SaZLIyOuXCtHkpJst+Wpcm\nLMyCa8BfP9GMb9KQdPDd1PPk1sd5VP79/L5dQZ0bI9+ymqssK9WcfIoXHdzG\nxdWWfteib79lSr1YP86MYurQxKdcUKdMQr5ZSfPs6YEZH8uhl4oWIenMuurQ\nttmejaqoqsqBVaAcJLlJN5kvMLlZRMNsSL5fRak0LbdQQMVvSPjw6cJnRpkf\nKtmjhvfu5cJtT7IuOMVvWLY/M/37+o0YH9ibhtSYdObErc6HarM9NnYSGNGR\navLi09unje3WyeO8rsVrT7tdRtK3uffu6NWeaL9pTJIjJrM4NPbx8cdyX7M7\nPYYVHu7j4KgoNJAYIKtkV5o9MsOcldicis+RYNutfrhFOZ0hJbqinZ8bI8h5\nUObFuOfItJsfJrJfUOfIqc+PXqQtK8RnSbA4Mcd3Tm0SGbpXQ8aqp7RLNs+s\novHfzpVhV9iggMd1TLtbRKUdKXEQFsd4XrZRPLIgMZUeJ+jKvrAlK6AhJ65A\nMpMpKuC3j5obIsRwS7hAN8l/YtvDvnYXHbAoLI47SIUsOMenorF4gO/m4+fH\npo4vLZ8oKMukqp0cJbhVSMV2UuPR0bAfMLIrLrg/OcJwT8h+Vt+wn8eurLlh\nQrIfKHQOHHQOHf///////yH5BAEAAP8ALAAAAABuAIwAAAj/AP8JHDhQXjpz\n/PopXNiPn0OHDRMmbKhQIsOJFS1SxAhxI8SHFzVeDBnx48iNBAeeOkcxokeX\nFRdOnAlSokaaLXNujJkxo8iYHRkKtWkzZSsaOXkAWsoUECynsHgoqEW1qtVa\n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\nGg4lOnRGDKRZsoS7pMPSA6YXNWLsKJLkSZOVwKhMGSTTrJf9ZNKcomXKTrQY\nevr02cSIvKJxi6aJkaVuXaZMs1ziO5UqPawnuXK9AWEW2Jhja9pMuzMd27YW\nLNga10fuZYUPkdZdqpTv575YbJQbkCHw1sEpb9wQMstwWLFkbfppjJPc/wTI\nhHhJ5r0BBGbMRzfb7ez5MwwbpTMsx5pa9eob2CBM5yETpmzGtTE8hrybN29b\nc1oBn6trc9K7nhmUy6BcOUrn0KHLcr0FQvWYMxdnb3w7t/fvwFMiFvKG0uw8\n4kRLYjkGG0RtMPlWc+GGdyCwbwtYrOsHu7K0a+K/AEO04K0CF8InBvPOg2GE\nKpZTrsHSUotwwgnnmW4LHGGBKbb9bMqhsSly082CW0QMkDLLSvQHFQFiOESX\nLGzQpkUY22swA8Lko9EFLqfBEcdvMhRrwx610OLHtJ5Rc01ahHnCzTeFkXNO\nOfWQkwQ6NNFzTz2X0GQJQAMVdJEYsBhBAyrbK/9tgBcbrCTCG7bkkstvvvwm\nzPzI7JEcNLXDCYICQhXVkAIMMdWQd0x1Y9VdiuHGA1hjhfWQQzyg9dZDYmBg\nyioSVfRKFwfYZ8ZIJ3XhGhe83OLSSwEZU78ea+pUO2wK8MFaUUMl9dReDOll\n1VXbuYIZWWOl1dZDLpGhV3YZXLTR9vZhUMJijUX2mmveYRZcQDLlsCZOp21s\nCx+uLTjbbE/11ttv3diFkSHKRReGcthtN1hgrdxH2Awk5fJefK+ZZ9lvVvXW\n2cT+ZSwHgdHCpmCYDb4WYVNL7baXbsN9FdYYbKDA4otddBdYeffZx9iPjw35\nmmlKNtnUfmXSNNqAW9b/6eWYY8YWYW0V7tYQhxWAwwege61y6OXkbdDoSUFe\nWuR3wP3akKhjUtlHlqklG+YqsjaY620VNgQDMcQQouwrX3zR6KKFZfttyKtw\n+utQnRUL2mjLYjnvtLDpu9e9/ZYZ8FK3maLwwn8OmlF3lWNc7df3gfzteaZZ\n+NTKx5y6RxJ69/333mvBwHOLQ/fhiR2SV34HS47hmnAafJ9gh3AaDMcB7LE/\nIoPY441dhOzDz94VN3DPNmoeM5drAyfK7lWH34baYetVCidBIT6C5UMhB4r2\nn3FheSANRVGCwhBmObtlbgqXyYYNyuYFAMQFCtPwQf3spxAraGBRR+Af91wX\n/zsPoCIuCCAV13yAMsWo7zIOaJHFSHEZHZABdWK4X0JoIAENLIeDCXFA2rgX\nuwG8MC6kKGGoZuaDTEhtd/vBTBoyYLYqeAEzFpihGCagEBqIQQJVGMAOEdLD\n2L0uHJdBAMIOhsTELHExwLnS/i6zAQlIQItWxKIccejGL/4wjPvw4kHSQApA\nBhKQUDCiEWE2C93dTSEW2EMjaWABhbgnA3g8SAj4cElK+kMJWoyjBK6YECtw\nUgKZ7N8ejdZHfzjgGgNY5SpnZsisJXFHikwICTLBskzUECFtxJ/FFKKETmrx\nkwixQiclYAX+mfKUCpnBEZzpzHpkS2Yxm0ViMNcjhf+QABs5uKUuD9KoTOaP\nQb80picxaExk8lCZfIxLNuBhrWnurZpjoiVCbAkBbnrTH2pbTjgZVAVyGnOY\nBylmJ9P5xXWOUS6WEB3ZqgmTazLxMk40WntQub3lbIOc7OjkQP1RUI4e9CCl\nfJ3jjCbEogDAE6KrAiKlVs+4gJF7GUDlDLLnUWCyg6Ps8GgxdyrSVK5zH/WI\noARjZjFEQhSmRCEFg9SGSqIoQadT7alOJcAOoJJUmeFA6VBIETqk+ssPKizK\nDorxwx9CdShSvapOqzpVoO7ApMocgAdcIb74HeSroEOqEn8w1mgVRR0KyEEw\nKqoctTZEquzggFsVooepskP/DwqZAAfmakpGvc4HXSXF54CWVLthALASRYhB\nFpmDd4QxsQxRQmNd61HITnWyCVHC9MTnCsY9U7dH4AM8spGQvVrsiRB4Fg/8\ncFxsJmQDHvUHLQyhWsy01rXs2MFj2ZGC6862KKRgHGY6K9zlEPdyP8AJcteo\n3ClsQCHq0AF0QdkN+HbjlxygL31hO13tMrW7lwkB0BiUoR3x4EfmrYlCNjAF\nCRAoIWmwQexQqQcyxHe+9eXAfVOQAg7k16v7jQsAHGi2Bv0gUzyQQ05Ga+Cy\n0MBEDsZgN8gQ4QnXt7oJ0QOGOZACDTeEu0aTCwC80EKhDcAHMDGHWATMsuMC\nFsVl/9GnP0Jg0kw24MUv/qUTOGDlCj8WETfGsVx2vI+UzsATIFZUaTIRk3QY\n+ZYlFq0Ce5QJHBXgdU+MRCSwEYlVBCHPQZhyn7vhhD9fWdAc2DKhKXxhRCc6\n0Yi4LOPcl6hGVUFqc4gJLGaxufKO1s2VkrOj63znOkciCKMedZ+n7ARUp1rQ\niLAyIlyNYURcONaInrWs9ci4JyJOaFYawDzP8Q+ZwAICLckbgd08i290eh9V\nCIadQw3qO5Oa1H1GNRlSjeorO2HLruZ2rLudAm+Dm9Gxcx/GXmSIMbnjH5W2\nzy2RbOzM+cENBRAWs0N9b3zXWdp8pra1r61tbXdb4N/2Nv8i5gzeIJd5Gjui\nwT+AzQ9YVGrYnNO0Agm27GBkvNnNzje+921qf/+b1QEfuMDFPe5lk/lspUG3\nWKbQCofLBBBuwNEs3C3aikcrB2TTeM81HgmOd3zf/PZ3yFPNaqSXfODF0EDK\nE9e6liZmCvJwOLD7AQhU2efSbG6zm7VgiG1ofBc+//nGgZ7vbYw67aVux4v/\nfXSSK53by/HVrzIwDZTBBANUrzpMeAAIWASeB4P/AQ9+cHjEJx7xWgDE5nLQ\neMdHXvKbg/zkMZ23H/1oFRjYPOc9v3nQ58Aw0xn9LACvO7HQAOZVf/jl0ii1\nHcXe9bPX3euftaPL5R71tIf97nsy7/o0WlP2r4/JOU7B+r5nqva7jz1EdZ97\n4qNe+bonfvCfVXvly1762beOOdLBd+Q7PCAAOw==\n",
          "alt": "Rails logo"
        };
        await smart_collection.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        smart_collection = ShopifyAPI::SmartCollection.new(session: test_session)
        smart_collection.id = 482865238
        smart_collection.image = {
          "attachment" => "R0lGODlhbgCMAPf/APbr48VySrxTO7IgKt2qmKQdJeK8lsFjROG5p/nz7Zg3\nMNmnd7Q1MLNVS9GId71hSJMZIuzTu4UtKbeEeakhKMl8U8WYjfr18YQaIbAf\nKKwhKdKzqpQtLebFortOOejKrOjZ1Mt7aMNpVbAqLLV7bsNqR+3WwMqEWenN\nsZYxL/Ddy/Pm2e7ZxLlUQrIjNPXp3bU5MbhENbEtLtqhj5ZQTfHh0bMxL7Ip\nNsNyUYkZIrZJPcqGdYIUHb5aPKkeJnoUHd2yiJkiLKYiKLRFOsyJXKVDO8up\nosFaS+TBnK4kKti5sNaYg/z49aqYl5kqLrljUtORfMOlo/36+H4ZH8yDYq0f\nKKFYTaU9MrY8MrZBNXwXHpgaIdGVYu/byLZNP9SaZLIyOuXCtHkpJst+Wpcm\nLMyCa8BfP9GMb9KQdPDd1PPk1sd5VP79/L5dQZ0bI9+ymqssK9WcfIoXHdzG\nxdWWfteib79lSr1YP86MYurQxKdcUKdMQr5ZSfPs6YEZH8uhl4oWIenMuurQ\nttmejaqoqsqBVaAcJLlJN5kvMLlZRMNsSL5fRak0LbdQQMVvSPjw6cJnRpkf\nKtmjhvfu5cJtT7IuOMVvWLY/M/37+o0YH9ibhtSYdObErc6HarM9NnYSGNGR\navLi09unje3WyeO8rsVrT7tdRtK3uffu6NWeaL9pTJIjJrM4NPbx8cdyX7M7\nPYYVHu7j4KgoNJAYIKtkV5o9MsOcldicis+RYNutfrhFOZ0hJbqinZ8bI8h5\nUObFuOfItJsfJrJfUOfIqc+PXqQtK8RnSbA4Mcd3Tm0SGbpXQ8aqp7RLNs+s\novHfzpVhV9iggMd1TLtbRKUdKXEQFsd4XrZRPLIgMZUeJ+jKvrAlK6AhJ65A\nMpMpKuC3j5obIsRwS7hAN8l/YtvDvnYXHbAoLI47SIUsOMenorF4gO/m4+fH\npo4vLZ8oKMukqp0cJbhVSMV2UuPR0bAfMLIrLrg/OcJwT8h+Vt+wn8eurLlh\nQrIfKHQOHHQOHf///////yH5BAEAAP8ALAAAAABuAIwAAAj/AP8JHDhQXjpz\n/PopXNiPn0OHDRMmbKhQIsOJFS1SxAhxI8SHFzVeDBnx48iNBAeeOkcxokeX\nFRdOnAlSokaaLXNujJkxo8iYHRkKtWkzZSsaOXkAWsoUECynsHgoqEW1qtVa\n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\nGg4lOnRGDKRZsoS7pMPSA6YXNWLsKJLkSZOVwKhMGSTTrJf9ZNKcomXKTrQY\nevr02cSIvKJxi6aJkaVuXaZMs1ziO5UqPawnuXK9AWEW2Jhja9pMuzMd27YW\nLNga10fuZYUPkdZdqpTv575YbJQbkCHw1sEpb9wQMstwWLFkbfppjJPc/wTI\nhHhJ5r0BBGbMRzfb7ez5MwwbpTMsx5pa9eob2CBM5yETpmzGtTE8hrybN29b\nc1oBn6trc9K7nhmUy6BcOUrn0KHLcr0FQvWYMxdnb3w7t/fvwFMiFvKG0uw8\n4kRLYjkGG0RtMPlWc+GGdyCwbwtYrOsHu7K0a+K/AEO04K0CF8InBvPOg2GE\nKpZTrsHSUotwwgnnmW4LHGGBKbb9bMqhsSly082CW0QMkDLLSvQHFQFiOESX\nLGzQpkUY22swA8Lko9EFLqfBEcdvMhRrwx610OLHtJ5Rc01ahHnCzTeFkXNO\nOfWQkwQ6NNFzTz2X0GQJQAMVdJEYsBhBAyrbK/9tgBcbrCTCG7bkkstvvvwm\nzPzI7JEcNLXDCYICQhXVkAIMMdWQd0x1Y9VdiuHGA1hjhfWQQzyg9dZDYmBg\nyioSVfRKFwfYZ8ZIJ3XhGhe83OLSSwEZU78ea+pUO2wK8MFaUUMl9dReDOll\n1VXbuYIZWWOl1dZDLpGhV3YZXLTR9vZhUMJijUX2mmveYRZcQDLlsCZOp21s\nCx+uLTjbbE/11ttv3diFkSHKRReGcthtN1hgrdxH2Awk5fJefK+ZZ9lvVvXW\n2cT+ZSwHgdHCpmCYDb4WYVNL7baXbsN9FdYYbKDA4otddBdYeffZx9iPjw35\nmmlKNtnUfmXSNNqAW9b/6eWYY8YWYW0V7tYQhxWAwwege61y6OXkbdDoSUFe\nWuR3wP3akKhjUtlHlqklG+YqsjaY620VNgQDMcQQouwrX3zR6KKFZfttyKtw\n+utQnRUL2mjLYjnvtLDpu9e9/ZYZ8FK3maLwwn8OmlF3lWNc7df3gfzteaZZ\n+NTKx5y6RxJ69/333mvBwHOLQ/fhiR2SV34HS47hmnAafJ9gh3AaDMcB7LE/\nIoPY441dhOzDz94VN3DPNmoeM5drAyfK7lWH34baYetVCidBIT6C5UMhB4r2\nn3FheSANRVGCwhBmObtlbgqXyYYNyuYFAMQFCtPwQf3spxAraGBRR+Af91wX\n/zsPoCIuCCAV13yAMsWo7zIOaJHFSHEZHZABdWK4X0JoIAENLIeDCXFA2rgX\nuwG8MC6kKGGoZuaDTEhtd/vBTBoyYLYqeAEzFpihGCagEBqIQQJVGMAOEdLD\n2L0uHJdBAMIOhsTELHExwLnS/i6zAQlIQItWxKIccejGL/4wjPvw4kHSQApA\nBhKQUDCiEWE2C93dTSEW2EMjaWABhbgnA3g8SAj4cElK+kMJWoyjBK6YECtw\nUgKZ7N8ejdZHfzjgGgNY5SpnZsisJXFHikwICTLBskzUECFtxJ/FFKKETmrx\nkwixQiclYAX+mfKUCpnBEZzpzHpkS2Yxm0ViMNcjhf+QABs5uKUuD9KoTOaP\nQb80picxaExk8lCZfIxLNuBhrWnurZpjoiVCbAkBbnrTH2pbTjgZVAVyGnOY\nBylmJ9P5xXWOUS6WEB3ZqgmTazLxMk40WntQub3lbIOc7OjkQP1RUI4e9CCl\nfJ3jjCbEogDAE6KrAiKlVs+4gJF7GUDlDLLnUWCyg6Ps8GgxdyrSVK5zH/WI\noARjZjFEQhSmRCEFg9SGSqIoQadT7alOJcAOoJJUmeFA6VBIETqk+ssPKizK\nDorxwx9CdShSvapOqzpVoO7ApMocgAdcIb74HeSroEOqEn8w1mgVRR0KyEEw\nKqoctTZEquzggFsVooepskP/DwqZAAfmakpGvc4HXSXF54CWVLthALASRYhB\nFpmDd4QxsQxRQmNd61HITnWyCVHC9MTnCsY9U7dH4AM8spGQvVrsiRB4Fg/8\ncFxsJmQDHvUHLQyhWsy01rXs2MFj2ZGC6862KKRgHGY6K9zlEPdyP8AJcteo\n3ClsQCHq0AF0QdkN+HbjlxygL31hO13tMrW7lwkB0BiUoR3x4EfmrYlCNjAF\nCRAoIWmwQexQqQcyxHe+9eXAfVOQAg7k16v7jQsAHGi2Bv0gUzyQQ05Ga+Cy\n0MBEDsZgN8gQ4QnXt7oJ0QOGOZACDTeEu0aTCwC80EKhDcAHMDGHWATMsuMC\nFsVl/9GnP0Jg0kw24MUv/qUTOGDlCj8WETfGsVx2vI+UzsATIFZUaTIRk3QY\n+ZYlFq0Ce5QJHBXgdU+MRCSwEYlVBCHPQZhyn7vhhD9fWdAc2DKhKXxhRCc6\n0Yi4LOPcl6hGVUFqc4gJLGaxufKO1s2VkrOj63znOkciCKMedZ+n7ARUp1rQ\niLAyIlyNYURcONaInrWs9ci4JyJOaFYawDzP8Q+ZwAICLckbgd08i290eh9V\nCIadQw3qO5Oa1H1GNRlSjeorO2HLruZ2rLudAm+Dm9Gxcx/GXmSIMbnjH5W2\nzy2RbOzM+cENBRAWs0N9b3zXWdp8pra1r61tbXdb4N/2Nv8i5gzeIJd5Gjui\nwT+AzQ9YVGrYnNO0Agm27GBkvNnNzje+921qf/+b1QEfuMDFPe5lk/lspUG3\nWKbQCofLBBBuwNEs3C3aikcrB2TTeM81HgmOd3zf/PZ3yFPNaqSXfODF0EDK\nE9e6liZmCvJwOLD7AQhU2efSbG6zm7VgiG1ofBc+//nGgZ7vbYw67aVux4v/\nfXSSK53by/HVrzIwDZTBBANUrzpMeAAIWASeB4P/AQ9+cHjEJx7xWgDE5nLQ\neMdHXvKbg/zkMZ23H/1oFRjYPOc9v3nQ58Aw0xn9LACvO7HQAOZVf/jl0ii1\nHcXe9bPX3euftaPL5R71tIf97nsy7/o0WlP2r4/JOU7B+r5nqva7jz1EdZ97\n4qNe+bonfvCfVXvly1762beOOdLBd+Q7PCAAOw==\n",
          "alt" => "Rails logo"
        }
        smart_collection.save!

#####

        // Session is built by the OAuth process

        const smart_collection = new shopify.rest.SmartCollection({session: session});
        smart_collection.id = 482865238;
        smart_collection.image = {
          "attachment": "R0lGODlhbgCMAPf/APbr48VySrxTO7IgKt2qmKQdJeK8lsFjROG5p/nz7Zg3\nMNmnd7Q1MLNVS9GId71hSJMZIuzTu4UtKbeEeakhKMl8U8WYjfr18YQaIbAf\nKKwhKdKzqpQtLebFortOOejKrOjZ1Mt7aMNpVbAqLLV7bsNqR+3WwMqEWenN\nsZYxL/Ddy/Pm2e7ZxLlUQrIjNPXp3bU5MbhENbEtLtqhj5ZQTfHh0bMxL7Ip\nNsNyUYkZIrZJPcqGdYIUHb5aPKkeJnoUHd2yiJkiLKYiKLRFOsyJXKVDO8up\nosFaS+TBnK4kKti5sNaYg/z49aqYl5kqLrljUtORfMOlo/36+H4ZH8yDYq0f\nKKFYTaU9MrY8MrZBNXwXHpgaIdGVYu/byLZNP9SaZLIyOuXCtHkpJst+Wpcm\nLMyCa8BfP9GMb9KQdPDd1PPk1sd5VP79/L5dQZ0bI9+ymqssK9WcfIoXHdzG\nxdWWfteib79lSr1YP86MYurQxKdcUKdMQr5ZSfPs6YEZH8uhl4oWIenMuurQ\nttmejaqoqsqBVaAcJLlJN5kvMLlZRMNsSL5fRak0LbdQQMVvSPjw6cJnRpkf\nKtmjhvfu5cJtT7IuOMVvWLY/M/37+o0YH9ibhtSYdObErc6HarM9NnYSGNGR\navLi09unje3WyeO8rsVrT7tdRtK3uffu6NWeaL9pTJIjJrM4NPbx8cdyX7M7\nPYYVHu7j4KgoNJAYIKtkV5o9MsOcldicis+RYNutfrhFOZ0hJbqinZ8bI8h5\nUObFuOfItJsfJrJfUOfIqc+PXqQtK8RnSbA4Mcd3Tm0SGbpXQ8aqp7RLNs+s\novHfzpVhV9iggMd1TLtbRKUdKXEQFsd4XrZRPLIgMZUeJ+jKvrAlK6AhJ65A\nMpMpKuC3j5obIsRwS7hAN8l/YtvDvnYXHbAoLI47SIUsOMenorF4gO/m4+fH\npo4vLZ8oKMukqp0cJbhVSMV2UuPR0bAfMLIrLrg/OcJwT8h+Vt+wn8eurLlh\nQrIfKHQOHHQOHf///////yH5BAEAAP8ALAAAAABuAIwAAAj/AP8JHDhQXjpz\n/PopXNiPn0OHDRMmbKhQIsOJFS1SxAhxI8SHFzVeDBnx48iNBAeeOkcxokeX\nFRdOnAlSokaaLXNujJkxo8iYHRkKtWkzZSsaOXkAWsoUECynsHgoqEW1qtVa\n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\nGg4lOnRGDKRZsoS7pMPSA6YXNWLsKJLkSZOVwKhMGSTTrJf9ZNKcomXKTrQY\nevr02cSIvKJxi6aJkaVuXaZMs1ziO5UqPawnuXK9AWEW2Jhja9pMuzMd27YW\nLNga10fuZYUPkdZdqpTv575YbJQbkCHw1sEpb9wQMstwWLFkbfppjJPc/wTI\nhHhJ5r0BBGbMRzfb7ez5MwwbpTMsx5pa9eob2CBM5yETpmzGtTE8hrybN29b\nc1oBn6trc9K7nhmUy6BcOUrn0KHLcr0FQvWYMxdnb3w7t/fvwFMiFvKG0uw8\n4kRLYjkGG0RtMPlWc+GGdyCwbwtYrOsHu7K0a+K/AEO04K0CF8InBvPOg2GE\nKpZTrsHSUotwwgnnmW4LHGGBKbb9bMqhsSly082CW0QMkDLLSvQHFQFiOESX\nLGzQpkUY22swA8Lko9EFLqfBEcdvMhRrwx610OLHtJ5Rc01ahHnCzTeFkXNO\nOfWQkwQ6NNFzTz2X0GQJQAMVdJEYsBhBAyrbK/9tgBcbrCTCG7bkkstvvvwm\nzPzI7JEcNLXDCYICQhXVkAIMMdWQd0x1Y9VdiuHGA1hjhfWQQzyg9dZDYmBg\nyioSVfRKFwfYZ8ZIJ3XhGhe83OLSSwEZU78ea+pUO2wK8MFaUUMl9dReDOll\n1VXbuYIZWWOl1dZDLpGhV3YZXLTR9vZhUMJijUX2mmveYRZcQDLlsCZOp21s\nCx+uLTjbbE/11ttv3diFkSHKRReGcthtN1hgrdxH2Awk5fJefK+ZZ9lvVvXW\n2cT+ZSwHgdHCpmCYDb4WYVNL7baXbsN9FdYYbKDA4otddBdYeffZx9iPjw35\nmmlKNtnUfmXSNNqAW9b/6eWYY8YWYW0V7tYQhxWAwwege61y6OXkbdDoSUFe\nWuR3wP3akKhjUtlHlqklG+YqsjaY620VNgQDMcQQouwrX3zR6KKFZfttyKtw\n+utQnRUL2mjLYjnvtLDpu9e9/ZYZ8FK3maLwwn8OmlF3lWNc7df3gfzteaZZ\n+NTKx5y6RxJ69/333mvBwHOLQ/fhiR2SV34HS47hmnAafJ9gh3AaDMcB7LE/\nIoPY441dhOzDz94VN3DPNmoeM5drAyfK7lWH34baYetVCidBIT6C5UMhB4r2\nn3FheSANRVGCwhBmObtlbgqXyYYNyuYFAMQFCtPwQf3spxAraGBRR+Af91wX\n/zsPoCIuCCAV13yAMsWo7zIOaJHFSHEZHZABdWK4X0JoIAENLIeDCXFA2rgX\nuwG8MC6kKGGoZuaDTEhtd/vBTBoyYLYqeAEzFpihGCagEBqIQQJVGMAOEdLD\n2L0uHJdBAMIOhsTELHExwLnS/i6zAQlIQItWxKIccejGL/4wjPvw4kHSQApA\nBhKQUDCiEWE2C93dTSEW2EMjaWABhbgnA3g8SAj4cElK+kMJWoyjBK6YECtw\nUgKZ7N8ejdZHfzjgGgNY5SpnZsisJXFHikwICTLBskzUECFtxJ/FFKKETmrx\nkwixQiclYAX+mfKUCpnBEZzpzHpkS2Yxm0ViMNcjhf+QABs5uKUuD9KoTOaP\nQb80picxaExk8lCZfIxLNuBhrWnurZpjoiVCbAkBbnrTH2pbTjgZVAVyGnOY\nBylmJ9P5xXWOUS6WEB3ZqgmTazLxMk40WntQub3lbIOc7OjkQP1RUI4e9CCl\nfJ3jjCbEogDAE6KrAiKlVs+4gJF7GUDlDLLnUWCyg6Ps8GgxdyrSVK5zH/WI\noARjZjFEQhSmRCEFg9SGSqIoQadT7alOJcAOoJJUmeFA6VBIETqk+ssPKizK\nDorxwx9CdShSvapOqzpVoO7ApMocgAdcIb74HeSroEOqEn8w1mgVRR0KyEEw\nKqoctTZEquzggFsVooepskP/DwqZAAfmakpGvc4HXSXF54CWVLthALASRYhB\nFpmDd4QxsQxRQmNd61HITnWyCVHC9MTnCsY9U7dH4AM8spGQvVrsiRB4Fg/8\ncFxsJmQDHvUHLQyhWsy01rXs2MFj2ZGC6862KKRgHGY6K9zlEPdyP8AJcteo\n3ClsQCHq0AF0QdkN+HbjlxygL31hO13tMrW7lwkB0BiUoR3x4EfmrYlCNjAF\nCRAoIWmwQexQqQcyxHe+9eXAfVOQAg7k16v7jQsAHGi2Bv0gUzyQQ05Ga+Cy\n0MBEDsZgN8gQ4QnXt7oJ0QOGOZACDTeEu0aTCwC80EKhDcAHMDGHWATMsuMC\nFsVl/9GnP0Jg0kw24MUv/qUTOGDlCj8WETfGsVx2vI+UzsATIFZUaTIRk3QY\n+ZYlFq0Ce5QJHBXgdU+MRCSwEYlVBCHPQZhyn7vhhD9fWdAc2DKhKXxhRCc6\n0Yi4LOPcl6hGVUFqc4gJLGaxufKO1s2VkrOj63znOkciCKMedZ+n7ARUp1rQ\niLAyIlyNYURcONaInrWs9ci4JyJOaFYawDzP8Q+ZwAICLckbgd08i290eh9V\nCIadQw3qO5Oa1H1GNRlSjeorO2HLruZ2rLudAm+Dm9Gxcx/GXmSIMbnjH5W2\nzy2RbOzM+cENBRAWs0N9b3zXWdp8pra1r61tbXdb4N/2Nv8i5gzeIJd5Gjui\nwT+AzQ9YVGrYnNO0Agm27GBkvNnNzje+921qf/+b1QEfuMDFPe5lk/lspUG3\nWKbQCofLBBBuwNEs3C3aikcrB2TTeM81HgmOd3zf/PZ3yFPNaqSXfODF0EDK\nE9e6liZmCvJwOLD7AQhU2efSbG6zm7VgiG1ofBc+//nGgZ7vbYw67aVux4v/\nfXSSK53by/HVrzIwDZTBBANUrzpMeAAIWASeB4P/AQ9+cHjEJx7xWgDE5nLQ\neMdHXvKbg/zkMZ23H/1oFRjYPOc9v3nQ58Aw0xn9LACvO7HQAOZVf/jl0ii1\nHcXe9bPX3euftaPL5R71tIf97nsy7/o0WlP2r4/JOU7B+r5nqva7jz1EdZ97\n4qNe+bonfvCfVXvly1762beOOdLBd+Q7PCAAOw==\n",
          "alt": "Rails logo"
        };
        await smart_collection.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"smart_collection":{"updated_at":"2026-01-09T17:33:36-05:00","id":482865238,"handle":"smart-ipods","title":"Smart iPods","body_html":"<p>The best selling ipod ever</p>","published_at":"2008-02-01T19:00:00-05:00","sort_order":"manual","template_suffix":null,"disjunctive":false,"rules":[{"column":"type","relation":"equals","condition":"Cult Products"}],"published_scope":"web","admin_graphql_api_id":"gid://shopify/Collection/482865238","image":{"created_at":"2026-01-09T17:33:36-05:00","alt":"Rails logo","width":110,"height":140,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/collections/fd43f2c8883f6e9b680e3295fd990d2c.gif?v=1767998016"}}}

  * #### Update a smart collection by setting a new collection image alternative text

#####

        curl -d '{"smart_collection":{"id":482865238,"image":{"alt":"Rails logo"}}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections/482865238.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const smart_collection = new admin.rest.resources.SmartCollection({session: session});

        smart_collection.id = 482865238;
        smart_collection.image = {
          "alt": "Rails logo"
        };
        await smart_collection.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        smart_collection = ShopifyAPI::SmartCollection.new(session: test_session)
        smart_collection.id = 482865238
        smart_collection.image = {
          "alt" => "Rails logo"
        }
        smart_collection.save!

#####

        // Session is built by the OAuth process

        const smart_collection = new shopify.rest.SmartCollection({session: session});
        smart_collection.id = 482865238;
        smart_collection.image = {
          "alt": "Rails logo"
        };
        await smart_collection.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"smart_collection":{"updated_at":"2026-01-09T17:33:16-05:00","id":482865238,"handle":"smart-ipods","title":"Smart iPods","body_html":"<p>The best selling ipod ever</p>","published_at":"2008-02-01T19:00:00-05:00","sort_order":"manual","template_suffix":null,"disjunctive":false,"rules":[{"column":"type","relation":"equals","condition":"Cult Products"}],"published_scope":"web","admin_graphql_api_id":"gid://shopify/Collection/482865238","image":{"alt":"Rails logo","created_at":"2026-01-09T17:33:13-05:00","width":110,"height":140,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/collections/rails_logo20260109-27647-dtok48.gif?v=1767997996"}}}

  * #### Update the description of a smart collection

#####

        curl -d '{"smart_collection":{"id":482865238,"body_html":"<p>5000 songs in your pocket</p>"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections/482865238.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const smart_collection = new admin.rest.resources.SmartCollection({session: session});

        smart_collection.id = 482865238;
        smart_collection.body_html = "<p>5000 songs in your pocket</p>";
        await smart_collection.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        smart_collection = ShopifyAPI::SmartCollection.new(session: test_session)
        smart_collection.id = 482865238
        smart_collection.body_html = "<p>5000 songs in your pocket</p>"
        smart_collection.save!

#####

        // Session is built by the OAuth process

        const smart_collection = new shopify.rest.SmartCollection({session: session});
        smart_collection.id = 482865238;
        smart_collection.body_html = "<p>5000 songs in your pocket</p>";
        await smart_collection.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"smart_collection":{"body_html":"<p>5000 songs in your pocket</p>","title":"Smart iPods","handle":"smart-ipods","id":482865238,"updated_at":"2026-01-09T17:34:02-05:00","published_at":"2008-02-01T19:00:00-05:00","sort_order":"manual","template_suffix":null,"disjunctive":false,"rules":[{"column":"type","relation":"equals","condition":"Cult Products"}],"published_scope":"web","admin_graphql_api_id":"gid://shopify/Collection/482865238","image":{"created_at":"2026-01-09T17:04:11-05:00","alt":"MP3 Player 8gb","width":123,"height":456,"src":"https://cdn.shopify.com/s/files/1/0005/4838/0009/collections/ipod_nano_8gb.jpg?v=1767996251"}}}


* * *

##

[Anchor to PUT request, Updates the ordering type of products in a smart collection](/docs/api/admin-rest/latest/resources/smartcollection#put-smart-collections-smart-collection-id-order?products\[\]=921728736&products\[\]=632910392)

put

Updates the ordering type of products in a smart collection

[collectionUpdate](/docs/api/admin-graphql/latest/mutations/collectionUpdate)

[collectionReorderProducts](/docs/api/admin-graphql/latest/mutations/collectionReorderProducts?example=updates-the-ordering-type-of-products-in-a-smart-collection)

Updates the ordering type of products in a smart collection

###

[Anchor to Parameters of Updates the ordering type of products in a smart collection](/docs/api/admin-rest/latest/resources/smartcollection#put-smart-collections-smart-collection-id-order?products\[\]=921728736&products\[\]=632910392-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

smart_collection_id

string**string**

required**required**

* * *

products

An array of product IDs, in the order that you want them to appear at the top of the collection. When `products` is specified but empty, any previously sorted products are cleared.

* * *

sort_order

default (current value)**default (current value)**

The type of sorting to apply. Valid values are listed in the Properties section above.

* * *

Was this section helpful?

YesNo

###

[Anchor to put-smart-collections-smart-collection-id-order?products[]=921728736&products[]=632910392-examples](/docs/api/admin-rest/latest/resources/smartcollection#put-smart-collections-smart-collection-id-order?products\[\]=921728736&products\[\]=632910392-examples)Examples

Update manually-sorted products in the smart collection

Query parameters

Update the type of ordering applied to the smart collection

Query parameters

sort_order=alpha-desc

default (current value)**default (current value)**

The type of sorting to apply. Valid values are listed in the Properties section above.

Was this section helpful?

YesNo

put

## /admin/api/2026-01/smart_collections/482865238/order.json?products[]=921728736&products[]=632910392

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections/482865238/order.json?products%5B%5D=921728736&products%5B%5D=632910392" \

-H "X-Shopify-Access-Token: {access_token}" \

-H "Content-Type: application/json"

{}

## Response

JSON

9

1

2

HTTP/1.1 200 OK

{}

### examples

  * #### Update manually-sorted products in the smart collection

#####

        curl -d '{}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections/482865238/order.json?products%5B%5D=921728736&products%5B%5D=632910392" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const smart_collection = new admin.rest.resources.SmartCollection({session: session});

        smart_collection.id = 482865238;
        await smart_collection.order({
          products: ["921728736", "632910392"],
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        smart_collection = ShopifyAPI::SmartCollection.new(session: test_session)
        smart_collection.id = 482865238
        smart_collection.order(
          session: test_session,
          products: ["921728736", "632910392"],
        )

#####

        // Session is built by the OAuth process

        const smart_collection = new shopify.rest.SmartCollection({session: session});
        smart_collection.id = 482865238;
        await smart_collection.order({
          products: ["921728736", "632910392"],
        });

#### response

        HTTP/1.1 200 OK{}

  * #### Update the type of ordering applied to the smart collection

#####

        curl -d '{}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections/482865238/order.json?sort_order=alpha-desc" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const smart_collection = new admin.rest.resources.SmartCollection({session: session});

        smart_collection.id = 482865238;
        await smart_collection.order({
          sort_order: "alpha-desc",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        smart_collection = ShopifyAPI::SmartCollection.new(session: test_session)
        smart_collection.id = 482865238
        smart_collection.order(
          session: test_session,
          sort_order: "alpha-desc",
        )

#####

        // Session is built by the OAuth process

        const smart_collection = new shopify.rest.SmartCollection({session: session});
        smart_collection.id = 482865238;
        await smart_collection.order({
          sort_order: "alpha-desc",
        });

#### response

        HTTP/1.1 200 OK{}


* * *

##

[Anchor to DELETE request, Removes a smart collection](/docs/api/admin-rest/latest/resources/smartcollection#delete-smart-collections-smart-collection-id)

del

Removes a smart collection

[collectionDelete](/docs/api/admin-graphql/latest/mutations/collectionDelete?example=removes-a-smart-collection)

Removes a smart collection

###

[Anchor to Parameters of Removes a smart collection](/docs/api/admin-rest/latest/resources/smartcollection#delete-smart-collections-smart-collection-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

smart_collection_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to delete-smart-collections-smart-collection-id-examples](/docs/api/admin-rest/latest/resources/smartcollection#delete-smart-collections-smart-collection-id-examples)Examples

Remove a smart collection

Path parameters

smart_collection_id=482865238

string**string**

required**required**

Was this section helpful?

YesNo

del

## /admin/api/2026-01/smart_collections/482865238.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections/482865238.json" \

-H "X-Shopify-Access-Token: {access_token}"

{}

## Response

JSON

9

1

2

HTTP/1.1 200 OK

{}

### examples

  * #### Remove a smart collection

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/smart_collections/482865238.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.SmartCollection.delete({
          session: session,
          id: 482865238,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::SmartCollection.delete(
          session: test_session,
          id: 482865238,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.SmartCollection.delete({
          session: session,
          id: 482865238,
        });

#### response

        HTTP/1.1 200 OK{}