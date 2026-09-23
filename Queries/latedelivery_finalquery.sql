USE DA2_PROJECT;
GO

-- Late delivery percentage by state
SELECT
    customer_state,
    COUNT(*) AS total_orders,
    SUM(is_late) AS late_orders,
    CAST(SUM(is_late) * 100.0 / COUNT(*) AS DECIMAL(5,2)) AS late_delivery_percentage
FROM vw_late_deliveries
GROUP BY customer_state
ORDER BY late_delivery_percentage DESC;

-- Cities experiencing the longest delivery delays
SELECT
    customer_city,
    AVG(delay_days) AS avg_delay_days
FROM vw_late_deliveries
WHERE is_late = 1
GROUP BY customer_city
ORDER BY avg_delay_days DESC;

--Sellers Causing the Most Late Deliveries
SELECT
    seller_id,
    seller_state,
    COUNT(*) AS total_orders,
    SUM(is_late) AS late_orders,
    CAST(SUM(is_late) * 100.0 / COUNT(*) AS DECIMAL(5,2)) AS late_delivery_percentage
FROM vw_late_deliveries
GROUP BY seller_id, seller_state
HAVING SUM(is_late) >= 10
ORDER BY late_delivery_percentage DESC;

--Sellers with the Longest Average Delays
SELECT
    seller_id,
    seller_state,
    AVG(delay_days) AS avg_delay_days
FROM vw_late_deliveries
WHERE is_late = 1
GROUP BY seller_id, seller_state
ORDER BY avg_delay_days DESC

