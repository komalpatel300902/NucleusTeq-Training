SELECT p.project_id  AS project_id, ROUND(AVG(e.experience_years),2) AS average_years
FROM project AS p , employee AS e
WHERE p.employee_id = e.employee_id
GROUP BY p.project_id 
;