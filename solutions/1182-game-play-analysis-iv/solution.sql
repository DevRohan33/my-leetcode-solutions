# Write your MySQL query statement below
WITH FirstLogin AS (
    SELECT player_id, MIN(event_date) AS first_login_date
    FROM Activity
    GROUP BY player_id
),
NextDayLogin AS (
    SELECT DISTINCT a.player_id
    FROM Activity a
    JOIN FirstLogin fl ON a.player_id = fl.player_id
    WHERE a.event_date = DATE_ADD(fl.first_login_date, INTERVAL 1 DAY)
)
SELECT ROUND(COUNT(DISTINCT ndl.player_id) / COUNT(DISTINCT fl.player_id), 2) AS fraction
FROM FirstLogin fl
LEFT JOIN NextDayLogin ndl ON fl.player_id = ndl.player_id;


