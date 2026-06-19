# directory API methods

*Source: https://docs.joinmastodon.org/methods/directory/*

---

# directory API methods

A directory of profiles that your website is aware of.

## View profile directory


    GET /api/v1/directory HTTP/1.1


List accounts visible in the directory.

**Returns:** Array of [Account](/entities/Account/)
**OAuth:** Public
**Version history:**
3.0.0 - added

#### Request

##### Query parameters

offset
    Number. Skip the first n results.
limit
    Number. How many accounts to load. Defaults to 40 accounts. Max 80 accounts.
order
    String. Use `active` to sort by most recently posted statuses (default) or `new` to sort by most recently created profiles.
local
    Boolean. If true, returns only local accounts.

#### Response

##### 200: OK

Sample results with limit=2


    [
      {
        "id": "796927",
        "username": "eternalNo3",
        "acct": "eternalNo3@best-friends.chat",
        "display_name": "ESD＠┓（谷）┏",
        // ...
      },
      {
        "id": "787648",
        "username": "ariel",
        "acct": "ariel@best-friends.chat",
        "display_name": "あやっしー🧜🏻‍♀️",
        // ...
      }
    ]


* * *

## See also

[app/controllers/api/v1/directories_controller.rb](https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/directories_controller.rb)

Last updated May 1, 2026 · [Improve this page](https://github.com/mastodon/documentation/tree/main/content/en/methods/directory.md)