# Write your MySQL query statement below
DELETE p
FROM Person p
JOIN (
  SELECT email, MIN(id) as min_id
  FROM Person
  GROUP BY email
) m ON p.email = m.email AND p.id > m.min_id;
