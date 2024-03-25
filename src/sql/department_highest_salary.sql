-- Write your MySQL query statement below
SELECT dept.name AS Department , emp.name AS Employee , emp.salary AS Salary
FROM  employee AS emp
INNER JOIN department AS dept
ON emp.departmentId = dept.id
WHERE (emp.departmentId , emp.salary) IN
(SELECT departmentId AS dept_id , MAX(salary) AS Salary
FROM employee GROUP BY departmentId);