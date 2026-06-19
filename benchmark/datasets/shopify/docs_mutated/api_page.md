# Page

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/page*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# Page

Ask assistant

Requires `content` access scope.

**Requires `content` access scope.:**

In addition to an online storefront, Shopify stores come with a tool for creating basic HTML web pages. Store owners can create any number of pages to hold static content, such as an **About us** page, a **Contact us** page, or a page with customer testimonials.

These web pages are represented by the Page resource, and their HTML content is contained in the value of the `body_html` property. The Page resource lets you retrieve, create, update, and delete web pages for a store.

Pages are meant to be used for long-term, static content that rarely changes. For creating content on a regular basis, use the [Blog](/docs/admin-api/rest/reference/online-store/blog) resource instead.

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/pages.json](/docs/api/admin-rest/latest/resources/page#post-pages)

Creates a page

[pageCreate](/docs/api/admin-graphql/latest/mutations/pageCreate?example=creates-a-page)

  * [get/admin/api/latest/pages.json](/docs/api/admin-rest/latest/resources/page#get-pages)

Retrieves a list of pages

[pages](/docs/api/admin-graphql/latest/queries/pages?example=retrieves-a-list-of-pages)

  * [get/admin/api/latest/pages/{page_id}.json](/docs/api/admin-rest/latest/resources/page#get-pages-page-id)

Retrieves a single page by its ID

[page](/docs/api/admin-graphql/latest/queries/page?example=retrieves-a-single-page-by-its-id)

  * [get/admin/api/latest/pages/count.json](/docs/api/admin-rest/latest/resources/page#get-pages-count)

Retrieves a page count

[pagesCount](/docs/api/admin-graphql/latest/queries/pagesCount?example=retrieves-a-page-count)

  * [put/admin/api/latest/pages/{page_id}.json](/docs/api/admin-rest/latest/resources/page#put-pages-page-id)

Updates a page

[pageUpdate](/docs/api/admin-graphql/latest/mutations/pageUpdate?example=updates-a-page)

  * [del/admin/api/latest/pages/{page_id}.json](/docs/api/admin-rest/latest/resources/page#delete-pages-page-id)

Deletes a page

[pageDelete](/docs/api/admin-graphql/latest/mutations/pageDelete?example=deletes-a-page)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/page#resource-object)

## The Page resource

[Anchor to ](/docs/api/admin-rest/latest/resources/page#resource-object-properties)

### Properties

* * *

author

->[author](/docs/api/admin-graphql/latest/objects/Page)

The name of the person who created the page.

* * *

body_html

->[bodyHtml](/docs/api/admin-graphql/latest/objects/Page)

The text content of the page, complete with HTML markup.

* * *

created_at

read-only**read-only**

->[createdAt](/docs/api/admin-graphql/latest/objects/Page#field-Page.fields.createdAt)

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the page was created.

* * *

handle

->[handle](/docs/api/admin-graphql/latest/objects/Page#field-Page.fields.handle)

A unique, human-friendly string for the page, generated automatically from its title. In themes, the Liquid templating language refers to a page by its handle.

* * *

id

read-only**read-only**

->[id](/docs/api/admin-graphql/latest/objects/Page#field-Page.fields.id)

The unique numeric identifier for the page.

* * *

metafield

->[metafields](/docs/api/admin-graphql/latest/objects/Page#field-Page.fields.metafields)

Additional information attached to the Page object. It has the following properties:

Show metafield properties

  * **key** : An identifier for the metafield. (maximum: 30 characters)
  * **namespace** : A container for a set of metadata. Namespaces help distinguish between metadata created by different apps. (maximum: 20 characters)
  * **value** : The information to be stored as metadata.
  * **type** : The metafield's information type. Refer to the [full list of types](/apps/metafields/types).
  * **description (optional)** : Additional information about the metafield.


For more information on attaching metadata to Shopify resources, see the [Metafield](/docs/admin-api/rest/reference/metafield) resource.

* * *

published_at

->[publishedAt](/docs/api/admin-graphql/latest/objects/Page#field-Page.fields.publishedAt)

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the page was published. Returns `null` when the page is hidden.

* * *

shop_id

read-only**read-only**

deprecated**deprecated**

The ID of the shop to which the page belongs.

* * *

template_suffix

->[templateSuffix](/docs/api/admin-graphql/latest/objects/Page#field-Page.fields.templateSuffix)

The suffix of the [template](/api/liquid/objects/template) that is used to render the page. If the value is an empty string or `null`, then the default page template is used.

* * *

title

->[title](/docs/api/admin-graphql/latest/objects/Page#field-Page.fields.title)

The title of the page.

* * *

updated_at

read-only**read-only**

->[updatedAt](/docs/api/admin-graphql/latest/objects/Page#field-Page.fields.updatedAt)

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the page was last updated.

* * *

admin_graphql_api_id

read-only**read-only**

->[id](/docs/api/admin-graphql/latest/objects/Page#field-Page.fields.id)

The GraphQL GID of the page.

* * *

Was this section helpful?

YesNo

{}

## The Page resource

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

{

"author": "Lydia",

"body_html": "Contact us at <a href='mailto:contact@example.com'>contact@example.com</a>.",

"created_at": "2008-07-15T20:00:00-04:00",

"handle": "contact-us",

"id": 131092082,

"metafield": {

"key": "new",

"value": "new value",

"type": "single_line_text_field",

"namespace": "global"

},

"published_at": "2014-07-16T20:00:00-04:00",

"shop_id": 548380009,

"template_suffix": "contact",

"title": "Contact us",

"updated_at": "2008-07-16T20:00:00-04:00",

"admin_graphql_api_id": "gid://shopify/OnlineStorePage/131092082"

}

* * *

##

[Anchor to POST request, Creates a page](/docs/api/admin-rest/latest/resources/page#post-pages)

post

Creates a page

[pageCreate](/docs/api/admin-graphql/latest/mutations/pageCreate?example=creates-a-page)

Creates a page

###

[Anchor to Parameters of Creates a page](/docs/api/admin-rest/latest/resources/page#post-pages-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-pages-examples](/docs/api/admin-rest/latest/resources/page#post-pages-examples)Examples

Create a page with HTML markup

Request body

page

Page resource**Page resource**

Show page properties

page.title:"Warranty information"

->[title](/docs/api/admin-graphql/latest/input-objects/PageCreateInput#fields-title)

The title of the page.

page.body_html:"<h2>Warranty</h2>\n<p>Returns accepted if we receive items <strong>30 days after purchase</strong>.</p>"

->[body](/docs/api/admin-graphql/latest/input-objects/PageCreateInput#fields-body)

The text content of the page, complete with HTML markup.

Create a page with a metafield

Request body

page

Page resource**Page resource**

Show page properties

page.title:"Warranty information"

->[title](/docs/api/admin-graphql/latest/input-objects/PageCreateInput#fields-title)

The title of the page.

page.body_html:"<h2>Warranty</h2>\n<p>Returns accepted if we receive items <strong>30 days after purchase</strong>.</p>"

->[body](/docs/api/admin-graphql/latest/input-objects/PageCreateInput#fields-body)

The text content of the page, complete with HTML markup.

Create an unpublished page

Request body

page

Page resource**Page resource**

Show page properties

page.title:"Warranty information"

->[title](/docs/api/admin-graphql/latest/input-objects/PageCreateInput#fields-title)

The title of the page.

page.body_html:"<h2>Warranty</h2>\n<p>Returns accepted if we receive items <strong>30 days after purchase</strong>.</p>"

->[body](/docs/api/admin-graphql/latest/input-objects/PageCreateInput#fields-body)

The text content of the page, complete with HTML markup.

Creating a page without a title fails and returns an error

Was this section helpful?

YesNo

post

## /admin/api/2026-01/pages.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"page":{"title":"Warranty information","body_html":"<h2>Warranty</h2>\n<p>Returns accepted if we receive items <strong>30 days after purchase</strong>.</p>"}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/pages.json" \

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

"page": {

"id": 1025371375,

"title": "Warranty information",

"shop_id": 548380009,

"handle": "warranty-information",

"body_html": "<h2>Warranty</h2>\n<p>Returns accepted if we receive items <strong>30 days after purchase</strong>.</p>",

"author": "Shopify API",

"created_at": "2026-01-09T19:38:54-05:00",

"updated_at": "2026-01-09T19:38:54-05:00",

"published_at": "2026-01-09T19:38:54-05:00",

"template_suffix": null,

"admin_graphql_api_id": "gid://shopify/Page/1025371375"

}

}

### examples

  * #### Create a page with HTML markup

#####

        curl -d '{"page":{"title":"Warranty information","body_html":"<h2>Warranty</h2>\n<p>Returns accepted if we receive items <strong>30 days after purchase</strong>.</p>"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/pages.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const page = new admin.rest.resources.Page({session: session});

        page.title = "Warranty information";
        page.body_html = "<h2>Warranty</h2>\n<p>Returns accepted if we receive items <strong>30 days after purchase</strong>.</p>";
        await page.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        page = ShopifyAPI::Page.new(session: test_session)
        page.title = "Warranty information"
        page.body_html = "<h2>Warranty</h2>\n<p>Returns accepted if we receive items <strong>30 days after purchase</strong>.</p>"
        page.save!

#####

        // Session is built by the OAuth process

        const page = new shopify.rest.Page({session: session});
        page.title = "Warranty information";
        page.body_html = "<h2>Warranty</h2>\n<p>Returns accepted if we receive items <strong>30 days after purchase</strong>.</p>";
        await page.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"page":{"id":1025371375,"title":"Warranty information","shop_id":548380009,"handle":"warranty-information","body_html":"<h2>Warranty</h2>\n<p>Returns accepted if we receive items <strong>30 days after purchase</strong>.</p>","author":"Shopify API","created_at":"2026-01-09T19:38:54-05:00","updated_at":"2026-01-09T19:38:54-05:00","published_at":"2026-01-09T19:38:54-05:00","template_suffix":null,"admin_graphql_api_id":"gid://shopify/Page/1025371375"}}

  * #### Create a page with a metafield

#####

        curl -d '{"page":{"title":"Warranty information","body_html":"<h2>Warranty</h2>\n<p>Returns accepted if we receive items <strong>30 days after purchase</strong>.</p>","metafields":[{"key":"new","value":"new value","type":"single_line_text_field","namespace":"global"}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/pages.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const page = new admin.rest.resources.Page({session: session});

        page.title = "Warranty information";
        page.body_html = "<h2>Warranty</h2>\n<p>Returns accepted if we receive items <strong>30 days after purchase</strong>.</p>";
        page.metafields = [
          {
            "key": "new",
            "value": "new value",
            "type": "single_line_text_field",
            "namespace": "global"
          }
        ];
        await page.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        page = ShopifyAPI::Page.new(session: test_session)
        page.title = "Warranty information"
        page.body_html = "<h2>Warranty</h2>\n<p>Returns accepted if we receive items <strong>30 days after purchase</strong>.</p>"
        page.metafields = [
          {
            "key" => "new",
            "value" => "new value",
            "type" => "single_line_text_field",
            "namespace" => "global"
          }
        ]
        page.save!

#####

        // Session is built by the OAuth process

        const page = new shopify.rest.Page({session: session});
        page.title = "Warranty information";
        page.body_html = "<h2>Warranty</h2>\n<p>Returns accepted if we receive items <strong>30 days after purchase</strong>.</p>";
        page.metafields = [
          {
            "key": "new",
            "value": "new value",
            "type": "single_line_text_field",
            "namespace": "global"
          }
        ];
        await page.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"page":{"id":1025371374,"title":"Warranty information","shop_id":548380009,"handle":"warranty-information","body_html":"<h2>Warranty</h2>\n<p>Returns accepted if we receive items <strong>30 days after purchase</strong>.</p>","author":"Shopify API","created_at":"2026-01-09T19:38:49-05:00","updated_at":"2026-01-09T19:38:49-05:00","published_at":"2026-01-09T19:38:49-05:00","template_suffix":null,"admin_graphql_api_id":"gid://shopify/Page/1025371374"}}

  * #### Create an unpublished page

#####

        curl -d '{"page":{"title":"Warranty information","body_html":"<h2>Warranty</h2>\n<p>Returns accepted if we receive items <strong>30 days after purchase</strong>.</p>","published":false}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/pages.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const page = new admin.rest.resources.Page({session: session});

        page.title = "Warranty information";
        page.body_html = "<h2>Warranty</h2>\n<p>Returns accepted if we receive items <strong>30 days after purchase</strong>.</p>";
        page.published = false;
        await page.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        page = ShopifyAPI::Page.new(session: test_session)
        page.title = "Warranty information"
        page.body_html = "<h2>Warranty</h2>\n<p>Returns accepted if we receive items <strong>30 days after purchase</strong>.</p>"
        page.published = false
        page.save!

#####

        // Session is built by the OAuth process

        const page = new shopify.rest.Page({session: session});
        page.title = "Warranty information";
        page.body_html = "<h2>Warranty</h2>\n<p>Returns accepted if we receive items <strong>30 days after purchase</strong>.</p>";
        page.published = false;
        await page.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"page":{"id":1025371372,"title":"Warranty information","shop_id":548380009,"handle":"warranty-information","body_html":"<h2>Warranty</h2>\n<p>Returns accepted if we receive items <strong>30 days after purchase</strong>.</p>","author":"Shopify API","created_at":"2026-01-09T19:38:38-05:00","updated_at":"2026-01-09T19:38:38-05:00","published_at":null,"template_suffix":null,"admin_graphql_api_id":"gid://shopify/Page/1025371372"}}

  * #### Creating a page without a title fails and returns an error

#####

        curl -d '{"page":{"body":"foobar"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/pages.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const page = new admin.rest.resources.Page({session: session});

        page.body = "foobar";
        await page.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        page = ShopifyAPI::Page.new(session: test_session)
        page.body = "foobar"
        page.save!

#####

        // Session is built by the OAuth process

        const page = new shopify.rest.Page({session: session});
        page.body = "foobar";
        await page.save({
          update: true,
        });

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":{"title":["can't be blank"]}}


* * *

##

[Anchor to GET request, Retrieves a list of pages](/docs/api/admin-rest/latest/resources/page#get-pages)

get

Retrieves a list of pages

[pages](/docs/api/admin-graphql/latest/queries/pages?example=retrieves-a-list-of-pages)

Retrieve a list of all pages. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

###

[Anchor to Parameters of Retrieves a list of pages](/docs/api/admin-rest/latest/resources/page#get-pages-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

created_at_max

Show pages created before date (format: 2014-04-25T16:15:47-04:00).

* * *

created_after

Show pages created after date (format: 2014-04-25T16:15:47-04:00).

* * *

fields

Show only certain fields, specified by a comma-separated list of field names.

* * *

handle

Retrieve a page with a given handle.

* * *

count

≤ 250**≤ 250**

default 50**default 50**

The maximum number of results to show.

* * *

published_at_max

Show pages published before date (format: 2014-04-25T16:15:47-04:00).

* * *

published_at_min

Show pages published after date (format: 2014-04-25T16:15:47-04:00).

* * *

published_status

default any**default any**

Restrict results to pages with a given published status:

Show published_status properties

  * **published** : Show only published pages.

  * **unpublished** : Show only unpublished pages.

  * **any** : Show published and unpublished pages.


* * *

after_id

Restrict results to after the specified ID.

* * *

title

Retrieve pages with a given title.

* * *

updated_at_max

Show pages last updated before date (format: 2014-04-25T16:15:47-04:00).

* * *

updated_at_min

Show pages last updated after date (format: 2014-04-25T16:15:47-04:00).

* * *

Was this section helpful?

YesNo

###

[Anchor to get-pages-examples](/docs/api/admin-rest/latest/resources/page#get-pages-examples)Examples

Get all pages for a shop

Retrieve a list of all pages after the specified ID

Query parameters

after_id=108828309

Restrict results to after the specified ID.

Was this section helpful?

YesNo

get

## /admin/api/2026-01/pages.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/pages.json" \

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

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

49

50

51

52

53

54

55

56

57

HTTP/1.1 200 OK

{

"pages": [

{

"id": 108828309,

"title": "Sample Page",

"shop_id": 548380009,

"handle": "sample",

"body_html": "<p>this is a <strong>sample</strong> page.</p>",

"author": "Dennis",

"created_at": "2008-07-15T20:00:00-04:00",

"updated_at": "2008-07-16T20:00:00-04:00",

"published_at": null,

"template_suffix": null,

"admin_graphql_api_id": "gid://shopify/Page/108828309"

},

{

"id": 169524623,

"title": "Store hours",

"shop_id": 548380009,

"handle": "store-hours",

"body_html": "<p>We never close.</p>",

"author": "Jobs",

"created_at": "2013-12-31T19:00:00-05:00",

"updated_at": "2013-12-31T19:00:00-05:00",

"published_at": "2014-02-01T19:00:00-05:00",

"template_suffix": null,

"admin_graphql_api_id": "gid://shopify/Page/169524623"

},

{

"id": 322471,

"title": "Support",

"shop_id": 548380009,

"handle": "support",

"body_html": "<p>Come in store for support.</p>",

"author": "Dennis",

"created_at": "2009-07-15T20:00:00-04:00",

"updated_at": "2009-07-16T20:00:00-04:00",

"published_at": null,

"template_suffix": null,

"admin_graphql_api_id": "gid://shopify/Page/322471"

},

{

"id": 131092082,

"title": "Terms of Services",

"shop_id": 548380009,

"handle": "tos",

"body_html": "<p>We make <strong>perfect</strong> stuff, we don't need a warranty.</p>",

"author": "Dennis",

"created_at": "2008-07-15T20:00:00-04:00",

"updated_at": "2008-07-16T20:00:00-04:00",

"published_at": "2008-07-15T20:00:00-04:00",

"template_suffix": null,

"admin_graphql_api_id": "gid://shopify/Page/131092082"

}

]

}

### examples

  * #### Get all pages for a shop

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/pages.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Page.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Page.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Page.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"pages":[{"id":108828309,"title":"Sample Page","shop_id":548380009,"handle":"sample","body_html":"<p>this is a <strong>sample</strong> page.</p>","author":"Dennis","created_at":"2008-07-15T20:00:00-04:00","updated_at":"2008-07-16T20:00:00-04:00","published_at":null,"template_suffix":null,"admin_graphql_api_id":"gid://shopify/Page/108828309"},{"id":169524623,"title":"Store hours","shop_id":548380009,"handle":"store-hours","body_html":"<p>We never close.</p>","author":"Jobs","created_at":"2013-12-31T19:00:00-05:00","updated_at":"2013-12-31T19:00:00-05:00","published_at":"2014-02-01T19:00:00-05:00","template_suffix":null,"admin_graphql_api_id":"gid://shopify/Page/169524623"},{"id":322471,"title":"Support","shop_id":548380009,"handle":"support","body_html":"<p>Come in store for support.</p>","author":"Dennis","created_at":"2009-07-15T20:00:00-04:00","updated_at":"2009-07-16T20:00:00-04:00","published_at":null,"template_suffix":null,"admin_graphql_api_id":"gid://shopify/Page/322471"},{"id":131092082,"title":"Terms of Services","shop_id":548380009,"handle":"tos","body_html":"<p>We make <strong>perfect</strong> stuff, we don't need a warranty.</p>","author":"Dennis","created_at":"2008-07-15T20:00:00-04:00","updated_at":"2008-07-16T20:00:00-04:00","published_at":"2008-07-15T20:00:00-04:00","template_suffix":null,"admin_graphql_api_id":"gid://shopify/Page/131092082"}]}

  * #### Retrieve a list of all pages after the specified ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/pages.json?after_id=108828309" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Page.all({
          session: session,
          after_id: "108828309",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Page.all(
          session: test_session,
          after_id: "108828309",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Page.all({
          session: session,
          after_id: "108828309",
        });

#### response

        HTTP/1.1 200 OK{"pages":[{"id":131092082,"title":"Terms of Services","shop_id":548380009,"handle":"tos","body_html":"<p>We make <strong>perfect</strong> stuff, we don't need a warranty.</p>","author":"Dennis","created_at":"2008-07-15T20:00:00-04:00","updated_at":"2008-07-16T20:00:00-04:00","published_at":"2008-07-15T20:00:00-04:00","template_suffix":null,"admin_graphql_api_id":"gid://shopify/Page/131092082"},{"id":169524623,"title":"Store hours","shop_id":548380009,"handle":"store-hours","body_html":"<p>We never close.</p>","author":"Jobs","created_at":"2013-12-31T19:00:00-05:00","updated_at":"2013-12-31T19:00:00-05:00","published_at":"2014-02-01T19:00:00-05:00","template_suffix":null,"admin_graphql_api_id":"gid://shopify/Page/169524623"}]}


* * *

##

[Anchor to GET request, Retrieves a single page by its ID](/docs/api/admin-rest/latest/resources/page#get-pages-page-id)

get

Retrieves a single page by its ID

[page](/docs/api/admin-graphql/latest/queries/page?example=retrieves-a-single-page-by-its-id)

Retrieves a single page by its ID.

###

[Anchor to Parameters of Retrieves a single page by its ID](/docs/api/admin-rest/latest/resources/page#get-pages-page-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

page_id

string**string**

required**required**

* * *

fields

Show only certain fields, specified by a comma-separated list of field names.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-pages-page-id-examples](/docs/api/admin-rest/latest/resources/page#get-pages-page-id-examples)Examples

Retrieve a single page

Path parameters

page_id=131092082

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/pages/131092082.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/pages/131092082.json" \

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

"page": {

"id": 131092082,

"title": "Terms of Services",

"shop_id": 548380009,

"handle": "tos",

"body_html": "<p>We make <strong>perfect</strong> stuff, we don't need a warranty.</p>",

"author": "Dennis",

"created_at": "2008-07-15T20:00:00-04:00",

"updated_at": "2008-07-16T20:00:00-04:00",

"published_at": "2008-07-15T20:00:00-04:00",

"template_suffix": null,

"admin_graphql_api_id": "gid://shopify/Page/131092082"

}

}

### examples

  * #### Retrieve a single page

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/pages/131092082.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Page.find({
          session: session,
          id: 131092082,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Page.find(
          session: test_session,
          id: 131092082,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Page.find({
          session: session,
          id: 131092082,
        });

#### response

        HTTP/1.1 200 OK{"page":{"id":131092082,"title":"Terms of Services","shop_id":548380009,"handle":"tos","body_html":"<p>We make <strong>perfect</strong> stuff, we don't need a warranty.</p>","author":"Dennis","created_at":"2008-07-15T20:00:00-04:00","updated_at":"2008-07-16T20:00:00-04:00","published_at":"2008-07-15T20:00:00-04:00","template_suffix":null,"admin_graphql_api_id":"gid://shopify/Page/131092082"}}


* * *

##

[Anchor to GET request, Retrieves a page count](/docs/api/admin-rest/latest/resources/page#get-pages-count)

get

Retrieves a page count

[pagesCount](/docs/api/admin-graphql/latest/queries/pagesCount?example=retrieves-a-page-count)

Retrieves a page count.

###

[Anchor to Parameters of Retrieves a page count](/docs/api/admin-rest/latest/resources/page#get-pages-count-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

created_at_max

Count pages created before date (format: 2014-04-25T16:15:47-04:00).

* * *

created_after

Count pages created after date (format: 2014-04-25T16:15:47-04:00).

* * *

published_at_max

Show pages published before date (format: 2014-04-25T16:15:47-04:00).

* * *

published_at_min

Show pages published after date (format: 2014-04-25T16:15:47-04:00).

* * *

published_status

default any**default any**

Count pages with a given published status:

Show published_status properties

  * **published** : Count published pages.

  * **unpublished** : Count unpublished pages.

  * **any** : Count published and unpublished pages.


* * *

title

Count pages with a given title.

* * *

updated_at_max

Count pages last updated before date (format: 2014-04-25T16:15:47-04:00).

* * *

updated_at_min

Count pages last updated after date (format: 2014-04-25T16:15:47-04:00).

* * *

Was this section helpful?

YesNo

###

[Anchor to get-pages-count-examples](/docs/api/admin-rest/latest/resources/page#get-pages-count-examples)Examples

Retrieve a count of all pages

Was this section helpful?

YesNo

get

## /admin/api/2026-01/pages/count.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/pages/count.json" \

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

"count": 4

}

### examples

  * #### Retrieve a count of all pages

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/pages/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Page.count({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Page.count(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Page.count({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"count":4}


* * *

##

[Anchor to PUT request, Updates a page](/docs/api/admin-rest/latest/resources/page#put-pages-page-id)

put

Updates a page

[pageUpdate](/docs/api/admin-graphql/latest/mutations/pageUpdate?example=updates-a-page)

Updates a page

###

[Anchor to Parameters of Updates a page](/docs/api/admin-rest/latest/resources/page#put-pages-page-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

page_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to put-pages-page-id-examples](/docs/api/admin-rest/latest/resources/page#put-pages-page-id-examples)Examples

Add a metafield to a page

Path parameters

page_id=131092082

string**string**

required**required**

Request body

page

Page resource**Page resource**

Show page properties

page.id:131092082

read-only**read-only**

The unique numeric identifier for the page.

Hide a published page

Path parameters

page_id=131092082

string**string**

required**required**

Request body

page

Page resource**Page resource**

Show page properties

page.id:131092082

read-only**read-only**

The unique numeric identifier for the page.

Show a hidden page

Path parameters

page_id=131092082

string**string**

required**required**

Request body

page

Page resource**Page resource**

Show page properties

page.id:131092082

read-only**read-only**

The unique numeric identifier for the page.

Update an existing page completely

Path parameters

page_id=131092082

string**string**

required**required**

Request body

page

Page resource**Page resource**

Show page properties

page.id:131092082

read-only**read-only**

The unique numeric identifier for the page.

page.body_html:"<p>Returns accepted if we receive the items <strong>14 days</strong> after purchase.</p>"

->[body](/docs/api/admin-graphql/latest/input-objects/PageUpdateInput#fields-body)

The text content of the page, complete with HTML markup.

page.author:"Christopher Gorski"

->[author](/docs/api/admin-graphql/latest/input-objects/PageUpdateInput)

The name of the person who created the page.

page.title:"New warranty"

->[title](/docs/api/admin-graphql/latest/input-objects/PageUpdateInput#fields-title)

The title of the page.

page.handle:"new-warranty"

->[handle](/docs/api/admin-graphql/latest/input-objects/PageUpdateInput#fields-handle)

A unique, human-friendly string for the page, generated automatically from its title. In themes, the Liquid templating language refers to a page by its handle.

Update the body HTML of an existing page

Path parameters

page_id=131092082

string**string**

required**required**

Request body

page

Page resource**Page resource**

Show page properties

page.id:131092082

read-only**read-only**

The unique numeric identifier for the page.

page.body_html:"<p>Returns accepted if we receive the items 14 days after purchase.</p>"

->[body](/docs/api/admin-graphql/latest/input-objects/PageUpdateInput#fields-body)

The text content of the page, complete with HTML markup.

Was this section helpful?

YesNo

put

## /admin/api/2026-01/pages/131092082.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"page":{"id":131092082,"metafields":[{"key":"new","value":"new value","type":"single_line_text_field","namespace":"global"}]}}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/pages/131092082.json" \

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

"page": {

"shop_id": 548380009,

"title": "Terms of Services",

"handle": "tos",

"body_html": "<p>We make <strong>perfect</strong> stuff, we don't need a warranty.</p>",

"id": 131092082,

"author": "Dennis",

"created_at": "2008-07-15T20:00:00-04:00",

"updated_at": "2008-07-16T20:00:00-04:00",

"published_at": "2008-07-15T20:00:00-04:00",

"template_suffix": null,

"admin_graphql_api_id": "gid://shopify/Page/131092082"

}

}

### examples

  * #### Add a metafield to a page

#####

        curl -d '{"page":{"id":131092082,"metafields":[{"key":"new","value":"new value","type":"single_line_text_field","namespace":"global"}]}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/pages/131092082.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const page = new admin.rest.resources.Page({session: session});

        page.id = 131092082;
        page.metafields = [
          {
            "key": "new",
            "value": "new value",
            "type": "single_line_text_field",
            "namespace": "global"
          }
        ];
        await page.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        page = ShopifyAPI::Page.new(session: test_session)
        page.id = 131092082
        page.metafields = [
          {
            "key" => "new",
            "value" => "new value",
            "type" => "single_line_text_field",
            "namespace" => "global"
          }
        ]
        page.save!

#####

        // Session is built by the OAuth process

        const page = new shopify.rest.Page({session: session});
        page.id = 131092082;
        page.metafields = [
          {
            "key": "new",
            "value": "new value",
            "type": "single_line_text_field",
            "namespace": "global"
          }
        ];
        await page.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"page":{"shop_id":548380009,"title":"Terms of Services","handle":"tos","body_html":"<p>We make <strong>perfect</strong> stuff, we don't need a warranty.</p>","id":131092082,"author":"Dennis","created_at":"2008-07-15T20:00:00-04:00","updated_at":"2008-07-16T20:00:00-04:00","published_at":"2008-07-15T20:00:00-04:00","template_suffix":null,"admin_graphql_api_id":"gid://shopify/Page/131092082"}}

  * #### Hide a published page

#####

        curl -d '{"page":{"id":131092082,"published":false}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/pages/131092082.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const page = new admin.rest.resources.Page({session: session});

        page.id = 131092082;
        page.published = false;
        await page.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        page = ShopifyAPI::Page.new(session: test_session)
        page.id = 131092082
        page.published = false
        page.save!

#####

        // Session is built by the OAuth process

        const page = new shopify.rest.Page({session: session});
        page.id = 131092082;
        page.published = false;
        await page.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"page":{"shop_id":548380009,"published_at":null,"title":"Terms of Services","handle":"tos","body_html":"<p>We make <strong>perfect</strong> stuff, we don't need a warranty.</p>","id":131092082,"author":"Dennis","created_at":"2008-07-15T20:00:00-04:00","updated_at":"2026-01-09T19:38:31-05:00","template_suffix":null,"admin_graphql_api_id":"gid://shopify/Page/131092082"}}

  * #### Show a hidden page

#####

        curl -d '{"page":{"id":131092082,"published":true}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/pages/131092082.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const page = new admin.rest.resources.Page({session: session});

        page.id = 131092082;
        page.published = true;
        await page.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        page = ShopifyAPI::Page.new(session: test_session)
        page.id = 131092082
        page.published = true
        page.save!

#####

        // Session is built by the OAuth process

        const page = new shopify.rest.Page({session: session});
        page.id = 131092082;
        page.published = true;
        await page.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"page":{"shop_id":548380009,"published_at":"2026-01-09T19:38:47-05:00","title":"Terms of Services","handle":"tos","body_html":"<p>We make <strong>perfect</strong> stuff, we don't need a warranty.</p>","id":131092082,"author":"Dennis","created_at":"2008-07-15T20:00:00-04:00","updated_at":"2026-01-09T19:38:47-05:00","template_suffix":null,"admin_graphql_api_id":"gid://shopify/Page/131092082"}}

  * #### Update an existing page completely

#####

        curl -d '{"page":{"id":131092082,"body_html":"<p>Returns accepted if we receive the items <strong>14 days</strong> after purchase.</p>","author":"Christopher Gorski","title":"New warranty","handle":"new-warranty"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/pages/131092082.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const page = new admin.rest.resources.Page({session: session});

        page.id = 131092082;
        page.body_html = "<p>Returns accepted if we receive the items <strong>14 days</strong> after purchase.</p>";
        page.author = "Christopher Gorski";
        page.title = "New warranty";
        page.handle = "new-warranty";
        await page.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        page = ShopifyAPI::Page.new(session: test_session)
        page.id = 131092082
        page.body_html = "<p>Returns accepted if we receive the items <strong>14 days</strong> after purchase.</p>"
        page.author = "Christopher Gorski"
        page.title = "New warranty"
        page.handle = "new-warranty"
        page.save!

#####

        // Session is built by the OAuth process

        const page = new shopify.rest.Page({session: session});
        page.id = 131092082;
        page.body_html = "<p>Returns accepted if we receive the items <strong>14 days</strong> after purchase.</p>";
        page.author = "Christopher Gorski";
        page.title = "New warranty";
        page.handle = "new-warranty";
        await page.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"page":{"shop_id":548380009,"author":"Christopher Gorski","body_html":"<p>Returns accepted if we receive the items <strong>14 days</strong> after purchase.</p>","handle":"new-warranty","title":"New warranty","id":131092082,"created_at":"2008-07-15T20:00:00-04:00","updated_at":"2026-01-09T19:38:57-05:00","published_at":"2008-07-15T20:00:00-04:00","template_suffix":null,"admin_graphql_api_id":"gid://shopify/Page/131092082"}}

  * #### Update the body HTML of an existing page

#####

        curl -d '{"page":{"id":131092082,"body_html":"<p>Returns accepted if we receive the items 14 days after purchase.</p>"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/pages/131092082.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const page = new admin.rest.resources.Page({session: session});

        page.id = 131092082;
        page.body_html = "<p>Returns accepted if we receive the items 14 days after purchase.</p>";
        await page.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        page = ShopifyAPI::Page.new(session: test_session)
        page.id = 131092082
        page.body_html = "<p>Returns accepted if we receive the items 14 days after purchase.</p>"
        page.save!

#####

        // Session is built by the OAuth process

        const page = new shopify.rest.Page({session: session});
        page.id = 131092082;
        page.body_html = "<p>Returns accepted if we receive the items 14 days after purchase.</p>";
        await page.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"page":{"shop_id":548380009,"body_html":"<p>Returns accepted if we receive the items 14 days after purchase.</p>","title":"Terms of Services","handle":"tos","id":131092082,"author":"Dennis","created_at":"2008-07-15T20:00:00-04:00","updated_at":"2026-01-09T19:38:52-05:00","published_at":"2008-07-15T20:00:00-04:00","template_suffix":null,"admin_graphql_api_id":"gid://shopify/Page/131092082"}}


* * *

##

[Anchor to DELETE request, Deletes a page](/docs/api/admin-rest/latest/resources/page#delete-pages-page-id)

del

Deletes a page

[pageDelete](/docs/api/admin-graphql/latest/mutations/pageDelete?example=deletes-a-page)

Deletes a page.

###

[Anchor to Parameters of Deletes a page](/docs/api/admin-rest/latest/resources/page#delete-pages-page-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

page_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to delete-pages-page-id-examples](/docs/api/admin-rest/latest/resources/page#delete-pages-page-id-examples)Examples

Delete a page

Path parameters

page_id=131092082

string**string**

required**required**

Was this section helpful?

YesNo

del

## /admin/api/2026-01/pages/131092082.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/pages/131092082.json" \

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

  * #### Delete a page

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/pages/131092082.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Page.delete({
          session: session,
          id: 131092082,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Page.delete(
          session: test_session,
          id: 131092082,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Page.delete({
          session: session,
          id: 131092082,
        });

#### response

        HTTP/1.1 200 OK{}