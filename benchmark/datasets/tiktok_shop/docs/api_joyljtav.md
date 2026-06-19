# Analytics Open API Metric Consistency Adjustment Announcement

*Source: https://partner.tiktokshop.com/docv2/page/joyljtav*

---

### 1. Overview & Background
To provide developers and merchants with a more consistent and accurate data experience, we will soon be adjusting the metric attribution for select Analytics Open APIs. This upgrade is designed to harmonize data definitions across different analytics products and help our partners more accurately measure business performance.
### 2. Summary of Changes
To ensure a smooth transition, we will be introducing a **new API version** while making backward-compatible adjustments to the **current API version**.

* **Current API Version**:
   * **Data Source Update**: The data source for relevant metrics will be updated to a new, unified attribution model to align with other platform products, such as the Seller Center.
   * **No Structural Changes**: API response field names and data structures will remain unchanged to minimize impact on existing applications.
   * **Description Updates**: We will update the descriptions for all affected fields in the developer documentation to reflect the new attribution logic.
* **New API Version**:
   * **Comprehensive Upgrade**: The new API version will feature updated data sources, field names, and descriptions to provide clearer and more valuable business metrics.
   * **Optional Migration**: We encourage partners to evaluate the benefits of the new API version and plan their migration according to their own business needs and development cycles.
* **Data Behavior Note**:
   * Both API versions will return concrete numeric values. Due to the unified attribution logic, minor differences may be observed for the same metric between the old and new data sources. This is expected behavior, and the data returned by the API should be considered final.

### 3. Impact & Actions for ISVs
This adjustment offers partners greater flexibility:

* **No Mandatory Migration**: If you wish to maintain your current integration, the backward-compatible changes to the current API version will ensure your application continues to function correctly. You only need to be aware of the updated metric descriptions in the developer documentation.
* **Evaluate the New Version**: The new API version provides more accurate and comprehensive attribution metrics, which can help you build more powerful data analytics applications. We recommend reviewing the "Expected Changes" below to assess the value of the new API for your business and plan your adoption accordingly.

### 4. Expected Changes
<span style="background-color: rgba(255,246,122, 0.8)">The following table outlines the expected changes to help you prepare. The final scope of API changes (including additions or removals) and field descriptions are </span><span style="background-color: rgba(255,246,122, 0.8)"><strong>subject to the official release</strong></span><span style="background-color: rgba(255,246,122, 0.8)"> and will be detailed in the developer documentation.</span>

| **API** | **Current Version API: Fields with Updated Data Source (New Attribution)** | **New Version API Metrics** |
| --- | --- | --- |
| Get Video Performance | gmv, order_count, item_sold_count | Attributed GMV, Attributed order count, Attributed items sold count |
| Get Shop LIVE Performance Per Minutes | **Overall**: gmv, items_sold <br> **Intervals**: gmv, items_sold, sku_orders, main_orders, customers, avg_price, click_to_order_rate, gpm, created_sku_orders, sku_order_rate | **Overall**: Attributed GMV, Attributed items sold <br> **Intervals**: Attributed GMV, Attributed items sold, Attributed SKU orders, Attributed main orders, Attributed avg. price, Attributed SKU order CTOR, Attributed main order CTOR, Watch attributed GPM, Show attributed GPM |
| Get shop LIVE products performance list | direct_gmv, items_sold, created_sku_orders, avg_price, sku_orders, main_orders, payment_rate, add_to_cart_count, sku_order_ctor, main_order_ctor, watch_gpm | Attributed GMV, Attributed items sold, Attributed created SKU orders, Attributed SKU orders, Attributed main orders |
| Get Shop Product Performance Detail | top_contents.contents.items_sold, top_contents.contents.gmv, top_creators.gmv, top_creators.items_sold | Top content - attributed items sold, Top content - attributed GMV, Top creators - attributed GMV, Top creators - attributed items sold |
| Get Shop SKU Performance | gmv, gmv_breakdown, items_sold, items_sold_breakdown | Attributed GMV breakdown, Attributed items sold breakdown |
| Get Shop Video Performance List | gmv, gpm, sku_orders, items_sold, avg_customers | Attributed GMV, Attributed GPM, Attributed SKU orders, Attributed items sold, Attributed avg. customers |
| Get Shop Video Performance Overview | gmv, sku_orders, avg_customers | Attributed GMV, Attributed SKU orders, Attributed avg. customers |
| Get Shop Video Performance Details | **Overall**: gmv, gpm, items_sold, customers <br> **Breakdowns**: gmv, gpm, items_sold, customers | Attributed GMV, Attributed GPM, Attributed items sold, Attributed customers |
| Get Shop Video Product Performance List | gmv, units_sold, daily_avg_buyers | Attributed GMV, Attributed units sold, Attributed daily avg. buyers |
| Get Shop LIVE Performance List | gmv, products_added, different_products_sold, created_sku_orders, sku_orders, items_sold, customers, avg_price, click_to_order_rate, 24h_live_gmv | Attributed GMV, Attributed products added, Attributed different products sold, Attributed created SKU orders, Attributed SKU orders, Attributed items sold, Attributed customers, Attributed 24h live GMV |
| Get Shop LIVE Performance Overview | gmv, sku_orders, customers, items_sold, click_to_order_rate | Attributed GMV, Attributed SKU orders, Attributed customers, Attributed items sold |

<span style="background-color: rgba(255,246,122, 0.8)"><strong>Disclaimer</strong></span><span style="background-color: rgba(255,246,122, 0.8)">: The list above is for planning purposes only and may be subject to change. Please refer to the official developer documentation at the time of release for the final and definitive list of APIs and fields.</span>
### 5. Timeline & Key Statements

* **Expected Launch Date**: We expect to complete this rollout by the **end of March 2026**. Any changes to this timeline will be communicated through the developer portal.
* **Final Consistency Statement**: All API changes are **subject to the final released version** and will be consistent with the data attribution models used in official products like the Seller Center.

Thank you for your understanding and support.