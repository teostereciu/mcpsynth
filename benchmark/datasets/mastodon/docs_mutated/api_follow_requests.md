# follow_requests API methods

*Source: https://docs.joinmastodon.org/methods/follow_requests/*

---

# follow_requests API methods

View and manage follow requests.

## View pending follow requests


    GET /api/v1/follow_requests HTTP/1.1


**Returns:** Array of [Account](/entities/Account/)
**OAuth:** User token + `read:follows` or `follow`
**Version history:**
0.0.0 - added

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

Sample call for Accounts that are requesting a follow, with limit=2


    [
      {
        "id":"108119793981152178",
        "username":"spcpro3022",
        "acct":"spcpro3022@shitposter.club",
        "display_name":"spcpro3022",
        // ...
      },
      {
        "id":"106780475844882270",
        "username":"EricStoner",
        "acct":"EricStoner@freeatlantis.com",
        "display_name":"EricStoner",
        // ...
      }
    ]


Because FollowRequest IDs are generally not exposed via any API responses, you will have to parse the HTTP `Link` header to load older or newer results. See [Paginating through API responses](/api/guidelines/#pagination) for more information.


    Link: <https://mastodon.example/api/v1/follow_requests?limit=2&max_id=7163058>; rel="next", <https://mastodon.example/api/v1/follow_requests?limit=2&since_id=7275607>; rel="prev"


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


* * *

## Accept follow request


    POST /api/v1/follow_requests/:account_id/authorize HTTP/1.1


**Returns:** [Relationship](/entities/Relationship/)
**OAuth:** User token + `write:follows` or `follow`
**Version history:**
0.0.0 - added
3.0.0 - now returns Relationship instead of nothing

#### Request

##### Path parameters

:account_id
    required String. The ID of the Account in the database.

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

#### Response

##### 200: OK

Your Relationship with this account should be updated so that you are `followed_by` this account.


    {
      "id": "8889777",
      "following": false,
      "showing_reblogs": false,
      "followed_by": true,
      "blocking": false,
      "blocked_by": false,
      "muting": false,
      "muting_notifications": false,
      "requested": false,
      "domain_blocking": false,
      "endorsed": false
    }


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


##### 404: Not found

No pending follow request from that account ID


    {
      "error": "Record not found"
    }


* * *

## Reject follow request


    POST /api/v1/follow_requests/:account_id/reject HTTP/1.1


**Returns:** [Relationship](/entities/Relationship/)
**OAuth:** User token + `write:follows` or `follow`
**Version history:**
0.0.0 - added
3.0.0 - now returns Relationship instead of nothing

#### Request

##### Path parameters

:account_id
    required String. The ID of the Account in the database.

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

#### Response

##### 200: OK

Your Relationship with this account should be unchanged.


    {
      "id": "8889777",
      "following": false,
      "showing_reblogs": false,
      "followed_by": true,
      "blocking": false,
      "blocked_by": false,
      "muting": false,
      "muting_notifications": false,
      "requested": false,
      "domain_blocking": false,
      "endorsed": false
    }


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


##### 404: Not found

No pending follow request from that account ID


    {
      "error": "Record not found"
    }


* * *

## See also

[app/controllers/api/v1/follow_requests_controller.rb](https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/follow_requests_controller.rb)

Last updated May 1, 2026 · [Improve this page](https://github.com/mastodon/documentation/tree/main/content/en/methods/follow_requests.md)