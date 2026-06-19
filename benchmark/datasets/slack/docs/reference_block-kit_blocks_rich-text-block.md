# Rich text block

*Source: https://docs.slack.dev/reference/block-kit/blocks/rich-text-block*

---

## Fields​

Field| Type| Description| Required?| `type`| String| The type of block. For a rich text block, `type` is always `rich_text`.| Required| `elements`| Object[]| An array of rich text objects - [`rich_text_section`](/reference/block-kit/blocks/rich-text-block#section), [`rich_text_list`](/reference/block-kit/blocks/rich-text-block#list), [`rich_text_preformatted`](/reference/block-kit/blocks/rich-text-block#preformatted), and [`rich_text_quote`](/reference/block-kit/blocks/rich-text-block#quote). See your specific desired element below for more details.| Required| `block_id`| String| A unique identifier for a block. If not specified, one will be generated. Maximum length for this field is 255 characters. `block_id` should be unique for each message or view and each iteration of a message or view. If a message or view is updated, use a new `block_id`.| Optional
---|---|---|---

## Usage info​

It is also the output of the Slack client's WYSIWYG message composer, so all messages sent by end-users will have this format. Use this block to include user-defined formatted text in your Block Kit payload. While it is possible to format text with `mrkdwn`, `rich_text` is strongly preferred and allows greater flexibility.

You might encounter a `rich_text` block in a message payload, as a built-in type in apps created with the Deno Slack SDK, or as output of the [`rich_text_input`](/reference/block-kit/block-elements/rich-text-input-element) block element.

Rich text blocks can be deeply nested. For instance: a `rich_text_list` can contain a `rich_text_section` which can contain bold style text. More details on how that works is shown in the examples.

Sub-elements are what comprise the `elements` array in a rich text block. There are four available rich text object sub-elements.: `rich_text_section`, `rich_text_list`, `rich_text_preformatted`, and `rich_text_quote`. Because many of the elements include a section block, the details of that element are listed first, followed by the others.

### Section element: `rich_text_section`​

Field| Type| Description| Required?| `type`| String| The type of sub-element; in this case, `rich_text_section`.| Required| `elements`| Object []| An array of rich text elements.| Required
---|---|---|---
`rich_text_section` example

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "rich_text",
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "text",
                                "text": "Hello there, I am a basic rich text block!"
                            }
                        ]
                    }
                ]
            },
            {
                "type": "rich_text",
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "text",
                                "text": "Hello there, "
                            },
                            {
                                "type": "text",
                                "text": "I am a bold rich text block!",
                                "style": {
                                    "bold": true
                                }
                            }
                        ]
                    }
                ]
            },
            {
                "type": "rich_text",
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "text",
                                "text": "Hello there, "
                            },
                            {
                                "type": "text",
                                "text": "I am an italic rich text block!",
                                "style": {
                                    "italic": true
                                }
                            }
                        ]
                    }
                ]
            },
            {
                "type": "rich_text",
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "text",
                                "text": "Hello there, "
                            },
                            {
                                "type": "text",
                                "text": "I am a strikethrough rich text block!",
                                "style": {
                                    "strike": true
                                }
                            }
                        ]
                    }
                ]
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/#%7B%22blocks%22:%5B%7B%22type%22:%22rich_text%22,%22elements%22:%5B%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22Hello%20there,%20I%20am%20a%20basic%20rich%20text%20block!%22%7D%5D%7D%5D%7D,%7B%22type%22:%22rich_text%22,%22elements%22:%5B%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22Hello%20there,%20%22%7D,%7B%22type%22:%22text%22,%22text%22:%22I%20am%20a%20bold%20rich%20text%20block!%22,%22style%22:%7B%22bold%22:true%7D%7D%5D%7D%5D%7D,%7B%22type%22:%22rich_text%22,%22elements%22:%5B%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22Hello%20there,%20%22%7D,%7B%22type%22:%22text%22,%22text%22:%22I%20am%20an%20italic%20rich%20text%20block!%22,%22style%22:%7B%22italic%22:true%7D%7D%5D%7D%5D%7D,%7B%22type%22:%22rich_text%22,%22elements%22:%5B%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22Hello%20there,%20%22%7D,%7B%22type%22:%22text%22,%22text%22:%22I%20am%20a%20strikethrough%20rich%20text%20block!%22,%22style%22:%7B%22strike%22:true%7D%7D%5D%7D%5D%7D%5D%7D)

