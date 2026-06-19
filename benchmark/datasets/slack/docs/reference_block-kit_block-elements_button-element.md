# Button element

*Source: https://docs.slack.dev/reference/block-kit/block-elements/button-element*

---

Example:

## Fields​

Field| Type| Description| Required?| `type`| String| The type of element. In this case `type` is always `button`.| Required| `text`| Object| A [text object](/reference/block-kit/composition-objects/text-object) that defines the button's text. Can only be of `type: plain_text`. `text` may truncate with ~30 characters. Maximum length for the `text` in this field is 75 characters.| Required| `action_id`| String| An identifier for this action. You can use this when you receive an interaction payload to [identify the source of the action](/interactivity/handling-user-interaction#payloads). Should be unique among all other `action_id`s in the containing block. Maximum length is 255 characters.| Optional| `url`| String| A URL to load in the user's browser when the button is clicked. Maximum length is 3000 characters. If you're using `url`, you'll still receive an [interaction payload](/interactivity/handling-user-interaction#payloads) and will need to [send an acknowledgement response](/interactivity/handling-user-interaction#acknowledgment_response).| Optional| `value`| String| The value to send along with the [interaction payload](/interactivity/handling-user-interaction#payloads). Maximum length is 2000 characters.| Optional| `style`| String| Decorates buttons with alternative visual color schemes. Use this option with restraint.`primary` gives buttons a green outline and text, ideal for affirmation or confirmation actions. `primary` should only be used for one button within a set.`danger` gives buttons a red outline and text, and should be used when the action is destructive. Use `danger` even more sparingly than `primary`.If you don't include this field, the default button style will be used.| Optional| `confirm`| Object| A [confirm object](/reference/block-kit/composition-objects/confirmation-dialog-object) that defines an optional confirmation dialog after the button is clicked.| Optional| `accessibility_label`| String| A label for longer descriptive text about a button element. This label will be read out by screen readers _instead of_ the button [`text`](/reference/block-kit/composition-objects/text-object) object. Maximum length is 75 characters.| Optional
---|---|---|---

## Examples​

A regular interactive button:


    {
      "type": "button",
      "text": {
        "type": "plain_text",
        "text": "Click Me"
      },
      "value": "click_me_123",
      "action_id": "button"
    }


A button with a `primary` `style` attribute:


    {
      "type": "button",
      "text": {
        "type": "plain_text",
        "text": "Save"
      },
      "style": "primary",
      "value": "click_me_123",
      "action_id": "button"
    }


A link button:


    {
      "type": "button",
      "text": {
        "type": "plain_text",
        "text": "Link Button"
      },
      "url": "https://docs.slack.dev/block-kit"
    }


The button element must be used inside either the [section](/reference/block-kit/blocks/section-block) or [actions](/reference/block-kit/blocks/actions-block) block, like this:


    {
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "This is a section block with a button."
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me"
                    },
                    "value": "click_me_123",
                    "action_id": "button"
                }
            },
            {
                "type": "actions",
                "block_id": "actionblock789",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Primary Button"
                        },
                        "style": "primary",
                        "value": "click_me_456"
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Link Button"
                        },
                        "url": "https://api.slack.com/block-kit"
                    }
                ]
            }
        ]
    }


[View in Block Kit Builder](https://api.slack.com/tools/block-kit-builder?blocks=%5B%0A%09%7B%0A%09%09%22type%22%3A%20%22section%22%2C%0A%09%09%22text%22%3A%20%7B%0A%09%09%09%22type%22%3A%20%22mrkdwn%22%2C%0A%09%09%09%22text%22%3A%20%22This%20is%20a%20section%20block%20with%20a%20button.%22%0A%09%09%7D%2C%0A%09%09%22accessory%22%3A%20%7B%0A%09%09%09%22type%22%3A%20%22button%22%2C%0A%09%09%09%22text%22%3A%20%7B%0A%09%09%09%09%22type%22%3A%20%22plain_text%22%2C%0A%09%09%09%09%22text%22%3A%20%22Click%20Me%22%0A%09%09%09%7D%2C%0A%09%09%09%22value%22%3A%20%22click_me_123%22%2C%0A%09%09%09%22action_id%22%3A%20%22button%22%0A%09%09%7D%0A%09%7D%2C%0A%09%7B%0A%09%09%22type%22%3A%20%22actions%22%2C%0A%09%09%22block_id%22%3A%20%22actionblock789%22%2C%0A%09%09%22elements%22%3A%20%5B%0A%09%09%09%7B%0A%09%09%09%09%22type%22%3A%20%22button%22%2C%0A%09%09%09%09%22text%22%3A%20%7B%0A%09%09%09%09%09%22type%22%3A%20%22plain_text%22%2C%0A%09%09%09%09%09%22text%22%3A%20%22Primary%20Button%22%0A%09%09%09%09%7D%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22style%22%3A%20%22primary%22%2C%0A%09%09%09%09%22value%22%3A%20%22click_me_456%22%0A%09%09%09%7D%2C%0A%09%09%09%7B%0A%09%09%09%09%22type%22%3A%20%22button%22%2C%0A%09%09%09%09%22text%22%3A%20%7B%0A%09%09%09%09%09%22type%22%3A%20%22plain_text%22%2C%0A%09%09%09%09%09%22text%22%3A%20%22Link%20Button%22%0A%09%09%09%09%7D%2C%0A%09%09%09%09%22url%22%3A%20%22https%3A%2F%2Fapi.slack.com%2Fblock-kit%22%0A%09%09%09%7D%0A%09%09%5D%0A%09%7D%0A%5D)