BULK INSERT returns_table
FROM 'C:\Users\ADMIN\OneDrive\Documents\DA 2\cleandata\online_retail_final.csv'
WITH (
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);

SELECT COUNT(*) FROM returns_table;
SELECT TOP 5 * FROM returns_table;
