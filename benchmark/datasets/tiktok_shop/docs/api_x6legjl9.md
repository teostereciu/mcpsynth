# (63) Activity change

*Source: https://partner.tiktokshop.com/docv2/page/x6legjl9*

---

## Trigger scenario
The Activity change webhook is designed to notify partners about modifications related to  activities and the products associated with them. This allows applications to stay synchronized with changes in activity details or product inclusion/exclusion lists.
## Data business parameters
| Properties | Type | Example | Description |
| --- | --- | --- | --- |
| shop_id | String | "7494049642642441621" | The ID of the shop. |
| timestamp | Int64 | 1732526400 | The time when this webhook was triggered, represented by Unix timestamp. |
| tts_notification_id | String | "7327112393057371910" | The ID of the notification. |
| type | Int64 | 63 | The ID of the webhook type. |
| data | Object |  |  |
| └ activity_id | String | "7136104329798256386" | The ID of the promotion activity. |
| └ update_time | Int64 | 1732526465 | The time when the status changed, represented as a Unix timestamp (seconds). |
| └ change_type | String | CREATE | The type of activity changes.  <br>  <br> * CREATE <br> * UPDATE <br> * DEACTIVATE |
| └ product_update_list | Object |  | Products included in an updated scope. |
| └└ product_ids | []String | ["123456","789012"] | Included product IDs. |
| └└ exclude_product_ids | []String | ["345678"] | IDs of the BXGY exclude products to remove. <br> Max count: 100. |
| └└ benefit_product_ids | []String | ["456789"] | TikTokShop product ID list. |
| └ product_remove_list | Object |  | Products removed from the activity. |
| └└ product_ids | []String | ["111222","333444"] | Removed product IDs. |
| └└ sku_ids | []String | ["111","222"] | Removed SKU IDs. |
| └└ benefit_product_ids | []String | ["555666"] | TikTokShop product ID list. |
| └└ exclude_product_ids | []String | ["345678"] | IDs of the BXGY exclude products to remove. <br> Max count: 100. |

## Event example
```JSON
{
  "type": 63,
  "timestamp": 1678886400,
  "shop_id": "789123456789123456",
  "tts_notification_id": "000000000000000001",
  "data": {
    "activity_id": "act_123456789012345678",
    "update_time": 1678886400,
    "change_type": "product_update",
    "product_update_list": {
      "product_ids": [
        "11111111",
        "22222222"
      ],
      "exclude_product_ids": [
        "33333333"
      ],
      "benefit_product_ids": [
        "44444444"
      ]
    },
    "product_remove_list": {
      "product_ids": [
        "55555555"
      ],
      "sku_ids": [
        "66666666"
      ],
      "benefit_product_ids": [],
      "exclude_product_ids": []
    }
  }
}
```