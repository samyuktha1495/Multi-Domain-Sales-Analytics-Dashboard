USE DA2_PROJECT;
GO

ALTER VIEW vw_late_deliveries AS
SELECT
    o.order_id,
    o.customer_id,
    c.customer_city,
    c.customer_state,

    oi.seller_id,
    s.seller_city,
    s.seller_state,

    o.purchase_date,
    o.delivered_date,
    o.estimated_delivery_date,

    DATEDIFF(
        DAY,
        o.estimated_delivery_date,
        o.delivered_date
    ) AS delay_days,

    CASE
        WHEN o.delivered_date > o.estimated_delivery_date THEN 1
        ELSE 0
    END AS is_late

FROM deliveries_orders_table o
JOIN deliveries_customers_table c
    ON o.customer_id = c.customer_id
JOIN deliveries_order_items_table oi
    ON o.order_id = oi.order_id
JOIN deliveries_sellers_table s
    ON oi.seller_id = s.seller_id
WHERE o.delivered_date IS NOT NULL;


