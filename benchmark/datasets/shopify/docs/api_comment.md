# Comment

*Source: https://shopify.dev/docs/api/admin-rest/2026-01/resources/comment*

---

Choose a version:

unstable 2026-04 release candidate2026-01 latest2025-10 2025-07 2025-04

2026-01latest

# Comment

Ask assistant

Requires `content` access scope.

**Requires `content` access scope.:**

Requires access to [protected customer data](https://shopify.dev/apps/store/data-protection/protected-customer-data).

**Requires access to [protected customer data](https://shopify.dev/apps/store/data-protection/protected-customer-data).:**

A comment is a reader's response to an article in a blog. Comments appear on the article page in reverse chronological order, typically after the article body. Just as a blog can have any number of articles, an article can have any number of comments.

Article comments are a target for spammers, so Shopify blogs use a spam detection system to identify comments that are likely to be spam. Shop owners can also can mark comments as spam or not spam. Comments that are marked as spam are removed from the Shopify admin and don't appear in the blog.

Was this section helpful?

YesNo

#

## Endpoints

  * [post/admin/api/latest/comments.json](/docs/api/admin-rest/latest/resources/comment#post-comments)

Creates a comment for an article

deprecated

**

deprecated

**

  * [ post/admin/api/latest/comments/{comment_id}/approve.json](/docs/api/admin-rest/latest/resources/comment#post-comments-comment-id-approve)

Approves a comment

[commentApprove](/docs/api/admin-graphql/latest/mutations/commentApprove?example=approves-a-comment)

  * [post/admin/api/latest/comments/{comment_id}/not_spam.json](/docs/api/admin-rest/latest/resources/comment#post-comments-comment-id-not-spam)

Marks a comment as not spam

[commentNotSpam](/docs/api/admin-graphql/latest/mutations/commentNotSpam?example=marks-a-comment-as-not-spam)

  * [post/admin/api/latest/comments/{comment_id}/remove.json](/docs/api/admin-rest/latest/resources/comment#post-comments-comment-id-remove)

Removes a comment

[commentDelete](/docs/api/admin-graphql/latest/mutations/commentDelete?example=removes-a-comment)

  * [post/admin/api/latest/comments/{comment_id}/restore.json](/docs/api/admin-rest/latest/resources/comment#post-comments-comment-id-restore)

Restores a previously removed comment

deprecated

**

deprecated

**

  * [ post/admin/api/latest/comments/{comment_id}/spam.json](/docs/api/admin-rest/latest/resources/comment#post-comments-comment-id-spam)

Marks a comment as spam

[commentSpam](/docs/api/admin-graphql/latest/mutations/commentSpam?example=marks-a-comment-as-spam)

  * [get/admin/api/latest/comments.json?since_id=118373535](/docs/api/admin-rest/latest/resources/comment#get-comments?since-id=118373535)

Retrieves a list of comments

[comments](/docs/api/admin-graphql/latest/queries/comments?example=retrieves-a-list-of-comments)

  * [get/admin/api/latest/comments/{comment_id}.json](/docs/api/admin-rest/latest/resources/comment#get-comments-comment-id)

Retrieves a single comment by its ID

[comment](/docs/api/admin-graphql/latest/queries/comment?example=retrieves-a-single-comment-by-its-id)

  * [get/admin/api/latest/comments/count.json?article_id=134645308&blog_id=241253187](/docs/api/admin-rest/latest/resources/comment#get-comments-count?article-id=134645308&blog-id=241253187)

Retrieves a count of comments

[article](/docs/api/admin-graphql/latest/queries/article)

  * [put/admin/api/latest/comments/{comment_id}.json](/docs/api/admin-rest/latest/resources/comment#put-comments-comment-id)

Updates a comment of an article

deprecated

**

deprecated

**


* * *

[ Anchor to ](/docs/api/admin-rest/latest/resources/comment#resource-object)

## The Comment resource

[Anchor to ](/docs/api/admin-rest/latest/resources/comment#resource-object-properties)

### Properties

* * *

article_id

A unique numeric identifier for the article that the comment belongs to.

* * *

author

[](/apps/store/data-protection/protected-customer-data)

The name of the author of the comment.

* * *

blog_id

A unique numeric identifier for the blog containing the article that the comment belongs to.

* * *

body

The basic [Textile markup](https://en.wikipedia.org/wiki/Textile_\(markup_language\)) of a comment.

* * *

body_html

The text of the comment, complete with HTML markup.

* * *

created_at

read-only**read-only**

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the comment was created.

* * *

email

[](/apps/store/data-protection/protected-customer-data)

The email address of the author of the comment.

* * *

id

read-only**read-only**

A unique numeric identifier for the comment.

* * *

ip

[](/apps/store/data-protection/protected-customer-data)

The IP address from which the comment was posted.

* * *

published_at

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the comment was published.

* * *

status

read-only**read-only**

The status of the comment. Valid values:

Show status properties

  * **pending** : The comment has been created but is awaiting spam detection. Depending on the result of the spam detection and the shop owner's comment preferences, this property will be transitioned to either `spam`, `unapproved`, or `approved`.
  * **unapproved (default)** : The comment is awaiting approval by the shop owner. It's not visible to the readers of the blog.
  * **published** : The comment has been approved (if the blog requires comments to be approved) and is visible to readers of the blog.
  * **spam** : The comment has been marked as spam and removed from the Shopify admin. It's not visible to readers of the blog.
  * **removed** : The comment has been removed by the shop owner. It's not visible to readers of the blog.


* * *

updated_at

read-only**read-only**

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the comment was last modified. When the comment is created, this matches the value of `created_at`. If the blog requires comments to be approved, then this value is updated to the date and time when the comment is approved.

* * *

user_agent

The user agent string provided by the software used to create the comment (usually a browser).

* * *

Was this section helpful?

YesNo

{}

## The Comment resource

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

{

"article_id": 134645308,

"author": "Soleone",

"blog_id": 241253187,

"body": "This is a _great_ article.",

"body_html": "<p>This is a <em>great</em> article.</p>",

"created_at": "2012-08-24T14:01:46-04:00",

"email": "soleone@example.net",

"id": 653537639,

"ip": "127.0.0.1",

"published_at": "2012-08-24T14:02:00-04:00",

"status": "unapproved",

"updated_at": "2012-08-24T14:02:00-04:00",

"user_agent": "Mozilla/5.0"

}

* * *

##

[Anchor to POST request, Creates a comment for an article](/docs/api/admin-rest/latest/resources/comment#post-comments)

post

Creates a comment for an article

deprecated**deprecated**

Creates a comment for an article

###

[Anchor to Parameters of Creates a comment for an article](/docs/api/admin-rest/latest/resources/comment#post-comments-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-comments-examples](/docs/api/admin-rest/latest/resources/comment#post-comments-examples)Examples

Create a comment for an article of a blog using basic Textile markup

Request body

comment[](/apps/store/data-protection/protected-customer-data)

Comment resource**Comment resource**

Show comment properties

comment.body:"I like comments\nAnd I like posting them *RESTfully*."

The basic [Textile markup](https://en.wikipedia.org/wiki/Textile_\(markup_language\)) of a comment.

comment.author:"Your name"[](/apps/store/data-protection/protected-customer-data)

The name of the author of the comment.

comment.email:"your@email.com"[](/apps/store/data-protection/protected-customer-data)

The email address of the author of the comment.

comment.ip:"107.20.160.121"[](/apps/store/data-protection/protected-customer-data)

The IP address from which the comment was posted.

comment.blog_id:241253187

A unique numeric identifier for the blog containing the article that the comment belongs to.

comment.article_id:134645308

A unique numeric identifier for the article that the comment belongs to.

Creating a comment without a body, author, and email fails and returns an error

Request body

comment[](/apps/store/data-protection/protected-customer-data)

Comment resource**Comment resource**

Show comment properties

comment.article_id:134645308

A unique numeric identifier for the article that the comment belongs to.

Was this section helpful?

YesNo

post

## /admin/api/2026-01/comments.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"comment":{"body":"I like comments\nAnd I like posting them *RESTfully*.","author":"Your name","email":"your@email.com","ip":"107.20.160.121","blog_id":241253187,"article_id":134645308}}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/comments.json" \

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

HTTP/1.1 201 Created

{

"comment": {

"id": 757536354,

"body": "I like comments\nAnd I like posting them *RESTfully*.",

"body_html": "<p>I like comments<br>\nAnd I like posting them <strong>RESTfully</strong>.</p>",

"author": "Your name",

"email": "your@email.com",

"status": "pending",

"article_id": 134645308,

"blog_id": 241253187,

"created_at": "2026-01-09T22:34:55-05:00",

"updated_at": "2026-01-09T22:34:55-05:00",

"ip": "107.20.160.121",

"user_agent": null,

"published_at": null

}

}

### examples

  * #### Create a comment for an article of a blog using basic Textile markup

#####

        curl -d '{"comment":{"body":"I like comments\nAnd I like posting them *RESTfully*.","author":"Your name","email":"your@email.com","ip":"107.20.160.121","blog_id":241253187,"article_id":134645308}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/comments.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const comment = new admin.rest.resources.Comment({session: session});

        comment.body = "I like comments\nAnd I like posting them *RESTfully*.";
        comment.author = "Your name";
        comment.email = "your@email.com";
        comment.ip = "107.20.160.121";
        comment.blog_id = 241253187;
        comment.article_id = 134645308;
        await comment.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        comment = ShopifyAPI::Comment.new(session: test_session)
        comment.body = "I like comments\nAnd I like posting them *RESTfully*."
        comment.author = "Your name"
        comment.email = "your@email.com"
        comment.ip = "107.20.160.121"
        comment.blog_id = 241253187
        comment.article_id = 134645308
        comment.save!

#####

        // Session is built by the OAuth process

        const comment = new shopify.rest.Comment({session: session});
        comment.body = "I like comments\nAnd I like posting them *RESTfully*.";
        comment.author = "Your name";
        comment.email = "your@email.com";
        comment.ip = "107.20.160.121";
        comment.blog_id = 241253187;
        comment.article_id = 134645308;
        await comment.save({
          update: true,
        });

#### response

        HTTP/1.1 201 Created{"comment":{"id":757536354,"body":"I like comments\nAnd I like posting them *RESTfully*.","body_html":"<p>I like comments<br>\nAnd I like posting them <strong>RESTfully</strong>.</p>","author":"Your name","email":"your@email.com","status":"pending","article_id":134645308,"blog_id":241253187,"created_at":"2026-01-09T22:34:55-05:00","updated_at":"2026-01-09T22:34:55-05:00","ip":"107.20.160.121","user_agent":null,"published_at":null}}

  * #### Creating a comment without a body, author, and email fails and returns an error

#####

        curl -d '{"comment":{"article_id":134645308}}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/comments.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const comment = new admin.rest.resources.Comment({session: session});

        comment.article_id = 134645308;
        await comment.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        comment = ShopifyAPI::Comment.new(session: test_session)
        comment.article_id = 134645308
        comment.save!

#####

        // Session is built by the OAuth process

        const comment = new shopify.rest.Comment({session: session});
        comment.article_id = 134645308;
        await comment.save({
          update: true,
        });

#### response

        HTTP/1.1 422 Unprocessable Entity{"errors":{"author":["can't be blank"],"body":["can't be blank"],"email":["must be formatted as an email"]}}


* * *

##

[Anchor to POST request, Approves a comment](/docs/api/admin-rest/latest/resources/comment#post-comments-comment-id-approve)

post

Approves a comment

[commentApprove](/docs/api/admin-graphql/latest/mutations/commentApprove?example=approves-a-comment)

Approves a comment

###

[Anchor to Parameters of Approves a comment](/docs/api/admin-rest/latest/resources/comment#post-comments-comment-id-approve-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

comment_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-comments-comment-id-approve-examples](/docs/api/admin-rest/latest/resources/comment#post-comments-comment-id-approve-examples)Examples

Approve a comment and publish it to the blog

Path parameters

comment_id=653537639

string**string**

required**required**

Was this section helpful?

YesNo

post

## /admin/api/2026-01/comments/653537639/approve.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/comments/653537639/approve.json" \

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

"published_at": "2026-01-09T22:34:33-05:00",

"status": "published",

"blog_id": 241253187,

"article_id": 134645308,

"author": "Soleone",

"body": "Hi author, I really _like_ what you're doing there.",

"email": "soleone@example.net",

"body_html": "<p>Hi author, I really <em>like</em> what you're doing there.</p>",

"id": 653537639,

"created_at": "2026-01-09T22:32:40-05:00",

"updated_at": "2026-01-09T22:34:33-05:00",

"ip": "127.0.0.1",

"user_agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1"

}

### examples

  * #### Approve a comment and publish it to the blog

#####

        curl -d '{}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/comments/653537639/approve.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const comment = new admin.rest.resources.Comment({session: session});

        comment.id = 653537639;
        await comment.approve({});

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        comment = ShopifyAPI::Comment.new(session: test_session)
        comment.id = 653537639
        comment.approve(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        const comment = new shopify.rest.Comment({session: session});
        comment.id = 653537639;
        await comment.approve({});

#### response

        HTTP/1.1 200 OK{"published_at":"2026-01-09T22:34:33-05:00","status":"published","blog_id":241253187,"article_id":134645308,"author":"Soleone","body":"Hi author, I really _like_ what you're doing there.","email":"soleone@example.net","body_html":"<p>Hi author, I really <em>like</em> what you're doing there.</p>","id":653537639,"created_at":"2026-01-09T22:32:40-05:00","updated_at":"2026-01-09T22:34:33-05:00","ip":"127.0.0.1","user_agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1"}


* * *

##

[Anchor to POST request, Marks a comment as not spam](/docs/api/admin-rest/latest/resources/comment#post-comments-comment-id-not-spam)

post

Marks a comment as not spam

[commentNotSpam](/docs/api/admin-graphql/latest/mutations/commentNotSpam?example=marks-a-comment-as-not-spam)

Marks a comment as not spam

###

[Anchor to Parameters of Marks a comment as not spam](/docs/api/admin-rest/latest/resources/comment#post-comments-comment-id-not-spam-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

comment_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-comments-comment-id-not-spam-examples](/docs/api/admin-rest/latest/resources/comment#post-comments-comment-id-not-spam-examples)Examples

Mark a comment as not spam, restoring it to an unapproved or published state

Path parameters

comment_id=653537639

string**string**

required**required**

Was this section helpful?

YesNo

post

## /admin/api/2026-01/comments/653537639/not_spam.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/comments/653537639/not_spam.json" \

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

"published_at": "2026-01-09T22:34:53-05:00",

"status": "published",

"blog_id": 241253187,

"article_id": 134645308,

"author": "Soleone",

"body": "Hi author, I really _like_ what you're doing there.",

"email": "soleone@example.net",

"body_html": "<p>Hi author, I really <em>like</em> what you're doing there.</p>",

"id": 653537639,

"created_at": "2026-01-09T22:32:40-05:00",

"updated_at": "2026-01-09T22:34:53-05:00",

"ip": "127.0.0.1",

"user_agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1"

}

### examples

  * #### Mark a comment as not spam, restoring it to an unapproved or published state

#####

        curl -d '{}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/comments/653537639/not_spam.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const comment = new admin.rest.resources.Comment({session: session});

        comment.id = 653537639;
        await comment.not_spam({});

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        comment = ShopifyAPI::Comment.new(session: test_session)
        comment.id = 653537639
        comment.not_spam(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        const comment = new shopify.rest.Comment({session: session});
        comment.id = 653537639;
        await comment.not_spam({});

#### response

        HTTP/1.1 200 OK{"published_at":"2026-01-09T22:34:53-05:00","status":"published","blog_id":241253187,"article_id":134645308,"author":"Soleone","body":"Hi author, I really _like_ what you're doing there.","email":"soleone@example.net","body_html":"<p>Hi author, I really <em>like</em> what you're doing there.</p>","id":653537639,"created_at":"2026-01-09T22:32:40-05:00","updated_at":"2026-01-09T22:34:53-05:00","ip":"127.0.0.1","user_agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1"}


* * *

##

[Anchor to POST request, Removes a comment](/docs/api/admin-rest/latest/resources/comment#post-comments-comment-id-remove)

post

Removes a comment

[commentDelete](/docs/api/admin-graphql/latest/mutations/commentDelete?example=removes-a-comment)

Removes a comment

###

[Anchor to Parameters of Removes a comment](/docs/api/admin-rest/latest/resources/comment#post-comments-comment-id-remove-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

comment_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-comments-comment-id-remove-examples](/docs/api/admin-rest/latest/resources/comment#post-comments-comment-id-remove-examples)Examples

Remove a comment

Path parameters

comment_id=653537639

string**string**

required**required**

Was this section helpful?

YesNo

post

## /admin/api/2026-01/comments/653537639/remove.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/comments/653537639/remove.json" \

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

"published_at": null,

"status": "removed",

"blog_id": 241253187,

"article_id": 134645308,

"author": "Soleone",

"body": "Hi author, I really _like_ what you're doing there.",

"email": "soleone@example.net",

"body_html": "<p>Hi author, I really <em>like</em> what you're doing there.</p>",

"id": 653537639,

"created_at": "2026-01-09T22:32:40-05:00",

"updated_at": "2026-01-09T22:35:00-05:00",

"ip": "127.0.0.1",

"user_agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1"

}

### examples

  * #### Remove a comment

#####

        curl -d '{}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/comments/653537639/remove.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const comment = new admin.rest.resources.Comment({session: session});

        comment.id = 653537639;
        await comment.remove({});

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        comment = ShopifyAPI::Comment.new(session: test_session)
        comment.id = 653537639
        comment.remove(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        const comment = new shopify.rest.Comment({session: session});
        comment.id = 653537639;
        await comment.remove({});

#### response

        HTTP/1.1 200 OK{"published_at":null,"status":"removed","blog_id":241253187,"article_id":134645308,"author":"Soleone","body":"Hi author, I really _like_ what you're doing there.","email":"soleone@example.net","body_html":"<p>Hi author, I really <em>like</em> what you're doing there.</p>","id":653537639,"created_at":"2026-01-09T22:32:40-05:00","updated_at":"2026-01-09T22:35:00-05:00","ip":"127.0.0.1","user_agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1"}


* * *

##

[Anchor to POST request, Restores a previously removed comment](/docs/api/admin-rest/latest/resources/comment#post-comments-comment-id-restore)

post

Restores a previously removed comment

deprecated**deprecated**

Restores a previously removed comment

###

[Anchor to Parameters of Restores a previously removed comment](/docs/api/admin-rest/latest/resources/comment#post-comments-comment-id-restore-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

comment_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-comments-comment-id-restore-examples](/docs/api/admin-rest/latest/resources/comment#post-comments-comment-id-restore-examples)Examples

Restore a removed comment

Path parameters

comment_id=653537639

string**string**

required**required**

Was this section helpful?

YesNo

post

## /admin/api/2026-01/comments/653537639/restore.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/comments/653537639/restore.json" \

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

"published_at": "2026-01-09T22:34:39-05:00",

"status": "published",

"blog_id": 241253187,

"article_id": 134645308,

"author": "Soleone",

"body": "Hi author, I really _like_ what you're doing there.",

"email": "soleone@example.net",

"body_html": "<p>Hi author, I really <em>like</em> what you're doing there.</p>",

"id": 653537639,

"created_at": "2026-01-09T22:32:40-05:00",

"updated_at": "2026-01-09T22:34:39-05:00",

"ip": "127.0.0.1",

"user_agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1"

}

### examples

  * #### Restore a removed comment

#####

        curl -d '{}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/comments/653537639/restore.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const comment = new admin.rest.resources.Comment({session: session});

        comment.id = 653537639;
        await comment.restore({});

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        comment = ShopifyAPI::Comment.new(session: test_session)
        comment.id = 653537639
        comment.restore(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        const comment = new shopify.rest.Comment({session: session});
        comment.id = 653537639;
        await comment.restore({});

#### response

        HTTP/1.1 200 OK{"published_at":"2026-01-09T22:34:39-05:00","status":"published","blog_id":241253187,"article_id":134645308,"author":"Soleone","body":"Hi author, I really _like_ what you're doing there.","email":"soleone@example.net","body_html":"<p>Hi author, I really <em>like</em> what you're doing there.</p>","id":653537639,"created_at":"2026-01-09T22:32:40-05:00","updated_at":"2026-01-09T22:34:39-05:00","ip":"127.0.0.1","user_agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1"}


* * *

##

[Anchor to POST request, Marks a comment as spam](/docs/api/admin-rest/latest/resources/comment#post-comments-comment-id-spam)

post

Marks a comment as spam

[commentSpam](/docs/api/admin-graphql/latest/mutations/commentSpam?example=marks-a-comment-as-spam)

Marks a comment as spam

###

[Anchor to Parameters of Marks a comment as spam](/docs/api/admin-rest/latest/resources/comment#post-comments-comment-id-spam-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

comment_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to post-comments-comment-id-spam-examples](/docs/api/admin-rest/latest/resources/comment#post-comments-comment-id-spam-examples)Examples

Mark a comment as spam

Path parameters

comment_id=653537639

string**string**

required**required**

Was this section helpful?

YesNo

post

## /admin/api/2026-01/comments/653537639/spam.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{}' \

-X POST "https://your-development-store.myshopify.com/admin/api/2026-01/comments/653537639/spam.json" \

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

"published_at": null,

"status": "spam",

"blog_id": 241253187,

"article_id": 134645308,

"author": "Soleone",

"body": "Hi author, I really _like_ what you're doing there.",

"email": "soleone@example.net",

"body_html": "<p>Hi author, I really <em>like</em> what you're doing there.</p>",

"id": 653537639,

"created_at": "2026-01-09T22:32:40-05:00",

"updated_at": "2026-01-09T22:34:30-05:00",

"ip": "127.0.0.1",

"user_agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1"

}

### examples

  * #### Mark a comment as spam

#####

        curl -d '{}' \
        -X POST "https://your-development-store.myshopify.com/admin/api/2026-01/comments/653537639/spam.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const comment = new admin.rest.resources.Comment({session: session});

        comment.id = 653537639;
        await comment.spam({});

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        comment = ShopifyAPI::Comment.new(session: test_session)
        comment.id = 653537639
        comment.spam(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        const comment = new shopify.rest.Comment({session: session});
        comment.id = 653537639;
        await comment.spam({});

#### response

        HTTP/1.1 200 OK{"published_at":null,"status":"spam","blog_id":241253187,"article_id":134645308,"author":"Soleone","body":"Hi author, I really _like_ what you're doing there.","email":"soleone@example.net","body_html":"<p>Hi author, I really <em>like</em> what you're doing there.</p>","id":653537639,"created_at":"2026-01-09T22:32:40-05:00","updated_at":"2026-01-09T22:34:30-05:00","ip":"127.0.0.1","user_agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1"}


* * *

##

[Anchor to GET request, Retrieves a list of comments](/docs/api/admin-rest/latest/resources/comment#get-comments?since-id=118373535)

get

Retrieves a list of comments

[comments](/docs/api/admin-graphql/latest/queries/comments?example=retrieves-a-list-of-comments)

Retrieves a list of comments. **Note:** This endpoint implements pagination by using links that are provided in the response header. To learn more, refer to [Make paginated requests to the REST Admin API](/api/usage/pagination-rest).

###

[Anchor to Parameters of Retrieves a list of comments](/docs/api/admin-rest/latest/resources/comment#get-comments?since-id=118373535-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

created_at_max

Show comments created before date (format: 2014-04-25T16:15:47-04:00).

* * *

created_at_min

Show comments created after date (format: 2014-04-25T16:15:47-04:00).

* * *

fields

Show only certain fields, specified by a comma-separated list of field names.

* * *

limit

≤ 250**≤ 250**

default 50**default 50**

The maximum number of results to retrieve.

* * *

published_at_max

Show comments published before date (format: 2014-04-25T16:15:47-04:00).

* * *

published_at_min

Show comments published after date (format: 2014-04-25T16:15:47-04:00).

* * *

published_status

default any**default any**

Filter results by their published status.

Show published_status properties

  * **published** : Show only published comments.

  * **unpublished** : Show only unpublished comments.

  * **any** : Show comments of any published status.


* * *

since_id

Restrict results to after the specified ID.

* * *

status

Filter results by their status.

Show status properties

  * **pending** : Show only pending comments.

  * **published** : Show only published comments.

  * **unapproved** : Show only unapproved comments.


* * *

updated_at_max

Show comments last updated before date (format: 2014-04-25T16:15:47-04:00).

* * *

updated_at_min

Show comments last updated after date (format: 2014-04-25T16:15:47-04:00).

* * *

Was this section helpful?

YesNo

###

[Anchor to get-comments?since-id=118373535-examples](/docs/api/admin-rest/latest/resources/comment#get-comments?since-id=118373535-examples)Examples

Retrieve all comments for this shop after the specified ID

Query parameters

since_id=118373535

Restrict results to after the specified ID.

Retrieve all the comments for a certain article of a blog

Query parameters

article_id=134645308

A unique numeric identifier for the article that the comment belongs to.

blog_id=241253187

A unique numeric identifier for the blog containing the article that the comment belongs to.

Retrieve all the comments for all the articles of a blog

Query parameters

blog_id=241253187

A unique numeric identifier for the blog containing the article that the comment belongs to.

Retrieve all the comments for this shop

Was this section helpful?

YesNo

get

## /admin/api/2026-01/comments.json?since_id=118373535

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/comments.json?since_id=118373535" \

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

HTTP/1.1 200 OK

{

"comments": [

{

"id": 653537639,

"body": "Hi author, I really _like_ what you're doing there.",

"body_html": "<p>Hi author, I really <em>like</em> what you're doing there.</p>",

"author": "Soleone",

"email": "soleone@example.net",

"status": "unapproved",

"article_id": 134645308,

"blog_id": 241253187,

"created_at": "2026-01-09T22:32:40-05:00",

"updated_at": "2026-01-09T22:32:40-05:00",

"ip": "127.0.0.1",

"user_agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",

"published_at": null

}

]

}

### examples

  * #### Retrieve all comments for this shop after the specified ID

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/comments.json?since_id=118373535" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Comment.all({
          session: session,
          since_id: "118373535",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Comment.all(
          session: test_session,
          since_id: "118373535",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Comment.all({
          session: session,
          since_id: "118373535",
        });

#### response

        HTTP/1.1 200 OK{"comments":[{"id":653537639,"body":"Hi author, I really _like_ what you're doing there.","body_html":"<p>Hi author, I really <em>like</em> what you're doing there.</p>","author":"Soleone","email":"soleone@example.net","status":"unapproved","article_id":134645308,"blog_id":241253187,"created_at":"2026-01-09T22:32:40-05:00","updated_at":"2026-01-09T22:32:40-05:00","ip":"127.0.0.1","user_agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1","published_at":null}]}

  * #### Retrieve all the comments for a certain article of a blog

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/comments.json?article_id=134645308&blog_id=241253187" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Comment.all({
          session: session,
          article_id: "134645308",
          blog_id: "241253187",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Comment.all(
          session: test_session,
          article_id: "134645308",
          blog_id: "241253187",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Comment.all({
          session: session,
          article_id: "134645308",
          blog_id: "241253187",
        });

#### response

        HTTP/1.1 200 OK{"comments":[{"id":653537639,"body":"Hi author, I really _like_ what you're doing there.","body_html":"<p>Hi author, I really <em>like</em> what you're doing there.</p>","author":"Soleone","email":"soleone@example.net","status":"unapproved","article_id":134645308,"blog_id":241253187,"created_at":"2026-01-09T22:32:40-05:00","updated_at":"2026-01-09T22:32:40-05:00","ip":"127.0.0.1","user_agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1","published_at":null},{"id":118373535,"body":"Hi author, I really _like_ what you're doing there.","body_html":"<p>Hi author, I really <em>like</em> what you're doing there.</p>","author":"Soleone","email":"soleone@example.net","status":"published","article_id":134645308,"blog_id":241253187,"created_at":"2026-01-09T22:32:40-05:00","updated_at":"2026-01-09T22:32:40-05:00","ip":"127.0.0.1","user_agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1","published_at":null}]}

  * #### Retrieve all the comments for all the articles of a blog

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/comments.json?blog_id=241253187" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Comment.all({
          session: session,
          blog_id: "241253187",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Comment.all(
          session: test_session,
          blog_id: "241253187",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Comment.all({
          session: session,
          blog_id: "241253187",
        });

#### response

        HTTP/1.1 200 OK{"comments":[{"id":653537639,"body":"Hi author, I really _like_ what you're doing there.","body_html":"<p>Hi author, I really <em>like</em> what you're doing there.</p>","author":"Soleone","email":"soleone@example.net","status":"unapproved","article_id":134645308,"blog_id":241253187,"created_at":"2026-01-09T22:32:40-05:00","updated_at":"2026-01-09T22:32:40-05:00","ip":"127.0.0.1","user_agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1","published_at":null},{"id":118373535,"body":"Hi author, I really _like_ what you're doing there.","body_html":"<p>Hi author, I really <em>like</em> what you're doing there.</p>","author":"Soleone","email":"soleone@example.net","status":"published","article_id":134645308,"blog_id":241253187,"created_at":"2026-01-09T22:32:40-05:00","updated_at":"2026-01-09T22:32:40-05:00","ip":"127.0.0.1","user_agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1","published_at":null}]}

  * #### Retrieve all the comments for this shop

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/comments.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Comment.all({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Comment.all(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Comment.all({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"comments":[{"id":653537639,"body":"Hi author, I really _like_ what you're doing there.","body_html":"<p>Hi author, I really <em>like</em> what you're doing there.</p>","author":"Soleone","email":"soleone@example.net","status":"unapproved","article_id":134645308,"blog_id":241253187,"created_at":"2026-01-09T22:32:40-05:00","updated_at":"2026-01-09T22:32:40-05:00","ip":"127.0.0.1","user_agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1","published_at":null},{"id":118373535,"body":"Hi author, I really _like_ what you're doing there.","body_html":"<p>Hi author, I really <em>like</em> what you're doing there.</p>","author":"Soleone","email":"soleone@example.net","status":"published","article_id":134645308,"blog_id":241253187,"created_at":"2026-01-09T22:32:40-05:00","updated_at":"2026-01-09T22:32:40-05:00","ip":"127.0.0.1","user_agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1","published_at":null}]}


* * *

##

[Anchor to GET request, Retrieves a single comment by its ID](/docs/api/admin-rest/latest/resources/comment#get-comments-comment-id)

get

Retrieves a single comment by its ID

[comment](/docs/api/admin-graphql/latest/queries/comment?example=retrieves-a-single-comment-by-its-id)

Retrieves a single comment by its ID

###

[Anchor to Parameters of Retrieves a single comment by its ID](/docs/api/admin-rest/latest/resources/comment#get-comments-comment-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

comment_id

string**string**

required**required**

* * *

fields

Show only certain fields, specified by a comma-separated list of field names.

* * *

Was this section helpful?

YesNo

###

[Anchor to get-comments-comment-id-examples](/docs/api/admin-rest/latest/resources/comment#get-comments-comment-id-examples)Examples

Retrieve a single comment

Path parameters

comment_id=118373535

string**string**

required**required**

Was this section helpful?

YesNo

get

## /admin/api/2026-01/comments/118373535.json

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/comments/118373535.json" \

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

"comment": {

"id": 118373535,

"body": "Hi author, I really _like_ what you're doing there.",

"body_html": "<p>Hi author, I really <em>like</em> what you're doing there.</p>",

"author": "Soleone",

"email": "soleone@example.net",

"status": "published",

"article_id": 134645308,

"blog_id": 241253187,

"created_at": "2026-01-09T22:32:40-05:00",

"updated_at": "2026-01-09T22:32:40-05:00",

"ip": "127.0.0.1",

"user_agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",

"published_at": null

}

}

### examples

  * #### Retrieve a single comment

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/comments/118373535.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Comment.find({
          session: session,
          id: 118373535,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Comment.find(
          session: test_session,
          id: 118373535,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Comment.find({
          session: session,
          id: 118373535,
        });

#### response

        HTTP/1.1 200 OK{"comment":{"id":118373535,"body":"Hi author, I really _like_ what you're doing there.","body_html":"<p>Hi author, I really <em>like</em> what you're doing there.</p>","author":"Soleone","email":"soleone@example.net","status":"published","article_id":134645308,"blog_id":241253187,"created_at":"2026-01-09T22:32:40-05:00","updated_at":"2026-01-09T22:32:40-05:00","ip":"127.0.0.1","user_agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1","published_at":null}}


* * *

##

[Anchor to GET request, Retrieves a count of comments](/docs/api/admin-rest/latest/resources/comment#get-comments-count?article-id=134645308&blog-id=241253187)

get

Retrieves a count of comments

[article](/docs/api/admin-graphql/latest/queries/article)

Retrieves a count of comments

###

[Anchor to Parameters of Retrieves a count of comments](/docs/api/admin-rest/latest/resources/comment#get-comments-count?article-id=134645308&blog-id=241253187-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

created_at_max

Count comments created before date (format: 2014-04-25T16:15:47-04:00).

* * *

created_at_min

Count comments created after date (format: 2014-04-25T16:15:47-04:00).

* * *

published_at_max

Count comments published before date (format: 2014-04-25T16:15:47-04:00).

* * *

published_at_min

Count comments published after date (format: 2014-04-25T16:15:47-04:00).

* * *

published_status

default any**default any**

Retrieve a count of comments with a given published status.

Show published_status properties

  * **published** : Count only published comments.

  * **unpublished** : Count only unpublished comments.

  * **any** : Count comments of any published status.


* * *

status

Retrieve a count of comments with a given status.

Show status properties

  * **pending** : Count pending comments.

  * **published** : Count published comments.

  * **unapproved** : Count unapproved comments.


* * *

updated_at_max

Count comments last updated before date (format: 2014-04-25T16:15:47-04:00).

* * *

updated_at_min

Count comments last updated after date (format: 2014-04-25T16:15:47-04:00).

* * *

Was this section helpful?

YesNo

###

[Anchor to get-comments-count?article-id=134645308&blog-id=241253187-examples](/docs/api/admin-rest/latest/resources/comment#get-comments-count?article-id=134645308&blog-id=241253187-examples)Examples

Count all comments for a certain article of a blog

Query parameters

article_id=134645308

A unique numeric identifier for the article that the comment belongs to.

blog_id=241253187

A unique numeric identifier for the blog containing the article that the comment belongs to.

Count all the comments for all the articles of a blog

Query parameters

blog_id=241253187

A unique numeric identifier for the blog containing the article that the comment belongs to.

Count all the comments for this shop

Was this section helpful?

YesNo

get

## /admin/api/2026-01/comments/count.json?article_id=134645308&blog_id=241253187

cURLRemixRubyNode.js

Copy

9

1

2

curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/comments/count.json?article_id=134645308&blog_id=241253187" \

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

  * #### Count all comments for a certain article of a blog

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/comments/count.json?article_id=134645308&blog_id=241253187" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Comment.count({
          session: session,
          article_id: "134645308",
          blog_id: "241253187",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Comment.count(
          session: test_session,
          article_id: "134645308",
          blog_id: "241253187",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Comment.count({
          session: session,
          article_id: "134645308",
          blog_id: "241253187",
        });

#### response

        HTTP/1.1 200 OK{"count":2}

  * #### Count all the comments for all the articles of a blog

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/comments/count.json?blog_id=241253187" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Comment.count({
          session: session,
          blog_id: "241253187",
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Comment.count(
          session: test_session,
          blog_id: "241253187",
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Comment.count({
          session: session,
          blog_id: "241253187",
        });

#### response

        HTTP/1.1 200 OK{"count":2}

  * #### Count all the comments for this shop

#####

        curl -X GET "https://your-development-store.myshopify.com/admin/api/2026-01/comments/count.json" \
        -H "X-Shopify-Access-Token: {access_token}"


#####

        await admin.rest.resources.Comment.count({
          session: session,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        ShopifyAPI::Comment.count(
          session: test_session,
        )

#####

        // Session is built by the OAuth process

        await shopify.rest.Comment.count({
          session: session,
        });

#### response

        HTTP/1.1 200 OK{"count":2}


* * *

##

[Anchor to PUT request, Updates a comment of an article](/docs/api/admin-rest/latest/resources/comment#put-comments-comment-id)

put

Updates a comment of an article

deprecated**deprecated**

Updates a comment of an article

###

[Anchor to Parameters of Updates a comment of an article](/docs/api/admin-rest/latest/resources/comment#put-comments-comment-id-parameters)Parameters

* * *

api_version

string**string**

required**required**

* * *

comment_id

string**string**

required**required**

* * *

Was this section helpful?

YesNo

###

[Anchor to put-comments-comment-id-examples](/docs/api/admin-rest/latest/resources/comment#put-comments-comment-id-examples)Examples

Update the body of an existing comment

Path parameters

comment_id=118373535

string**string**

required**required**

Request body

comment[](/apps/store/data-protection/protected-customer-data)

Comment resource**Comment resource**

Show comment properties

comment.id:118373535

read-only**read-only**

A unique numeric identifier for the comment.

comment.body:"You can even update through a web service."

The basic [Textile markup](https://en.wikipedia.org/wiki/Textile_\(markup_language\)) of a comment.

comment.author:"Your new name"[](/apps/store/data-protection/protected-customer-data)

The name of the author of the comment.

comment.email:"your@updated-email.com"[](/apps/store/data-protection/protected-customer-data)

The email address of the author of the comment.

comment.published_at:"2026-01-10T03:34:41.562Z"

The date and time ([ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format) when the comment was published.

Was this section helpful?

YesNo

put

## /admin/api/2026-01/comments/118373535.json

cURLRemixRubyNode.js

Copy

9

1

2

3

4

curl -d '{"comment":{"id":118373535,"body":"You can even update through a web service.","author":"Your new name","email":"your@updated-email.com","published_at":"2026-01-10T03:34:41.562Z"}}' \

-X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/comments/118373535.json" \

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

HTTP/1.1 200 OK

{

"comment": {

"author": "Your new name",

"body": "You can even update through a web service.",

"email": "your@updated-email.com",

"published_at": "2026-01-09T22:34:41-05:00",

"status": "published",

"blog_id": 241253187,

"article_id": 134645308,

"body_html": "<p>You can even update through a web service.</p>",

"id": 118373535,

"created_at": "2026-01-09T22:32:40-05:00",

"updated_at": "2026-01-09T22:34:42-05:00",

"ip": "127.0.0.1",

"user_agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1"

}

}

### examples

  * #### Update the body of an existing comment

#####

        curl -d '{"comment":{"id":118373535,"body":"You can even update through a web service.","author":"Your new name","email":"your@updated-email.com","published_at":"2026-01-10T03:34:41.562Z"}}' \
        -X PUT "https://your-development-store.myshopify.com/admin/api/2026-01/comments/118373535.json" \
        -H "X-Shopify-Access-Token: {access_token}" \
        -H "Content-Type: application/json"


#####

        const { admin, session } = await authenticate.admin(request);

        const comment = new admin.rest.resources.Comment({session: session});

        comment.id = 118373535;
        comment.body = "You can even update through a web service.";
        comment.author = "Your new name";
        comment.email = "your@updated-email.com";
        comment.published_at = "2026-01-10T03:34:41.562Z";
        await comment.save({
          update: true,
        });

#####

        # Session is activated via Authentication
        test_session = ShopifyAPI::Context.active_session

        comment = ShopifyAPI::Comment.new(session: test_session)
        comment.id = 118373535
        comment.body = "You can even update through a web service."
        comment.author = "Your new name"
        comment.email = "your@updated-email.com"
        comment.published_at = "2026-01-10T03:34:41.562Z"
        comment.save!

#####

        // Session is built by the OAuth process

        const comment = new shopify.rest.Comment({session: session});
        comment.id = 118373535;
        comment.body = "You can even update through a web service.";
        comment.author = "Your new name";
        comment.email = "your@updated-email.com";
        comment.published_at = "2026-01-10T03:34:41.562Z";
        await comment.save({
          update: true,
        });

#### response

        HTTP/1.1 200 OK{"comment":{"author":"Your new name","body":"You can even update through a web service.","email":"your@updated-email.com","published_at":"2026-01-09T22:34:41-05:00","status":"published","blog_id":241253187,"article_id":134645308,"body_html":"<p>You can even update through a web service.</p>","id":118373535,"created_at":"2026-01-09T22:32:40-05:00","updated_at":"2026-01-09T22:34:42-05:00","ip":"127.0.0.1","user_agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4; en-us) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1"}}