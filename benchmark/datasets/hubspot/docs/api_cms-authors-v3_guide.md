# CMS API | Blog Authors

*Source: https://developers.hubspot.com/docs/api-reference/cms-authors-v3/guide*

---

Authors

# CMS API | Blog Authors

The blog authors endpoints are used to create and manage hubspot blog authors

Scope requirements

Use the blog authors API to manage author information for your blog posts. Learn more about how to create and maintain your blog on the [HubSpot Knowledge Base.](https://knowledge.hubspot.com/web-content/topics#blog)

##

​

Changes in V3

The following properties are deprecated and will not be included in the response of any of the V3 endpoints:

  * `user_id`
  * `username`
  * `googlePlus`
  * `gravatarUrl`
  * `twitterUsername`
  * `hasSocialProfiles`


##

​

Search blog authors

To retrieve an account’s blog authors, make a `GET` request to `/cms/v3/blogs/authors`. You can filter and sort the authors returned in the response using the operators and properties described below. You can also use the standard filters using the _createdAt_ and _updatedAt_ dates.

###

​

Filtering

Provide any filters as query parameters in your request, by adding the **property name** , followed by **two underscore characters** , then include the associated **operator** as a suffix. For example, you can filter the results to only include authors where the `displayName` property contains the word _J__ohn_ using the parameter: `&displayName__icontains=john`. You can include any number of filters as query parameters in the request URL. All filters are ANDed together. ORing filters is not currently supported. The available filter types are listed below:

Operator| Description
---|---
`eq`| Equal to
`ne`| Not equal to
`contains`| Contains
`lt`| Less than
`lte`| Less than or equal to
`gt`| Greater than
`gte`| Greater than or equal to
`is_null`| Null
`not_null`| Not null
`like`| Is like
`not_like`| Not like
`icontains`| Contains (case sensitive)
`startswith`| Starts with
`in`| In

The table below lists the properties that can be filtered on, along with their supported filter types.

Operator| Description
---|---
`id`| `eq`, `in`, `not_in`
`fullName`| `eq`, `in`, `contains`
`email`| `eq`, `ne`, `not_null`
`slug`| `eq`
`createdAt`| `eq`, `gt`, `gte`, `lt`, `lte`
`updatedAt`| `eq`, `gt`, `gte`, `lt`, `lte`
`name`| `eq`, `in`, `contains`
`deletedAt`| `eq`, `gt`, `gte`, `lt`, `lte`
`createdById`| `eq`
`updatedById`| `eq`
`language`| `in`, `not_null`
`translatedFromId`| `null`, `not_null`

To filter blog authors based on a multi-language group, you can include one of the query parameters in the table below. For example, to get blog authors associated with the German variation of your blog, you’d include `language_in=de` as a query parameter.

Parameter| Description
---|---
`translatedFromId__is_null`| Primary blog author in a multi-language group.
`translatedFromId__not_null`| Variation blog author in a multi-language group.
`language__in`| Blog author with a specific language.

###

​

Sorting and paginating

You can provide sorting and pagination options as query parameters. Specify the **property name** as the value to the sort query parameter to return the blog authors in the natural order of that property. You can reverse the sorting order by including a dash character before the property name (e.g., `sort=-createdAt`). By combining query parameters for filtering, sorting, and paging, you can retrieve blog authors that match more advanced search criteria. For example, the request below fetches blog authors that don’t have a language assigned, ordered by the most recently updated. The limit and offset parameters below return the second page of results.


    curl
    https://api.hubapi.com/cms/v3/blogs/authors?sort=-updatedAt&&language__not_null&limit=10&offset=10 \
      --request POST \
      --header "Content-Type: application/json"


##

​

Create blog authors

To create a blog author, make a `POST` request to `/cms/v3/blogs/authors`, and include a JSON payload that represents the blog author model. The `fullName` field is required when creating a blog author. To set the URL of a blog author profile page, you must provide the `slug` field in your request. Review the required parameters and the structure of the blog author model in the [reference documentation](https://developers.hubspot.com/docs/api-reference/cms-authors-v3/guide#post-%2Fcms%2Fv3%2Fblogs%2Fauthors). You can also [create blog authors directly in your HubSpot account](https://knowledge.hubspot.com/blog/create-and-manage-your-blog-authors#create-a-new-blog-author).

##

​

Edit blog authors

To update a blog author, make a `PATCH` request to `/cms/v3/blogs/authors/{objectId}`, where `objectId` is the ID of the associated author. Include a JSON payload representing the blog author model in your request. Review the required parameters and the structure of the blog author model in the [reference documentation](https://developers.hubspot.com/docs/api-reference/cms-authors-v3/guide#patch-%2Fcms%2Fv3%2Fblogs%2Fauthors%2F%7Bobjectid%7D). You can also [edit a blog author’s profile directly in your HubSpot account](https://knowledge.hubspot.com/blog/create-and-manage-your-blog-authors#edit-a-blog-author-s-profile).

##

​

Multi-language management

To help you maintain blog authors across multiple languages, HubSpot’s CMS allows you to group together blog authors of language variants of the same content. A blog author with a language set may only be used on blog posts of the same language. Blog authors that do not have a language set are considered global and may be used on all blog posts. To learn more about working with multi-language blog authors, check out [this Knowledge Base article](https://knowledge.hubspot.com/blog/create-a-multi-language-blog#create-blog-authors-in-multiple-languages).

###

​

Create a new language variant

To create a new language variant for an existing blog author, make a `POST` request to `/multi-language/create-language-variant` and include a JSON payload containing the ID of the blog author to clone and the language identifier of the new variant.

###

​

Attach a blog author to an existing multi-language group

To add a blog author to an existing multi-language group, make a `POST` request to `/multi-language/attach-to-lang-group` and include a JSON payload containing the ID of the target blog author, the language identifier of the blog author being added, and the `primaryId` of the blog author designated as the primary author in the target multi-language group.

###

​

Detach a blog author from a multi-language group

To remove a blog author from a multi-language group, make a `POST` request to `/multi-language/detach-from-lang-group` endpoint, and include a JSON payload that contains the ID of the target blog author.

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)