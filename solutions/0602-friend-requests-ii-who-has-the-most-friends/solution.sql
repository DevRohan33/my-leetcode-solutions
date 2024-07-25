# Write your MySQL query statement below
WITH FriendCounts AS (
    SELECT requester_id AS person_id, COUNT(DISTINCT accepter_id) AS friend_count
    FROM RequestAccepted
    GROUP BY requester_id
    UNION ALL
    SELECT accepter_id AS person_id, COUNT(DISTINCT requester_id) AS friend_count
    FROM RequestAccepted
    GROUP BY accepter_id
),
AggregatedCounts AS (
    SELECT person_id, SUM(friend_count) AS total_friends
    FROM FriendCounts
    GROUP BY person_id
)
SELECT person_id AS id, total_friends AS num
FROM AggregatedCounts
ORDER BY total_friends DESC
LIMIT 1;


