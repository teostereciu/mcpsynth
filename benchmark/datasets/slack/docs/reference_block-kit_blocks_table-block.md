# Table block

*Source: https://docs.slack.dev/reference/block-kit/blocks/table-block*

---

## Fields​

Field| Type| Description| Required?| `type`| string| Always "table".| Required| `block_id`| string| A unique identifier for a block. If not specified, a `block_id` will be generated. You can use this `block_id` when you receive an interaction payload to identify the source of the action. Maximum length for this field is 255 characters. `block_id` should be unique for each message and each iteration of a message. If a message is updated, use a new `block_id`.| Optional| `rows`| array| An array consisting of table rows. Maximum 100 rows. Each row object is an array with a max of 20 table cells. Table cells can have a type of `rich_text`.| Required| `column_settings`| array| An array describing column behavior. If there are fewer items in the `column_settings` array than there are columns in the table, then the items in the the `column_settings` array will describe the same number of columns in the table as there are in the array itself. Any additional columns will have the default behavior. Maximum 20 items. See below for column settings schema.| Optional
---|---|---|---

### Schema for `column_settings`​

Field| Type| Description| Required?| `align`| string| The alignment for items in this column. Can be `left`, `center`, or `right`. Defaults to `left` if not defined.| Optional| `is_wrapped`| boolean| Whether the contents of this column should be wrapped or not. Defaults to `false` if not defined.| Optional
---|---|---|---

## Usage info​

Apps can programmatically publish messages that include a table by providing a table block in the `attachments` or `blocks` fields of a [`chat.postMessage`](/reference/methods/chat.postMessage#arguments) request. These fields support a top-level table block with `raw_text` and `rich_text` options. Tables may include formatted text (bold text, emoji, mentions, hyperlinks, etc.) with a `rich_text` table cell block type, while a `raw_text` cell supports more basic characters. You must include a value for one of either the top-level blocks or text arguments in the message payload.

The `column_settings` property lets you change text alignment and text wrapping behavior for table columns. In the `JSON` example below, the first column has text wrapping enabled and the second column right aligned. Use null to skip a column.

One table is allowed per message, which is appended as an attachment to the bottom of the message. Sending more than one table block will result in the error `invalid_attachments` with response metadata indicating `only_one_table_allowed`.

Below is an example attachments value that you should send as a URL-encoded string in your request inside the `blocks` array.

## Examples​

  * JSON
  * Python SDK
  * Node SDK
  * Java SDK




    {
        "blocks": [
            {
                "type": "table",
                "column_settings": [
                    {
                        "is_wrapped": true
                    },
                    {
                        "align": "right"
                    }
                ],
                "rows": [
                    [
                        {
                            "type": "raw_text",
                            "text": "Header A"
                        },
                        {
                            "type": "raw_text",
                            "text": "Header B"
                        }
                    ],
                    [
                        {
                            "type": "raw_text",
                            "text": "Data 1A"
                        },
                        {
                            "type": "rich_text",
                            "elements": [
                                {
                                    "type": "rich_text_section",
                                    "elements": [
                                        {
                                            "text": "Data 1B",
                                            "type": "link",
                                            "url": "https://slack.com"
                                        }
                                    ]
                                }
                            ]
                        }
                    ],
                    [
                        {
                            "type": "raw_text",
                            "text": "Data 2A"
                        },
                        {
                            "type": "rich_text",
                            "elements": [
                                {
                                    "type": "rich_text_section",
                                    "elements": [
                                        {
                                            "text": "Data 2B",
                                            "type": "link",
                                            "url": "https://slack.com"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                ]
            }
        ]
    }


[View in Block Kit Builder](https://app.slack.com/block-kit-builder/T024BE7LD#%7B%22blocks%22:%5B%7B%22type%22:%22table%22,%22column_settings%22:%5B%7B%22is_wrapped%22:true%7D,%7B%22align%22:%22right%22%7D%5D,%22rows%22:%5B%5B%7B%22type%22:%22raw_text%22,%22text%22:%22Header%20A%22%7D,%7B%22type%22:%22raw_text%22,%22text%22:%22Header%20B%22%7D%5D,%5B%7B%22type%22:%22raw_text%22,%22text%22:%22Data%201A%22%7D,%7B%22type%22:%22rich_text%22,%22elements%22:%5B%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22text%22:%22Data%201B%22,%22type%22:%22link%22,%22url%22:%22https://slack.com%22%7D%5D%7D%5D%7D%5D,%5B%7B%22type%22:%22raw_text%22,%22text%22:%22Data%202A%22%7D,%7B%22type%22:%22rich_text%22,%22elements%22:%5B%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22text%22:%22Data%202B%22,%22type%22:%22link%22,%22url%22:%22https://slack.com%22%7D%5D%7D%5D%7D%5D%5D%7D%5D%7D)

Support coming soon!


    export function example01() {
      /**
       * @type {import('@slack/types').TableBlock}
       */
      const block = {
        type: "table",
        column_settings: [
          {
            is_wrapped: true,
          },
          {
            align: "right",
          },
        ],
        rows: [
          [
            {
              type: "raw_text",
              text: "Header A",
            },
            {
              type: "raw_text",
              text: "Header B",
            },
          ],
          [
            {
              type: "raw_text",
              text: "Data 1A",
            },
            {
              type: "rich_text",
              elements: [
                {
                  type: "rich_text_section",
                  elements: [
                    {
                      text: "Data 1B",
                      type: "link",
                      url: "https://slack.com",
                    },
                  ],
                },
              ],
            },
          ],
          [
            {
              type: "raw_text",
              text: "Data 2A",
            },
            {
              type: "rich_text",
              elements: [
                {
                  type: "rich_text_section",
                  elements: [
                    {
                      text: "Data 2B",
                      type: "link",
                      url: "https://slack.com",
                    },
                  ],
                },
              ],
            },
          ],
        ],
      };
      return block;
    }


Support coming soon!