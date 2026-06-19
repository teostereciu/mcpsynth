# mutes API methods

*Source: https://docs.joinmastodon.org/methods/mutes/*

---

# mutes API methods

View your mutes. See also accounts/:id/{mute,unmute}

## View muted accounts


    GET /api/v1/mutes HTTP/1.1


Accounts the user has muted.

**Returns:** Array of [MutedAccount](/entities/Account/#MutedAccount)
**OAuth:** User token + `read:mutes` or `follow`
**Version history:**
0.0.0 - added
3.3.0 - added `mute_expires_at`

#### Request

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

##### Query parameters

max_id
    **Internal parameter.** Use HTTP `Link` header for pagination.
since_id
    **Internal parameter.** Use HTTP `Link` header for pagination.
limit
    Integer. Maximum number of results to return. Defaults to 40 accounts. Max 80 accounts.

#### Response

##### 200: OK

Sample response with limit=2.


    [
      {
        "id": "963076",
        "username": "Simia91",
        "acct": "Simia91",
        "display_name": "",
        // ...
      },
      {
        "id": "1001524",
        "username": "hakogamae",
        "acct": "hakogamae",
        "display_name": "Hakogamae 🔞",
        // ...
      }
    ]


Because Mute IDs are generally not exposed via any API responses, you will have to parse the HTTP `Link` header to load older or newer results. See [Paginating through API responses](/api/guidelines/#pagination) for more information.


    Link: <https://mastodon.example/api/v1/mutes?limit=2&max_id=317646>; rel="next", <https://mastodon.example/api/v1/mutes?limit=2&since_id=317647>; rel="prev"


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


* * *

## See also

[POST /api/v1/accounts/:id/mute ](/methods/accounts/#mute)[POST /api/v1/accounts/:id/unmute ](/methods/accounts/#unmute)[app/controllers/api/v1/mutes_controller.rb](https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/mutes_controller.rb)

Last updated May 1, 2026 · [Improve this page](https://github.com/mastodon/documentation/tree/main/content/en/methods/mutes.md)