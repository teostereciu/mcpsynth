# Divider block

*Source: https://docs.slack.dev/reference/block-kit/blocks/divider-block*

---

## Fields​

Field| Type| Description| Required?| `type`| String| The type of block. For a divider block, `type` is always `divider`.| Required| `block_id`| String| A unique identifier for a block. If not specified, one will be generated. Maximum length for this field is 255 characters. `block_id` should be unique for each message and each iteration of a message. If a message is updated, use a new `block_id`.| Optional
---|---|---|---

## Usage Info​

A content divider, like an `<hr>`, to split up different blocks inside of a message. The divider block is nice and neat, requiring only a `type`.

## Examples​

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "divider"
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/#%7B%22blocks%22:%5B%7B%22type%22:%22divider%22,%22block_id%22:%22divider1%22%7D%5D%7D)

block-kit/src/blocks/divider.py


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/divider.py#L4-L12
)

block-kit/src/blocks/divider.js


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/divider.js#L12-L20
)

block-kit/src/main/java/blocks/Divider.java


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/Divider.java#L10-L18
)