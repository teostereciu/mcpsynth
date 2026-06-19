# custom_emojis API methods

*Source: https://docs.joinmastodon.org/methods/custom_emojis/*

---

# custom_emojis API methods

Each site can define and upload its own custom emoji to be attached to profiles or statuses.

## View all custom emoji


    GET /api/v1/custom_emojis HTTP/1.1


Returns custom emojis that are available on the server.

**Returns:** Array of [CustomEmoji](/entities/CustomEmoji/)
**OAuth:** Public
**Version history:**
2.0.0 - added
3.0.0 - optional `category` added to response

#### Response

##### 200: OK

Sample response from mastodon.social


    [
      {
        "shortcode": "aaaa",
        "url": "https://files.mastodon.social/custom_emojis/images/000/007/118/original/aaaa.png",
        "static_url": "https://files.mastodon.social/custom_emojis/images/000/007/118/static/aaaa.png",
        "visible_in_picker": true
      },
      {
        "shortcode": "AAAAAA",
        "url": "https://files.mastodon.social/custom_emojis/images/000/071/387/original/AAAAAA.png",
        "static_url": "https://files.mastodon.social/custom_emojis/images/000/071/387/static/AAAAAA.png",
        "visible_in_picker": true
      },

      // [...]

      {
        "shortcode": "blobaww",
        "url": "https://files.mastodon.social/custom_emojis/images/000/011/739/original/blobaww.png",
        "static_url": "https://files.mastodon.social/custom_emojis/images/000/011/739/static/blobaww.png",
        "visible_in_picker": true,
        "category": "Blobs"
      },

      // [...]

      {
        "shortcode": "yikes",
        "url": "https://files.mastodon.social/custom_emojis/images/000/031/275/original/yikes.png",
        "static_url": "https://files.mastodon.social/custom_emojis/images/000/031/275/static/yikes.png",
        "visible_in_picker": true
      },
      {
        "shortcode": "ziltoid",
        "url": "https://files.mastodon.social/custom_emojis/images/000/017/094/original/05252745eb087806.png",
        "static_url": "https://files.mastodon.social/custom_emojis/images/000/017/094/static/05252745eb087806.png",
        "visible_in_picker": true
      }
    ]


* * *

## See also

[app/controllers/api/v1/custom_emojis_controller.rb](https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/custom_emojis_controller.rb)

Last updated May 1, 2026 · [Improve this page](https://github.com/mastodon/documentation/tree/main/content/en/methods/custom_emojis.md)