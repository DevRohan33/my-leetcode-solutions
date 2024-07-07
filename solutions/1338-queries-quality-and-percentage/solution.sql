# Write your MySQL query statement below
WITH Quality_CTE AS (
    SELECT 
        query_name,
        AVG(rating / position) AS quality
    FROM Queries
    GROUP BY query_name
),
Poor_Query_Percentage_CTE AS (
    SELECT 
        query_name,
        100.0 * SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) / COUNT(*) AS poor_query_percentage
    FROM Queries
    GROUP BY query_name
)
SELECT 
    q.query_name,
    ROUND(q.quality, 2) AS quality,
    ROUND(p.poor_query_percentage, 2) AS poor_query_percentage
FROM Quality_CTE q
JOIN Poor_Query_Percentage_CTE p
ON q.query_name = p.query_name;


