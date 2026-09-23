-- Identify customers causing the highest financial loss due to returns
SELECT
    customer_id,
    country,
    total_return_transactions,
    total_items_returned,
    total_return_value
FROM vw_returns_abuse
ORDER BY total_return_value DESC;

-- Customers with unusually high return frequency
SELECT
    customer_id,
    country,
    total_return_transactions,
    total_items_returned
FROM vw_returns_abuse
WHERE total_return_transactions >= 10
ORDER BY total_return_transactions DESC;