block-kit/src/blocks/rich_text.py


    loading...


[View on GitHub](
https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/rich_text.py#L11-L69
)

block-kit/src/blocks/rich_text.js


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/rich_text.js#L12-L96
)

block-kit/src/main/java/blocks/RichText.java


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/RichText.java#L20-L58
)

### List element: `rich_text_list`​

Field| Type| Description| Required?| `type`| String| The type of sub-element; in this case, `rich_text_list`.| Required| `style`| String| Either `bullet` or `ordered`, the latter meaning a numbered list.| Required| `elements`| Object []| An array of [`rich_text_section`](/reference/block-kit/blocks/rich-text-block#section) objects containing two properties: `type`, which is "rich_text_section", and `elements`, which is an array of rich text element objects.| Required| `indent`| Number| Sub-list indent level.| Optional| `offset`| Number| Number to offset the first number in the list. For example, if the `offset = 4`, the first number in the ordered list would be 5.| Optional| `border`| Number| Turn the border on or off.| Optional
---|---|---|---
`rich_text_list` example

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "rich_text",
                "block_id": "block1",
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "text",
                                "text": "My favorite Slack features (in no particular order):"
                            }
                        ]
                    },
                    {
                        "type": "rich_text_list",
                        "elements": [
                            {
                                "type": "rich_text_section",
                                "elements": [
                                    {
                                        "type": "text",
                                        "text": "Huddles"
                                    }
                                ]
                            },
                            {
                                "type": "rich_text_section",
                                "elements": [
                                    {
                                        "type": "text",
                                        "text": "Canvas"
                                    }
                                ]
                            },
                            {
                                "type": "rich_text_section",
                                "elements": [
                                    {
                                        "type": "text",
                                        "text": "Developing with Block Kit"
                                    }
                                ]
                            }
                        ],
                        "style": "bullet",
                        "indent": 0,
                        "border": 1
                    }
                ]
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/T024BE7LD#%7B%22blocks%22:%5B%7B%22type%22:%22rich_text%22,%22block_id%22:%22block1%22,%22elements%22:%5B%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22My%20favorite%20Slack%20features%20\(in%20no%20particular%20order\):%22%7D%5D%7D,%7B%22type%22:%22rich_text_list%22,%22elements%22:%5B%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22Huddles%22%7D%5D%7D,%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22Canvas%22%7D%5D%7D,%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22Developing%20with%20Block%20Kit%22%7D%5D%7D%5D,%22style%22:%22bullet%22,%22indent%22:0,%22border%22:1%7D%5D%7D%5D%7D)

block-kit/src/blocks/rich_text.py


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/rich_text.py#L72-L106
)

block-kit/src/blocks/rich_text.js


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/rich_text.js#L103-L158
)

block-kit/src/main/java/blocks/RichText.java


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/RichText.java#L63-L93
)

Let's say we want to create a nested list, for example something that looks like this:

Breakfast foods I enjoy:

  * Hashbrowns
  * Eggs
    * Scrambled
    * Over easy
  * Pancakes, extra syrup


