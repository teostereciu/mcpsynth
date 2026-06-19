# followed_tags API methods

*Source: https://docs.joinmastodon.org/methods/followed_tags/*

---

# followed_tags API methods

View your followed hashtags.

## View all followed tags


    GET /api/v1/followed_tags HTTP/1.1


List your followed hashtags.

**Returns:** Array of [Tag](/entities/Tag/)
**OAuth:** User token + `read:follows`
**Version history:**
4.0.0 - added
4.1.0 - add pagination headers

#### Request

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

##### Query parameters

max_id
    **Internal parameter.** Use HTTP `Link` header for pagination.
since_id
    **Internal parameter.** Use HTTP `Link` header for pagination.
min_id
    **Internal parameter.** Use HTTP `Link` header for pagination.
limit
    Integer. Maximum number of results to return. Defaults to 100 tags. Max 200 tags.

#### Response

##### 200: OK

List of followed hashtags


    [
      {
        "id": "802",
        "name": "Caturday",
        "url": "http://mastodon.example/tags/caturday",
        "history": [
          {
            "day": "1668556800",
            "accounts": "0",
            "uses": "0"
          },
          {
            "day": "1668470400",
            "accounts": "0",
            "uses": "0"
          },
          {
            "day": "1668384000",
            "accounts": "0",
            "uses": "0"
          },
          {
            "day": "1668297600",
            "accounts": "1",
            "uses": "1"
          },
          {
            "day": "1668211200",
            "accounts": "0",
            "uses": "0"
          },
          {
            "day": "1668124800",
            "accounts": "0",
            "uses": "0"
          },
          {
            "day": "1668038400",
            "accounts": "0",
            "uses": "0"
          }
        ],
        "following": true
      },
      // ...
    ]


To paginate through the records in the followed tags collection, you must use the HTTP `Link` header to load older or newer results. The `id` property in the results refers to the [Tag](/entities/Tag/), not the record representing the following relationship to a Tag. See [Paginating through API responses](/api/guidelines/#pagination) for more information.


    Link: <http://mastodon.example/api/v1/followed_tags?limit=1&max_id=2>; rel="next", <http://mastodon.example/api/v1/followed_tags?limit=1&since_id=2>; rel="prev"


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


* * *

## See also

[POST /api/v1/tags/:id/follow ](/methods/tags/#follow)[POST /api/v1/tags/:id/unfollow ](/methods/tags/#unfollow)[app/controllers/api/v1/followed_tags_controller.rb](https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/followed_tags_controller.rb)

Last updated May 1, 2026 · [Improve this page](https://github.com/mastodon/documentation/tree/main/content/en/methods/followed_tags.md)