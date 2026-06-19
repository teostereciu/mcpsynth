# (56) Sample Application Status Change

*Source: https://partner.tiktokshop.com/docv2/page/urzvzank*

---

## Trigger scenario
This webhook will trigger when the creator's sample application status changes.
## Data business parameters
| **Parameter name** | **Data Type** | **Sample** | **Description** |
| --- | --- | --- | --- |
| type | int | `56` | The ID of the webhook type. |
| tts_notification_id | string | `"7327112393057371910"` | The ID of the notification. |
| shop_id | string | `"7494049642642441621"` | TikTok shop ID |
| timestamp | int | `1644412885` | The UNIX timestamp when this webhook was triggered. |
| data | object |  |  |
| └application_id | string | `"123456"` | The id of the sample application |
| └new_status | string | `"PENDING"` | The status of sample applications. <br> The possible enumerated values are: <br>  <br> * `PENDING`: The sample application is waiting for the seller's review. <br> * `AWAITING_SHIPMENT`: The application is approved, and the seller needs to ship the sample. <br> * `SHIPPED`: The sample has been shipped by the seller and is waiting for the creator to receive the package. <br> * `CONTENT_PENDING`: The creator has received the sample package and is expected to create content. <br> * `REJECT_CANCELLED`: The sample application has been rejected by the seller. <br> * `OVERDUE_CANCELLED`: The sample application has expired due to being overdue. <br> * `UNFULFILL_CANCELLED`: The creator did not fulfill the commitment to create content within the agreed timeframe. <br> * `DEL_OPEN_COLLAB`: Open collaboration has been deleted. <br> * `SELLER_NOT_SHIP_CANCELLED`: The seller did not ship the sample within the required timeframe. <br> * `WITHDRAW_CANCELLED`: The creator withdrew the sample application before the seller approved it. <br> * `UNFULFILLABLE_CANCELLED`: The application was cancelled due to reasons beyond the creator's control, making it impossible to create content. <br> * `OPS_CANCELLED`: The application was manually cancelled by operations staff. <br> * `OPS_FAILED`: The application was marked as failed by operations staff. <br> * `OPS_COMPLETED`: The application was manually marked as completed by operations staff. <br> * `COMPLETED`: The application is complete, and the creator has posted the content. <br>  <br> This field allows for tracking the status of a sample application throughout its lifecycle, providing visibility into each stage of the process for sellers and creators. |
| └creator | []object |  | Creator detailed information. It includes various details such as the creator's TikTok user name and TikTok user id. |
| └└creator_open_id | string | `"uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg"` | Creator Open ID. [More details](https://partner.tiktokshop.com/docv2/page/3obfokj6) |
| └product | []object |  | Product information. |
| └└id | string | `"1729859829942358814"` | The product identifier. |
| └└sku_id | string | `"1729859567502267166"` | The unique id of product sku which the creator applied for as a sample. |
## Event example
```JSON
{
  "type": 56,
  "shop_id": "7494049642642441621",
  "tts_notification_id": "7327112393057371910",
  "timestamp": 1644412885,
  "data": {
    "application_id": "123456",
    "new_status": "PENDING",
    "creator": {
      "creator_open_id": "uACafQAAAABmUU2qon4R0vUYvUVS3QC6CICP2m5A2-wd77j8R9G0yg"
    },
    "product": {
      "id": "1729859829942358814",
      "sku_id": "1729859567502267166"
    }
  }
}
```