To create that in rich text, create three instances of `rich_text_list`, the middle one using the `indent` property to indent the types of eggs into that sub-list.

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "rich_text",
                "block_id": "block1",
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "text",
                                "text": "Breakfast foods I enjoy:"
                            }
                        ]
                    },
                    {
                        "type": "rich_text_list",
                        "style": "bullet",
                        "elements": [
                            {
                                "type": "rich_text_section",
                                "elements": [
                                    {
                                        "type": "text",
                                        "text": "Hashbrowns"
                                    }
                                ]
                            },
                            {
                                "type": "rich_text_section",
                                "elements": [
                                    {
                                        "type": "text",
                                        "text": "Eggs"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "rich_text_list",
                        "style": "bullet",
                        "indent": 1,
                        "elements": [
                            {
                                "type": "rich_text_section",
                                "elements": [
                                    {
                                        "type": "text",
                                        "text": "Scrambled"
                                    }
                                ]
                            },
                            {
                                "type": "rich_text_section",
                                "elements": [
                                    {
                                        "type": "text",
                                        "text": "Over easy"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "rich_text_list",
                        "style": "bullet",
                        "elements": [
                            {
                                "type": "rich_text_section",
                                "elements": [
                                    {
                                        "type": "text",
                                        "text": "Pancakes, extra syrup"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/T024BE7LD#%7B%22blocks%22:%5B%7B%22type%22:%22rich_text%22,%22block_id%22:%22block1%22,%22elements%22:%5B%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22Breakfast%20foods%20I%20enjoy:%22%7D%5D%7D,%7B%22type%22:%22rich_text_list%22,%22style%22:%22bullet%22,%22elements%22:%5B%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22Hashbrowns%22%7D%5D%7D,%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22Eggs%22%7D%5D%7D%5D%7D,%7B%22type%22:%22rich_text_list%22,%22style%22:%22bullet%22,%22indent%22:1,%22elements%22:%5B%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22Scrambled%22%7D%5D%7D,%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22Over%20easy%22%7D%5D%7D%5D%7D,%7B%22type%22:%22rich_text_list%22,%22style%22:%22bullet%22,%22elements%22:%5B%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22Pancakes,%20extra%20syrup%22%7D%5D%7D%5D%7D%5D%7D%5D%7D)

block-kit/src/blocks/rich_text.py


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/rich_text.py#L109-L154
)

block-kit/src/blocks/rich_text.js


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/rich_text.js#L165-L249
)

block-kit/src/main/java/blocks/RichText.java


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/RichText.java#L98-L144
)

### Preformatted code block element: `rich_text_preformatted`​

Field| Type| Description| Required?| `type`| String| The type of the sub-element; in this case, `rich_text_preformatted`.| Required| `elements`| Object []| An array of rich text elements.| Required| `border`| Number| Turn the border on or off.| Optional| `language`| String| The language of the code block, used for syntax highlighting (e.g., `"python"`, `"javascript"`, `"json"`).| Optional
---|---|---|---
`rich_text_preformatted` example

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "rich_text",
                "elements": [
                    {
                        "type": "rich_text_preformatted",
                        "elements": [
                            {
                                "type": "text",
                                "text": "{\n  \"object\": {\n    \"description\": \"this is an example of a json object\"\n  }\n}"
                            }
                        ],
                        "border": 0
                    }
                ]
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/T024BE7LD#%7B%22blocks%22:%5B%7B%22type%22:%22rich_text%22,%22elements%22:%5B%7B%22type%22:%22rich_text_preformatted%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22%7B%5Cn%20%20%5C%22object%5C%22:%20%7B%5Cn%20%20%20%20%5C%22description%5C%22:%20%5C%22this%20is%20an%20example%20of%20a%20json%20object%5C%22%5Cn%20%20%7D%5Cn%7D%22%7D%5D,%22border%22:0%7D%5D%7D%5D%7D)

block-kit/src/blocks/rich_text.py


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/rich_text.py#L157-L173
)

block-kit/src/blocks/rich_text.js


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/rich_text.js#L256-L276
)

block-kit/src/main/java/blocks/RichText.java


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/RichText.java#L149-L158
)

### Quote element: `rich_text_quote`​

Field| Type| Description| Required?| `type`| String| The type of the sub-element; in this case, `rich_text_quote`.| Required| `elements`| Object []| An array of rich text elements.| Required| `border`| Number| Turn the border on or off.| Optional
---|---|---|---
`rich_text_quote` example

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "rich_text",
                "block_id": "Vrzsu",
                "elements": [
                    {
                        "type": "rich_text_quote",
                        "elements": [
                            {
                                "type": "text",
                                "text": "What we need is good examples in our documentation."
                            }
                        ]
                    },
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "text",
                                "text": "Yes - I completely agree, Luke!"
                            }
                        ]
                    }
                ]
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/T024BE7LD#%7B%22blocks%22:%5B%7B%22type%22:%22rich_text%22,%22block_id%22:%22Vrzsu%22,%22elements%22:%5B%7B%22type%22:%22rich_text_quote%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22What%20we%20need%20is%20good%20examples%20in%20our%20documentation.%22%7D%5D%7D,%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22Yes%20-%20I%20completely%20agree,%20Luke!%22%7D%5D%7D%5D%7D%5D%7D)

block-kit/src/blocks/rich_text.py


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/rich_text.py#L176-L197
)

block-kit/src/blocks/rich_text.js


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/rich_text.js#L283-L312
)

block-kit/src/main/java/blocks/RichText.java


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/RichText.java#L163-L177
)

### Rich text element types​

For the rich text elements that have a field of `elements`, the following types are possible.

#### `broadcast`​

The following are the properties of the `broadcast` object type in the `elements` array.

Field| Type| Description| Required?| `type`| String| The type of object; in this case, "broadcast".| Required| `range`| String| The range of the broadcast; value can be `here`, `channel`, or `everyone`. Using `here` notifies only the active members of a channel; `channel` notifies all members of a channel; `everyone` notifies every person in the #general channel.| Required| `style`| Object| An object of six optional boolean properties that dictate style: `bold`, `italic`, `strike`, and `underline`.| Optional
---|---|---|---
`broadcast` example

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "rich_text",
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "broadcast",
                                "range": "everyone"
                            }
                        ]
                    }
                ]
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/T024BE7LD#%7B%22blocks%22:%5B%7B%22type%22:%22rich_text%22,%22elements%22:%5B%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22broadcast%22,%22range%22:%22everyone%22%7D%5D%7D%5D%7D%5D%7D)

