# CMS API | Blog Posts

*Source: https://developers.hubspot.com/docs/api/cms/blog-post*

---

Posts

# CMS API | Blog Posts

Use the blog posts API to create, manage, and publish blog posts on your website.

Scope requirements

You can use the blog post API to publish and manage blog posts. Learn more about how to create and maintain your blog on the [HubSpot Knowledge Base.](https://knowledge.hubspot.com/web-content/topics#blog)

##

​

Changes in V3

  * The following properties are deprecated and will not be included in the response of any of the V3 endpoints:
    * `campaign_name`
    * `is_draft`
    * `keywords`
  * The `topicIds` property has been renamed to `tagIds`.


##

​

Retrieve blog posts

You can retrieve blog posts either individually by ID or by retrieving all blog posts:

  * To retrieve all blog posts, make a `GET` request to `/cms/v3/blogs/posts`.
  * To retrieve an individual blog post, make a `GET` request to `/cms/v3/blogs/posts/{postId}`.


###

​

Retrieve all blog posts

When retrieving all blog posts, you can filter and sort the returned results using query parameters. For example, the following request would retrieve the first 10 blog posts created after January 1, 2024:


    curl https://api.hubapi.com/cms/v3/blogs/posts?createdAfter=2024-01-01T00:00:00Z&limit=10 \
      --request GET \
      --header "Authorization: Bearer YOUR_ACCESS_TOKEN"


The following query parameters are available:

Parameter| Type| Description
---|---|---
`after`| String| The paging cursor token of the last successfully read resource. Available from `paging.next.after` in paginated responses.
`archived`| Boolean| Whether to return only results that have been archived. Defaults to `false`.
`createdAfter`| String| Only return blog posts created after this date (ISO 8601 format).
`createdAt`| String| Only return blog posts created at exactly this date (ISO 8601 format).
`createdBefore`| String| Only return blog posts created before this date (ISO 8601 format).
`limit`| Integer| Maximum number of results per page. Default is `20`.
`property`| String| Specify specific properties to return from the posts.
`sort`| Array| Specify the order in which the blog posts are returned. Valid fields are `createdAt` (default), `name`, `updatedAt`, `createdBy`, `updatedBy`. Prefix with `-` to reverse the order (e.g., `-createdAt`).
`updatedAfter`| String| Only return blog posts last updated after this date (ISO 8601 format).
`updatedAt`| String| Only return blog posts last updated at exactly this date (ISO 8601 format).
`updatedBefore`| String| Only return blog posts last updated before this date (ISO 8601 format).

The response includes a `total` count and an array of blog post objects:


    {
      "total": 2,
      "results": [
        {
          "id": "184993428780",
          "slug": "example-blog-post",
          "contentGroupId": "184993428123",
          "campaign": "3b56cd5e-2c88-4b01-aed0-0d5a5e5e5e5e",
          "categoryId": 3,
          "state": "PUBLISHED",
          "name": "Example Blog Post",
          "mabExperimentId": "",
          "authorName": "John Doe",
          "abTestId": "",
          "createdById": "12345678",
          "updatedById": "12345678",
          "domain": "",
          "abStatus": "master",
          "folderId": "",
          "widgetContainers": {},
          "widgets": {},
          "language": "en",
          "translatedFromId": "",
          "translations": {},
          "dynamicPageHubDbTableId": "",
          "blogAuthorId": "4183274253",
          "tagIds": [12345678901],
          "htmlTitle": "Example Blog Post | My Company Blog",
          "enableGoogleAmpOutputOverride": false,
          "useFeaturedImage": true,
          "postBody": "<p>Welcome to my blog post! Neat, huh?</p>",
          "postSummary": "A summary of my blog post.",
          "rssBody": "",
          "rssSummary": "",
          "currentlyPublished": true,
          "archivedInDashboard": false,
          "createdAt": "2024-01-15T10:30:00.000Z",
          "updatedAt": "2024-01-15T14:45:00.000Z",
          "publishDate": "2024-01-15T12:00:00.000Z",
          "currentState": "PUBLISHED",
          "url": "https://www.example.com/blog/example-blog-post",
          "featuredImage": "https://www.example.com/hubfs/featured-image.jpg",
          "featuredImageAltText": "Featured image alt text",
          "metaDescription": "This is the meta description for the blog post."
        }
      ],
      "paging": {
        "next": {
          "after": "Mg%3D%3D",
          "link": "https://api.hubspot.com/cms/v3/blogs/posts?after=Mg%3D%3D"
        }
      }
    }


See all 53 lines

The `authorName` field returns the name of the user who most recently published the blog post, not the name of the blog author associated with the post. To get the blog author’s information, use the `blogAuthorId` field to look up the author via the [blog authors API](/docs/api-reference/legacy/cms/blogs/authors/guide).

###

​

Retrieve a single blog post

To retrieve details for a specific blog post, make a `GET` request to `/cms/v3/blogs/posts/{postId}`. For example, the request below would retrieve the details for the blog post with ID `184993428780`:


    curl https://api.hubapi.com/cms/v3/blogs/posts/184993428780 \
      --request GET \
      --header "Authorization: Bearer YOUR_ACCESS_TOKEN"


You can optionally include the `property` query parameter to return only specific properties.

###

​

Filtering

You can filter blog posts using query parameters. Provide the property name, followed by two underscore characters, then include the associated operator as a suffix. For example, you can filter the results to only include blog posts where the `name` property contains the word `marketing` using the parameter: `&name__contains=marketing`.

Filter| Operator
---|---
Equals| `eq` (or none)
Not equal| `ne`
Contains| `contains`
Contains (case insensitive)| `icontains`
Less than| `lt`
Less than or equal| `lte`
Greater than| `gt`
Greater than or equal| `gte`
Null| `is_null`
Not null| `not_null`
Like| `like`
Not like| `not_like`
Starts with| `startswith`
In| `in`
Not in| `nin`

The table below lists the properties that can be filtered on, along with their supported filter types.

Property| Supported filters
---|---
`id`| `eq`, `in`
`slug`| `eq`, `in`, `nin`, `icontains`
`campaign`| `eq`, `in`
`state`| `eq`, `ne`, `in`, `nin`, `contains`
`publishDate`| `eq`, `gt`, `gte` , `lt` ,`lte`
`createdAt`| `eq`, `gt`, `gte` , `lt` ,`lte`
`updatedAt`| `eq`, `gt`, `gte` , `lt` ,`lte`
`name`| `eq`, `in`, `icontains`
`archivedAt`| `eq`, `gt`, `gte`, `lt` ,`lte`
`createdById`| `eq`
`updatedById`| `eq`
`blogAuthorId`| `eq`, `in`
`translatedFromId`| `is_null`, `not_null`
`contentGroupId`| `eq`, `in`
`tagId`| `eq`, `in`

####

​

Filtering by publish state

Publish State| Query parameters
---|---
Draft| `state=DRAFT`
Scheduled| `state=SCHEDULED`
Published| `state=PUBLISHED`

The `currentState` field on the blog post object is a generated field which also reflects the blog’s publish state, but you cannot use it as a property to filter against in your requests.

####

​

Filtering for multi-language posts

Description| Query parameters
---|---
Primary blog post in a multi-language group| `translatedFromId__is_null`
Variation blog post in a multi-language group| `translatedFromId__not_null`
Blog post with specific language| `contentGroupId__eq`

###

​

Sorting and paginating

You can provide sorting and pagination options as query parameters. Specify the property name as the value to the `sort` query parameter to return the blog posts in the natural order of that property. You can reverse the sorting order by including a dash character before the property name (e.g., `sort=-createdAt`). By combining query parameters for filtering, sorting, and pagination, you can retrieve blog posts that match more advanced search criteria. For example, the request below fetches blog posts that have a language assigned, ordered by the most recently updated, and returns the second page of results:


    curl 'https://api.hubapi.com/cms/v3/blogs/posts?sort=-updatedAt&language__not_null&limit=10&after=MTA%3D' \
      --request GET \
      --header "Authorization: Bearer YOUR_ACCESS_TOKEN"


##

​

Create a blog post

To create a new blog post, make a `POST` request to `/cms/v3/blogs/posts`. For example, the request below would create a new draft blog post:


    curl https://api.hubapi.com/cms/v3/blogs/posts \
      --request POST \
      --header "Authorization: Bearer YOUR_ACCESS_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "name": "Example blog post",
        "contentGroupId": "184993428780",
        "slug": "slug-at-the-end-of-the-url",
        "blogAuthorId": "4183274253",
        "metaDescription": "My meta description.",
        "useFeaturedImage": false,
        "postBody": "<p>Welcome to my blog post! Neat, huh?</p>"
      }'


