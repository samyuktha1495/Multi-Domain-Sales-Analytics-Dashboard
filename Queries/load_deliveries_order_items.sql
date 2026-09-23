BULK INSERT deliveries_order_items_table
FROM 'C:\Users\ADMIN\OneDrive\Documents\DA 2\cleandata\olist_order_items_final.csv'
WITH (
    FIRSTROW = 2,              -- skip header
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    TABLOCK
);

SELECT TOP 10 *
FROM deliveries_order_items_table;

