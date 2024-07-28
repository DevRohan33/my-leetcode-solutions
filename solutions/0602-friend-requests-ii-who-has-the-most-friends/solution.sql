# Write your MySQL query statement below
WITH FriendCount AS (
    SELECT requester_id AS id
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id
    FROM RequestAccepted
),
FriendSummary AS (
    SELECT id, COUNT(*) AS num
    FROM FriendCount
    GROUP BY id
)
SELECT id, num
FROM FriendSummary
ORDER BY num DESC
LIMIT 1;


