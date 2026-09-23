CREATE VIEW vw_suspicious_reviews AS
SELECT
    reviewer_id,
    country,
    COUNT(*) AS total_reviews,
    COUNT(DISTINCT rating) AS rating_variety,
    MIN(rating) AS min_rating,
    MAX(rating) AS max_rating
FROM reviews_table
GROUP BY reviewer_id, country;

SELECT TOP 1000* FROM vw_suspicious_reviews