# Input block

*Source: https://docs.slack.dev/reference/block-kit/blocks/input-block*

---

## Fields​

Field| Type| Description| Required?| `type`| String| The type of block. For an input block, `type` is always `input`.| Required| `label`| Object| A label that appears above an input element in the form of a [text object](/reference/block-kit/composition-objects/text-object) that must have `type` of `plain_text`. Maximum length for the `text` in this field is 2000 characters.| Required| `element`| Object| A block element. See above for full list.| Required| `dispatch_action`| Boolean| A boolean that indicates whether or not the use of elements in this block should dispatch a [`block_actions`](/reference/interaction-payloads/block_actions-payload) payload. Defaults to `false`. This field is incompatible with the [`file_input`](/reference/block-kit/block-elements/file-input-element) block element. If `dispatch_action` is set to `true` and a `file_input` block element is provided, an unsupported type error will be raised.| Optional| `block_id`| String| A unique identifier for a block. If not specified, one will be generated. Maximum length for this field is 255 characters. `block_id` should be unique for each message or view and each iteration of a message or view. If a message or view is updated, use a new `block_id`.| Optional| `hint`| Object| An optional hint that appears below an input element in a lighter grey. It must be a [text object](/reference/block-kit/composition-objects/text-object) with a `type` of `plain_text`. Maximum length for the `text` in this field is 2000 characters.| Optional| `optional`| Boolean| A boolean that indicates whether the input element may be empty when a user submits the modal. Defaults to `false`.| Optional
---|---|---|---

## Usage info​

Read our guides to collecting input [in modals](/surfaces/modals#gathering_input) or [in Home tabs](/surfaces/app-home#gathering_input) to learn how input blocks pass information to your app.

## Examples​

An input block containing a [plain-text input element](/reference/block-kit/block-elements/plain-text-input-element):

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "input",
                "element": {
                    "type": "plain_text_input"
                },
                "label": {
                    "type": "plain_text",
                    "text": "Label",
                    "emoji": true
                }
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/#%7B%22blocks%22:%5B%7B%22type%22:%22input%22,%22element%22:%7B%22type%22:%22plain_text_input%22%7D,%22label%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Label%22,%22emoji%22:true%7D%7D%5D%7D)

block-kit/src/blocks/input.py


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/input.py#L6-L17
)

block-kit/src/blocks/input.js


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/input.js#L12-L28
)

block-kit/src/main/java/blocks/Input.java


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/Input.java#L16-L20
)