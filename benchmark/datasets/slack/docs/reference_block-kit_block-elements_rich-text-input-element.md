# Rich text input element

*Source: https://docs.slack.dev/reference/block-kit/block-elements/rich-text-input-element*

---

## Fields​

Field| Type| Description| Required?| `type`| String| The type of element. In this case `type` is always `rich_text_input`.| Required| `action_id`| String| An identifier for the input value when the parent modal is submitted. You can use this when you receive a `view_submission` payload [to identify the value of the input element](/surfaces/modals#interactions). Should be unique in the containing block. Maximum length is 255 characters.| Required| `initial_value`| [Rich text](/reference/block-kit/blocks/rich-text-block)| The initial value in the rich text input when it is loaded.| Optional| `dispatch_action_config`| Object| A [dispatch configuration object](/reference/block-kit/composition-objects/dispatch-action-configuration-object) that determines when during text input the element returns a [`block_actions`](/reference/interaction-payloads/block_actions-payload) payload.| Optional| `focus_on_load`| Boolean| Indicates whether the element will be set to auto focus within the [`view object`](/reference/views). Only one element can be set to `true`. Defaults to `false`.| Optional| `placeholder`| Object| A [`plain_text`](/reference/block-kit/composition-objects/text-object) object that defines the placeholder text shown in the plain-text input. Maximum length for the `text` in this field is 150 characters.| Optional
---|---|---|---

## Example​

The rich text input element must be used inside of the [input](/reference/block-kit/blocks/input-block) block. This example shows an input block containing a rich text input element.


    {
        "blocks": [
            {
                "type": "input",
                "element": {
                    "type": "rich_text_input",
                    "action_id": "rich_text_input-action",
                    "dispatch_action_config": {
                        "trigger_actions_on": [
                            "on_character_entered"
                        ]
                    },
                    "focus_on_load": true,
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Enter text"
                    }
                },
                "label": {
                    "type": "plain_text",
                    "text": "Label",
                    "emoji": true
                }
            }
        ],
        "type": "home"
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/T024BE7LD#%7B%22type%22:%22modal%22,%22title%22:%7B%22type%22:%22plain_text%22,%22text%22:%22My%20App%22,%22emoji%22:true%7D,%22submit%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Submit%22,%22emoji%22:true%7D,%22close%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Cancel%22,%22emoji%22:true%7D,%22blocks%22:%5B%7B%22type%22:%22input%22,%22dispatch_action%22:true,%22element%22:%7B%22type%22:%22rich_text_input%22,%22action_id%22:%22rich_text_input-action%22,%22dispatch_action_config%22:%7B%22trigger_actions_on%22:%5B%22on_enter_pressed%22,%22on_character_entered%22%5D%7D%7D,%22label%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Label%22,%22emoji%22:true%7D%7D%5D%7D)