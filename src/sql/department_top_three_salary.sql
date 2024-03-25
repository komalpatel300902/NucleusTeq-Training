-- Write your MySQL query statement below
SELECT tbl.dept_name AS Department , tbl.emp_name AS Employee , tbl.salary AS Salary
FROM 
(SELECT dept.name AS dept_name, emp.name AS emp_name , emp.salary AS salary,
DENSE_RANK() OVER (PARTITION BY emp.departmentId ORDER BY emp.salary DESC) AS sal_rank
FROM employee AS emp
INNER JOIN department AS dept
ON emp.departmentId = dept.id) AS tbl
WHERE tbl.sal_rank < 4
ORDER BY tbl.salary DESC;