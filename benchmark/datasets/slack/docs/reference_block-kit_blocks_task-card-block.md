# Task card block

*Source: https://docs.slack.dev/reference/block-kit/blocks/task-card-block*

---

## Fields​

Field| Type| Description| Required?| `type`| String| The type of block. For this block, type will always be `task_card`.| Required| `task_id`| String| ID for the task.| Required| `title`| String| Title of the task in plain text.| Required| `details`| Object| Details of the task in the form of a single [`rich_text`](/reference/block-kit/blocks/rich-text-block) entity.| Optional| `output`| Object| Output of the task in the form of a single [`rich_text`](/reference/block-kit/blocks/rich-text-block) entity.| Optional| `sources`| Array| Array of [URL source elements](/reference/block-kit/block-elements/url-source-element) used to generate a response.| Optional| `status`| String| The state of a task. Can be `"pending"`, `"in_progress"`, `"complete"`, or `"error"`.| Optional| `block_id`| String| A unique identifier for a block. If not specified, one will be generated. Maximum length for this field is 255 characters. `block_id` should be unique for each message and each iteration of a message. If a message is updated, use a new `block_id`.| Optional
---|---|---|---

## Usage info​

A `task_card` block displays a single task which represents a single action. It includes a title, optional details and output (both as rich text), sources, and a status indicator.

## Examples​

  * JSON




    {
      "blocks": [
        {
          "type": "task_card",
          "task_id": "task_1",
          "title": "Fetching weather data",
          "status": "pending",
          "output": {
            "type": "rich_text",
            "elements": [
              {
                "type": "rich_text_section",
                "elements": [
                  {
                    "type": "text",
                    "text": "Found weather data for Chicago from 2 sources"
                  }
                ]
              }
            ]
          },
          "sources": [
            {
              "type": "url",
              "url": "https://weather.com/",
              "text": "weather.com"
            },
            {
              "type": "url",
              "url": "https://www.accuweather.com/",
              "text": "accuweather.com"
            }
          ]
        }
      ]
    }