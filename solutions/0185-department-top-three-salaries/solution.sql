# Write your MySQL query statement below
WITH TopSalaries AS (
    SELECT
        e.departmentId,
        e.salary,
        DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) as salary_rank
    FROM
        Employee e
    GROUP BY
        e.departmentId, e.salary
),
HighEarners AS (
    SELECT
        t.departmentId,
        e.name,
        e.salary
    FROM
        TopSalaries t
        JOIN Employee e ON t.departmentId = e.departmentId AND t.salary = e.salary
    WHERE
        t.salary_rank <= 3
)
SELECT
    d.name AS Department,
    h.name AS Employee,
    h.salary AS Salary
FROM
    HighEarners h
    JOIN Department d ON h.departmentId = d.id
ORDER BY
    Department, Salary DESC, Employee;

