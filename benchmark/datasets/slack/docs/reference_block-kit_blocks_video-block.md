# Video block

*Source: https://docs.slack.dev/reference/block-kit/blocks/video-block*

---

## Fields​

Property| Type| Description| Required?| `type`| string| The type of block. For a video block, type will always be `video`.| Required| `alt_text`| string| A tooltip for the video. Required for accessibility| Required| `author_name`| string| Author name to be displayed. Must be less than 50 characters.| Optional| `block_id`| string| A unique identifier for a block. If not specified, one will be generated. Maximum length for this field is 255 characters. `block_id` should be unique for each message and each iteration of a message. If a message is updated, use a new `block_id`.| Optional| `description`| Object| Description for video in the form of a [text object](/reference/block-kit/composition-objects/text-object) that must have `type` of `plain_text`. `text` within must be less than 200 characters.| Preferred| `provider_icon_url`| string| Icon for the video provider, e.g. YouTube icon.| Optional| `provider_name`| string| The originating application or domain of the video, e.g. YouTube.| Optional| `title`| Object| Video title in the form of a [text object](/reference/block-kit/composition-objects/text-object) that must have `type` of `plain_text`. `text` within must be less than 200 characters.| Required| `title_url`| string| Hyperlink for the title text. Must correspond to the non-embeddable URL for the video. Must go to an HTTPS URL.| Preferred| `thumbnail_url`| string| The thumbnail image URL| Required| `video_url`| string| The URL to be embedded. Must match any existing [unfurl domains](/messaging/unfurling-links-in-messages#configuring_domains) within the app and point to a HTTPS URL.| Required
---|---|---|---

## Usage info​

A `video` block is designed to embed videos in all app surfaces (e.g. link unfurls, messages, modals, App Home) — anywhere you can put blocks! To use the video block within your app, you must have the [`links.embed:write`](/reference/scopes/links.embed.write) scope.

The metadata received in the block payload will be used to construct the description, provider, and title of the video in all clients. Developers have the flexibility to leave non-mandatory fields null and use other blocks to format this content.

### Requirements​

  * Video blocks can only be posted by apps; users are not allowed to post embedded videos directly from Block Kit Builder.
  * Your app must have the the [`links.embed:write`](/reference/scopes/links.embed.write) scope for both user and bot tokens.
  * `video_url` has to be included in the [unfurl domains](/messaging/unfurling-links-in-messages#configuring_domains) specified in your app.
  * `video_url` should be publicly accessible, unless the app relies on information received from the [Events API](/apis/events-api/) payloads to make a decision on whether the viewer(s) of the content should have access. If so, the service could create a unique URL accessible only via Slack.
  * `video_url` must be compatible with an embeddable iFrame.
  * `video_url` must return a 2xx code OR 3xx with less than 5 redirects and an eventual 2xx.
  * `video_url` must not point to any Slack-related domain.


### Constraints​

  * Embeddable video players only (audio-only permitted)
  * Navigation, scrolling and overlays are not allowed within the iFrame.
  * Interactivity (e.g. likes, comments, and reactions) are allowed within your player but shouldn't completely overlay or navigate away from the content being embedded. These interactions will be anonymous since no user data is transferred to the embedded view.


## Examples​

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "video",
                "title": {
                    "type": "plain_text",
                    "text": "Use the Events API to create a dynamic App Home",
                    "emoji": true
                },
                "title_url": "https://www.youtube.com/watch?v=8876OZV_Yy0",
                "description": {
                    "type": "plain_text",
                    "text": "Slack sure is nifty!",
                    "emoji": true
                },
                "video_url": "https://www.youtube.com/embed/8876OZV_Yy0?feature=oembed&autoplay=1",
                "alt_text": "Use the Events API to create a dynamic App Home",
                "thumbnail_url": "https://i.ytimg.com/vi/8876OZV_Yy0/hqdefault.jpg"
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/#%7B%22blocks%22:%5B%7B%22type%22:%22video%22,%22title%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Use%20the%20Events%20API%20to%20create%20a%20dynamic%20App%20Home%20.%22,%22emoji%22:true%7D,%22title_url%22:%22https://www.youtube.com/watch?v=8876OZV_Yy0%22,%22description%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Slack%20sure%20is%20nifty!.%22,%22emoji%22:true%7D,%22video_url%22:%22https://www.youtube.com/embed/8876OZV_Yy0?feature=oembed&autoplay=1%22,%22alt_text%22:%22Use%20the%20Events%20API%20to%20create%20a%20dynamic%20App%20Home%22,%22thumbnail_url%22:%22https://i.ytimg.com/vi/8876OZV_Yy0/hqdefault.jpg%22%7D%5D%7D)

block-kit/src/blocks/video.py


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/video.py#L5-L22
)

block-kit/src/blocks/video.js


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/video.js#L12-L35
)

block-kit/src/main/java/blocks/Video.java


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/Video.java#L15-L26
)