-- # Write your MySQL query statement below
SELECT `firstName` , `lastName` , `city` , `state` 
FROM `person` AS p
LEFT JOIN `address` AS a
ON p.personid = a.personid;