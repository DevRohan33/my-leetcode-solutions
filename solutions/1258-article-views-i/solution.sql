# Write your MySQL query statement below
SELECT DISTINCT author_id as id
FROM Views
where viewer_id = author_id
order by id ;


