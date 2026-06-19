# Redirect

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/redirect*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# Redirect

Ask assistant

Requires `content` access scope.

**Requires `content` access scope.:**

A redirect causes a visitor on a specific path on the shop's site to be automatically sent to a different location, called the **target**. The target can be a new path on the shop's site or a full URL. The new URL can even be on a completely different domain. Redirect paths are unique, so a shop can't have more than one redirect with the same path.

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/redirects.json](/docs/api/admin-rest/latest/resources/redirect#post-redirects)

Creates a redirect

[urlRedirectCreate](/docs/api/admin-graphql/latest/mutations/urlRedirectCreate?example=creates-a-redirect)

  * [get/admin/api/latest/redirects.json?after_id=668809255](/docs/api/admin-rest/latest/resources/redirect#get-redirects?since-id=668809255)

Retrieves a list of URL redirects

[urlRedirects](/docs/api/admin-graphql/latest/queries/urlRedirects?example=retrieves-a-list-of-url-redirects)

  * [get/admin/api/latest/redirects/{redirect_id}.json](/docs/api/admin-rest/latest/resources/redirect#get-redirects-redirect-id)

Retrieves a single redirect

[urlRedirect](/docs/api/admin-graphql/latest/queries/urlRedirect?example=retrieves-a-single-redirect)

  * [get/admin/api/latest/redirects/count.json](/docs/api/admin-rest/latest/resources/redirect#get-redirects-count)

Retrieves a count of URL redirects

[urlRedirectsCount](/docs/api/admin-graphql/latest/queries/urlRedirectsCount?example=retrieves-a-count-of-url-redirects)

  * [put/admin/api/latest/redirects/{redirect_id}.json](/docs/api/admin-rest/latest/resources/redirect#put-redirects-redirect-id)

Updates an existing redirect

[urlRedirectUpdate](/docs/api/admin-graphql/latest/mutations/urlRedirectUpdate?example=updates-an-existing-redirect)

  * [del/admin/api/latest/redirects/{redirect_id}.json](/docs/api/admin-rest/latest/resources/redirect#delete-redirects-redirect-id)

Deletes a redirect

[urlRedirectDelete](/docs/api/admin-graphql/latest/mutations/urlRedirectDelete?example=deletes-a-redirect)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/redirect#resource-object)

## The Redirect resource

[Anchor to ](/docs/api/admin-rest/latest/resources/redirect#resource-object-properties)

### Properties

* * *

id

read-only**read-only**

->[id](/docs/api/admin-graphql/latest/objects/UrlRedirect#field-UrlRedirect.fields.id)

The ID for the redirect.

* * *

path

->[path](/docs/api/admin-graphql/latest/objects/UrlRedirect#field-UrlRedirect.fields.path)

The old path to be redirected. When the user visits this path, they will be redirected to the target. (maximum: 1024 characters)

* * *

target

->[target](/docs/api/admin-graphql/latest/objects/UrlRedirect#field-UrlRedirect.fields.target)

The target location where the user will be redirected. When the user visits the old path specified by the `path` property, they will be redirected to this location. This property can be set to any path on the shop's site, or to an external URL. (maximum: 255 characters)

* * *

Was this section helpful?

YesNo

{}

## The Redirect resource

9

1

2

3

4

5

{

"id": 304339089,

"path": "/products.php",

"target": "/products"

}

* * *

##

[Anchor to POST request, Creates a redirect](/docs/api/admin-rest/latest/resources/redirect#post-redirects)

post

Creates a redirect

[urlRedirectCreate](/docs/api/admin-graphql/latest/mutations/urlRedirectCreate?example=creates-a-redirect)

Creates a redirect. When you provide a full URL as the value of the `path` property, it will be saved as an absolute path without the domain. For example, `"path": "<http://www.example.com/springwear>"` will be saved as `"path": "springwear"`.

###

[Anchor to Parameters of Creates a redirect](/docs/api/admin-rest/latest/resources/redirect#post-redirects-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-redirects-examples](/docs/api/admin-rest/latest/resources/redirect#post-redirects-examples)Examples

Create a redirect

Request body

redirect

Redirect resource**Redirect resource**

Show redirect properties

redirect.path:"/ipod"

->[path](/docs/api/admin-graphql/latest/input-objects/UrlRedirectInput#fields-path)

The old path to be redirected. When the user visits this path, they will be redirected to the target. (maximum: 1024 characters)

redirect.target:"/pages/itunes"

->[target](/docs/api/admin-graphql/latest/input-objects/UrlRedirectInput#fields-target)

The target location where the user will be redirected. When the user visits the old path specified by the `path` property, they will be redirected to this location. This property can be set to any path on the shop's site, or to an external URL. (maximum: 255 characters)

Create a redirect using a full URL for the path, which will be saved as an absolute path without a domain

Request body

redirect

Redirect resource**Redirect resource**

Show redirect properties

redirect.path:"http://www.apple.com/forums"

->[path](/docs/api/admin-graphql/latest/input-objects/UrlRedirectInput#fields-path)

The old path to be redirected. When the user visits this path, they will be redirected to the target. (maximum: 1024 characters)

redirect.target:"http://forums.apple.com"

->[target](/docs/api/admin-graphql/latest/input-objects/UrlRedirectInput#fields-target)

The target location where the user will be redirected. When the user visits the old path specified by the `path` property, they will be redirected to this location. This property can be set to any path on the shop's site, or to an external URL. (maximum: 255 characters)

Creating a redirect without a path or target fails and returns an error

Was this section helpful?

YesNo

post

## /admin/api/2026-01/redirects.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"redirect":{"path":"/ipod","target":"/pages/itunes"}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/redirects.json" \

-H "X-Shopify-Access-Token: {access_token}" \

-H "Content-Type: application/json"

{}

## Response

JSON

9

1

2

3

4

5

6

7

8

HTTP/1.1 201 Created

{

"redirect": {

"id": 984542201,

"path": "/ipod",

"target": "/pages/itunes"

}

}

### examples

  * #### Create a redirect

#####

        curl -d '{"redirect":{"path":"/ipod","target":"/pages/itunes"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/redirects.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const redirect = new admin.rest.resources.Redirect({session: session});

        redirect.path = "/ipod";
        redirect.target = "/pages/itunes";
        await redirect.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        redirect = ShopifyAPI::Redirect.new(session: test_session)
        redirect.path = "/ipod"
        redirect.target = "/pages/itunes"
        redirect.save!

#####

        // Session is built by the OAuth process

        const redirect = new shopify.rest.Redirect({session: session});
        redirect.path = "/ipod";
        redirect.target = "/pages/itunes";
        await redirect.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"redirect":{"id":984542201,"path":"/ipod","target":"/pages/itunes"}}

  * #### Create a redirect using a full URL for the path, which will be saved as an absolute path without a domain

#####

        curl -d '{"redirect":{"path":"http://www.apple.com/forums","target":"http://forums.apple.com"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/redirects.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const redirect = new admin.rest.resources.Redirect({session: session});

        redirect.path = "http://www.apple.com/forums";
        redirect.target = "http://forums.apple.com";
        await redirect.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        redirect = ShopifyAPI::Redirect.new(session: test_session)
        redirect.path = "http://www.apple.com/forums"
        redirect.target = "http://forums.apple.com"
        redirect.save!

#####

        // Session is built by the OAuth process

        const redirect = new shopify.rest.Redirect({session: session});
        redirect.path = "http://www.apple.com/forums";
        redirect.target = "http://forums.apple.com";
        await redirect.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"redirect":{"id":984542202,"path":"/forums","target":"http://forums.apple.com/"}}

  * #### Creating a redirect without a path or target fails and returns an error

#####

        curl -d '{"redirect":{"body":"foobar"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/redirects.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const redirect = new admin.rest.resources.Redirect({session: session});

        redirect.body = "foobar";
        await redirect.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        redirect = ShopifyAPI::Redirect.new(session: test_session)
        redirect.body = "foobar"
        redirect.save!

#####

        // Session is built by the OAuth process

        const redirect = new shopify.rest.Redirect({session: session});
        redirect.body = "foobar";
        await redirect.save({
          update: true,
        });

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":{"path":["can't be blank"],"target":["can't be blank","can't be the same as path"]}}


* * *

##

[Anchor to GET request, Retrieves a list of URL redirects](/docs/api/admin-rest/latest/resources/redirect#get-redirects?since-id=668809255)

get

Retrieves a list of URL redirects

[urlRedirects](/docs/api/admin-graphql/latest/queries/urlRedirects?example=retrieves-a-list-of-url-redirects)

Retrieves a list of URL redirects. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

###

[Anchor to Parameters of Retrieves a list of URL redirects](/docs/api/admin-rest/latest/resources/redirect#get-redirects?since-id=668809255-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fields

Show only certain fields, specified by a comma-separated list of field names.

* * *

count

≤ 250**≤ 250**

default 50**default 50**

The maximum number of results to show.

* * *

path

Show redirects with a given path.

* * *

after_id

Restrict results to after the specified ID.

* * *

target

Show redirects with a given target.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-redirects?since-id=668809255-examples](/docs/api/admin-rest/latest/resources/redirect#get-redirects?since-id=668809255-examples)Examples

Retrieve a list of URL redirects after a specified ID

Query parameters

after_id=668809255

Restrict results to after the specified ID.

Retrieve a list of all redirects

Was this section helpful?

YesNo

get

## /admin/api/2026-01/redirects.json?after_id=668809255

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/redirects.json?after_id=668809255" \

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

HTTP/1.1 200 OK

{

"redirects": [

{

"id": 950115854,

"path": "/ibook",

"target": "/products/macbook"

}

]

}

### examples

  * #### Retrieve a list of URL redirects after a specified ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/redirects.json?after_id=668809255" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Redirect.all({
          session: session,
          after_id: "668809255",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Redirect.all(
          session: test_session,
          after_id: "668809255",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Redirect.all({
          session: session,
          after_id: "668809255",
        });

#### response

        HTTP/1.1 200 OK{"redirects":[{"id":950115854,"path":"/ibook","target":"/products/macbook"}]}

  * #### Retrieve a list of all redirects

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/redirects.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Redirect.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Redirect.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Redirect.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"redirects":[{"id":304339089,"path":"/products.php","target":"/products"},{"id":668809255,"path":"/leopard","target":"/pages/macosx"},{"id":950115854,"path":"/ibook","target":"/products/macbook"}]}


* * *

##

[Anchor to GET request, Retrieves a single redirect](/docs/api/admin-rest/latest/resources/redirect#get-redirects-redirect-id)

get

Retrieves a single redirect

[urlRedirect](/docs/api/admin-graphql/latest/queries/urlRedirect?example=retrieves-a-single-redirect)

Retrieves a single redirect

###

[Anchor to Parameters of Retrieves a single redirect](/docs/api/admin-rest/latest/resources/redirect#get-redirects-redirect-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

redirect_id

string**string**

required**required**

* * *

fields

Show only certain fields, specified by a comma-separated list of field names.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-redirects-redirect-id-examples](/docs/api/admin-rest/latest/resources/redirect#get-redirects-redirect-id-examples)Examples

Retrieve a single redirect by its ID

Path parameters

redirect_id=668809255

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/redirects/668809255.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/redirects/668809255.json" \

-H "X-Shopify-Access-Token: {access_token}"

{}

## Response

JSON

9

1

2

3

4

5

6

7

8

HTTP/1.1 200 OK

{

"redirect": {

"id": 668809255,

"path": "/leopard",

"target": "/pages/macosx"

}

}

### examples

  * #### Retrieve a single redirect by its ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/redirects/668809255.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Redirect.find({
          session: session,
          id: 668809255,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Redirect.find(
          session: test_session,
          id: 668809255,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Redirect.find({
          session: session,
          id: 668809255,
        });

#### response

        HTTP/1.1 200 OK{"redirect":{"id":668809255,"path":"/leopard","target":"/pages/macosx"}}


* * *

##

[Anchor to GET request, Retrieves a count of URL redirects](/docs/api/admin-rest/latest/resources/redirect#get-redirects-count)

get

Retrieves a count of URL redirects

[urlRedirectsCount](/docs/api/admin-graphql/latest/queries/urlRedirectsCount?example=retrieves-a-count-of-url-redirects)

Retrieves a count of URL redirects

###

[Anchor to Parameters of Retrieves a count of URL redirects](/docs/api/admin-rest/latest/resources/redirect#get-redirects-count-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

path

Count redirects with given path.

* * *

target

Count redirects with given target.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-redirects-count-examples](/docs/api/admin-rest/latest/resources/redirect#get-redirects-count-examples)Examples

Count all redirects

Was this section helpful?

YesNo

get

## /admin/api/2026-01/redirects/count.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/redirects/count.json" \

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

"count": 3

}

### examples

  * #### Count all redirects

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/redirects/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Redirect.count({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Redirect.count(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Redirect.count({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"count":3}


* * *

##

[Anchor to PUT request, Updates an existing redirect](/docs/api/admin-rest/latest/resources/redirect#put-redirects-redirect-id)

put

Updates an existing redirect

[urlRedirectUpdate](/docs/api/admin-graphql/latest/mutations/urlRedirectUpdate?example=updates-an-existing-redirect)

Updates an existing [redirect](https://shopify.dev/api/admin-rest/latest/resources/redirect)

###

[Anchor to Parameters of Updates an existing redirect](/docs/api/admin-rest/latest/resources/redirect#put-redirects-redirect-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

redirect_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to put-redirects-redirect-id-examples](/docs/api/admin-rest/latest/resources/redirect#put-redirects-redirect-id-examples)Examples

Update both the source (path) and target URIs of a redirect

Path parameters

redirect_id=950115854

string**string**

required**required**

Request body

redirect

Redirect resource**Redirect resource**

Show redirect properties

redirect.id:950115854

read-only**read-only**

The ID for the redirect.

redirect.path:"/powermac"

->[path](/docs/api/admin-graphql/latest/input-objects/UrlRedirectInput#fields-path)

The old path to be redirected. When the user visits this path, they will be redirected to the target. (maximum: 1024 characters)

redirect.target:"/pages/macpro"

->[target](/docs/api/admin-graphql/latest/input-objects/UrlRedirectInput#fields-target)

The target location where the user will be redirected. When the user visits the old path specified by the `path` property, they will be redirected to this location. This property can be set to any path on the shop's site, or to an external URL. (maximum: 255 characters)

Update the source (path) URI of a redirect

Path parameters

redirect_id=668809255

string**string**

required**required**

Request body

redirect

Redirect resource**Redirect resource**

Show redirect properties

redirect.id:668809255

read-only**read-only**

The ID for the redirect.

redirect.path:"/tiger"

->[path](/docs/api/admin-graphql/latest/input-objects/UrlRedirectInput#fields-path)

The old path to be redirected. When the user visits this path, they will be redirected to the target. (maximum: 1024 characters)

Update the target URI of a redirect

Path parameters

redirect_id=668809255

string**string**

required**required**

Request body

redirect

Redirect resource**Redirect resource**

Show redirect properties

redirect.id:668809255

read-only**read-only**

The ID for the redirect.

redirect.target:"/pages/macpro"

->[target](/docs/api/admin-graphql/latest/input-objects/UrlRedirectInput#fields-target)

The target location where the user will be redirected. When the user visits the old path specified by the `path` property, they will be redirected to this location. This property can be set to any path on the shop's site, or to an external URL. (maximum: 255 characters)

Was this section helpful?

YesNo

put

## /admin/api/2026-01/redirects/950115854.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"redirect":{"id":950115854,"path":"/powermac","target":"/pages/macpro"}}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/redirects/950115854.json" \

-H "X-Shopify-Access-Token: {access_token}" \

-H "Content-Type: application/json"

{}

## Response

JSON

9

1

2

3

4

5

6

7

8

HTTP/1.1 200 OK

{

"redirect": {

"path": "/powermac",

"target": "/pages/macpro",

"id": 950115854

}

}

### examples

  * #### Update both the source (path) and target URIs of a redirect

#####

        curl -d '{"redirect":{"id":950115854,"path":"/powermac","target":"/pages/macpro"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/redirects/950115854.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const redirect = new admin.rest.resources.Redirect({session: session});

        redirect.id = 950115854;
        redirect.path = "/powermac";
        redirect.target = "/pages/macpro";
        await redirect.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        redirect = ShopifyAPI::Redirect.new(session: test_session)
        redirect.id = 950115854
        redirect.path = "/powermac"
        redirect.target = "/pages/macpro"
        redirect.save!

#####

        // Session is built by the OAuth process

        const redirect = new shopify.rest.Redirect({session: session});
        redirect.id = 950115854;
        redirect.path = "/powermac";
        redirect.target = "/pages/macpro";
        await redirect.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"redirect":{"path":"/powermac","target":"/pages/macpro","id":950115854}}

  * #### Update the source (path) URI of a redirect

#####

        curl -d '{"redirect":{"id":668809255,"path":"/tiger"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/redirects/668809255.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const redirect = new admin.rest.resources.Redirect({session: session});

        redirect.id = 668809255;
        redirect.path = "/tiger";
        await redirect.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        redirect = ShopifyAPI::Redirect.new(session: test_session)
        redirect.id = 668809255
        redirect.path = "/tiger"
        redirect.save!

#####

        // Session is built by the OAuth process

        const redirect = new shopify.rest.Redirect({session: session});
        redirect.id = 668809255;
        redirect.path = "/tiger";
        await redirect.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"redirect":{"path":"/tiger","target":"/pages/macosx","id":668809255}}

  * #### Update the target URI of a redirect

#####

        curl -d '{"redirect":{"id":668809255,"target":"/pages/macpro"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/redirects/668809255.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const redirect = new admin.rest.resources.Redirect({session: session});

        redirect.id = 668809255;
        redirect.target = "/pages/macpro";
        await redirect.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        redirect = ShopifyAPI::Redirect.new(session: test_session)
        redirect.id = 668809255
        redirect.target = "/pages/macpro"
        redirect.save!

#####

        // Session is built by the OAuth process

        const redirect = new shopify.rest.Redirect({session: session});
        redirect.id = 668809255;
        redirect.target = "/pages/macpro";
        await redirect.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"redirect":{"target":"/pages/macpro","path":"/leopard","id":668809255}}


* * *

##

[Anchor to DELETE request, Deletes a redirect](/docs/api/admin-rest/latest/resources/redirect#delete-redirects-redirect-id)

del

Deletes a redirect

[urlRedirectDelete](/docs/api/admin-graphql/latest/mutations/urlRedirectDelete?example=deletes-a-redirect)

Deletes a redirect

###

[Anchor to Parameters of Deletes a redirect](/docs/api/admin-rest/latest/resources/redirect#delete-redirects-redirect-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

redirect_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to delete-redirects-redirect-id-examples](/docs/api/admin-rest/latest/resources/redirect#delete-redirects-redirect-id-examples)Examples

Delete an existing redirect

Path parameters

redirect_id=668809255

string**string**

required**required**

Was this section helpful?

YesNo

del

## /admin/api/2026-01/redirects/668809255.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/redirects/668809255.json" \

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

  * #### Delete an existing redirect

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/redirects/668809255.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Redirect.delete({
          session: session,
          id: 668809255,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Redirect.delete(
          session: test_session,
          id: 668809255,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Redirect.delete({
          session: session,
          id: 668809255,
        });

#### response

        HTTP/1.1 200 OK{}