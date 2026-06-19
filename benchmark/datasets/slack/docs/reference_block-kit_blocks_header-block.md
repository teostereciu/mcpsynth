# Header block

*Source: https://docs.slack.dev/reference/block-kit/blocks/header-block*

---

## Fields​

Field| Type| Description| Required?| `type`| String| The type of block. For this block, type will always be `header`.| Required| `text`| Object| The text for the block, in the form of a [`plain_text` text object](/reference/block-kit/composition-objects/text-object). Maximum length for the `text` in this field is 150 characters.| Required| `block_id`| String| A unique identifier for a block. If not specified, one will be generated. Maximum length for this field is 255 characters. `block_id` should be unique for each message and each iteration of a message. If a message is updated, use a new `block_id`.| Optional
---|---|---|---

## Usage info​

A `header` is a plain-text block that displays in a larger, bold font. Use it to delineate between different groups of content in your app's surfaces.

## Examples​

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "A Heartfelt Header"
                }
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/#%7B%22blocks%22:%5B%7B%22type%22:%22header%22,%22text%22:%7B%22type%22:%22plain_text%22,%22text%22:%22A%20Heartfelt%20Header%22%7D%7D%5D%7D)

block-kit/src/blocks/header.py


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/header.py#L5-L13
)

block-kit/src/blocks/header.js


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/header.js#L12-L24
)

block-kit/src/main/java/blocks/Header.java


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/Header.java#L11-L19
)