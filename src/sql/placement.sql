/*
Enter your query here.
*/
WITH emp AS
(SELECT s.id AS id , s.name AS name , f.friend_id AS friend_id ,p.salary AS salary
 FROM students AS s
 INNER JOIN friends AS f
 ON s.id = f.id
 INNER JOIN packages AS p
 ON f.id = p.id
 )
 SELECT e.name AS name
 FROM emp AS e
 INNER JOIN packages AS p
 ON e.friend_id = p.id
WHERE e.salary < p.salary
  ORDER BY p.salary ;