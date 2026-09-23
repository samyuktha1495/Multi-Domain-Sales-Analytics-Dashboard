BULK INSERT deliveries_customers_table
FROM 'C:\Users\ADMIN\OneDrive\Documents\DA 2\cleandata\olist_customers_final.csv'
WITH (
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a'
);

SELECT COUNT(*) FROM deliveries_customers_table;
SELECT TOP 5 * FROM deliveries_customers_table;
