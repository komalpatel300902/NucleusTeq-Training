# Write your MySQL query statement below
SELECT e1.employee_id , e1.name , COUNT(e2.reports_to) AS reports_count , ROUND(AVG(e2.age)) AS average_age
FROM employees e1, employees e2
WHERE e1.employee_id = e2.reports_to
GROUP BY e1.employee_id
ORDER BY e1.employee_id ASC;