block-kit/src/blocks/rich_text.py


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/rich_text.py#L200-L211
)

block-kit/src/blocks/rich_text.js


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/rich_text.js#L319-L338
)

block-kit/src/main/java/blocks/RichText.java


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/RichText.java#L182-L189
)

#### `color`​

The following are the properties of the `color` object type in the `elements` array.

Field| Type| Description| Required?| `type`| String| The type of object; in this case, "color".| Required| `value`| String| The hex value for the color.| Required| `style`| Object| An object of six optional boolean properties that dictate style: `bold`, `italic`, `strike`, `highlight`, `client_highlight`, and `underline`.| Optional
---|---|---|---
`color` example

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "rich_text",
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "color",
                                "value": "#F405B3"
                            }
                        ]
                    }
                ]
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/T024BE7LD#%7B%22blocks%22:%5B%7B%22type%22:%22rich_text%22,%22elements%22:%5B%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22color%22,%22value%22:%22#F405B3%22%7D%5D%7D%5D%7D%5D%7D)

block-kit/src/blocks/rich_text.py


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/rich_text.py#L214-L225
)

block-kit/src/blocks/rich_text.js


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/rich_text.js#L345-L364
)

block-kit/src/main/java/blocks/RichText.java


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/RichText.java#L194-L200
)

#### `channel`​

The following are the properties of the `channel` object type in the `elements` array.

