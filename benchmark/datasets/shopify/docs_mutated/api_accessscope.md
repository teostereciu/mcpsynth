# AccessScope

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/accessscope*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# AccessScope

Ask assistant

The AccessScope resource allows you to retrieve the permissions that a merchant has granted to an app, such as `read_orders` and `write_products`. These permissions allow apps to access data from a shop, and are granted when a merchant installs the app or updates an existing installation of the app.

The list of access scopes retrieved is based on the access token for the request. It returns only those access scopes that are associated with the token.

For more information about access scopes, see the [access scopes API reference](https://shopify.dev/api/usage/access-scopes).

Note

If your app is already installed on a shop and you want the merchant to grant additional access scopes, you need to redirect the merchant to the app install page with the additional requested scopes. After a merchant installs the updated app, any subsequent calls made to the AccessScope resource will return the updated list of granted access scopes.

**Note:**

If your app is already installed on a shop and you want the merchant to grant additional access scopes, you need to redirect the merchant to the app install page with the additional requested scopes. After a merchant installs the updated app, any subsequent calls made to the AccessScope resource will return the updated list of granted access scopes.

Was this section helpful?

YesNo

#

## Endpoints

  * [get/admin/oauth/access_scopes.json](/docs/api/admin-rest/latest/resources/accessscope#get-admin-oauth-access-scopes)

Get a list of access scopes

[currentAppInstallation](/docs/api/admin-graphql/latest/queries/currentAppInstallation?example=get-a-list-of-access-scopes)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/accessscope#resource-object)

## The AccessScope resource

[Anchor to ](/docs/api/admin-rest/latest/resources/accessscope#resource-object-properties)

### Properties

* * *

access_scopes

->[accessScopes](/docs/api/admin-graphql/latest/objects/AppInstallation#field-AppInstallation.fields.accessScopes)

The list of access scopes associated with the access token.

* * *

Was this section helpful?

YesNo

{}

## The AccessScope resource

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

{

"access_scopes": [

{

"handle": "write_product_listings"

},

{

"handle": "read_shipping"

}

]

}

* * *

##

[Anchor to GET request, Get a list of access scopes](/docs/api/admin-rest/latest/resources/accessscope#get-admin-oauth-access-scopes)

get

Get a list of access scopes

[currentAppInstallation](/docs/api/admin-graphql/latest/queries/currentAppInstallation?example=get-a-list-of-access-scopes)

Retrieves a list of access scopes associated with the access token.

###

[Anchor to Parameters of Get a list of access scopes](/docs/api/admin-rest/latest/resources/accessscope#get-admin-oauth-access-scopes-parameters)Parameters

* * *

Was this section helpful?

YesNo

###

[Anchor to get-admin-oauth-access-scopes-examples](/docs/api/admin-rest/latest/resources/accessscope#get-admin-oauth-access-scopes-examples)Examples

List all scopes

Was this section helpful?

YesNo

get

## /admin/oauth/access_scopes.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/oauth/access_scopes.json" \

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

HTTP/1.1 200 OK

{

"access_scopes": [

{

"handle": "read_products"

},

{

"handle": "write_orders"

},

{

"handle": "read_orders"

}

]

}

### examples

  * #### List all scopes

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/oauth/access_scopes.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.AccessScope.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::AccessScope.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.AccessScope.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"access_scopes":[{"handle":"read_products"},{"handle":"write_orders"},{"handle":"read_orders"}]}