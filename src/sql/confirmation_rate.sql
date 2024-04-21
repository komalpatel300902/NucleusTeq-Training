# Write your MySQL query statement below
-- STEP 2: CREATE TABLE : ALL ID : ACTION = COUNT(CONFIRMED)
-- STEP 1: CREATE TABLE : ALL ID : ACTION = COUNT(CONFIRMED,TIMEOUT)
WITH a AS(
    SELECT s.user_id , COUNT(c.action) AS action
    FROM signups AS s
    LEFT JOIN confirmations AS c
    ON s.user_id = c.user_id
    GROUP BY s.user_id
), b AS (
    SELECT s.user_id , COUNT(t.action) AS action
    FROM signups AS s
    LEFT JOIN (
        SELECT user_id , action 
        FROM confirmations 
        WHERE action = "confirmed"
    ) AS t
    ON s.user_id = t.user_id
    GROUP BY s.user_id
)
SELECT a.user_id,
CASE 
    WHEN a.action = 0 THEN ROUND(0,2)
    ELSE ROUND((b.action/a.action),2)
END AS confirmation_rate
FROM a
INNER JOIN b
ON a.user_id = b.user_id
;