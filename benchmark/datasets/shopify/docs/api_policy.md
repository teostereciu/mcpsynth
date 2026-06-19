# Policy

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/policy*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# Policy

Ask assistant

You can use the Policy resource to access the policies that a merchant has configured for their shop, such as their refund and privacy policies.

Only the shop owner can edit this information from the Shopify admin. The Policy resource lets you only retrieve information about a shop's policies.

Was this section helpful?

YesNo

#

## Endpoints

  * [get/admin/api/latest/policies.json](/docs/api/admin-rest/latest/resources/policy#get-policies)

Retrieves a list of the shop's policies

[shop](/docs/api/admin-graphql/latest/queries/shop?example=retrieves-a-list-of-the-shops-policies)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/policy#resource-object)

## The Policy resource

[Anchor to ](/docs/api/admin-rest/latest/resources/policy#resource-object-properties)

### Properties

* * *

title

->[title](/docs/api/admin-graphql/latest/objects/ShopPolicy#field-ShopPolicy.fields.title)

The name of the policy.

* * *

body

->[body](/docs/api/admin-graphql/latest/objects/ShopPolicy#field-ShopPolicy.fields.body)

A description of the policy.

* * *

url

->[url](/docs/api/admin-graphql/latest/objects/ShopPolicy#field-ShopPolicy.fields.url)

The public URL of the policy.

* * *

created_at

->[createdAt](/docs/api/admin-graphql/latest/objects/ShopPolicy#field-ShopPolicy.fields.createdAt)

The date and time ([ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601)) when the policy was created.

* * *

updated_at

->[updatedAt](/docs/api/admin-graphql/latest/objects/ShopPolicy#field-ShopPolicy.fields.updatedAt)

The date and time ([ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601)) when the policy was last modified.

* * *

handle

->[type](/docs/api/admin-graphql/latest/objects/ShopPolicy#field-ShopPolicy.fields.type)

A unique identifer for the policy used to build the policy's URL.

* * *

Was this section helpful?

YesNo

{}

## The Policy resource

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

{

"title": {

"title": "Refund Policy"

},

"body": {

"body": "You have 30 days to get a refund"

},

"url": {

"url": "https://jsmith.myshopify.com/548380009/policies/878590288"

},

"created_at": {

"created_at": "2012-02-15T15:12:21-05:00"

},

"updated_at": {

"updated_at": "2012-08-24T14:01:47-04:00"

},

"handle": {

"handle": "terms-of-service"

}

}

* * *

##

[Anchor to GET request, Retrieves a list of the shop's policies](/docs/api/admin-rest/latest/resources/policy#get-policies)

get

Retrieves a list of the shop's policies

[shop](/docs/api/admin-graphql/latest/queries/shop?example=retrieves-a-list-of-the-shops-policies)

Retrieves a list of the shop's policies

###

[Anchor to Parameters of Retrieves a list of the shop's policies](/docs/api/admin-rest/latest/resources/policy#get-policies-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-policies-examples](/docs/api/admin-rest/latest/resources/policy#get-policies-examples)Examples

Retrieve a list of the shop's policies

Was this section helpful?

YesNo

get

## /admin/api/2026-01/policies.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/policies.json" \

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

HTTP/1.1 200 OK

{

"policies": [

{

"body": "You have 30 days to get a refund",

"created_at": "2026-01-09T22:36:08-05:00",

"updated_at": "2026-01-09T22:36:08-05:00",

"handle": "refund-policy",

"title": "Refund policy",

"url": "https://jsmith.myshopify.com/548380009/policies/997884057"

}

]

}

### examples

  * #### Retrieve a list of the shop's policies

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/policies.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Policy.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Policy.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Policy.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"policies":[{"body":"You have 30 days to get a refund","created_at":"2026-01-09T22:36:08-05:00","updated_at":"2026-01-09T22:36:08-05:00","handle":"refund-policy","title":"Refund policy","url":"https://jsmith.myshopify.com/548380009/policies/997884057"}]}