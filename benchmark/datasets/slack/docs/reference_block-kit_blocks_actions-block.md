# Actions block

*Source: https://docs.slack.dev/reference/block-kit/blocks/actions-block*

---

## Fields​

Field| Type| Description| Required?| `type`| String| The type of block. For an actions block, `type` is always `actions`.| Required| `elements`| Object[]| An array of interactive [element objects](/reference/block-kit/block-elements) \- [buttons](/reference/block-kit/block-elements/button-element), [select menus](/reference/block-kit/block-elements/select-menu-element), [overflow menus](/reference/block-kit/block-elements/overflow-menu-element), or [date pickers](/reference/block-kit/block-elements/date-picker-element). There is a maximum of 25 elements in each action block.| Required| `block_id`| String| A unique identifier for a block. If not specified, a `block_id` will be generated. You can use this `block_id` when you receive an interaction payload to [identify the source of the action](/interactivity/handling-user-interaction#payloads). Maximum length for this field is 255 characters. `block_id` should be unique for each message and each iteration of a message. If a message is updated, use a new `block_id`.| Optional
---|---|---|---

## Examples​

**Example 1** : An actions block with a select menu and a button:

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "actions",
                "block_id": "actions1",
                "elements": [
                    {
                        "type": "static_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Which witch is the witchiest witch?"
                        },
                        "action_id": "select_2",
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Matilda"
                                },
                                "value": "matilda"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Glinda"
                                },
                                "value": "glinda"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Granny Weatherwax"
                                },
                                "value": "grannyWeatherwax"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Hermione"
                                },
                                "value": "hermione"
                            }
                        ]
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Cancel"
                        },
                        "value": "cancel",
                        "action_id": "button_1"
                    }
                ]
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/#%7B%22blocks%22:%5B%7B%22type%22:%22actions%22,%22block_id%22:%22actions1%22,%22elements%22:%5B%7B%22type%22:%22static_select%22,%22placeholder%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Which%20witch%20is%20the%20witchiest%20witch?%22%7D,%22action_id%22:%22select_2%22,%22options%22:%5B%7B%22text%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Matilda%22%7D,%22value%22:%22matilda%22%7D,%7B%22text%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Glinda%22%7D,%22value%22:%22glinda%22%7D,%7B%22text%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Granny%20Weatherwax%22%7D,%22value%22:%22grannyWeatherwax%22%7D,%7B%22text%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Hermione%22%7D,%22value%22:%22hermione%22%7D%5D%7D,%7B%22type%22:%22button%22,%22text%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Cancel%22%7D,%22value%22:%22cancel%22,%22action_id%22:%22button_1%22%7D%5D%7D%5D%7D)

block-kit/src/blocks/actions.py


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/actions.py#L11-L41
)

block-kit/src/blocks/actions.js


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/actions.js#L12-L70
)

block-kit/src/main/java/blocks/Actions.java


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/Actions.java#L16-L46
)

* * *

**Example 2** : An actions block with a datepicker, an overflow, and a button:

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "actions",
                "block_id": "actionblock789",
                "elements": [
                    {
                        "type": "datepicker",
                        "action_id": "datepicker123",
                        "initial_date": "1990-04-28",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select a date"
                        }
                    },
                    {
                        "type": "overflow",
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "*this is plain_text text*"
                                },
                                "value": "value-0"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "*this is plain_text text*"
                                },
                                "value": "value-1"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "*this is plain_text text*"
                                },
                                "value": "value-2"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "*this is plain_text text*"
                                },
                                "value": "value-3"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "*this is plain_text text*"
                                },
                                "value": "value-4"
                            }
                        ],
                        "action_id": "overflow"
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Click Me"
                        },
                        "value": "click_me_123",
                        "action_id": "button"
                    }
                ]
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/#%7B%22blocks%22:%5B%7B%22type%22:%22actions%22,%22block_id%22:%22actionblock789%22,%22elements%22:%5B%7B%22type%22:%22datepicker%22,%22action_id%22:%22datepicker123%22,%22initial_date%22:%221990-04-28%22,%22placeholder%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Select%20a%20date%22%7D%7D,%7B%22type%22:%22overflow%22,%22options%22:%5B%7B%22text%22:%7B%22type%22:%22plain_text%22,%22text%22:%22*this%20is%20plain_text%20text*%22%7D,%22value%22:%22value-0%22%7D,%7B%22text%22:%7B%22type%22:%22plain_text%22,%22text%22:%22*this%20is%20plain_text%20text*%22%7D,%22value%22:%22value-1%22%7D,%7B%22text%22:%7B%22type%22:%22plain_text%22,%22text%22:%22*this%20is%20plain_text%20text*%22%7D,%22value%22:%22value-2%22%7D,%7B%22text%22:%7B%22type%22:%22plain_text%22,%22text%22:%22*this%20is%20plain_text%20text*%22%7D,%22value%22:%22value-3%22%7D,%7B%22text%22:%7B%22type%22:%22plain_text%22,%22text%22:%22*this%20is%20plain_text%20text*%22%7D,%22value%22:%22value-4%22%7D%5D,%22action_id%22:%22overflow%22%7D,%7B%22type%22:%22button%22,%22text%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Click%20Me%22%7D,%22value%22:%22click_me_123%22,%22action_id%22:%22button%22%7D%5D%7D%5D%7D)

block-kit/src/blocks/actions.py


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/actions.py#L44-L88
)

block-kit/src/blocks/actions.js


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/actions.js#L77-L147
)

block-kit/src/main/java/blocks/Actions.java


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/Actions.java#L51-L83
)