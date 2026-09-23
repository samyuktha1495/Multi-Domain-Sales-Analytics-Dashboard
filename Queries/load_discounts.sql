BULK INSERT discounts_table
FROM 'C:\Users\ADMIN\OneDrive\Documents\DA 2\cleandata\amazon_sale_pricing_final.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    ROWTERMINATOR = '0x0a'
);

SELECT COUNT(*) FROM discounts_table;
SELECT TOP 10 * FROM discounts_table;
