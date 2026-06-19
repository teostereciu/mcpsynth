from mcp.server.fastmcp import FastMCP

from generated_tools.billing import (
    create_coupon,
    create_invoice,
    create_invoice_preview,
    create_promotion_code,
    create_subscription,
    retrieve_coupon,
    retrieve_invoice,
    retrieve_promotion_code,
    retrieve_subscription,
    update_coupon,
    update_invoice,
    update_promotion_code,
    update_subscription,
)
from generated_tools.catalog import (
    create_price,
    create_product,
    retrieve_price,
    retrieve_product,
    update_price,
    update_product,
)
from generated_tools.checkout import (
    create_checkout_session,
    create_payment_link,
    list_payment_link_line_items,
    retrieve_checkout_session,
    update_checkout_session,
    update_payment_link,
)
from generated_tools.connect import (
    create_account,
    create_transfer,
    retrieve_account,
    retrieve_transfer,
    update_account,
    update_transfer,
)
from generated_tools.customers import create_customer, retrieve_customer, update_customer
from generated_tools.payments import (
    create_charge,
    create_payment_intent,
    create_payout,
    create_refund,
    create_setup_intent,
    retrieve_charge,
    retrieve_payment_intent,
    retrieve_payout,
    retrieve_refund,
    retrieve_setup_intent,
    update_charge,
    update_payment_intent,
    update_payout,
    update_refund,
    update_setup_intent,
)

mcp = FastMCP("stripe")

for fn in [
    create_payment_intent,
    update_payment_intent,
    retrieve_payment_intent,
    create_charge,
    update_charge,
    retrieve_charge,
    create_refund,
    update_refund,
    retrieve_refund,
    create_payout,
    update_payout,
    retrieve_payout,
    create_setup_intent,
    update_setup_intent,
    retrieve_setup_intent,
    create_customer,
    update_customer,
    retrieve_customer,
    create_product,
    update_product,
    retrieve_product,
    create_price,
    update_price,
    retrieve_price,
    create_subscription,
    update_subscription,
    retrieve_subscription,
    create_invoice_preview,
    create_invoice,
    update_invoice,
    retrieve_invoice,
    create_coupon,
    update_coupon,
    retrieve_coupon,
    create_promotion_code,
    update_promotion_code,
    retrieve_promotion_code,
    create_checkout_session,
    update_checkout_session,
    retrieve_checkout_session,
    create_payment_link,
    update_payment_link,
    list_payment_link_line_items,
    create_account,
    update_account,
    retrieve_account,
    create_transfer,
    update_transfer,
    retrieve_transfer,
]:
    mcp.tool()(fn)


if __name__ == "__main__":
    mcp.run()
