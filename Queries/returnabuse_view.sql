CREATE VIEW vw_returns_abuse AS
SELECT
    customer_id,
    country,
    COUNT(*) AS total_return_transactions,
    SUM(ABS(quantity)) AS total_items_returned,
    SUM(ABS(quantity * unit_price)) AS total_return_value,
    MIN(invoice_date) AS first_return_date,
    MAX(invoice_date) AS last_return_date
FROM returns_table
WHERE quantity < 0
GROUP BY customer_id, country;

SELECT TOP 100* FROM vw_returns_abuse