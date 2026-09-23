-- Reviewers with many reviews but no rating diversity
SELECT
    reviewer_id,
    country,
    total_reviews,
    rating_variety,
    min_rating,
    max_rating
FROM vw_suspicious_reviews
WHERE rating_variety = 1
  AND total_reviews >= 5
ORDER BY total_reviews DESC;

-- Geographic clustering of suspicious reviewers
SELECT
    country,
    COUNT(*) AS suspicious_reviewer_count
FROM vw_suspicious_reviews
WHERE rating_variety = 1
GROUP BY country
ORDER BY suspicious_reviewer_count DESC;
