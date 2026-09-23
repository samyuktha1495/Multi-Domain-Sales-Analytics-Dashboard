BULK INSERT reviews_table
FROM 'C:\Users\ADMIN\OneDrive\Documents\DA 2\cleandata\amazon_reviews_final.csv'
WITH (
    FORMAT = 'CSV',
    FIRSTROW = 2,
    FIELDQUOTE = '"',
    CODEPAGE = '65001',   
    ROWTERMINATOR = '0x0a'
);


SELECT COUNT(*) FROM reviews_table;
SELECT TOP 5 * FROM reviews_table;
