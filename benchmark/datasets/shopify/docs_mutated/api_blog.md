# Blog

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/blog*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# Blog

Ask assistant

Requires `content` access scope.

**Requires `content` access scope.:**

In addition to an online storefront, Shopify shops come with a built-in blogging engine, allowing a shop to have one or more blogs.

Shop owners are encouraged to use blogs to:

  * Make announcements
  * Talk about their products in more detail
  * Show off their expertise
  * Connect with their customers and
  * Boost their shop's search engine rankings


Shopify blogs are like most other blogs: a content management system for articles posted in reverse chronological order. Articles can be posted under one or more user-defined categories and tagged with one or more user-defined tags, with an option to allow readers to post comments to articles. An Atom feed is automatically generated for each blog, allowing for syndication. The search functionality built into every shop also searches the text in blog articles.

Blogs are meant to be used as a type of magazine or newsletter for the shop, with content that changes over time. If your shop needs a static page (such as an "About Us" page), we recommend that you use a Page instead.

Also see the [Article resource](/docs/admin-api/rest/reference/online-store/article) for managing blog articles.

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/blogs.json](/docs/api/admin-rest/latest/resources/blog#post-blogs)

Create a new Blog

[blogCreate](/docs/api/admin-graphql/latest/mutations/blogCreate?example=create-a-new-blog)

  * [get/admin/api/latest/blogs.json](/docs/api/admin-rest/latest/resources/blog#get-blogs)

Retrieve a list of all blogs

[blogs](/docs/api/admin-graphql/latest/queries/blogs?example=retrieve-a-list-of-all-blogs)

  * [get/admin/api/latest/blogs/{blog_id}.json](/docs/api/admin-rest/latest/resources/blog#get-blogs-blog-id)

Receive a single Blog

[blog](/docs/api/admin-graphql/latest/queries/blog?example=receive-a-single-blog)

  * [get/admin/api/latest/blogs/count.json](/docs/api/admin-rest/latest/resources/blog#get-blogs-count)

Receive a count of all Blogs

[blogsCount](/docs/api/admin-graphql/latest/queries/blogsCount?example=receive-a-count-of-all-blogs)

  * [put/admin/api/latest/blogs/{blog_id}.json](/docs/api/admin-rest/latest/resources/blog#put-blogs-blog-id)

Modify an existing Blog

[blogUpdate](/docs/api/admin-graphql/latest/mutations/blogUpdate?example=modify-an-existing-blog)

  * [del/admin/api/latest/blogs/{blog_id}.json](/docs/api/admin-rest/latest/resources/blog#delete-blogs-blog-id)

Remove an existing Blog

[blogDelete](/docs/api/admin-graphql/latest/mutations/blogDelete?example=remove-an-existing-blog)


* * *

[Anchor to ](/docs/api/admin-rest/latest/resources/blog#resource-object)

## The Blog resource

[Anchor to ](/docs/api/admin-rest/latest/resources/blog#resource-object-properties)

### Properties

* * *

commentable

->[commentPolicy](/docs/api/admin-graphql/latest/objects/Blog#field-Blog.fields.commentPolicy)

Indicates whether readers can post comments to the blog and if comments are moderated or not. Possible values are:

Show commentable properties

  * **no (default)** : Readers cannot post comments to blog articles.
  * **moderate** : Readers can post comments to blog articles, but comments must be moderated before they appear.
  * **yes** : Readers can post comments to blog articles without moderation.


* * *

created_at

read-only**read-only**

->[createdAt](/docs/api/admin-graphql/latest/objects/Blog#field-Blog.fields.createdAt)

The date and time when the blog was created. The API returns this value in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601).

* * *

feedburner

->[path](/docs/api/admin-graphql/latest/objects/BlogFeed#field-BlogFeed.fields.path)

FeedBurner is a web feed management provider and can be enabled to provide custom RSS feeds for Shopify bloggers. Google has stopped supporting FeedBurner, and new or existing blogs that are not already integrated with FeedBurner can't use the service. This property will default to blank unless FeedBurner is enabled.

* * *

feedburner_location

->[location](/docs/api/admin-graphql/latest/objects/BlogFeed#field-BlogFeed.fields.location)

The URL that points to the FeedBurner location for blogs that have FeedBurner enabled. Google has stopped supporting FeedBurner, and new or existing blogs that are not already integrated with FeedBurner can't use the service. This property will default to blank unless FeedBurner is enabled

* * *

handle

->[handle](/docs/api/admin-graphql/latest/objects/Blog#field-Blog.fields.handle)

A human-friendly unique string that is automatically generated from the title if no handle is sent during the creation of a blog. Duplicate handles are appended with an incremental number, for example, `blog-2`. The handle is customizable and is used by the Liquid templating language to refer to the blog. If you change the handle of a blog, then it can negatively affect the SEO of the shop. We recommend that you create a URL redirect to avoid any SEO issues.

* * *

id

read-only**read-only**

->[id](/docs/api/admin-graphql/latest/objects/Blog#field-Blog.fields.id)

A unique numeric identifier for the blog.

* * *

metafields

array**array**

write-only**write-only**

->[metafields](/docs/api/admin-graphql/latest/objects/Blog#field-Blog.fields.metafields)

Attaches additional metadata to a store's resources:

Show metafields properties

  * **key (required)** : Identifier for the metafield (maximum of 30 characters).
  * **namespace (required)** : Container for a set of metadata. Namespaces help distinguish between metadata you created and metadata created by another individual with a similar namespace (maximum of 20 characters).
  * **value (required)** : Information to be stored as metadata.
  * **type (required)** : The metafield's information type. Refer to the [full list of types](/apps/metafields/types).
  * **description (optional)** : Additional information about the metafield.


For more information on attaching metadata to Shopify resources, see the [Metafield](/api/admin-rest/latest/resources/metafield) resource.

* * *

tags

read-only**read-only**

->[tags](/docs/api/admin-graphql/latest/objects/Blog#field-Blog.fields.tags)

A list of tags associated with the 200 most recent blog articles. Tags are additional short descriptors formatted as a string of comma-separated values. For example, if an article has three tags: tag1, tag2, tag3. Tags are limited to 255 characters.

* * *

template_suffix

->[templateSuffix](/docs/api/admin-graphql/latest/objects/Blog#field-Blog.fields.templateSuffix)

States the name of the template a blog is using if it is using an alternate template. If a blog is using the default blog.liquid template, the value returned is "null".

* * *

title

->[title](/docs/api/admin-graphql/latest/objects/Blog#field-Blog.fields.title)

The title of the blog.

* * *

updated_at

read-only**read-only**

->[updatedAt](/docs/api/admin-graphql/latest/objects/Blog#field-Blog.fields.updatedAt)

The date and time when changes were last made to the blog's properties. Note that this is not updated when creating, modifying or deleting articles in the blog. The API returns this value in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601).

* * *

admin_graphql_api_id

read-only**read-only**

->[id](/docs/api/admin-graphql/latest/objects/Blog#field-Blog.fields.id)

The GraphQL GID of the blog.

* * *

Was this section helpful?

YesNo

{}

## The Blog resource

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

{

"commentable": "no",

"created_at": "2012-03-13T16:09:54-04:00",

"feedburner": null,

"feedburner_location": null,

"handle": "apple-blog",

"id": 241253187,

"tags": "tagged",

"template_suffix": null,

"title": "My Blog",

"updated_at": "2021-12-01T14:52:12-04:00",

"admin_graphql_api_id": "gid://shopify/OnlineStoreBlog/241253187"

}

* * *

##

[Anchor to POST request, Create a new Blog](/docs/api/admin-rest/latest/resources/blog#post-blogs)

post

Create a new Blog

[blogCreate](/docs/api/admin-graphql/latest/mutations/blogCreate?example=create-a-new-blog)

Create a new blog

###

[Anchor to Parameters of Create a new Blog](/docs/api/admin-rest/latest/resources/blog#post-blogs-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

title

required**required**

The title of the blog. Maximum length: 255 characters.

* * *

Was this section helpful?

YesNo

###

[Anchor to post-blogs-examples](/docs/api/admin-rest/latest/resources/blog#post-blogs-examples)Examples

Create a new empty blog

Request body

blog

Blog resource**Blog resource**

Show blog properties

blog.title:"Apple main blog"

->[title](/docs/api/admin-graphql/latest/input-objects/BlogCreateInput#fields-title)

The title of the blog.

Create a new empty blog with a metafield

Request body

blog

Blog resource**Blog resource**

Show blog properties

blog.title:"Apple main blog"

->[title](/docs/api/admin-graphql/latest/input-objects/BlogCreateInput#fields-title)

The title of the blog.

blog.metafields:[{"key":"sponsor","value":"Shopify","type":"single_line_text_field","namespace":"global"}]

array**array**

write-only**write-only**

->[metafields](/docs/api/admin-graphql/latest/input-objects/BlogCreateInput#fields-metafields)

Attaches additional metadata to a store's resources:

Show metafields properties

  * **key (required)** : Identifier for the metafield (maximum of 30 characters).
  * **namespace (required)** : Container for a set of metadata. Namespaces help distinguish between metadata you created and metadata created by another individual with a similar namespace (maximum of 20 characters).
  * **value (required)** : Information to be stored as metadata.
  * **type (required)** : The metafield's information type. Refer to the [full list of types](/apps/metafields/types).
  * **description (optional)** : Additional information about the metafield.


For more information on attaching metadata to Shopify resources, see the [Metafield](/api/admin-rest/latest/resources/metafield) resource.

Trying to create a blog without a title will return an error

Was this section helpful?

YesNo

post

## /admin/api/2026-01/blogs.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"blog":{"title":"Apple main blog"}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/blogs.json" \

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

"blog": {

"id": 1008414255,

"handle": "apple-main-blog",

"title": "Apple main blog",

"updated_at": "2026-01-09T17:29:09-05:00",

"commentable": "no",

"feedburner": null,

"feedburner_location": null,

"created_at": "2026-01-09T17:29:09-05:00",

"template_suffix": null,

"tags": "",

"admin_graphql_api_id": "gid://shopify/Blog/1008414255"

}

}

### examples

  * #### Create a new empty blog

#####

        curl -d '{"blog":{"title":"Apple main blog"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/blogs.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const blog = new admin.rest.resources.Blog({session: session});

        blog.title = "Apple main blog";
        await blog.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        blog = ShopifyAPI::Blog.new(session: test_session)
        blog.title = "Apple main blog"
        blog.save!

#####

        // Session is built by the OAuth process

        const blog = new shopify.rest.Blog({session: session});
        blog.title = "Apple main blog";
        await blog.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"blog":{"id":1008414255,"handle":"apple-main-blog","title":"Apple main blog","updated_at":"2026-01-09T17:29:09-05:00","commentable":"no","feedburner":null,"feedburner_location":null,"created_at":"2026-01-09T17:29:09-05:00","template_suffix":null,"tags":"","admin_graphql_api_id":"gid://shopify/Blog/1008414255"}}

  * #### Create a new empty blog with a metafield

#####

        curl -d '{"blog":{"title":"Apple main blog","metafields":[{"key":"sponsor","value":"Shopify","type":"single_line_text_field","namespace":"global"}]}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/blogs.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const blog = new admin.rest.resources.Blog({session: session});

        blog.title = "Apple main blog";
        blog.metafields = [
          {
            "key": "sponsor",
            "value": "Shopify",
            "type": "single_line_text_field",
            "namespace": "global"
          }
        ];
        await blog.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        blog = ShopifyAPI::Blog.new(session: test_session)
        blog.title = "Apple main blog"
        blog.metafields = [
          {
            "key" => "sponsor",
            "value" => "Shopify",
            "type" => "single_line_text_field",
            "namespace" => "global"
          }
        ]
        blog.save!

#####

        // Session is built by the OAuth process

        const blog = new shopify.rest.Blog({session: session});
        blog.title = "Apple main blog";
        blog.metafields = [
          {
            "key": "sponsor",
            "value": "Shopify",
            "type": "single_line_text_field",
            "namespace": "global"
          }
        ];
        await blog.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"blog":{"id":1008414253,"handle":"apple-main-blog","title":"Apple main blog","updated_at":"2026-01-09T17:28:56-05:00","commentable":"no","feedburner":null,"feedburner_location":null,"created_at":"2026-01-09T17:28:56-05:00","template_suffix":null,"tags":"","admin_graphql_api_id":"gid://shopify/Blog/1008414253"}}

  * #### Trying to create a blog without a title will return an error

#####

        curl -d '{"blog":{"body":"foobar"}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/blogs.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const blog = new admin.rest.resources.Blog({session: session});

        blog.body = "foobar";
        await blog.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        blog = ShopifyAPI::Blog.new(session: test_session)
        blog.body = "foobar"
        blog.save!

#####

        // Session is built by the OAuth process

        const blog = new shopify.rest.Blog({session: session});
        blog.body = "foobar";
        await blog.save({
          update: true,
        });

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":{"title":["can't be blank"]}}


* * *

##

[Anchor to GET request, Retrieve a list of all blogs](/docs/api/admin-rest/latest/resources/blog#get-blogs)

get

Retrieve a list of all blogs

[blogs](/docs/api/admin-graphql/latest/queries/blogs?example=retrieve-a-list-of-all-blogs)

Retrieve a list of all blogs. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

###

[Anchor to Parameters of Retrieve a list of all blogs](/docs/api/admin-rest/latest/resources/blog#get-blogs-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

fields

comma-separated list of fields to include in the response

* * *

handle

Filter by blog handle

* * *

count

≤ 250**≤ 250**

default 50**default 50**

The maximum number of results to retrieve.

* * *

after_id

Restrict results to after the specified ID

* * *

Was this section helpful?

YesNo

###

[Anchor to get-blogs-examples](/docs/api/admin-rest/latest/resources/blog#get-blogs-examples)Examples

Get all blogs for a shop

Get all blogs for a shop after a specified ID

Query parameters

after_id=241253187

Restrict results to after the specified ID

Was this section helpful?

YesNo

get

## /admin/api/2026-01/blogs.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/blogs.json" \

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

"blogs": [

{

"id": 382285388,

"handle": "banana-blog",

"title": "A Gnu Blog",

"updated_at": "2006-02-02T19:00:00-05:00",

"commentable": "no",

"feedburner": null,

"feedburner_location": null,

"created_at": "2026-01-09T17:04:11-05:00",

"template_suffix": null,

"tags": "",

"admin_graphql_api_id": "gid://shopify/Blog/382285388"

},

{

"id": 241253187,

"handle": "apple-blog",

"title": "Mah Blog",

"updated_at": "2006-02-01T19:00:00-05:00",

"commentable": "no",

"feedburner": null,

"feedburner_location": null,

"created_at": "2026-01-09T17:04:11-05:00",

"template_suffix": null,

"tags": "Announcing, Mystery",

"admin_graphql_api_id": "gid://shopify/Blog/241253187"

}

]

}

### examples

  * #### Get all blogs for a shop

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/blogs.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Blog.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Blog.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Blog.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"blogs":[{"id":382285388,"handle":"banana-blog","title":"A Gnu Blog","updated_at":"2006-02-02T19:00:00-05:00","commentable":"no","feedburner":null,"feedburner_location":null,"created_at":"2026-01-09T17:04:11-05:00","template_suffix":null,"tags":"","admin_graphql_api_id":"gid://shopify/Blog/382285388"},{"id":241253187,"handle":"apple-blog","title":"Mah Blog","updated_at":"2006-02-01T19:00:00-05:00","commentable":"no","feedburner":null,"feedburner_location":null,"created_at":"2026-01-09T17:04:11-05:00","template_suffix":null,"tags":"Announcing, Mystery","admin_graphql_api_id":"gid://shopify/Blog/241253187"}]}

  * #### Get all blogs for a shop after a specified ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/blogs.json?after_id=241253187" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Blog.all({
          session: session,
          after_id: "241253187",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Blog.all(
          session: test_session,
          after_id: "241253187",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Blog.all({
          session: session,
          after_id: "241253187",
        });

#### response

        HTTP/1.1 200 OK{"blogs":[{"id":382285388,"handle":"banana-blog","title":"A Gnu Blog","updated_at":"2006-02-02T19:00:00-05:00","commentable":"no","feedburner":null,"feedburner_location":null,"created_at":"2026-01-09T17:04:11-05:00","template_suffix":null,"tags":"","admin_graphql_api_id":"gid://shopify/Blog/382285388"},{"id":1008414254,"handle":"apple-main-blog","title":"Apple main blog","updated_at":"2026-01-09T17:28:57-05:00","commentable":"no","feedburner":null,"feedburner_location":null,"created_at":"2026-01-09T17:28:57-05:00","template_suffix":null,"tags":"","admin_graphql_api_id":"gid://shopify/Blog/1008414254"}]}


* * *

##

[Anchor to GET request, Receive a single Blog](/docs/api/admin-rest/latest/resources/blog#get-blogs-blog-id)

get

Receive a single Blog

[blog](/docs/api/admin-graphql/latest/queries/blog?example=receive-a-single-blog)

Get a single blog by its ID

###

[Anchor to Parameters of Receive a single Blog](/docs/api/admin-rest/latest/resources/blog#get-blogs-blog-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

blog_id

string**string**

required**required**

* * *

fields

comma-separated list of fields to include in the response

* * *

Was this section helpful?

YesNo

###

[Anchor to get-blogs-blog-id-examples](/docs/api/admin-rest/latest/resources/blog#get-blogs-blog-id-examples)Examples

Get a single blog

Path parameters

blog_id=241253187

string**string**

required**required**

Get the id and title of a single blog

Path parameters

blog_id=241253187

string**string**

required**required**

Query parameters

fields=id,title

comma-separated list of fields to include in the response

Was this section helpful?

YesNo

get

## /admin/api/2026-01/blogs/241253187.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/blogs/241253187.json" \

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

"blog": {

"id": 241253187,

"handle": "apple-blog",

"title": "Mah Blog",

"updated_at": "2006-02-01T19:00:00-05:00",

"commentable": "no",

"feedburner": null,

"feedburner_location": null,

"created_at": "2026-01-09T17:04:11-05:00",

"template_suffix": null,

"tags": "Announcing, Mystery",

"admin_graphql_api_id": "gid://shopify/Blog/241253187"

}

}

### examples

  * #### Get a single blog

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/blogs/241253187.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Blog.find({
          session: session,
          id: 241253187,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Blog.find(
          session: test_session,
          id: 241253187,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Blog.find({
          session: session,
          id: 241253187,
        });

#### response

        HTTP/1.1 200 OK{"blog":{"id":241253187,"handle":"apple-blog","title":"Mah Blog","updated_at":"2006-02-01T19:00:00-05:00","commentable":"no","feedburner":null,"feedburner_location":null,"created_at":"2026-01-09T17:04:11-05:00","template_suffix":null,"tags":"Announcing, Mystery","admin_graphql_api_id":"gid://shopify/Blog/241253187"}}

  * #### Get the id and title of a single blog

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/blogs/241253187.json?fields=id%2Ctitle" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Blog.find({
          session: session,
          id: 241253187,
          fields: "id,title",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Blog.find(
          session: test_session,
          id: 241253187,
          fields: "id,title",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Blog.find({
          session: session,
          id: 241253187,
          fields: "id,title",
        });

#### response

        HTTP/1.1 200 OK{"blog":{"id":241253187,"title":"Mah Blog"}}


* * *

##

[Anchor to GET request, Receive a count of all Blogs](/docs/api/admin-rest/latest/resources/blog#get-blogs-count)

get

Receive a count of all Blogs

[blogsCount](/docs/api/admin-graphql/latest/queries/blogsCount?example=receive-a-count-of-all-blogs)

Get a count of all blogs

###

[Anchor to Parameters of Receive a count of all Blogs](/docs/api/admin-rest/latest/resources/blog#get-blogs-count-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to get-blogs-count-examples](/docs/api/admin-rest/latest/resources/blog#get-blogs-count-examples)Examples

Get the blogs count for a shop

Was this section helpful?

YesNo

get

## /admin/api/2026-01/blogs/count.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/blogs/count.json" \

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

"count": 2

}

### examples

  * #### Get the blogs count for a shop

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/blogs/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Blog.count({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Blog.count(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Blog.count({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"count":2}


* * *

##

[Anchor to PUT request, Modify an existing Blog](/docs/api/admin-rest/latest/resources/blog#put-blogs-blog-id)

put

Modify an existing Blog

[blogUpdate](/docs/api/admin-graphql/latest/mutations/blogUpdate?example=modify-an-existing-blog)

Update a blog

###

[Anchor to Parameters of Modify an existing Blog](/docs/api/admin-rest/latest/resources/blog#put-blogs-blog-id-parameters)Parameters

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

[Anchor to put-blogs-blog-id-examples](/docs/api/admin-rest/latest/resources/blog#put-blogs-blog-id-examples)Examples

Add a metafield to an existing blog

Path parameters

blog_id=241253187

string**string**

required**required**

Request body

blog

Blog resource**Blog resource**

Show blog properties

blog.id:241253187

read-only**read-only**

A unique numeric identifier for the blog.

blog.metafields:[{"key":"sponsor","value":"Shopify","type":"single_line_text_field","namespace":"global"}]

array**array**

write-only**write-only**

->[metafields](/docs/api/admin-graphql/latest/input-objects/BlogUpdateInput#fields-metafields)

Attaches additional metadata to a store's resources:

Show metafields properties

  * **key (required)** : Identifier for the metafield (maximum of 30 characters).
  * **namespace (required)** : Container for a set of metadata. Namespaces help distinguish between metadata you created and metadata created by another individual with a similar namespace (maximum of 20 characters).
  * **value (required)** : Information to be stored as metadata.
  * **type (required)** : The metafield's information type. Refer to the [full list of types](/apps/metafields/types).
  * **description (optional)** : Additional information about the metafield.


For more information on attaching metadata to Shopify resources, see the [Metafield](/api/admin-rest/latest/resources/metafield) resource.

Update an existing blog title

Path parameters

blog_id=241253187

string**string**

required**required**

Request body

blog

Blog resource**Blog resource**

Show blog properties

blog.id:241253187

read-only**read-only**

A unique numeric identifier for the blog.

blog.title:"IPod Updates"

->[title](/docs/api/admin-graphql/latest/input-objects/BlogUpdateInput#fields-title)

The title of the blog.

Update an existing blog title and handle and also activate comments

Path parameters

blog_id=241253187

string**string**

required**required**

Request body

blog

Blog resource**Blog resource**

Show blog properties

blog.id:241253187

read-only**read-only**

A unique numeric identifier for the blog.

blog.title:"IPod Updates"

->[title](/docs/api/admin-graphql/latest/input-objects/BlogUpdateInput#fields-title)

The title of the blog.

blog.handle:"ipod-updates"

->[handle](/docs/api/admin-graphql/latest/input-objects/BlogUpdateInput#fields-handle)

A human-friendly unique string that is automatically generated from the title if no handle is sent during the creation of a blog. Duplicate handles are appended with an incremental number, for example, `blog-2`. The handle is customizable and is used by the Liquid templating language to refer to the blog. If you change the handle of a blog, then it can negatively affect the SEO of the shop. We recommend that you create a URL redirect to avoid any SEO issues.

blog.commentable:"moderate"

->[commentPolicy](/docs/api/admin-graphql/latest/input-objects/BlogUpdateInput#fields-commentPolicy)

Indicates whether readers can post comments to the blog and if comments are moderated or not. Possible values are:

Show commentable properties

  * **no (default)** : Readers cannot post comments to blog articles.
  * **moderate** : Readers can post comments to blog articles, but comments must be moderated before they appear.
  * **yes** : Readers can post comments to blog articles without moderation.


Was this section helpful?

YesNo

put

## /admin/api/2026-01/blogs/241253187.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"blog":{"id":241253187,"metafields":[{"key":"sponsor","value":"Shopify","type":"single_line_text_field","namespace":"global"}]}}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/blogs/241253187.json" \

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

"blog": {

"title": "Mah Blog",

"handle": "apple-blog",

"commentable": "no",

"feedburner_location": null,

"feedburner": null,

"id": 241253187,

"updated_at": "2006-02-01T19:00:00-05:00",

"created_at": "2026-01-09T17:04:11-05:00",

"template_suffix": null,

"tags": "Announcing, Mystery",

"admin_graphql_api_id": "gid://shopify/Blog/241253187"

}

}

### examples

  * #### Add a metafield to an existing blog

#####

        curl -d '{"blog":{"id":241253187,"metafields":[{"key":"sponsor","value":"Shopify","type":"single_line_text_field","namespace":"global"}]}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/blogs/241253187.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const blog = new admin.rest.resources.Blog({session: session});

        blog.id = 241253187;
        blog.metafields = [
          {
            "key": "sponsor",
            "value": "Shopify",
            "type": "single_line_text_field",
            "namespace": "global"
          }
        ];
        await blog.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        blog = ShopifyAPI::Blog.new(session: test_session)
        blog.id = 241253187
        blog.metafields = [
          {
            "key" => "sponsor",
            "value" => "Shopify",
            "type" => "single_line_text_field",
            "namespace" => "global"
          }
        ]
        blog.save!

#####

        // Session is built by the OAuth process

        const blog = new shopify.rest.Blog({session: session});
        blog.id = 241253187;
        blog.metafields = [
          {
            "key": "sponsor",
            "value": "Shopify",
            "type": "single_line_text_field",
            "namespace": "global"
          }
        ];
        await blog.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"blog":{"title":"Mah Blog","handle":"apple-blog","commentable":"no","feedburner_location":null,"feedburner":null,"id":241253187,"updated_at":"2006-02-01T19:00:00-05:00","created_at":"2026-01-09T17:04:11-05:00","template_suffix":null,"tags":"Announcing, Mystery","admin_graphql_api_id":"gid://shopify/Blog/241253187"}}

  * #### Update an existing blog title

#####

        curl -d '{"blog":{"id":241253187,"title":"IPod Updates"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/blogs/241253187.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const blog = new admin.rest.resources.Blog({session: session});

        blog.id = 241253187;
        blog.title = "IPod Updates";
        await blog.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        blog = ShopifyAPI::Blog.new(session: test_session)
        blog.id = 241253187
        blog.title = "IPod Updates"
        blog.save!

#####

        // Session is built by the OAuth process

        const blog = new shopify.rest.Blog({session: session});
        blog.id = 241253187;
        blog.title = "IPod Updates";
        await blog.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"blog":{"title":"IPod Updates","handle":"apple-blog","commentable":"no","feedburner_location":null,"feedburner":null,"id":241253187,"updated_at":"2026-01-09T17:29:04-05:00","created_at":"2026-01-09T17:04:11-05:00","template_suffix":null,"tags":"Announcing, Mystery","admin_graphql_api_id":"gid://shopify/Blog/241253187"}}

  * #### Update an existing blog title and handle and also activate comments

#####

        curl -d '{"blog":{"id":241253187,"title":"IPod Updates","handle":"ipod-updates","commentable":"moderate"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/blogs/241253187.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const blog = new admin.rest.resources.Blog({session: session});

        blog.id = 241253187;
        blog.title = "IPod Updates";
        blog.handle = "ipod-updates";
        blog.commentable = "moderate";
        await blog.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        blog = ShopifyAPI::Blog.new(session: test_session)
        blog.id = 241253187
        blog.title = "IPod Updates"
        blog.handle = "ipod-updates"
        blog.commentable = "moderate"
        blog.save!

#####

        // Session is built by the OAuth process

        const blog = new shopify.rest.Blog({session: session});
        blog.id = 241253187;
        blog.title = "IPod Updates";
        blog.handle = "ipod-updates";
        blog.commentable = "moderate";
        await blog.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"blog":{"title":"IPod Updates","handle":"ipod-updates","commentable":"moderate","feedburner_location":null,"feedburner":null,"id":241253187,"updated_at":"2026-01-09T17:28:59-05:00","created_at":"2026-01-09T17:04:11-05:00","template_suffix":null,"tags":"Announcing, Mystery","admin_graphql_api_id":"gid://shopify/Blog/241253187"}}


* * *

##

[Anchor to DELETE request, Remove an existing Blog](/docs/api/admin-rest/latest/resources/blog#delete-blogs-blog-id)

del

Remove an existing Blog

[blogDelete](/docs/api/admin-graphql/latest/mutations/blogDelete?example=remove-an-existing-blog)

Delete a blog

###

[Anchor to Parameters of Remove an existing Blog](/docs/api/admin-rest/latest/resources/blog#delete-blogs-blog-id-parameters)Parameters

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

[Anchor to delete-blogs-blog-id-examples](/docs/api/admin-rest/latest/resources/blog#delete-blogs-blog-id-examples)Examples

Remove an existing blog from a shop

Path parameters

blog_id=241253187

string**string**

required**required**

Was this section helpful?

YesNo

del

## /admin/api/2026-01/blogs/241253187.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/blogs/241253187.json" \

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

  * #### Remove an existing blog from a shop

#####

        curl -X DELETE "https://your-development-store.myshopify.com/admin/api/2026-01/blogs/241253187.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Blog.delete({
          session: session,
          id: 241253187,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Blog.delete(
          session: test_session,
          id: 241253187,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Blog.delete({
          session: session,
          id: 241253187,
        });

#### response

        HTTP/1.1 200 OK{}