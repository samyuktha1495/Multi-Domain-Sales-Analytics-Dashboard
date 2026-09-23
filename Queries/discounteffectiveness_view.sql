CREATE VIEW vw_discount_effectiveness AS
SELECT
    product_id,
    discount_flag,
    COUNT(*) AS total_orders,
    SUM(quantity) AS total_quantity_sold,
    SUM(sales_amount) AS total_sales_amount,
    AVG(sales_amount) AS avg_order_value
FROM discounts_table
GROUP BY product_id, discount_flag;

SELECT TOP 100* FROM vw_discount_effectiveness