Field| Type| Description| Required?| `type`| String| The type of object; in this case, "channel".| Required| `channel_id`| String| The ID of the channel to be mentioned.| Required| `style`| Object| An object of six optional boolean properties that dictate style: `bold`, `italic`, `strike`, `highlight`, `client_highlight`, `underline`, and `unlink`.| Optional
---|---|---|---
`channel` example

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "rich_text",
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "channel",
                                "channel_id": "C123ABC456"
                            }
                        ]
                    }
                ]
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/#%7B%2522blocks%2522%3A%255B%257B%2522type%2522%3A%2522rich_text%2522%2C%2522elements%2522%3A%255B%257B%2522type%2522%3A%2522rich_text_section%2522%2C%2522elements%2522%3A%255B%257B%2522type%2522%3A%2522channel%2522%2C%2522channel_id%2522%3A%2522C123ABC456%2522%257D%255D%257D%255D%257D%255D%257D)

block-kit/src/blocks/rich_text.py


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/rich_text.py#L228-L239
)

block-kit/src/blocks/rich_text.js


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/rich_text.js#L371-L390
)

block-kit/src/main/java/blocks/RichText.java


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/RichText.java#L205-L212
)

#### `date`​

The following are the properties of the `date` object type in the `elements` array.

Field| Type| Description| Required?| `type`| String| The type of object; in this case "date".| Required| `timestamp`| Number| A Unix timestamp for the date to be displayed in seconds.| Required| `format`| String| A template string containing curly-brace-enclosed tokens to substitute your provided `timestamp`. See details below.| Required| `url`| String| URL to link the entire `format` string to.| Optional| `fallback`| String| Text to display in place of the date should parsing, formatting or displaying fail.| Optional| `style`| Object| An object of six optional boolean properties that dictate style: `bold`, `italic`, `strike`, `highlight`, `client_highlight`, and `underline`.| Optional
---|---|---|---

#### Date format strings​

The following are the template strings allowed by the `format` property of the `date` element type.

  * `{day_divider_pretty}`: Shows `today`, `yesterday` or `tomorrow` if applicable. Otherwise, if the date is in current year, uses the `{date_long}` format without the year. Otherwise, falls back to using the `{date_long}` format.
  * `{date_num}`: Shows date as YYYY-MM-DD.
  * `{date_slash}`: Shows date as DD/MM/YYYY (subject to locale preferences).
  * `{date_long}`: Shows date as a long-form sentence including day-of-week, e.g. `Monday, December 23rd, 2013`.
  * `{date_long_full}`: Shows date as a long-form sentence without day-of-week, e.g. `August 9, 2020`.
  * `{date_long_pretty}`: Shows `yesterday`, `today` or `tomorrow`, otherwise uses the `{date_long}` format.
  * `{date}`: Same as `{date_long_full}` but without the year.
  * `{date_pretty}`: Shows `today`, `yesterday` or `tomorrow` if applicable, otherwise uses the `{date}` format.
  * `{date_short}`: Shows date using short month names without day-of-week, e.g. `Aug 9, 2020`.
  * `{date_short_pretty}`: Shows `today`, `yesterday` or `tomorrow` if applicable, otherwise uses the `{date_short}` format.
  * `{time}`: Depending on user preferences, shows just the time-of-day portion of the timestamp using either 12 or 24 hour clock formats, e.g. `2:34 PM` or `14:34`.
  * `{time_secs}`: Depending on user preferences, shows just the time-of-day portion of the timestamp using either 12 or 24 hour clock formats, including seconds, e.g. `2:34:56 PM` or `14:34:56`.
  * `{ago}`: A human-readable period of time, e.g. `3 minutes ago`, `4 hours ago`, `2 days ago`.

`date` example

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "rich_text",
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "date",
                                "timestamp": 1720710212,
                                "format": "{date_num} at {time}",
                                "fallback": "timey"
                            }
                        ]
                    }
                ]
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/T024BE7LD#%7B%22blocks%22:%5B%7B%22type%22:%22rich_text%22,%22elements%22:%5B%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22date%22,%22timestamp%22:1720710212,%22format%22:%22%7Bdate_num%7D%20at%20%7Btime%7D%22,%22fallback%22:%22timey%22%7D%5D%7D%5D%7D%5D%7D)

