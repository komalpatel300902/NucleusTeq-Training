-- Write your MySQL query statement below
--  STEP 1 FETCH REGISTER OF USER PRESENT IN USERS
--  STEP 2 GROUP BY CONTEST_ID -> R.COUNT(UUER_ID)*100/U.USER_ID 
WITH al AS (
    SELECT r.contest_id AS contest_id, r.user_id AS user_id 
    FROM register AS r
    WHERE r.user_id = ANY (SELECT user_id FROM users)
)
SELECT a.contest_id , ROUND(100*COUNT(a.user_id)/(SELECT COUNT(user_id) FROM users),2) AS percentage
FROM al AS a
GROUP BY a.contest_id 
ORDER BY percentage DESC ,contest_id ASC;