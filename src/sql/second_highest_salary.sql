# Write your MySQL query statement below
WITH tbl AS
(
SELECT salary AS salary,
DENSE_RANK() OVER (ORDER BY salary DESC) AS sal_rank
FROM employee
)
SELECT 
CASE
    WHEN COUNT(tbl2.salary) = 0 THEN NULL
    ELSE tbl2.salary
END AS SecondHighestSalary
FROM
    (SELECT tbl.salary AS salary
    FROM tbl
    WHERE tbl.sal_rank = 2
    GROUP BY  tbl.sal_rank) AS tbl2
;