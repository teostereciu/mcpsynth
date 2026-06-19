# blocks API methods

*Source: https://docs.joinmastodon.org/methods/blocks/*

---

# blocks API methods

View your blocks. See also accounts/:id/{block,unblock}

## View blocked users


    GET /api/v1/blocks HTTP/1.1


Returns your blocked accounts.

**Returns:** Array of [Account](/entities/Account/)
**OAuth:** User token + `read:blocks`
**Version history:**
0.0.0 - added
3.3.0 - both `min_id` and `max_id` can be used at the same time now

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
    Integer. Maximum number of results to return. Defaults to 40 accounts. Max 80 accounts.

#### Response

##### 200: OK

Sample call with limit=2.


    [
      {
        "id": "585315",
        "username": "admin",
        "acct": "admin@happylittle.cloudns.cc",
        "display_name": "☁️  ⛅ Happy Little Clouds ⛅ ☁️",
        // ...
      },
      {
        "id": "650568",
        "username": "Nikolai_Kingsley",
        "acct": "Nikolai_Kingsley@dobbs.town",
        "display_name": "Rev.Dr. Nikolai Kingsley",
        // ...
      }
    ]


Because Block IDs are generally not exposed via any API responses, you will have to parse the HTTP `Link` header to load older or newer results. See [Paginating through API responses](/api/guidelines/#pagination) for more information.


    Link: <https://mastodon.example/api/v1/blocks?limit=2&max_id=441449>; rel="next", <https://mastodon.example/api/v1/blocks?limit=2&since_id=444808>; rel="prev"


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


* * *

## See also

[POST /api/v1/accounts/:id/block ](/methods/accounts/#block)[POST /api/v1/accounts/:id/unblock ](/methods/accounts/#unblock)[app/controllers/api/v1/blocks_controller.rb](https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/blocks_controller.rb)

Last updated May 1, 2026 · [Improve this page](https://github.com/mastodon/documentation/tree/main/content/en/methods/blocks.md)