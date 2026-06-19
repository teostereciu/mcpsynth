# Metafield

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/metafield*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# Metafield

Ask assistant

Metafields are a flexible way to attach additional information to a Shopify resource (e.g. Product, Collection, etc.). Some examples of data stored using metafields include specifications, size charts, downloadable documents, release dates, images, or part numbers. Metafields are identified by an owner resource, a namespace, and a key and they store a value along with type information for that context.

## Resources that can have metafields

  * [Article](https://shopify.dev/api/admin-rest/latest/resources/article)
  * [Blog](https://shopify.dev/api/admin-rest/latest/resources/blog)
  * [Collection](https://shopify.dev/api/admin-rest/latest/resources/collection)
  * [Smart Collection](https://shopify.dev/api/admin-rest/latest/resources/smartcollection)
  * [Customer](https://shopify.dev/api/admin-rest/latest/resources/customer)
  * [Draft Order](https://shopify.dev/api/admin-rest/latest/resources/draftorder)
  * [Location](https://shopify.dev/api/admin-rest/latest/resources/location)
  * [Order](https://shopify.dev/api/admin-rest/latest/resources/order)
  * [Page](https://shopify.dev/api/admin-rest/latest/resources/page)
  * [Product](https://shopify.dev/api/admin-rest/latest/resources/product)
  * [Product Image](https://shopify.dev/api/admin-rest/latest/resources/product-image)
  * [Product Variant](https://shopify.dev/api/admin-rest/latest/resources/product-variant)
  * [Shop](https://shopify.dev/api/admin-rest/latest/resources/shop)


Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/blogs/{blog_id}/metafields.json](/docs/api/admin-rest/latest/resources/metafield#post-blogs-blog-id-metafields)

Create a metafield

[metafieldsSet](/docs/api/admin-graphql/latest/mutations/metafieldsSet?example=create-a-metafield)

  * [get/admin/api/latest/blogs/{blog_id}/metafields.json](/docs/api/admin-rest/latest/resources/metafield#get-blogs-blog-id-metafields)

Retrieve a list of metafields from the resource's endpoint

[product](/docs/api/admin-graphql/latest/queries/product)

  * [get/admin/api/latest/blogs/{blog_id}/metafields/{metafield_id}.json](/docs/api/admin-rest/latest/resources/metafield#get-blogs-blog-id-metafields-metafield-id)

Retrieve a specific metafield

[product](/docs/api/admin-graphql/latest/queries/product)

  * [get/admin/api/latest/blogs/{blog_id}/metafields/count.json](/docs/api/admin-rest/latest/resources/metafield#get-blogs-blog-id-metafields-count)

Retrieve a count of a resource's metafields.

[metafieldDefinition](/docs/api/admin-graphql/latest/queries/metafieldDefinition?example=retrieve-a-count-of-a-resources-metafields)

  * [put/admin/api/latest/blogs/{blog_id}/metafields/{metafield_id}.json](/docs/api/admin-rest/latest/resources/metafield#put-blogs-blog-id-metafields-metafield-id)

Updates a metafield

[metafieldsSet](/docs/api/admin-graphql/latest/mutations/metafieldsSet?example=updates-a-metafield)

  * [del/admin/api/latest/blogs/{blog_id}/metafields/{metafield_id}.json](/docs/api/admin-rest/latest/resources/metafield#delete-blogs-blog-id-metafields-metafield-id)

Deletes a metafield by its ID

[metafieldsDelete](/docs/api/admin-graphql/latest/mutations/metafieldsDelete?example=deletes-a-metafield-by-its-id)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/metafield#resource-object)

## The Metafield resource

[Anchor to ](/docs/api/admin-rest/latest/resources/metafield#resource-object-properties)

### Properties

* * *

created_at

read-only**read-only**

->[createdAt](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.createdAt)

The date and time ([ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601)) when the metafield was created.

* * *

description

->[description](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.description)

The description of the metafield.

* * *

id

read-only**read-only**

->[id](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.id)

The unique ID of the metafield.
Required when updating a metafield, but should not be included when creating as it's created automatically.

* * *

key

->[key](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.key)

The unique identifier for a metafield within its namespace.
Must be 3-64 characters long and can contain alphanumeric, hyphen, and underscore characters.

* * *

namespace

->[namespace](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.namespace)

The container for a group of metafields that the metafield is or will be associated with. Used in tandem with `key` to lookup a metafield on a resource, preventing conflicts with other metafields with the same `key`.
Must be 3-255 characters long and can contain alphanumeric, hyphen, and underscore characters.

* * *

owner_id

->[owner](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.owner)

The unique ID of the resource that the metafield is attached to.

* * *

owner_resource

->[ownerType](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.ownerType)

The type of resource that the metafield is attached to.

* * *

updated_at

read-only**read-only**

->[updatedAt](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.updatedAt)

The date and time ([ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601)) when the metafield was last updated.

* * *

value

->[value](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.value)

The data stored in the metafield. Always stored as a string, regardless of the metafield's type.

* * *

type

->[type](/docs/api/admin-graphql/latest/objects/Metafield#field-Metafield.fields.type)

The type of data that is stored in the metafield. Refer to the list of [supported types](/apps/metafields/types).

* * *

Was this section helpful?

YesNo

{}

## The Metafield resource

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

{

"created_at": "2012-03-13T16:09:54-04:00",

"description": "The number of units at the warehouse.",

"id": 915396206,

"key": "warehouse",

"namespace": "inventory",

"owner_id": 548380009,

"owner_resource": "product",

"updated_at": "2012-08-24T14:02:15-04:00",

"value": "25",

"type": "single_line_text_field"

}

* * *

##

[Anchor to POST request, Create a metafield](/docs/api/admin-rest/latest/resources/metafield#post-blogs-blog-id-metafields)

post

Create a metafield

[metafieldsSet](/docs/api/admin-graphql/latest/mutations/metafieldsSet?example=create-a-metafield)

You can create any number of metafields for a resource. To create metafields, use the corresponding resource's endpoint as listed on the examples.

###

[Anchor to Parameters of Create a metafield](/docs/api/admin-rest/latest/resources/metafield#post-blogs-blog-id-metafields-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

blog_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-blogs-blog-id-metafields-examples](/docs/api/admin-rest/latest/resources/metafield#post-blogs-blog-id-metafields-examples)Examples

Create a metafield for a blog

Path parameters

blog_id=382285388

string**string**

required**required**

Request body

metafield

Metafield resource**Metafield resource**

Show metafield properties

metafield.namespace:"my_fields"

->[namespace](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-namespace)

The container for a group of metafields that the metafield is or will be associated with. Used in tandem with `key` to lookup a metafield on a resource, preventing conflicts with other metafields with the same `key`.
Must be 3-255 characters long and can contain alphanumeric, hyphen, and underscore characters.

metafield.key:"sponsor"

->[key](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-key)

The unique identifier for a metafield within its namespace.
Must be 3-64 characters long and can contain alphanumeric, hyphen, and underscore characters.

metafield.type:"single_line_text_field"

->[type](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-type)

The type of data that is stored in the metafield. Refer to the list of [supported types](/apps/metafields/types).

metafield.value:"Shopify"

->[value](/docs/api/admin-graphql/latest/input-objects/MetafieldsSetInput#fields-value)

The data stored in the metafield. Always stored as a string, regardless of the metafield's type.

Create a metafield for a collection

Request body

metafield

Metafield resource**Metafield resource**

Show metafield properties

metafield.namespace:"my_fields"

->[namespace](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-namespace)

The container for a group of metafields that the metafield is or will be associated with. Used in tandem with `key` to lookup a metafield on a resource, preventing conflicts with other metafields with the same `key`.
Must be 3-255 characters long and can contain alphanumeric, hyphen, and underscore characters.

metafield.key:"discount"

->[key](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-key)

The unique identifier for a metafield within its namespace.
Must be 3-64 characters long and can contain alphanumeric, hyphen, and underscore characters.

metafield.type:"single_line_text_field"

->[type](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-type)

The type of data that is stored in the metafield. Refer to the list of [supported types](/apps/metafields/types).

metafield.value:"25%"

->[value](/docs/api/admin-graphql/latest/input-objects/MetafieldsSetInput#fields-value)

The data stored in the metafield. Always stored as a string, regardless of the metafield's type.

Create a metafield for a customer

Request body

metafield

Metafield resource**Metafield resource**

Show metafield properties

metafield.namespace:"discounts"

->[namespace](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-namespace)

The container for a group of metafields that the metafield is or will be associated with. Used in tandem with `key` to lookup a metafield on a resource, preventing conflicts with other metafields with the same `key`.
Must be 3-255 characters long and can contain alphanumeric, hyphen, and underscore characters.

metafield.key:"special"

->[key](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-key)

The unique identifier for a metafield within its namespace.
Must be 3-64 characters long and can contain alphanumeric, hyphen, and underscore characters.

metafield.value:"yes"

->[value](/docs/api/admin-graphql/latest/input-objects/MetafieldsSetInput#fields-value)

The data stored in the metafield. Always stored as a string, regardless of the metafield's type.

metafield.type:"single_line_text_field"

->[type](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-type)

The type of data that is stored in the metafield. Refer to the list of [supported types](/apps/metafields/types).

Create a metafield for a draft order

Request body

metafield

Metafield resource**Metafield resource**

Show metafield properties

metafield.namespace:"my_fields"

->[namespace](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-namespace)

The container for a group of metafields that the metafield is or will be associated with. Used in tandem with `key` to lookup a metafield on a resource, preventing conflicts with other metafields with the same `key`.
Must be 3-255 characters long and can contain alphanumeric, hyphen, and underscore characters.

metafield.key:"purchase_order"

->[key](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-key)

The unique identifier for a metafield within its namespace.
Must be 3-64 characters long and can contain alphanumeric, hyphen, and underscore characters.

metafield.type:"single_line_text_field"

->[type](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-type)

The type of data that is stored in the metafield. Refer to the list of [supported types](/apps/metafields/types).

metafield.value:"97453"

->[value](/docs/api/admin-graphql/latest/input-objects/MetafieldsSetInput#fields-value)

The data stored in the metafield. Always stored as a string, regardless of the metafield's type.

Create a metafield for a page

Request body

metafield

Metafield resource**Metafield resource**

Show metafield properties

metafield.namespace:"my_fields"

->[namespace](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-namespace)

The container for a group of metafields that the metafield is or will be associated with. Used in tandem with `key` to lookup a metafield on a resource, preventing conflicts with other metafields with the same `key`.
Must be 3-255 characters long and can contain alphanumeric, hyphen, and underscore characters.

metafield.key:"subtitle"

->[key](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-key)

The unique identifier for a metafield within its namespace.
Must be 3-64 characters long and can contain alphanumeric, hyphen, and underscore characters.

metafield.type:"single_line_text_field"

->[type](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-type)

The type of data that is stored in the metafield. Refer to the list of [supported types](/apps/metafields/types).

metafield.value:"A subtitle for my page"

->[value](/docs/api/admin-graphql/latest/input-objects/MetafieldsSetInput#fields-value)

The data stored in the metafield. Always stored as a string, regardless of the metafield's type.

Create a metafield for a product

Request body

metafield

Metafield resource**Metafield resource**

Show metafield properties

metafield.namespace:"inventory"

->[namespace](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-namespace)

The container for a group of metafields that the metafield is or will be associated with. Used in tandem with `key` to lookup a metafield on a resource, preventing conflicts with other metafields with the same `key`.
Must be 3-255 characters long and can contain alphanumeric, hyphen, and underscore characters.

metafield.key:"warehouse"

->[key](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-key)

The unique identifier for a metafield within its namespace.
Must be 3-64 characters long and can contain alphanumeric, hyphen, and underscore characters.

metafield.value:25

->[value](/docs/api/admin-graphql/latest/input-objects/MetafieldsSetInput#fields-value)

The data stored in the metafield. Always stored as a string, regardless of the metafield's type.

metafield.type:"number_integer"

->[type](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-type)

The type of data that is stored in the metafield. Refer to the list of [supported types](/apps/metafields/types).

Create a metafield for a product image

Request body

metafield

Metafield resource**Metafield resource**

Show metafield properties

metafield.namespace:"translation"

->[namespace](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-namespace)

The container for a group of metafields that the metafield is or will be associated with. Used in tandem with `key` to lookup a metafield on a resource, preventing conflicts with other metafields with the same `key`.
Must be 3-255 characters long and can contain alphanumeric, hyphen, and underscore characters.

metafield.key:"title_spanish"

->[key](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-key)

The unique identifier for a metafield within its namespace.
Must be 3-64 characters long and can contain alphanumeric, hyphen, and underscore characters.

metafield.type:"single_line_text_field"

->[type](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-type)

The type of data that is stored in the metafield. Refer to the list of [supported types](/apps/metafields/types).

metafield.value:"botas"

->[value](/docs/api/admin-graphql/latest/input-objects/MetafieldsSetInput#fields-value)

The data stored in the metafield. Always stored as a string, regardless of the metafield's type.

Create a metafield for a product variant

Request body

metafield

Metafield resource**Metafield resource**

Show metafield properties

metafield.namespace:"my_fields"

->[namespace](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-namespace)

The container for a group of metafields that the metafield is or will be associated with. Used in tandem with `key` to lookup a metafield on a resource, preventing conflicts with other metafields with the same `key`.
Must be 3-255 characters long and can contain alphanumeric, hyphen, and underscore characters.

metafield.key:"liner_material"

->[key](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-key)

The unique identifier for a metafield within its namespace.
Must be 3-64 characters long and can contain alphanumeric, hyphen, and underscore characters.

metafield.type:"single_line_text_field"

->[type](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-type)

The type of data that is stored in the metafield. Refer to the list of [supported types](/apps/metafields/types).

metafield.value:"synthetic leather"

->[value](/docs/api/admin-graphql/latest/input-objects/MetafieldsSetInput#fields-value)

The data stored in the metafield. Always stored as a string, regardless of the metafield's type.

Create a metafield for an article

Request body

metafield

Metafield resource**Metafield resource**

Show metafield properties

metafield.namespace:"my_fields"

->[namespace](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-namespace)

The container for a group of metafields that the metafield is or will be associated with. Used in tandem with `key` to lookup a metafield on a resource, preventing conflicts with other metafields with the same `key`.
Must be 3-255 characters long and can contain alphanumeric, hyphen, and underscore characters.

metafield.key:"category"

->[key](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-key)

The unique identifier for a metafield within its namespace.
Must be 3-64 characters long and can contain alphanumeric, hyphen, and underscore characters.

metafield.type:"single_line_text_field"

->[type](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-type)

The type of data that is stored in the metafield. Refer to the list of [supported types](/apps/metafields/types).

metafield.value:"outdoors"

->[value](/docs/api/admin-graphql/latest/input-objects/MetafieldsSetInput#fields-value)

The data stored in the metafield. Always stored as a string, regardless of the metafield's type.

Create a metafield for an order

Request body

metafield

Metafield resource**Metafield resource**

Show metafield properties

metafield.namespace:"my_fields"

->[namespace](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-namespace)

The container for a group of metafields that the metafield is or will be associated with. Used in tandem with `key` to lookup a metafield on a resource, preventing conflicts with other metafields with the same `key`.
Must be 3-255 characters long and can contain alphanumeric, hyphen, and underscore characters.

metafield.key:"purchase_order"

->[key](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-key)

The unique identifier for a metafield within its namespace.
Must be 3-64 characters long and can contain alphanumeric, hyphen, and underscore characters.

metafield.type:"single_line_text_field"

->[type](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-type)

The type of data that is stored in the metafield. Refer to the list of [supported types](/apps/metafields/types).

metafield.value:"123"

->[value](/docs/api/admin-graphql/latest/input-objects/MetafieldsSetInput#fields-value)

The data stored in the metafield. Always stored as a string, regardless of the metafield's type.

Create a metafield for the Shop resource

Request body

metafield

Metafield resource**Metafield resource**

Show metafield properties

metafield.namespace:"my_fields"

->[namespace](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-namespace)

The container for a group of metafields that the metafield is or will be associated with. Used in tandem with `key` to lookup a metafield on a resource, preventing conflicts with other metafields with the same `key`.
Must be 3-255 characters long and can contain alphanumeric, hyphen, and underscore characters.

metafield.key:"my_items"

->[key](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-key)

The unique identifier for a metafield within its namespace.
Must be 3-64 characters long and can contain alphanumeric, hyphen, and underscore characters.

metafield.value:"{\"items\":[\"some item\"]}"

->[value](/docs/api/admin-graphql/latest/input-objects/MetafieldsSetInput#fields-value)

The data stored in the metafield. Always stored as a string, regardless of the metafield's type.

metafield.type:"json"

->[type](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-type)

The type of data that is stored in the metafield. Refer to the list of [supported types](/apps/metafields/types).

Creating a metafield without a key will fail and return an error

Request body

metafield

Metafield resource**Metafield resource**

Show metafield properties

metafield.key:null

->[key](/docs/api/admin-graphql/latest/input-objects/MetafieldDefinitionInput#fields-key)

The unique identifier for a metafield within its namespace.
Must be 3-64 characters long and can contain alphanumeric, hyphen, and underscore characters.

Was this section helpful?

YesNo

post

## /admin/api/2026-01/blogs/382285388/metafields.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"metafield":{"namespace":"my_fields","key":"sponsor","type":"single_line_text_field","value":"Shopify"}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/blogs/382285388/metafields.json" \

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

HTTP/1.1 201 Created

{

"metafield": {

"id": 1069228999,

"namespace": "my_fields",

"key": "sponsor",

"value": "Shopify",

"description": null,

"owner_id": 382285388,

"created_at": "2026-01-09T19:17:34-05:00",

"updated_at": "2026-01-09T19:17:34-05:00",

"owner_resource": "blog",

"type": "single_line_text_field",

"admin_graphql_api_id": "gid://shopify/Metafield/1069228999"

}

}

### examples

  * #### Create a metafield for a blog

#####

        curl -d '{"metafield":{"namespace":"my_fields","key":"sponsor","type":"single_line_text_field","value":"Shopify"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/blogs/382285388/metafields.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const metafield = new admin.rest.resources.Metafield({session: session});

        metafield.blog_id = 382285388;
        metafield.namespace = "my_fields";
        metafield.key = "sponsor";
        metafield.type = "single_line_text_field";
        metafield.value = "Shopify";
        await metafield.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        metafield = ShopifyAPI::Metafield.new(session: test_session)
        metafield.blog_id = 382285388
        metafield.namespace = "my_fields"
        metafield.key = "sponsor"
        metafield.type = "single_line_text_field"
        metafield.value = "Shopify"
        metafield.save!

#####

        // Session is built by the OAuth process

        const metafield = new shopify.rest.Metafield({session: session});
        metafield.blog_id = 382285388;
        metafield.namespace = "my_fields";
        metafield.key = "sponsor";
        metafield.type = "single_line_text_field";
        metafield.value = "Shopify";
        await metafield.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"metafield":{"id":1069228999,"namespace":"my_fields","key":"sponsor","value":"Shopify","description":null,"owner_id":382285388,"created_at":"2026-01-09T19:17:34-05:00","updated_at":"2026-01-09T19:17:34-05:00","owner_resource":"blog","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/1069228999"}}

  * #### Create a metafield for a collection

#####

        curl -d '{"metafield":{"namespace":"my_fields","key":"discount","type":"single_line_text_field","value":"25%"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/collections/482865238/metafields.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const metafield = new admin.rest.resources.Metafield({session: session});

        metafield.collection_id = 482865238;
        metafield.namespace = "my_fields";
        metafield.key = "discount";
        metafield.type = "single_line_text_field";
        metafield.value = "25%";
        await metafield.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        metafield = ShopifyAPI::Metafield.new(session: test_session)
        metafield.collection_id = 482865238
        metafield.namespace = "my_fields"
        metafield.key = "discount"
        metafield.type = "single_line_text_field"
        metafield.value = "25%"
        metafield.save!

#####

        // Session is built by the OAuth process

        const metafield = new shopify.rest.Metafield({session: session});
        metafield.collection_id = 482865238;
        metafield.namespace = "my_fields";
        metafield.key = "discount";
        metafield.type = "single_line_text_field";
        metafield.value = "25%";
        await metafield.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"metafield":{"id":1069229007,"namespace":"my_fields","key":"discount","value":"25%","description":null,"owner_id":482865238,"created_at":"2026-01-09T19:33:27-05:00","updated_at":"2026-01-09T19:33:27-05:00","owner_resource":"collection","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/1069229007"}}

  * #### Create a metafield for a customer

#####

        curl -d '{"metafield":{"namespace":"discounts","key":"special","value":"yes","type":"single_line_text_field"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/metafields.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const metafield = new admin.rest.resources.Metafield({session: session});

        metafield.customer_id = 207119551;
        metafield.namespace = "discounts";
        metafield.key = "special";
        metafield.value = "yes";
        metafield.type = "single_line_text_field";
        await metafield.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        metafield = ShopifyAPI::Metafield.new(session: test_session)
        metafield.customer_id = 207119551
        metafield.namespace = "discounts"
        metafield.key = "special"
        metafield.value = "yes"
        metafield.type = "single_line_text_field"
        metafield.save!

#####

        // Session is built by the OAuth process

        const metafield = new shopify.rest.Metafield({session: session});
        metafield.customer_id = 207119551;
        metafield.namespace = "discounts";
        metafield.key = "special";
        metafield.value = "yes";
        metafield.type = "single_line_text_field";
        await metafield.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"metafield":{"id":1069229009,"namespace":"discounts","key":"special","value":"yes","description":null,"owner_id":207119551,"created_at":"2026-01-09T19:33:32-05:00","updated_at":"2026-01-09T19:33:32-05:00","owner_resource":"customer","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/1069229009"}}

  * #### Create a metafield for a draft order

#####

        curl -d '{"metafield":{"namespace":"my_fields","key":"purchase_order","type":"single_line_text_field","value":"97453"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders/622762746/metafields.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const metafield = new admin.rest.resources.Metafield({session: session});

        metafield.draft_order_id = 622762746;
        metafield.namespace = "my_fields";
        metafield.key = "purchase_order";
        metafield.type = "single_line_text_field";
        metafield.value = "97453";
        await metafield.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        metafield = ShopifyAPI::Metafield.new(session: test_session)
        metafield.draft_order_id = 622762746
        metafield.namespace = "my_fields"
        metafield.key = "purchase_order"
        metafield.type = "single_line_text_field"
        metafield.value = "97453"
        metafield.save!

#####

        // Session is built by the OAuth process

        const metafield = new shopify.rest.Metafield({session: session});
        metafield.draft_order_id = 622762746;
        metafield.namespace = "my_fields";
        metafield.key = "purchase_order";
        metafield.type = "single_line_text_field";
        metafield.value = "97453";
        await metafield.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"metafield":{"id":1069229003,"namespace":"my_fields","key":"purchase_order","value":"97453","description":null,"owner_id":622762746,"created_at":"2026-01-09T19:33:01-05:00","updated_at":"2026-01-09T19:33:01-05:00","owner_resource":"draft_order","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/1069229003"}}

  * #### Create a metafield for a page

#####

        curl -d '{"metafield":{"namespace":"my_fields","key":"subtitle","type":"single_line_text_field","value":"A subtitle for my page"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/pages/131092082/metafields.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const metafield = new admin.rest.resources.Metafield({session: session});

        metafield.page_id = 131092082;
        metafield.namespace = "my_fields";
        metafield.key = "subtitle";
        metafield.type = "single_line_text_field";
        metafield.value = "A subtitle for my page";
        await metafield.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        metafield = ShopifyAPI::Metafield.new(session: test_session)
        metafield.page_id = 131092082
        metafield.namespace = "my_fields"
        metafield.key = "subtitle"
        metafield.type = "single_line_text_field"
        metafield.value = "A subtitle for my page"
        metafield.save!

#####

        // Session is built by the OAuth process

        const metafield = new shopify.rest.Metafield({session: session});
        metafield.page_id = 131092082;
        metafield.namespace = "my_fields";
        metafield.key = "subtitle";
        metafield.type = "single_line_text_field";
        metafield.value = "A subtitle for my page";
        await metafield.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"metafield":{"id":1069229008,"namespace":"my_fields","key":"subtitle","value":"A subtitle for my page","description":null,"owner_id":131092082,"created_at":"2026-01-09T19:33:28-05:00","updated_at":"2026-01-09T19:33:28-05:00","owner_resource":"page","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/1069229008"}}

  * #### Create a metafield for a product

#####

        curl -d '{"metafield":{"namespace":"inventory","key":"warehouse","value":25,"type":"number_integer"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392/metafields.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const metafield = new admin.rest.resources.Metafield({session: session});

        metafield.product_id = 632910392;
        metafield.namespace = "inventory";
        metafield.key = "warehouse";
        metafield.value = 25;
        metafield.type = "number_integer";
        await metafield.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        metafield = ShopifyAPI::Metafield.new(session: test_session)
        metafield.product_id = 632910392
        metafield.namespace = "inventory"
        metafield.key = "warehouse"
        metafield.value = 25
        metafield.type = "number_integer"
        metafield.save!

#####

        // Session is built by the OAuth process

        const metafield = new shopify.rest.Metafield({session: session});
        metafield.product_id = 632910392;
        metafield.namespace = "inventory";
        metafield.key = "warehouse";
        metafield.value = 25;
        metafield.type = "number_integer";
        await metafield.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"metafield":{"id":1069229006,"namespace":"inventory","key":"warehouse","value":25,"description":null,"owner_id":632910392,"created_at":"2026-01-09T19:33:24-05:00","updated_at":"2026-01-09T19:33:24-05:00","owner_resource":"product","type":"number_integer","admin_graphql_api_id":"gid://shopify/Metafield/1069229006"}}

  * #### Create a metafield for a product image

#####

        curl -d '{"metafield":{"namespace":"translation","key":"title_spanish","type":"single_line_text_field","value":"botas"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/product_images/850703190/metafields.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const metafield = new admin.rest.resources.Metafield({session: session});

        metafield.product_image_id = 850703190;
        metafield.namespace = "translation";
        metafield.key = "title_spanish";
        metafield.type = "single_line_text_field";
        metafield.value = "botas";
        await metafield.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        metafield = ShopifyAPI::Metafield.new(session: test_session)
        metafield.product_image_id = 850703190
        metafield.namespace = "translation"
        metafield.key = "title_spanish"
        metafield.type = "single_line_text_field"
        metafield.value = "botas"
        metafield.save!

#####

        // Session is built by the OAuth process

        const metafield = new shopify.rest.Metafield({session: session});
        metafield.product_image_id = 850703190;
        metafield.namespace = "translation";
        metafield.key = "title_spanish";
        metafield.type = "single_line_text_field";
        metafield.value = "botas";
        await metafield.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"metafield":{"id":1069229012,"namespace":"translation","key":"title_spanish","value":"botas","description":null,"owner_id":850703190,"created_at":"2026-01-09T19:33:45-05:00","updated_at":"2026-01-09T19:33:45-05:00","owner_resource":"product_image","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/1069229012"}}

  * #### Create a metafield for a product variant

#####

        curl -d '{"metafield":{"namespace":"my_fields","key":"liner_material","type":"single_line_text_field","value":"synthetic leather"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/variants/49148385/metafields.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const metafield = new admin.rest.resources.Metafield({session: session});

        metafield.variant_id = 49148385;
        metafield.namespace = "my_fields";
        metafield.key = "liner_material";
        metafield.type = "single_line_text_field";
        metafield.value = "synthetic leather";
        await metafield.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        metafield = ShopifyAPI::Metafield.new(session: test_session)
        metafield.variant_id = 49148385
        metafield.namespace = "my_fields"
        metafield.key = "liner_material"
        metafield.type = "single_line_text_field"
        metafield.value = "synthetic leather"
        metafield.save!

#####

        // Session is built by the OAuth process

        const metafield = new shopify.rest.Metafield({session: session});
        metafield.variant_id = 49148385;
        metafield.namespace = "my_fields";
        metafield.key = "liner_material";
        metafield.type = "single_line_text_field";
        metafield.value = "synthetic leather";
        await metafield.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"metafield":{"id":1069228998,"namespace":"my_fields","key":"liner_material","value":"synthetic leather","description":null,"owner_id":49148385,"created_at":"2026-01-09T19:17:28-05:00","updated_at":"2026-01-09T19:17:28-05:00","owner_resource":"variant","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/1069228998"}}

  * #### Create a metafield for an article

#####

        curl -d '{"metafield":{"namespace":"my_fields","key":"category","type":"single_line_text_field","value":"outdoors"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/articles/674387490/metafields.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const metafield = new admin.rest.resources.Metafield({session: session});

        metafield.article_id = 674387490;
        metafield.namespace = "my_fields";
        metafield.key = "category";
        metafield.type = "single_line_text_field";
        metafield.value = "outdoors";
        await metafield.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        metafield = ShopifyAPI::Metafield.new(session: test_session)
        metafield.article_id = 674387490
        metafield.namespace = "my_fields"
        metafield.key = "category"
        metafield.type = "single_line_text_field"
        metafield.value = "outdoors"
        metafield.save!

#####

        // Session is built by the OAuth process

        const metafield = new shopify.rest.Metafield({session: session});
        metafield.article_id = 674387490;
        metafield.namespace = "my_fields";
        metafield.key = "category";
        metafield.type = "single_line_text_field";
        metafield.value = "outdoors";
        await metafield.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"metafield":{"id":1069228996,"namespace":"my_fields","key":"category","value":"outdoors","description":null,"owner_id":674387490,"created_at":"2026-01-09T19:17:17-05:00","updated_at":"2026-01-09T19:17:17-05:00","owner_resource":"article","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/1069228996"}}

  * #### Create a metafield for an order

#####

        curl -d '{"metafield":{"namespace":"my_fields","key":"purchase_order","type":"single_line_text_field","value":"123"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/metafields.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const metafield = new admin.rest.resources.Metafield({session: session});

        metafield.order_id = 450789469;
        metafield.namespace = "my_fields";
        metafield.key = "purchase_order";
        metafield.type = "single_line_text_field";
        metafield.value = "123";
        await metafield.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        metafield = ShopifyAPI::Metafield.new(session: test_session)
        metafield.order_id = 450789469
        metafield.namespace = "my_fields"
        metafield.key = "purchase_order"
        metafield.type = "single_line_text_field"
        metafield.value = "123"
        metafield.save!

#####

        // Session is built by the OAuth process

        const metafield = new shopify.rest.Metafield({session: session});
        metafield.order_id = 450789469;
        metafield.namespace = "my_fields";
        metafield.key = "purchase_order";
        metafield.type = "single_line_text_field";
        metafield.value = "123";
        await metafield.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"metafield":{"id":1069228994,"namespace":"my_fields","key":"purchase_order","value":"123","description":null,"owner_id":450789469,"created_at":"2026-01-09T19:17:14-05:00","updated_at":"2026-01-09T19:17:14-05:00","owner_resource":"order","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/1069228994"}}

  * #### Create a metafield for the Shop resource

#####

        curl -d '{"metafield":{"namespace":"my_fields","key":"my_items","value":"{\"items\":[\"some item\"]}","type":"json"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/metafields.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const metafield = new admin.rest.resources.Metafield({session: session});

        metafield.namespace = "my_fields";
        metafield.key = "my_items";
        metafield.value = "{\"items\":[\"some item\"]}";
        metafield.type = "json";
        await metafield.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        metafield = ShopifyAPI::Metafield.new(session: test_session)
        metafield.namespace = "my_fields"
        metafield.key = "my_items"
        metafield.value = "{\"items\":[\"some item\"]}"
        metafield.type = "json"
        metafield.save!

#####

        // Session is built by the OAuth process

        const metafield = new shopify.rest.Metafield({session: session});
        metafield.namespace = "my_fields";
        metafield.key = "my_items";
        metafield.value = "{\"items\":[\"some item\"]}";
        metafield.type = "json";
        await metafield.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"metafield":{"id":1069229002,"namespace":"my_fields","key":"my_items","value":"{\"items\":[\"some item\"]}","description":null,"owner_id":548380009,"created_at":"2026-01-09T19:17:41-05:00","updated_at":"2026-01-09T19:17:41-05:00","owner_resource":"shop","type":"json","admin_graphql_api_id":"gid://shopify/Metafield/1069229002"}}

  * #### Creating a metafield without a key will fail and return an error

#####

        curl -d '{"metafield":{"key":null}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/metafields.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const metafield = new admin.rest.resources.Metafield({session: session});

        metafield.key = null;
        await metafield.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        metafield = ShopifyAPI::Metafield.new(session: test_session)
        metafield.key = nil
        metafield.save!

#####

        // Session is built by the OAuth process

        const metafield = new shopify.rest.Metafield({session: session});
        metafield.key = null;
        await metafield.save({
          update: true,
        });

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":{"type":["can't be blank"],"namespace":["can't be blank","is too short (minimum is 3 characters)"],"key":["can't be blank","is too short (minimum is 2 characters)"]}}


* * *

##

[Anchor to GET request, Retrieve a list of metafields from the resource's endpoint](/docs/api/admin-rest/latest/resources/metafield#get-blogs-blog-id-metafields)

get

Retrieve a list of metafields from the resource's endpoint

[product](/docs/api/admin-graphql/latest/queries/product)

Retrieves a list of metafields attached to a particular resource by using the resource's endpoint.

###

[Anchor to Parameters of Retrieve a list of metafields from the resource's endpoint](/docs/api/admin-rest/latest/resources/metafield#get-blogs-blog-id-metafields-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

blog_id

string**string**

required**required**

* * *

created_at_max

Show metafields created before date (format: 2022-02-25T16:15:47-04:00)

* * *

created_after

Show metafields created after date (format: 2022-02-25T16:15:47-04:00)

* * *

fields

Retrieve only certain fields, specified by a comma-separated list of fields names.

* * *

key

Show metafields with given key

* * *

count

≤ 250**≤ 250**

default 50**default 50**

The maximum number of results to show on a page.

* * *

namespace

Show metafields with given namespace

* * *

after_id

Show metafields created after the specified ID.

* * *

type

The type of data that the metafield stores in the `value` field. Refer to the list of [supported types](/apps/metafields/types).

* * *

updated_at_max

Show metafields last updated before date (format: 2022-02-25T16:15:47-04:00)

* * *

updated_at_min

Show metafields last updated after date (format: 2022-02-25T16:15:47-04:00)

* * *

Was this section helpful?

YesNo

###

[Anchor to get-blogs-blog-id-metafields-examples](/docs/api/admin-rest/latest/resources/metafield#get-blogs-blog-id-metafields-examples)Examples

Retrieve metafields attached to a Blog

Path parameters

blog_id=382285388

string**string**

required**required**

Retrieve metafields attached to a Collection

Retrieve metafields attached to a Customer

Retrieve metafields attached to a Draft Order

Retrieve metafields attached to a Page

Retrieve metafields attached to a Product

Retrieve metafields attached to a Product Image

Retrieve metafields attached to a Product Variant

Retrieve metafields attached to an Article

Retrieve metafields attached to an Order

Retrieve metafields attached to the Shop

Retrieve metafields attached to the Shop after the specified ID

Query parameters

after_id=721389482

Show metafields created after the specified ID.

Was this section helpful?

YesNo

get

## /admin/api/2026-01/blogs/382285388/metafields.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/blogs/382285388/metafields.json" \

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

HTTP/1.1 200 OK

{

"metafields": [

{

"id": 1069228995,

"namespace": "my_fields",

"key": "sponsor",

"value": "Shopify",

"description": null,

"owner_id": 382285388,

"created_at": "2026-01-09T19:17:14-05:00",

"updated_at": "2026-01-09T19:17:14-05:00",

"owner_resource": "blog",

"type": "single_line_text_field",

"admin_graphql_api_id": "gid://shopify/Metafield/1069228995"

}

]

}

### examples

  * #### Retrieve metafields attached to a Blog

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/blogs/382285388/metafields.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.all({
          session: session,
          blog_id: 382285388,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.all(
          session: test_session,
          blog_id: 382285388,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.all({
          session: session,
          blog_id: 382285388,
        });

#### response

        HTTP/1.1 200 OK{"metafields":[{"id":1069228995,"namespace":"my_fields","key":"sponsor","value":"Shopify","description":null,"owner_id":382285388,"created_at":"2026-01-09T19:17:14-05:00","updated_at":"2026-01-09T19:17:14-05:00","owner_resource":"blog","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/1069228995"}]}

  * #### Retrieve metafields attached to a Collection

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/collections/482865238/metafields.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.all({
          session: session,
          collection_id: 482865238,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.all(
          session: test_session,
          collection_id: 482865238,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.all({
          session: session,
          collection_id: 482865238,
        });

#### response

        HTTP/1.1 200 OK{"metafields":[{"id":519046726,"namespace":"notes","key":"descriptionription","value":"Collection description","description":"Custom Collection notes","owner_id":482865238,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"collection","type":"multi_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/519046726"},{"id":624849518,"namespace":"global","key":"description_tag","value":"Some seo description value","description":null,"owner_id":482865238,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"collection","type":"multi_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/624849518"},{"id":1010236510,"namespace":"global","key":"title_tag","value":"Some seo title value","description":null,"owner_id":482865238,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"collection","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/1010236510"},{"id":1069229014,"namespace":"my_fields","key":"discount","value":"25%","description":null,"owner_id":482865238,"created_at":"2026-01-09T19:33:50-05:00","updated_at":"2026-01-09T19:33:50-05:00","owner_resource":"collection","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/1069229014"}]}

  * #### Retrieve metafields attached to a Customer

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/metafields.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.all({
          session: session,
          customer_id: 207119551,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.all(
          session: test_session,
          customer_id: 207119551,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.all({
          session: session,
          customer_id: 207119551,
        });

#### response

        HTTP/1.1 200 OK{"metafields":[{"id":220591908,"namespace":"discounts","key":"returning_customer","value":"no","description":"Customer deserves discount","owner_id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"customer","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/220591908"},{"id":1069229011,"namespace":"discounts","key":"special","value":"yes","description":null,"owner_id":207119551,"created_at":"2026-01-09T19:33:40-05:00","updated_at":"2026-01-09T19:33:40-05:00","owner_resource":"customer","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/1069229011"}]}

  * #### Retrieve metafields attached to a Draft Order

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders/622762746/metafields.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.all({
          session: session,
          draft_order_id: 622762746,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.all(
          session: test_session,
          draft_order_id: 622762746,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.all({
          session: session,
          draft_order_id: 622762746,
        });

#### response

        HTTP/1.1 200 OK{"metafields":[{"id":106172460,"namespace":"notes","key":"note","value":"B flat","description":"This is for notes","owner_id":622762746,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"draft_order","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/106172460"},{"id":1069229010,"namespace":"my_fields","key":"purchase_order","value":"97453","description":null,"owner_id":622762746,"created_at":"2026-01-09T19:33:36-05:00","updated_at":"2026-01-09T19:33:36-05:00","owner_resource":"draft_order","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/1069229010"}]}

  * #### Retrieve metafields attached to a Page

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/pages/131092082/metafields.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.all({
          session: session,
          page_id: 131092082,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.all(
          session: test_session,
          page_id: 131092082,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.all({
          session: session,
          page_id: 131092082,
        });

#### response

        HTTP/1.1 200 OK{"metafields":[{"id":290519330,"namespace":"translation","key":"title_fr","value":"Le TOS","description":"Page French title translation","owner_id":131092082,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"page","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/290519330"},{"id":1069228992,"namespace":"my_fields","key":"subtitle","value":"A subtitle for my page","description":null,"owner_id":131092082,"created_at":"2026-01-09T19:17:05-05:00","updated_at":"2026-01-09T19:17:05-05:00","owner_resource":"page","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/1069228992"}]}

  * #### Retrieve metafields attached to a Product

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392/metafields.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.all({
          session: session,
          product_id: 632910392,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.all(
          session: test_session,
          product_id: 632910392,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.all({
          session: session,
          product_id: 632910392,
        });

#### response

        HTTP/1.1 200 OK{"metafields":[{"id":51714266,"namespace":"my_namespace","key":"my_key","value":"Hello","description":null,"owner_id":632910392,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"product","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/51714266"},{"id":116539875,"namespace":"descriptors","key":"subtitle","value":"The best ipod","description":null,"owner_id":632910392,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"product","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/116539875"},{"id":263497237,"namespace":"installments","key":"disable","value":true,"description":null,"owner_id":632910392,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"product","type":"boolean","admin_graphql_api_id":"gid://shopify/Metafield/263497237"},{"id":273160493,"namespace":"facts","key":"isbn","value":"978-0-14-004259-7","description":null,"owner_id":632910392,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"product","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/273160493"},{"id":524118066,"namespace":"facts","key":"ean","value":"0123456789012","description":null,"owner_id":632910392,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"product","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/524118066"},{"id":543636738,"namespace":"reviews","key":"rating_count","value":1,"description":null,"owner_id":632910392,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"product","type":"number_integer","admin_graphql_api_id":"gid://shopify/Metafield/543636738"},{"id":572384404,"namespace":"reviews","key":"rating","value":"{\"value\": \"3.5\", \"scale_min\": \"1.0\", \"scale_max\": \"5.0\"}","description":null,"owner_id":632910392,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"product","type":"rating","admin_graphql_api_id":"gid://shopify/Metafield/572384404"},{"id":613330208,"namespace":"shopify_filter","key":"display","value":"retina","description":"This field keeps track of the type of display","owner_id":632910392,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"product","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/613330208"},{"id":779326701,"namespace":"facts","key":"upc","value":"012345678901","description":null,"owner_id":632910392,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"product","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/779326701"},{"id":845366454,"namespace":"translations","key":"title_fr","value":"produit","description":"French product title","owner_id":632910392,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"product","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/845366454"},{"id":861799889,"namespace":"my_other_fields","key":"organic","value":true,"description":null,"owner_id":632910392,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"product","type":"boolean","admin_graphql_api_id":"gid://shopify/Metafield/861799889"},{"id":870326793,"namespace":"descriptors","key":"care_guide","value":"Wash in cold water","description":null,"owner_id":632910392,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"product","type":null,"admin_graphql_api_id":"gid://shopify/Metafield/870326793"},{"id":908250163,"namespace":"my_other_fields","key":"shipping_policy","value":"Ships for free in Canada","description":null,"owner_id":632910392,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"product","type":"multi_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/908250163"},{"id":925288667,"namespace":"my_other_fields","key":"year_released","value":2019,"description":null,"owner_id":632910392,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"product","type":"number_integer","admin_graphql_api_id":"gid://shopify/Metafield/925288667"},{"id":1001077698,"namespace":"my_fields","key":"best_for","value":"travel","description":null,"owner_id":632910392,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"product","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/1001077698"},{"id":1029402048,"namespace":"my_other_fields","key":"ingredients","value":"[\"apple\", \"music\", \"u2\"]","description":null,"owner_id":632910392,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"product","type":"list.single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/1029402048"},{"id":1069229004,"namespace":"inventory","key":"warehouse","value":25,"description":null,"owner_id":632910392,"created_at":"2026-01-09T19:33:06-05:00","updated_at":"2026-01-09T19:33:06-05:00","owner_resource":"product","type":"number_integer","admin_graphql_api_id":"gid://shopify/Metafield/1069229004"}]}

  * #### Retrieve metafields attached to a Product Image

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/product_images/850703190/metafields.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.all({
          session: session,
          product_image_id: 850703190,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.all(
          session: test_session,
          product_image_id: 850703190,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.all({
          session: session,
          product_image_id: 850703190,
        });

#### response

        HTTP/1.1 200 OK{"metafields":[{"id":625663657,"namespace":"translation","key":"title_fr","value":"tbn","description":"French product image title","owner_id":498048120,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"media_image","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/625663657"},{"id":1069229001,"namespace":"translation","key":"title_spanish","value":"botas","description":null,"owner_id":498048120,"created_at":"2026-01-09T19:17:39-05:00","updated_at":"2026-01-09T19:17:39-05:00","owner_resource":"media_image","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/1069229001"}]}

  * #### Retrieve metafields attached to a Product Variant

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/variants/49148385/metafields.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.all({
          session: session,
          variant_id: 49148385,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.all(
          session: test_session,
          variant_id: 49148385,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.all({
          session: session,
          variant_id: 49148385,
        });

#### response

        HTTP/1.1 200 OK{"metafields":[{"id":1069229013,"namespace":"my_fields","key":"liner_material","value":"synthetic leather","description":null,"owner_id":49148385,"created_at":"2026-01-09T19:33:46-05:00","updated_at":"2026-01-09T19:33:46-05:00","owner_resource":"variant","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/1069229013"}]}

  * #### Retrieve metafields attached to an Article

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/articles/674387490/metafields.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.all({
          session: session,
          article_id: 674387490,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.all(
          session: test_session,
          article_id: 674387490,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.all({
          session: session,
          article_id: 674387490,
        });

#### response

        HTTP/1.1 200 OK{"metafields":[{"id":1069229005,"namespace":"my_fields","key":"category","value":"outdoors","description":null,"owner_id":674387490,"created_at":"2026-01-09T19:33:21-05:00","updated_at":"2026-01-09T19:33:21-05:00","owner_resource":"article","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/1069229005"}]}

  * #### Retrieve metafields attached to an Order

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/metafields.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.all({
          session: session,
          order_id: 450789469,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.all(
          session: test_session,
          order_id: 450789469,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.all({
          session: session,
          order_id: 450789469,
        });

#### response

        HTTP/1.1 200 OK{"metafields":[{"id":915396079,"namespace":"notes","key":"buyer","value":"Notes about this buyer","description":"This field is for buyer notes","owner_id":450789469,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"order","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/915396079"},{"id":1069228993,"namespace":"my_fields","key":"purchase_order","value":"123","description":null,"owner_id":450789469,"created_at":"2026-01-09T19:17:05-05:00","updated_at":"2026-01-09T19:17:05-05:00","owner_resource":"order","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/1069228993"}]}

  * #### Retrieve metafields attached to the Shop

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/metafields.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"metafields":[{"id":721389482,"namespace":"affiliates","key":"app_key","value":"app_key","description":null,"owner_id":548380009,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"shop","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/721389482"}]}

  * #### Retrieve metafields attached to the Shop after the specified ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/metafields.json?after_id=721389482" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.all({
          session: session,
          after_id: "721389482",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.all(
          session: test_session,
          after_id: "721389482",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.all({
          session: session,
          after_id: "721389482",
        });

#### response

        HTTP/1.1 200 OK{"metafields":[{"id":1069229000,"namespace":"my_fields","key":"my_items","value":"{\"items\":[\"some item\"]}","description":null,"owner_id":548380009,"created_at":"2026-01-09T19:17:38-05:00","updated_at":"2026-01-09T19:17:38-05:00","owner_resource":"shop","type":"json","admin_graphql_api_id":"gid://shopify/Metafield/1069229000"}]}


* * *

##

[Anchor to GET request, Retrieve a specific metafield](/docs/api/admin-rest/latest/resources/metafield#get-blogs-blog-id-metafields-metafield-id)

get

Retrieve a specific metafield

[product](/docs/api/admin-graphql/latest/queries/product)

Retrieve a metafield by specifying the ID. All fields of a metafield are returned unless specific fields are named.

###

[Anchor to Parameters of Retrieve a specific metafield](/docs/api/admin-rest/latest/resources/metafield#get-blogs-blog-id-metafields-metafield-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

blog_id

string**string**

required**required**

* * *

metafield_id

string**string**

required**required**

* * *

fields

Retrieve only certain fields, specified by a comma-separated list of fields names.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-blogs-blog-id-metafields-metafield-id-examples](/docs/api/admin-rest/latest/resources/metafield#get-blogs-blog-id-metafields-metafield-id-examples)Examples

Retrieve a single metafield by its ID attached to a Blog

Retrieve a single metafield by its ID attached to a Collection

Retrieve a single metafield by its ID attached to a Customer

Retrieve a single metafield by its ID attached to a Draft Order

Retrieve a single metafield by its ID attached to a Page

Retrieve a single metafield by its ID attached to a Product

Retrieve a single metafield by its ID attached to a Product Image

Retrieve a single metafield by its ID attached to a Product Variant

Retrieve a single metafield by its ID attached to an Article

Retrieve a single metafield by its ID attached to an Order

Retrieve a single metafield by its ID attached to the Shop resource

Was this section helpful?

YesNo

get

## /admin/api/2026-01/blogs/382285388/metafields/534526895.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/blogs/382285388/metafields/534526895.json" \

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

HTTP/1.1 200 OK

{

"metafield": {

"id": 534526895,

"namespace": "translation",

"key": "title_fr",

"value": "Le iPod",

"description": "Blog French title translation",

"owner_id": 241253187,

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T17:04:11-05:00",

"owner_resource": "blog",

"type": "single_line_text_field",

"admin_graphql_api_id": "gid://shopify/Metafield/534526895"

}

}

### examples

  * #### Retrieve a single metafield by its ID attached to a Blog

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/blogs/382285388/metafields/534526895.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.find({
          session: session,
          blog_id: 382285388,
          id: 534526895,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.find(
          session: test_session,
          blog_id: 382285388,
          id: 534526895,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.find({
          session: session,
          blog_id: 382285388,
          id: 534526895,
        });

#### response

        HTTP/1.1 200 OK{"metafield":{"id":534526895,"namespace":"translation","key":"title_fr","value":"Le iPod","description":"Blog French title translation","owner_id":241253187,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"blog","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/534526895"}}

  * #### Retrieve a single metafield by its ID attached to a Collection

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/collections/482865238/metafields/1010236510.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.find({
          session: session,
          collection_id: 482865238,
          id: 1010236510,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.find(
          session: test_session,
          collection_id: 482865238,
          id: 1010236510,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.find({
          session: session,
          collection_id: 482865238,
          id: 1010236510,
        });

#### response

        HTTP/1.1 200 OK{"metafield":{"id":1010236510,"namespace":"global","key":"title_tag","value":"Some seo title value","description":null,"owner_id":482865238,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"collection","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/1010236510"}}

  * #### Retrieve a single metafield by its ID attached to a Customer

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/metafields/220591908.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.find({
          session: session,
          customer_id: 207119551,
          id: 220591908,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.find(
          session: test_session,
          customer_id: 207119551,
          id: 220591908,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.find({
          session: session,
          customer_id: 207119551,
          id: 220591908,
        });

#### response

        HTTP/1.1 200 OK{"metafield":{"id":220591908,"namespace":"discounts","key":"returning_customer","value":"no","description":"Customer deserves discount","owner_id":207119551,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"customer","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/220591908"}}

  * #### Retrieve a single metafield by its ID attached to a Draft Order

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders/622762746/metafields/106172460.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.find({
          session: session,
          draft_order_id: 622762746,
          id: 106172460,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.find(
          session: test_session,
          draft_order_id: 622762746,
          id: 106172460,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.find({
          session: session,
          draft_order_id: 622762746,
          id: 106172460,
        });

#### response

        HTTP/1.1 200 OK{"metafield":{"id":106172460,"namespace":"notes","key":"note","value":"B flat","description":"This is for notes","owner_id":622762746,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"draft_order","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/106172460"}}

  * #### Retrieve a single metafield by its ID attached to a Page

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/pages/131092082/metafields/290519330.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.find({
          session: session,
          page_id: 131092082,
          id: 290519330,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.find(
          session: test_session,
          page_id: 131092082,
          id: 290519330,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.find({
          session: session,
          page_id: 131092082,
          id: 290519330,
        });

#### response

        HTTP/1.1 200 OK{"metafield":{"id":290519330,"namespace":"translation","key":"title_fr","value":"Le TOS","description":"Page French title translation","owner_id":131092082,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"page","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/290519330"}}

  * #### Retrieve a single metafield by its ID attached to a Product

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392/metafields/1001077698.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.find({
          session: session,
          product_id: 632910392,
          id: 1001077698,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.find(
          session: test_session,
          product_id: 632910392,
          id: 1001077698,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.find({
          session: session,
          product_id: 632910392,
          id: 1001077698,
        });

#### response

        HTTP/1.1 200 OK{"metafield":{"id":1001077698,"namespace":"my_fields","key":"best_for","value":"travel","description":null,"owner_id":632910392,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"product","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/1001077698"}}

  * #### Retrieve a single metafield by its ID attached to a Product Image

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/product_images/850703190/metafields/625663657.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.find({
          session: session,
          product_image_id: 850703190,
          id: 625663657,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.find(
          session: test_session,
          product_image_id: 850703190,
          id: 625663657,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.find({
          session: session,
          product_image_id: 850703190,
          id: 625663657,
        });

#### response

        HTTP/1.1 200 OK{"metafield":{"id":625663657,"namespace":"translation","key":"title_fr","value":"tbn","description":"French product image title","owner_id":498048120,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"media_image","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/625663657"}}

  * #### Retrieve a single metafield by its ID attached to a Product Variant

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/variants/49148385/metafields/323119633.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.find({
          session: session,
          variant_id: 49148385,
          id: 323119633,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.find(
          session: test_session,
          variant_id: 49148385,
          id: 323119633,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.find({
          session: session,
          variant_id: 49148385,
          id: 323119633,
        });

#### response

        HTTP/1.1 200 OK{"metafield":{"id":323119633,"namespace":"my_fields","key":"color","value":"Pink","description":null,"owner_id":808950810,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"variant","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/323119633"}}

  * #### Retrieve a single metafield by its ID attached to an Article

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/articles/674387490/metafields/838981074.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.find({
          session: session,
          article_id: 674387490,
          id: 838981074,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.find(
          session: test_session,
          article_id: 674387490,
          id: 838981074,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.find({
          session: session,
          article_id: 674387490,
          id: 838981074,
        });

#### response

        HTTP/1.1 200 OK{"metafield":{"id":838981074,"namespace":"translation","key":"title_fr","value":"Le Article","description":"Article French title translation","owner_id":134645308,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"article","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/838981074"}}

  * #### Retrieve a single metafield by its ID attached to an Order

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/metafields/915396079.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.find({
          session: session,
          order_id: 450789469,
          id: 915396079,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.find(
          session: test_session,
          order_id: 450789469,
          id: 915396079,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.find({
          session: session,
          order_id: 450789469,
          id: 915396079,
        });

#### response

        HTTP/1.1 200 OK{"metafield":{"id":915396079,"namespace":"notes","key":"buyer","value":"Notes about this buyer","description":"This field is for buyer notes","owner_id":450789469,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"order","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/915396079"}}

  * #### Retrieve a single metafield by its ID attached to the Shop resource

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/metafields/721389482.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.find({
          session: session,
          id: 721389482,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.find(
          session: test_session,
          id: 721389482,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.find({
          session: session,
          id: 721389482,
        });

#### response

        HTTP/1.1 200 OK{"metafield":{"id":721389482,"namespace":"affiliates","key":"app_key","value":"app_key","description":null,"owner_id":548380009,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T17:04:11-05:00","owner_resource":"shop","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/721389482"}}


* * *

##

[Anchor to GET request, Retrieve a count of a resource's metafields.](/docs/api/admin-rest/latest/resources/metafield#get-blogs-blog-id-metafields-count)

get

Retrieve a count of a resource's metafields.

[metafieldDefinition](/docs/api/admin-graphql/latest/queries/metafieldDefinition?example=retrieve-a-count-of-a-resources-metafields)

Get a count of all metafields that belong to a particular resource.

###

[Anchor to Parameters of Retrieve a count of a resource's metafields.](/docs/api/admin-rest/latest/resources/metafield#get-blogs-blog-id-metafields-count-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

blog_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-blogs-blog-id-metafields-count-examples](/docs/api/admin-rest/latest/resources/metafield#get-blogs-blog-id-metafields-count-examples)Examples

Retrieve a count of metafields attached to a Blog

Path parameters

blog_id=382285388

string**string**

required**required**

Retrieve a count of metafields attached to a Collection

Retrieve a count of metafields attached to a Customer

Retrieve a count of metafields attached to a Draft Order

Retrieve a count of metafields attached to a Page

Retrieve a count of metafields attached to a Product

Retrieve a count of metafields attached to a Product Image

Retrieve a count of metafields attached to a Product Variant

Retrieve a count of metafields attached to an Article

Retrieve a count of metafields attached to an Order

Retrieve a count of metafields attached to the Shop resource

Was this section helpful?

YesNo

get

## /admin/api/2026-01/blogs/382285388/metafields/count.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/blogs/382285388/metafields/count.json" \

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

"count": 0

}

### examples

  * #### Retrieve a count of metafields attached to a Blog

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/blogs/382285388/metafields/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.count({
          session: session,
          blog_id: 382285388,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.count(
          session: test_session,
          blog_id: 382285388,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.count({
          session: session,
          blog_id: 382285388,
        });

#### response

        HTTP/1.1 200 OK{"count":0}

  * #### Retrieve a count of metafields attached to a Collection

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/collections/482865238/metafields/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.count({
          session: session,
          collection_id: 482865238,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.count(
          session: test_session,
          collection_id: 482865238,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.count({
          session: session,
          collection_id: 482865238,
        });

#### response

        HTTP/1.1 200 OK{"count":3}

  * #### Retrieve a count of metafields attached to a Customer

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/metafields/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.count({
          session: session,
          customer_id: 207119551,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.count(
          session: test_session,
          customer_id: 207119551,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.count({
          session: session,
          customer_id: 207119551,
        });

#### response

        HTTP/1.1 200 OK{"count":1}

  * #### Retrieve a count of metafields attached to a Draft Order

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders/622762746/metafields/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.count({
          session: session,
          draft_order_id: 622762746,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.count(
          session: test_session,
          draft_order_id: 622762746,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.count({
          session: session,
          draft_order_id: 622762746,
        });

#### response

        HTTP/1.1 200 OK{"count":1}

  * #### Retrieve a count of metafields attached to a Page

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/pages/131092082/metafields/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.count({
          session: session,
          page_id: 131092082,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.count(
          session: test_session,
          page_id: 131092082,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.count({
          session: session,
          page_id: 131092082,
        });

#### response

        HTTP/1.1 200 OK{"count":1}

  * #### Retrieve a count of metafields attached to a Product

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392/metafields/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.count({
          session: session,
          product_id: 632910392,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.count(
          session: test_session,
          product_id: 632910392,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.count({
          session: session,
          product_id: 632910392,
        });

#### response

        HTTP/1.1 200 OK{"count":16}

  * #### Retrieve a count of metafields attached to a Product Image

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/product_images/850703190/metafields/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.count({
          session: session,
          product_image_id: 850703190,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.count(
          session: test_session,
          product_image_id: 850703190,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.count({
          session: session,
          product_image_id: 850703190,
        });

#### response

        HTTP/1.1 200 OK{"count":1}

  * #### Retrieve a count of metafields attached to a Product Variant

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/variants/49148385/metafields/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.count({
          session: session,
          variant_id: 49148385,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.count(
          session: test_session,
          variant_id: 49148385,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.count({
          session: session,
          variant_id: 49148385,
        });

#### response

        HTTP/1.1 200 OK{"count":0}

  * #### Retrieve a count of metafields attached to an Article

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/articles/674387490/metafields/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.count({
          session: session,
          article_id: 674387490,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.count(
          session: test_session,
          article_id: 674387490,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.count({
          session: session,
          article_id: 674387490,
        });

#### response

        HTTP/1.1 200 OK{"count":0}

  * #### Retrieve a count of metafields attached to an Order

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/metafields/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.count({
          session: session,
          order_id: 450789469,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.count(
          session: test_session,
          order_id: 450789469,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.count({
          session: session,
          order_id: 450789469,
        });

#### response

        HTTP/1.1 200 OK{"count":1}

  * #### Retrieve a count of metafields attached to the Shop resource

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/metafields/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.count({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.count(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.count({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"count":1}


* * *

##

[Anchor to PUT request, Updates a metafield](/docs/api/admin-rest/latest/resources/metafield#put-blogs-blog-id-metafields-metafield-id)

put

Updates a metafield

[metafieldsSet](/docs/api/admin-graphql/latest/mutations/metafieldsSet?example=updates-a-metafield)

Updates a metafield. The properties that can be updated are `value` and `type`.

###

[Anchor to Parameters of Updates a metafield](/docs/api/admin-rest/latest/resources/metafield#put-blogs-blog-id-metafields-metafield-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

blog_id

string**string**

required**required**

* * *

metafield_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to put-blogs-blog-id-metafields-metafield-id-examples](/docs/api/admin-rest/latest/resources/metafield#put-blogs-blog-id-metafields-metafield-id-examples)Examples

Update a metafield for a Blog

Request body

metafield

Metafield resource**Metafield resource**

Show metafield properties

metafield.id:534526895

read-only**read-only**

The unique ID of the metafield.
Required when updating a metafield, but should not be included when creating as it's created automatically.

metafield.value:"a translated blog title"

->[value](/docs/api/admin-graphql/latest/input-objects/MetafieldsSetInput#fields-value)

The data stored in the metafield. Always stored as a string, regardless of the metafield's type.

metafield.type:"single_line_text_field"

The type of data that is stored in the metafield. Refer to the list of [supported types](/apps/metafields/types).

Update a metafield for a Collection

Request body

metafield

Metafield resource**Metafield resource**

Show metafield properties

metafield.id:1010236510

read-only**read-only**

The unique ID of the metafield.
Required when updating a metafield, but should not be included when creating as it's created automatically.

metafield.value:"seo title"

->[value](/docs/api/admin-graphql/latest/input-objects/MetafieldsSetInput#fields-value)

The data stored in the metafield. Always stored as a string, regardless of the metafield's type.

metafield.type:"single_line_text_field"

The type of data that is stored in the metafield. Refer to the list of [supported types](/apps/metafields/types).

Update a metafield for a Customer

Request body

metafield

Metafield resource**Metafield resource**

Show metafield properties

metafield.id:220591908

read-only**read-only**

The unique ID of the metafield.
Required when updating a metafield, but should not be included when creating as it's created automatically.

metafield.value:"yes"

->[value](/docs/api/admin-graphql/latest/input-objects/MetafieldsSetInput#fields-value)

The data stored in the metafield. Always stored as a string, regardless of the metafield's type.

metafield.type:"single_line_text_field"

The type of data that is stored in the metafield. Refer to the list of [supported types](/apps/metafields/types).

Update a metafield for a Draft Order

Request body

metafield

Metafield resource**Metafield resource**

Show metafield properties

metafield.id:106172460

read-only**read-only**

The unique ID of the metafield.
Required when updating a metafield, but should not be included when creating as it's created automatically.

metafield.value:"110000"

->[value](/docs/api/admin-graphql/latest/input-objects/MetafieldsSetInput#fields-value)

The data stored in the metafield. Always stored as a string, regardless of the metafield's type.

metafield.type:"single_line_text_field"

The type of data that is stored in the metafield. Refer to the list of [supported types](/apps/metafields/types).

Update a metafield for a Page

Request body

metafield

Metafield resource**Metafield resource**

Show metafield properties

metafield.id:290519330

read-only**read-only**

The unique ID of the metafield.
Required when updating a metafield, but should not be included when creating as it's created automatically.

metafield.value:"An updated translation"

->[value](/docs/api/admin-graphql/latest/input-objects/MetafieldsSetInput#fields-value)

The data stored in the metafield. Always stored as a string, regardless of the metafield's type.

metafield.type:"single_line_text_field"

The type of data that is stored in the metafield. Refer to the list of [supported types](/apps/metafields/types).

Update a metafield for a Product

Request body

metafield

Metafield resource**Metafield resource**

Show metafield properties

metafield.id:1001077698

read-only**read-only**

The unique ID of the metafield.
Required when updating a metafield, but should not be included when creating as it's created automatically.

metafield.value:"having fun"

->[value](/docs/api/admin-graphql/latest/input-objects/MetafieldsSetInput#fields-value)

The data stored in the metafield. Always stored as a string, regardless of the metafield's type.

metafield.type:"single_line_text_field"

The type of data that is stored in the metafield. Refer to the list of [supported types](/apps/metafields/types).

Update a metafield for a Product Image

Request body

metafield

Metafield resource**Metafield resource**

Show metafield properties

metafield.id:625663657

read-only**read-only**

The unique ID of the metafield.
Required when updating a metafield, but should not be included when creating as it's created automatically.

metafield.value:"translated description"

->[value](/docs/api/admin-graphql/latest/input-objects/MetafieldsSetInput#fields-value)

The data stored in the metafield. Always stored as a string, regardless of the metafield's type.

metafield.type:"single_line_text_field"

The type of data that is stored in the metafield. Refer to the list of [supported types](/apps/metafields/types).

Update a metafield for a Product Variant

Request body

metafield

Metafield resource**Metafield resource**

Show metafield properties

metafield.id:323119633

read-only**read-only**

The unique ID of the metafield.
Required when updating a metafield, but should not be included when creating as it's created automatically.

metafield.value:"Red"

->[value](/docs/api/admin-graphql/latest/input-objects/MetafieldsSetInput#fields-value)

The data stored in the metafield. Always stored as a string, regardless of the metafield's type.

metafield.type:"single_line_text_field"

The type of data that is stored in the metafield. Refer to the list of [supported types](/apps/metafields/types).

Update a metafield for a Shop resource

Request body

metafield

Metafield resource**Metafield resource**

Show metafield properties

metafield.id:721389482

read-only**read-only**

The unique ID of the metafield.
Required when updating a metafield, but should not be included when creating as it's created automatically.

metafield.value:"[\"something new\"]"

->[value](/docs/api/admin-graphql/latest/input-objects/MetafieldsSetInput#fields-value)

The data stored in the metafield. Always stored as a string, regardless of the metafield's type.

metafield.type:"list.single_line_text_field"

The type of data that is stored in the metafield. Refer to the list of [supported types](/apps/metafields/types).

Update a metafield for an Article

Request body

metafield

Metafield resource**Metafield resource**

Show metafield properties

metafield.id:838981074

read-only**read-only**

The unique ID of the metafield.
Required when updating a metafield, but should not be included when creating as it's created automatically.

metafield.value:"a translated title"

->[value](/docs/api/admin-graphql/latest/input-objects/MetafieldsSetInput#fields-value)

The data stored in the metafield. Always stored as a string, regardless of the metafield's type.

metafield.type:"single_line_text_field"

The type of data that is stored in the metafield. Refer to the list of [supported types](/apps/metafields/types).

Update a metafield for an Order

Request body

metafield

Metafield resource**Metafield resource**

Show metafield properties

metafield.id:915396079

read-only**read-only**

The unique ID of the metafield.
Required when updating a metafield, but should not be included when creating as it's created automatically.

metafield.value:"Provided a discount code"

->[value](/docs/api/admin-graphql/latest/input-objects/MetafieldsSetInput#fields-value)

The data stored in the metafield. Always stored as a string, regardless of the metafield's type.

metafield.type:"single_line_text_field"

The type of data that is stored in the metafield. Refer to the list of [supported types](/apps/metafields/types).

Was this section helpful?

YesNo

put

## /admin/api/2026-01/blogs/382285388/metafields/534526895.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"metafield":{"id":534526895,"value":"a translated blog title","type":"single_line_text_field"}}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/blogs/382285388/metafields/534526895.json" \

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

HTTP/1.1 200 OK

{

"metafield": {

"value": "a translated blog title",

"owner_id": 241253187,

"description": "Blog French title translation",

"namespace": "translation",

"key": "title_fr",

"id": 534526895,

"created_at": "2026-01-09T17:04:11-05:00",

"updated_at": "2026-01-09T19:32:57-05:00",

"owner_resource": "blog",

"type": "single_line_text_field",

"admin_graphql_api_id": "gid://shopify/Metafield/534526895"

}

}

### examples

  * #### Update a metafield for a Blog

#####

        curl -d '{"metafield":{"id":534526895,"value":"a translated blog title","type":"single_line_text_field"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/blogs/382285388/metafields/534526895.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const metafield = new admin.rest.resources.Metafield({session: session});

        metafield.blog_id = 382285388;
        metafield.id = 534526895;
        metafield.value = "a translated blog title";
        metafield.type = "single_line_text_field";
        await metafield.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        metafield = ShopifyAPI::Metafield.new(session: test_session)
        metafield.blog_id = 382285388
        metafield.id = 534526895
        metafield.value = "a translated blog title"
        metafield.type = "single_line_text_field"
        metafield.save!

#####

        // Session is built by the OAuth process

        const metafield = new shopify.rest.Metafield({session: session});
        metafield.blog_id = 382285388;
        metafield.id = 534526895;
        metafield.value = "a translated blog title";
        metafield.type = "single_line_text_field";
        await metafield.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"metafield":{"value":"a translated blog title","owner_id":241253187,"description":"Blog French title translation","namespace":"translation","key":"title_fr","id":534526895,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T19:32:57-05:00","owner_resource":"blog","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/534526895"}}

  * #### Update a metafield for a Collection

#####

        curl -d '{"metafield":{"id":1010236510,"value":"seo title","type":"single_line_text_field"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/collections/482865238/metafields/1010236510.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const metafield = new admin.rest.resources.Metafield({session: session});

        metafield.collection_id = 482865238;
        metafield.id = 1010236510;
        metafield.value = "seo title";
        metafield.type = "single_line_text_field";
        await metafield.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        metafield = ShopifyAPI::Metafield.new(session: test_session)
        metafield.collection_id = 482865238
        metafield.id = 1010236510
        metafield.value = "seo title"
        metafield.type = "single_line_text_field"
        metafield.save!

#####

        // Session is built by the OAuth process

        const metafield = new shopify.rest.Metafield({session: session});
        metafield.collection_id = 482865238;
        metafield.id = 1010236510;
        metafield.value = "seo title";
        metafield.type = "single_line_text_field";
        await metafield.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"metafield":{"value":"seo title","owner_id":482865238,"description":null,"namespace":"global","key":"title_tag","id":1010236510,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T19:32:59-05:00","owner_resource":"collection","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/1010236510"}}

  * #### Update a metafield for a Customer

#####

        curl -d '{"metafield":{"id":220591908,"value":"yes","type":"single_line_text_field"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/metafields/220591908.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const metafield = new admin.rest.resources.Metafield({session: session});

        metafield.customer_id = 207119551;
        metafield.id = 220591908;
        metafield.value = "yes";
        metafield.type = "single_line_text_field";
        await metafield.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        metafield = ShopifyAPI::Metafield.new(session: test_session)
        metafield.customer_id = 207119551
        metafield.id = 220591908
        metafield.value = "yes"
        metafield.type = "single_line_text_field"
        metafield.save!

#####

        // Session is built by the OAuth process

        const metafield = new shopify.rest.Metafield({session: session});
        metafield.customer_id = 207119551;
        metafield.id = 220591908;
        metafield.value = "yes";
        metafield.type = "single_line_text_field";
        await metafield.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"metafield":{"value":"yes","owner_id":207119551,"description":"Customer deserves discount","namespace":"discounts","key":"returning_customer","id":220591908,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T19:33:29-05:00","owner_resource":"customer","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/220591908"}}

  * #### Update a metafield for a Draft Order

#####

        curl -d '{"metafield":{"id":106172460,"value":"110000","type":"single_line_text_field"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders/622762746/metafields/106172460.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const metafield = new admin.rest.resources.Metafield({session: session});

        metafield.draft_order_id = 622762746;
        metafield.id = 106172460;
        metafield.value = "110000";
        metafield.type = "single_line_text_field";
        await metafield.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        metafield = ShopifyAPI::Metafield.new(session: test_session)
        metafield.draft_order_id = 622762746
        metafield.id = 106172460
        metafield.value = "110000"
        metafield.type = "single_line_text_field"
        metafield.save!

#####

        // Session is built by the OAuth process

        const metafield = new shopify.rest.Metafield({session: session});
        metafield.draft_order_id = 622762746;
        metafield.id = 106172460;
        metafield.value = "110000";
        metafield.type = "single_line_text_field";
        await metafield.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"metafield":{"value":"110000","owner_id":622762746,"description":"This is for notes","namespace":"notes","key":"note","id":106172460,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T19:33:26-05:00","owner_resource":"draft_order","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/106172460"}}

  * #### Update a metafield for a Page

#####

        curl -d '{"metafield":{"id":290519330,"value":"An updated translation","type":"single_line_text_field"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/pages/131092082/metafields/290519330.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const metafield = new admin.rest.resources.Metafield({session: session});

        metafield.page_id = 131092082;
        metafield.id = 290519330;
        metafield.value = "An updated translation";
        metafield.type = "single_line_text_field";
        await metafield.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        metafield = ShopifyAPI::Metafield.new(session: test_session)
        metafield.page_id = 131092082
        metafield.id = 290519330
        metafield.value = "An updated translation"
        metafield.type = "single_line_text_field"
        metafield.save!

#####

        // Session is built by the OAuth process

        const metafield = new shopify.rest.Metafield({session: session});
        metafield.page_id = 131092082;
        metafield.id = 290519330;
        metafield.value = "An updated translation";
        metafield.type = "single_line_text_field";
        await metafield.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"metafield":{"value":"An updated translation","owner_id":131092082,"description":"Page French title translation","namespace":"translation","key":"title_fr","id":290519330,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T19:17:16-05:00","owner_resource":"page","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/290519330"}}

  * #### Update a metafield for a Product

#####

        curl -d '{"metafield":{"id":1001077698,"value":"having fun","type":"single_line_text_field"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392/metafields/1001077698.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const metafield = new admin.rest.resources.Metafield({session: session});

        metafield.product_id = 632910392;
        metafield.id = 1001077698;
        metafield.value = "having fun";
        metafield.type = "single_line_text_field";
        await metafield.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        metafield = ShopifyAPI::Metafield.new(session: test_session)
        metafield.product_id = 632910392
        metafield.id = 1001077698
        metafield.value = "having fun"
        metafield.type = "single_line_text_field"
        metafield.save!

#####

        // Session is built by the OAuth process

        const metafield = new shopify.rest.Metafield({session: session});
        metafield.product_id = 632910392;
        metafield.id = 1001077698;
        metafield.value = "having fun";
        metafield.type = "single_line_text_field";
        await metafield.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"metafield":{"value":"having fun","owner_id":632910392,"description":null,"namespace":"my_fields","key":"best_for","id":1001077698,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T19:17:21-05:00","owner_resource":"product","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/1001077698"}}

  * #### Update a metafield for a Product Image

#####

        curl -d '{"metafield":{"id":625663657,"value":"translated description","type":"single_line_text_field"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/product_images/850703190/metafields/625663657.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const metafield = new admin.rest.resources.Metafield({session: session});

        metafield.product_image_id = 850703190;
        metafield.id = 625663657;
        metafield.value = "translated description";
        metafield.type = "single_line_text_field";
        await metafield.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        metafield = ShopifyAPI::Metafield.new(session: test_session)
        metafield.product_image_id = 850703190
        metafield.id = 625663657
        metafield.value = "translated description"
        metafield.type = "single_line_text_field"
        metafield.save!

#####

        // Session is built by the OAuth process

        const metafield = new shopify.rest.Metafield({session: session});
        metafield.product_image_id = 850703190;
        metafield.id = 625663657;
        metafield.value = "translated description";
        metafield.type = "single_line_text_field";
        await metafield.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"metafield":{"value":"translated description","owner_id":498048120,"description":"French product image title","namespace":"translation","key":"title_fr","id":625663657,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T19:33:34-05:00","owner_resource":"media_image","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/625663657"}}

  * #### Update a metafield for a Product Variant

#####

        curl -d '{"metafield":{"id":323119633,"value":"Red","type":"single_line_text_field"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/variants/49148385/metafields/323119633.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const metafield = new admin.rest.resources.Metafield({session: session});

        metafield.variant_id = 49148385;
        metafield.id = 323119633;
        metafield.value = "Red";
        metafield.type = "single_line_text_field";
        await metafield.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        metafield = ShopifyAPI::Metafield.new(session: test_session)
        metafield.variant_id = 49148385
        metafield.id = 323119633
        metafield.value = "Red"
        metafield.type = "single_line_text_field"
        metafield.save!

#####

        // Session is built by the OAuth process

        const metafield = new shopify.rest.Metafield({session: session});
        metafield.variant_id = 49148385;
        metafield.id = 323119633;
        metafield.value = "Red";
        metafield.type = "single_line_text_field";
        await metafield.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"metafield":{"value":"Red","owner_id":808950810,"description":null,"namespace":"my_fields","key":"color","id":323119633,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T19:17:13-05:00","owner_resource":"variant","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/323119633"}}

  * #### Update a metafield for a Shop resource

#####

        curl -d '{"metafield":{"id":721389482,"value":"[\"something new\"]","type":"list.single_line_text_field"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/metafields/721389482.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const metafield = new admin.rest.resources.Metafield({session: session});

        metafield.id = 721389482;
        metafield.value = "[\"something new\"]";
        metafield.type = "list.single_line_text_field";
        await metafield.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        metafield = ShopifyAPI::Metafield.new(session: test_session)
        metafield.id = 721389482
        metafield.value = "[\"something new\"]"
        metafield.type = "list.single_line_text_field"
        metafield.save!

#####

        // Session is built by the OAuth process

        const metafield = new shopify.rest.Metafield({session: session});
        metafield.id = 721389482;
        metafield.value = "[\"something new\"]";
        metafield.type = "list.single_line_text_field";
        await metafield.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"metafield":{"value":"[\"something new\"]","owner_id":548380009,"description":null,"namespace":"affiliates","key":"app_key","id":721389482,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T19:33:12-05:00","owner_resource":"shop","type":"list.single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/721389482"}}

  * #### Update a metafield for an Article

#####

        curl -d '{"metafield":{"id":838981074,"value":"a translated title","type":"single_line_text_field"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/articles/674387490/metafields/838981074.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const metafield = new admin.rest.resources.Metafield({session: session});

        metafield.article_id = 674387490;
        metafield.id = 838981074;
        metafield.value = "a translated title";
        metafield.type = "single_line_text_field";
        await metafield.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        metafield = ShopifyAPI::Metafield.new(session: test_session)
        metafield.article_id = 674387490
        metafield.id = 838981074
        metafield.value = "a translated title"
        metafield.type = "single_line_text_field"
        metafield.save!

#####

        // Session is built by the OAuth process

        const metafield = new shopify.rest.Metafield({session: session});
        metafield.article_id = 674387490;
        metafield.id = 838981074;
        metafield.value = "a translated title";
        metafield.type = "single_line_text_field";
        await metafield.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"metafield":{"value":"a translated title","owner_id":134645308,"description":"Article French title translation","namespace":"translation","key":"title_fr","id":838981074,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T19:17:18-05:00","owner_resource":"article","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/838981074"}}

  * #### Update a metafield for an Order

#####

        curl -d '{"metafield":{"id":915396079,"value":"Provided a discount code","type":"single_line_text_field"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/metafields/915396079.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const metafield = new admin.rest.resources.Metafield({session: session});

        metafield.order_id = 450789469;
        metafield.id = 915396079;
        metafield.value = "Provided a discount code";
        metafield.type = "single_line_text_field";
        await metafield.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        metafield = ShopifyAPI::Metafield.new(session: test_session)
        metafield.order_id = 450789469
        metafield.id = 915396079
        metafield.value = "Provided a discount code"
        metafield.type = "single_line_text_field"
        metafield.save!

#####

        // Session is built by the OAuth process

        const metafield = new shopify.rest.Metafield({session: session});
        metafield.order_id = 450789469;
        metafield.id = 915396079;
        metafield.value = "Provided a discount code";
        metafield.type = "single_line_text_field";
        await metafield.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"metafield":{"value":"Provided a discount code","owner_id":450789469,"description":"This field is for buyer notes","namespace":"notes","key":"buyer","id":915396079,"created_at":"2026-01-09T17:04:11-05:00","updated_at":"2026-01-09T19:17:30-05:00","owner_resource":"order","type":"single_line_text_field","admin_graphql_api_id":"gid://shopify/Metafield/915396079"}}


* * *

##

[Anchor to DELETE request, Deletes a metafield by its ID](/docs/api/admin-rest/latest/resources/metafield#delete-blogs-blog-id-metafields-metafield-id)

del

Deletes a metafield by its ID

[metafieldsDelete](/docs/api/admin-graphql/latest/mutations/metafieldsDelete?example=deletes-a-metafield-by-its-id)

Deletes a metafield by its ID.

###

[Anchor to Parameters of Deletes a metafield by its ID](/docs/api/admin-rest/latest/resources/metafield#delete-blogs-blog-id-metafields-metafield-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

blog_id

string**string**

required**required**

* * *

metafield_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to delete-blogs-blog-id-metafields-metafield-id-examples](/docs/api/admin-rest/latest/resources/metafield#delete-blogs-blog-id-metafields-metafield-id-examples)Examples

Delete a metafield by its ID for a Blog

Delete a metafield by its ID for a Collection

Delete a metafield by its ID for a Customer

Delete a metafield by its ID for a Draft Order

Delete a metafield by its ID for a Page

Delete a metafield by its ID for a Product

Delete a metafield by its ID for a Product Image

Delete a metafield by its ID for a Product Variant

Delete a metafield by its ID for an Article

Delete a metafield by its ID for an Order

Delete a metafield by its ID for the Shop resource

Was this section helpful?

YesNo

del

## /admin/api/2026-01/blogs/382285388/metafields/534526895.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/blogs/382285388/metafields/534526895.json" \

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

  * #### Delete a metafield by its ID for a Blog

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/blogs/382285388/metafields/534526895.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.delete({
          session: session,
          blog_id: 382285388,
          id: 534526895,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.delete(
          session: test_session,
          blog_id: 382285388,
          id: 534526895,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.delete({
          session: session,
          blog_id: 382285388,
          id: 534526895,
        });

#### response

        HTTP/1.1 200 OK{}

  * #### Delete a metafield by its ID for a Collection

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/collections/482865238/metafields/1010236510.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.delete({
          session: session,
          collection_id: 482865238,
          id: 1010236510,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.delete(
          session: test_session,
          collection_id: 482865238,
          id: 1010236510,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.delete({
          session: session,
          collection_id: 482865238,
          id: 1010236510,
        });

#### response

        HTTP/1.1 200 OK{}

  * #### Delete a metafield by its ID for a Customer

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/customers/207119551/metafields/220591908.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.delete({
          session: session,
          customer_id: 207119551,
          id: 220591908,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.delete(
          session: test_session,
          customer_id: 207119551,
          id: 220591908,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.delete({
          session: session,
          customer_id: 207119551,
          id: 220591908,
        });

#### response

        HTTP/1.1 200 OK{}

  * #### Delete a metafield by its ID for a Draft Order

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/draft_orders/622762746/metafields/106172460.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.delete({
          session: session,
          draft_order_id: 622762746,
          id: 106172460,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.delete(
          session: test_session,
          draft_order_id: 622762746,
          id: 106172460,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.delete({
          session: session,
          draft_order_id: 622762746,
          id: 106172460,
        });

#### response

        HTTP/1.1 200 OK{}

  * #### Delete a metafield by its ID for a Page

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/pages/131092082/metafields/290519330.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.delete({
          session: session,
          page_id: 131092082,
          id: 290519330,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.delete(
          session: test_session,
          page_id: 131092082,
          id: 290519330,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.delete({
          session: session,
          page_id: 131092082,
          id: 290519330,
        });

#### response

        HTTP/1.1 200 OK{}

  * #### Delete a metafield by its ID for a Product

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/products/632910392/metafields/1001077698.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.delete({
          session: session,
          product_id: 632910392,
          id: 1001077698,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.delete(
          session: test_session,
          product_id: 632910392,
          id: 1001077698,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.delete({
          session: session,
          product_id: 632910392,
          id: 1001077698,
        });

#### response

        HTTP/1.1 200 OK{}

  * #### Delete a metafield by its ID for a Product Image

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/product_images/850703190/metafields/625663657.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.delete({
          session: session,
          product_image_id: 850703190,
          id: 625663657,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.delete(
          session: test_session,
          product_image_id: 850703190,
          id: 625663657,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.delete({
          session: session,
          product_image_id: 850703190,
          id: 625663657,
        });

#### response

        HTTP/1.1 200 OK{}

  * #### Delete a metafield by its ID for a Product Variant

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/variants/49148385/metafields/323119633.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.delete({
          session: session,
          variant_id: 49148385,
          id: 323119633,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.delete(
          session: test_session,
          variant_id: 49148385,
          id: 323119633,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.delete({
          session: session,
          variant_id: 49148385,
          id: 323119633,
        });

#### response

        HTTP/1.1 200 OK{}

  * #### Delete a metafield by its ID for an Article

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/articles/674387490/metafields/838981074.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.delete({
          session: session,
          article_id: 674387490,
          id: 838981074,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.delete(
          session: test_session,
          article_id: 674387490,
          id: 838981074,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.delete({
          session: session,
          article_id: 674387490,
          id: 838981074,
        });

#### response

        HTTP/1.1 200 OK{}

  * #### Delete a metafield by its ID for an Order

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/orders/450789469/metafields/915396079.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.delete({
          session: session,
          order_id: 450789469,
          id: 915396079,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.delete(
          session: test_session,
          order_id: 450789469,
          id: 915396079,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.delete({
          session: session,
          order_id: 450789469,
          id: 915396079,
        });

#### response

        HTTP/1.1 200 OK{}

  * #### Delete a metafield by its ID for the Shop resource

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/metafields/721389482.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Metafield.delete({
          session: session,
          id: 721389482,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Metafield.delete(
          session: test_session,
          id: 721389482,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Metafield.delete({
          session: session,
          id: 721389482,
        });

#### response

        HTTP/1.1 200 OK{}