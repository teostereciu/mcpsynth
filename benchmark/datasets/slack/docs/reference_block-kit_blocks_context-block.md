# Context block

*Source: https://docs.slack.dev/reference/block-kit/blocks/context-block*

---

## Fields​

Field| Type| Description| Required?| `type`| String| The type of block. For a context block, `type` is always `context`.| Required| `elements`| Object[]| An array of [image elements](/reference/block-kit/block-elements/image-element) and [text objects](/reference/block-kit/composition-objects/text-object). Maximum number of items is 10.| Required| `block_id`| String| A unique identifier for a block. If not specified, one will be generated. Maximum length for this field is 255 characters. `block_id` should be unique for each message and each iteration of a message. If a message is updated, use a new `block_id`.| Optional
---|---|---|---

## Examples​

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "context",
                "elements": [
                    {
                        "type": "image",
                        "image_url": "https://image.freepik.com/free-photo/red-drawing-pin_1156-445.jpg",
                        "alt_text": "images"
                    },
                    {
                        "type": "mrkdwn",
                        "text": "Location: **Dogpatch**"
                    }
                ]
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/#%7B%22blocks%22:%5B%7B%22type%22:%22context%22,%22elements%22:%5B%7B%22type%22:%22image%22,%22image_url%22:%22https://image.freepik.com/free-photo/red-drawing-pin_1156-445.jpg%22,%22alt_text%22:%22images%22%7D,%7B%22type%22:%22mrkdwn%22,%22text%22:%22Location:%20*Dogpatch*%22%7D%5D%7D%5D%7D)

block-kit/src/blocks/context.py


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/context.py#L4-L20
)

block-kit/src/blocks/context.js


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/context.js#L12-L32
)

block-kit/src/main/java/blocks/Context.java


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/Context.java#L13-L24
)