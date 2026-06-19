# Section block

*Source: https://docs.slack.dev/reference/block-kit/blocks/section-block*

---

## Fields​

Field| Type| Description| Required?| `type`| String| The type of block. For a section block, type will always be `section`.| Required| `text`| Object| The text for the block, in the form of a [text object](/reference/block-kit/composition-objects/text-object). Minimum length for the `text` in this field is 1 and maximum length is 3000 characters. This field is not _required_ if a valid array of `fields` objects is provided instead.| **Preferred**| `block_id`| String| A unique identifier for a block. If not specified, one will be generated. You can use this `block_id` when you receive an interaction payload to [identify the source of the action](/interactivity/handling-user-interaction#payloads). Maximum length for this field is 255 characters. `block_id` should be unique for each message and each iteration of a message. If a message is updated, use a new `block_id`.| Optional| `fields`| Object[]| Required if no `text` is provided. An array of [text objects](/reference/block-kit/composition-objects/text-object). Any text objects included with `fields` will be rendered in a compact format that allows for 2 columns of side-by-side text. Maximum number of items is 10. Maximum length for the `text` in each item is 2000 characters. [Click here for an example](https://api.slack.com/tools/block-kit-builder?blocks=%5B%0A%09%7B%0A%09%09%22type%22%3A%20%22section%22%2C%0A%09%09%22text%22%3A%20%7B%0A%09%09%09%22text%22%3A%20%22A%20message%20*with%20some%20bold%20text*%20and%20_some%20italicized%20text_.%22%2C%0A%09%09%09%22type%22%3A%20%22mrkdwn%22%0A%09%09%7D%2C%0A%09%09%22fields%22%3A%20%5B%0A%09%09%09%7B%0A%09%09%09%09%22type%22%3A%20%22mrkdwn%22%2C%0A%09%09%09%09%22text%22%3A%20%22*Priority*%22%0A%09%09%09%7D%2C%0A%09%09%09%7B%0A%09%09%09%09%22type%22%3A%20%22mrkdwn%22%2C%0A%09%09%09%09%22text%22%3A%20%22*Type*%22%0A%09%09%09%7D%2C%0A%09%09%09%7B%0A%09%09%09%09%22type%22%3A%20%22plain_text%22%2C%0A%09%09%09%09%22text%22%3A%20%22High%22%0A%09%09%09%7D%2C%0A%09%09%09%7B%0A%09%09%09%09%22type%22%3A%20%22plain_text%22%2C%0A%09%09%09%09%22text%22%3A%20%22String%22%0A%09%09%09%7D%0A%09%09%5D%0A%09%7D%0A%5D).| _Maybe_| `accessory`| Object| One of the compatible [element objects](/reference/block-kit/blocks/section-block) noted above. Be sure to confirm the desired element works with `section`.| Optional| `expand`| Boolean| Whether or not this section block's text should always expand when rendered. If false or not provided, it may be rendered with a 'see more' option to expand and show the full text. For [AI Assistant apps](/ai), this allows the app to post long messages without users needing to click 'see more' to expand the message.| Optional
---|---|---|---

## Usage info​

A `section` can be used as a text block, in combination with text fields, or side-by-side with certain [block elements](/reference/block-kit/block-elements).

## Examples​

**Example 1** : A text section block:

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "A message *with some bold text* and _some italicized text_."
                }
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/T024BE7LD#%7B%22blocks%22:%5B%7B%22type%22:%22section%22,%22text%22:%7B%22type%22:%22mrkdwn%22,%22text%22:%22A%20message%20*with%20some%20bold%20text*%20and%20_some%20italicized%20text_.%22%7D%7D%5D%7D)

block-kit/src/blocks/section.py


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/section.py#L6-L18
)

block-kit/src/blocks/section.js


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/section.js#L12-L24
)

block-kit/src/main/java/blocks/Section.java


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/Section.java#L17-L21
)

* * *

**Example 2** : A section block containing text fields:

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "text": "A message *with some bold text* and _some italicized text_.",
                    "type": "mrkdwn"
                },
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": "High"
                    },
                    {
                        "type": "plain_text",
                        "emoji": true,
                        "text": "Silly"
                    }
                ]
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/#%7B%22blocks%22:%5B%7B%22type%22:%22section%22,%22text%22:%7B%22text%22:%22A%20message%20*with%20some%20bold%20text*%20and%20_some%20italicized%20text_.%22,%22type%22:%22mrkdwn%22%7D,%22fields%22:%5B%7B%22type%22:%22mrkdwn%22,%22text%22:%22*Priority*%22%7D,%7B%22type%22:%22mrkdwn%22,%22text%22:%22*Type*%22%7D,%7B%22type%22:%22plain_text%22,%22text%22:%22High%22%7D,%7B%22type%22:%22plain_text%22,%22text%22:%22Silly%22%7D%5D%7D%5D%7D)

block-kit/src/blocks/section.py


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/section.py#L21-L34
)

block-kit/src/blocks/section.js


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/section.js#L31-L54
)

block-kit/src/main/java/blocks/Section.java


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/Section.java#L26-L33
)

* * *

**Example 3** : A section block containing a datepicker element:

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "text": "*Haley* has requested you set a deadline for finding a house",
                    "type": "mrkdwn"
                },
                "accessory": {
                    "type": "datepicker",
                    "action_id": "datepicker123",
                    "initial_date": "1990-04-28",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select a date"
                    }
                }
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/#%7B%22blocks%22:%5B%7B%22type%22:%22section%22,%22text%22:%7B%22text%22:%22*Haley*%20has%20requested%20you%20set%20a%20deadline%20for%20finding%20a%20house%22,%22type%22:%22mrkdwn%22%7D,%22accessory%22:%7B%22type%22:%22datepicker%22%7D%7D%5D%7D)

block-kit/src/blocks/section.py


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/section.py#L37-L51
)

block-kit/src/blocks/section.js


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/section.js#L61-L82
)

block-kit/src/main/java/blocks/Section.java


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/Section.java#L38-L45
)