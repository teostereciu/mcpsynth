# preferences API methods

*Source: https://docs.joinmastodon.org/methods/preferences/*

---

# preferences API methods

Preferred common behaviors to be shared across clients.

## View user preferences


    GET /api/v1/preferences HTTP/1.1


Preferences defined by the user in their account settings.

**Returns:** Preferences by key and value
**OAuth:** User token + `read:accounts`
**Version history:**
2.8.0 - added
4.5.0 (`mastodon` [API version](/entities/Instance/#api-versions) 7) - added `posting:default:quoted_policy`

#### Request

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

#### Response

##### 200: OK


    {
      "posting:default:post_visibility": "public",
      "posting:default:is_sensitive": false,
      "posting:default:lang": null,
      "posting:default:quote_policy": "followers",
      "reading:expand:media": "default",
      "reading:expand:spoilers": false
    }


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


* * *

## See also

[app/controllers/api/v1/preferences_controller.rb](https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/preferences_controller.rb)

Last updated May 1, 2026 · [Improve this page](https://github.com/mastodon/documentation/tree/main/content/en/methods/preferences.md)