The following request body parameters are available:

Parameter| Type| Description
---|---|---
`name` | String| The title of the blog post.
`contentGroupId` | String| The ID of the parent blog to publish the post to. You can retrieve the ID using the [blog settings API](guides/cms-api/blog-settings).
`slug`| String| The URL slug of the blog post. HubSpot will automatically generate the full URL using this value, along with the parent blog domain and slug. If no value is provided, the `name` value will be used as a temporary slug (hyphenated). You will need to set a specific slug before the post can be published.
`blogAuthorId`| String| The ID of the blog author. You can retrieve this value using the [blog authors API](/docs/api-reference/legacy/cms/blogs/authors/guide).
`metaDescription`| String| The post’s meta description.
`useFeaturedImage`| Boolean| Whether to include a featured image for the blog post. By default, this field is set to `true`. To include a featured image, include a value for the `featuredImage` parameter.
`featuredImage`| String| The URL of the featured image.
`featuredImageAltText`| String| Alt text for the featured image.
`postBody`| String| The HTML content of the blog post.
`postSummary`| String| The summary of the blog post that will appear on the main listing page.
`htmlTitle`| String| The HTML title of the post.
`tagIds`| Array| An array of tag IDs to associate with the post.
`language`| String| The ISO 639 language code of the post (e.g., `en`, `de`, `fr`).
`publishDate`| String| The date (ISO 8601 format) the blog post is to be published at.

