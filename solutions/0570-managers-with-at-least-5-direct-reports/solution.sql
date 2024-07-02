# Write your MySQL query statement belo
SELECT 
    e1.name
FROM 
    Employee e1
JOIN 
    (SELECT 
         managerId, COUNT(*) AS report_count
     FROM 
         Employee
     WHERE 
         managerId IS NOT NULL
     GROUP BY 
         managerId
     HAVING 
         COUNT(*) >= 5) e2
ON 
    e1.id = e2.managerId;


