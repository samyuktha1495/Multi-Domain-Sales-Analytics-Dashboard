-- Compare sales performance with and without discounts
SELECT
    product_id,
    SUM(CASE WHEN discount_flag = 1 THEN total_quantity_sold ELSE 0 END) AS discounted_quantity,
    SUM(CASE WHEN discount_flag = 0 THEN total_quantity_sold ELSE 0 END) AS nondiscounted_quantity,
    SUM(CASE WHEN discount_flag = 1 THEN total_sales_amount ELSE 0 END) AS discounted_sales,
    SUM(CASE WHEN discount_flag = 0 THEN total_sales_amount ELSE 0 END) AS nondiscounted_sales
FROM vw_discount_effectiveness
GROUP BY product_id;

-- Products where discounted sales underperform
SELECT
    product_id,
    total_quantity_sold,
    total_sales_amount
FROM vw_discount_effectiveness
WHERE discount_flag = 1
ORDER BY total_sales_amount ASC;