By default, the post will be created as an unpublished draft. If needed, a blog post can be published at the time of creation as long as the properties necessary for publishing are set.

Editing blog post content directly in HubSpot using the content editor is the simplest way to modify content. While you can use the API to create and update blog post, it’s not recommended over using the editor, especially for blogs that rely on more complex modules.

##

​

Update a blog post

To update an existing blog post, make a `PATCH` request to `/cms/v3/blogs/posts/{postId}`. For example, the request below would update the title and URL slug of a blog post:


    curl https://api.hubapi.com/cms/v3/blogs/posts/184993428780 \
      --request PATCH \
      --header "Authorization: Bearer YOUR_ACCESS_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "name": "Updated blog post title",
        "slug": "my-updated-post"
      }'


This request updates both the draft and live versions of the post. To update only the draft version without affecting the live content, make a `PATCH` request to `/cms/v3/blogs/posts/{postId}/draft` instead. The following request body parameters are available:

Parameter| Type| Description
---|---|---
`name`| String| The title of the blog post.
`slug`| String| The URL slug of the blog post.
`blogAuthorId`| String| The ID of the blog author.
`metaDescription`| String| The post’s meta description.
`useFeaturedImage`| Boolean| Whether to include a featured image for the blog post.
`featuredImage`| String| The URL of the featured image.
`featuredImageAltText`| String| Alt text for the featured image.
`postBody`| String| The HTML content of the blog post.
`postSummary`| String| The summary of the blog post.
`htmlTitle`| String| The HTML title of the post.
`tagIds`| Array| An array of tag IDs to associate with the post.
`language`| String| The ISO 639 language code of the post.
`publishDate`| String| The date (ISO 8601 format) the blog post is to be published at.
`archivedInDashboard`| Boolean| Set to `true` to archive the post in the dashboard (the post may still be live).

Properties you provide in the request payload will override existing draft properties without any complex merging logic. As a result, if you’re updating nested properties, you should provide the full definition of the object. Partial updates are not supported for nested objects.

##

​

Delete a blog post

To delete an existing blog post, make a `DELETE` request to `/cms/v3/blogs/posts/{postId}`. For example, the request below would delete the blog post with ID `184993428780`:


    curl https://api.hubapi.com/cms/v3/blogs/posts/184993428780 \
      --request DELETE \
      --header "Authorization: Bearer YOUR_ACCESS_TOKEN"


A successful deletion returns a `204 No Content` response with no body.

This is not the same as the in-app archive function. To perform a dashboard archive, send a normal update with the `archivedInDashboard` field set to `true`.

##

​

Draft and live versions

