# File block

*Source: https://docs.slack.dev/reference/block-kit/blocks/file-block*

---

## Fields​

Field| Type| Description| Required?| `type`| String| The type of block. For a file block, `type` is always `file`.| Required| `external_id`| String| The external unique ID for this file.| Required| `source`| String| At the moment, `source` will always be `remote` for a remote file.| Required| `block_id`| String| A unique identifier for a block. If not specified, one will be generated. Maximum length for this field is 255 characters. `block_id` should be unique for each message and each iteration of a message. If a message is updated, use a new `block_id`.| Optional
---|---|---|---

## Usage info​

You can't add this block to app surfaces directly, but it will show up when [retrieving messages](/messaging/retrieving-messages) that contain remote files.

If you want to add remote files to messages, [follow our guide](/messaging/working-with-files#remote).

## Examples​

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "file",
                "external_id": "ABCD1",
                "source": "remote"
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/T024BE7LD#%7B%22blocks%22:%5B%7B%22type%22:%22file%22,%22external_id%22:%22ABCD1%22,%22source%22:%22remote%22%7D%5D%7D)

block-kit/src/blocks/file.py


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/file.py#L4-L12
)

block-kit/src/blocks/file.js


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/file.js#L12-L22
)

block-kit/src/main/java/blocks/File.java


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/File.java#L10-L18
)