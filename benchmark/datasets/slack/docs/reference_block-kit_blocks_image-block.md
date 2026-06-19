# Image block

*Source: https://docs.slack.dev/reference/block-kit/blocks/image-block*

---

## Fields​

Field| Type| Description| Required?| `type`| String| The type of block. For an image block, `type` is always `image`.| Required| `alt_text`| String| A plain-text summary of the image. This should not contain any markup. Maximum length for this field is 2000 characters.| Required| `image_url`| String| The URL for a publicly hosted image. You must provide either an `image_url` or `slack_file`. Maximum length for this field is 3000 characters.| Optional| `slack_file`| Object| A [Slack image file object](/reference/block-kit/composition-objects/slack-file-object) that defines the source of the image.| Optional| `title`| Object| An optional title for the image in the form of a [text object](/reference/block-kit/composition-objects/text-object) that can only be of `type: plain_text`. Maximum length for the `text` in this field is 2000 characters.| Optional| `block_id`| String| A unique identifier for a block. If not specified, one will be generated. Maximum length for this field is 255 characters. `block_id` should be unique for each message and each iteration of a message. If a message is updated, use a new `block_id`.| Optional
---|---|---|---

## Usage info​

An image block, designed to make those cat photos really pop. Supported file types include `png`, `jpg`, `jpeg`, and `gif`.

## Examples​

The following three examples show different ways to get the following result:

**Example 1** : An image block using `image_url`:

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "image",
                "title": {
                    "type": "plain_text",
                    "text": "Please enjoy this photo of a kitten"
                },
                "block_id": "image4",
                "image_url": "http://placekitten.com/500/500",
                "alt_text": "An incredibly cute kitten."
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/#%7B%22blocks%22:%5B%7B%22type%22:%22image%22,%22title%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Please%20enjoy%20this%20photo%20of%20a%20kitten%22%7D,%22block_id%22:%22image4%22,%22image_url%22:%22https://pbs.twimg.com/profile_images/625633822235693056/lNGUneLX_400x400.jpg%22,%22alt_text%22:%22An%20incredibly%20cute%20kitten.%22%7D%5D%7D)

block-kit/src/blocks/image.py


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/image.py#L5-L18
)

block-kit/src/blocks/image.js


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/image.js#L12-L27
)

block-kit/src/main/java/blocks/Image.java


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/Image.java#L16-L22
)

* * *

**Example 2** : An image block using `slack_file` with a `url`:

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "image",
                "title": {
                    "type": "plain_text",
                    "text": "Please enjoy this photo of a kitten"
                },
                "block_id": "image4",
                "slack_file": {
                    "url": "https://files.slack.com/files-pri/T0123456-F0123456/xyz.png"
                },
                "alt_text": "An incredibly cute kitten."
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/#%7B%22blocks%22:%5B%7B%22type%22:%22image%22,%22title%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Please%20enjoy%20this%20photo%20of%20a%20kitten%22%7D,%22block_id%22:%22image4%22,%22slack_file%22:%7B%22url%22:%22https://files.slack.com/files-pri/T0123456-F0123456/xyz.png%22%7D,%22alt_text%22:%22An%20incredibly%20cute%20kitten.%22%7D%5D%7D)

block-kit/src/blocks/image.py


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/image.py#L21-L33
)

block-kit/src/blocks/image.js


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/image.js#L34-L51
)

block-kit/src/main/java/blocks/Image.java


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/Image.java#L27-L35
)

* * *

**Example 3** : An image block using `slack_file` with a `id`:

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "image",
                "title": {
                    "type": "plain_text",
                    "text": "Please enjoy this photo of a kitten"
                },
                "block_id": "image4",
                "slack_file": {
                    "id": "F0123456"
                },
                "alt_text": "An incredibly cute kitten."
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/#%7B%22blocks%22:%5B%7B%22type%22:%22image%22,%22title%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Please%20enjoy%20this%20photo%20of%20a%20kitten%22%7D,%22block_id%22:%22image4%22,%22slack_file%22:%7B%22id%22:%22F0123456%22%7D,%22alt_text%22:%22An%20incredibly%20cute%20kitten.%22%7D%5D%7D)

block-kit/src/blocks/image.py


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/image.py#L36-L46
)

block-kit/src/blocks/image.js


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/image.js#L58-L75
)

block-kit/src/main/java/blocks/Image.java


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/Image.java#L40-L46
)