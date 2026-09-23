BULK INSERT deliveries_orders_table
FROM 'C:\Users\ADMIN\OneDrive\Documents\DA 2\cleandata\olist_orders_final.csv'
WITH (
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a'
);

SELECT COUNT(*) FROM deliveries_orders_table;
SELECT TOP 5 * FROM deliveries_orders_table;