block-kit/src/blocks/rich_text.py


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/rich_text.py#L242-L259
)

block-kit/src/blocks/rich_text.js


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/rich_text.js#L397-L418
)

block-kit/src/main/java/blocks/RichText.java


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/RichText.java#L217-L226
)

#### `emoji`​

The following are the properties of the `emoji` object type in the `elements` array.

Field| Type| Description| Required?| `type`| String| The type of object; in this case, "emoji".| Required| `name`| String| The name of the emoji; i.e. "wave" or "wave::skin-tone-2".| Required| `unicode`| String| Represents the unicode code point of the emoji, where applicable.| Optional
---|---|---|---
`emoji` example

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "rich_text",
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "emoji",
                                "name": "basketball"
                            },
                            {
                                "type": "text",
                                "text": " "
                            },
                            {
                                "type": "emoji",
                                "name": "snowboarder"
                            },
                            {
                                "type": "text",
                                "text": " "
                            },
                            {
                                "type": "emoji",
                                "name": "checkered_flag"
                            }
                        ]
                    }
                ]
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/#%7B%2522blocks%2522%3A%255B%257B%2522type%2522%3A%2522rich_text%2522%2C%2522elements%2522%3A%255B%257B%2522type%2522%3A%2522rich_text_section%2522%2C%2522elements%2522%3A%255B%257B%2522type%2522%3A%2522emoji%2522%2C%2522name%2522%3A%2522basketball%2522%257D%2C%257B%2522type%2522%3A%2522text%2522%2C%2522text%2522%3A%2522%2520%2522%257D%2C%257B%2522type%2522%3A%2522emoji%2522%2C%2522name%2522%3A%2522snowboarder%2522%257D%2C%257B%2522type%2522%3A%2522text%2522%2C%2522text%2522%3A%2522%2520%2522%257D%2C%257B%2522type%2522%3A%2522emoji%2522%2C%2522name%2522%3A%2522checkered_flag%2522%257D%255D%257D%255D%257D%255D%257D)

block-kit/src/blocks/rich_text.py


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/rich_text.py#L262-L279
)

block-kit/src/blocks/rich_text.js


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/rich_text.js#L425-L460
)

block-kit/src/main/java/blocks/RichText.java


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/RichText.java#L231-L247
)

#### `link`​

The following are the properties of the `link` object type in the `elements` array.

Field| Type| Description| Required?| `type`| String| The type of object; in this case "link".| Required| `url`| String| The link's url.| Required| `text`| String| The text shown to the user (instead of the url). If no text is provided, the url is used.| Optional| `unsafe`| Boolean| Indicates whether the link is safe.| Optional| `style`| Object| An object containing four boolean properties: `bold`, `italic`, `strike`, `code`, and `underline`.| Optional
---|---|---|---
`link` example

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "rich_text",
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "link",
                                "url": "https://docs.slack.dev"
                            }
                        ]
                    }
                ]
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/#%7B%2522blocks%2522%3A%255B%257B%2522type%2522%3A%2522rich_text%2522%2C%2522elements%2522%3A%255B%257B%2522type%2522%3A%2522rich_text_section%2522%2C%2522elements%2522%3A%255B%257B%2522type%2522%3A%2522link%2522%2C%2522url%2522%3A%2522https%3A%2F%2Fapi.slack.com%2522%257D%255D%257D%255D%257D%255D%257D)

block-kit/src/blocks/rich_text.py


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/rich_text.py#L282-L293
)

block-kit/src/blocks/rich_text.js


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/rich_text.js#L467-L486
)

block-kit/src/main/java/blocks/RichText.java


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/RichText.java#L252-L259
)

#### `text`​

The following are the properties of the `text` object type in the `elements` array.