Blog posts in HubSpot have both draft and live versions.

  * **Draft blog posts** appear in HubSpot’s editor, but are not live on the website. They can be reviewed and edited by users in HubSpot or via the API, and can be published when needed. After a blog post is published, the draft version can be updated as needed, then later published to update the live content.
  * **Live blog posts** are blog posts that appear on the website. The draft version can be updated without affecting the live blog post content. Published posts can be unpublished to remove them from the website and return them to a draft version.


###

​

Retrieve the draft version

To retrieve the draft version of a blog post, make a `GET` request to `/cms/v3/blogs/posts/{postId}/draft`.


    curl https://api.hubapi.com/cms/v3/blogs/posts/184993428780/draft \
      --request GET \
      --header "Authorization: Bearer YOUR_ACCESS_TOKEN"


###

​

Update the draft version

To update only the draft version of a blog post (without affecting the live content), make a `PATCH` request to `/cms/v3/blogs/posts/{postId}/draft`.


    curl https://api.hubapi.com/cms/v3/blogs/posts/184993428780/draft \
      --request PATCH \
      --header "Authorization: Bearer YOUR_ACCESS_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "name": "Updated draft title",
        "postBody": "<p>Updated draft content.</p>"
      }'


Because this request only updates the draft, you would need to make a second request to publish the changes to the website.

###

​

Reset a draft

To reset the draft version of a blog post back to its current live version, make a `POST` request to `/cms/v3/blogs/posts/{postId}/draft/reset`. This endpoint does not require a request body.


    curl https://api.hubapi.com/cms/v3/blogs/posts/184993428780/draft/reset \
      --request POST \
      --header "Authorization: Bearer YOUR_ACCESS_TOKEN"


##

​

Publishing blog posts

Depending on the state of the blog post, there are different endpoints you can use to publish it.

###

​

Publish a draft

If the blog post is currently a draft (not yet published), make a `PATCH` request to the `/cms/v3/blogs/posts/{postId}` endpoint. In the request body, include a JSON payload that sets the `state` to `PUBLISHED`:


    curl https://api.hubapi.com/cms/v3/blogs/posts/184993428780 \
      --request PATCH \
      --header "Authorization: Bearer YOUR_ACCESS_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "state": "PUBLISHED"
      }'


The post must have the following properties set in order to be published:

Property| Type| Description
---|---|---
`name` | String| The title of the blog post.
`contentGroupId` | String| The ID of the parent blog to publish the post to. You can retrieve the ID using the [blogs API](guides/cms-api/blog-settings).
`slug` | String| The URL slug of the blog post. If no slug was specified at the time of creation, HubSpot will have assigned a temporary slug to the post. This temporary slug must be updated to a specific value in order for the post to be published.
`blogAuthorId` | String| The ID of the blog author. You can retrieve this value using the [blog authors API](/docs/api-reference/legacy/cms/blogs/authors/guide).
`metaDescription` | String| The post’s meta description.
`featuredImage`| String| An image to use as the post’s featured image. Alternatively, you can opt to not include a featured image by omitting this field and instead setting `useFeaturedImage` to `false`.
`state` | String| The publish state of the post. Must be set to `PUBLISHED`.

###

​

Push draft changes live

If the blog post is currently published, you can publish any content that’s currently drafted by making a `POST` request to `/cms/v3/blogs/posts/{postId}/draft/push-live`. This endpoint does not require a request body.


    curl https://api.hubapi.com/cms/v3/blogs/posts/184993428780/draft/push-live \
      --request POST \
      --header "Authorization: Bearer YOUR_ACCESS_TOKEN"


###

​

Schedule a draft to be published

As an alternative to immediate publishing, you can schedule the draft version of your blog post to be published later by making a `POST` request to `/cms/v3/blogs/posts/schedule`. In the request body, include a JSON payload that contains the `id` of the target blog post and a `publishDate` (ISO 8601 format).


    curl https://api.hubapi.com/cms/v3/blogs/posts/schedule \
      --request POST \
      --header "Authorization: Bearer YOUR_ACCESS_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "id": "184993428780",
        "publishDate": "2024-06-01T12:00:00Z"
      }'


##

​

Clone a blog post

To create a copy of an existing blog post, make a `POST` request to `/cms/v3/blogs/posts/clone`.


    curl https://api.hubapi.com/cms/v3/blogs/posts/clone \
      --request POST \
      --header "Authorization: Bearer YOUR_ACCESS_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "id": "184993428780",
        "cloneName": "Copy of Example Blog Post"
      }'


