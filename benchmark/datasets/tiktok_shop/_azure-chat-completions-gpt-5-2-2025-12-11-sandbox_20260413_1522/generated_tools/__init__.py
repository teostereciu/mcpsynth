from __future__ import annotations

from fastmcp import FastMCP

from . import analytics, customer_service, finance, fulfillment, orders, products, promotions, returns, seller

mcp = FastMCP("tiktok-shop")


# Seller
@mcp.tool()
def seller_get_authorized_shops():
    return seller.get_authorized_shops()


@mcp.tool()
def seller_get_seller_permissions(shop_cipher: str | None = None):
    return seller.get_seller_permissions(shop_cipher=shop_cipher)


# Products
@mcp.tool()
def products_get_categories(
    locale: str | None = None,
    keyword: str | None = None,
    category_version: str | None = None,
    listing_platform: str | None = None,
    include_prohibited_categories: bool | None = None,
    shop_cipher: str | None = None,
):
    return products.get_categories(
        locale=locale,
        keyword=keyword,
        category_version=category_version,
        listing_platform=listing_platform,
        include_prohibited_categories=include_prohibited_categories,
        shop_cipher=shop_cipher,
    )


@mcp.tool()
def products_create_product(product: dict, shop_cipher: str | None = None):
    return products.create_product(product, shop_cipher=shop_cipher)


@mcp.tool()
def products_search_products(
    keyword: str | None = None,
    status: str | None = None,
    page_size: int = 20,
    page_token: str | None = None,
    shop_cipher: str | None = None,
):
    return products.search_products(
        keyword=keyword,
        status=status,
        page_size=page_size,
        page_token=page_token,
        shop_cipher=shop_cipher,
    )


@mcp.tool()
def products_get_product(product_id: str, shop_cipher: str | None = None):
    return products.get_product(product_id, shop_cipher=shop_cipher)


@mcp.tool()
def products_update_inventory(
    product_id: str,
    sku_id: str,
    quantity: int,
    warehouse_id: str | None = None,
    shop_cipher: str | None = None,
):
    return products.update_inventory(
        product_id=product_id,
        sku_id=sku_id,
        quantity=quantity,
        warehouse_id=warehouse_id,
        shop_cipher=shop_cipher,
    )


@mcp.tool()
def products_update_price(
    product_id: str,
    sku_id: str,
    price: float,
    currency: str = "USD",
    shop_cipher: str | None = None,
):
    return products.update_price(
        product_id=product_id,
        sku_id=sku_id,
        price=price,
        currency=currency,
        shop_cipher=shop_cipher,
    )


# Orders
@mcp.tool()
def orders_search_orders(
    order_status: str | None = None,
    page_size: int = 20,
    page_token: str | None = None,
    sort_field: str = "create_time",
    sort_order: str = "DESC",
    shop_cipher: str | None = None,
):
    return orders.search_orders(
        order_status=order_status,
        page_size=page_size,
        page_token=page_token,
        sort_field=sort_field,
        sort_order=sort_order,
        shop_cipher=shop_cipher,
    )


@mcp.tool()
def orders_get_order_detail(order_id: str, shop_cipher: str | None = None):
    return orders.get_order_detail(order_id, shop_cipher=shop_cipher)


# Fulfillment
@mcp.tool()
def fulfillment_search_packages(
    package_status: str | None = None,
    page_size: int = 20,
    page_token: str | None = None,
    sort_field: str = "create_time",
    sort_order: str = "DESC",
    shop_cipher: str | None = None,
):
    return fulfillment.search_packages(
        package_status=package_status,
        page_size=page_size,
        page_token=page_token,
        sort_field=sort_field,
        sort_order=sort_order,
        shop_cipher=shop_cipher,
    )


@mcp.tool()
def fulfillment_ship_package(package_id: str, handover_method: str = "DROP_OFF", shop_cipher: str | None = None):
    return fulfillment.ship_package(package_id, handover_method=handover_method, shop_cipher=shop_cipher)


@mcp.tool()
def fulfillment_get_package_shipping_document(
    package_id: str,
    document_type: str = "SHIPPING_LABEL",
    shop_cipher: str | None = None,
):
    return fulfillment.get_package_shipping_document(package_id, document_type=document_type, shop_cipher=shop_cipher)


@mcp.tool()
def fulfillment_get_warehouse_list(shop_cipher: str | None = None):
    return fulfillment.get_warehouse_list(shop_cipher=shop_cipher)


# Promotions
@mcp.tool()
def promotions_create_activity(activity: dict, shop_cipher: str | None = None):
    return promotions.create_activity(activity, shop_cipher=shop_cipher)


# Finance
@mcp.tool()
def finance_get_payments(
    sort_field: str = "create_time",
    sort_order: str = "DESC",
    page_size: int = 20,
    page_token: str | None = None,
    shop_cipher: str | None = None,
):
    return finance.get_payments(
        sort_field=sort_field,
        sort_order=sort_order,
        page_size=page_size,
        page_token=page_token,
        shop_cipher=shop_cipher,
    )


@mcp.tool()
def finance_get_statements(page_size: int = 10, page_token: str | None = None, shop_cipher: str | None = None):
    return finance.get_statements(page_size=page_size, page_token=page_token, shop_cipher=shop_cipher)


# Analytics
@mcp.tool()
def analytics_get_shop_performance_last_7_days(shop_cipher: str | None = None):
    return analytics.get_shop_performance_last_7_days(shop_cipher=shop_cipher)


# Returns/Refunds/Cancellations
@mcp.tool()
def returns_search_returns(
    return_status: list[str] | None = None,
    page_size: int = 10,
    page_token: str | None = None,
    shop_cipher: str | None = None,
):
    return returns.search_returns(
        return_status=return_status,
        page_size=page_size,
        page_token=page_token,
        shop_cipher=shop_cipher,
    )


@mcp.tool()
def returns_search_cancellations(status: str | None = None, page_size: int = 10, page_token: str | None = None, shop_cipher: str | None = None):
    return returns.search_cancellations(status=status, page_size=page_size, page_token=page_token, shop_cipher=shop_cipher)


# Customer service
@mcp.tool()
def customer_service_get_conversations(page_size: int = 10, page_token: str | None = None, shop_cipher: str | None = None):
    return customer_service.get_conversations(page_size=page_size, page_token=page_token, shop_cipher=shop_cipher)


@mcp.tool()
def customer_service_send_message(conversation_id: str, message: str, shop_cipher: str | None = None):
    return customer_service.send_message(conversation_id=conversation_id, message=message, shop_cipher=shop_cipher)