Field| Type| Description| Required?| `type`| String| The type of object; in this case, "text".| Required| `text`| String| The text shown to the user.| Required| `style`| Object| An object containing four boolean fields, none of which are required: `bold`, `italic`, `strike`, `code`, and `underline`.| Optional
---|---|---|---
`text` example


    {
      "type": "rich_text",
      "elements": [
        {
          "type": "rich_text_section",
          "elements": [
            {
              "type": "text",
              "text": "Hello there, "
            },
            {
              "type": "text",
              "text": "I am a bold rich text block!",
              "style": {
                "bold": true
              }
            }
          ]
        }
      ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/#%7B%2522blocks%2522%3A%255B%257B%2522type%2522%3A%2522rich_text%2522%2C%2522elements%2522%3A%255B%257B%2522type%2522%3A%2522rich_text_section%2522%2C%2522elements%2522%3A%255B%257B%2522type%2522%3A%2522text%2522%2C%2522text%2522%3A%2522Hello%2520there%2C%2520%2522%257D%2C%257B%2522type%2522%3A%2522text%2522%2C%2522text%2522%3A%2522I%2520am%2520a%2520bold%2520rich%2520text%2520block%21%2522%2C%2522style%2522%3A%257B%2522bold%2522%3Atrue%257D%257D%255D%257D%255D%257D%255D%257D)

#### `user`​

The following are the properties of the `user` object type in the `elements` array.

Field| Type| Description| Required?| `type`| String| The type of object; in this case, "user".| Required| `user_id`| String| The ID of the user to be mentioned.| Required| `style`| Object| An object of six optional boolean properties that dictate style: `bold`, `italic`, `strike`, `highlight`, `client_highlight`, `unlink`, and `underline`.| Optional
---|---|---|---
`user` example

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "rich_text",
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "user",
                                "user_id": "U123ABC456"
                            }
                        ]
                    }
                ]
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/#%7B%2522blocks%2522%3A%255B%257B%2522type%2522%3A%2522rich_text%2522%2C%2522elements%2522%3A%255B%257B%2522type%2522%3A%2522rich_text_section%2522%2C%2522elements%2522%3A%255B%257B%2522type%2522%3A%2522user%2522%2C%2522user_id%2522%3A%2522U123ABC456%2522%257D%255D%257D%255D%257D%255D%257D)

block-kit/src/blocks/rich_text.py


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/rich_text.py#L296-L307
)

block-kit/src/blocks/rich_text.js


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/rich_text.js#L493-L512
)

block-kit/src/main/java/blocks/RichText.java


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/RichText.java#L264-L271
)

#### `usergroup`​

The following ar the properties of the `usergroup` object type in the `elements` array.

Field| Type| Description| Required?| `type`| String| The type of object; in this case "usergroup".| Required| `usergroup_id`| String| The ID of the user group to be mentioned.| Required| `style`| Object| An object of six optional boolean properties that dictate style: `bold`, `italic`, `strike`, `highlight`, `client_highlight`, `unlink`, and `underline`.| Optional
---|---|---|---
`usergroup` example

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "rich_text",
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "usergroup",
                                "usergroup_id": "G123ABC456"
                            }
                        ]
                    }
                ]
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/#%7B%2522blocks%2522%3A%255B%257B%2522type%2522%3A%2522rich_text%2522%2C%2522elements%2522%3A%255B%257B%2522type%2522%3A%2522rich_text_section%2522%2C%2522elements%2522%3A%255B%257B%2522type%2522%3A%2522usergroup%2522%2C%2522usergroup_id%2522%3A%2522G123ABC456%2522%257D%255D%257D%255D%257D%255D%257D)

block-kit/src/blocks/rich_text.py


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-python-examples/blob/main/block-kit/src/blocks/rich_text.py#L310-L321
)

block-kit/src/blocks/rich_text.js


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-js-examples/blob/main/block-kit/src/blocks/rich_text.js#L519-L538
)

block-kit/src/main/java/blocks/RichText.java


    loading...


[View on GitHub](https://github.com/slack-samples/bolt-java-examples/blob/main/block-kit/src/main/java/blocks/RichText.java#L276-L283
)