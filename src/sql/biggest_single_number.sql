# Write your MySQL query statement below
WITH a AS(
    SELECT num 
    FROM(
        SELECT num , 1 AS n 
        FROM mynumbers
    ) AS mnumber
    GROUP BY num
    HAVING COUNT(n) = 1
)
SELECT MAX(a.num)  AS num
FROM a;