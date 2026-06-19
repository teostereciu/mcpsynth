# featured_tags API methods

*Source: https://docs.joinmastodon.org/methods/featured_tags/*

---

# featured_tags API methods

Feature tags that you use frequently on your profile.

## View your featured tags


    GET /api/v1/featured_tags HTTP/1.1


List all hashtags featured on your profile.

**Returns:** Array of [FeaturedTag](/entities/FeaturedTag/)
**OAuth:** User token + `read:accounts`
**Version history:**
3.0.0 - added

#### Request

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

#### Response

##### 200: OK

The `id` property of the items in this response refers to the [FeaturedTag](/entities/FeaturedTag/) entity, and is not the `id` for a [Tag](/entities/Tag/) entity.


    [
      {
        "id": "627",
        "name": "nowplaying",
        "url": "https://mastodon.social/@trwnh/tagged/nowplaying",
        "statuses_count": 70,
        "last_status_at": "2022-08-29T12:03:35.061Z"
      }
    ]


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


* * *

## Feature a tag


    POST /api/v1/featured_tags HTTP/1.1


Promote a hashtag on your profile.

**Returns:** [FeaturedTag](/entities/FeaturedTag/)
**OAuth:** User token + `write:accounts`
**Version history:**
3.0.0 - added

#### Request

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

##### Form data parameters

name
    required String. The hashtag to be featured, without the hash sign.

#### Response

##### 200: OK

A FeaturedTag will be created with the specified `name`.


    {
      "id": "13174",
      "name": "circasurvive",
      "url": "https://mastodon.social/@trwnh/tagged/circasurvive",
      "statuses_count": 23,
      "last_status_at": "2021-10-22T14:47:35.357Z"
    }


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


##### 422: Unprocessable entity

If `name` is not a valid hashtag, e.g. contains illegal characters or only numbers


    {
      "error": "Validation failed: Tag is invalid"
    }


* * *

## Unfeature a tag


    DELETE /api/v1/featured_tags/:id HTTP/1.1


Stop promoting a hashtag on your profile.

**Returns:** Empty
**OAuth:** User token + `write:accounts`
**Version history:**
3.0.0 - added

#### Request

##### Path parameters

:id
    required String. The ID of the FeaturedTag in the database.

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

#### Response

##### 200: OK

The tag was unfeatured.


    {}


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


##### 404: Not found

FeaturedTag is not owned by you or does not exist


    {
      "error": "Record not found"
    }


* * *

## View suggested tags to feature


    GET /api/v1/featured_tags/suggestions HTTP/1.1


Shows up to 10 recently-used tags.

**Returns:** Array of [Tag](/entities/Tag/)
**OAuth:** User token + `read:accounts`
**Version history:**
3.0.0 - added

#### Request

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

#### Response

##### 200: OK

Truncated results to first and last tag.


    [
      {
        "id": "4325",
        "name": "nowplaying",
        "url": "https://mastodon.social/tags/nowplaying",
        "history": [
          {
            "day": "1574553600",
            "uses": "200",
            "accounts": "31"
          },
          {
            "day": "1574467200",
            "uses": "272",
            "accounts": "39"
          },
          {
            "day": "1574380800",
            "uses": "345",
            "accounts": "40"
          },
          {
            "day": "1574294400",
            "uses": "366",
            "accounts": "46"
          },
          {
            "day": "1574208000",
            "uses": "226",
            "accounts": "32"
          },
          {
            "day": "1574121600",
            "uses": "217",
            "accounts": "42"
          },
          {
            "day": "1574035200",
            "uses": "214",
            "accounts": "34"
          }
        ]
      },
      // ...
      {
        "id": "1684",
        "name": "mastothemes",
        "url": "https://mastodon.social/tags/mastothemes",
        "history": [
          {
            "day": "1574553600",
            "uses": "0",
            "accounts": "0"
          },
          {
            "day": "1574467200",
            "uses": "0",
            "accounts": "0"
          },
          {
            "day": "1574380800",
            "uses": "0",
            "accounts": "0"
          },
          {
            "day": "1574294400",
            "uses": "0",
            "accounts": "0"
          },
          {
            "day": "1574208000",
            "uses": "0",
            "accounts": "0"
          },
          {
            "day": "1574121600",
            "uses": "0",
            "accounts": "0"
          },
          {
            "day": "1574035200",
            "uses": "0",
            "accounts": "0"
          }
        ]
      }
    ]


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


* * *

## See also

[app/controllers/api/v1/featured_tags_controller.rb ](https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/featured_tags_controller.rb)[app/controllers/api/v1/featured_tags/suggestions_controller.rb](https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/featured_tags/suggestions_controller.rb)

Last updated May 1, 2026 · [Improve this page](https://github.com/mastodon/documentation/tree/main/content/en/methods/featured_tags.md)