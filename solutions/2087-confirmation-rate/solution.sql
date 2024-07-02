# Write your MySQL query statement below
WITH ConfirmationsSummary AS (
    SELECT 
        user_id,
        COUNT(*) AS total_requests,
        SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END) AS confirmed_requests
    FROM 
        Confirmations
    GROUP BY 
        user_id
)

SELECT 
    s.user_id,
    ROUND(COALESCE(cs.confirmed_requests, 0) / COALESCE(cs.total_requests, 1), 2) AS confirmation_rate
FROM 
    Signups s
LEFT JOIN 
    ConfirmationsSummary cs
ON 
    s.user_id = cs.user_id
ORDER BY 
    s.user_id;