Parameter| Type| Description
---|---|---
`id` | String| The ID of the blog post to clone.
`cloneName`| String| The name for the cloned blog post.

##

​

Revisions

You can access previous versions of a blog post and restore them if needed.

###

​

Get all revisions

To retrieve all previous versions of a blog post, make a `GET` request to `/cms/v3/blogs/posts/{postId}/revisions`.


    curl https://api.hubapi.com/cms/v3/blogs/posts/184993428780/revisions \
      --request GET \
      --header "Authorization: Bearer YOUR_ACCESS_TOKEN"


###

​

Get a specific revision

To retrieve a specific previous version, make a `GET` request to `/cms/v3/blogs/posts/{postId}/revisions/{revisionId}`.

###

​

Restore a revision

To restore a blog post to a previous version, make a `POST` request to `/cms/v3/blogs/posts/{postId}/revisions/{revisionId}/restore`. This will update both the draft and live versions. To restore a previous version to the draft only (without affecting the live content), make a `POST` request to `/cms/v3/blogs/posts/{postId}/revisions/{revisionId}/restore-to-draft`.

##

​

Multi-language management

To help you maintain blog posts across multiple languages, HubSpot’s CMS allows you to group together language variants of the same content. You can learn more about working with multi-language blog posts in [on HubSpot’s Knowledge Base](https://knowledge.hubspot.com/blog/create-a-multi-language-blog#create-a-blog-post-in-multiple-languages).

###

​

Create a new language variant

You can create a new language variant for an existing blog post by making a `POST` request to the `/cms/v3/blogs/posts/multi-language/create-language-variation` endpoint.


    curl https://api.hubapi.com/cms/v3/blogs/posts/multi-language/create-language-variation \
      --request POST \
      --header "Authorization: Bearer YOUR_ACCESS_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "id": "184993428780",
        "language": "de"
      }'


Parameter| Type| Description
---|---|---
`id` | String| The ID of the blog post to clone.
`language` | String| The language code of the new variant (e.g., `de`, `fr`, `es`).

###

​

Attach a blog post to an existing multi-language group

You can add a blog post to an existing multi-language group by making a `POST` request to the `/cms/v3/blogs/posts/multi-language/attach-to-lang-group` endpoint.


    curl https://api.hubapi.com/cms/v3/blogs/posts/multi-language/attach-to-lang-group \
      --request POST \
      --header "Authorization: Bearer YOUR_ACCESS_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "id": "184993428781",
        "language": "de",
        "primaryId": "184993428780"
      }'


Parameter| Type| Description
---|---|---
`id` | String| The ID of the target blog post to attach.
`language` | String| The language identifier of the blog post being added.
`primaryId` | String| The ID of the blog post designated as the primary blog post in the target multi-language group.

###

​

Detach a blog post from a multi-language group

To detach a blog post from a multi-language group, make a `POST` request to the `/cms/v3/blogs/posts/multi-language/detach-from-lang-group` endpoint.


    curl https://api.hubapi.com/cms/v3/blogs/posts/multi-language/detach-from-lang-group \
      --request POST \
      --header "Authorization: Bearer YOUR_ACCESS_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "id": "184993428781"
      }'


###

​

Set a new primary language

To change the primary language of a multi-language group, make a `PUT` request to `/cms/v3/blogs/posts/multi-language/set-new-lang-primary`:


    curl https://api.hubapi.com/cms/v3/blogs/posts/multi-language/set-new-lang-primary \
      --request PUT \
      --header "Authorization: Bearer YOUR_ACCESS_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "id": "184993428781"
      }'


###

​

Update languages in a multi-language group

To explicitly set new languages for each post in a multi-language group, make a `POST` request to `/cms/v3/blogs/posts/multi-language/update-languages`:


    curl https://api.hubapi.com/cms/v3/blogs/posts/multi-language/update-languages \
      --request POST \
      --header "Authorization: Bearer YOUR_ACCESS_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "primaryId": "184993428780",
        "languages": {
          "184993428780": "en",
          "184993428781": "de",
          "184993428782": "fr"
        }
      }'


Parameter| Type| Description
---|---|---
`primaryId` | String| The ID of the primary blog post in the multi-language group.
`languages` | Object| A map of blog post IDs to their associated language codes.

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)